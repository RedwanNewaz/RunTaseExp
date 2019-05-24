#!/usr/bin/env bash

#read files from a directory
function ReadFiles(){
    FILES=()
    for file in ./$1/*
    do
        FILES+=($file)
    done

}
echo which folder ?
read FOLDER
ReadFiles $FOLDER
#write data into a file
function WriteLog(){
    rm benchmark.log
    echo 1.0 >> benchmark.log
    echo 30 >> benchmark.log
    echo $1 >>benchmark.log
}

function RunExp(){
    echo "OUT/$1.json"
    ./T_ASE_SERVER_Benchmark --benchmark_repetitions=3 --benchmark_out_format=json --benchmark_out=./OUT/$1.json
}
if [ -d $FOLDER ]; then
  echo FOLDER FOUND
  else
  echo NOT A VALID FOLDER
  exit $?
fi


if [ -d "./OUT" ]; then
  rm -rf OUT
fi
mkdir OUT
var=0
for f in ${FILES[*]}
    do
        var=`expr $var + 1`
        WriteLog $f
        RunExp $var
    done


#config/wafr_tests/test_instances/p_7