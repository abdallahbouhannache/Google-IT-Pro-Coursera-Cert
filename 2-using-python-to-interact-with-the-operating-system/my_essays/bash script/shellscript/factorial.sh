#!/bin/sh

factorial()
{
  if [ "$1" -gt "1" ]; then
    i=`expr $1 - 1`
    j=`factorial $i`
    k=`expr $1 \* $j`
    echo $k
  else
    echo 1
  fi
}

myfunc()
{
  echo "I was called as : $@"
  x=2
}

echo "Script was called with $@"
x=1

echo "x is $x"
#myfunc 1 2 3
myfunc 1 2 3 | tee out.log
echo "x is $x"


while :
do
  echo "Enter a number:"
  read x
  factorial $x
done

