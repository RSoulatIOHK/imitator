(*****************************************************************
 *
 *                     IMITATOR II
 * 
 * Laboratoire Specification et Verification (ENS Cachan & CNRS, France)
 * Author:        Etienne Andre
 * Created:       2012/05/10
 * Last modified: 2014/03/15
 *
 ****************************************************************)
 
open Global


type distribution_mode =
	| Non_distributed
	| Distributed



class imitator_options :
	object
(*		val mutable nb_args : int 
		val mutable acyclic : bool ref
		val mutable branch_and_bound : bool ref
		val mutable cart : bool ref
		val mutable cartonly : bool ref
		val mutable check_point : bool ref
		val mutable completeIM : bool ref
		val mutable counterex : bool ref
(* 		val mutable dynamic : bool ref *)
		val mutable distributed : distribution_mode ref
		val mutable dynamic_clock_elimination : bool ref
		val mutable efim : bool ref
		val mutable fancy : bool ref
		val mutable file : string ref
		val mutable files_prefix : string ref
(* 		val mutable forcePi0 : bool ref *)
		val mutable fromGML : bool ref
		val mutable imitator_mode : Global.imitator_mode ref
		val mutable inclusion : bool ref
		val mutable nb_args : int
		val mutable merge : bool ref
		val mutable merge_before : bool ref
		val mutable no_random : bool ref
		val mutable pi0file : string ref
		val mutable pi_compatible : bool ref
		val mutable post_limit : int option ref
		val mutable pta2clp : bool ref
		val mutable pta2gml : bool ref
		val mutable pta2jpg : bool ref
		val mutable states_limit : int option ref
		val mutable statistics : bool ref
		val mutable step : NumConst.t ref
		val mutable sync_auto_detection : bool ref
		val mutable time_limit : int option ref
		val mutable timed_mode : bool ref
		val mutable tree : bool ref
		val mutable union : bool ref
		val mutable with_dot : bool ref
		val mutable with_graphics_source : bool ref
		val mutable with_log : bool ref
		val mutable with_parametric_log : bool ref*)
		
		method acyclic : bool
		method acyclic_unset : unit
		method branch_and_bound : bool
		method branch_and_bound_unset : unit
		method cart : bool
		method cartonly : bool
		method check_point : bool
		method completeIM : bool
		method counterex : bool
(* 		method dynamic : bool *)
		method distribution_mode : distribution_mode
		method dynamic_clock_elimination : bool
		method efim : bool
		method fancy : bool
		method file : string
		method files_prefix : string
(* 		method forcePi0 : bool *)
		method fromGML : bool
		method imitator_mode : imitator_mode
		method inclusion : bool
		method nb_args : int
		method merge : bool
		method merge_before : bool
		method no_random : bool
		method pi0file : string
		method pi_compatible : bool
		method post_limit : int option
		method pta2clp : bool
		method pta2gml : bool
		method pta2jpg : bool
		method states_limit : int option
		method statistics : bool
		method step : NumConst.t
		method sync_auto_detection : bool
		method time_limit : int option
		method timed_mode : bool
		method tree : bool
		method union : bool
		method with_dot : bool
		method with_graphics_source : bool
		method with_log : bool
		method with_parametric_log : bool
		method parse : unit
		
		(* Recall options *)
		method recall : unit -> unit
		
end