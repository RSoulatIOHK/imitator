open DiscreteExpressions
open OCamlUtilities
open Constants

type variable = int

(* Non-linear custom expression without PPL *)
type nonlinear_inequality = DiscreteExpressions.discrete_arithmetic_expression * DiscreteExpressions.relop * DiscreteExpressions.discrete_arithmetic_expression

type nonlinear_constraint =
  | True_nonlinear_constraint
  | False_nonlinear_constraint
  | Nonlinear_constraint of DiscreteExpressions.discrete_boolean_expression list

(* if all true, it's satisfied *)
let check_nonlinear_inequalities discrete_valuation =
  List.for_all (DiscreteExpressionEvaluator.check_discrete_boolean_expression discrete_valuation)

(* Check if a nonlinear constraint is satisfied *)
let check_nonlinear_constraint discrete_valuation = function
    | True_nonlinear_constraint -> true
    | False_nonlinear_constraint -> false
    | Nonlinear_constraint nonlinear_inequalities -> check_nonlinear_inequalities discrete_valuation nonlinear_inequalities

let is_linear_nonlinear_constraint = function
    | True_nonlinear_constraint
    | False_nonlinear_constraint -> true
    | Nonlinear_constraint nonlinear_inequalities ->
        List.for_all DiscreteExpressions.is_linear_discrete_boolean_expression nonlinear_inequalities

(* Get string of non-linear constraint inequalities with customized strings *)
let customized_string_of_nonlinear_constraint customized_string variable_names = function
    | True_nonlinear_constraint -> customized_string.boolean_string.true_string
    | False_nonlinear_constraint -> customized_string.boolean_string.false_string
    | Nonlinear_constraint nonlinear_constraint ->
	    " " ^
	    (string_of_list_of_string_with_sep
		    customized_string.boolean_string.and_operator
		    (List.rev_map (DiscreteExpressions.customized_string_of_discrete_boolean_expression customized_string variable_names) nonlinear_constraint)
	    )

(* Get string of non-linear constraint inequalities with default strings *)
let string_of_nonlinear_constraint = customized_string_of_nonlinear_constraint global_default_string

