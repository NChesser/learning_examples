#!/bin/bash

#For Loops - Examples

#Loop between a Start and End Point 

for number in {1..10}
do
        echo "$number"
done

#How to skip Numbers in a Range

for number in {0..100..10}
do
        echo "$number"
done

#Regular For Loop

for ((number=0; number<100; number++)){
        echo "$number"done

#Regular For Loop

for ((number=0; number<100; number++)){
        echo "$number"
}

#For Loops for files

for FILE in `ls` ; do
        echo $FILE
done

#While Loop - examples

#Simple while loop


#Another way to do the same thing

n2=0

while (( $n2 < 10 ))
do
        echo "$n2"
        n2=$(( n2+1 ))
done