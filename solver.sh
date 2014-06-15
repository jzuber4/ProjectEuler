#!/bin/bash
function usage {
   echo Usage: solver.sh [-t]
   echo Runs all the problems in the Solutions directory 
   echo flag: -t runs each problem with the \'time\' command
   exit 1
}

cd Solutions

# args checking
if [ $# -gt "2" ]; then
    usage;
fi

t=False
if [ $# -eq "1" ]; then
    if [ "$1" == "-t" ]; then
        t=True
    else
        usage;
    fi
fi

i=1
for problem in ./Problem*.py; do
    echo Solution to problem $i
    # timed or non-timed modes
    if [ $t == "True" ]; then
        time python $problem
    else 
        python $problem
    fi
    i=$((i+1))
done

