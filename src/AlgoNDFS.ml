(************************************************************
 *
 *                       IMITATOR
 *
 * LIPN, Université Paris 13 (France)
 * Université de Lorraine, CNRS, Inria, LORIA, Nancy, France
 *
 * Module description: NDFS algorithms
 *
 * File contributors : Laure Petrucci, Étienne André
 * Created           : 2019/03/12
 * Last modified     : 2020/08/27
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
open AbstractAlgorithm
open AbstractProperty
open Result
open AlgoStateBased
open State
open Statistics

(************************************************************)
(************************************************************)
(* Types and exceptions for NDFS *)
(************************************************************)
(************************************************************)


exception DFS_Limit_detected of bfs_limit_reached

(************************************************************)
(************************************************************)
(* Class definition *)
(************************************************************)
(************************************************************)
class algoNDFS =
	object (self) inherit algoStateBased as super

	(************************************************************)
	(* Class variables *)
	(************************************************************)
	val mutable constraint_valuations : LinearConstraint.p_nnconvex_constraint option = None
		(* for the evaluation of the synthesis result *)
	val mutable cyclecount = 0 (* counter for the cycles found *)
	val mutable processed_blue = 0 (* number of states processed by a blue dfs *)
	val mutable depth_reached = false (* used when a max depth has been reached *)

	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(* Name of the algorithm *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	method algorithm_name = "NDFS"

	(************************************)
	(* Check the states and time limits *)
	(************************************)
	method private check_and_update_queue_dfs_limit =

	try(
	(* States limit *)
	begin
	match options#states_limit with
		| None -> ()
		| Some limit -> if StateSpace.nb_states state_space > limit then(
(* 				termination_status <- States_limit; *)
			raise (DFS_Limit_detected States_limit_reached)
		)
	end
	;
	(* Time limit *)
	begin
	match options#time_limit with
		| None -> ()
		| Some limit -> if time_from start_time > (float_of_int limit) then(
(* 				termination_status <- Time_limit; *)
			raise (DFS_Limit_detected Time_limit_reached)
		)
	end
	;
	(* If reached here, then everything is fine: keep going *)
	()
	)
	(* If exception caught, then update termination status, and return the reason *)
	with DFS_Limit_detected reason ->
		limit_reached <- reason


	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(*-*                                                       *-*)
	(*-*                       NDFS code                       *-*)
	(*-*                                                       *-*)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)

	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(* Main method to run NDFS exploration [WORK IN PROGRESS] *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	method explore_layer_bfs init_state_index =


		(* Statistics *)
		counter_explore_using_strategy#increment;
		counter_explore_using_strategy#start;

		let options = Input.get_options() in
		limit_reached <- Keep_going;

		(************************************)
		(* basic queues for NDFS algorithms *)
		(************************************)
		let cyan = ref [] in
		let blue = Hashtbl.create 100 in
		let red = ref [] in
		let pending = ref [] in (* used in the layered algorithms *)

		(**************************************)
		(* variable for the synthesis results *)
		(**************************************)
		let constraint_list = ref [] in (* list of results found *)
		let collected_constr = ref (LinearConstraint.false_p_nnconvex_constraint()) in


                (* Table add, test and remove; a state is present as it maps to ():unit *)
                let table_add table state_index =
                        Hashtbl.replace table state_index ()
                in
                let table_rem table state_index =
                        Hashtbl.remove table state_index
                in
                let table_test table state_index =
                        List.length (Hashtbl.find_all table state_index) > 0
                in

		(***********************)
		(* printing the queues *)
		(***********************)
		let printqueue colour thequeue =
			if verbose_mode_greater Verbose_low then(
				let rec r_printqueue thequeue = match thequeue with
					| [] -> "";
					| state_index::body  ->
						(string_of_int state_index) ^ " " ^ (r_printqueue body);
				in print_message Verbose_low("Queue " ^ colour ^ " : [ "
						^ r_printqueue thequeue ^ "]")
			);
		in

	        let printtable colour thetable =
                        if verbose_mode_greater Verbose_low then(
                                let printrecord state_index u rest =
                                        (string_of_int state_index) ^ " " ^ rest;
                                in print_message Verbose_low("Table " ^ colour ^ " : [ "
                                        ^ Hashtbl.fold printrecord thetable "" ^ "]")
                        );
                in

		let printpendingqueue colour thequeue =
			if verbose_mode_greater Verbose_low then(
				let rec r_printqueue thequeue = match thequeue with
					| [] -> "";
					| (state_index,state_depth)::body  ->
						"(" ^ (string_of_int state_index)
							^ ", " ^ (string_of_int state_depth) ^ ") "
							^ (r_printqueue body);
				in print_message Verbose_low("Queue " ^ colour ^ " : [ "
						^ r_printqueue thequeue ^ "]")
			);
		in

		(***************************************)
		(* put accepting states first in queue *)
		(***************************************)
		let reorderqueue thequeue =
			if not options#no_acceptfirst then (
				let newqueue = ref [] in
				List.iter (fun astate ->
					if (State.is_accepting (StateSpace.get_state state_space astate)) then (
						newqueue := astate::(!newqueue);
					) else (newqueue := (!newqueue)@[astate];)
				) thequeue;
				(!newqueue)
			) else thequeue
		in


		(*** TODO: factor the following 2 functions!!! ***)

		(***************************************************)
		(* Check equality of zone projection on parameters *)
		(***************************************************)
		let same_parameter_projection state_index1 state_index2 =
			let state1 = StateSpace.get_state state_space state_index1 in
			let constr1 = LinearConstraint.px_hide_nonparameters_and_collapse state1.px_constraint in
			let state2 = StateSpace.get_state state_space state_index2 in
			let constr2 = LinearConstraint.px_hide_nonparameters_and_collapse state2.px_constraint in
			print_message Verbose_high ("Projected constraint 1: \n"
				^ LinearConstraint.string_of_p_linear_constraint model.variable_names constr1
				^ " state: "
				^ (StateSpace.string_of_state_index state_index1));
			print_message Verbose_high ("Projected constraint 2: \n"
				^ LinearConstraint.string_of_p_linear_constraint model.variable_names constr2
				^ " state: "
				^ (StateSpace.string_of_state_index state_index2));
			LinearConstraint.p_is_equal constr1 constr2
		in

		(****************************************************)
		(* Check inclusion of zone projection on parameters *)
		(****************************************************)
		let smaller_parameter_projection state_index1 state_index2 =
			let state1 = StateSpace.get_state state_space state_index1 in
			let constr1 = LinearConstraint.px_hide_nonparameters_and_collapse state1.px_constraint in
			let state2 = StateSpace.get_state state_space state_index2 in
			let constr2 = LinearConstraint.px_hide_nonparameters_and_collapse state2.px_constraint in
			print_message Verbose_high ("Projected constraint 1: \n"
				^ LinearConstraint.string_of_p_linear_constraint model.variable_names constr1
				^ " state: "
				^ (StateSpace.string_of_state_index state_index1));
			print_message Verbose_high ("Projected constraint 2: \n"
				^ LinearConstraint.string_of_p_linear_constraint model.variable_names constr2
				^ " state: "
				^ (StateSpace.string_of_state_index state_index2));
			LinearConstraint.p_is_leq constr1 constr2
		in

		(****************************************************************************************)
		(* Check if parameter constraint is included in a non-convex list of convex constraints *)
		(****************************************************************************************)
		let check_parameter_leq_list astate_index =
			print_highlighted_message Shell_bold Verbose_high
				("Testing inclusion of parameter zone in list of collected constraints");
			let astate = StateSpace.get_state state_space astate_index in
			let linear_aconstr =
				LinearConstraint.px_hide_nonparameters_and_collapse astate.px_constraint in
			let astate_constr =
				LinearConstraint.p_nnconvex_constraint_of_p_linear_constraint linear_aconstr in
			if (LinearConstraint.p_nnconvex_constraint_is_leq astate_constr !collected_constr) then (
				print_highlighted_message Shell_bold Verbose_medium("Pruning with inclusion in collected constraints");
				true
			) else false
		in

		(*************************************)
		(* Returns True if thequeue is empty *)
		(*************************************)
		let queue_is_empty thequeue = match thequeue with
			| [] -> true;
			| _ -> false;
		in

		(**************************************************)
		(* add a state and its depth to the pending queue *)
		(**************************************************)
		let add_pending astate_index astate_depth =
		begin
			match options#pending_order with
			| Pending_none ->
				(* standard queuing *)
				pending := (astate_index,astate_depth)::(!pending)
			| Pending_param ->
				(* add the state in the right place in the queue: larger parametric projections of zones first *)
				if (queue_is_empty !pending) then
					pending := [(astate_index,astate_depth)]
				else (
					let newpending = ref [] in
					while not (queue_is_empty !pending) do
						match (!pending) with
							| [] -> raise (InternalError ("Impossible situation in algoNDFS: the queue should not be empty"))
							| (first_state_index,first_state_depth)::body ->
								if (smaller_parameter_projection first_state_index astate_index) then (
									(* insert a state before the current state *)
									newpending := (!newpending)@[(astate_index,astate_depth)];
									newpending := (!newpending)@(!pending);
									pending := [];
								) else (
									newpending := (!newpending)@[(first_state_index,first_state_depth)];
									pending := body;
									if (queue_is_empty !pending) then
										(* no more states to compare with *)
										newpending := (!newpending)@[(astate_index,astate_depth)];
								)
					done;
					pending := !newpending;
				)
			| Pending_accept ->
				(* insert accepting states at the head, others at the tail *)
				if (State.is_accepting (StateSpace.get_state state_space astate_index)) then (
						pending := (astate_index,astate_depth)::(!pending);
				) else (pending := (!pending)@[(astate_index,astate_depth)];
				)
			| Pending_zone ->
				(* add the state in the right place in the queue: larger zones first *)
				if (queue_is_empty !pending) then
					pending := [(astate_index,astate_depth)]
				else (
					let newpending = ref [] in
					let astate = StateSpace.get_state state_space astate_index in
					let astate_loc, astate_constr =
							astate.global_location, astate.px_constraint in
					while not (queue_is_empty !pending) do
						match (!pending) with
							| [] -> raise (InternalError ("Impossible situation in algoNDFS: the queue should not be empty"))
							| (first_state_index,first_state_depth)::body ->
								let state1 =
										StateSpace.get_state state_space first_state_index in
								let state1_loc, state1_constr =
										state1.global_location, state1.px_constraint in
								if (LinearConstraint.px_is_leq state1_constr astate_constr) then (
									(* insert a state before the current state *)
									newpending := (!newpending)@[(astate_index,astate_depth)];
									newpending := (!newpending)@(!pending);
									pending := [];
								) else (
									newpending :=
										(!newpending)@[(first_state_index,first_state_depth)];
									pending := body;
									if (queue_is_empty !pending) then
										(* no more states to compare with *)
										newpending :=
											(!newpending)@[(astate_index,astate_depth)];
								)
					done;
					pending := !newpending;
				)
			end;
			printpendingqueue "Pending (state added)" !pending
		in

		(**********************************)
		(* Check the subsumption relation *)
		(**********************************)
		let subsumes bigstate_index smallstate_index =
			(* Does bigstate subsume smallstate? *)
			print_message Verbose_high "Compare (big?) state:";
			print_message Verbose_high (ModelPrinter.string_of_state model
						(StateSpace.get_state state_space bigstate_index));
			print_message Verbose_high "with (small?) state:";
			print_message Verbose_high (ModelPrinter.string_of_state model
						(StateSpace.get_state state_space smallstate_index));
			(* get the big state *)
			let bigstate = StateSpace.get_state state_space bigstate_index in
			let stateb_loc, stateb_constr = bigstate.global_location, bigstate.px_constraint in
			(* get the small state *)
			let smallstate = StateSpace.get_state state_space smallstate_index in
			let states_loc, states_constr = smallstate.global_location, smallstate.px_constraint in
			(* check that the location is the same *)
			if not (Location.location_equal stateb_loc states_loc) then false
			else (LinearConstraint.px_is_leq states_constr stateb_constr) (* check the inclusion of constraints *)
		in

		let setsubsumes setbig smallstate =
			(* Does an element of the set subsume smallstate? *)
                        (* we traverse all states with the same location modulo hash collision *)
                        let similar_states = StateSpace.get_comparable_states state_space smallstate in
                        let check_sub bigstate = (table_test setbig bigstate) && (subsumes bigstate smallstate) in
			List.exists check_sub similar_states
		in

		let subsumesset bigstate setsmall =
			(* Does bigstate subsume some element of the set? *)
                        (* we traverse all states with the same location modulo hash collision *)
                        let similar_states = StateSpace.get_comparable_states state_space bigstate in
                        let check_sub smallstate = (table_test setsmall smallstate) && (subsumes bigstate smallstate) in
			List.exists check_sub similar_states
		in

		let layersetsubsumes setbig smallstate =
			(* Does an element of the set subsume smallstate and is in the same layer? *)
                        (* we traverse all states with the same location modulo hash collision *)
                        let similar_states = StateSpace.get_comparable_states state_space smallstate in
                        let check_sub bigstate =
                                (table_test setbig bigstate) && (subsumes bigstate smallstate) && (same_parameter_projection bigstate smallstate) in
			List.exists check_sub similar_states
		in

		(******************************************)
		(* printing zone projection on parameters *)
		(******************************************)
		let print_projection verbose_level thestate =
			let state_constr = (StateSpace.get_state state_space thestate).px_constraint in
			let constr = LinearConstraint.px_hide_nonparameters_and_collapse state_constr in
			print_message verbose_level ("Projected constraint : \n"
				^ LinearConstraint.string_of_p_linear_constraint model.variable_names constr)
		in

		(***********************************)
		(* Function to perform a lookahead *)
		(***********************************)
		let withLookahead thesuccessors =
			if not options#no_lookahead then (
				try ((List.find (fun suc_id ->
					(State.is_accepting (StateSpace.get_state state_space suc_id)) &&
				(List.mem suc_id !cyan)) thesuccessors), true)
				with Not_found -> init_state_index, false
			) else init_state_index, false
		in

		(*****************************)
		(* Function for no lookahead *)
		(*****************************)
		let noLookahead thesuccessors = init_state_index, false in

		(***************************)
		(* General Scheme of a DFS *)
		(***************************)
		let rec rundfs enterdfs predfs lookahead cyclefound filterdfs testaltdfs alternativedfs
			testrecursivedfs postdfs thestate thestate_depth =
			(* Check the termination condition *)
			self#check_and_update_queue_dfs_limit;
			(* Update termination condition *)
			begin
			match limit_reached with
			(*** NOTE: check None, as it may have been edited from outside, in which case it should not be Regular_termination ***)
			| Keep_going when termination_status = None -> termination_status <- Some (Result.Regular_termination)
			(*** NOTE: obliged to comment out the condition below, otherwise there is a compiling warning… ***)
			| Keep_going (*when termination_status <> None*) -> ()

			(* Termination due to time limit reached *)
			| Time_limit_reached -> termination_status <- Some (Result.Time_limit (List.length !cyan))

			(* Termination due to a number of explored states reached *)
			| States_limit_reached -> termination_status <- Some (Result.States_limit (List.length !cyan))

			(* Termination due to state space depth limit reached *)
			| Depth_limit_reached -> termination_status <- Some (Result.Depth_limit (List.length !cyan))
			end;
			if (limit_reached <> Keep_going) then raise (TerminateAnalysis)
			else(
			print_highlighted_message Shell_bold Verbose_low("Executing rundfs at depth "
				^ (string_of_int thestate_depth)
				^ " with "
				^ (if State.is_accepting (StateSpace.get_state state_space thestate)
					then "accepting " else "")
				^ "state "
				^ (StateSpace.string_of_state_index thestate)
				^ ":\n"
				^ (ModelPrinter.string_of_state model
					(StateSpace.get_state state_space thestate)));
			let depth_ok = match options#depth_limit with
				| None -> true
				| Some depth_value -> if (depth_value  > thestate_depth) then true
										else (depth_reached <- true; false)
			in
			if (depth_ok && enterdfs thestate) then (
				predfs thestate;
				let successors = reorderqueue (StateSpace.get_successors state_space thestate) in
				let rec process_sucs suclist = match suclist with
					| [] -> ();
					| suc_id::body ->
						print_message Verbose_low("Handling "
							^ (if State.is_accepting (StateSpace.get_state state_space suc_id)
								then "accepting " else "")
							^ "successor "
							^ (ModelPrinter.string_of_state model
								(StateSpace.get_state state_space suc_id)));
						if (filterdfs thestate suc_id) then (
							if (testaltdfs thestate suc_id) then (alternativedfs suc_id thestate_depth)
							else
							if (testrecursivedfs suc_id) then (
								rundfs enterdfs predfs lookahead cyclefound filterdfs testaltdfs alternativedfs testrecursivedfs postdfs suc_id (thestate_depth + 1))
						);
						process_sucs body;
				in
				let cyclestate, found = lookahead successors in
				(* if the cycle is found:
					- in the standard version, an exception is raised and the algorithm terminates
					- in the collecting version, the other sucessors cannot lead to a better zone,
						so there is no need to process them.
						However, the state must be marked blue and removed from cyan in the blue dfs *)
				if (found) then
					cyclefound thestate cyclestate
				else (process_sucs successors;
					postdfs thestate thestate_depth)
			))
		in

		(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
		(*                     State Space Exploration                       *)
		(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)

		print_message Verbose_standard("---------------- Starting exploration ----------------");

		(* Get the property to check whether we are in synthesis or witness mode *)
		let property = Input.get_property() in

		begin
		match options#exploration_order with

			| Exploration_NDFS ->
(* NDFS without subsumption *)
				(* set up the dfs blue calls *)
				let enterdfs (astate : State.state_index) : bool =
					if (options#counterex = false &&
							check_parameter_leq_list astate) then (
                                                table_add blue astate;
						printtable "Blue" blue;
						false
					) else true in
				let predfs (astate : State.state_index) : unit =
					processed_blue <- processed_blue + 1;
					cyan := astate::(!cyan);
					printqueue "Cyan" !cyan;
					(*** WARNING (ÉA, 2019/07/11): this statement is a bit strange with unit type ***)
					let _ = self#post_from_one_state astate in ();
					() in
				let cyclefound (thestate : State.state_index) (astate : State.state_index) : unit =
					cyclecount <- cyclecount + 1;
					if (options#counterex = true) then
						print_highlighted_message Shell_bold Verbose_standard
							("Cycle found at state " ^ (string_of_int astate))
					else print_highlighted_message Shell_bold Verbose_standard
							("Cycle " ^ (string_of_int cyclecount) ^ " found at state " ^ (string_of_int astate));
					print_message Verbose_standard
						(ModelPrinter.string_of_state model
							(StateSpace.get_state state_space astate));
					(* For synthesis: we do not stop immediately *)
					if (options#counterex = false) then
						termination_status <- Some Regular_termination
					else termination_status <- Some Target_found;
					print_projection Verbose_standard astate;
					let state_constr = (StateSpace.get_state state_space astate).px_constraint in
					constraint_list := (LinearConstraint.px_hide_nonparameters_and_collapse state_constr)::(!constraint_list);
					collected_constr :=	LinearConstraint.p_nnconvex_constraint_of_p_linear_constraints !constraint_list;
					if (options#counterex = true) then raise TerminateAnalysis;
					table_add blue astate;
					printtable "Blue" blue;
					(* and the current state is popped from the cyan list *)
					match !cyan with
					| thestate::body ->
						cyan := body;
						printqueue "Cyan" !cyan;
					| _ -> print_message Verbose_standard "Error popping from cyan";
				in
				let filterdfs (thestate : State.state_index) (astate : State.state_index) : bool =
					if (not (table_test blue astate) &&
						not (List.mem astate !cyan)) then true else false in
				let testaltdfs (thestate : State.state_index) (astate : State.state_index) : bool =
					false in
				let alternativedfs (astate : State.state_index) (astate_depth : int) : unit =
					() in
				let testrecursivedfs (astate : State.state_index) : bool =
					true in
				let postdfs (astate : State.state_index) (astate_depth : int) : unit =
					(* launch red dfs only if not with a smaller constraint than a state marked by a lookahead *)
					if ((not (check_parameter_leq_list astate)) &&
							(State.is_accepting (StateSpace.get_state state_space astate))) then (
						(* set up the dfs red calls *)
						let enterdfs (astate : State.state_index) : bool =
							true in
						let predfs (astate : State.state_index) : unit =
							red := astate::(!red);
							printqueue "Red" !red in
						let cyclefound (thestate : State.state_index) (astate : State.state_index) : unit =
							cyclecount <- cyclecount + 1;
							if (options#counterex = true) then
								print_highlighted_message Shell_bold Verbose_standard
									("Cycle found at state " ^ (string_of_int astate))
							else print_highlighted_message Shell_bold Verbose_standard
								("Cycle " ^ (string_of_int cyclecount) ^ " found at state " ^ (string_of_int astate));
							print_message Verbose_standard
								(ModelPrinter.string_of_state model
									(StateSpace.get_state state_space astate));
							(* For synthesis: we do not stop immediately *)
							termination_status <- Some Target_found;
							print_projection Verbose_standard astate;
							let state_constr = (StateSpace.get_state state_space astate).px_constraint in
							constraint_list := (LinearConstraint.px_hide_nonparameters_and_collapse state_constr)::(!constraint_list);
							collected_constr :=	LinearConstraint.p_nnconvex_constraint_of_p_linear_constraints !constraint_list;
							if (options#counterex = true) then raise TerminateAnalysis;
						in
						let filterdfs (thestate : State.state_index) (astate : State.state_index) : bool =
							true in
						let testaltdfs (thestate : State.state_index) (astate : State.state_index) : bool =
							if (List.mem astate !cyan) then true else false in
						let alternativedfs (astate : State.state_index) (astate_depth : int) : unit =
							cyclefound astate astate
						in
						let testrecursivedfs (astate : State.state_index) : bool =
							if (not (List.mem astate !red)) then true else false in
						let postdfs (astate : State.state_index) (astate_depth : int) : unit =
							() in
						rundfs enterdfs predfs noLookahead cyclefound filterdfs testaltdfs alternativedfs testrecursivedfs postdfs astate astate_depth
					);
					table_add blue astate;
					printtable "Blue" blue;
					match !cyan with
					| astate::body ->
						cyan := body;
						printqueue "Cyan" !cyan;
					| _ -> print_message Verbose_standard "Error popping from cyan";
					() in
				(try (rundfs enterdfs predfs withLookahead cyclefound filterdfs testaltdfs alternativedfs testrecursivedfs postdfs init_state_index 0;)
					with TerminateAnalysis -> ());
				print_message Verbose_low("Finished the calls")

			| Exploration_NDFS_sub ->
(* NDFS with subsumption *)
				(* set up the dfs blue calls *)
				let enterdfs (astate : State.state_index) : bool =
					if (options#counterex = false && check_parameter_leq_list astate) then (
						(* State astate has been handled and must now become blue *)
						table_add blue astate;
						printtable "Blue" blue;
						false
					) else true
				in
				let predfs (astate : State.state_index) : unit =
					processed_blue <- processed_blue + 1;
					cyan := astate::(!cyan);
					printqueue "Cyan" !cyan;
					(*** WARNING (ÉA, 2019/07/11): this statement is a bit strange with unit type ***)
					let _ = self#post_from_one_state astate in ();
					() in
				let cyclefound (thestate : State.state_index) (astate : State.state_index) : unit =
					cyclecount <- cyclecount + 1;
					if (options#counterex = true) then
						print_highlighted_message Shell_bold Verbose_standard
							("Cycle found at state " ^ (string_of_int astate))
					else print_highlighted_message Shell_bold Verbose_standard
							("Cycle " ^ (string_of_int cyclecount) ^ " found at state " ^ (string_of_int astate));
					print_message Verbose_standard
						(ModelPrinter.string_of_state model
							(StateSpace.get_state state_space astate));
							(* For synthesis: we do not stop immediately *)
					if (options#counterex = false) then
						termination_status <- Some Regular_termination
					else termination_status <- Some Target_found;
					print_projection Verbose_standard astate;
					let state_constr = (StateSpace.get_state state_space astate).px_constraint in
					constraint_list := (LinearConstraint.px_hide_nonparameters_and_collapse state_constr)::(!constraint_list);
					collected_constr :=	LinearConstraint.p_nnconvex_constraint_of_p_linear_constraints !constraint_list;
					if (options#counterex = true) then raise TerminateAnalysis;
					(* the state where the lookahead has found a cycle is now set blue *)
					table_add blue astate;
					printtable "Blue" blue;
					(* and the current state is popped from the cyan list *)
					match !cyan with
					| thestate::body ->
						cyan := body;
						printqueue "Cyan" !cyan;
					| _ -> print_message Verbose_standard "Error popping from cyan";
				in
				let filterdfs (thestate : State.state_index) (astate : State.state_index) : bool =
					if (not (table_test blue astate) &&
						not (List.mem astate !cyan) &&
						not (setsubsumes !red astate)) then true else false in
				let testaltdfs (thestate : State.state_index) (astate : State.state_index) : bool =
					false in
				let alternativedfs (astate: State.state_index) (astate_depth : int) : unit =
					() in
				let testrecursivedfs (astate: State.state_index) : bool =
					true in
				let postdfs (astate: State.state_index) (astate_depth : int) : unit =
					(* launch red dfs only if not with a smaller constraint than a state marked by a lookahead *)
					if ((not (check_parameter_leq_list astate)) &&
							(State.is_accepting (StateSpace.get_state state_space astate))) then (
						(* set up the dfs red calls *)
						let enterdfs (astate: State.state_index) : bool =
							true in
						let predfs (astate: State.state_index) : unit =
							red := astate::(!red);
							printqueue "Red" !red in
						let cyclefound (thestate : State.state_index) (astate : State.state_index) : unit =
							cyclecount <- cyclecount + 1;
							if (options#counterex = true) then
								print_highlighted_message Shell_bold Verbose_standard
									("Cycle found at state " ^ (string_of_int astate))
							else print_highlighted_message Shell_bold Verbose_standard
								("Cycle " ^ (string_of_int cyclecount) ^ " found at state " ^ (string_of_int astate));
							print_message Verbose_standard
								(ModelPrinter.string_of_state model
									(StateSpace.get_state state_space astate));
							(* For synthesis: we do not stop immediately *)
							if (options#counterex = false) then
								termination_status <- Some Regular_termination
							else termination_status <- Some Target_found;
							print_projection Verbose_standard astate;
							let state_constr = (StateSpace.get_state state_space astate).px_constraint in
							constraint_list := (LinearConstraint.px_hide_nonparameters_and_collapse state_constr)::(!constraint_list);
							collected_constr :=	LinearConstraint.p_nnconvex_constraint_of_p_linear_constraints !constraint_list;
							if (options#counterex = true) then raise TerminateAnalysis;
						in
						let filterdfs (thestate : State.state_index) (astate : State.state_index) : bool =
							if (same_parameter_projection thestate astate) then true
							else false in
						let testaltdfs (thestate : State.state_index) (astate : State.state_index) : bool =
							if (subsumesset astate !cyan) then true else false in
						let alternativedfs (astate : State.state_index) (astate_depth : int) : unit =
							cyclefound astate astate
						in
						let testrecursivedfs (astate : State.state_index) : bool =
							if (not (setsubsumes !red astate)) then true else false in
						let postdfs (astate : State.state_index) (astate_depth : int) : unit =
							() in
						rundfs enterdfs predfs noLookahead cyclefound filterdfs testaltdfs alternativedfs testrecursivedfs postdfs astate astate_depth
					);
					table_add blue astate;
					printtable "Blue" blue;
					match !cyan with
					| astate::body ->
						cyan := body;
						printqueue "Cyan" !cyan;
					| _ -> print_message Verbose_standard "Error popping from cyan";
					() in
				(try (rundfs enterdfs predfs withLookahead cyclefound filterdfs testaltdfs alternativedfs testrecursivedfs postdfs init_state_index 0;)
					with TerminateAnalysis -> ());
				print_message Verbose_low("Finished the calls")

			| Exploration_layer_NDFS ->
(* NDFS with layers but no subsumption *)
				(* set up the dfs blue calls *)
				add_pending init_state_index 0;
				(try (while !pending != [] do
					match !pending with
					| [] -> print_message Verbose_standard ("Impossible case");
					| (thestate,thestate_depth)::body ->
						pending := body;
						print_message Verbose_low ("Popped state "
							^ (string_of_int thestate));
						printpendingqueue "Pending" !pending;
						if (not (table_test blue thestate)) then
						begin
						let enterdfs (astate : State.state_index) : bool =
							if (options#counterex = false && check_parameter_leq_list astate) then (
								(* State astate has been handled and must now become blue *)
								table_add blue astate;
								printtable "Blue" blue;
								false
							) else true
						in
						let predfs (astate : State.state_index) : unit =
							processed_blue <- processed_blue + 1;
							cyan := astate::(!cyan);
							printqueue "Cyan" !cyan;
							(*** WARNING (ÉA, 2019/07/11): this statement is a bit strange with unit type ***)
							let _ = self#post_from_one_state astate in ();
							() in
						let cyclefound (thestate : State.state_index) (astate : State.state_index) : unit =
							cyclecount <- cyclecount + 1;
							if (options#counterex = true) then
								print_highlighted_message Shell_bold Verbose_standard
									("Cycle found at state " ^ (string_of_int astate))
							else print_highlighted_message Shell_bold Verbose_standard
									("Cycle " ^ (string_of_int cyclecount) ^ " found at state " ^ (string_of_int astate));
							print_message Verbose_standard
								(ModelPrinter.string_of_state model
									(StateSpace.get_state state_space astate));
								(* For synthesis: we do not stop immediately *)
							if (options#counterex = false) then
								termination_status <- Some Regular_termination
							else termination_status <- Some Target_found;
							print_projection Verbose_standard astate;
							let state_constr = (StateSpace.get_state state_space astate).px_constraint in
							constraint_list := (LinearConstraint.px_hide_nonparameters_and_collapse state_constr)::(!constraint_list);
							collected_constr :=	LinearConstraint.p_nnconvex_constraint_of_p_linear_constraints !constraint_list;
							if (options#counterex = true) then raise TerminateAnalysis;
							(* the state where the lookahead has found a cycle is now set blue *)
							table_add blue astate;
							printtable "Blue" blue;
							(* and the current state is popped from the cyan list *)
							match !cyan with
							| thestate::body ->
								cyan := body;
								printqueue "Cyan" !cyan;
							| _ -> print_message Verbose_standard "Error popping from cyan";
						in
						let filterdfs (thestate : State.state_index) (astate : State.state_index) : bool =
							if (not (table_test blue astate) &&
								not (List.mem astate !cyan)) then true else false in
						let testaltdfs (thestate : State.state_index) (astate : State.state_index) : bool =
							if (not (same_parameter_projection thestate astate)) then true
							else false in
						let alternativedfs (astate: State.state_index) (astate_depth : int) : unit =
							add_pending astate (astate_depth + 1) in
						let testrecursivedfs (astate: State.state_index) : bool =
							true in
						let postdfs (astate: State.state_index) (astate_depth : int) : unit =
							(* launch red dfs only if not with a smaller constraint than a state marked by a lookahead *)
							if ((not (check_parameter_leq_list astate)) &&
									(State.is_accepting (StateSpace.get_state state_space astate))) then (
								(* set up the dfs red calls *)
								let enterdfs (astate: State.state_index) : bool =
									true in
								let predfs (astate: State.state_index) : unit =
									red := astate::(!red);
									printqueue "Red" !red in
								let cyclefound (thestate : State.state_index) (astate : State.state_index) : unit =
									cyclecount <- cyclecount + 1;
									if (options#counterex = true) then
										print_highlighted_message Shell_bold Verbose_standard
											("Cycle found at state " ^ (string_of_int astate))
									else print_highlighted_message Shell_bold Verbose_standard
										("Cycle " ^ (string_of_int cyclecount) ^ " found at state " ^ (string_of_int astate));
									print_message Verbose_standard
										(ModelPrinter.string_of_state model
											(StateSpace.get_state state_space astate));
									(* For synthesis: we do not stop immediately *)
									if (options#counterex = false) then
										termination_status <- Some Regular_termination
									else termination_status <- Some Target_found;
									print_projection Verbose_standard astate;
									let state_constr = (StateSpace.get_state state_space astate).px_constraint in
									constraint_list := (LinearConstraint.px_hide_nonparameters_and_collapse state_constr)::(!constraint_list);
									collected_constr :=	LinearConstraint.p_nnconvex_constraint_of_p_linear_constraints !constraint_list;
								if (options#counterex = true) then raise TerminateAnalysis;
								in
								let filterdfs (thestate : State.state_index) (astate : State.state_index) : bool =
									if (same_parameter_projection thestate astate) then true
									else false in
								let testaltdfs (thestate : State.state_index) (astate : State.state_index) : bool =
									if (List.mem astate !cyan) then true
									else false in
								let alternativedfs (astate : State.state_index) (astate_depth : int) : unit =
									cyclefound astate astate
								in
								let testrecursivedfs (astate : State.state_index) : bool =
									if (not (List.mem astate !red)) then true
									else false in
								let postdfs (astate : State.state_index) (astate_depth : int) : unit =
									() in
								rundfs enterdfs predfs noLookahead cyclefound filterdfs testaltdfs alternativedfs testrecursivedfs postdfs astate astate_depth
							);
							table_add blue astate;
							printtable "Blue" blue;
							match !cyan with
							| astate::body ->
								cyan := body;
								printqueue "Cyan" !cyan;
							| _ -> print_message Verbose_standard "Error popping from cyan";
							() in
						rundfs enterdfs predfs withLookahead cyclefound filterdfs testaltdfs alternativedfs testrecursivedfs postdfs thestate thestate_depth;
						end;
				done;)

							with TerminateAnalysis -> ());
				print_message Verbose_low("Finished the calls")

			| Exploration_layer_NDFS_sub ->
(* NDFS with layers and subsumption *)
				(* set up the dfs blue calls *)
				add_pending init_state_index 0;
				(try (while !pending != [] do
					match !pending with
					| [] -> print_message Verbose_standard ("Impossible case");
					| (thestate,thestate_depth)::body ->
						pending := body;
						print_message Verbose_low ("Popped state "
							^ (string_of_int thestate));
						printpendingqueue "Pending" !pending;
						if (not (table_test blue thestate)) then
						begin
						let enterdfs (astate : State.state_index) : bool =
							if (options#counterex = false && check_parameter_leq_list astate) then (
								(* State astate has been handled and must now become blue *)
								table_add blue astate;
								printtable "Blue" blue;
								false
							) else true
						in
						let predfs (astate : State.state_index) : unit =
							processed_blue <- processed_blue + 1;
							cyan := astate::(!cyan);
							printqueue "Cyan" !cyan;
							(*** WARNING (ÉA, 2019/07/11): this statement is a bit strange with unit type ***)
							let _ = self#post_from_one_state astate in ();
							() in
						let cyclefound (thestate : State.state_index) (astate : State.state_index) : unit =
							cyclecount <- cyclecount + 1;
							if (options#counterex = true) then
								print_highlighted_message Shell_bold Verbose_standard
									("Cycle found at state " ^ (string_of_int astate))
							else print_highlighted_message Shell_bold Verbose_standard
									("Cycle " ^ (string_of_int cyclecount) ^ " found at state " ^ (string_of_int astate));
							print_message Verbose_standard
								(ModelPrinter.string_of_state model
									(StateSpace.get_state state_space astate));
								(* For synthesis: we do not stop immediately *)
							if (options#counterex = false) then
								termination_status <- Some Regular_termination
							else termination_status <- Some Target_found;
							print_projection Verbose_standard astate;
							let state_constr = (StateSpace.get_state state_space astate).px_constraint in
							constraint_list := (LinearConstraint.px_hide_nonparameters_and_collapse state_constr)::(!constraint_list);
							collected_constr :=	LinearConstraint.p_nnconvex_constraint_of_p_linear_constraints !constraint_list;
							if (options#counterex = true) then raise TerminateAnalysis;
							(* the state where the lookahead has found a cycle is now set blue *)
							table_add blue astate;
							printtable "Blue" blue;
							(* and the current state is popped from the cyan list *)
							match !cyan with
							| thestate::body ->
								cyan := body;
								printqueue "Cyan" !cyan;
							| _ -> print_message Verbose_standard "Error popping from cyan";
						in
						let filterdfs (thestate : State.state_index) (astate : State.state_index) : bool =
							if (not (table_test blue astate) &&
								not (List.mem astate !cyan) &&
								not (layersetsubsumes !red astate)) then true else false in
						let testaltdfs (thestate : State.state_index) (astate : State.state_index) : bool =
							if (not (same_parameter_projection thestate astate)) then true
							else false in
						let alternativedfs (astate: State.state_index) (astate_depth : int) : unit =
							add_pending astate (astate_depth + 1) in
						let testrecursivedfs (astate: State.state_index) : bool =
							true in
						let postdfs (astate: State.state_index) (astate_depth : int) : unit =
							(* launch red dfs only if not with a smaller constraint than a state marked by a lookahead *)
							if ((not (check_parameter_leq_list astate)) &&
									(State.is_accepting (StateSpace.get_state state_space astate))) then (
								(* set up the dfs red calls *)
								let enterdfs (astate: State.state_index) : bool =
									true in
								let predfs (astate: State.state_index) : unit =
									red := astate::(!red);
									printqueue "Red" !red in
								let cyclefound (thestate : State.state_index) (astate : State.state_index) : unit =
									cyclecount <- cyclecount + 1;
									if (options#counterex = true) then
										print_highlighted_message Shell_bold Verbose_standard
											("Cycle found at state " ^ (string_of_int astate))
									else print_highlighted_message Shell_bold Verbose_standard
										("Cycle " ^ (string_of_int cyclecount) ^ " found at state " ^ (string_of_int astate));
									print_message Verbose_standard
										(ModelPrinter.string_of_state model
											(StateSpace.get_state state_space astate));
									(* For synthesis: we do not stop immediately *)
									if (options#counterex = false) then
										termination_status <- Some Regular_termination
									else termination_status <- Some Target_found;
									print_projection Verbose_standard astate;
									let state_constr = (StateSpace.get_state state_space astate).px_constraint in
									constraint_list := (LinearConstraint.px_hide_nonparameters_and_collapse state_constr)::(!constraint_list);
									collected_constr :=	LinearConstraint.p_nnconvex_constraint_of_p_linear_constraints !constraint_list;
								if (options#counterex = true) then raise TerminateAnalysis;
								in
								let filterdfs (thestate : State.state_index) (astate : State.state_index) : bool =
									if (same_parameter_projection thestate astate) then true
									else false in
								let testaltdfs (thestate : State.state_index) (astate : State.state_index) : bool =
									if (subsumesset astate !cyan) then true
									else false in
								let alternativedfs (astate : State.state_index) (astate_depth : int) : unit =
									cyclefound astate astate
								in
								let testrecursivedfs (astate : State.state_index) : bool =
									if (not (layersetsubsumes !red astate)) then true
									else false in
								let postdfs (astate : State.state_index) (astate_depth : int) : unit =
									() in
								rundfs enterdfs predfs noLookahead cyclefound filterdfs testaltdfs alternativedfs testrecursivedfs postdfs astate astate_depth
							);
							table_add blue astate;
							printtable "Blue" blue;
							match !cyan with
							| astate::body ->
								cyan := body;
								printqueue "Cyan" !cyan;
							| _ -> print_message Verbose_standard "Error popping from cyan";
							() in
						rundfs enterdfs predfs withLookahead cyclefound filterdfs testaltdfs alternativedfs testrecursivedfs postdfs thestate thestate_depth;
						end;
				done;)

							with TerminateAnalysis -> ());
				print_message Verbose_low("Finished the calls")

			| _ -> raise (InternalError ("Unknown exploration order in NDFS"))
		end;

		(* combine the linear constraints *)
		constraint_valuations <- Some !collected_constr;

		print_message Verbose_standard("---------------- Ending exploration ------------------");

		(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
		(*                 End of State Space Exploration                    *)
		(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)

		(* Statistics *)
		counter_explore_using_strategy#stop;

		(* The end *)
		()

	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(* Variable initialization *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	method initialize_variables =
		super#initialize_variables;

		(* Nothing to do *)
		()

	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(* Add a new state to the state space (if indeed needed) *)
	(* Side-effects: modify new_states_indexes *)
	(*** TODO: move new_states_indexes to a variable of the class ***)
	(* Return true if the state is not discarded by the algorithm, i.e., if it is either added OR was already present before *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	method add_a_new_state source_state_index combined_transition new_state =
		(* Try to add the new state to the state space *)
		let addition_result = StateSpace.add_state state_space (self#state_comparison_operator_of_options) new_state in

		begin
		match addition_result with
		(* If the state was present: do nothing *)
		| StateSpace.State_already_present _ -> ()
		(* If this is really a new state, or a state larger than a former state *)
		| StateSpace.New_state new_state_index | StateSpace.State_replacing new_state_index ->

			(* First check whether this is a bad tile according to the property and the nature of the state *)
			(*** NOTE: in fact not necessary for this algorithm ***)
			self#update_statespace_nature new_state;

			(* Add the state_index to the list of new states (used to compute their successors at the next iteration) *)
			new_states_indexes <- new_state_index :: new_states_indexes;

		end; (* end if new state *)


		(*** TODO: move the rest to a higher level function? (post_from_one_state?) ***)

		(* Update the transitions *)
		self#add_transition_to_state_space (source_state_index, combined_transition, (*** HACK ***) match addition_result with | StateSpace.State_already_present new_state_index | StateSpace.New_state new_state_index | StateSpace.State_replacing new_state_index -> new_state_index) addition_result;

		(* The state is necessarily kept by the algorithm *)
		true


	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(** Actions to perform with the initial state; returns true unless the initial state cannot be kept (in which case the algorithm will stop immediately) *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	method process_initial_state _ =
		(* Always keep the initial state *)
		true


	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(* Actions to perform when meeting a state with no successors: nothing to do for this algorithm *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	method process_deadlock_state state_index = ()


	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(** Actions to perform at the end of the computation of the *successors* of post^n (i.e., when this method is called, the successors were just computed). Nothing to do for this algorithm. *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	method process_post_n (post_n : State.state_index list) = ()


	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(** Check whether the algorithm should terminate at the end of some post, independently of the number of states to be processed (e.g., if the constraint is already true or false) *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	method check_termination_at_post_n = false


	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(* Method packaging the result output by the algorithm *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	method compute_result =
		self#print_algo_message_newline Verbose_standard (
			"State space exploration completed " ^ (after_seconds ()) ^ "."
		);

		let nb_states = StateSpace.nb_states state_space in
		print_message Verbose_standard ("Number of computed states: " ^ (string_of_int nb_states));
		print_message Verbose_standard ("Number of processed states: " ^ (string_of_int processed_blue));
		print_message Verbose_standard ("Number of cycles found: " ^ (string_of_int cyclecount));

		(* Get the termination status *)
		 let termination_status = match termination_status with
			| None -> raise (InternalError "Termination status not set in NDFS exploration")
			| Some status -> status
		in

		let soundness =
			if (termination_status = Regular_termination && not depth_reached)
			then Constraint_exact
			else Constraint_maybe_under
		in

		let constr_result = match constraint_valuations with
				| None -> LinearConstraint.false_p_nnconvex_constraint()
				| Some constr -> constr
		in

		(* Return result *)
		Single_synthesis_result
		{
			(* Accepting_cycle_constraint *)
			result = Good_constraint (constr_result, soundness);

			(* English description of the constraint *)
			constraint_description = "constraint for detecting accepting cycles via NDFS exploration";

			(* Explored state space *)
			state_space			= state_space;

			(* Total computation time of the algorithm *)
			computation_time	= time_from start_time;

			(* Termination *)
			termination			= termination_status;
		}

(************************************************************)
(************************************************************)
end;;
(************************************************************)
(************************************************************)
