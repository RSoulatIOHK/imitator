(*****************************************************************
 *
 *                       IMITATOR
 *
 * Université Paris 13, LIPN, CNRS, France
 * Université de Lorraine, CNRS, Inria, LORIA, Nancy, France
 *
 * Author:        Étienne André
 *
 * File contributors : Étienne André, Jaime Arias, Laure Petrucci
 * Created           : 2015/03/24
 *
 ****************************************************************)

open OCamlUtilities
open Exceptions
open AbstractModel
open AbstractProperty
open DiscreteExpressions
open Constants




(************************************************************)
(** Constants *)
(************************************************************)

let tikz_boolean_string = { default_string with
    and_operator = " \\land ";
    or_operator = " \\lor ";
    not_operator = "\\neg";
    in_operator = " \\in ";
	le_operator   = "\\leq";
	neq_operator  = "\\neq";
	ge_operator   = "\\geq";
}

let tikz_string = { global_default_string with boolean_string = tikz_boolean_string }

(************************************************************
 Functions
************************************************************)

(** Escape strings for LaTeX names *)
let escape_latex str =
	Str.global_replace (Str.regexp "_") ("\\_") str


let variable_names_with_style variable_index =
	(* Get the model *)
	let model = Input.get_model() in
	let name = escape_latex (model.variable_names variable_index) in
	match model.type_of_variables variable_index with
	| DiscreteType.Var_type_clock -> "\\styleclock{" ^ name ^ "}"
	| DiscreteType.Var_type_discrete _ -> "\\styledisc{" ^ name ^ "}"
	| DiscreteType.Var_type_parameter -> "\\styleparam{" ^ name ^ "}"


(** Proper form for constraints *)
let tikz_string_of_lc_gen lc_fun lc =
	let lc_string = lc_fun variable_names_with_style lc in
	(* Do some replacements *)
	"& $" ^ Str.global_replace (Str.regexp ">=") ("\\geq")
		(Str.global_replace (Str.regexp "&") ("$\\\\\\\\\n\t\t$\\land$ & $")
			(Str.global_replace (Str.regexp "a") ("a") lc_string)
		)
	^ "$"

let tikz_custom_string =
    let tikz_boolean_string = { Constants.default_string with or_operator = " || " } in
    { Constants.global_default_string with boolean_string = tikz_boolean_string }

(** Proper form for constraints *)
let tikz_string_of_linear_constraint =
	tikz_string_of_lc_gen (ModelPrinter.customized_string_of_guard tikz_custom_string)


(** Proper form for constraints *)
let tikz_string_of_guard =
	tikz_string_of_lc_gen (ModelPrinter.customized_string_of_guard tikz_custom_string)



(* Add a header to the model *)
let string_of_header model =
	(* Retrieve the input options *)
	let options = Input.get_options () in
	          "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	^ "\n" ^" % File automatically generated by " ^ Constants.program_name ^ ""
	^ "\n" ^" % Version  : " ^ (ImitatorUtilities.program_name_and_version_and_nickname_and_build)
	^ "\n" ^" % Model    : '" ^ options#model_file_name ^ "'"
	^ "\n" ^" % Generated: " ^ (now()) ^ ""
	^ "\n" ^" % "
	^ "\n" ^" % (node positioning not yet supported, you may need to manually edit the file)"
	^ "\n" ^" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"


(** Convert a sync into a string *)
let string_of_sync model action_index =
	match model.action_types action_index with
	| Action_type_sync -> "\n\t\t & $\\styleact{" ^ (escape_latex (model.action_names action_index)) ^ "}$\\\\"
	| Action_type_nosync -> ""


(** Convert clock updates into a string *)
let string_of_clock_updates model clock_updates =
	let sep = "\\n" in
	let wrap_reset variable_index =  "\n\t\t & $" ^ (variable_names_with_style variable_index) ^ ":=0$\\\\" in
	let wrap_expr variable_index linear_term = "\n\t\t & $"
		^ (variable_names_with_style variable_index)
			^ ":= "
			^ (LinearConstraint.string_of_pxd_linear_term variable_names_with_style linear_term)^"$\\\\% " in
	ModelPrinter.string_of_clock_updates_template model clock_updates wrap_reset wrap_expr sep

