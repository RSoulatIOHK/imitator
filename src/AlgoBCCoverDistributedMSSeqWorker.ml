(************************************************************
 *
 *                       IMITATOR
 * 
 * Université Paris 13, LIPN, CNRS, France
 * Université de Lorraine, CNRS, Inria, LORIA, Nancy, France
 * 
 * Module description: Classical Behavioral Cartography with exhaustive coverage of integer points [AF10]. Distribution mode: master-worker with sequential distribution of points. [ACE14]
 * Worker algorithm
 * 
 * File contributors : Étienne André
 * Created           : 2016/03/10
 *
 ************************************************************)


(************************************************************)
(************************************************************)
(* Modules *)
(************************************************************)
(************************************************************)
open AlgoBCCoverDistributedMSPointBasedWorker

(************************************************************)
(************************************************************)
(* Internal exceptions *)
(************************************************************)
(************************************************************)


(************************************************************)
(************************************************************)
(* Class definition *)
(************************************************************)
(************************************************************)
class algoBCCoverDistributedMSSeqWorker (v0 : HyperRectangle.hyper_rectangle) (step : NumConst.t) (algo_instance_function : (PVal.pval -> AlgoStateBased.algoStateBased)) (tiles_manager_type : AlgoCartoGeneric.tiles_storage) =
	object (self) inherit AlgoBCCoverDistributedMSPointBasedWorker.algoBCCoverDistributedMSPointBasedWorker v0 step algo_instance_function tiles_manager_type as super
	
	(************************************************************)
	(* Class variables *)
	(************************************************************)

	
	
	(************************************************************)
	(* Class methods *)
	(************************************************************)

	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	(* Name of the algorithm *)
	(*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*)
	method algorithm_name = "BC (full cov) distr MS seq WORKER#" ^ (string_of_int worker_rank) ^ ""

	

(************************************************************)
(************************************************************)
end;;
(************************************************************)
(************************************************************)
