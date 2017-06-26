#!/bin/bash

#Shell functions

Hello () {
        echo "Hello World"
}

Hello

#Pass parameters to a function

Hello2 () {
        echo "Hello World $1 $2"
}

Hello2 Nick Chris

#return a value

Hello3 () {
	echo "Hello World $1 $2"
	return 10
}

#Invoke function
Hello3 Nick Chris

#Capture return value with last command
ret=$?

echo "return value is $ret"