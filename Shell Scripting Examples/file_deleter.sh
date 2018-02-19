#!/usr/bin/bash
# script for deleting log files 
# author: Nick Chesser

# probably have to set this in the ssh
shopt -s extglob

function delete_logs() {
  DIR=$1
  PATTERN=$2
  cd $DIR
  rm !($PATTERN).log
}

PATTERN=" "

for last; do true; done

if [ last == 'keep_recent' ];
then
  DATE=$(date +%Y%m)
  PATTERN="*$DATE*.log"
  set -- "${@:1:$(($#-1))}"
 fi
 
 DIRS="$@"
 
 for DIR in $DIRS
 do
  delete_logs $DIR $PATTERN
 done
