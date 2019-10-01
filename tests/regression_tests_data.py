#!/usr/bin/python
# -*- coding: utf-8 -*-
#************************************************************
#
#                       IMITATOR
#
#             Data for non-regression tests
#
# Université Paris 13, LIPN, CNRS, France
#
# File description: non-regression tests data
#
# File contributors : Étienne André, Jaime Arias
#
# Created           : 2015/10/23
# Last modified     : 2019/09/10
#************************************************************



#************************************************************
# TESTS TO CARRY
#************************************************************
tests = [

	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
	# SYNTACTIC TESTS
	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/09
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test the L/U-nature (L-PTA)',
		'input_files': ['testL.imi'],
		'options'    : '-mode checksyntax -output-result',
		'expectations' : [
			{'file': 'testL.res' , 'content' : """
L/U subclass                            : L-PTA
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/09
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test the L/U-nature (U-PTA)',
		'input_files': ['testU.imi'],
		'options'    : '-mode checksyntax -output-result',
		'expectations' : [
			{'file': 'testU.res' , 'content' : """
L/U subclass                            : U-PTA
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/09
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test the L/U-nature (L/U-PTA)',
		'input_files': ['testLU.imi'],
		'options'    : '-mode checksyntax -output-result',
		'expectations' : [
			{'file': 'testLU.res' , 'content' : """
L/U subclass                            : L/U-PTA
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/09
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test the L/U-nature (none)',
		'input_files': ['testNotLU.imi'],
		'options'    : '-mode checksyntax -output-result',
		'expectations' : [
			{'file': 'testNotLU.res' , 'content' : """
L/U subclass                            : not L/U
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/09
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test the L/U-nature (flip-flop: U)',
		'input_files': ['flipflop.imi'],
		'options'    : '-mode checksyntax -output-result',
		'expectations' : [
			{'file': 'flipflop.res' , 'content' : """
L/U subclass                            : U-PTA
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/09
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test the L/U-nature (JR15: L/U)',
		'input_files': ['JLR-TACAS13.imi'],
		'options'    : '-mode checksyntax -output-result',
		'expectations' : [
			{'file': 'JLR-TACAS13.res' , 'content' : """
L/U subclass                            : L/U-PTA
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/09
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test the detection of silent actions: no',
		'input_files': ['testLU.imi'],
		'options'    : '-mode checksyntax -output-result',
		'expectations' : [
			{'file': 'testLU.res' , 'content' : """
Has silent actions?                            : false
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/09
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test the detection of silent actions: yes',
		'input_files': ['testNotLU.imi'],
		'options'    : '-mode checksyntax -output-result',
		'expectations' : [
			{'file': 'testNotLU.res' , 'content' : """
Has silent actions?                            : true
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/09
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test the detection of silent actions: JR15',
		'input_files': ['JLR-TACAS13.imi'],
		'options'    : '-mode checksyntax -output-result',
		'expectations' : [
			{'file': 'JLR-TACAS13.res' , 'content' : """
Has silent actions?                            : true
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/09
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test the detection of strong determinism: yes',
		'input_files': ['testLU.imi'],
		'options'    : '-mode checksyntax -output-result',
		'expectations' : [
			{'file': 'testLU.res' , 'content' : """
Is strongly deterministic?              : true
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/09
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test the detection of strong determinism: yes',
		'input_files': ['testStrongDet.imi'],
		'options'    : '-mode checksyntax -output-result',
		'expectations' : [
			{'file': 'testStrongDet.res' , 'content' : """
Is strongly deterministic?              : true
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/09
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test the detection of strong determinism: yes',
		'input_files': ['testStrongDet2.imi'],
		'options'    : '-mode checksyntax -output-result',
		'expectations' : [
			{'file': 'testStrongDet2.res' , 'content' : """
Is strongly deterministic?              : true
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/09
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test the detection of strong determinism: no',
		'input_files': ['testNotStrongDet.imi'],
		'options'    : '-mode checksyntax -output-result',
		'expectations' : [
			{'file': 'testNotStrongDet.res' , 'content' : """
Is strongly deterministic?              : false
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	##------------------------------------------------------------
	{
		'purpose'    : 'Test variable elimination in Boolean expressions',
		'input_files': ['testConditions.imi'],
		'options'    : '-mode statespace -output-states',
		'expectations' : [
			{'file': 'testConditions-statespace.states' , 'content' : """
  STATE 0:
  pta: l1, i = 0, j = 0, l = 0 ==>
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	##------------------------------------------------------------]

	,

	##------------------------------------------------------------
	{
		'purpose'    : 'Test evaluation of <if> branch in conditional update',
		'input_files': ['testConditions.imi'],
		'options'    : '-mode statespace -output-states',
		'expectations' : [
			{'file': 'testConditions-statespace.states' , 'content' : """
	STATE 1:
	pta: l2, i = 0, j = 0, l = 15 ==>
	& x >= 0
	& p = 1
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	##------------------------------------------------------------]

	,

	##------------------------------------------------------------
	{
		'purpose'    : 'Test evaluation of <else> branch in conditional update',
		'input_files': ['testConditions.imi'],
		'options'    : '-mode statespace -output-states',
		'expectations' : [
			{'file': 'testConditions-statespace.states' , 'content' : """
	STATE 2:
  pta: l1, i = 2, j = 0, l = 15 ==>
	& x >= 2
	& p = 1
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	##------------------------------------------------------------]

	,

	##------------------------------------------------------------
	{
		'purpose'    : 'Test include files [1]',
		'input_files': ['tests_include_model/example-include-1a.imi'],
		'options'    : '-PTA2IMI -no-var-autoremove',
		'expectations' : [
			{'file': 'tests_include_model/example-include-1a-regenerated.imi' , 'content' : """
var
	x
		: clock;

	i
		: discrete;

	p
		: parameter;


(************************************************************)
 automaton pta2
(************************************************************)
 synclabs: a;

loc l1: invariant True
	when  x = 1 do {x := 0}  sync a goto l1;
 end (* pta2 *)
(************************************************************)


(************************************************************)
 automaton pta1
(************************************************************)
 synclabs: a;

loc l1: invariant True
	when  x = 1 do {x := 0}  sync a goto l1;
 end (* pta1 *)
(************************************************************)


(************************************************************)
(* Initial state *)
(************************************************************)

init := True
	(*------------------------------------------------------------*)
	(* Initial location *)
	(*------------------------------------------------------------*)
	& loc[pta2] = l1
	& loc[pta1] = l1

	(*------------------------------------------------------------*)
	(* Initial discrete assignments *)
	(*------------------------------------------------------------*)
	& i = 0

	(*------------------------------------------------------------*)
	(* Initial constraint *)
	(*------------------------------------------------------------*)
	 &  p >= 0
& x = 0

;

(************************************************************)
(* Property specification *)
(************************************************************)

property := unreachable loc[pta1] = l1




(************************************************************)
(* The end *)
(************************************************************)
end
			"""
			} # end result file
			,
		] # end expectations
	} # end test case
	##------------------------------------------------------------]

	,

	##------------------------------------------------------------
	{
		'purpose'    : 'Test include files [2]',
		'input_files': ['tests_include_model/example-include-2a.imi'],
		'options'    : '-PTA2IMI -no-var-autoremove',
		'expectations' : [
			{'file': 'tests_include_model/example-include-2a-regenerated.imi' , 'content' : """
var
	x, y
		: clock;

	i, j
		: discrete;

	p
		: parameter;


(************************************************************)
 automaton pta2
(************************************************************)
 synclabs: a;

loc l1: invariant True
	when  y = 1 do {y := p}  sync a goto l1;
 end (* pta2 *)
(************************************************************)


(************************************************************)
 automaton pta1
(************************************************************)
 synclabs: a;

loc l1: invariant True
	when  p + 1 = x do {x := 0}  sync a goto l1;
 end (* pta1 *)
(************************************************************)


(************************************************************)
(* Initial state *)
(************************************************************)

init := True
	(*------------------------------------------------------------*)
	(* Initial location *)
	(*------------------------------------------------------------*)
	& loc[pta2] = l1
	& loc[pta1] = l1

	(*------------------------------------------------------------*)
	(* Initial discrete assignments *)
	(*------------------------------------------------------------*)
	& i = 0
	& j = 0

	(*------------------------------------------------------------*)
	(* Initial constraint *)
	(*------------------------------------------------------------*)
	 &  p >= 1
& x = 0
& y = 0

;

(************************************************************)
(* Property specification *)
(************************************************************)

property := unreachable loc[pta1] = l1 & loc[pta2] = l1




(************************************************************)
(* The end *)
(************************************************************)
end
			"""
			} # end result file
			,
		] # end expectations
	} # end test case
	##------------------------------------------------------------]

	,

	##------------------------------------------------------------
	{
		'purpose'    : 'Test include files [3]',
		'input_files': ['tests_include_model/example-include-3a.imi'],
		'options'    : '-PTA2IMI -no-var-autoremove',
		'expectations' : [
			{'file': 'tests_include_model/example-include-3a-regenerated.imi' , 'content' : """
var
	x, y
		: clock;

	i, j
		: discrete;

	p
		: parameter;


(************************************************************)
 automaton pta2
(************************************************************)
 synclabs: a;

loc l1: invariant True
	when  y = 1 do {y := p}  sync a goto l1;
 end (* pta2 *)
(************************************************************)


(************************************************************)
 automaton pta1
(************************************************************)
 synclabs: a;

loc l1: invariant True
	when  p + 1 = x do {x := 0}  sync a goto l1;
 end (* pta1 *)
(************************************************************)


(************************************************************)
(* Initial state *)
(************************************************************)

init := True
	(*------------------------------------------------------------*)
	(* Initial location *)
	(*------------------------------------------------------------*)
	& loc[pta2] = l1
	& loc[pta1] = l1

	(*------------------------------------------------------------*)
	(* Initial discrete assignments *)
	(*------------------------------------------------------------*)
	& i = 0
	& j = 0

	(*------------------------------------------------------------*)
	(* Initial constraint *)
	(*------------------------------------------------------------*)
	 &  p >= 1
& x = 0
& y = 0

;

(************************************************************)
(* Property specification *)
(************************************************************)

property := unreachable loc[pta1] = l1 & loc[pta2] = l1




(************************************************************)
(* The end *)
(************************************************************)
end
			"""
			} # end result file
			,
		] # end expectations
	} # end test case
	##------------------------------------------------------------]

	,

	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
	# STATE SPACE GENERATION
	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

	#------------------------------------------------------------
	{
		# Test version             : TODO
		# Test since               : TODO
		# Test for IMITATOR version: TODO
		'purpose'    : 'Test the state space',
		'input_files': ['flipflop.imi'],
		'options'    : '-mode statespace -output-states -no-var-autoremove', #TODO: re-do without '-no-var-autoremove'
		'expectations' : [
			{'file': 'flipflop-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  input: Input0, g1: G10011, g2: G2101, g3: G30011, g4: G410, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 5 >= s
& dG3_u >= 8
& dG4_u >= 3
& s >= 0
& ckG1 >= s
& ckG2 >= s
& ckG3 >= s
& ckG4 >= s

  Projection onto the parameters:
   dG4_u >= 3
& dG3_u >= 8

  /************************************************************/
  STATE 1:
  input: Input1, g1: G11011, g2: G2101, g3: G30011, g4: G410, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 12 >= s
& dG3_u >= 8
& dG4_u >= 3
& s >= 5
& ckG2 >= s
& ckG3 >= s
& ckG4 >= s
& s = 5 + ckG1

  Projection onto the parameters:
   dG4_u >= 3
& dG3_u >= 8

  /************************************************************/
  STATE 2:
  input: Input1, g1: G11010, g2: G2001, g3: G30011, g4: G410, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 15 >= s
& dG3_u >= 8
& dG4_u >= 3
& s >= 12
& ckG2 >= s
& ckG3 >= s
& ckG4 >= s
& s = 5 + ckG1

  Projection onto the parameters:
   dG4_u >= 3
& dG3_u >= 8

  /************************************************************/
  STATE 3:
  input: Input2, g1: G11110, g2: G2011, g3: G30111, g4: G410, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& dG3_u + 15 >= s
& 32 >= s
& dG3_u >= 8
& dG4_u >= 3
& ckG2 >= s
& s >= 15
& ckG4 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 8
& dG4_u >= 3

  /************************************************************/
  STATE 4:
  input: Input3, g1: G10110, g2: G2011, g3: G30111, g4: G410, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 39 >= s
& dG3_u + 15 >= s
& dG4_u >= 3
& ckG2 >= s
& s >= 32
& ckG4 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 17
& dG4_u >= 3

  /************************************************************/
  STATE 5:
  input: Input2, g1: G11110, g2: G2011, g3: G30110, g4: G400, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 32 >= s
& dG3_u + ckG4 + 15 >= s
& dG4_u >= 3
& s >= 23 + ckG4
& ckG4 >= 0
& ckG2 >= s
& dG4_u >= ckG4
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 8
& dG4_u >= 3

  /************************************************************/
  STATE 6:
  input: Input4, g1: G10010, g2: G2001, g3: G30011, g4: G410, automatically_generated_observer: loc_AutoGen_obs_2 ==>
& dG3_u >= 24
& dG4_u >= 3
& ckG2 >= 39
& ckG4 >= 39
& s = 0
& ckG1 = 0
& ckG3 = 24

  Projection onto the parameters:
   dG4_u >= 3
& dG3_u >= 24

  /************************************************************/
  STATE 7:
  input: Input3, g1: G10110, g2: G2011, g3: G30110, g4: G400, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 39 >= s
& dG3_u + ckG4 + 15 >= s
& dG4_u >= 3
& s >= 32 + ckG4
& ckG4 >= 0
& ckG2 >= s
& dG4_u >= ckG4
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 17
& dG4_u >= 3

  /************************************************************/
  STATE 8:
  input: Input3, g1: G10110, g2: G2011, g3: G30110, g4: G400, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 39 >= s
& dG3_u + ckG4 + 15 >= s
& dG4_u >= ckG4
& dG4_u >= 3
& ckG2 >= s
& s >= 32
& s >= 23 + ckG4
& ckG4 + 32 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u + dG4_u >= 17
& dG4_u >= 3
& dG3_u >= 8

  /************************************************************/
  STATE 9:
  input: Input2, g1: G11110, g2: G2011, g3: G31110, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& dG3_u + ckG4 + 15 >= s
& dG4_u >= 3
& s >= 23 + ckG4
& ckG4 >= 3
& ckG2 >= s
& 32 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 8
& dG4_u >= 3

  /************************************************************/
  STATE 10:
  input: Input4, g1: G10010, g2: G2001, g3: G30010, g4: G400, automatically_generated_observer: loc_AutoGen_obs_2 ==>
& dG3_u + ckG4 >= 24
& dG4_u >= ckG4
& dG4_u >= 3
& ckG2 >= 39
& ckG4 >= 0
& 7 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 0

  Projection onto the parameters:
   dG3_u + dG4_u >= 24
& dG3_u >= 17
& dG4_u >= 3

  /************************************************************/
  STATE 11:
  input: Input3, g1: G10110, g2: G2011, g3: G31110, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& dG3_u + ckG4 + 15 >= s
& dG4_u >= 3
& s >= 32 + ckG4
& ckG4 >= 3
& ckG2 >= s
& 39 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 17
& dG4_u >= 3

  /************************************************************/
  STATE 12:
  input: Input4, g1: G10010, g2: G2001, g3: G30010, g4: G400, automatically_generated_observer: loc_AutoGen_obs_2 ==>
& dG3_u + ckG4 >= 24
& dG4_u >= ckG4
& ckG2 >= 39
& ckG4 >= 7
& 16 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 0

  Projection onto the parameters:
   dG4_u >= 7
& dG3_u >= 8
& dG3_u + dG4_u >= 24

  /************************************************************/
  STATE 13:
  input: Input3, g1: G10110, g2: G2011, g3: G31110, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& 39 >= s
& dG3_u + ckG4 + 15 >= s
& dG4_u + s >= 32 + ckG4
& dG4_u >= 3
& s >= 32
& s >= 23 + ckG4
& ckG4 >= 3
& ckG2 >= s
& ckG4 + 32 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u + dG4_u >= 17
& dG3_u >= 8
& dG4_u >= 3

  /************************************************************/
  STATE 14:
  input: Input3, g1: G10110, g2: G2011, g3: G31110, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& 39 >= s
& dG3_u + ckG4 + 15 >= s
& dG4_u >= 3
& ckG2 >= s
& s >= 32
& s >= 23 + ckG4
& ckG4 + 29 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 8
& dG4_u >= 3

  /************************************************************/
  STATE 15:
  input: Input4, g1: G10010, g2: G2001, g3: G31010, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& dG3_u + ckG4 >= 24
& dG4_u + 7 >= ckG4
& dG4_u >= 3
& ckG2 >= 39
& ckG4 >= 7
& 16 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 24

  Projection onto the parameters:
   dG3_u + dG4_u >= 17
& dG3_u >= 8
& dG4_u >= 3

  /************************************************************/
  STATE 16:
  input: Input4, g1: G10010, g2: G2001, g3: G31010, g4: G401, automatically_generated_observer: loc_AutoGen_obs_2 ==>
& dG3_u + ckG4 >= 24
& dG4_u >= ckG4
& ckG2 >= 39
& ckG4 >= 7
& 16 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 0

  Projection onto the parameters:
   dG4_u >= 7
& dG3_u >= 8
& dG3_u + dG4_u >= 24

  /************************************************************/
  STATE 17:
  input: Input4, g1: G10010, g2: G2001, g3: G31010, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& dG3_u + ckG4 >= 24
& dG4_u >= 3
& ckG2 >= 39
& ckG4 >= 3
& 7 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 24

  Projection onto the parameters:
   dG3_u >= 17
& dG4_u >= 3

  /************************************************************/
  STATE 18:
  input: Input4, g1: G10010, g2: G2001, g3: G31010, g4: G401, automatically_generated_observer: loc_AutoGen_obs_2 ==>
& dG3_u + ckG4 >= 24
& dG4_u >= ckG4
& ckG2 >= 39
& ckG4 >= 3
& 7 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 0

  Projection onto the parameters:
   dG4_u >= 3
& dG3_u >= 17
& dG3_u + dG4_u >= 24

  /************************************************************/
  STATE 19:
  input: Input4, g1: G10010, g2: G2001, g3: G31010, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& dG3_u + ckG4 >= 24
& dG4_u >= 3
& ckG2 >= 39
& ckG4 >= 10
& 16 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 24

  Projection onto the parameters:
   dG3_u >= 8
& dG4_u >= 3

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1 via "dUp"
  s_1 -> s_2 via "qG1Down"
  s_2 -> s_3 via "ckUp"
  s_3 -> s_4 via "dDown"
  s_3 -> s_5 via "qG3Down"
  s_4 -> s_6 via "ckDown"
  s_4 -> s_7 via "qG3Down"
  s_5 -> s_8 via "dDown"
  s_5 -> s_9 via "qUp"
  s_7 -> s_10 via "ckDown"
  s_7 -> s_11 via "qUp"
  s_8 -> s_12 via "ckDown"
  s_8 -> s_13 via "qUp"
  s_9 -> s_14 via "dDown"
  s_10 -> s_18 via "qUp"
  s_11 -> s_17 via "ckDown"
  s_12 -> s_16 via "qUp"
  s_13 -> s_15 via "ckDown"
  s_14 -> s_19 via "ckDown"
			"""
			} #end statespace file
		] # end expectations
	} # end test case
	,
	#------------------------------------------------------------
	{
		# Test version: 2.11
		# Test since  : 2019/03/07
		'purpose'    : 'Test state space with projection',
		'input_files': ['testProjectP.imi'],
		'options'    : '-mode statespace -output-states',
		'expectations' : [
			{'file': 'testProjectP-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l1 ==>
& pabs >= 0
& p1 >= x
& p3 >= 0
& x >= 0
& x = xabs

  Projection onto the parameters:
   p3 >= 0
& p1 >= 0
& pabs >= 0

  Projection onto selected parameters {pabs}:
   pabs >= 0

  /************************************************************/
  STATE 1:
  pta: l2 ==>
& pabs >= 0
& p1 >= 0
& p3 >= x
& x >= 0
& p1 + x = xabs

  Projection onto the parameters:
   p3 >= 0
& p1 >= 0
& pabs >= 0

  Projection onto selected parameters {pabs}:
   pabs >= 0

  /************************************************************/
  STATE 2:
  pta: lfinal ==>
& pabs >= 0
& p3 >= 0
& pabs = p1
& x = 0
& pabs = xabs

  Projection onto the parameters:
   p3 >= 0
& p1 >= 0
& pabs = p1

  Projection onto selected parameters {pabs}:
   pabs >= 0

  /************************************************************/
  STATE 3:
  pta: l3 ==>
& 2 >= x
& pabs >= 0
& p1 >= 0
& p3 >= 0
& x >= 0
& p1 + p3 + x = xabs

  Projection onto the parameters:
   p3 >= 0
& p1 >= 0
& pabs >= 0

  Projection onto selected parameters {pabs}:
   pabs >= 0

  /************************************************************/
  STATE 4:
  pta: lfinal ==>
& pabs >= p1
& p1 >= 0
& pabs = p1 + p3
& x = 0
& pabs = xabs

  Projection onto the parameters:
   p3 >= 0
& p1 >= 0
& pabs = p1 + p3

  Projection onto selected parameters {pabs}:
   pabs >= 0

  /************************************************************/
  STATE 5:
  pta: l4 ==>
& 2 >= x
& pabs >= 0
& p1 >= 0
& p3 >= 2
& x >= 0
& p1 + x + 2 = xabs

  Projection onto the parameters:
   p3 >= 2
& p1 >= 0
& pabs >= 0

  Projection onto selected parameters {pabs}:
   pabs >= 0

  /************************************************************/
  STATE 6:
  pta: lfinal ==>
& pabs >= 2
& p3 >= 2
& pabs = 2 + p1
& x = 0
& pabs = xabs

  Projection onto the parameters:
   p3 >= 2
& pabs >= 2
& pabs = 2 + p1

  Projection onto selected parameters {pabs}:
   pabs >= 2

  /************************************************************/
  STATE 7:
  pta: l4 ==>
& 2 >= x
& pabs >= 0
& p1 + p3 + x + 2 >= xabs
& p1 >= 0
& p3 >= 0
& x >= 0
& xabs >= p1 + p3 + x

  Projection onto the parameters:
   p3 >= 0
& p1 >= 0
& pabs >= 0

  Projection onto selected parameters {pabs}:
   pabs >= 0

  /************************************************************/
  STATE 8:
  pta: lfinal ==>
& p1 + p3 + 2 >= pabs
& pabs >= p1 + p3
& p1 >= 0
& p3 >= 0
& x = 0
& pabs = xabs

  Projection onto the parameters:
   p1 + p3 + 2 >= pabs
& pabs >= p1 + p3
& p3 >= 0
& p1 >= 0

  Projection onto selected parameters {pabs}:
   pabs >= 0

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1 via "a"
  s_0 -> s_2 via "a"
  s_1 -> s_3 via "a"
  s_1 -> s_4 via "a"
  s_1 -> s_5 via "b"
  s_1 -> s_6 via "b"
  s_3 -> s_7 via "a"
  s_3 -> s_8 via "a"
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test urgency',
		'input_files': ['testUrgency.imi'],
		'options'    : '-mode statespace -output-states',
		'expectations' : [
			{'file': 'testUrgency-statespace.states' , 'content' : """
		  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_0 via "a"
  s_0 -> s_1 via "b"
  s_0 -> s_2 via "b"
  s_1 -> s_3 via "c"
  s_2 -> s_4 via "b"
  s_2 -> s_4 via "c"
  s_3 -> s_1 via "b"
  s_3 -> s_3 via "a"
  s_4 -> s_4 via "a"
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test synchronization model',
		'input_files': ['testSynchro.imi'],
		'options'    : '-mode statespace -output-states',
		'expectations' : [
			{'file': 'testSynchro-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta1: l1, pta2: l1, pta3: l1 ==>
& 3 >= x
& x >= 0

  Projection onto the parameters:
  True

  /************************************************************/
  STATE 1:
  pta1: l1, pta2: l1, pta3: l2 ==>
& 3 >= x
& x >= 0

  Projection onto the parameters:
  True

  /************************************************************/
  STATE 2:
  pta1: l1, pta2: l1, pta3: l3 ==>
& x >= 0

  Projection onto the parameters:
  True

  /************************************************************/
  STATE 3:
  pta1: l2, pta2: l2, pta3: l3 ==>
& x >= 4

  Projection onto the parameters:
  True

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1 via "c"
  s_1 -> s_2 via "a"
  s_2 -> s_3 via "b"
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test updates (printing)',
		'input_files': ['testUpdates.imi'],
		'options'    : '-PTA2IMI',
		'expectations' : [
			{'file': 'testUpdates-regenerated.imi' , 'content' : """
  urgent loc idle: invariant True
	when True do {x := 1/2*p + x + -7*i + -1, y := y + 1, i := ((3 * i - 1)) / ((5 * i) * i)}  sync a goto idle;
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test updates (state space)',
		'input_files': ['testUpdates.imi'],
		'options'    : '-mode statespace -depth-limit 4 -output-states',
		'expectations' : [
			{'file': 'testUpdates-statespace.states' , 'content' : """

  /************************************************************/
  INITIAL
  STATE 0:
  autom: idle, i = 1 ==>
& p >= 0
& x = 0
& y = 0

  Projection onto the parameters:
   p >= 0

  /************************************************************/
  STATE 1:
  autom: idle, i = 2/5 ==>
& p >= 0
& 5*p = 38 + 10*x
& y = 1

  Projection onto the parameters:
   p >= 0

  /************************************************************/
  STATE 2:
  autom: idle, i = 1/4 ==>
& p >= 0
& 20*p = 131 + 20*x
& y = 2

  Projection onto the parameters:
   p >= 0

  /************************************************************/
  STATE 3:
  autom: idle, i = -4/5 ==>
& p >= 0
& 30*p = 39 + 20*x
& y = 3

  Projection onto the parameters:
   p >= 0
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test clock elimination',
		'input_files': ['loopingTAdyn.imi'],
		'options'    : '-mode statespace -dynamic-elimination -output-states -depth-limit 10', # NOTE: depth-limit is just a safety to avoid yielding a loop if the test fails!
		'expectations' : [
			{'file': 'loopingTAdyn-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l0 ==>
&True

  Projection onto the parameters:
  True

  /************************************************************/
  STATE 1:
  pta: l1 ==>
& x >= 0

  Projection onto the parameters:
  True

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1
  s_1 -> s_1 via "a"
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test discrete variable automatic elimination',
		'input_files': ['testVarElim.imi'],
		'options'    : '-mode statespace -output-states',
		'expectations' : [
			# NOTE: we just parse the beginning of state 1 to check that the variables are properly removed
			{'file': 'testVarElim-statespace.states' , 'content' : """
  STATE 1:
  pta: l1, i = 0, j = 0 ==>
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test absence of discrete variable automatic elimination',
		'input_files': ['testVarElim.imi'],
		'options'    : '-mode statespace -output-states -no-var-autoremove',
		'expectations' : [
			# NOTE: we just parse the beginning of state 1 to check that the variables are properly removed
			{'file': 'testVarElim-statespace.states' , 'content' : """
  STATE 1:
  pta: l1, i = 0, j = 0, k = 0, l = 0 ==>
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF (old version) with bad initial state',
		'input_files': ['testEFdegenerate1.imi'],
		'options'    : '-mode EFold -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFdegenerate1.res' , 'content' : """
BEGIN CONSTRAINT
 p2 >= 0
& p1 >= 0
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 0
Number of transitions                   : 0
Number of computed states               : 0
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF with bad initial state',
		'input_files': ['testEFdegenerate1.imi'],
		'options'    : '-mode EF -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFdegenerate1.res' , 'content' : """
BEGIN CONSTRAINT
False
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 0
Number of transitions                   : 0
Number of computed states               : 0
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF (old version) with bad initial state and some constrained valuations',
		'input_files': ['testEFdegenerate2.imi'],
		'options'    : '-mode EFold -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFdegenerate2.res' , 'content' : """
BEGIN CONSTRAINT
 p1 >= p2
& p2 >= 0
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 0
Number of transitions                   : 0
Number of computed states               : 0
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF with bad initial state and some constrained valuations',
		'input_files': ['testEFdegenerate2.imi'],
		'options'    : '-mode EF -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFdegenerate2.res' , 'content' : """
BEGIN CONSTRAINT
False
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 0
Number of transitions                   : 0
Number of computed states               : 0
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF with the new syntax from 2.10.1',
		'input_files': ['fischer_2.imi'],
		'options'    : '-mode EF -merge -incl -output-result',
		'expectations' : [
			{'file': 'fischer_2.res' , 'content' : """
BEGIN CONSTRAINT
 a >= 0
& b > a
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF (old version) with basic unreachability property for Fischer:3',
		'input_files': ['F3.imi'],
		'options'    : '-mode EFold -merge -incl -output-result',
		'expectations' : [
			{'file': 'F3.res' , 'content' : """
BEGIN CONSTRAINT
 Delta > delta
& delta >= 0
 OR
 Delta > 2*delta
& delta >= 0
END CONSTRAINT
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF with basic unreachability property for Fischer:3',
		'input_files': ['F3.imi'],
		'options'    : '-mode EF -merge -incl -output-result',
		'expectations' : [
			{'file': 'F3.res' , 'content' : """
BEGIN CONSTRAINT
delta >= Delta
    & Delta >= 0
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF with basic unreachability property for Fischer:3 (double-directional inclusion)',
		'input_files': ['F3.imi'],
		'options'    : '-mode EF -merge -incl2 -output-result',
		'expectations' : [
			{'file': 'F3.res' , 'content' : """
BEGIN CONSTRAINT
delta >= Delta
    & Delta >= 0
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF with basic unreachability property for Fischer:3 (queueBFS exploration order)',
		'input_files': ['F3.imi'],
		'options'    : '-mode EF -merge -incl -explOrder queueBFS -output-result',
		'expectations' : [
			{'file': 'F3.res' , 'content' : """
BEGIN CONSTRAINT
delta >= Delta
    & Delta >= 0
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF with basic unreachability property for Fischer:3 (layerBFS exploration order) with counterexample',
		'input_files': ['F3.imi'],
		'options'    : '-mode EF -merge -incl -explOrder layerBFS -counterexample -output-result',
		'expectations' : [
			{'file': 'F3.res' , 'content' : """
BEGIN CONSTRAINT
 2*delta >= Delta
& Delta >= 0
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : possible over-approximation
Termination                             : terminated after reaching a target state (some states may have been unexplored)
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF with basic unreachability property for Fischer:3 (queueBFS exploration order) with counterexample',
		'input_files': ['F3.imi'],
		'options'    : '-mode EF -merge -incl -explOrder queueBFS -counterexample -output-result',
		'expectations' : [
			{'file': 'F3.res' , 'content' : """
BEGIN CONSTRAINT
 2*delta >= Delta
& Delta >= 0
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : possible over-approximation
Termination                             : terminated after reaching a target state (some states may have been unexplored)
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF (old version) with complex unreachability property',
		'input_files': ['coffeeDrinker-TACAS.imi'],
		'options'    : '-mode EFold -merge -output-result',
		'expectations' : [
			{'file': 'coffeeDrinker-TACAS.res' , 'content' : """
BEGIN CONSTRAINT
 15 >= p_add_sugar
& p_button > 0
& p_add_sugar + p_coffee >= 15
& p_add_sugar >= 3*p_button
& p_coffee > 0
 OR
 p_add_sugar + p_coffee >= 15
& p_button >= 5
& 15 >= p_add_sugar
& p_coffee > 0
& p_add_sugar >= 2*p_button
 OR
 3*p_button >= p_add_sugar + p_coffee
& p_add_sugar >= 2*p_button
& 15 >= p_add_sugar + p_coffee
& p_coffee > 0
 OR
 5 >= p_button
& p_button > 0
& p_add_sugar >= 15
& p_coffee > 0
 OR
 15 >= 2*p_button
& p_button >= 5
& p_add_sugar >= 15
& p_coffee > 0
 OR
 p_add_sugar + p_coffee >= 15
& p_add_sugar >= p_button
& 15 >= p_add_sugar
& p_coffee > 0
& 2*p_button >= 15
 OR
 p_add_sugar >= p_button
& p_coffee > 0
& 15 >= p_add_sugar + p_coffee
& 2*p_button >= p_add_sugar + p_coffee
 OR
 p_coffee > 0
& 15 >= p_add_sugar
& p_add_sugar > 0
& p_add_sugar + p_coffee >= 15
& p_button >= 15
 OR
 p_add_sugar > 0
& 15 >= p_add_sugar + p_coffee
& p_coffee > 0
& p_button >= p_add_sugar + p_coffee
 OR
 2*p_button >= 15
& 15 >= p_button
& p_add_sugar >= 15
& p_coffee > 0
 OR
 p_button >= 15
& p_coffee > 0
& p_add_sugar >= 15
END CONSTRAINT
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF with complex unreachability property',
		'input_files': ['coffeeDrinker-TACAS.imi'],
		'options'    : '-mode EF -merge -output-result',
		'expectations' : [
			{'file': 'coffeeDrinker-TACAS.res' , 'content' : """
BEGIN CONSTRAINT
 p_add_sugar > 0
& 2*p_button > p_add_sugar
& p_add_sugar + p_coffee > 2*p_button
& 15 > 2*p_button
OR
  p_add_sugar >= 2*p_button
& p_add_sugar + p_coffee > 3*p_button
& 3*p_button > p_add_sugar
& 5 > p_button
OR
  p_add_sugar > 0
& 2*p_button >= 15
& p_add_sugar + p_coffee > 15
& 15 > p_button
& p_button > p_add_sugar
OR
  2*p_button >= p_add_sugar + p_coffee
& p_add_sugar > 0
& p_add_sugar + p_coffee > p_button
& p_button > p_add_sugar
& 15 >= p_add_sugar + p_coffee
OR
  15 > p_add_sugar + p_coffee
& p_coffee > 0
& p_button > 0
& 5 > p_button
& p_add_sugar >= 3*p_button
END CONSTRAINT
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF (old version) with observer + depth-limit + project-result (quite basic)',
		'input_files': ['coffeeDrinker-TACAS-within.imi'],
		'options'    : '-mode EFold -merge -depth-limit 10 -output-result',
		'expectations' : [
			{'file': 'coffeeDrinker-TACAS-within.res' , 'content' : """
BEGIN CONSTRAINT
 p_coffee > 0
END CONSTRAINT
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test EF with observer + depth-limit + project-result (quite basic)',
		'input_files': ['coffeeDrinker-TACAS-within.imi'],
		'options'    : '-mode EF -merge -depth-limit 10 -output-result',
		'expectations' : [
			{'file': 'coffeeDrinker-TACAS-within.res' , 'content' : """
BEGIN CONSTRAINT
 False
END CONSTRAINT
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/05/30
		# Test for IMITATOR version: 2.11
		'purpose'    : 'Test EFunsafe',
		'input_files': ['testEFcounterex.imi'],
		'options'    : '-mode EFunsafe -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFcounterex.res' , 'content' : """
BEGIN CONSTRAINT
 p = 1
 OR
 p = 2
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/05/30
		# Test for IMITATOR version: 2.11
		'purpose'    : 'Test EFunsafe with counterexample',
		'input_files': ['testEFcounterex.imi'],
		'options'    : '-mode EFunsafe -merge -incl -counterexample -output-result',
		'expectations' : [
			{'file': 'testEFcounterex.res' , 'content' : """
BEGIN CONSTRAINT
 p = 1
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : possible under-approximation
Termination                             : terminated after reaching a target state (some states may have been unexplored)
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFmin on a toy example',
		'input_files': ['testEFmin.imi'],
		'options'    : '-mode EFmin -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFmin.res' , 'content' : """
BEGIN CONSTRAINT
 p >= 2
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 10
Number of transitions                   : 9
Number of computed states               : 12
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFmax on a toy example',
		'input_files': ['testEFmax.imi'],
		'options'    : '-mode EFmax -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFmax.res' , 'content' : """
BEGIN CONSTRAINT
 p >= 0
& 11 >= p
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 10
Number of transitions                   : 9
Number of computed states               : 20
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmin on a clock-free toy example 1',
		'input_files': ['testEFsynthminParams1.imi'],
		'options'    : '-mode EFsynthmin -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthminParams1.res' , 'content' : """
BEGIN CONSTRAINT
 p1 = 1
& p2 = 2
OR
  p1 = 1
& p2 = 3
OR
  p1 = 1
& p2 = 4
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmin on a clock-free toy example 2',
		'input_files': ['testEFsynthminParams2.imi'],
		'options'    : '-mode EFsynthmin -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthminParams2.res' , 'content' : """
BEGIN CONSTRAINT
 p1 = 1
& p2 = 2
OR
  p1 = 1
& p2 = 3
OR
  p1 = 1
& p2 = 4
OR
  p1 = 1
& p2 = 5
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmin on a clock-free toy example 3',
		'input_files': ['testEFsynthminParams3.imi'],
		'options'    : '-mode EFsynthmin -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthminParams3.res' , 'content' : """
BEGIN CONSTRAINT
 3*p1 > 1
& 1 > p1
& p2 = 4
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmin on a clock-free toy example 4',
		'input_files': ['testEFsynthminParams4.imi'],
		'options'    : '-mode EFsynthmin -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthminParams4.res' , 'content' : """
BEGIN CONSTRAINT
 3*p1 > 1
& 1 > p1
& 2*p1 = p2
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmin on a clock-free toy example 5',
		'input_files': ['testEFsynthminParams5.imi'],
		'options'    : '-mode EFsynthmin -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthminParams5.res' , 'content' : """
BEGIN CONSTRAINT
 p1 = 0
& p2 = 4
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmin on a clock-free toy example 6',
		'input_files': ['testEFsynthminParams6.imi'],
		'options'    : '-mode EFsynthmin -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthminParams6.res' , 'content' : """
BEGIN CONSTRAINT
 p1 > 0
& p1 + 1 = p2
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmin on a toy example',
		'input_files': ['testEFsynthmin.imi'],
		'options'    : '-mode EFsynthmin -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthmin.res' , 'content' : """
BEGIN CONSTRAINT
 3 >= p2
& p2 >= 2
& p1 = 3
OR
  p1 = 3
& p2 = 1
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmax on a clock-free toy example 1',
		'input_files': ['testEFsynthmaxParams1.imi'],
		'options'    : '-mode EFsynthmax -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthmaxParams1.res' , 'content' : """
BEGIN CONSTRAINT
 p1 = 1
& p2 = 2
OR
  p1 = 1
& p2 = 3
OR
  p1 = 1
& p2 = 4
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmax on a clock-free toy example 2',
		'input_files': ['testEFsynthmaxParams2.imi'],
		'options'    : '-mode EFsynthmax -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthmaxParams2.res' , 'content' : """

BEGIN CONSTRAINT
 p1 = 1
& p2 = 2
OR
  p1 = 1
& p2 = 3
OR
  p1 = 1
& p2 = 4
OR
  p1 = 1
& p2 = 5
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmax on a clock-free toy example 3',
		'input_files': ['testEFsynthmaxParams3.imi'],
		'options'    : '-mode EFsynthmax -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthmaxParams3.res' , 'content' : """
BEGIN CONSTRAINT
 3*p1 > 4
& 2 > p1
& p2 = 4
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmax on a clock-free toy example 4',
		'input_files': ['testEFsynthmaxParams4.imi'],
		'options'    : '-mode EFsynthmax -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthmaxParams4.res' , 'content' : """
BEGIN CONSTRAINT
 p1 >= 0
& 5 > 3*p1
& 2*p1 = p2
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmax on a clock-free toy example 5',
		'input_files': ['testEFsynthmaxParams5.imi'],
		'options'    : '-mode EFsynthmax -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthmaxParams5.res' , 'content' : """
BEGIN CONSTRAINT
 p1 >= 1
& p2 = 3
OR
  p1 >= 2
& p2 = 5
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmax on a clock-free toy example 6',
		'input_files': ['testEFsynthmaxParams6.imi'],
		'options'    : '-mode EFsynthmax -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthmaxParams6.res' , 'content' : """
BEGIN CONSTRAINT
 p1 >= p2
& p1 > 0
& p2 >= 0
OR
  p1 >= 1
& p2 = 3
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFsynthmax on a toy example',
		'input_files': ['testEFsynthmax.imi'],
		'options'    : '-mode EFsynthmax -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFsynthmax.res' , 'content' : """
BEGIN CONSTRAINT
 p1 >= 10
& p2 >= 0
OR
  p1 >= 3
& p2 = 2
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFexemplify on a toy example',
		'input_files': ['testCounterExSimple-3.imi'],
		'options'    : '-mode EFexemplify -output-result',
		'expectations' : [
			{'file': 'testCounterExSimple-3.res' , 'content' : """
BEGIN RESULT
(************************************************************)
 Run #1


 Valuation:
  p = 1/2

 Other valuations with equivalent (discrete) run:
 2*p = 1

 Run nature: valid run

 Run:
Concrete run for parameter valuation:
  p = 1/2

pta: l1 ==> 
p = 1/2 & x = 0 & global_time = 0
 | 
 | via d = 3
 | followed by combined transition [PTA pta: guard{ 2*p = 1
& x = 3} updates{x := 0}  sync a Target ltarget] 
 | 
 v  pta: ltarget ==> 
p = 1/2 & x = 0 & global_time = 3
(************************************************************)


(************************************************************)
 Run #2

 Valuation:
  p = 0

 Other valuations with equivalent (discrete) run:
 2*p > 1
OR
  p >= 0
& 1 > 2*p

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 0

pta: l1 ==> 
p = 0 & x = 0 & global_time = 0
 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l1 ==> 
p = 0 & x = 1 & global_time = 1
(************************************************************)


(************************************************************)
 Run #3

 Valuation:
  p = 1/2

 Other valuations with equivalent (discrete) run:
 2*p = 1

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 1/2

pta: l1 ==> 
p = 1/2 & x = 0 & global_time = 0
 | 
 | via d = 0
 | followed by impossible transition labeled with a
 | 
 v  pta: ltarget ==> 
p = 1/2 & x = 0 & global_time = 0
(************************************************************)
END RESULT
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFexemplify on a toy example (clock initially non-zero, strict constraints)',
		'input_files': ['testCounterExSimple-4.imi'],
		'options'    : '-mode EFexemplify -output-result',
		'expectations' : [
			{'file': 'testCounterExSimple-4.res' , 'content' : """
BEGIN RESULT
(************************************************************)
 Run #1


 Valuation:
  p = 4095/2

 Other valuations with equivalent (discrete) run:
 2048 > p
& p > 2047

 Run nature: valid run

 Run:
Concrete run for parameter valuation:
  p = 4095/2

pta: l1 ==> 
p = 4095/2 & x = 1 & global_time = 0
 | 
 | via d = 1/2
 | followed by combined transition [PTA pta: guard{True
&  p = 2046 + x} updates{}  sync a Target ltarget] 
 | 
 v  pta: ltarget ==> 
p = 4095/2 & x = 3/2 & global_time = 1/2
(************************************************************)


(************************************************************)
 Run #2

 Valuation:
  p = 0

 Other valuations with equivalent (discrete) run:
 2047 >= p
& p >= 0
OR
  p >= 2048

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 0

pta: l1 ==> 
p = 0 & x = 1 & global_time = 0
 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l1 ==> 
p = 0 & x = 2 & global_time = 1
(************************************************************)


(************************************************************)
 Run #3

 Valuation:
  p = 4095/2

 Other valuations with equivalent (discrete) run:
 2048 > p
& p > 2047

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 4095/2

pta: l1 ==> 
p = 4095/2 & x = 1 & global_time = 0
 | 
 | via d = 0
 | followed by impossible transition labeled with a
 | 
 v  pta: ltarget ==> 
p = 4095/2 & x = 1 & global_time = 0
(************************************************************)
END RESULT

"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFexemplify on a toy example (violation possible only in the initial state)',
		'input_files': ['testCounterExSimple-5.imi'],
		'options'    : '-mode EFexemplify -output-result',
		'expectations' : [
			{'file': 'testCounterExSimple-5.res' , 'content' : """
BEGIN RESULT
(************************************************************)
 Run #1

 Valuation:
  p = 1

 Other valuations with equivalent (discrete) run:
 p > 0

 Run nature: valid run

 Run:
Concrete run for parameter valuation:
  p = 1

pta: l1 ==> 
p = 1 & x = 1 & global_time = 0
 | 
 | via d = 1/4
 | followed by combined transition [PTA pta: guard{ p > 0} updates{}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p = 1 & x = 5/4 & global_time = 1/4

 | 
 | via d = 1/4
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l3] 
 | 
 v  pta: l3 ==> 
p = 1 & x = 3/2 & global_time = 1/2

 | 
 | via d = 1/2
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target ltarget] 
 | 
 v  pta: ltarget ==> 
p = 1 & x = 2 & global_time = 1
(************************************************************)


(************************************************************)
 Run #2

 Valuation:
  p = 0

 Other valuations with equivalent (discrete) run:
 p = 0

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 0

pta: l1 ==> 
p = 0 & x = 1 & global_time = 0
 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l1 ==> 
p = 0 & x = 2 & global_time = 1

 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l2 ==> 
p = 0 & x = 3 & global_time = 2

 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l3 ==> 
p = 0 & x = 4 & global_time = 3
(************************************************************)


(************************************************************)
 Run #3

 Valuation:
  p = 1

 Other valuations with equivalent (discrete) run:
 p > 0

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 1

pta: l1 ==> 
p = 1 & x = 1 & global_time = 0
 | 
 | via d = 0
 | followed by impossible transition labeled with a
 | 
 v  pta: l2 ==> 
p = 1 & x = 1 & global_time = 0

 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l2 ==> 
p = 1 & x = 2 & global_time = 1

 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l3 ==> 
p = 1 & x = 3 & global_time = 2
(************************************************************)
END RESULT

"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFexemplify on a toy example (violation possible only at position 2)',
		'input_files': ['testCounterExSimple-5b.imi'],
		'options'    : '-mode EFexemplify -output-result',
		'expectations' : [
			{'file': 'testCounterExSimple-5b.res' , 'content' : """
BEGIN RESULT
(************************************************************)
 Run #1

 Valuation:
  p = 1

 Other valuations with equivalent (discrete) run:
 p > 0

 Run nature: valid run

 Run:
Concrete run for parameter valuation:
  p = 1

pta: l1 ==> 
p = 1 & x = 1 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p = 1 & x = 1 & global_time = 0

 | 
 | via d = 1/2
 | followed by combined transition [PTA pta: guard{ p > 0} updates{}  sync a Target l3] 
 | 
 v  pta: l3 ==> 
p = 1 & x = 3/2 & global_time = 1/2

 | 
 | via d = 1/2
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target ltarget] 
 | 
 v  pta: ltarget ==> 
p = 1 & x = 2 & global_time = 1
(************************************************************)


(************************************************************)
 Run #2

 Valuation:
  p = 0

 Other valuations with equivalent (discrete) run:
 p = 0

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 0

pta: l1 ==> 
p = 0 & x = 1 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p = 0 & x = 1 & global_time = 0
 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l2 ==> 
p = 0 & x = 2 & global_time = 1

 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l3 ==> 
p = 0 & x = 3 & global_time = 2
(************************************************************)


(************************************************************)
 Run #3

 Valuation:
  p = 1

 Other valuations with equivalent (discrete) run:
 p > 0

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 1

pta: l1 ==> 
p = 1 & x = 1 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p = 1 & x = 1 & global_time = 0
 | 
 | via d = 0
 | followed by impossible transition labeled with a
 | 
 v  pta: l3 ==> 
p = 1 & x = 1 & global_time = 0

 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l3 ==> 
p = 1 & x = 2 & global_time = 1
(************************************************************)
END RESULT

"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,
	
	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFexemplify on a toy example (violation possible only at last position)',
		'input_files': ['testCounterExSimple-5c.imi'],
		'options'    : '-mode EFexemplify -output-result',
		'expectations' : [
			{'file': 'testCounterExSimple-5c.res' , 'content' : """
BEGIN RESULT
(************************************************************)
 Run #1

 Valuation:
  p = 1

 Other valuations with equivalent (discrete) run:
 p > 0

 Run nature: valid run

 Run:
Concrete run for parameter valuation:
  p = 1

pta: l1 ==> 
p = 1 & x = 1 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p = 1 & x = 1 & global_time = 0

 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l3] 
 | 
 v  pta: l3 ==> 
p = 1 & x = 1 & global_time = 0

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ p > 0} updates{}  sync a Target ltarget] 
 | 
 v  pta: ltarget ==> 
p = 1 & x = 2 & global_time = 1
(************************************************************)


(************************************************************)
 Run #2

 Valuation:
  p = 0

 Other valuations with equivalent (discrete) run:
 p = 0

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 0

pta: l1 ==> 
p = 0 & x = 1 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p = 0 & x = 1 & global_time = 0

 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l3] 
 | 
 v  pta: l3 ==> 
p = 0 & x = 1 & global_time = 0
 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l3 ==> 
p = 0 & x = 2 & global_time = 1
(************************************************************)


(************************************************************)
 Run #3

 Valuation:
  p = 1

 Other valuations with equivalent (discrete) run:
 p > 0

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 1

pta: l1 ==> 
p = 1 & x = 1 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p = 1 & x = 1 & global_time = 0

 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l3] 
 | 
 v  pta: l3 ==> 
p = 1 & x = 1 & global_time = 0
 | 
 | via d = 0
 | followed by impossible transition labeled with a
 | 
 v  pta: ltarget ==> 
p = 1 & x = 1 & global_time = 0
(************************************************************)
END RESULT
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFexemplify on a toy example (no bad parameter valuation derived)',
		'input_files': ['testCounterExSimple-6.imi'],
		'options'    : '-mode EFexemplify -output-result',
		'expectations' : [
			{'file': 'testCounterExSimple-6.res' , 'content' : """
BEGIN RESULT

(************************************************************)
 Run #1

 Valuation:
  p = 2

 Other valuations with equivalent (discrete) run:
 p > 1

 Run nature: valid run

 Run:
Concrete run for parameter valuation:
  p = 2

pta: l1 ==> 
p = 2 & x = 2 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{ p > 0} updates{}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p = 2 & x = 2 & global_time = 0

 | 
 | via d = 1/4
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l3] 
 | 
 v  pta: l3 ==> 
p = 2 & x = 9/4 & global_time = 1/4

 | 
 | via d = 1/4
 | followed by combined transition [PTA pta: guard{True} updates{x := 0}  sync a Target ltarget] 
 | 
 v  pta: ltarget ==> 
p = 2 & x = 0 & global_time = 1/2
(************************************************************)


(************************************************************)
 Run #2

 Valuation:
  p = 2

 Other valuations with equivalent (discrete) run:
 p > 1

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 2

pta: l1 ==> 
p = 2 & x = 2 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{ p > 0} updates{}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p = 2 & x = 2 & global_time = 0

 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l3] 
 | 
 v  pta: l3 ==> 
p = 2 & x = 2 & global_time = 0
 | 
 | via d = 0
 | followed by impossible transition labeled with a
 | 
 v  pta: ltarget ==> 
p = 2 & x = 2 & global_time = 0
(************************************************************)

END RESULT
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFexemplify on a toy example (no bad parameter nor clock valuation derived)',
		'input_files': ['testCounterExSimple-7.imi'],
		'options'    : '-mode EFexemplify -output-result',
		'expectations' : [
			{'file': 'testCounterExSimple-7.res' , 'content' : """

BEGIN RESULT

(************************************************************)
 Run #1

 Valuation:
  p = 2

 Other valuations with equivalent (discrete) run:
 p > 1

 Run nature: valid run

 Run:
Concrete run for parameter valuation:
  p = 2

pta: l1 ==> 
p = 2 & x = 3/2 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{ p > 0} updates{}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p = 2 & x = 3/2 & global_time = 0

 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l3] 
 | 
 v  pta: l3 ==> 
p = 2 & x = 3/2 & global_time = 0

 | 
 | via d = 1/2
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target ltarget] 
 | 
 v  pta: ltarget ==> 
p = 2 & x = 2 & global_time = 1/2
(************************************************************)

END RESULT

"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFexemplify on a toy example (no bad parameter nor clock valuation derived)',
		'input_files': ['testCounterExSimple-8.imi'],
		'options'    : '-mode EFexemplify -output-result -output-cart',
		'expectations' : [
			{'file': 'testCounterExSimple-8.res' , 'content' : """

BEGIN RESULT

(************************************************************)
 Run #1

 Valuation:
  p1 = 1
& p2 = 1/2

 Other valuations with equivalent (discrete) run:
 p1 > p2
& p2 > 0
& 6 > p2

 Run nature: valid run

 Run:
Concrete run for parameter valuation:
  p1 = 1
& p2 = 1/2

pta: l1 ==> 
p1 = 1 & p2 = 1/2 & x = 2 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{ p2 > 0} updates{}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p1 = 1 & p2 = 1/2 & x = 2 & global_time = 0

 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l3] 
 | 
 v  pta: l3 ==> 
p1 = 1 & p2 = 1/2 & x = 2 & global_time = 0

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ p1 > p2
& p2 + x > p1} updates{}  sync a Target ltarget] 
 | 
 v  pta: ltarget ==> 
p1 = 1 & p2 = 1/2 & x = 3 & global_time = 1
(************************************************************)


(************************************************************)
 Run #2

 Valuation:
  p1 = 3
& p2 = 3

 Other valuations with equivalent (discrete) run:
 p1 > 0
& p2 >= p1
& 6 > p2

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p1 = 3
& p2 = 3

pta: l1 ==> 
p1 = 3 & p2 = 3 & x = 3/2 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{ p2 > 0} updates{}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p1 = 3 & p2 = 3 & x = 3/2 & global_time = 0

 | 
 | via d = 1/2
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l3] 
 | 
 v  pta: l3 ==> 
p1 = 3 & p2 = 3 & x = 2 & global_time = 1/2
 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l3 ==> 
p1 = 3 & p2 = 3 & x = 3 & global_time = 3/2
(************************************************************)


(************************************************************)
 Run #3

 Valuation:
  p1 = 1
& p2 = 1/2

 Other valuations with equivalent (discrete) run:
 p1 > p2
& p2 > 0
& 6 > p2

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p1 = 1
& p2 = 1/2

pta: l1 ==> 
p1 = 1 & p2 = 1/2 & x = 3/2 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{ p2 > 0} updates{}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p1 = 1 & p2 = 1/2 & x = 3/2 & global_time = 0

 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{}  sync a Target l3] 
 | 
 v  pta: l3 ==> 
p1 = 1 & p2 = 1/2 & x = 3/2 & global_time = 0
 | 
 | via d = 0
 | followed by impossible transition labeled with a
 | 
 v  pta: ltarget ==> 
p1 = 1 & p2 = 1/2 & x = 3/2 & global_time = 0
(************************************************************)
END RESULT

"""
			} # end result file
			,
			# NOTE: Just check its existence
			{'file': 'testCounterExSimple-8_ex_3_neg.png' , 'content' : ""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFexemplify on a toy monitoring-style example',
		'input_files': ['testCounterExSimple-9.imi'],
		'options'    : '-mode EFexemplify -output-result',
		'expectations' : [
			{'file': 'testCounterExSimple-9.res' , 'content' : """

BEGIN RESULT

(************************************************************)
 Run #1

 Valuation:
  p = 1

 Other valuations with equivalent (discrete) run:
 p >= 0

 Run nature: valid run

 Run:
Concrete run for parameter valuation:
  p = 1

pta: l1 ==> 
p = 1 & x = 0 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{x := 0}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p = 1 & x = 0 & global_time = 0

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ p = x} updates{x := 0}  sync b Target l3] 
 | 
 v  pta: l3 ==> 
p = 1 & x = 0 & global_time = 1

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ p = x} updates{}  sync b Target ltarget] 
 | 
 v  pta: ltarget ==> 
p = 1 & x = 1 & global_time = 2
(************************************************************)


(************************************************************)
 Run #2

 Valuation:
  p = 1

 Other valuations with equivalent (discrete) run:
 p >= 0

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 1

pta: l1 ==> 
p = 1 & x = 0 & global_time = 0
 | 
 | via d = 0
 | followed by combined transition [PTA pta: guard{True} updates{x := 0}  sync a Target l2] 
 | 
 v  pta: l2 ==> 
p = 1 & x = 0 & global_time = 0

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ p = x} updates{x := 0}  sync b Target l3] 
 | 
 v  pta: l3 ==> 
p = 1 & x = 0 & global_time = 1
 | 
 | via d = 0
 | followed by impossible transition labeled with b
 | 
 v  pta: ltarget ==> 
p = 1 & x = 0 & global_time = 1
(************************************************************)
END RESULT

"""
			} # end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFexemplify on a toy example without parameter',
		'input_files': ['testCounterExSimple.imi'],
		'options'    : '-mode EFexemplify -output-result',
		'expectations' : [
			{'file': 'testCounterExSimple.res' , 'content' : """

BEGIN RESULT

(************************************************************)
 Run #1

 Valuation:
  

 Other valuations with equivalent (discrete) run:
True

 Run nature: valid run

 Run:
Concrete run for parameter valuation:
  

pta: l1, d1 = 1/2, d2 = 50 ==> 
x = 0 & global_time = 0
 | 
 | via d = 3
 | followed by combined transition [PTA pta: guard{ x = 3} updates{x := 0}  sync a Target l2] 
 | 
 v  pta: l2, d1 = 1/2, d2 = 50 ==> 
x = 0 & global_time = 3

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ x = 1} updates{x := 0, d1 := d1 + 2}  sync a Target l3] 
 | 
 v  pta: l3, d1 = 5/2, d2 = 50 ==> 
x = 0 & global_time = 4

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ x = 1} updates{d2 := (d2) / 2}  sync a Target l4] 
 | 
 v  pta: l4, d1 = 5/2, d2 = 25 ==> 
x = 1 & global_time = 5

 | 
 | via d = 7
 | followed by combined transition [PTA pta: guard{ x = 8} updates{}  sync a Target lbad] 
 | 
 v  pta: lbad, d1 = 5/2, d2 = 25 ==> 
x = 8 & global_time = 12
(************************************************************)


(************************************************************)
 Run #2

 Valuation:
  

 Other valuations with equivalent (discrete) run:
True

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  

pta: l1, d1 = 1/2, d2 = 50 ==> 
x = 0 & global_time = 0
 | 
 | via d = 3
 | followed by combined transition [PTA pta: guard{ x = 3} updates{x := 0}  sync a Target l2] 
 | 
 v  pta: l2, d1 = 1/2, d2 = 50 ==> 
x = 0 & global_time = 3

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ x = 1} updates{x := 0, d1 := d1 + 2}  sync a Target l3] 
 | 
 v  pta: l3, d1 = 5/2, d2 = 50 ==> 
x = 0 & global_time = 4

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ x = 1} updates{d2 := (d2) / 2}  sync a Target l4] 
 | 
 v  pta: l4, d1 = 5/2, d2 = 25 ==> 
x = 1 & global_time = 5
 | 
 | via d = 0
 | followed by impossible transition labeled with a
 | 
 v  pta: lbad, d1 = 5/2, d2 = 25 ==> 
x = 1 & global_time = 5
(************************************************************)

END RESULT

"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test EFexemplify on a toy example with parameters and discrete variables',
		'input_files': ['testCounterExSimple-2.imi'],
		'options'    : '-mode EFexemplify -output-result',
		'expectations' : [
			{'file': 'testCounterExSimple-2.res' , 'content' : """

BEGIN RESULT

(************************************************************)
 Run #1

 Valuation:
  p = 1/2

 Other valuations with equivalent (discrete) run:
 1 > p
& p >= 0

 Run nature: valid run

 Run:
Concrete run for parameter valuation:
  p = 1/2

pta: l1, d1 = 1/2 ==> 
p = 1/2 & x = 0 & global_time = 0
 | 
 | via d = 3
 | followed by combined transition [PTA pta: guard{ x = 3} updates{x := 0}  sync a Target l2] 
 | 
 v  pta: l2, d1 = 1/2 ==> 
p = 1/2 & x = 0 & global_time = 3

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ x = 1} updates{x := 0, d1 := d1 + 2}  sync a Target l3] 
 | 
 v  pta: l3, d1 = 5/2 ==> 
p = 1/2 & x = 0 & global_time = 4

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ 1 > p
& x = 1} updates{d1 := (d1) / 2}  sync a Target l4] 
 | 
 v  pta: l4, d1 = 5/4 ==> 
p = 1/2 & x = 1 & global_time = 5

 | 
 | via d = 7
 | followed by combined transition [PTA pta: guard{ x = 8} updates{}  sync a Target lbad] 
 | 
 v  pta: lbad, d1 = 5/4 ==> 
p = 1/2 & x = 8 & global_time = 12
(************************************************************)


(************************************************************)
 Run #2

 Valuation:
  p = 1

 Other valuations with equivalent (discrete) run:
 p >= 1

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 1

pta: l1, d1 = 1/2 ==> 
p = 1 & x = 0 & global_time = 0
 | 
 | via d = 3
 | followed by combined transition [PTA pta: guard{ x = 3} updates{x := 0}  sync a Target l2] 
 | 
 v  pta: l2, d1 = 1/2 ==> 
p = 1 & x = 0 & global_time = 3

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ x = 1} updates{x := 0, d1 := d1 + 2}  sync a Target l3] 
 | 
 v  pta: l3, d1 = 5/2 ==> 
p = 1 & x = 0 & global_time = 4
 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l3, d1 = 5/2 ==> 
p = 1 & x = 1 & global_time = 5

 | 
 | via d = 1
 | followed by impossible transition labeled with a
 | 
 v  pta: l4, d1 = 5/4 ==> 
p = 1 & x = 2 & global_time = 6
(************************************************************)


(************************************************************)
 Run #3

 Valuation:
  p = 1/2

 Other valuations with equivalent (discrete) run:
 1 > p
& p >= 0

 Run nature: impossible run

 Run:
Impossible concrete run for parameter valuation:
  p = 1/2

pta: l1, d1 = 1/2 ==> 
p = 1/2 & x = 0 & global_time = 0
 | 
 | via d = 3
 | followed by combined transition [PTA pta: guard{ x = 3} updates{x := 0}  sync a Target l2] 
 | 
 v  pta: l2, d1 = 1/2 ==> 
p = 1/2 & x = 0 & global_time = 3

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ x = 1} updates{x := 0, d1 := d1 + 2}  sync a Target l3] 
 | 
 v  pta: l3, d1 = 5/2 ==> 
p = 1/2 & x = 0 & global_time = 4

 | 
 | via d = 1
 | followed by combined transition [PTA pta: guard{ 1 > p
& x = 1} updates{d1 := (d1) / 2}  sync a Target l4] 
 | 
 v  pta: l4, d1 = 5/4 ==> 
p = 1/2 & x = 1 & global_time = 5
 | 
 | via d = 0
 | followed by impossible transition labeled with a
 | 
 v  pta: lbad, d1 = 5/4 ==> 
p = 1/2 & x = 1 & global_time = 5
(************************************************************)
END RESULT
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test LoopSynth: flip-flop (no loop)',
		'input_files': ['flipflop.imi'],
		'options'    : '-mode LoopSynth -output-result',
		'expectations' : [
			{'file': 'flipflop.res' , 'content' : """
BEGIN CONSTRAINT
False
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 20
Number of transitions                   : 19
Number of computed states               : 20
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test LoopSynth: simple example with loop',
		'input_files': ['PDFC4.imi'],
		'options'    : '-mode LoopSynth -output-result',
		'expectations' : [
			{'file': 'PDFC4.res' , 'content' : """
BEGIN CONSTRAINT
 10 >= p2
& p2 >= 0
& p1 >= 0
& p1 + 5 >= p2
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 2
Number of transitions                   : 2
Number of computed states               : 3
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test LoopSynth: simple example with loop for any valuation',
		'input_files': ['PDFC5.imi'],
		'options'    : '-mode LoopSynth -output-result',
		'expectations' : [
			{'file': 'PDFC5.res' , 'content' : """
BEGIN CONSTRAINT
 p3 >= 0
& p2 >= 0
& p1 >= 0
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 5
Number of transitions                   : 6
Number of computed states               : 7
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test AccLoopSynth: flipflop (no loop)',
		'input_files': ['flipflop.imi'],
		'options'    : '-mode AccLoopSynth -output-result',
		'expectations' : [
			{'file': 'flipflop.res' , 'content' : """
BEGIN CONSTRAINT
False
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 20
Number of transitions                   : 19
Number of computed states               : 20
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/22
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test AccLoopSynth: simple example 1',
		'input_files': ['testNDFS-1.imi'],
		'options'    : '-mode AccLoopSynth -output-result',
		'expectations' : [
			{'file': 'testNDFS-1.res' , 'content' : """
BEGIN CONSTRAINT
 p = 1
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 3
Number of transitions                   : 4
Number of computed states               : 5
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/22
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test AccLoopSynth: simple example 2',
		'input_files': ['testNDFS-2.imi'],
		'options'    : '-mode AccLoopSynth -output-result',
		'expectations' : [
			{'file': 'testNDFS-2.res' , 'content' : """
BEGIN CONSTRAINT
 p = 2
OR
  p = 1
OR
  p = 4
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 9
Number of transitions                   : 13
Number of computed states               : 14
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/22
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test AccLoopSynth: simple example 3 (accepting for all valuations)',
		'input_files': ['PDFC5.imi'],
		'options'    : '-mode AccLoopSynth -output-result',
		'expectations' : [
			{'file': 'PDFC5.res' , 'content' : """
BEGIN CONSTRAINT
 p3 >= 0
& p2 >= 0
& p1 >= 0
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 5
Number of transitions                   : 6
Number of computed states               : 7
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test AccLoopSynthNDFS emptiness: flipflop (no loop)',
		'input_files': ['flipflop.imi'],
		'options'    : '-mode AccLoopSynthNDFS -output-result -counterexample',
		'expectations' : [
			{'file': 'flipflop.res' , 'content' : """
BEGIN CONSTRAINT
False
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test AccLoopSynthNDFS with complete constraint: flipflop (no loop)',
		'input_files': ['flipflop.imi'],
		'options'    : '-mode AccLoopSynthNDFS -explOrder NDFSsub -output-result',
		'expectations' : [
			{'file': 'flipflop.res' , 'content' : """
BEGIN CONSTRAINT
False
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/07/22
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test AccLoopSynthNDFS emptiness: simple example 1',
		'input_files': ['testNDFS-1.imi'],
		'options'    : '-mode AccLoopSynthNDFS -output-result -counterexample',
		'expectations' : [
			{'file': 'testNDFS-1.res' , 'content' : """
BEGIN CONSTRAINT
 p = 1
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : possible under-approximation
Termination                             : terminated after reaching a target state (some states may have been unexplored)
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/08/01
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test AccLoopSynthNDFS: simple example 1 with complete constraint',
		'input_files': ['testNDFS-1.imi'],
		'options'    : '-mode AccLoopSynthNDFS -explOrder NDFSsub -output-result',
		'expectations' : [
			{'file': 'testNDFS-1.res' , 'content' : """
BEGIN CONSTRAINT
 p = 1
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/08/01
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test AccLoopSynthNDFS emptiness: simple example 2',
		'input_files': ['testNDFS-2.imi'],
		'options'    : '-mode AccLoopSynthNDFS -output-result -counterexample',
		'expectations' : [
			{'file': 'testNDFS-2.res' , 'content' : """
BEGIN CONSTRAINT
 p = 4
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : possible under-approximation
Termination                             : terminated after reaching a target state (some states may have been unexplored)
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/08/01
		# Test for IMITATOR version: 2.12
		'purpose'    : 'Test AccLoopSynthNDFS: simple example 2 with complete constraint',
		'input_files': ['testNDFS-2.imi'],
		'options'    : '-mode AccLoopSynthNDFS -explOrder NDFSsub -output-result',
		'expectations' : [
			{'file': 'testNDFS-2.res' , 'content' : """
BEGIN CONSTRAINT
   p = 2
 OR
   p = 1
 OR
   p = 4
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test NZCUB: flip-flop (no loop)',
		'input_files': ['flipflop.imi'],
		'options'    : '-mode NZCUB -output-result',
		'expectations' : [
			{'file': 'flipflop.res' , 'content' : """
BEGIN CONSTRAINT
False
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 20
Number of transitions                   : 19
Number of computed states               : 20
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test NZCUB: PDFC4 (loop but Zeno)',
		'input_files': ['PDFC4.imi'],
		'options'    : '-mode NZCUB -output-result',
		'expectations' : [
			{'file': 'PDFC4.res' , 'content' : """
BEGIN CONSTRAINT
False
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 4
Number of transitions                   : 4
Number of computed states               : 5
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test NZCUB: CUBPTA1 (non-Zeno loop)',
		'input_files': ['CUBPTA1.imi'],
		'options'    : '-mode NZCUB -output-result',
		'expectations' : [
			{'file': 'CUBPTA1.res' , 'content' : """
BEGIN CONSTRAINT
 p1 >= 0
& p2 >= 1
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 4
Number of transitions                   : 4
Number of computed states               : 5
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test NZCUB: CUBPTA2 (2 non-Zeno loops)',
		'input_files': ['CUBPTA2.imi'],
		'options'    : '-mode NZCUB -output-result',
		'expectations' : [
			{'file': 'CUBPTA2.res' , 'content' : """
BEGIN CONSTRAINT
 p2 >= 0
& p1 >= 5
OR
  p1 >= 0
& p2 >= 1
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Number of states                        : 9
Number of transitions                   : 14
Number of computed states               : 15
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test PDFC: very basic example without clocks',
		'input_files': ['PDFC1.imi'],
		'options'    : '-mode PDFC -output-result -output-states',
		'expectations' : [
			{'file': 'PDFC1.res' , 'content' : """
BEGIN CONSTRAINT
 p1 >= 0
& p2 >= p1
END CONSTRAINT

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Number of states              : 2
Number of transitions         : 2
Number of computed states     : 3
"""
			} #end result file
			,
			{'file': 'PDFC1-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l1 ==>
& p1 >= 0
& p2 >= 0

  Projection onto the parameters:
   p1 >= 0
& p2 >= 0

  /************************************************************/
  STATE 1:
  pta: l2 ==>
& p1 >= 0
& p2 >= p1

  Projection onto the parameters:
   p1 >= 0
& p2 >= p1

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1 via "a"
  s_1 -> s_1 via "a"
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test PDFC: very basic example (false result)',
		'input_files': ['PDFC3.imi'],
		'options'    : '-mode PDFC -output-result  -output-states',
		'expectations' : [
			{'file': 'PDFC3.res' , 'content' : """
BEGIN CONSTRAINT
False
END CONSTRAINT

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Number of states              : 2
Number of transitions         : 1
Number of computed states     : 2
"""
			} #end result file
			,
			{'file': 'PDFC3-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l1 ==>
& p1 + 5 >= x
& p1 >= 0
& p2 >= 0
& x >= 0

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 1:
  pta: l2 ==>
& p1 >= 0
& p1 + 5 >= p2
& p2 >= 0
& x >= p2
& 10 >= x

  Projection onto the parameters:
   10 >= p2
& p2 >= 0
& p1 >= 0
& p1 + 5 >= p2

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1 via "a"
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test PDFC: very basic example (normal result)',
		'input_files': ['PDFC4.imi'],
		'options'    : '-mode PDFC -output-result  -output-states',
		'expectations' : [
			{'file': 'PDFC4.res' , 'content' : """
BEGIN CONSTRAINT
 p1 + 5 >= p2
& p1 >= 0
& p2 >= 0
& 10 >= p2
END CONSTRAINT

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Number of states              : 2
Number of transitions         : 2
Number of computed states     : 3
"""
			} #end result file
			,
			{'file': 'PDFC4-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l1 ==>
& p1 + 5 >= x
& p1 >= 0
& p2 >= 0
& x >= 0

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 1:
  pta: l2 ==>
& p1 >= 0
& p1 + 5 >= p2
& p2 >= 0
& x >= p2
& 10 >= x

  Projection onto the parameters:
   10 >= p2
& p2 >= 0
& p1 >= 0
& p1 + 5 >= p2

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1 via "a"
  s_1 -> s_1 via "a"
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test PDFC: very basic example (false result)',
		'input_files': ['PDFC6.imi'],
		'options'    : '-mode PDFC -output-result  -output-states -no-var-autoremove', #TODO: re-do without '-no-var-autoremove'
		'expectations' : [
			{'file': 'PDFC6.res' , 'content' : """
BEGIN CONSTRAINT
False
END CONSTRAINT

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Number of states              : 2
Number of transitions         : 1
Number of computed states     : 2
"""
			} #end result file
			,
			{'file': 'PDFC6-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l1 ==>
& p >= 0
& x1 >= 0

  Projection onto the parameters:
   p >= 0

  /************************************************************/
  STATE 1:
  pta: l2 ==>
& p >= 0
& x1 >= 0

  Projection onto the parameters:
   p >= 0

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1 via "a"
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test PDFC: very basic example (true result)',
		'input_files': ['PDFC7.imi'],
		'options'    : '-mode PDFC -output-result  -output-states',
		'expectations' : [
			{'file': 'PDFC7.res' , 'content' : """
BEGIN CONSTRAINT
 p >= 0
END CONSTRAINT

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Number of states              : 2
Number of transitions         : 2
Number of computed states     : 3
"""
			} #end result file
			,
			{'file': 'PDFC7-statespace.states' , 'content' : """

  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l1 ==>
& p >= 0
& x1 >= 0

  Projection onto the parameters:
   p >= 0

  /************************************************************/
  STATE 1:
  pta: l2 ==>
& p >= 0
& x1 >= p

  Projection onto the parameters:
   p >= 0

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1 via "a"
  s_1 -> s_1 via "a"
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test PDFC: basic example with disjunction',
		'input_files': ['PDFC5.imi'],
		'options'    : '-mode PDFC -output-result  -output-states',
		'expectations' : [
			{'file': 'PDFC5.res' , 'content' : """
BEGIN CONSTRAINT
 p1 >= 0
& p2 >= 0
& p1 + 5 = p3
OR
  p1 >= 0
& p3 > 5 + p1
& p2 >= 5 + p1
OR
  p1 >= 0
& p1 + 5 > p3
& p3 >= 0
& p2 >= 5 + p1
END CONSTRAINT

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Number of states              : 5
Number of transitions         : 6
Number of computed states     : 7
"""
			} #end result file
			,
			{'file': 'PDFC5-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l1 ==>
& p1 + 5 >= x1
& p1 >= 0
& p2 >= 0
& p3 >= 0
& x1 >= 0
& x1 = x2

  Projection onto the parameters:
   p3 >= 0
& p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 1:
  pta: l2 ==>
& p1 >= 0
& p2 >= 0
& p3 >= 0
& x1 >= 0
& x1 = x2

  Projection onto the parameters:
   p3 >= 0
& p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 2:
  pta: l3 ==>
& p1 >= 0
& p1 + 5 >= p3
& p2 >= 0
& p3 >= 0
& x1 >= p3
& x1 = x2

  Projection onto the parameters:
   p1 + 5 >= p3
& p3 >= 0
& p1 >= 0
& p2 >= 0

  /************************************************************/
  STATE 3:
  pta: l3 ==>
& p1 >= 0
& p2 >= 0
& p3 >= 0
& x1 >= 0
& x1 = x2

  Projection onto the parameters:
   p3 >= 0
& p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 4:
  pta: l2 ==>
& p1 >= 0
& p1 + 5 >= p3
& p2 >= 0
& p3 >= 0
& x1 >= p3
& x1 = x2

  Projection onto the parameters:
   p1 + 5 >= p3
& p3 >= 0
& p1 >= 0
& p2 >= 0

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1 via "a"
  s_0 -> s_2
  s_1 -> s_3 via "a"
  s_2 -> s_4 via "a"
  s_3 -> s_1 via "a"
  s_4 -> s_2 via "a"
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test PDFC: example with early termination due to false constraint',
		'input_files': ['flipflop.imi'],
		'options'    : '-mode PDFC -output-result  -output-states -no-var-autoremove', #TODO: re-do without '-no-var-autoremove'
		'expectations' : [
			{'file': 'flipflop.res' , 'content' : """
BEGIN CONSTRAINT
False
END CONSTRAINT

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Number of states              : 20
Number of transitions         : 19
Number of computed states     : 20
"""
			} #end result file
			,
			{'file': 'flipflop-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  input: Input0, g1: G10011, g2: G2101, g3: G30011, g4: G410, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 5 >= s
& dG3_u >= 8
& dG4_u >= 3
& s >= 0
& ckG1 >= s
& ckG2 >= s
& ckG3 >= s
& ckG4 >= s

  Projection onto the parameters:
   dG4_u >= 3
& dG3_u >= 8

  /************************************************************/
  STATE 1:
  input: Input1, g1: G11011, g2: G2101, g3: G30011, g4: G410, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 12 >= s
& dG3_u >= 8
& dG4_u >= 3
& s >= 5
& ckG2 >= s
& ckG3 >= s
& ckG4 >= s
& s = 5 + ckG1

  Projection onto the parameters:
   dG4_u >= 3
& dG3_u >= 8

  /************************************************************/
  STATE 2:
  input: Input1, g1: G11010, g2: G2001, g3: G30011, g4: G410, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 15 >= s
& dG3_u >= 8
& dG4_u >= 3
& s >= 12
& ckG2 >= s
& ckG3 >= s
& ckG4 >= s
& s = 5 + ckG1

  Projection onto the parameters:
   dG4_u >= 3
& dG3_u >= 8

  /************************************************************/
  STATE 3:
  input: Input2, g1: G11110, g2: G2011, g3: G30111, g4: G410, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& dG3_u + 15 >= s
& 32 >= s
& dG3_u >= 8
& dG4_u >= 3
& ckG2 >= s
& s >= 15
& ckG4 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 8
& dG4_u >= 3

  /************************************************************/
  STATE 4:
  input: Input3, g1: G10110, g2: G2011, g3: G30111, g4: G410, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 39 >= s
& dG3_u + 15 >= s
& dG4_u >= 3
& ckG2 >= s
& s >= 32
& ckG4 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 17
& dG4_u >= 3

  /************************************************************/
  STATE 5:
  input: Input2, g1: G11110, g2: G2011, g3: G30110, g4: G400, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 32 >= s
& dG3_u + ckG4 + 15 >= s
& dG4_u >= 3
& s >= 23 + ckG4
& ckG4 >= 0
& ckG2 >= s
& dG4_u >= ckG4
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 8
& dG4_u >= 3

  /************************************************************/
  STATE 6:
  input: Input4, g1: G10010, g2: G2001, g3: G30011, g4: G410, automatically_generated_observer: loc_AutoGen_obs_2 ==>
& dG3_u >= 24
& dG4_u >= 3
& ckG2 >= 39
& ckG4 >= 39
& s = 0
& ckG1 = 0
& ckG3 = 24

  Projection onto the parameters:
   dG4_u >= 3
& dG3_u >= 24

  /************************************************************/
  STATE 7:
  input: Input3, g1: G10110, g2: G2011, g3: G30110, g4: G400, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 39 >= s
& dG3_u + ckG4 + 15 >= s
& dG4_u >= 3
& s >= 32 + ckG4
& ckG4 >= 0
& ckG2 >= s
& dG4_u >= ckG4
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 17
& dG4_u >= 3

  /************************************************************/
  STATE 8:
  input: Input3, g1: G10110, g2: G2011, g3: G30110, g4: G400, automatically_generated_observer: loc_AutoGen_obs_0 ==>
& 39 >= s
& dG3_u + ckG4 + 15 >= s
& dG4_u >= ckG4
& dG4_u >= 3
& ckG2 >= s
& s >= 32
& s >= 23 + ckG4
& ckG4 + 32 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u + dG4_u >= 17
& dG4_u >= 3
& dG3_u >= 8

  /************************************************************/
  STATE 9:
  input: Input2, g1: G11110, g2: G2011, g3: G31110, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& dG3_u + ckG4 + 15 >= s
& dG4_u >= 3
& s >= 23 + ckG4
& ckG4 >= 3
& ckG2 >= s
& 32 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 8
& dG4_u >= 3

  /************************************************************/
  STATE 10:
  input: Input4, g1: G10010, g2: G2001, g3: G30010, g4: G400, automatically_generated_observer: loc_AutoGen_obs_2 ==>
& dG3_u + ckG4 >= 24
& dG4_u >= ckG4
& dG4_u >= 3
& ckG2 >= 39
& ckG4 >= 0
& 7 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 0

  Projection onto the parameters:
   dG3_u + dG4_u >= 24
& dG3_u >= 17
& dG4_u >= 3

  /************************************************************/
  STATE 11:
  input: Input3, g1: G10110, g2: G2011, g3: G31110, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& dG3_u + ckG4 + 15 >= s
& dG4_u >= 3
& s >= 32 + ckG4
& ckG4 >= 3
& ckG2 >= s
& 39 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 17
& dG4_u >= 3

  /************************************************************/
  STATE 12:
  input: Input4, g1: G10010, g2: G2001, g3: G30010, g4: G400, automatically_generated_observer: loc_AutoGen_obs_2 ==>
& dG3_u + ckG4 >= 24
& dG4_u >= ckG4
& ckG2 >= 39
& ckG4 >= 7
& 16 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 0

  Projection onto the parameters:
   dG4_u >= 7
& dG3_u >= 8
& dG3_u + dG4_u >= 24

  /************************************************************/
  STATE 13:
  input: Input3, g1: G10110, g2: G2011, g3: G31110, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& 39 >= s
& dG3_u + ckG4 + 15 >= s
& dG4_u + s >= 32 + ckG4
& dG4_u >= 3
& s >= 32
& s >= 23 + ckG4
& ckG4 >= 3
& ckG2 >= s
& ckG4 + 32 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u + dG4_u >= 17
& dG3_u >= 8
& dG4_u >= 3

  /************************************************************/
  STATE 14:
  input: Input3, g1: G10110, g2: G2011, g3: G31110, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& 39 >= s
& dG3_u + ckG4 + 15 >= s
& dG4_u >= 3
& ckG2 >= s
& s >= 32
& s >= 23 + ckG4
& ckG4 + 29 >= s
& s = 5 + ckG1
& s = 15 + ckG3

  Projection onto the parameters:
   dG3_u >= 8
& dG4_u >= 3

  /************************************************************/
  STATE 15:
  input: Input4, g1: G10010, g2: G2001, g3: G31010, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& dG3_u + ckG4 >= 24
& dG4_u + 7 >= ckG4
& dG4_u >= 3
& ckG2 >= 39
& ckG4 >= 7
& 16 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 24

  Projection onto the parameters:
   dG3_u + dG4_u >= 17
& dG3_u >= 8
& dG4_u >= 3

  /************************************************************/
  STATE 16:
  input: Input4, g1: G10010, g2: G2001, g3: G31010, g4: G401, automatically_generated_observer: loc_AutoGen_obs_2 ==>
& dG3_u + ckG4 >= 24
& dG4_u >= ckG4
& ckG2 >= 39
& ckG4 >= 7
& 16 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 0

  Projection onto the parameters:
   dG4_u >= 7
& dG3_u >= 8
& dG3_u + dG4_u >= 24

  /************************************************************/
  STATE 17:
  input: Input4, g1: G10010, g2: G2001, g3: G31010, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& dG3_u + ckG4 >= 24
& dG4_u >= 3
& ckG2 >= 39
& ckG4 >= 3
& 7 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 24

  Projection onto the parameters:
   dG3_u >= 17
& dG4_u >= 3

  /************************************************************/
  STATE 18:
  input: Input4, g1: G10010, g2: G2001, g3: G31010, g4: G401, automatically_generated_observer: loc_AutoGen_obs_2 ==>
& dG3_u + ckG4 >= 24
& dG4_u >= ckG4
& ckG2 >= 39
& ckG4 >= 3
& 7 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 0

  Projection onto the parameters:
   dG4_u >= 3
& dG3_u >= 17
& dG3_u + dG4_u >= 24

  /************************************************************/
  STATE 19:
  input: Input4, g1: G10010, g2: G2001, g3: G31010, g4: G401, automatically_generated_observer: loc_AutoGen_obs_1 ==>
& dG3_u + ckG4 >= 24
& dG4_u >= 3
& ckG2 >= 39
& ckG4 >= 10
& 16 >= ckG4
& s = 0
& ckG1 = 0
& ckG3 = 24

  Projection onto the parameters:
   dG3_u >= 8
& dG4_u >= 3

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1 via "dUp"
  s_1 -> s_2 via "qG1Down"
  s_2 -> s_3 via "ckUp"
  s_3 -> s_4 via "dDown"
  s_3 -> s_5 via "qG3Down"
  s_4 -> s_6 via "ckDown"
  s_4 -> s_7 via "qG3Down"
  s_5 -> s_8 via "dDown"
  s_5 -> s_9 via "qUp"
  s_7 -> s_10 via "ckDown"
  s_7 -> s_11 via "qUp"
  s_8 -> s_12 via "ckDown"
  s_8 -> s_13 via "qUp"
  s_9 -> s_14 via "dDown"
  s_10 -> s_18 via "qUp"
  s_11 -> s_17 via "ckDown"
  s_12 -> s_16 via "qUp"
  s_13 -> s_15 via "ckDown"
  s_14 -> s_19 via "ckDown"
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test PDFC: example with basic backward under-approximation',
		'input_files': ['PDFC8.imi'],
		'options'    : '-mode PDFC -output-result -depth-limit 5 -no-var-autoremove', #TODO: re-do without '-no-var-autoremove'
		'expectations' : [
			{'file': 'PDFC8.res' , 'content' : """
BEGIN CONSTRAINT
 p1 > 2
& 3 >= p1
OR
  p1 > 0
& 2 > p1
<good|bad>
 p1 > 3
OR
  p1 = 2
OR
  p1 = 0
END CONSTRAINT

------------------------------------------------------------
Constraint soundness          : possible under-approximation <good|bad> possible under-approximation
Termination                   : depth limit (1 successor unexplored)
Constraint nature             : good/bad
------------------------------------------------------------
Number of states              : 7
Number of transitions         : 7
Number of computed states     : 8
"""
			} #end result file
		] # end expectations
	} # end test case
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test PDFC: example with basic backward under-approximation and exact result',
		'input_files': ['PDFC8b.imi'],
		'options'    : '-mode PDFC -output-result -depth-limit 5 -no-var-autoremove', #TODO: re-do without '-no-var-autoremove'
		'expectations' : [
			{'file': 'PDFC8b.res' , 'content' : """
BEGIN CONSTRAINT
 p1 > 2
& 3 >= p1
OR
  p1 > 0
& 2 > p1
END CONSTRAINT

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : depth limit (1 successor unexplored)
Constraint nature             : good
------------------------------------------------------------
Number of states              : 7
Number of transitions         : 7
Number of computed states     : 8
"""
			} #end result file
		] # end expectations
	} # end test case
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test PDFC: another example with basic backward under-approximation',
		'input_files': ['PDFC9.imi'],
		'options'    : '-mode PDFC -output-result -depth-limit 5 -no-var-autoremove', #TODO: re-do without '-no-var-autoremove'
		'expectations' : [
			{'file': 'PDFC9.res' , 'content' : """
BEGIN CONSTRAINT
 p1 > 2
<good|bad>
 2 >= p1
& p1 >= 0
END CONSTRAINT

------------------------------------------------------------
Constraint soundness          : possible under-approximation <good|bad> possible under-approximation
Termination                   : depth limit (1 successor unexplored)
Constraint nature             : good/bad
------------------------------------------------------------
Number of states              : 7
Number of transitions         : 8
Number of computed states     : 9
"""
			} #end result file
		] # end expectations
	} # end test case
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test PDFC: again another example with basic backward under-approximation',
		'input_files': ['PDFC9b.imi'],
		'options'    : '-mode PDFC -output-result -depth-limit 5 -no-var-autoremove', #TODO: re-do without '-no-var-autoremove'
		'expectations' : [
			{'file': 'PDFC9b.res' , 'content' : """
BEGIN CONSTRAINT
 p1 > 2
<good|bad>
 2 >= p1
& p1 >= 0
END CONSTRAINT

------------------------------------------------------------
Constraint soundness          : possible under-approximation <good|bad> possible under-approximation
Termination                   : depth limit (1 successor unexplored)
Constraint nature             : good/bad
------------------------------------------------------------
Number of states              : 7
Number of transitions         : 8
Number of computed states     : 9
"""
			} #end result file
		] # end expectations
	} # end test case
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test the inverse method (flip-flop)',
		'input_files': ['flipflop.imi', 'flipflop.pi0'],
		'options'    : '-output-result',
		'expectations' : [
			{'file': 'flipflop.res' , 'content' : """
BEGIN CONSTRAINT
dG3_u + dG4_u >= 17 & dG3_u >= 8 & dG4_u >= 3 & 17 > dG3_u & 24 > dG3_u + dG4_u
END CONSTRAINT
			"""
			} #end result file
		] # end expectations
	} # end test case
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test the inverse method (SIMOP)',
		'input_files': ['simop.imi', 'simop.pi0'],
		'options'    : '-merge -no-random -output-result',
		'expectations' : [
			{'file': 'simop.res' , 'content' : """
BEGIN CONSTRAINT
500 >= COMct
    & COMct > 495
    & SIGmrt > 70 + 4*COMct
END CONSTRAINT
			"""
			} #end result file
		] # end expectations
	} # end test case
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test variants of IM: here IM',
		'input_files': ['testIM-IMK-IMunion.imi', 'testIM-IMK-IMunion.pi0'],
		'options'    : '-output-result',
		'expectations' : [
			{'file': 'testIM-IMK-IMunion.res' , 'content' : """
		  p = 2
		  """
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test variants of IM: here IMK',
		'input_files': ['testIM-IMK-IMunion.imi', 'testIM-IMK-IMunion.pi0'],
		'options'    : '-IMK -output-result',
		'expectations' : [
			{'file': 'testIM-IMK-IMunion.res' , 'content' : """
		 p > 1
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test variants of IM: here IMunion',
		'input_files': ['testIM-IMK-IMunion.imi', 'testIM-IMK-IMunion.pi0'],
		'options'    : '-IMunion -output-result',
		'expectations' : [
			{'file': 'testIM-IMK-IMunion.res' , 'content' : """
		4 >= p & p > 1
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test variants of IM (bis): here IM',
		'input_files': ['exVariantes.imi', 'exVariantes.pi0'],
		'options'    : '-output-result',
		'expectations' : [
			{'file': 'exVariantes.res' , 'content' : """
	p2 >= 3 & 5*p1 > p2 & p2 >= 4*p1
		  """
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test variants of IM (bis): here IMK',
		'input_files': ['exVariantes.imi', 'exVariantes.pi0'],
		'options'    : '-IMK -output-result -no-random',
		'expectations' : [
			{'file': 'exVariantes.res' , 'content' : """
 p2 > 2
& 5*p1 > p2
		  """
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test variants of IM (bis): here IMunion',
		'input_files': ['exVariantes.imi', 'exVariantes.pi0'],
		'options'    : '-IMunion -output-result -no-random',
		'expectations' : [
			{'file': 'exVariantes.res' , 'content' : """
		 5*p1 > p2 & p2 >= 3 OR 5*p1 > p2 & p2 > 2 & p2 >= 4*p1
		  """
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test IM on an incomplete example',
		'input_files': ['exIMnoncomplete.imi', 'exIMnoncomplete.pi0'],
		'options'    : '-output-result -no-random',
		'expectations' : [
			{'file': 'exIMnoncomplete.res' , 'content' : """
BEGIN CONSTRAINT
p1 >= 0
& p2 >= 0
& p3 > p1
END CONSTRAINT		  """
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test IMcomplete on an incomplete example',
		'input_files': ['exIMnoncomplete.imi', 'exIMnoncomplete.pi0'],
		'options'    : '-mode IMcomplete -output-result -no-random',
		'expectations' : [
			{'file': 'exIMnoncomplete.res' , 'content' : """
BEGIN CONSTRAINT
     p1 >= 0
    & p2 > p1
    & p3 >= 0
    OR
      p3 > p1
    & p2 >= 0
    & p1 >= p2
END CONSTRAINT		  """
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		# Test version             : 1
		# Test since               : 2019/05/30
		# Test for IMITATOR version: 2.11
		'purpose'    : 'Test PRP on a very simple example',
		'input_files': ['testEFcounterex.imi', 'testEFcounterex.pi0'],
		'options'    : '-mode PRP -merge -incl -output-result',
		'expectations' : [
			{'file': 'testEFcounterex.res' , 'content' : """
BEGIN CONSTRAINT
 p >= 0
& 1 > p
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} #end result file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test PRP (old version) on a simple example (good reference valuation)',
		'input_files': ['testPRP.imi', 'testPRP.pigood'],
		'options'    : '-PRP -output-result -output-states',
		'expectations' : [
			{'file': 'testPRP.res' , 'content' : """
BEGIN CONSTRAINT
	4 > p2
    & 3 > p1
    & p1 >= 0
    & p2 >= 0
END CONSTRAINT
		  """
			} # end result file
			,
			{'file': 'testPRP-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l1 ==>
& p1 >= 0
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 1:
  pta: l2 ==>
& p1 >= 0
& p2 >= 0
& x >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 2:
  pta: l3 ==>
& p1 >= x
& p2 >= 0
& x >= 0
& 1 >= p2
& x = y

  Projection onto the parameters:
   1 >= p2
& p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 3:
  pta: l4 ==>
& p1 >= p2
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p1 >= p2
& p2 >= 0

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1
  s_1 -> s_2
  s_1 -> s_3
  s_2 -> s_2
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test PRP on a simple example (good reference valuation)',
		'input_files': ['testPRP.imi', 'testPRP.pigood'],
		'options'    : '-mode PRP -output-result -output-states',
		'expectations' : [
			{'file': 'testPRP.res' , 'content' : """
BEGIN CONSTRAINT
	4 > p2
    & 3 > p1
    & p1 >= 0
    & p2 >= 0
END CONSTRAINT
		  """
			} # end result file
			,
			{'file': 'testPRP-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l1 ==>
& p1 >= 0
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 1:
  pta: l2 ==>
& p1 >= 0
& p2 >= 0
& x >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 2:
  pta: l3 ==>
& p1 >= x
& p2 >= 0
& x >= 0
& 1 >= p2
& x = y

  Projection onto the parameters:
   1 >= p2
& p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 3:
  pta: l4 ==>
& p1 >= p2
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p1 >= p2
& p2 >= 0

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1
  s_1 -> s_2
  s_1 -> s_3
  s_2 -> s_2
		  """
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test PRP (old version) on a simple example (bad reference valuation)',
		'input_files': ['testPRP.imi', 'testPRP.pibad'],
		'options'    : '-PRP -output-result -output-states',
		'expectations' : [
			{'file': 'testPRP.res' , 'content' : """
		 & p1 >= 0
OR
  p2 >= 0
& p1 >= 3
		  """
			} # end result file
			,
			{'file': 'testPRP-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l1 ==>
& p1 >= 0
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 1:
  pta: l2 ==>
& p1 >= 0
& p2 >= 0
& x >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 2:
  pta: locBad1 ==>
& p1 >= 0
& p2 >= 4
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 4
& p1 >= 0

  /************************************************************/
  STATE 3:
  pta: l4 ==>
& p1 >= p2
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p1 >= p2
& p2 >= 0

  /************************************************************/
  STATE 4:
  pta: locBad2 ==>
& p1 >= 3
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 3

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1
  s_0 -> s_2
  s_1 -> s_3
  s_1 -> s_4
		  """
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test PRP on a simple example (bad reference valuation)',
		'input_files': ['testPRP.imi', 'testPRP.pibad'],
		'options'    : '-mode PRP -output-result -output-states',
		'expectations' : [
			{'file': 'testPRP.res' , 'content' : """
		 & p1 >= 0
OR
  p2 >= 0
& p1 >= 3
		  """
			} # end result file
			,
			{'file': 'testPRP-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l1 ==>
& p1 >= 0
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 1:
  pta: l2 ==>
& p1 >= 0
& p2 >= 0
& x >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 2:
  pta: locBad1 ==>
& p1 >= 0
& p2 >= 4
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 4
& p1 >= 0

  /************************************************************/
  STATE 3:
  pta: l4 ==>
& p1 >= p2
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p1 >= p2
& p2 >= 0

  /************************************************************/
  STATE 4:
  pta: locBad2 ==>
& p1 >= 3
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 3

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1
  s_0 -> s_2
  s_1 -> s_3
  s_1 -> s_4
		  """
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test PRP (old version) on a simple example (looping reference valuation)',
		'input_files': ['testPRP.imi', 'testPRP.piloop'],
		'options'    : '-PRP -output-result -depth-limit 10 -output-states',
		'expectations' : [
			{'file': 'testPRP.res' , 'content' : """
 p2 >= 4
    & p1 >= 0
    OR
      p2 >= 0
    & p1 >= 3
		  """
			} # end result file
			,
			{'file': 'testPRP-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l1 ==>
& p1 >= 0
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 1:
  pta: l2 ==>
& p1 >= 0
& p2 >= 0
& x >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 2:
  pta: locBad1 ==>
& p1 >= 0
& p2 >= 4
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 4
& p1 >= 0

  /************************************************************/
  STATE 3:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 4:
  pta: l4 ==>
& p1 >= p2
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p1 >= p2
& p2 >= 0

  /************************************************************/
  STATE 5:
  pta: locBad2 ==>
& p1 >= 3
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 3

  /************************************************************/
  STATE 6:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 1 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 7:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 2 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 8:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 3 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 9:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 4 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 10:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 5 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 11:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 6 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 12:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 7 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 13:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 8 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1
  s_0 -> s_2
  s_0 -> s_3
  s_1 -> s_4
  s_1 -> s_5
  s_3 -> s_6
  s_6 -> s_7
  s_7 -> s_8
  s_8 -> s_9
  s_9 -> s_10
  s_10 -> s_11
  s_11 -> s_12
  s_12 -> s_13


		  """
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test PRP on a simple example (looping reference valuation)',
		'input_files': ['testPRP.imi', 'testPRP.piloop'],
		'options'    : '-mode PRP -output-result -depth-limit 10 -output-states',
		'expectations' : [
			{'file': 'testPRP.res' , 'content' : """
 p2 >= 4
    & p1 >= 0
    OR
      p2 >= 0
    & p1 >= 3
		  """
			} # end result file
			,
			{'file': 'testPRP-statespace.states' , 'content' : """
  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: l1 ==>
& p1 >= 0
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 1:
  pta: l2 ==>
& p1 >= 0
& p2 >= 0
& x >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 0

  /************************************************************/
  STATE 2:
  pta: locBad1 ==>
& p1 >= 0
& p2 >= 4
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 4
& p1 >= 0

  /************************************************************/
  STATE 3:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 4:
  pta: l4 ==>
& p1 >= p2
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p1 >= p2
& p2 >= 0

  /************************************************************/
  STATE 5:
  pta: locBad2 ==>
& p1 >= 3
& p2 >= 0
& y >= 0
& x = y

  Projection onto the parameters:
   p2 >= 0
& p1 >= 3

  /************************************************************/
  STATE 6:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 1 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 7:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 2 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 8:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 3 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 9:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 4 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 10:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 5 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 11:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 6 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 12:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 7 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  /************************************************************/
  STATE 13:
  pta: infiniteLoop ==>
& 1 >= x
& p1 >= 0
& p2 >= 5
& x >= 0
& x + 8 = y

  Projection onto the parameters:
   p2 >= 5
& p1 >= 0

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1
  s_0 -> s_2
  s_0 -> s_3
  s_1 -> s_4
  s_1 -> s_5
  s_3 -> s_6
  s_6 -> s_7
  s_7 -> s_8
  s_8 -> s_9
  s_9 -> s_10
  s_10 -> s_11
  s_11 -> s_12
  s_12 -> s_13


		  """
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode cover (grid)',
		'input_files': ['testBC-grid-plain.imi', 'testBC-grid4x4.v0'],
		'options'    : '-mode cover -output-result',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #1

 Pi1:
  p1 = 1
& p2 = 1

 K1:
 p2 >= 1
& p1 >= 1
& 2 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 5
Local number of transitions   : 4
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #2

 Pi2:
  p1 = 2
& p2 = 1

 K2:
 p2 >= 1
& p1 >= 2
& 2 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 6
Local number of transitions   : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #3

 Pi3:
  p1 = 3
& p2 = 1

 K3:
 p2 >= 1
& p1 >= 3
& 2 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 7
Local number of transitions   : 6
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #4

 Pi4:
  p1 = 4
& p2 = 1

 K4:
 p2 >= 1
& p1 >= 4
& 2 > p2
& 5 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 8
Local number of transitions   : 7
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #5

 Pi5:
  p1 = 1
& p2 = 2

 K5:
 p2 >= 2
& p1 >= 1
& 3 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 6
Local number of transitions   : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #6

 Pi6:
  p1 = 2
& p2 = 2

 K6:
 p2 >= 2
& p1 >= 2
& 3 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 7
Local number of transitions   : 6
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #7

 Pi7:
  p1 = 3
& p2 = 2

 K7:
 p2 >= 2
& p1 >= 3
& 3 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 8
Local number of transitions   : 7
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #8

 Pi8:
  p1 = 4
& p2 = 2

 K8:
 p2 >= 2
& p1 >= 4
& 3 > p2
& 5 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 9
Local number of transitions   : 8
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #9

 Pi9:
  p1 = 1
& p2 = 3

 K9:
 p2 >= 3
& p1 >= 1
& 4 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 7
Local number of transitions   : 6
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #10

 Pi10:
  p1 = 2
& p2 = 3

 K10:
 p2 >= 3
& p1 >= 2
& 4 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 8
Local number of transitions   : 7
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #11

 Pi11:
  p1 = 3
& p2 = 3

 K11:
 p2 >= 3
& p1 >= 3
& 4 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 9
Local number of transitions   : 8
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #12

 Pi12:
  p1 = 4
& p2 = 3

 K12:
 p2 >= 3
& p1 >= 4
& 4 > p2
& 5 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 10
Local number of transitions   : 9
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #13

 Pi13:
  p1 = 1
& p2 = 4

 K13:
 p2 >= 4
& p1 >= 1
& 5 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 8
Local number of transitions   : 7
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #14

 Pi14:
  p1 = 2
& p2 = 4

 K14:
 p2 >= 4
& p1 >= 2
& 5 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 9
Local number of transitions   : 8
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #15

 Pi15:
  p1 = 3
& p2 = 4

 K15:
 p2 >= 4
& p1 >= 3
& 5 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 10
Local number of transitions   : 9
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
 Tile #16

 Pi16:
  p1 = 4
& p2 = 4

 K16:
 p2 >= 4
& p1 >= 4
& 5 > p2
& 5 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 11
Local number of transitions   : 10
"""
			} # end BC file
			,
			# NOTE: actual result
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
GENERAL STATISTICS
(************************************************************)
------------------------------------------------------------
Number of integers in v0      : 16
Number of tiles computed      : 16
Coverage                      : integer-complete
Termination                   : regular termination
Number of unsuccessful points : 0
Average number of states      : 8.0
Average number of transitions : 7.0

"""
			} # end BC file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,


	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode cover (grid2)',
		'input_files': ['testBC-grid2-plain.imi', 'testBC-grid5x5.v0'],
		'options'    : '-mode cover -output-result',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)
			{'file': 'testBC-grid2-plain.res' , 'content' : """
(************************************************************)
 Tile #1

 Pi1:
  p1 = 0
& p2 = 0

 K1:
 p1 >= 0
& p2 >= 0
& 2 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 3
Local number of transitions   : 2
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
(************************************************************)
 Tile #2

 Pi2:
  p1 = 2
& p2 = 0

 K2:
 p1 >= 2
& p2 >= 0
& 2 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 4
Local number of transitions   : 3
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
(************************************************************)
 Tile #3

 Pi3:
  p1 = 4
& p2 = 0

 K3:
 p1 >= 4
& p2 >= 0
& 2 > p2
& 6 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 5
Local number of transitions   : 4
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
(************************************************************)
 Tile #4

 Pi4:
  p1 = 0
& p2 = 2

 K4:
 p1 >= 0
& p2 >= 2
& 4 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 4
Local number of transitions   : 3
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
(************************************************************)
 Tile #5

 Pi5:
  p1 = 2
& p2 = 2

 K5:
 p1 >= 2
& p2 >= 2
& 4 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 5
Local number of transitions   : 4
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
(************************************************************)
 Tile #6

 Pi6:
  p1 = 4
& p2 = 2

 K6:
 p1 >= 4
& p2 >= 2
& 4 > p2
& 6 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 6
Local number of transitions   : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
(************************************************************)
 Tile #7

 Pi7:
  p1 = 0
& p2 = 4

 K7:
 p1 >= 0
& p2 >= 4
& 6 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 5
Local number of transitions   : 4
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
(************************************************************)
 Tile #8

 Pi8:
  p1 = 2
& p2 = 4

 K8:
 p1 >= 2
& p2 >= 4
& 6 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 6
Local number of transitions   : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
(************************************************************)
 Tile #9

 Pi9:
  p1 = 4
& p2 = 4

 K9:
 p1 >= 4
& p2 >= 4
& 6 > p2
& 6 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 7
Local number of transitions   : 6
"""
			} # end BC file
			,
			# NOTE: actual result
			{'file': 'testBC-grid2-plain.res' , 'content' : """
(************************************************************)
GENERAL STATISTICS
(************************************************************)
------------------------------------------------------------
Number of integers in v0      : 36
Number of tiles computed      : 9
Coverage                      : integer-complete
Termination                   : regular termination
Number of unsuccessful points : 27
Average number of states      : 5.0
Average number of transitions : 4.0

"""
			} # end BC file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode cover + depth-limit (grid)',
		'input_files': ['testBC-grid-plain.imi', 'testBC-grid4x4.v0'],
		'options'    : '-mode cover -depth-limit 5 -output-result',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)
			#{'file': 'testBC-grid-plain.res' , 'content' : """
#(************************************************************)
 #Tile #1

 #Pi1:
  #p1 = 1
#& p2 = 1

 #K1:
 #p2 >= 1
#& p1 >= 1
#& 2 > p2
#& 2 > p1

#------------------------------------------------------------
#Constraint soundness          : possible over-approximation
#Termination                   : depth limit (1 successor unexplored)
#Constraint nature             : good
#------------------------------------------------------------
#Local number of states        : 5
#Local number of transitions   : 4
#"""
			#} # end BC file
			#,
			#{'file': 'testBC-grid-plain.res' , 'content' : """
#(************************************************************)
 #Tile #2

 #Pi2:
  #p1 = 2
#& p2 = 1

 #K2:
 #p2 >= 1
#& p1 >= 2
#& 3 > p1

#------------------------------------------------------------
#Constraint soundness          : possible over-approximation
#Termination                   : depth limit (1 successor unexplored)
#Constraint nature             : good
#------------------------------------------------------------
#Local number of states        : 5
#Local number of transitions   : 4
#"""
			#} # end BC file
			#,
			#{'file': 'testBC-grid-plain.res' , 'content' : """
#(************************************************************)
 #Tile #3

 #Pi3:
  #p1 = 3
#& p2 = 1

 #K3:
 #p2 >= 0
#& p1 >= 3
#& 4 > p1

#------------------------------------------------------------
#Constraint soundness          : possible over-approximation
#Termination                   : depth limit (1 successor unexplored)
#Constraint nature             : good
#------------------------------------------------------------
#Local number of states        : 5
#Local number of transitions   : 4
#"""
			#} # end BC file
			#,
			#{'file': 'testBC-grid-plain.res' , 'content' : """
#(************************************************************)
 #Tile #4

 #Pi4:
  #p1 = 4
#& p2 = 1

 #K4:
 #p1 >= 4
#& p2 >= 0

#------------------------------------------------------------
#Constraint soundness          : possible over-approximation
#Termination                   : depth limit (1 successor unexplored)
#Constraint nature             : good
#------------------------------------------------------------
#Local number of states        : 5
#Local number of transitions   : 4
#"""
			#} # end BC file
			#,
			#{'file': 'testBC-grid-plain.res' , 'content' : """
#(************************************************************)
 #Tile #5

 #Pi5:
  #p1 = 1
#& p2 = 2

 #K5:
 #p2 >= 2
#& p1 >= 1
#& 2 > p1

#------------------------------------------------------------
#Constraint soundness          : possible over-approximation
#Termination                   : depth limit (1 successor unexplored)
#Constraint nature             : good
#------------------------------------------------------------
#Local number of states        : 5
#Local number of transitions   : 4
#"""
			#} # end BC file
			#,
			# NOTE: actual result
			#{'file': 'testBC-grid-plain.res' , 'content' : """
#(************************************************************)
#GENERAL STATISTICS
#(************************************************************)
#------------------------------------------------------------
#Number of integers in v0      : 16
#Number of tiles computed      : 5
#Coverage                      : unknown
#Termination                   : regular termination
#Number of unsuccessful points : 11
#Average number of states      : 5.0
#Average number of transitions : 4.0
#"""
			#} # end BC file
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
GENERAL STATISTICS
(************************************************************)
------------------------------------------------------------
Number of integers in v0                : 16
Number of tiles computed                : 0
Coverage                                : empty
Termination                             : regular termination
Number of unsuccessful points           : 16
"""
			} # end BC file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode cover with depth limit (JLR15)',
		'input_files': ['JLR-TACAS13.imi', 'JLR-TACAS13.v0'],
		'options'    : '-mode cover -depth-limit 10 -output-result',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)
			{'file': 'JLR-TACAS13.res' , 'content' : """
(************************************************************)
 Tile #1

 Pi1:
  a = 1
& b = 0

 K1:
 a > b
& b >= 0
& 2 > b
& 10 >= a

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Local number of states                  : 1
Local number of transitions             : 0
"""
			} # end BC file
			,
			{'file': 'JLR-TACAS13.res' , 'content' : """
(************************************************************)
 Tile #2

 Pi2:
  a = 3
& b = 2

 K2:
 a > b
& b >= 2
& 10 >= a

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : bad
------------------------------------------------------------
Local number of states                  : 2
Local number of transitions             : 1
"""
			} # end BC file
			,
			{'file': 'JLR-TACAS13.res' , 'content' : """
    Number of integers in v0                : 121
    Number of tiles computed                : 2
    Coverage                                : unknown
    Termination                             : regular termination
    Number of unsuccessful points           : 119
    Average number of states                : 1.5
    Average number of transitions           : 0.5
"""
			} # end BC file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode sequential + depth limit (grid with loop)',
		'input_files': ['testBC-grid-plain-loop.imi', 'testBC-grid3x3.v0'],
		'options'    : '-mode cover -depth-limit 10 -output-result',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)
			{'file': 'testBC-grid-plain-loop.res' , 'content' : """
(************************************************************)
 Tile #1

 Pi1:
  p1 = 2
& p2 = 1

 K1:
 p2 >= 1
& p1 >= 2
& 2 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Local number of states                  : 6
Local number of transitions             : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain-loop.res' , 'content' : """
(************************************************************)
 Tile #2

 Pi2:
  p1 = 3
& p2 = 1

 K2:
 p2 >= 1
& p1 >= 3
& 2 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Local number of states                  : 7
Local number of transitions             : 6
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain-loop.res' , 'content' : """
(************************************************************)
 Tile #3

 Pi3:
  p1 = 1
& p2 = 2

 K3:
 p2 >= 2
& p1 >= 1
& 3 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Local number of states                  : 6
Local number of transitions             : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain-loop.res' , 'content' : """
(************************************************************)
 Tile #4

 Pi4:
  p1 = 2
& p2 = 2

 K4:
 p2 >= 2
& p1 >= 2
& 3 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness                    : possible under-approximation
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Local number of states                  : 7
Local number of transitions             : 6
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain-loop.res' , 'content' : """
(************************************************************)
 Tile #5

 Pi5:
  p1 = 3
& p2 = 2

 K5:
 p2 >= 2
& p1 >= 3
& 3 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness                    : possible under-approximation
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Local number of states                  : 8
Local number of transitions             : 7
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain-loop.res' , 'content' : """
(************************************************************)
 Tile #6

 Pi6:
  p1 = 1
& p2 = 3

 K6:
 p2 >= 3
& p1 >= 1
& 4 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Local number of states                  : 7
Local number of transitions             : 6
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain-loop.res' , 'content' : """
(************************************************************)
 Tile #7

 Pi7:
  p1 = 2
& p2 = 3

 K7:
 p2 >= 3
& p1 >= 2
& 4 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness                    : possible under-approximation
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Local number of states                  : 8
Local number of transitions             : 7
"""
			} # end BC file
			,
			# NOTE: actual result
			{'file': 'testBC-grid-plain-loop.res' , 'content' : """
(************************************************************)
GENERAL STATISTICS
(************************************************************)
------------------------------------------------------------
Number of integers in v0                : 9
Number of tiles computed                : 7
Coverage                                : unknown
Termination                             : regular termination
Number of unsuccessful points           : 2
Average number of states                : 7.0
Average number of transitions           : 6.0
"""
			} # end BC file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode cover + graphical output (flip-flop)',
		'input_files': ['flipflop.imi', 'flipflop.v0'],
		'options'    : '-mode cover -output-result -output-cart -output-graphics-source',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)
			{'file': 'flipflop.res' , 'content' : """
 Pi1:
  dG3_u = 8
& dG4_u = 3

 K1:
 dG3_u >= 8
& dG4_u >= 3
& 17 > dG3_u + dG4_u

"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
Tile #2

 Pi2:
  dG3_u = 14
& dG4_u = 3

 K2:
 dG3_u + dG4_u >= 17
& dG3_u >= 8
& dG4_u >= 3
& 17 > dG3_u
& 24 > dG3_u + dG4_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 Tile #3

 Pi3:
  dG3_u = 17
& dG4_u = 3

 K3:
 dG3_u >= 17
& dG4_u >= 3
& 24 > dG3_u + dG4_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
Tile #4

 Pi4:
  dG3_u = 21
& dG4_u = 3

 K4:
 dG3_u + dG4_u >= 24
& dG4_u >= 3
& 7 > dG4_u
& 24 > dG3_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
Tile #5

 Pi5:
  dG3_u = 24
& dG4_u = 3

 K5:
 dG3_u >= 24
& dG4_u >= 3
& 7 > dG4_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
Tile #6

 Pi6:
  dG3_u = 17
& dG4_u = 7

 K6:
 dG3_u >= 17
& dG4_u >= 7
& 24 > dG3_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
Tile #7

 Pi7:
  dG3_u = 24
& dG4_u = 7

 K7:
 dG3_u >= 24
& dG4_u >= 7

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : bad
------------------------------------------------------------
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 Tile #8

 Pi8:
  dG3_u = 16
& dG4_u = 8

 K8:
 dG3_u >= 8
& dG3_u + dG4_u >= 24
& 17 > dG3_u

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : bad
------------------------------------------------------------
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
Number of integers in v0      : 644
Number of tiles computed      : 8
Coverage                      : integer-complete
Termination                   : regular termination
Number of unsuccessful points : 636
Average number of states      : 15.1
Average number of transitions : 14.1
"""
			} # end BC file
			,
			{'file': 'flipflop_cart_points_2.txt' , 'content' : """8. 9.
8. 16.
17. 7.
17. 3.
14. 3.
8. 9.
# """
			} # end tile file
			,
			{'file': 'flipflop_cart_points_8.txt' , 'content' : """17. 31.
17. 7.
8. 16.
8. 31.
17. 31.
# """
			} # end tile file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode cover with tiles limit (flip-flop)',
		'input_files': ['flipflop.imi', 'flipflop.v0'],
		'options'    : '-mode cover -cart-tiles-limit 4 -output-result',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)
			{'file': 'flipflop.res' , 'content' : """
(************************************************************)
 Tile #1

 Pi1:
  dG3_u = 8
& dG4_u = 3

 K1:
 dG3_u >= 8
& dG4_u >= 3
& 17 > dG3_u + dG4_u

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 8
Local number of transitions   : 7
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
(************************************************************)
 Tile #2

 Pi2:
  dG3_u = 14
& dG4_u = 3

 K2:
 dG3_u + dG4_u >= 17
& dG3_u >= 8
& dG4_u >= 3
& 17 > dG3_u
& 24 > dG3_u + dG4_u

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 11
Local number of transitions   : 10
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
(************************************************************)
 Tile #3

 Pi3:
  dG3_u = 17
& dG4_u = 3

 K3:
 dG3_u >= 17
& dG4_u >= 3
& 24 > dG3_u + dG4_u

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 15
Local number of transitions   : 14
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
(************************************************************)
 Tile #4

 Pi4:
  dG3_u = 21
& dG4_u = 3

 K4:
 dG3_u + dG4_u >= 24
& dG4_u >= 3
& 7 > dG4_u
& 24 > dG3_u

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : bad
------------------------------------------------------------
Local number of states        : 17
Local number of transitions   : 16
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
------------------------------------------------------------
Number of integers in v0      : 644
Number of tiles computed      : 4
Coverage                      : unknown
Termination                   : tiles limit
Number of unsuccessful points : 10
Average number of states      : 12.7
Average number of transitions : 11.7
"""
			} # end BC file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode random (grid)',
		'input_files': ['testBC-grid-plain.imi', 'testBC-grid4x4.v0'],
		'options'    : '-mode random50 -output-result',
		'expectations' : [
			# WARNING: this algorithm is… random! hence no absolute guarantee to find the result (this said, a max_tries of 20 generally allows one to find all tiles with a good probability)
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 1
& p1 >= 1
& 2 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 5
Local number of transitions   : 4
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 1
& p1 >= 2
& 2 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 6
Local number of transitions   : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 1
& p1 >= 3
& 2 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 7
Local number of transitions   : 6
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 1
& p1 >= 4
& 2 > p2
& 5 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 8
Local number of transitions   : 7
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 2
& p1 >= 1
& 3 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 6
Local number of transitions   : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 2
& p1 >= 2
& 3 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 7
Local number of transitions   : 6
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 2
& p1 >= 3
& 3 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 8
Local number of transitions   : 7
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 2
& p1 >= 4
& 3 > p2
& 5 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 9
Local number of transitions   : 8
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 3
& p1 >= 1
& 4 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 7
Local number of transitions   : 6
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 3
& p1 >= 2
& 4 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 8
Local number of transitions   : 7
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 3
& p1 >= 3
& 4 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 9
Local number of transitions   : 8
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 3
& p1 >= 4
& 4 > p2
& 5 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 10
Local number of transitions   : 9
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 4
& p1 >= 1
& 5 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 8
Local number of transitions   : 7
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 4
& p1 >= 2
& 5 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 9
Local number of transitions   : 8
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 4
& p1 >= 3
& 5 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 10
Local number of transitions   : 9
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 4
& p1 >= 4
& 5 > p2
& 5 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 11
Local number of transitions   : 10
"""
			} # end BC file
			,
			# NOTE: actual result
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
GENERAL STATISTICS
(************************************************************)
------------------------------------------------------------
Number of integers in v0      : 16
Number of tiles computed      : 16
Coverage                      : unknown
Termination                   : regular termination

"""
			} # end BC file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode random (grid2)',
		'input_files': ['testBC-grid2-plain.imi', 'testBC-grid5x5.v0'],
		'options'    : '-mode random75 -output-result',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 0
& p2 >= 0
& 2 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 3
Local number of transitions   : 2
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 2
& p2 >= 0
& 2 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 4
Local number of transitions   : 3
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 4
& p2 >= 0
& 2 > p2
& 6 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 5
Local number of transitions   : 4
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 0
& p2 >= 2
& 4 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 4
Local number of transitions   : 3
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 2
& p2 >= 2
& 4 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 5
Local number of transitions   : 4
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 4
& p2 >= 2
& 4 > p2
& 6 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 6
Local number of transitions   : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 0
& p2 >= 4
& 6 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 5
Local number of transitions   : 4
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 2
& p2 >= 4
& 6 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 6
Local number of transitions   : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 4
& p2 >= 4
& 6 > p2
& 6 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 7
Local number of transitions   : 6
"""
			} # end BC file
			,
			# NOTE: actual result
			{'file': 'testBC-grid2-plain.res' , 'content' : """
(************************************************************)
GENERAL STATISTICS
(************************************************************)
------------------------------------------------------------
Number of integers in v0      : 36
Number of tiles computed      : 9
Coverage                      : unknown
Termination                   : regular termination
"""
			} # end BC file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode random (flip-flop)',
		'input_files': ['flipflop.imi', 'flipflop.v0'],
		'options'    : '-mode random200 -output-result',
		'expectations' : [
			# WARNING: this algorithm is… random! hence no absolute guarantee to find the result (this said, a max_tries of 200 generally allows one to find all tiles with a good probability)
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)… and to check them separately as the order is of course unknown
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 8
& dG4_u >= 3
& 17 > dG3_u + dG4_u

"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u + dG4_u >= 17
& dG3_u >= 8
& dG4_u >= 3
& 17 > dG3_u
& 24 > dG3_u + dG4_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 17
& dG4_u >= 3
& 24 > dG3_u + dG4_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u + dG4_u >= 24
& dG4_u >= 3
& 7 > dG4_u
& 24 > dG3_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 24
& dG4_u >= 3
& 7 > dG4_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 17
& dG4_u >= 7
& 24 > dG3_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 24
& dG4_u >= 7

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : bad
------------------------------------------------------------
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 8
& dG3_u + dG4_u >= 24
& 17 > dG3_u

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : bad
------------------------------------------------------------
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
Average number of states      : 15.1
Average number of transitions : 14.1
"""
			} # end BC file
			,
			# NOTE: impossible to check graphics source, as the order of the tiles is not known
			#{'file': 'flipflop_cart_points_2.txt' , 'content' : """14. 3.
#8. 9.
#8. 16.
#17. 7.
#17. 3.
#14. 3.
## """
			#} # end tile file
			#,
			#{'file': 'flipflop_cart_points_8.txt' , 'content' : """17. 31.
#17. 7.
#8. 16.
#8. 31.
#17. 31.
## """
			#} # end tile file
			#,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode random+seq',
		'input_files': ['flipflop.imi', 'flipflop.v0'],
		'options'    : '-mode randomseq3 -output-result',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)… and to check them separately as the order is of course unknown
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 8
& dG4_u >= 3
& 17 > dG3_u + dG4_u

"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u + dG4_u >= 17
& dG3_u >= 8
& dG4_u >= 3
& 17 > dG3_u
& 24 > dG3_u + dG4_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 17
& dG4_u >= 3
& 24 > dG3_u + dG4_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u + dG4_u >= 24
& dG4_u >= 3
& 7 > dG4_u
& 24 > dG3_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 24
& dG4_u >= 3
& 7 > dG4_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 17
& dG4_u >= 7
& 24 > dG3_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 24
& dG4_u >= 7

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : bad
------------------------------------------------------------
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 8
& dG3_u + dG4_u >= 24
& 17 > dG3_u

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : bad
------------------------------------------------------------
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
Number of integers in v0      : 644
Number of tiles computed      : 8
Coverage                      : integer-complete
Termination                   : regular termination
"""
			} # end BC file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode shuffle (grid)',
		'input_files': ['testBC-grid-plain.imi', 'testBC-grid4x4.v0'],
		'options'    : '-mode shuffle -output-result',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 1
& p1 >= 1
& 2 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 5
Local number of transitions   : 4
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 1
& p1 >= 2
& 2 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 6
Local number of transitions   : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 1
& p1 >= 3
& 2 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 7
Local number of transitions   : 6
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 1
& p1 >= 4
& 2 > p2
& 5 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 8
Local number of transitions   : 7
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 2
& p1 >= 1
& 3 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 6
Local number of transitions   : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 2
& p1 >= 2
& 3 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 7
Local number of transitions   : 6
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 2
& p1 >= 3
& 3 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 8
Local number of transitions   : 7
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 2
& p1 >= 4
& 3 > p2
& 5 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 9
Local number of transitions   : 8
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 3
& p1 >= 1
& 4 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 7
Local number of transitions   : 6
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 3
& p1 >= 2
& 4 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 8
Local number of transitions   : 7
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 3
& p1 >= 3
& 4 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 9
Local number of transitions   : 8
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 3
& p1 >= 4
& 4 > p2
& 5 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 10
Local number of transitions   : 9
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 4
& p1 >= 1
& 5 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 8
Local number of transitions   : 7
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 4
& p1 >= 2
& 5 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 9
Local number of transitions   : 8
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 4
& p1 >= 3
& 5 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 10
Local number of transitions   : 9
"""
			} # end BC file
			,
			{'file': 'testBC-grid-plain.res' , 'content' : """
:
 p2 >= 4
& p1 >= 4
& 5 > p2
& 5 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 11
Local number of transitions   : 10
"""
			} # end BC file
			,
			# NOTE: actual result
			{'file': 'testBC-grid-plain.res' , 'content' : """
(************************************************************)
GENERAL STATISTICS
(************************************************************)
------------------------------------------------------------
Number of integers in v0      : 16
Number of tiles computed      : 16
Coverage                      : integer-complete
Termination                   : regular termination
Number of unsuccessful points : 0
Average number of states      : 8.0
Average number of transitions : 7.0
"""
			} # end BC file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode shuffle (grid2)',
		'input_files': ['testBC-grid2-plain.imi', 'testBC-grid5x5.v0'],
		'options'    : '-mode shuffle -output-result',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 0
& p2 >= 0
& 2 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 3
Local number of transitions   : 2
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 2
& p2 >= 0
& 2 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 4
Local number of transitions   : 3
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 4
& p2 >= 0
& 2 > p2
& 6 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 5
Local number of transitions   : 4
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 0
& p2 >= 2
& 4 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 4
Local number of transitions   : 3
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 2
& p2 >= 2
& 4 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 5
Local number of transitions   : 4
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 4
& p2 >= 2
& 4 > p2
& 6 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 6
Local number of transitions   : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 0
& p2 >= 4
& 6 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 5
Local number of transitions   : 4
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 2
& p2 >= 4
& 6 > p2
& 4 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 6
Local number of transitions   : 5
"""
			} # end BC file
			,
			{'file': 'testBC-grid2-plain.res' , 'content' : """
:
 p1 >= 4
& p2 >= 4
& 6 > p2
& 6 > p1

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : good
------------------------------------------------------------
Local number of states        : 7
Local number of transitions   : 6
"""
			} # end BC file
			,
			# NOTE: actual result
			{'file': 'testBC-grid2-plain.res' , 'content' : """
(************************************************************)
GENERAL STATISTICS
(************************************************************)
------------------------------------------------------------
Number of integers in v0      : 36
Number of tiles computed      : 9
Coverage                      : integer-complete
Termination                   : regular termination
Number of unsuccessful points : 27
Average number of states      : 5.0
Average number of transitions : 4.0
"""
			} # end BC file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode shuffle (flip-flop)',
		'input_files': ['flipflop.imi', 'flipflop.v0'],
		'options'    : '-mode shuffle -output-result',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)… and to check them separately as the order is of course unknown
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 8
& dG4_u >= 3
& 17 > dG3_u + dG4_u

"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u + dG4_u >= 17
& dG3_u >= 8
& dG4_u >= 3
& 17 > dG3_u
& 24 > dG3_u + dG4_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 17
& dG4_u >= 3
& 24 > dG3_u + dG4_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u + dG4_u >= 24
& dG4_u >= 3
& 7 > dG4_u
& 24 > dG3_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 24
& dG4_u >= 3
& 7 > dG4_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 17
& dG4_u >= 7
& 24 > dG3_u
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 24
& dG4_u >= 7

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : bad
------------------------------------------------------------
"""
			} # end BC file
			,
			{'file': 'flipflop.res' , 'content' : """
 dG3_u >= 8
& dG3_u + dG4_u >= 24
& 17 > dG3_u

------------------------------------------------------------
Constraint soundness          : exact
Termination                   : regular termination
Constraint nature             : bad
------------------------------------------------------------
"""
			} # end BC file
			,
			# NOTE: the actual result
			{'file': 'flipflop.res' , 'content' : """
Number of integers in v0      : 644
Number of tiles computed      : 8
Coverage                      : integer-complete
Termination                   : regular termination
Number of unsuccessful points : 636
Average number of states      : 15.1
Average number of transitions : 14.1
"""
			} # end BC file			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test BC in mode cover (on the case study BC vs. PRPC)',
		'input_files': ['diffBCPRPC.imi', 'diffBCPRPC.v0'],
		'options'    : '-mode cover -no-random -output-result',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)
			{'file': 'diffBCPRPC.res' , 'content' : """
(************************************************************)
 Tile #1

 Pi1:
  p1 = 0
& p2 = 0

 K1:
 p2 >= 0
& p1 >= 0
& 1 > p2
& 1 > p1

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Local number of states                  : 8
Local number of transitions             : 12
"""
			} # end BC file
			,
			{'file': 'diffBCPRPC.res' , 'content' : """
(************************************************************)
 Tile #2

 Pi2:
  p1 = 1
& p2 = 0

 K2:
 p2 >= 0
& p1 >= 1
& 1 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Local number of states                  : 8
Local number of transitions             : 12
"""
			} # end BC file
			,
			{'file': 'diffBCPRPC.res' , 'content' : """
(************************************************************)
 Tile #3

 Pi3:
  p1 = 2
& p2 = 0

 K3:
 p2 >= 0
& p1 >= 2
& 1 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : bad
------------------------------------------------------------
Local number of states                  : 7
Local number of transitions             : 10
"""
			} # end BC file
			,
			{'file': 'diffBCPRPC.res' , 'content' : """
(************************************************************)
 Tile #4

 Pi4:
  p1 = 3
& p2 = 0

 K4:
 p2 >= 0
& p1 >= 3
& 1 > p2
& 4 >= p1

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : bad
------------------------------------------------------------
Local number of states                  : 7
Local number of transitions             : 10
"""
			} # end BC file
			,
			{'file': 'diffBCPRPC.res' , 'content' : """
(************************************************************)
 Tile #5

 Pi5:
  p1 = 0
& p2 = 1

 K5:
 p2 >= 1
& p1 >= 0
& 2 > p2
& 1 > p1

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Local number of states                  : 7
Local number of transitions             : 11
"""
			} # end BC file
			,
			{'file': 'diffBCPRPC.res' , 'content' : """
(************************************************************)
 Tile #6

 Pi6:
  p1 = 1
& p2 = 1

 K6:
 p2 >= 1
& p1 >= 1
& 2 > p2
& 2 > p1

------------------------------------------------------------
Constraint soundness                    : possible under-approximation
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Local number of states                  : 8
Local number of transitions             : 12
"""
			} # end BC file
			,
			{'file': 'diffBCPRPC.res' , 'content' : """
(************************************************************)
 Tile #7

 Pi7:
  p1 = 2
& p2 = 1

 K7:
 p2 >= 1
& p1 >= 2
& 2 > p2
& 3 > p1

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : bad
------------------------------------------------------------
Local number of states                  : 7
Local number of transitions             : 10
"""
			} # end BC file
			,
			{'file': 'diffBCPRPC.res' , 'content' : """
(************************************************************)
 Tile #8

 Pi8:
  p1 = 3
& p2 = 1

 K8:
 p2 >= 1
& p1 >= 3
& 2 > p2
& 4 >= p1

------------------------------------------------------------
Constraint soundness                    : possible under-approximation
Termination                             : regular termination
Constraint nature                       : bad
------------------------------------------------------------
Local number of states                  : 7
Local number of transitions             : 10
"""
			} # end BC file
			,
			{'file': 'diffBCPRPC.res' , 'content' : """
(************************************************************)
 Tile #9

 Pi9:
  p1 = 0
& p2 = 2

 K9:
 p1 >= 0
& p2 >= 2
& 4 >= p2
& 2 > p1

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : bad
------------------------------------------------------------
Local number of states                  : 7
Local number of transitions             : 10
"""
			} # end BC file
			,
			{'file': 'diffBCPRPC.res' , 'content' : """
(************************************************************)
 Tile #10

 Pi10:
  p1 = 2
& p2 = 2

 K10:
 p1 >= 2
& p2 >= 2
& 4 >= p2
& 4 >= p1

------------------------------------------------------------
Constraint soundness                    : possible under-approximation
Termination                             : regular termination
Constraint nature                       : bad
------------------------------------------------------------
Local number of states                  : 8
Local number of transitions             : 11
"""
			} # end BC file
			,
			{'file': 'diffBCPRPC.res' , 'content' : """
------------------------------------------------------------
Number of integers in v0                : 25
Number of tiles computed                : 10
Coverage                                : integer-complete
Termination                             : regular termination
Number of unsuccessful points           : 15
Average number of states                : 7.4
Average number of transitions           : 10.8
"""
			} # end BC file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test PRPC (on the case study BC vs. PRPC)',
		'input_files': ['diffBCPRPC.imi', 'diffBCPRPC.v0'],
		'options'    : '-mode PRPC -no-random -output-result',
		'expectations' : [
			{'file': 'diffBCPRPC.res' , 'content' : """
BEGIN CONSTRAINT
 2 > p1
& p2 >= 0
& 2 > p2
& p1 >= 0
<good|bad>
 p2 >= 0
& p1 >= 2
& 4 >= p1
& 4 >= p2
OR
  p2 >= 2
& p1 >= 0
& 4 >= p1
& 4 >= p2
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact <good|bad> exact
Termination                             : regular termination
Constraint nature                       : good/bad
"""
			} # end BC file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test PRPC (old version) in mode cover with depth limit (JLR15)',
		'input_files': ['JLR-TACAS13.imi', 'JLR-TACAS13.v0'],
		'options'    : '-mode cover -PRP -depth-limit 10 -output-result',
		'expectations' : [
			# NOTE: no other way for now that checking separately the constraints (because the computation times may of course differ)
			{'file': 'JLR-TACAS13.res' , 'content' : """
(************************************************************)
 Tile #1

 Pi1:
  a = 1
& b = 0

 K1:
 2 > b
& b >= 0
& a > b
& 10 >= a

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
Local number of states                  : 1
Local number of transitions             : 0
"""
			} # end BC file
			,
			{'file': 'JLR-TACAS13.res' , 'content' : """
(************************************************************)
 Tile #2

 Pi2:
  a = 0
& b = 1

 K2:
 a >= 0
& 9*b >= 2
& 10 >= b
& b >= a


------------------------------------------------------------
Constraint soundness                    : possible under-approximation
Termination                             : depth limit (1 successor unexplored)
Constraint nature                       : bad
------------------------------------------------------------
Local number of states                  : 18
Local number of transitions             : 17
"""
			} # end BC file
			,
			{'file': 'JLR-TACAS13.res' , 'content' : """
(************************************************************)
 Tile #3

 Pi3:
  a = 3
& b = 2

 K3:
 b >= 2
& a >= 0
& 10 >= a
& 10 >= b

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : bad
------------------------------------------------------------
Local number of states                  : 2
Local number of transitions             : 1
"""
			} # end BC file
			,
			{'file': 'JLR-TACAS13.res' , 'content' : """
(************************************************************)
GENERAL STATISTICS
(************************************************************)
------------------------------------------------------------
Number of integers in v0                : 121
Number of tiles computed                : 3
Coverage                                : unknown
Termination                             : regular termination
Number of unsuccessful points           : 118
Average number of states                : 7.0
Average number of transitions           : 6.0
"""
			} # end BC file
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Simple example without merging',
		'input_files': ['exActionsNonPreserved.imi'],
		'options'    : '-mode statespace -output-states',
		'expectations' : [
			{'file': 'exActionsNonPreserved-statespace.states' , 'content' : """
		*/

  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: L1 ==>
& 2 >= x
& p >= 0
& x >= 0

  Projection onto the parameters:
   p >= 0

  /************************************************************/
  STATE 1:
  pta: L2 ==>
& p >= 0
& x >= 2
& 2 >= p

  Projection onto the parameters:
   2 >= p
& p >= 0

  /************************************************************/
  STATE 2:
  pta: L2 ==>
& p >= 2
& x >= 2

  Projection onto the parameters:
   p >= 2

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1 via "a"
  s_0 -> s_2 via "b"
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Simple example with merging',
		'input_files': ['exActionsNonPreserved.imi'],
		'options'    : '-mode statespace -output-states -merge',
		'expectations' : [
			{'file': 'exActionsNonPreserved-statespace.states' , 'content' : """
		*/

  DESCRIPTION OF THE STATES

  /************************************************************/
  INITIAL
  STATE 0:
  pta: L1 ==>
& 2 >= x
& p >= 0
& x >= 0

  Projection onto the parameters:
   p >= 0

  /************************************************************/
  STATE 1:
  pta: L2 ==>
& p >= 0
& x >= 2

  Projection onto the parameters:
   p >= 0

  DESCRIPTION OF THE TRANSITIONS
  s_0 -> s_1 via "a"
  s_0 -> s_1 via "b"
  """
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test the model printer',
		'input_files': ['Sched5.imi'],
		'options'    : '-PTA2IMI',
		'expectations' : [
			{'file': 'Sched5-regenerated.imi' , 'content' : """
 ************************************************************)
var
	t1_c, t1_d, t1_urgent, t1_arr_x, t2_c, t2_d, t2_urgent, t2_arr_x, t3_c, t3_d, t3_urgent, t3_arr_x, t4_c, t4_d, t4_urgent, t4_arr_x, t5_c, t5_d, t5_urgent, t5_arr_x, CPU1_urgent
		: clock;

	t4_C, t5_C
		: parameter;


(************************************************************)
 automaton Task_t1
(************************************************************)
 synclabs: t1_arr_event, t1_arr, t1_dis, t1_miss, t1_end;


loc t1_loc_idle: invariant True
	when True do {t1_urgent := 0}  sync t1_arr_event goto t1_loc_act_event;

loc t1_loc_act_event: invariant 0 >= t1_urgent
	when  t1_urgent = 0 do {t1_c := 0, t1_d := 0} sync t1_arr goto t1_loc_act;

loc t1_loc_act: invariant 8 >= t1_d stop{t1_c}
	when True do {} sync t1_dis goto t1_loc_exe;
	when  t1_d >= 8 do {} sync t1_miss goto t1_loc_miss;

loc t1_loc_exe: invariant 8 >= t1_d
& 2 >= t1_c
	when  t1_d >= 8
& 2 > t1_c do {}  sync t1_miss goto t1_loc_miss;
	when  t1_c = 2 do {} sync t1_end goto t1_loc_idle;

loc t1_loc_miss: invariant True
 end (* Task_t1 *)
(************************************************************)


(************************************************************)
 automaton Periodic_t1_arr
(************************************************************)
 synclabs: t1_arr_event;


loc t1_arr_loc_arr: invariant  8 >= t1_arr_x
	when  t1_arr_x = 8 do {t1_arr_x := 0}  sync t1_arr_event goto t1_arr_loc_arr;
 end (* Periodic_t1_arr *)
(************************************************************)


(************************************************************)
 automaton Task_t2
(************************************************************)
 synclabs: t2_arr_event, t2_arr, t2_dis, t2_miss, t2_pre, t2_end;


loc t2_loc_idle: invariant True
	when True do {t2_urgent := 0}  sync t2_arr_event goto t2_loc_act_event;

loc t2_loc_act_event: invariant  0 >= t2_urgent
	when  t2_urgent = 0 do {t2_c := 0, t2_d := 0}  sync t2_arr goto t2_loc_act;

loc t2_loc_act: invariant  20 >= t2_d stop{t2_c}
	when True do {}  sync t2_dis goto t2_loc_exe;
	when  t2_d >= 20 do {}  sync t2_miss goto t2_loc_miss;

loc t2_loc_exe: invariant  20 >= t2_d
& 5 >= t2_c
	when  5 > t2_c do {}  sync t2_pre goto t2_loc_act;
	when  t2_d >= 20
& 5 > t2_c do {}  sync t2_miss goto t2_loc_miss;
	when  t2_c = 5 do {}  sync t2_end goto t2_loc_idle;

loc t2_loc_miss: invariant True
 end (* Task_t2 *)
(************************************************************)


(************************************************************)
 automaton Periodic_t2_arr
(************************************************************)
 synclabs: t2_arr_event;


loc t2_arr_loc_arr: invariant  20 >= t2_arr_x
	when  t2_arr_x = 20 do {t2_arr_x := 0}  sync t2_arr_event goto t2_arr_loc_arr;
 end (* Periodic_t2_arr *)
(************************************************************)


(************************************************************)
 automaton Task_t3
(************************************************************)
 synclabs: t3_arr_event, t3_arr, t3_dis, t3_miss, t3_pre, t3_end;


loc t3_loc_idle: invariant True
	when True do {t3_urgent := 0}  sync t3_arr_event goto t3_loc_act_event;

loc t3_loc_act_event: invariant  0 >= t3_urgent
	when  t3_urgent = 0 do {t3_c := 0, t3_d := 0}  sync t3_arr goto t3_loc_act;

loc t3_loc_act: invariant  50 >= t3_d stop{t3_c}
	when True do {}  sync t3_dis goto t3_loc_exe;
	when  t3_d >= 50 do {}  sync t3_miss goto t3_loc_miss;

loc t3_loc_exe: invariant  50 >= t3_d
& 8 >= t3_c
	when  8 > t3_c do {}  sync t3_pre goto t3_loc_act;
	when  t3_d >= 50
& 8 > t3_c do {}  sync t3_miss goto t3_loc_miss;
	when  t3_c = 8 do {}  sync t3_end goto t3_loc_idle;

loc t3_loc_miss: invariant True
 end (* Task_t3 *)
(************************************************************)


(************************************************************)
 automaton Periodic_t3_arr
(************************************************************)
 synclabs: t3_arr_event;


loc t3_arr_loc_arr: invariant  50 >= t3_arr_x
	when  t3_arr_x = 50 do {t3_arr_x := 0}  sync t3_arr_event goto t3_arr_loc_arr;
 end (* Periodic_t3_arr *)
(************************************************************)


(************************************************************)
 automaton Task_t4
(************************************************************)
 synclabs: t4_arr_event, t4_arr, t4_dis, t4_miss, t4_pre, t4_end;


loc t4_loc_idle: invariant True
	when True do {t4_urgent := 0}  sync t4_arr_event goto t4_loc_act_event;

loc t4_loc_act_event: invariant  0 >= t4_urgent
	when  t4_urgent = 0 do {t4_c := 0, t4_d := 0}  sync t4_arr goto t4_loc_act;

loc t4_loc_act: invariant  100 >= t4_d stop{t4_c}
	when True do {}  sync t4_dis goto t4_loc_exe;
	when  t4_d >= 100 do {}  sync t4_miss goto t4_loc_miss;

loc t4_loc_exe: invariant  t4_C >= t4_c
& 100 >= t4_d
	when  t4_C > t4_c do {}  sync t4_pre goto t4_loc_act;
	when  t4_C > t4_c
& t4_d >= 100 do {}  sync t4_miss goto t4_loc_miss;
	when  t4_C = t4_c do {}  sync t4_end goto t4_loc_idle;

loc t4_loc_miss: invariant True
 end (* Task_t4 *)
(************************************************************)


(************************************************************)
 automaton Periodic_t4_arr
(************************************************************)
 synclabs: t4_arr_event;


loc t4_arr_loc_arr: invariant  100 >= t4_arr_x
	when  t4_arr_x = 100 do {t4_arr_x := 0}  sync t4_arr_event goto t4_arr_loc_arr;
 end (* Periodic_t4_arr *)
(************************************************************)


(************************************************************)
 automaton Task_t5
(************************************************************)
 synclabs: t5_arr_event, t5_arr, t5_dis, t5_miss, t5_pre, t5_end;


loc t5_loc_idle: invariant True
	when True do {t5_urgent := 0}  sync t5_arr_event goto t5_loc_act_event;

loc t5_loc_act_event: invariant  0 >= t5_urgent
	when  t5_urgent = 0 do {t5_c := 0, t5_d := 0}  sync t5_arr goto t5_loc_act;

loc t5_loc_act: invariant  200 >= t5_d stop{t5_c}
	when True do {}  sync t5_dis goto t5_loc_exe;
	when  t5_d >= 200 do {}  sync t5_miss goto t5_loc_miss;

loc t5_loc_exe: invariant  t5_C >= t5_c
& 200 >= t5_d
	when  t5_C > t5_c do {}  sync t5_pre goto t5_loc_act;
	when  t5_C > t5_c
& t5_d >= 200 do {}  sync t5_miss goto t5_loc_miss;
	when  t5_C = t5_c do {}  sync t5_end goto t5_loc_idle;

loc t5_loc_miss: invariant True
 end (* Task_t5 *)
(************************************************************)


(************************************************************)
 automaton Periodic_t5_arr
(************************************************************)
 synclabs: t5_arr_event;


loc t5_arr_loc_arr: invariant  200 >= t5_arr_x
	when  t5_arr_x = 200 do {t5_arr_x := 0}  sync t5_arr_event goto t5_arr_loc_arr;
 end (* Periodic_t5_arr *)
(************************************************************)


(************************************************************)
 automaton sched_CPU1
(************************************************************)
 synclabs: t1_arr, t2_arr, t3_arr, t4_arr, t5_arr, t1_dis, t2_dis, t3_dis, t4_dis, t5_dis, t5_end, t5_pre, t4_end, t4_pre, t3_end, t3_pre, t2_end, t2_pre, t1_end;


loc CPU1_loc_: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1;
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_At2;
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_At3;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_At4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_At5;

loc CPU1_loc_At1: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1;

loc CPU1_loc_At2: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2;

loc CPU1_loc_At3: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_dis goto CPU1_loc_Rt3;

loc CPU1_loc_At4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_dis goto CPU1_loc_Rt4;

loc CPU1_loc_At5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t5_dis goto CPU1_loc_Rt5;

loc CPU1_loc_Rt5: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt5;
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_At2Rt5;
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_At3Rt5;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_At4Rt5;
	when True do {CPU1_urgent := 0}  sync t5_end goto CPU1_loc_Et5;

loc CPU1_loc_Et5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  (* sync nosync_1*)  goto CPU1_loc_stop;

loc CPU1_loc_At1Rt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t5_pre goto CPU1_loc_At1Wt5;

loc CPU1_loc_At1Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt5;

loc CPU1_loc_At2Rt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t5_pre goto CPU1_loc_At2Wt5;

loc CPU1_loc_At2Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt5;

loc CPU1_loc_At3Rt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t5_pre goto CPU1_loc_At3Wt5;

loc CPU1_loc_At3Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_dis goto CPU1_loc_Rt3Wt5;

loc CPU1_loc_At4Rt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t5_pre goto CPU1_loc_At4Wt5;

loc CPU1_loc_At4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_dis goto CPU1_loc_Rt4Wt5;

loc CPU1_loc_Rt4: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt4;
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_At2Rt4;
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_At3Rt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt4Wt5;
	when True do {CPU1_urgent := 0}  sync t4_end goto CPU1_loc_Et4;

loc CPU1_loc_Et4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  (* sync nosync_2*)  goto CPU1_loc_stop;

loc CPU1_loc_At1Rt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_pre goto CPU1_loc_At1Wt4;

loc CPU1_loc_At1Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt4;

loc CPU1_loc_At2Rt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_pre goto CPU1_loc_At2Wt4;

loc CPU1_loc_At2Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt4;

loc CPU1_loc_At3Rt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_pre goto CPU1_loc_At3Wt4;

loc CPU1_loc_At3Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_dis goto CPU1_loc_Rt3Wt4;

loc CPU1_loc_Rt4Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt4Wt5;
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_At2Rt4Wt5;
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_At3Rt4Wt5;
	when True do {CPU1_urgent := 0}  sync t4_end goto CPU1_loc_Et4Wt5;

loc CPU1_loc_Et4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t5_dis goto CPU1_loc_Rt5;

loc CPU1_loc_At1Rt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_pre goto CPU1_loc_At1Wt4Wt5;

loc CPU1_loc_At1Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt4Wt5;

loc CPU1_loc_At2Rt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_pre goto CPU1_loc_At2Wt4Wt5;

loc CPU1_loc_At2Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt4Wt5;

loc CPU1_loc_At3Rt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_pre goto CPU1_loc_At3Wt4Wt5;

loc CPU1_loc_At3Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_dis goto CPU1_loc_Rt3Wt4Wt5;

loc CPU1_loc_Rt3: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt3;
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_At2Rt3;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt3Wt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt3Wt5;
	when True do {CPU1_urgent := 0}  sync t3_end goto CPU1_loc_Et3;

loc CPU1_loc_Et3: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  (* sync nosync_3*)  goto CPU1_loc_stop;

loc CPU1_loc_At1Rt3: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_pre goto CPU1_loc_At1Wt3;

loc CPU1_loc_At1Wt3: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt3;

loc CPU1_loc_At2Rt3: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_pre goto CPU1_loc_At2Wt3;

loc CPU1_loc_At2Wt3: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt3;

loc CPU1_loc_Rt3Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt3Wt5;
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_At2Rt3Wt5;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t3_end goto CPU1_loc_Et3Wt5;

loc CPU1_loc_Et3Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t5_dis goto CPU1_loc_Rt5;

loc CPU1_loc_At1Rt3Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_pre goto CPU1_loc_At1Wt3Wt5;

loc CPU1_loc_At1Wt3Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt3Wt5;

loc CPU1_loc_At2Rt3Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_pre goto CPU1_loc_At2Wt3Wt5;

loc CPU1_loc_At2Wt3Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt3Wt5;

loc CPU1_loc_Rt3Wt4: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt3Wt4;
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_At2Rt3Wt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t3_end goto CPU1_loc_Et3Wt4;

loc CPU1_loc_Et3Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_dis goto CPU1_loc_Rt4;

loc CPU1_loc_At1Rt3Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_pre goto CPU1_loc_At1Wt3Wt4;

loc CPU1_loc_At1Wt3Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt3Wt4;

loc CPU1_loc_At2Rt3Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_pre goto CPU1_loc_At2Wt3Wt4;

loc CPU1_loc_At2Wt3Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt3Wt4;

loc CPU1_loc_Rt3Wt4Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_At2Rt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t3_end goto CPU1_loc_Et3Wt4Wt5;

loc CPU1_loc_Et3Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_dis goto CPU1_loc_Rt4Wt5;

loc CPU1_loc_At1Rt3Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_pre goto CPU1_loc_At1Wt3Wt4Wt5;

loc CPU1_loc_At1Wt3Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt3Wt4Wt5;

loc CPU1_loc_At2Rt3Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_pre goto CPU1_loc_At2Wt3Wt4Wt5;

loc CPU1_loc_At2Wt3Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt3Wt4Wt5;

loc CPU1_loc_Rt2: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt2;
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_Rt2Wt3;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt2Wt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt2Wt5;
	when True do {CPU1_urgent := 0}  sync t2_end goto CPU1_loc_Et2;

loc CPU1_loc_Et2: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  (* sync nosync_4*)  goto CPU1_loc_stop;

loc CPU1_loc_At1Rt2: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_pre goto CPU1_loc_At1Wt2;

loc CPU1_loc_At1Wt2: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt2;

loc CPU1_loc_Rt2Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt2Wt5;
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_Rt2Wt3Wt5;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt2Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t2_end goto CPU1_loc_Et2Wt5;

loc CPU1_loc_Et2Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t5_dis goto CPU1_loc_Rt5;

loc CPU1_loc_At1Rt2Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_pre goto CPU1_loc_At1Wt2Wt5;

loc CPU1_loc_At1Wt2Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt2Wt5;

loc CPU1_loc_Rt2Wt4: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt2Wt4;
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_Rt2Wt3Wt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt2Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t2_end goto CPU1_loc_Et2Wt4;

loc CPU1_loc_Et2Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_dis goto CPU1_loc_Rt4;

loc CPU1_loc_At1Rt2Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_pre goto CPU1_loc_At1Wt2Wt4;

loc CPU1_loc_At1Wt2Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt2Wt4;

loc CPU1_loc_Rt2Wt4Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt2Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_Rt2Wt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t2_end goto CPU1_loc_Et2Wt4Wt5;

loc CPU1_loc_Et2Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_dis goto CPU1_loc_Rt4Wt5;

loc CPU1_loc_At1Rt2Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_pre goto CPU1_loc_At1Wt2Wt4Wt5;

loc CPU1_loc_At1Wt2Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt2Wt4Wt5;

loc CPU1_loc_Rt2Wt3: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt2Wt3;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt2Wt3Wt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt2Wt3Wt5;
	when True do {CPU1_urgent := 0}  sync t2_end goto CPU1_loc_Et2Wt3;

loc CPU1_loc_Et2Wt3: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_dis goto CPU1_loc_Rt3;

loc CPU1_loc_At1Rt2Wt3: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_pre goto CPU1_loc_At1Wt2Wt3;

loc CPU1_loc_At1Wt2Wt3: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt2Wt3;

loc CPU1_loc_Rt2Wt3Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt2Wt3Wt5;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt2Wt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t2_end goto CPU1_loc_Et2Wt3Wt5;

loc CPU1_loc_Et2Wt3Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_dis goto CPU1_loc_Rt3Wt5;

loc CPU1_loc_At1Rt2Wt3Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_pre goto CPU1_loc_At1Wt2Wt3Wt5;

loc CPU1_loc_At1Wt2Wt3Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt2Wt3Wt5;

loc CPU1_loc_Rt2Wt3Wt4: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt2Wt3Wt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt2Wt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t2_end goto CPU1_loc_Et2Wt3Wt4;

loc CPU1_loc_Et2Wt3Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_dis goto CPU1_loc_Rt3Wt4;

loc CPU1_loc_At1Rt2Wt3Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_pre goto CPU1_loc_At1Wt2Wt3Wt4;

loc CPU1_loc_At1Wt2Wt3Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt2Wt3Wt4;

loc CPU1_loc_Rt2Wt3Wt4Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t1_arr goto CPU1_loc_At1Rt2Wt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t2_end goto CPU1_loc_Et2Wt3Wt4Wt5;

loc CPU1_loc_Et2Wt3Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_dis goto CPU1_loc_Rt3Wt4Wt5;

loc CPU1_loc_At1Rt2Wt3Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_pre goto CPU1_loc_At1Wt2Wt3Wt4Wt5;

loc CPU1_loc_At1Wt2Wt3Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t1_dis goto CPU1_loc_Rt1Wt2Wt3Wt4Wt5;

loc CPU1_loc_Rt1: invariant True
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_Rt1Wt2;
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_Rt1Wt3;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt1Wt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt1Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1;

loc CPU1_loc_Et1: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  (* sync nosync_5*)  goto CPU1_loc_stop;

loc CPU1_loc_Rt1Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_Rt1Wt2Wt5;
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_Rt1Wt3Wt5;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt1Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt5;

loc CPU1_loc_Et1Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t5_dis goto CPU1_loc_Rt5;

loc CPU1_loc_Rt1Wt4: invariant True
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_Rt1Wt2Wt4;
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_Rt1Wt3Wt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt1Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt4;

loc CPU1_loc_Et1Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_dis goto CPU1_loc_Rt4;

loc CPU1_loc_Rt1Wt4Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_Rt1Wt2Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_Rt1Wt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt4Wt5;

loc CPU1_loc_Et1Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t4_dis goto CPU1_loc_Rt4Wt5;

loc CPU1_loc_Rt1Wt3: invariant True
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_Rt1Wt2Wt3;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt1Wt3Wt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt1Wt3Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt3;

loc CPU1_loc_Et1Wt3: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_dis goto CPU1_loc_Rt3;

loc CPU1_loc_Rt1Wt3Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_Rt1Wt2Wt3Wt5;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt1Wt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt3Wt5;

loc CPU1_loc_Et1Wt3Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_dis goto CPU1_loc_Rt3Wt5;

loc CPU1_loc_Rt1Wt3Wt4: invariant True
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_Rt1Wt2Wt3Wt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt1Wt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt3Wt4;

loc CPU1_loc_Et1Wt3Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_dis goto CPU1_loc_Rt3Wt4;

loc CPU1_loc_Rt1Wt3Wt4Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t2_arr goto CPU1_loc_Rt1Wt2Wt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt3Wt4Wt5;

loc CPU1_loc_Et1Wt3Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t3_dis goto CPU1_loc_Rt3Wt4Wt5;

loc CPU1_loc_Rt1Wt2: invariant True
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_Rt1Wt2Wt3;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt1Wt2Wt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt1Wt2Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt2;

loc CPU1_loc_Et1Wt2: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2;

loc CPU1_loc_Rt1Wt2Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_Rt1Wt2Wt3Wt5;
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt1Wt2Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt2Wt5;

loc CPU1_loc_Et1Wt2Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt5;

loc CPU1_loc_Rt1Wt2Wt4: invariant True
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_Rt1Wt2Wt3Wt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt1Wt2Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt2Wt4;

loc CPU1_loc_Et1Wt2Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt4;

loc CPU1_loc_Rt1Wt2Wt4Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t3_arr goto CPU1_loc_Rt1Wt2Wt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt2Wt4Wt5;

loc CPU1_loc_Et1Wt2Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt4Wt5;

loc CPU1_loc_Rt1Wt2Wt3: invariant True
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt1Wt2Wt3Wt4;
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt1Wt2Wt3Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt2Wt3;

loc CPU1_loc_Et1Wt2Wt3: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt3;

loc CPU1_loc_Rt1Wt2Wt3Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t4_arr goto CPU1_loc_Rt1Wt2Wt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt2Wt3Wt5;

loc CPU1_loc_Et1Wt2Wt3Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt3Wt5;

loc CPU1_loc_Rt1Wt2Wt3Wt4: invariant True
	when True do {CPU1_urgent := 0}  sync t5_arr goto CPU1_loc_Rt1Wt2Wt3Wt4Wt5;
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt2Wt3Wt4;

loc CPU1_loc_Et1Wt2Wt3Wt4: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt3Wt4;

loc CPU1_loc_Rt1Wt2Wt3Wt4Wt5: invariant True
	when True do {CPU1_urgent := 0}  sync t1_end goto CPU1_loc_Et1Wt2Wt3Wt4Wt5;

loc CPU1_loc_Et1Wt2Wt3Wt4Wt5: invariant  0 >= CPU1_urgent
	when  CPU1_urgent = 0 do {}  sync t2_dis goto CPU1_loc_Rt2Wt3Wt4Wt5;

loc CPU1_loc_stop: invariant True
 end (* sched_CPU1 *)
(************************************************************)


(************************************************************)
 automaton OBS_dline
(************************************************************)
 synclabs: t1_miss, t2_miss, t3_miss, t4_miss, t5_miss;


loc dline_loc_nomiss: invariant True
	when True do {t1_d := 0}  sync t1_miss goto dline_loc_miss;
	when True do {t1_d := 0}  sync t2_miss goto dline_loc_miss;
	when True do {t1_d := 0}  sync t3_miss goto dline_loc_miss;
	when True do {t1_d := 0}  sync t4_miss goto dline_loc_miss;
	when True do {t1_d := 0}  sync t5_miss goto dline_loc_miss;

loc dline_loc_miss: invariant  t1_d = 0 stop{t1_d}
 end (* OBS_dline *)
(************************************************************)

(************************************************************)
(* Initial state *)
(************************************************************)

init := True
	(*------------------------------------------------------------*)
	(* Initial location *)
	(*------------------------------------------------------------*)
	& loc[Task_t1] = t1_loc_idle
	& loc[Periodic_t1_arr] = t1_arr_loc_arr
	& loc[Task_t2] = t2_loc_idle
	& loc[Periodic_t2_arr] = t2_arr_loc_arr
	& loc[Task_t3] = t3_loc_idle
	& loc[Periodic_t3_arr] = t3_arr_loc_arr
	& loc[Task_t4] = t4_loc_idle
	& loc[Periodic_t4_arr] = t4_arr_loc_arr
	& loc[Task_t5] = t5_loc_idle
	& loc[Periodic_t5_arr] = t5_arr_loc_arr
	& loc[sched_CPU1] = CPU1_loc_
	& loc[OBS_dline] = dline_loc_nomiss

	(*------------------------------------------------------------*)
	(* Initial discrete assignments *)
	(*------------------------------------------------------------*)

	(*------------------------------------------------------------*)
	(* Initial constraint *)
	(*------------------------------------------------------------*)
	 &  t5_C >= 10
& t4_C >= 10
& 50 >= t5_C
& 50 >= t4_C
& t1_c = 0
& t1_d = 0
& t1_urgent = 0
& t1_arr_x = 8
& t2_c = 0
& t2_d = 0
& t2_urgent = 0
& t2_arr_x = 20
& t3_c = 0
& t3_d = 0
& t3_urgent = 0
& t3_arr_x = 50
& t4_c = 0
& t4_d = 0
& t4_urgent = 0
& t4_arr_x = 100
& t5_c = 0
& t5_d = 0
& t5_urgent = 0
& t5_arr_x = 200
& CPU1_urgent = 0

;

(************************************************************)
(* Property specification *)
(************************************************************)

property := unreachable loc[OBS_dline] = dline_loc_miss


(************************************************************)
(* The end *)
(************************************************************)
end
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test the graphical state space generation (no details)',
		'input_files': ['CUBPTA1.imi'],
		'options'    : '-mode statespace -output-trace-set-nodetails -output-graphics-source',
		'expectations' : [
			{'file': 'CUBPTA1-statespace.dot' , 'content' : """
  s_0 -> s_1 [label="a"];
  s_1 -> s_2 [label="a"];
  s_2 -> s_3 [label="a"];
  s_3 -> s_2 [label="a"];

/* Initial state */
  s_init [shape=none, label="init"];
  s_init -> s_0;

/* Colors */

  s_0 [color=blue, style=filled];
  s_1 [color=yellow, style=filled];
  s_2 [color=blue, style=filled];
  s_3 [color=yellow, style=filled];
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test the graphical state space generation (normal)',
		'input_files': ['CUBPTA1.imi'],
		'options'    : '-mode statespace -output-trace-set -output-graphics-source',
		'expectations' : [
			{'file': 'CUBPTA1-statespace.dot' , 'content' : """
  s_0 -> s_1 [label="a"];
  s_1 -> s_2 [label="a"];
  s_2 -> s_3 [label="a"];
  s_3 -> s_2 [label="a"];

/* Initial state */
  s_init [shape=none, label="init"];
  s_init -> s_0;

/* Colors */

  s_0[fillcolor=blue, style=filled, shape=Mrecord, label="s_0|{pta : l1}"];
  s_1[fillcolor=yellow, style=filled, shape=Mrecord, label="s_1|{pta : l2}"];
  s_2[fillcolor=blue, style=filled, shape=Mrecord, label="s_2|{pta : l1}"];
  s_3[fillcolor=yellow, style=filled, shape=Mrecord, label="s_3|{pta : l2}"];
		"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		'purpose'    : 'Test the graphical state space generation (verbose)',
		'input_files': ['CUBPTA1.imi'],
		'options'    : '-mode statespace -output-trace-set-verbose -output-graphics-source',
		'expectations' : [
			{'file': 'CUBPTA1-statespace.dot' , 'content' : """
  s_0 -> s_1 [label="a"];
  s_1 -> s_2 [label="a"];
  s_2 -> s_3 [label="a"];
  s_3 -> s_2 [label="a"];

/* Initial state */
  s_init [shape=none, label="init"];
  s_init -> s_0;

/* Colors */

  s_0[fillcolor=blue, style=filled, shape=Mrecord, label="s_0|{pta : l1}|{ p1 \>= x \\n \& p2 \>= 0 \\n \& x \>= 0 \\n \& x = y| p2 \>= 0 \\n \& p1 \>= 0}"];
  s_1[fillcolor=yellow, style=filled, shape=Mrecord, label="s_1|{pta : l2}|{ p1 + x \>= y \\n \& p2 \>= y \\n \& x \>= 0 \\n \& y \>= x| p2 \>= 0 \\n \& p1 \>= 0}"];
  s_2[fillcolor=blue, style=filled, shape=Mrecord, label="s_2|{pta : l1}|{ p1 \>= x \\n \& p2 \>= 1 \\n \& x \>= 0 \\n \& x = y| p2 \>= 1 \\n \& p1 \>= 0}"];
  s_3[fillcolor=yellow, style=filled, shape=Mrecord, label="s_3|{pta : l2}|{ p1 + x \>= y \\n \& p2 \>= y \\n \& p2 \>= 1 \\n \& x \>= 0 \\n \& y \>= x| p1 \>= 0 \\n \& p2 \>= 1}"];
		"""
			} # end result file
			# NOTE (ÉA, 2018/06/05): I had to manually replace '\n' with '\\n' to make this test pass
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------
	,
	#------------------------------------------------------------
	{
		# Test version: 2.11
		# Test since  : 2019/03/07
		'purpose'    : 'Test the graphical state space generation (verbose with projection)',
		'input_files': ['CUBPTA1project.imi'],
		'options'    : '-mode statespace -output-trace-set-verbose -output-graphics-source',
		'expectations' : [
			{'file': 'CUBPTA1project-statespace.dot' , 'content' : """
  s_0 -> s_1 [label="a"];
  s_1 -> s_2 [label="a"];
  s_2 -> s_3 [label="a"];
  s_3 -> s_2 [label="a"];

/* Initial state */
  s_init [shape=none, label="init"];
  s_init -> s_0;

/* Colors */

  s_0[fillcolor=blue, style=filled, shape=Mrecord, label="s_0|{pta : l1}|{ p1 \>= x \\n \& p2 \>= 0 \\n \& x \>= 0 \\n \& x = y| p2 \>= 0 \\n \& p1 \>= 0| p2 \>= 0}"];
  s_1[fillcolor=yellow, style=filled, shape=Mrecord, label="s_1|{pta : l2}|{ p1 + x \>= y \\n \& p2 \>= y \\n \& x \>= 0 \\n \& y \>= x| p2 \>= 0 \\n \& p1 \>= 0| p2 \>= 0}"];
  s_2[fillcolor=blue, style=filled, shape=Mrecord, label="s_2|{pta : l1}|{ p1 \>= x \\n \& p2 \>= 1 \\n \& x \>= 0 \\n \& x = y| p2 \>= 1 \\n \& p1 \>= 0| p2 \>= 1}"];
  s_3[fillcolor=yellow, style=filled, shape=Mrecord, label="s_3|{pta : l2}|{ p1 + x \>= y \\n \& p2 \>= y \\n \& p2 \>= 1 \\n \& x \>= 0 \\n \& y \>= x| p1 \>= 0 \\n \& p2 \>= 1| p2 \>= 1}"];
		"""
			} # end result file
			# NOTE (ÉA, 2019/03/07): I had to manually replace '\n' with '\\n' to make this test pass
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test translation to HyTech',
		'input_files': ['flipflop.imi'],
		'options'    : '-PTA2HyTech -no-var-autoremove', #TODO: re-do without '-no-var-autoremove'
		'expectations' : [
			{'file': 'flipflop.hy' , 'content' : """
 -- Created to be compatible with 'hytech-v1.04f-Linux_static'
 --************************************************************
var
	s, ckG1, ckG2, ckG3, ckG4
		: clock;

	dG3_u, dG4_u
		: parameter;


--************************************************************
 automaton input
--************************************************************
 synclabs: dUp, ckUp, dDown, ckDown;
 initially Input0;

loc Input0: while  5 >= s wait{}
	when  s = 5 do {}  sync dUp goto Input1;

loc Input1: while  15 >= s wait{}
	when  s = 15 do {}  sync ckUp goto Input2;

loc Input2: while  32 >= s wait{}
	when  s = 32 do {}  sync dDown goto Input3;

loc Input3: while  39 >= s wait{}
	when  s = 39 do {s' = 0}  sync ckDown goto Input4;

loc Input4: while  0 >= s wait{}
 end -- input
--************************************************************


--************************************************************
 automaton g1
--************************************************************
 synclabs: dUp, ckUp, qG2Up, qG1Up, qG2Down, ckDown, qG1Down, dDown;
 initially G10011;

loc G10000: while  7 >= ckG1 wait{}
	when True do {ckG1' = 0}  sync dUp goto G11000;
	when True do {ckG1' = 0}  sync ckUp goto G10100;
	when True do {ckG1' = 0}  sync qG2Up goto G10010;
	when  ckG1 >= 7 do {}  sync qG1Up goto G10001;

loc G10001: while  ckG1 >= 0 wait{}
	when True do {}  sync dUp goto G11001;
	when True do {}  sync ckUp goto G10101;
	when True do {}  sync qG2Up goto G10011;

loc G10010: while  7 >= ckG1 wait{}
	when True do {}  sync dUp goto G11010;
	when True do {}  sync ckUp goto G10110;
	when True do {ckG1' = 0}  sync qG2Down goto G10000;
	when  ckG1 >= 7 do {}  sync qG1Up goto G10011;

loc G10011: while  ckG1 >= 0 wait{}
	when True do {ckG1' = 0}  sync dUp goto G11011;
	when True do {ckG1' = 0}  sync ckUp goto G10111;
	when True do {}  sync qG2Down goto G10001;

loc G10100: while  7 >= ckG1 wait{}
	when True do {ckG1' = 0}  sync dUp goto G11100;
	when True do {ckG1' = 0}  sync ckDown goto G10000;
	when True do {}  sync qG2Up goto G10110;
	when  ckG1 >= 7 do {}  sync qG1Up goto G10101;

loc G10101: while  ckG1 >= 0 wait{}
	when True do {}  sync dUp goto G11101;
	when True do {}  sync ckDown goto G10001;
	when True do {ckG1' = 0}  sync qG2Up goto G10111;

loc G10110: while  ckG1 >= 0 wait{}
	when True do {}  sync dUp goto G11110;
	when True do {ckG1' = 0}  sync ckDown goto G10010;
	when True do {ckG1' = 0}  sync qG2Down goto G10100;

loc G10111: while  7 >= ckG1 wait{}
	when True do {ckG1' = 0}  sync dUp goto G11111;
	when True do {}  sync ckDown goto G10011;
	when True do {}  sync qG2Down goto G10101;
	when  ckG1 >= 7 do {}  sync qG1Down goto G10110;

loc G11000: while  7 >= ckG1 wait{}
	when True do {ckG1' = 0}  sync dDown goto G10000;
	when True do {ckG1' = 0}  sync ckUp goto G11100;
	when True do {}  sync qG2Up goto G11010;
	when  ckG1 >= 7 do {}  sync qG1Up goto G11001;

loc G11001: while  ckG1 >= 0 wait{}
	when True do {}  sync dDown goto G10001;
	when True do {}  sync ckUp goto G11101;
	when True do {ckG1' = 0}  sync qG2Up goto G11011;

loc G11010: while  ckG1 >= 0 wait{}
	when True do {ckG1' = 0}  sync dDown goto G10010;
	when True do {}  sync ckUp goto G11110;
	when True do {ckG1' = 0}  sync qG2Down goto G11000;

loc G11011: while  7 >= ckG1 wait{}
	when True do {}  sync dDown goto G10011;
	when True do {ckG1' = 0}  sync ckUp goto G11111;
	when True do {}  sync qG2Down goto G11001;
	when  ckG1 >= 7 do {}  sync qG1Down goto G11010;

loc G11100: while  7 >= ckG1 wait{}
	when True do {ckG1' = 0}  sync dDown goto G10100;
	when True do {ckG1' = 0}  sync ckDown goto G11000;
	when True do {}  sync qG2Up goto G11110;
	when  ckG1 >= 7 do {}  sync qG1Up goto G11101;

loc G11101: while  ckG1 >= 0 wait{}
	when True do {}  sync dDown goto G10101;
	when True do {}  sync ckDown goto G11001;
	when True do {ckG1' = 0}  sync qG2Up goto G11111;

loc G11110: while  ckG1 >= 0 wait{}
	when True do {}  sync dDown goto G10110;
	when True do {}  sync ckDown goto G11010;
	when True do {ckG1' = 0}  sync qG2Down goto G11100;

loc G11111: while  7 >= ckG1 wait{}
	when True do {ckG1' = 0}  sync dDown goto G10111;
	when True do {ckG1' = 0}  sync ckDown goto G11011;
	when True do {}  sync qG2Down goto G11101;
	when  ckG1 >= 7 do {}  sync qG1Down goto G11110;
 end -- g1
--************************************************************


--************************************************************
 automaton g2
--************************************************************
 synclabs: qG1Up, ckUp, qG2Up, ckDown, qG1Down, qG2Down;
 initially G2101;

loc G2001: while  ckG2 >= 0 wait{}
	when True do {}  sync qG1Up goto G2101;
	when True do {}  sync ckUp goto G2011;

loc G2000: while  6 >= ckG2 wait{}
	when True do {ckG2' = 0}  sync qG1Up goto G2100;
	when True do {ckG2' = 0}  sync ckUp goto G2010;
	when  ckG2 >= 5 do {}  sync qG2Up goto G2001;

loc G2011: while  ckG2 >= 0 wait{}
	when True do {ckG2' = 0}  sync qG1Up goto G2111;
	when True do {}  sync ckDown goto G2001;

loc G2010: while  6 >= ckG2 wait{}
	when True do {}  sync qG1Up goto G2110;
	when True do {ckG2' = 0}  sync ckDown goto G2000;
	when  ckG2 >= 5 do {}  sync qG2Up goto G2011;

loc G2101: while  ckG2 >= 0 wait{}
	when True do {}  sync qG1Down goto G2001;
	when True do {ckG2' = 0}  sync ckUp goto G2111;

loc G2100: while  6 >= ckG2 wait{}
	when True do {ckG2' = 0}  sync qG1Down goto G2000;
	when True do {}  sync ckUp goto G2110;
	when  ckG2 >= 5 do {}  sync qG2Up goto G2101;

loc G2111: while  6 >= ckG2 wait{}
	when True do {}  sync qG1Down goto G2011;
	when True do {}  sync ckDown goto G2101;
	when  ckG2 >= 5 do {}  sync qG2Down goto G2110;

loc G2110: while  ckG2 >= 0 wait{}
	when True do {ckG2' = 0}  sync qG1Down goto G2010;
	when True do {ckG2' = 0}  sync ckDown goto G2100;
 end -- g2
--************************************************************


--************************************************************
 automaton g3
--************************************************************
 synclabs: qUp, ckUp, qG2Up, qG3Up, qG2Down, ckDown, qG3Down, qDown;
 initially G30011;

loc G30000: while  dG3_u >= ckG3 wait{}
	when True do {ckG3' = 0}  sync qUp goto G31000;
	when True do {ckG3' = 0}  sync ckUp goto G30100;
	when True do {ckG3' = 0}  sync qG2Up goto G30010;
	when  ckG3 >= 8 do {}  sync qG3Up goto G30001;

loc G30001: while  ckG3 >= 0 wait{}
	when True do {}  sync qUp goto G31001;
	when True do {}  sync ckUp goto G30101;
	when True do {}  sync qG2Up goto G30011;

loc G30010: while  dG3_u >= ckG3 wait{}
	when True do {}  sync qUp goto G31010;
	when True do {}  sync ckUp goto G30110;
	when True do {ckG3' = 0}  sync qG2Down goto G30000;
	when  ckG3 >= 8 do {}  sync qG3Up goto G30011;

loc G30011: while  ckG3 >= 0 wait{}
	when True do {ckG3' = 0}  sync qUp goto G31011;
	when True do {ckG3' = 0}  sync ckUp goto G30111;
	when True do {}  sync qG2Down goto G30001;

loc G30100: while  dG3_u >= ckG3 wait{}
	when True do {ckG3' = 0}  sync qUp goto G31100;
	when True do {ckG3' = 0}  sync ckDown goto G30000;
	when True do {}  sync qG2Up goto G30110;
	when  ckG3 >= 8 do {}  sync qG3Up goto G30101;

loc G30101: while  ckG3 >= 0 wait{}
	when True do {}  sync qUp goto G31101;
	when True do {}  sync ckDown goto G30001;
	when True do {ckG3' = 0}  sync qG2Up goto G30111;

loc G30110: while  ckG3 >= 0 wait{}
	when True do {}  sync qUp goto G31110;
	when True do {ckG3' = 0}  sync ckDown goto G30010;
	when True do {ckG3' = 0}  sync qG2Down goto G30100;

loc G30111: while  dG3_u >= ckG3 wait{}
	when True do {ckG3' = 0}  sync qUp goto G31111;
	when True do {}  sync ckDown goto G30011;
	when True do {}  sync qG2Down goto G30101;
	when  ckG3 >= 8 do {}  sync qG3Down goto G30110;

loc G31000: while  dG3_u >= ckG3 wait{}
	when True do {ckG3' = 0}  sync qDown goto G30000;
	when True do {ckG3' = 0}  sync ckUp goto G31100;
	when True do {}  sync qG2Up goto G31010;
	when  ckG3 >= 8 do {}  sync qG3Up goto G31001;

loc G31001: while  ckG3 >= 0 wait{}
	when True do {}  sync qDown goto G30001;
	when True do {}  sync ckUp goto G31101;
	when True do {ckG3' = 0}  sync qG2Up goto G31011;

loc G31010: while  ckG3 >= 0 wait{}
	when True do {ckG3' = 0}  sync qDown goto G30010;
	when True do {}  sync ckUp goto G31110;
	when True do {ckG3' = 0}  sync qG2Down goto G31000;

loc G31011: while  dG3_u >= ckG3 wait{}
	when True do {}  sync qDown goto G30011;
	when True do {ckG3' = 0}  sync ckUp goto G31111;
	when True do {}  sync qG2Down goto G31001;
	when  ckG3 >= 8 do {}  sync qG3Down goto G31010;

loc G31100: while  dG3_u >= ckG3 wait{}
	when True do {ckG3' = 0}  sync qDown goto G30100;
	when True do {ckG3' = 0}  sync ckDown goto G31000;
	when True do {}  sync qG2Up goto G31110;
	when  ckG3 >= 8 do {}  sync qG3Up goto G31101;

loc G31101: while  ckG3 >= 0 wait{}
	when True do {}  sync qDown goto G30101;
	when True do {}  sync ckDown goto G31001;
	when True do {ckG3' = 0}  sync qG2Up goto G31111;

loc G31110: while  ckG3 >= 0 wait{}
	when True do {}  sync qDown goto G30110;
	when True do {}  sync ckDown goto G31010;
	when True do {ckG3' = 0}  sync qG2Down goto G31100;

loc G31111: while  dG3_u >= ckG3 wait{}
	when True do {ckG3' = 0}  sync qDown goto G30111;
	when True do {ckG3' = 0}  sync ckDown goto G31011;
	when True do {}  sync qG2Down goto G31101;
	when  ckG3 >= 8 do {}  sync qG3Down goto G31110;
 end -- g3
--************************************************************


--************************************************************
 automaton g4
--************************************************************
 synclabs: qG3Up, qG3Down, qDown, qUp;
 initially G410;

loc G401: while  ckG4 >= 0 wait{}
	when True do {ckG4' = 0}  sync qG3Up goto G411;

loc G411: while  dG4_u >= ckG4 wait{}
	when True do {}  sync qG3Down goto G401;
	when  ckG4 >= 3 do {} sync qDown goto G410;

loc G410: while  ckG4 >= 0 wait{}
	when True do {ckG4' = 0}  sync qG3Down goto G400;

loc G400: while  dG4_u >= ckG4 wait{}
	when True do {}  sync qG3Up goto G410;
	when  ckG4 >= 3 do {} sync qUp goto G401;
 end -- g4
--************************************************************


--************************************************************
-- Initial state
--************************************************************
var init : region;

init := True
	------------------------------------------------------------
	-- Initial location
	------------------------------------------------------------
	& loc[input] = Input0
	& loc[g1] = G10011
	& loc[g2] = G2101
	& loc[g3] = G30011
	& loc[g4] = G410

	------------------------------------------------------------
	-- Initial discrete assignments
	------------------------------------------------------------

	------------------------------------------------------------
	-- Initial constraint
	------------------------------------------------------------
	 &  dG4_u >= 3
& ckG1 >= 0
& ckG2 >= 0
& ckG3 >= 0
& ckG4 >= 0
& dG3_u >= 8
& s = 0
;

--************************************************************
--* Property specification
--************************************************************

--property := if ckDown then qUp has happened before; (NOT CONSIDERED BY HYTECH)


--************************************************************
--* The end
--************************************************************

"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'Test translation to Uppaal with synchronization model',
		'input_files': ['testSynchroUppaal.imi'],
		'options'    : '-PTA2Uppaal',
		'expectations' : [
			{'file': 'testSynchroUppaal-uppaal.xml' , 'content' : """
/* Clocks declarations */
clock x;

/* Discrete variable declarations needed to encode IMITATOR's strong broadcast into Uppaal */
int nb__a = 3;

/* Action declarations */
broadcast chan a; /* This action is used in 3 automata: IMITATOR uses strong broadcast semantics, while Uppaal uses broadcast semantics; the correctness is ensured thanks to variable 'nb__a' */
chan b;
broadcast chan c;

	/*------------------------------------------------------------*/
	/* Initial constraint (not interpreted by Uppaal)             */
	/*------------------------------------------------------------*/
	 /*  x == 0 */
</declaration>

<template><name x="0" y="0">pta1</name><declaration>// No local declaration for automaton 'pta1'
</declaration>

<location id="id_pta0_loc0" x="0" y="0">
	<name x="0" y="-40">l1</name>
	<label kind="invariant" x="0" y="40">nb__a == 3</label></location>

<location id="id_pta0_loc1" x="200" y="0">
	<name x="200" y="-40">l2</name>
	<label kind="invariant" x="200" y="40">nb__a == 3</label></location>
 <init ref="id_pta0_loc0"/>

	<transition>
		<source ref="id_pta0_loc0"/>
		<target ref="id_pta0_loc0"/>
		<label kind="synchronisation" x="0" y="80">a!</label>
		<label kind="guard" x="0" y="40"> x == 3</label>
		<label kind="assignment" x="0" y="-40">x = 0, nb__a = 1</label>
	</transition>
	<transition>
		<source ref="id_pta0_loc0"/>
		<target ref="id_pta0_loc1"/>
		<label kind="synchronisation" x="100" y="80">b!</label>
		<label kind="guard" x="100" y="40"> x == 4</label>

	</transition>
 </template>


<template><name x="1" y="1">pta2</name><declaration>// No local declaration for automaton 'pta2'
</declaration>

<location id="id_pta1_loc0" x="0" y="0">
	<name x="0" y="-40">l1</name>
	<label kind="invariant" x="0" y="40">nb__a == 3</label></location>

<location id="id_pta1_loc1" x="200" y="0">
	<name x="200" y="-40">l2</name>
	<label kind="invariant" x="200" y="40">nb__a == 3</label></location>
 <init ref="id_pta1_loc0"/>

	<transition>
		<source ref="id_pta1_loc0"/>
		<target ref="id_pta1_loc0"/>
		<label kind="synchronisation" x="0" y="80">a?</label>
		<label kind="guard" x="0" y="40">true</label>
		<label kind="assignment" x="0" y="-40">x = 0, nb__a = nb__a + 1</label>
	</transition>
	<transition>
		<source ref="id_pta1_loc0"/>
		<target ref="id_pta1_loc1"/>
		<label kind="synchronisation" x="100" y="80">b?</label>
		<label kind="guard" x="100" y="40">true</label>

	</transition>
 </template>


<template><name x="2" y="2">pta3</name><declaration>// No local declaration for automaton 'pta3'
</declaration>

<location id="id_pta2_loc0" x="0" y="0">
	<name x="0" y="-40">l1</name>
	<label kind="invariant" x="0" y="40"> 3 &gt;= x &amp;&amp; nb__a == 3</label></location>

<location id="id_pta2_loc1" x="200" y="0">
	<name x="200" y="-40">l2</name>
	<label kind="invariant" x="200" y="40"> 3 &gt;= x &amp;&amp; nb__a == 3</label></location>

<location id="id_pta2_loc2" x="400" y="0">
	<name x="400" y="-40">l3</name>
	<label kind="invariant" x="400" y="40">nb__a == 3</label></location>
 <init ref="id_pta2_loc0"/>

	<transition>
		<source ref="id_pta2_loc0"/>
		<target ref="id_pta2_loc1"/>
		<label kind="synchronisation" x="100" y="80">c!</label>
		<label kind="guard" x="100" y="40"> x == 3</label>
		<label kind="assignment" x="100" y="-40">x = 0</label>
	</transition>
	<transition>
		<source ref="id_pta2_loc1"/>
		<target ref="id_pta2_loc2"/>
		<label kind="synchronisation" x="300" y="80">a?</label>
		<label kind="guard" x="300" y="40">true</label>
		<label kind="assignment" x="300" y="-40">x = 0, nb__a = nb__a + 1</label>
	</transition>
 </template>
<system>
// List one or more processes to be composed into a system.

system pta1, pta2, pta3;
</system></nta>
	"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'FMTV challenge: Test EF with project-result -verbose mute',
		'input_files': ['fmtv1A1-v2.imi'],
		'options'    : '-mode EF -merge -incl -output-result',
		'expectations' : [
			{'file': 'fmtv1A1-v2.res' , 'content' : """
BEGIN CONSTRAINT
125*e2e > 18126
OR
e2e >= 0
&
63 > e2e
END CONSTRAINT
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'FMTV challenge: Test EFmin',
		'input_files': ['fmtv1A1-v2-min.imi'],
		'options'    : '-mode EFmin -merge -incl -output-result -verbose mute',
		'expectations' : [
			{'file': 'fmtv1A1-v2-min.res' , 'content' : """
BEGIN CONSTRAINT
 e2e >= 63
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	#------------------------------------------------------------
	{
		'purpose'    : 'FMTV challenge: Test EFmax',
		'input_files': ['fmtv1A1-v2-max.imi'],
		'options'    : '-mode EFmax -merge -incl -output-result -verbose mute',
		'expectations' : [
			{'file': 'fmtv1A1-v2-max.res' , 'content' : """
BEGIN CONSTRAINT
 e2e >= 0
& 18126 >= 125*e2e
END CONSTRAINT

------------------------------------------------------------
Constraint soundness                    : exact
Termination                             : regular termination
Constraint nature                       : good
------------------------------------------------------------
"""
			} # end result file
			,
		] # end expectations
	} # end test case
	#------------------------------------------------------------

	,

	##------------------------------------------------------------
	#{
		#'purpose'    : 'XXXX',
		#'input_files': ['XXXX.imi', 'XXXX.pi0'],
		#'options'    : '-XXXX',
		#'expectations' : [
			#{'file': 'XXXX' , 'content' : """XXXX"""
			#} # end result file
			#,
		#] # end expectations
	#} # end test case
	##------------------------------------------------------------]

### THE END
]
