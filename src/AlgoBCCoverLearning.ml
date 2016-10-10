(************************************************************
 *
 *                       IMITATOR
 * 
 * LIPN, Université Paris 13, Sorbonne Paris Cité (France)
 * 
 * Module description: Behavioral Cartography with exhaustive coverage of integer points and learning-based abstraction.
 * 
 * File contributors : Étienne André
 * Created           : 2016/07/22
 * Last modified     : 2016/10/10
 *
 ************************************************************)


(************************************************************)
(************************************************************)
(* Modules *)
(************************************************************)
(************************************************************)
open OCamlUtilities
open ImitatorUtilities
open Exceptions
open AbstractModel
open Result
open AlgoBCCover


(************************************************************)
(************************************************************)
(* Constants related to the interfacing with the learning programs *)
(************************************************************)
(************************************************************)

let interface_script_name = "learning/learninginterface.py"

(* Strings to be present at the first line of the file name generated by the learning-based program *)
let string_ABSTRACTION = "===ABSTRACTION==="
let string_COUNTEREXAMPLE = "===COUNTEREXAMPLE==="


(************************************************************)
(************************************************************)
(* Class-indepdendent types *)
(************************************************************)
(************************************************************)
type learning_result =
	| Abstraction
	| CounterExample

(************************************************************)
(************************************************************)
(* Class definition *)
(************************************************************)
(************************************************************)
class algoBCCoverLearning =
	object (self) inherit algoBCCover as super
	
	(************************************************************)
	(* Class variables *)
	(************************************************************)

	(* Backup the original model (for final postprocessing) *)
	val original_model = Input.get_model ()
	(* Backup the original model file names *)
	val original_file = (Input.get_options ())#model_input_file_name
	val original_files_prefix = (Input.get_options ())#files_prefix
	
	
	
	(************************************************************)
	(* Class methods *)
	(************************************************************)

	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(* Name of the algorithm *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	method algorithm_name = "BC (full coverage with learning-based abstraction)"

	
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(* Safety redefinition *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(*** NOTE: safety redefinition: this cartography algorithm should NOT be parameterized by a method, as the method to be called on each point is statically chosen (it will be either EFsynth or PRP, depending on the abstraction) ***)
	method set_algo_instance_function _ : unit =
		raise (InternalError "Method 'set_algo_instance_function' should NOT be used in BCCoverlearning")

			
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(* Variable initialization *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	method initialize_variables =
		super#initialize_variables;
		
		(* The end *)
		()

	
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(* Call the algorithm on the current point: 1) run the abstraction 2) call either EFsynth or PRP depending on the result *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	method call_point =
		(* Retrieve the input options *)
		let options = Input.get_options () in
		
		(* Retrieve the current point *)
		let current_point = self#get_current_point_option in

		
		(*------------------------------------------------------------*)
		(* 1) Call the python script interfacing with the learning tool *)
		(*------------------------------------------------------------*)
		
		(* Create the file name for the model generated by learning *)
		let learning_based_model_filename_prefix = options#files_prefix ^ "_learning_" ^ (string_of_int current_iteration) in
		let learning_based_model_filename = learning_based_model_filename_prefix ^ "" ^ Constants.model_extension in

		(* Prepare command *)
		let script_line = "python " ^ interface_script_name
			(* 1st argument: input model *)
			^ " " ^ options#model_input_file_name
			(* 2nd argument: output model name *)
			^ " " ^ learning_based_model_filename
			(* 3rd argument: pi0 *)
			^ " \"" ^ (ModelPrinter.string_of_pi0 (Input.get_model ()) current_point) ^ "\""
		 in
		
		(* Call the script *)
		let execution = Sys.command script_line in
		if execution <> 0 then
			raise (InternalError ("Something went wrong in the command.\nExit code: " ^ (string_of_int execution) ^ ".\nCommand: '" ^ script_line ^ "'"););
		
		
		(*------------------------------------------------------------*)
		(* 2) Check that the output file was correctly generated *)
		(*------------------------------------------------------------*)
		
		if not (Sys.file_exists learning_based_model_filename) then(
			print_error ("File '" ^ learning_based_model_filename ^ "' not found!");
			raise (InterfacingError ("The file '" ^ learning_based_model_filename ^ "' that should have been generated by learning could not be found."))
		);
		
		
		(*------------------------------------------------------------*)
		(* 3) Find out whether this is a counter-example or an abstraction *)
		(*------------------------------------------------------------*)
		
		(* Read first line of the file *)
		let first_line = OCamlUtilities.read_first_line_from_file learning_based_model_filename in
		
		(* Remove comments and look for text *)
		let analysis_type = if Str.string_match (Str.regexp (".*(\\*\\(" ^ string_ABSTRACTION ^ "\\)\\*).*")) first_line 0 then Abstraction
			else if Str.string_match (Str.regexp (".*(\\*\\(" ^ string_COUNTEREXAMPLE ^ "\\)\\*).*")) first_line 0 then CounterExample
			else(
				print_error ("First line not recognized: " ^ first_line);
				raise (InterfacingError ("The type of the analysis (that should have been at the first line of the file generated by '" ^ interface_script_name ^ "') could not be recognized"))
			)
		in
		
		(* Print some information *)
		print_message Verbose_standard ("Model generated by learning: " ^ (match analysis_type with | Abstraction -> "abstraction" | CounterExample -> "counter-example"));
		

		(*------------------------------------------------------------*)
		(* 4) Parse and set the new model *)
		(*------------------------------------------------------------*)
		
		(* Set model name and model prefix name (needed before compiling!) *)
		options#set_file learning_based_model_filename;
		options#set_files_prefix learning_based_model_filename_prefix;
		
		(*** TODO: counter ***)
		let new_model = ParsingUtility.compile_model options false in
		(*** TODO: counter ***)
		
		(* Set model *)
		Input.set_model new_model;
		
		(* Print some information *)
		print_message Verbose_standard ("Original model: " ^ (string_of_int original_model.nb_automata) ^ " automata. New model: " ^ (string_of_int new_model.nb_automata) ^ "");
		
		
		(*------------------------------------------------------------*)
		(* 5) Call the proper algorithm *)
		(*------------------------------------------------------------*)
		
		(* Save the verbose mode as it may be modified *)
		let global_verbose_mode = get_verbose_mode() in

		(* Prevent the verbose messages (except in verbose medium, high or total) *)
		(*------------------------------------------------------------*)
		if not (verbose_mode_greater Verbose_medium) then
			set_verbose_mode Verbose_mute;

		(* Select the right algorithm according to the analysis type *)
		let algo_instance = match analysis_type with
			(* If counter-exemple: run EF on the parametric trace *)
			| CounterExample -> let myalgo :> AlgoBFS.algoBFS = new AlgoEFsynth.algoEFsynth in myalgo
			
			(* If abstraction: run PRP on this abstraction *)
			(*** NOTE: the current valuation (current_point) is already set in Input ***)
			| Abstraction -> let myalgo :> AlgoBFS.algoBFS = new AlgoPRP.algoPRP in myalgo
		in
		current_algo_instance <- algo_instance;
		
		(* Run! *)
		let imitator_result : imitator_result = current_algo_instance#run() in

		(* Create auxiliary files with the proper file prefix, if requested *)
		self#create_auxiliary_files imitator_result;

		(* Get the verbose mode back *)
		set_verbose_mode global_verbose_mode;
		(*------------------------------------------------------------*)

		
		(*------------------------------------------------------------*)
		(* 6) Remove the temporary model *)
		(*------------------------------------------------------------*)
		
		(* If option asks to keep the files: keep *)

		(*** TODO (not implemented yet as we need to create files manually for now...) ***)

		
		(* Set model name and model prefix name back to their original value *)
		options#set_file original_file;
		options#set_files_prefix original_files_prefix;

		(*------------------------------------------------------------*)
		(* Return result *)
		(*------------------------------------------------------------*)
		imitator_result
		


(************************************************************)
(************************************************************)
end;;
(************************************************************)
(************************************************************)