(* Convert a list of discrete updates into a string *)
let string_of_discrete_updates model updates =
	string_of_list_of_string_with_sep "\\n" (List.map (fun (parsed_update_type, global_expression) ->
			"\n\t\t & $"
			(* Convert the variable access to string *)
			^ ModelPrinter.string_of_parsed_update_type model parsed_update_type
			^ ":="
			(* Convert the arithmetic_expression *)
			^ ModelPrinter.string_of_global_expression variable_names_with_style global_expression
			(*** HACK!!! without the "%", a strange "\n" that occurs immediately after leads to a LaTeX compiling error when strictly >= 2 updates ***)
			^ "$\\\\% "
	) updates)

(** Convert a list of conditional updates into a string *)
let string_of_conditional_updates model conditional_updates =
	let wrap_if boolean_expr  = "\n\t\t\\multicolumn{2}{l}{if ($" ^ (customized_string_of_boolean_expression tikz_string variable_names_with_style boolean_expr) ^ "$) then}\\\\%" in
	let wrap_else = "\n\t\t\\multicolumn{2}{l}{else}\\\\%" in
	let wrap_end = "\n\t\t\\multicolumn{2}{l}{end}%" in
	let sep = "" in
	ModelPrinter.string_of_conditional_updates_template model conditional_updates string_of_clock_updates string_of_discrete_updates wrap_if wrap_else wrap_end sep

(* Convert a transition of a location into a string *)
let string_of_transition model automaton_index source_location transition =
	let clock_updates = transition.updates.clock in
	let discrete_updates = transition.updates.discrete in
	let conditional_updates = transition.updates.conditional in
	let source_location_name = model.location_names automaton_index source_location in
	let destination_location_name = model.location_names automaton_index transition.target in

	(*	\path (Q0) edge node{\begin{tabular}{c}
			\coulact{press?} \\
			$\coulclock{x} := 0$ \\
			$\coulclock{y} := 0$ \\
			\\end{tabular}} (Q1);*)
	"\n\n\t\t\\path (" ^ source_location_name ^ ") edge node{\\begin{tabular}{@{} c @{\\ } c@{} }"

	(* GUARD *)
	^ (if transition.guard <> AbstractModel.True_guard then (
		"\n\t\t" ^ (tikz_string_of_guard transition.guard) ^ "\\\\"
	) else "" )

	(* ACTION *)
	^ (string_of_sync model transition.action)

	(* UPDATES *)
	(* Clock updates *)
	^ (string_of_clock_updates model clock_updates)
	(* Discrete updates *)
 	^ (string_of_discrete_updates model discrete_updates)
	(* Conditional updates *)
	^ (string_of_conditional_updates model conditional_updates)

	(* The end *)
	^ "\n\t\t\\end{tabular}} (" ^ destination_location_name ^ ");"


(* Convert the transitions of a location into a string *)
let string_of_transitions_per_location model automaton_index location_index =
	string_of_list_of_string (
	(* For each action *)
	List.map (fun action_index ->
		(* Get the list of transitions *)
		let transitions = List.map model.transitions_description (model.transitions automaton_index location_index action_index) in
		(* Convert to string *)
		string_of_list_of_string (
			(* For each transition *)
			List.map (string_of_transition model automaton_index location_index) transitions
			)
		) (model.actions_per_location automaton_index location_index)
	)


(* Convert the transitions of an automaton into a string *)
let string_of_transitions model automaton_index =
	string_of_list_of_string_with_sep "\n " (List.map (fun location_index ->
		string_of_transitions_per_location model automaton_index location_index
	) (model.locations_per_automaton automaton_index))


(* Convert a location of an automaton into a string *)
let string_of_location model automaton_index location_index =
	(* LOCATION *)
