#!/bin/sh

echo "\$@"
echo "$@"
echo "\$*"
echo "$*"
## Another special variable is $?.
## This contains the exit value of the last run command.
## So the code:

## The $$ variable is the PID (Process IDentifier)
## The $! variable is the PID of the last run background process

##  Another interesting variable is IFS. 
##  This is the Internal Field Separator. 
##  The default value is SPACE TAB NEWLINE, 
##  but if you are changing it, 
##  it's easier to take a copy, as shown:

old_IFS="$IFS"
IFS=:
echo "Please input some data separated by colons ..."
read x y z
IFS=$old_IFS
echo "x is $x y is $y z is $z"


echo "I was called with $# parameters"
echo "My name is $0"
echo "My first parameter is $1"
echo "My second parameter is $2"
echo "All parameters are $@"

## to cout down arguments using shift

while [ "$#" -gt "0" ]
do
  echo "\$1 is $1"
  shift
done   

##mkdir rc{0,1,2,3,4,5,6,S}.d

# for runlevel in 0 1 2 3 4 5 6 S
# do
#   mkdir rc${runlevel}.d
# done



# This is a comment!
echo "Hello      World"       # This is a comment, too!
echo "Hello World"
echo "Hello * World"
echo Hello * World
echo Hello      World
echo "Hello" World
echo Hello "     " World
echo "Hello "*" World"
echo `hello` world ;echo $(hello) world
echo 'hello' world

echo "---------------------------"

while read input_text
do
  case $input_text in
        hello)          echo English    ;;
        howdy)          echo American   ;;
        gday)           echo Australian ;;
        bonjour)        echo French     ;;
        "guten tag")    echo German     ;;
        *)              echo Unknown Language: $input_text ;;
   esac
done  < myfile.txt

for i in * hello 1 * 2 goodbye 
do
  echo "Looping ... number $i"
done

INPUT_STR=hello

while [ $INPUT_STR != "exit" ]
do
	echo "type exit to quit!"
	read INPUT_STR
	echo "trying again!"
done

while :
do
	echo "Please type something in (^C to quit)"
	read INPUT_STRING
	echo "You typed: $INPUT_STRING"
done




