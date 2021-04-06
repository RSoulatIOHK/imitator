(************************************************************
 *
 *                       IMITATOR
 *
 * Université de Lorraine, CNRS, Inria, LORIA, Nancy, France
 *
 * Module description: arithmetic and Boolean expressions on discrete variables
 *
 * File contributors : Étienne André, Dylan Marinho
 * Created           : 2019/12/10
 * Last modified     : 2021/03/05
 *
 ************************************************************)

(* Expression type *)
type expression_type =
    | Expression_type_discrete_bool of DiscreteValue.var_type_discrete
    | Expression_type_discrete_arithmetic of DiscreteValue.var_type_discrete_number

(************************************************************)
(************************************************************)
(** Operators *)
(************************************************************)
(************************************************************)

(** Boolean operators *)

type relop = OP_L | OP_LEQ | OP_EQ | OP_NEQ | OP_GEQ | OP_G


(************************************************************)
(************************************************************)
(** Valuation *)
(************************************************************)
(************************************************************)
type discrete_valuation = Automaton.discrete_index -> DiscreteValue.discrete_value


(************************************************************)
(************************************************************)
(** Arithmetic expressions for discrete variables *)
(************************************************************)
(************************************************************)
type discrete_arithmetic_expression =
	| DAE_plus of discrete_arithmetic_expression * discrete_term
	| DAE_minus of discrete_arithmetic_expression * discrete_term
	| DAE_term of discrete_term

and discrete_term =
	| DT_mul of discrete_term * discrete_factor
	| DT_div of discrete_term * discrete_factor
	| DT_factor of discrete_factor

and discrete_factor =
	| DF_variable of Automaton.variable_index
	| DF_constant of DiscreteValue.discrete_value
	| DF_expression of discrete_arithmetic_expression
	| DF_unary_min of discrete_factor

(************************************************************)
(************************************************************)
(************************************************************)
(** Boolean expressions for discrete variables *)
(************************************************************)
(************************************************************)

(** Boolean expression *)
type boolean_expression =
	| True_bool (** True *)
	| False_bool (** False *)
	| Not_bool of boolean_expression (** Negation *)
	| And_bool of boolean_expression * boolean_expression (** Conjunction *)
	| Or_bool of boolean_expression * boolean_expression (** Disjunction *)
	| Discrete_boolean_expression of discrete_boolean_expression

and discrete_boolean_expression =
	(** Discrete arithmetic expression of the form Expr ~ Expr *)
	| Expression of discrete_arithmetic_expression * relop * discrete_arithmetic_expression
	(** Discrete arithmetic expression of the form 'Expr in [Expr, Expr ]' *)
	| Expression_in of discrete_arithmetic_expression * discrete_arithmetic_expression * discrete_arithmetic_expression
	(** Parsed boolean expression of the form Expr ~ Expr, with ~ = { &, | } or not (Expr) *)
	| Boolean_expression of boolean_expression
	(** discrete variable in boolean expression *)
	| DB_variable of Automaton.variable_index
	(** discrete constant in boolean expression *)
	| DB_constant of DiscreteValue.discrete_value


type typed_boolean_expression = boolean_expression * DiscreteValue.var_type_discrete
type typed_discrete_boolean_expression = discrete_boolean_expression * DiscreteValue.var_type_discrete

(****************************************************************)
(** Global expression *)
(****************************************************************)
type global_expression =
    (* A typed expression *)
    | Arithmetic_expression of discrete_arithmetic_expression * DiscreteValue.var_type_discrete_number
    | Bool_expression of typed_boolean_expression


val string_of_expression_type : expression_type -> string
(* Check if a variable type is compatible with an expression type *)
val is_var_type_discrete_compatible_with_expr_type : DiscreteValue.var_type_discrete -> expression_type -> bool
(* Check if a variable type is compatible with an expression type *)
val is_var_type_compatible_with_expr_type : DiscreteValue.var_type -> expression_type -> bool
(* Check if expression type is a boolean expression type *)
val is_bool_expression_type : expression_type -> bool
(* Check if expression type is a unknown number type *)
val is_unknown_number_expression_type : expression_type -> bool
(* Check if expression type is a bool of unknown number type *)
val is_bool_of_unknown_number_expression_type : expression_type -> bool

(* TODO benjamin comment all below *)

val eval_discrete_relop : relop -> Automaton.discrete_value -> Automaton.discrete_value -> bool

(************************************************************)
(** Evaluate global expressions with a valuation            *)
(************************************************************)
val eval_global_expression : discrete_valuation -> global_expression -> DiscreteValue.discrete_value

(************************************************************)
(** Evaluate a discrete arithmetic expression with a valuation *)
(************************************************************)
val eval_discrete_arithmetic_expression : discrete_valuation -> discrete_arithmetic_expression -> DiscreteValue.discrete_value

(************************************************************)
(** Evaluate a rational expression with a valuation *)
(************************************************************)
val eval_rational_expression : discrete_valuation -> discrete_arithmetic_expression -> NumConst.t

(************************************************************)
(** Check whether a Boolean expression evaluates to true when valuated with a valuation *)
(************************************************************)
val is_boolean_expression_satisfied : discrete_valuation -> boolean_expression -> bool
val check_discrete_boolean_expression : discrete_valuation -> discrete_boolean_expression -> bool


(* TODO benjamin comment end *)



(* String *)
val customized_string_of_global_expression : Constants.customized_string -> (Automaton.variable_index -> string) -> global_expression -> string
val string_of_global_expression : (Automaton.variable_index -> string) -> global_expression -> string

val customized_string_of_arithmetic_expression : Constants.customized_boolean_string -> (Automaton.variable_index -> string) -> discrete_arithmetic_expression -> string
val string_of_arithmetic_expression : (Automaton.variable_index -> string) -> discrete_arithmetic_expression -> string

val customized_string_of_boolean_expression : Constants.customized_boolean_string -> (Automaton.variable_index -> string) -> boolean_expression -> string
val string_of_boolean_expression : (Automaton.variable_index -> string) -> boolean_expression -> string

val customized_string_of_discrete_boolean_expression : Constants.customized_boolean_string -> (Automaton.variable_index -> string) -> discrete_boolean_expression -> string
val string_of_discrete_boolean_expression : (Automaton.variable_index -> string) -> discrete_boolean_expression -> string

val customized_string_of_typed_discrete_boolean_expression : Constants.customized_boolean_string -> (Automaton.variable_index -> string) -> discrete_boolean_expression * DiscreteValue.var_type_discrete -> string
val customized_string_of_arithmetic_expression_for_jani : Constants.customized_string -> (Automaton.variable_index -> string) -> discrete_arithmetic_expression -> string
val string_of_arithmetic_expression_for_jani : (Automaton.variable_index -> string) -> discrete_arithmetic_expression -> string

val customized_string_of_discrete_boolean_expression_for_jani : Constants.customized_string -> (Automaton.variable_index -> string) -> discrete_boolean_expression -> string
val string_of_discrete_boolean_expression_for_jani : (Automaton.variable_index -> string) -> discrete_boolean_expression -> string