(* 	\node[location, fill=cpale2] (Q0) {\coulloc{l0}}; *)

	let inital_global_location  = model.initial_location in
	let initial_location = Location.get_location inital_global_location automaton_index in

	let location_name = model.location_names automaton_index location_index in
	let invariant = model.invariants automaton_index location_index in
	let color_id = ((location_index) mod LatexHeader.nb_colors) + 1 in

	let has_invariant = (
        match invariant with
            | True_guard -> false
            | Continuous_guard continuous_invariant ->
                (* Costly test! But inherent to the invariants structure *)
                not (LinearConstraint.pxd_is_true continuous_invariant)
            | Discrete_continuous_guard discrete_continuous_invariant ->
                (* Costly test! But inherent to the invariants structure *)
                not (LinearConstraint.pxd_is_true discrete_continuous_invariant.continuous_guard)
            (* We assume that an exclusively discrete invariant does not count as an invariant *)
            | _ -> true)
    in
	let has_non_1rate_clocks = model.has_non_1rate_clocks && (model.stopwatches automaton_index location_index <> [] || model.flow automaton_index location_index <> []) in

	(*** TODO: better positioning! (from dot?) ***)
	let pos_x = 0 in
	let pos_y = -location_index in

	(* Handle initial *)
	let initial_str = if location_index = initial_location then "initial, " else "" in
	(* Handle accepting states *)
	let accepting_str = if model.is_accepting automaton_index location_index then "accepting, " else "" in

	(* Handle urgency *)
	let urgent_str = if model.is_urgent automaton_index location_index then "urgent, " else "" in

	
	(*** TODO: if accepting, change the style ***)
	
	"\n\t\t\\node[location, "
	^ initial_str
	^ accepting_str
	^ urgent_str
	^ "fill=loccolor" ^ (string_of_int color_id) ^ "] at (" ^ (string_of_int pos_x) ^ "," ^ (string_of_int pos_y) ^ ") (" ^ location_name ^ ") {\\styleloc{" ^ (if model.is_urgent automaton_index location_index then "U: " else "") ^ (escape_latex location_name) ^ "}};"

	(* INVARIANT AND STOPWATCHES *)
(*			% Invariant of location Q1
		\node [invariant,right] at (Q1.east) {
			\begin{tabular}{c @{\ } c}
				& $\coulclock{y} \leq \coulparam{p1}$\\
				$\\land$ & $\coulclock{x} \geq 5 \couldisc{i}$\\
			\\end{tabular}
		};*)

	^ (if has_invariant || has_non_1rate_clocks then (
		(* Comment *)
		let nature_for_comment =
			match has_invariant, has_non_1rate_clocks with
			| true , true -> "Invariant and non-1 flows"
			| true , false -> "Invariant"
			| false , true -> "Non-1 flows"
			| _ -> raise (InternalError("Here the model must have invariants or non-1 flows"))
		in
		"\n\t\t% " ^ nature_for_comment ^ " of location " ^ location_name
		(* Begin *)
		^ "\n\t\t\\node [invariant,right] at (" ^ location_name ^ ".east) {\\begin{tabular}{@{} c @{\\ } c@{} }"
		(* Invariant *)
		^ (if has_invariant then (tikz_string_of_linear_constraint invariant) ^ "\\\\" else "")
		(* Stopwatches and flows *)
		^ (if has_non_1rate_clocks then (
			(* Stopwatches *)
			let stopwatches = model.stopwatches automaton_index location_index in
			(if stopwatches <> [] then
				(" & stop(" ^ (string_of_list_of_string_with_sep ", " (List.map variable_names_with_style stopwatches)) ^ ")\\\\")
			else "")
			^
			(* Flows *)
			let flows = model.flow automaton_index location_index in
			(if flows <> [] then
				(" & " ^ (string_of_list_of_string_with_sep ", " (List.map (fun (clock_index, constant_flow) -> (variable_names_with_style clock_index) ^ "' = " ^ (NumConst.string_of_numconst constant_flow) ^ "") flows)) ^ "\\\\")
			else "")
			) else "")
		(* The end *)
		^ "\\end{tabular}};"
	) else "")


