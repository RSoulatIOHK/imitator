#!/usr/bin/env python
# coding=utf8

 ############################################################
 #                      IMITATOR MODEL
 #
 # Fischer mutual exclusion protocol (parametric timed version with n processes)
 #
 # Description     : Generator for Fischer with n processes. This model has no variable (the global variable is simulated with an untimed PTA); however, the reachability condition is expressed by a global variable that counts the number of processes in the critical sections. If more than n, the observer is going to a special location.
 # Correctness     : No more than 'n' (2, but can be changed) processes in critical section
 # Source          : "SAT-based Unbounded Model Checking of Timed Automata", Fundamatica Informatica 85(1-4): 425-440 (2008), Figure 1.
 # Authors         : Wojciech Penczek, Maciej Szreter
 # Script authors  : Michal Knapick, Étienne André
 #
 # Created         : 2015/05/15
 # Last modified   : 2021/09/01
 #
 # IMITATOR version: 3.1
 ############################################################

import sys


def getVars(n):
    print("var")
    print("\t"+", ".join(["x"+str(i) for i in range(1,n+1)]))
    print("\t: clock;\n")
    print("\tnb\n\t: int;\n")
    print("\tdelta, Delta\n\t: parameter;\n")


def getProcess(i):

    autStr = """automaton process{0}
\tsynclabs: Start{0}, SetX{0}, Enter{0}, SetX0{0};

\tloc idle{0}: invariant True
	\twhen True sync Start{0} do {{x{0} := 0}} goto trying{0};

\tloc trying{0}: invariant True
	\twhen x{0} < delta sync SetX{0} do {{x{0} := 0}} goto waiting{0};

\tloc waiting{0}: invariant True
	\twhen x{0} > Delta sync Enter{0} do {{nb := nb + 1}} goto critical{0};

\tloc critical{0}: invariant True
	\twhen True sync SetX0{0} do {{nb := nb - 1}} goto idle{0};

end (* automaton process{0} *)\n"""

    print(autStr.format(i))


def getVar(n):

    templ = "when True sync {0}{1} do {{}} goto Val{2};"

    starts = "\t"+"\n\t".join([templ.format("Start", j, 0) for j in range(1, n+1)])
    sets = "\t"+"\n\t".join([templ.format("SetX", j, j) for j in range(1, n+1)])

    def getloc(i):
        lstt = "\n\tloc Val{}: invariant True\n".format(i)
        if i == 0:
            lstt += starts + "\n"
        else:
            lstt += "\t" + templ.format("Enter", i, i) + "\n"
            lstt += "\t" + templ.format("SetX0", i, 0) + "\n"
        lstt += sets
        return lstt

    print("automaton variable")

    print("\tsynclabs:")
    labs = ["Start", "SetX", "Enter", "SetX0"]
    print("\t"+", ".join([lab + str(i) for i in range(1, n+1) for lab in labs]) + ";")

    for i in range(n + 1):
        print(getloc(i))

    print("end")


def getInit(n):
    print("\nautomaton observer")

    print("\n\tloc obs_OK: invariant True")
    print("\t	(* Change '2' with any number of processes in CS *)")
    print("\t	when nb = 2 do {} goto obs_BAD;")

    print("\n\tloc obs_BAD: invariant True")
    print("end (* observer *)")

    print("\n\ninit := {")
    print("\tdiscrete =")
    for lp in ["\t\tloc[process{0}] := idle{0},".format(i) for i in range(1, n+1)]:
        print(lp)
    print("\t\tloc[variable] := Val0,")
    print("\t\tloc[observer] := obs_OK,")
    print("\t\tnb := 0,")

    print("\t;")
    print("\n\tcontinuous =")
    print("\t\t(* Clocks initially 0 *)")
    for i in range(1, n+1):
        print("\t\t& x{} = 0".format(i))

    print("\t\t(* Non-negative parameters *)")
    print("\t\t& Delta >= 0\n\t\t& delta >= 0")
    print("\t;")
    print("}")

#    print("\nproperty := unreachable loc[observer] = obs_BAD;")

    print("\n(* End of automatically generated model *)")
    print ("end")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage simpMutexGen.py NoOfProcs")

    NoOfProcs = int(sys.argv[1])

    print("(*** WARNING! This IMITATOR model was automatically generated by " + sys.argv[0] + " ***)\n")

    getVars(NoOfProcs)

    for i in range(1, NoOfProcs + 1):
        getProcess(i)

    getVar(NoOfProcs)

    getInit(NoOfProcs)
