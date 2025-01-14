(************************************************************
 *
 *                       IMITATOR
 *
 * Université de Lorraine, CNRS, Inria, LORIA, Nancy, France
 *
 * Module description: Functions that extract information on parsed model (dependency graph of variables / functions, etc.)
 *
 * File contributors : Benjamin L.
 * Created           : 2022/05/18
 *
 ************************************************************)

open ParsingStructure
open ParsingStructureUtilities
open CustomModules

type automaton_name = string
type variable_name = string
type param_name = string
type fun_name = string
type id = int

type local_variable_ref = variable_name * fun_name * id
type param_ref = param_name * fun_name

(* Reference to a program component *)
type component =
    | System_ref
    | Automaton_ref of automaton_name
    | Global_variable_ref of variable_name
    | Local_variable_ref of local_variable_ref
    | Param_ref of param_ref
    | Fun_ref of fun_name

(* A components set *)
module ComponentSet : Set.S with type elt = component

(* Relation between two components a -> b mean a use b *)
type relation = component * component
(* Dependency graph as a list of relations between the components *)
type dependency_graph = component list (* declared components *) * relation list



val dependency_graph : parsed_model -> dependency_graph


(* Get dependency graph as string (dot graphviz format) *)
val string_of_dependency_graph : dependency_graph -> string

(* Get all declared components of model *)
val components_of_model : dependency_graph -> ComponentSet.t

val used_components_of_model : dependency_graph -> ComponentSet.t
val unused_components_of_model : dependency_graph -> ComponentSet.t

val used_functions_of_model : dependency_graph -> StringSet.t
val unused_functions_of_model : dependency_graph -> StringSet.t
val used_variables_of_model : dependency_graph -> StringSet.t
val unused_variables_of_model : dependency_graph -> StringSet.t

(* IMPLEMENT comments if needed *)
(*
val used_local_variables_of_model : dependency_graph -> local_variable_ref list
val unused_local_variables_of_model : dependency_graph -> local_variable_ref list
val used_parameters_of_model : dependency_graph -> param_ref list
val unused_parameters_of_model : dependency_graph -> param_ref list
*)

val assigned_variables_of_fun_def : parsed_fun_definition -> ComponentSet.t