(* Convert the locations of an automaton into a string *)
let string_of_locations model automaton_index =
	string_of_list_of_string_with_sep "\n " (List.map (fun location_index ->
		string_of_location model automaton_index location_index
	) (model.locations_per_automaton automaton_index))


(* Convert an automaton into a string *)
let string_of_automaton model automaton_index =

	let automaton_name = escape_latex (model.automata_names automaton_index) in

	"\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	^ "\n% automaton " ^ automaton_name ^ ""
	^ "\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

	^ "\n\t\\begin{subfigure}[b]{\\ratio}"
	^ "\n\t\\begin{tikzpicture}[pta, scale=2]" (*, thin*)

	(* Handling locations *)
	^ "\n " ^ (string_of_locations model automaton_index)

	(* Handling transitions *)
	^ "\n " ^ (string_of_transitions model automaton_index)

	^ "\n\t\\end{tikzpicture}"
	^ "\n\t\\caption{PTA " ^ automaton_name ^ "}"
	^ "\n\t\\label{pta:" ^ automaton_name ^ "}"
	^ "\n\t\\end{subfigure}"


(* Convert the automata into a string *)
let string_of_automata model =
	(* Retrieve the input options *)
(*	let options = Input.get_options () in

	let vertical_string_of_list_of_variables variables =
		let variables = List.map model.variable_names variables in
		string_of_list_of_string_with_sep "\\n" variables
	in


	"\n/**************************************************/"
	^ "\n/* Starting general graph */"
	^ "\n/**************************************************/"
	^ "\n digraph G {\n"
	^ "\n node [shape=Mrecord, fontsize=12];"
(* 	^ "\n rankdir=LR" *)
	^ "\n"
	(* General information *)
(* 	s_0[fillcolor=red, style=filled, shape=Mrecord, label="s_0|{InputInit|And111|Or111}"]; *)
^ "\nname[shape=none, style=bold, fontsize=24, label=\"" ^ options#file ^ "\"];"
	^ "\ngeneral_info[shape=record, label=\"" (*Model|{*)
	^ "{Clocks|" ^ (vertical_string_of_list_of_variables model.clocks) ^ "}"
	^ "|{Parameters|" ^ (vertical_string_of_list_of_variables model.parameters) ^ "}"
	^ (if model.discrete <> [] then
		"|{Discrete|" ^ (vertical_string_of_list_of_variables model.discrete) ^ "}"
		else "")
	^ "|{Initial|" ^ (escape_string_for_dot (LinearConstraint.string_of_px_linear_constraint model.variable_names model.initial_constraint)) ^ "}"
	^ "\"];" (*}*)
	(* To ensure that the name is above general info *)
	^ "\n name -> general_info [color=white];"
	^ "\ndate[shape=none, style=bold, fontsize=10, label=\"Generated: " ^ (now()) ^ "\"];"*)

	""
	^ (string_of_list_of_string_with_sep "\n\n" (
		List.map (fun automaton_index -> string_of_automaton model automaton_index
	) model.automata))


(* Convert the model into a string *)
let tikz_string_of_model model =
	let tikz_model =
	(* The small personnalized header *)
	string_of_header model
	(* The big LaTeX header *)
	^ LatexHeader.latex_header
(* 	^  "\n" ^ string_of_declarations model *)
	^  "\n" ^ string_of_automata model
	(* Footer *)
	^ "
\\end{figure}

\\end{document}
"
	in
	(* Replace escaped characters! *)
	(*String.escaped*) (*Scanf.unescaped *)
		tikz_model
(* 	Str.global_replace (Str.regexp_string "\\\n") "(ploufplouf)" tikz_model *)
(* 	Str.global_substitute (Str.regexp_string "command") (fun s -> print_string s; "(ploufplouf)") tikz_model *)
(* 	[^ \\t\\n] *)
