(************************************************************
 *
 *                       IMITATOR
 * 
 * LIPN, Université Paris 13, Sorbonne Paris Cité (France)
 * 
 * Module description: Classical Behavioral Cartography with exhaustive coverage of integer points [AF10]. Shuffled version, used for the distributed cartography. [ACN15]
 * 
 * File contributors : Étienne André
 * Created           : 2016/03/14
 * Last modified     : 2016/03/14
 *
 ************************************************************)


(************************************************************)
(* Modules *)
(************************************************************)
open AlgoCartoGeneric
open AlgoBCCover



(************************************************************)
(* Class definition *)
(************************************************************)
class algoBCShuffle :
	object inherit algoBCCover
		(************************************************************)
		(* Class variables *)
		(************************************************************)


		(************************************************************)
		(* Class methods *)
		(************************************************************)
		method algorithm_name : string
		
		method initialize_variables : unit
		
		(** Return a new instance of the algorithm to be iteratively called (typically IM or PRP) *)
		method algorithm_instance : AlgoIMK.algoIMK

		(* Create the initial point for the analysis *)
		method get_initial_point : more_points

		(* Find the next point *)
		method find_next_point : more_points

		method compute_bc_result : Result.imitator_result
end