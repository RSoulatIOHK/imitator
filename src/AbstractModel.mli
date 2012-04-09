(*****************************************************************
 *
 *                     HYMITATOR
 * 
 * Laboratoire Specification et Verification (ENS Cachan & CNRS, France)
 * Author:        Etienne Andre
 * Created:       2009/09/11
 * Last modified: 2010/03/29
 *
 ****************************************************************)



(****************************************************************)
(* Modules *)
(****************************************************************)
open Global
open LinearConstraint
open Automaton


(****************************************************************)
(** Environment *)
(****************************************************************)

(****************************************************************)
(** Indexes *)
(****************************************************************)

type action_index = int
type action_name = string
type transition_index = int

(****************************************************************)
(** Pi 0 *)
(****************************************************************)

type pi0 = variable_index -> NumConst.t
type pi0cube = (NumConst.t * NumConst.t * NumConst.t) array


(****************************************************************)
(** Types *)
(****************************************************************)

(** Type of variable in declarations *)
type var_type =
	| Var_type_clock
	| Var_type_analog
	| Var_type_discrete
	| Var_type_parameter

(** Type of sync actions *)
type action_type =
	| Action_type_sync
	| Action_type_nosync

(****************************************************************)
(** State *)
(****************************************************************)

(** State: location and constraint *)
type state = location * linear_constraint

type abstract_state  = location * bool list

type abstract_label =
	| Continuous
	| Discrete of action_index * (automaton_index * transition_index) list

type predicate = linear_inequality

 
(****************************************************************)
(** Transition *)
(****************************************************************) 

type update = 
	| All_free                    (* all variables unconstrained *)
	| All_stable                  (* all variables keep their value x'=x *)
	| Clocks_stable               (* all clocks stable, all analog unconstrained *)
	| Update of linear_constraint

(** update: variable_index := linear_term *)
type clock_update = clock_index * linear_term

(** update: variable_index := linear_term *)
type discrete_update = discrete_index * linear_term

(** Guard: linear constraint *)
type guard = linear_constraint

(** Transition: guard, updates, destination location *)
type transition = guard * update * discrete_update list * location_index

(** Activities describing the continuous flow conditions *)
type activity =
	| Undefined
	| Rectangular of linear_constraint
	| Affine of linear_constraint


(****************************************************************)
(** The abstract program *)
(****************************************************************)
type abstract_program = {
	(* Cardinality *)
	nb_automata : int;
	nb_actions : int;
	nb_clocks : int;
	nb_discrete : int;
	nb_parameters : int;
	nb_variables : int;
	
	(* a set of all unprimed continuous variables *)
	continuous : VariableSet.t;
	(* local continuous variables for each automaton *)
	continuous_per_automaton : automaton_index -> VariableSet.t;
	
	(* True for analogs, false otherwise *)
	is_analog : variable_index -> bool;
	(* The list of clock indexes *)
	clocks : clock_index list;
	(* True for clocks, false otherwise *)
	is_clock : variable_index -> bool;
	(* The list of discrete indexes *)
	discrete : discrete_index list;
	(* True for discrete, false otherwise *)
	is_discrete : variable_index -> bool;
	(* The list of parameter indexes *)
	parameters : parameter_index list;
	(* The non parameters (clocks and discrete) *)
	clocks_and_discrete : variable_index list;
	(* The function : variable_index -> variable name *)
	variable_names : variable_index -> variable_name;
	(* The type of variables *)
	type_of_variables : variable_index -> var_type;
	
	(* Renamed clocks *)
	renamed_clocks : variable_index list;
	(* True for renamed clocks, false otherwise *)
	is_renamed_clock : variable_index -> bool;
	(* Get the 'prime' equivalent of a variable *)
	prime_of_variable : variable_index -> variable_index;
	(* Get the normal equivalent of a 'prime' variable *)
	variable_of_prime : variable_index -> variable_index;
	(* Couples (x, x') for clock renamings *)
	renamed_clocks_couples : (variable_index * variable_index) list;
	(* Couples (x', x) for clock 'un'-renamings *)
	unrenamed_clocks_couples : (variable_index * variable_index) list;

	(* The automata *)
	automata : automaton_index list;
	(* The automata names *)
	automata_names : automaton_index -> automaton_name;
	
	(* The locations for each automaton *)
	locations_per_automaton : automaton_index -> location_index list;
	(* The location names for each automaton *)
	location_names : automaton_index -> location_index -> location_name;

	(* All action indexes *)
	actions : action_index list;
	(* Action names *)
	action_names : action_index -> action_name;
	(* The type of actions *)
	action_types : action_index -> action_type;
	(* The list of actions for each automaton *)
	actions_per_automaton : automaton_index -> (action_index list);
	(* The list of automatons for each action *)
	automata_per_action : action_index -> (automaton_index list);
	(* The list of actions for each automaton for each location *)
	actions_per_location : automaton_index -> location_index -> (action_index list);

	(* The invariant for each automaton and each location *)
	invariants : automaton_index -> location_index -> linear_constraint;
	(* the standard flow constraint for paramters, discrete and clocks *) 
	standard_flow : linear_constraint;
	(* The rate conditions of analog variables for each automaton and each location *)
	analog_flows : automaton_index -> location_index -> activity;
	(* The transitions for each automaton and each location and each action *)
	transitions : automaton_index -> location_index -> action_index -> (transition list);

	(* Init : the initial state *)
	init : state;
	(* bad states *)
	bad  : (automaton_index * location_index) list;
	
	(* initial predicates for abstraction *)
	predicates : linear_inequality list;
	(* bounded domain for predicate abstraction algorithm *)
	domain : linear_constraint;

	(* Acyclic mode *)
	acyclic : bool;
	(* Inclusion for the post operation *)
	inclusion : bool;
	(* Return union of last states *)
	union : bool;
	(* Random selection of the pi0-incompatible inequality *)
	random : bool;
	(* Mode for IMITATOR *)
	imitator_mode : imitator_mode;
	(* Mode with parametric constraints (clock elimination) in the log file *)
	with_parametric_log : bool;
	(* The name of the program *)
	program_name : string;
}


