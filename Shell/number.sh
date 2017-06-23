#!/bin/bash

number=0

echo -n "Enter a number >"
read number

echo "Number is $number"

if ["$number" = "100"]; then
        echo "Number is less than 100"
else
        echo "Number is greater than 100"
fi