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