#!/bin/bash

###########################################
# Script for generating experiments table #
# Author: Laure Petrucci                  #
# Version: 2.0                            #
# Date: 25/01/2020                        #
###########################################

function usage {
	echo -e "\033[1;31musage\033[0m: $0 -t timeout -o table_filename [-s | -i input_models]"
	exit
}

function process_results {
	echo -n `grep "cycles found" $one_result | cut -d: -f2 | sed -e 's/\[0m//'`' ; '>> $output_file
	echo -n `grep "processed states" $one_result | cut -d: -f2 | sed -e 's/\[0m//'`' ; ' >> $output_file
	exceeds_time=`grep "under-approximation" $one_result`
	if [ -z "$exceeds_time" ]
	then echo -n `grep "completed after" $one_result | sed -e 's/\[NDFS\] State space exploration completed after //' \
		| sed -e 's/ seconds.//' | sed -e 's/ second.//'  | sed -e 's/\[0m//'` >> $output_file
	else echo -n "TO" >> $output_file
	fi
}

# main part of the script

# get the options
timeout=60 # 1 minute by default
output_file=
exp_dir="tests/acceptingExamples"
input_files="BRP coffee \
		critical-region critical-region4 F3 F4 FDDI4 FischerAHV93 flipflop fmtv1A1-v2 \
		fmtv1A3-v2 JLR-TACAS13 \
		lynch lynch5 \
		Pipeline-KP12-2-3 Pipeline-KP12-2-5 Pipeline-KP12-3-3 \
		RCP Sched2.100.0 \
		Sched2.100.2 \
		Sched2.50.0 \
		Sched2.50.2 simop \
		spsmall tgcTogether2 \
		WFAS-BBLS15-det"
while getopts "t:o:si:'" opt; do
case $opt in
	t) timeout=$OPTARG ;;
	o) output_file=$OPTARG ;;
	s) input_files="BRP coffee \
		critical-region critical-region4 F3 F4 FDDI4 FischerAHV93 flipflop fmtv1A1-v2 \
		fmtv1A3-v2 JLR-TACAS13 \
		lynch lynch5 \
		Pipeline-KP12-2-3 Pipeline-KP12-2-5 Pipeline-KP12-3-3 \
		RCP Sched2.100.0 \
		Sched2.100.2 \
		Sched2.50.0 \
		Sched2.50.2 simop \
		spsmall tgcTogether2 \
		WFAS-BBLS15-det" ;;
	i) input_files=$OPTARG ;;
esac
done

if [ -z "$output_file" ]
then usage
fi

extension=".${output_file##*.}"
one_result="`basename $2 $extension`.tmp"
rm -f $one_result
rm -f $output_file
# table with layers
echo ' ; ; ; ; No strategy ; ; ; Subsumption ; ; ; Ordering ; ; ; Lookahead ; ; ; Order+Look ; ; ; O + L + Sub ; ;' > $output_file
echo 'Model ; L ; X ; P ; c ; s ; t ; c ; s ; t ; c ; s ; t ; c ; s ; t ; c ; s ; t ; c ; s ; t' >> $output_file
for f in $input_files
	do echo -e "Running experiments for model \033[1;31m$f\033[0m"
		bin/imitator -mode checksyntax -verbose low $exp_dir/$f.imi > $one_result 2> /dev/null
		# first column = benchmark file name
		echo -n "$f ; " >> $output_file
		# columns 2 to 4 = L, X, P
		echo -n `grep -e locations $one_result | cut -d, -f2,5,7 | sed -e 's/^ //' \
			| sed -e 's/ locations, / \; /' | sed -e 's/ clock variables, / \; /' \
			| sed -e 's/ parameters/ \;/' | sed -e 's/ parameter/ \; /' ` >> $output_file
	# no strategy
		echo -e "\twithout strategy"
		bin/imitator -mode AccLoopSynthNDFS -explOrder layerNDFS -no-lookahead -no-acceptfirst -time-limit $timeout $exp_dir/$f.imi > $one_result 2> /dev/null
		process_results
		echo -n ' ; ' >> $output_file
	# subsumption
		echo -e "\tsubsumption only"
		bin/imitator -mode AccLoopSynthNDFS -explOrder layerNDFSsub -no-lookahead -no-acceptfirst -time-limit $timeout $exp_dir/$f.imi > $one_result 2> /dev/null
		process_results
		echo -n ' ; ' >> $output_file
	# ordering
		echo -e "\tordering only"
		bin/imitator -mode AccLoopSynthNDFS -explOrder layerNDFS -no-lookahead -time-limit $timeout $exp_dir/$f.imi > $one_result 2> /dev/null
		process_results
		echo -n ' ; ' >> $output_file
	# lookahead
		echo -e "\tlookahead only"
		bin/imitator -mode AccLoopSynthNDFS -explOrder layerNDFS -no-acceptfirst -time-limit $timeout $exp_dir/$f.imi > $one_result 2> /dev/null
		process_results
		echo -n ' ; ' >> $output_file
	# lookahead + ordering
		echo -e "\tlookahead and ordering"
		bin/imitator -mode AccLoopSynthNDFS -explOrder layerNDFS -time-limit $timeout $exp_dir/$f.imi > $one_result 2> /dev/null
		process_results
		echo -n ' ; ' >> $output_file
	# lookahead + ordering + subsumption
		echo -e "\tsubsumption, lookahead and ordering"
		bin/imitator -mode AccLoopSynthNDFS -explOrder layerNDFSsub -time-limit $timeout $exp_dir/$f.imi > $one_result 2> /dev/null
		process_results
		echo '' >> $output_file
	done
rm -f $one_result