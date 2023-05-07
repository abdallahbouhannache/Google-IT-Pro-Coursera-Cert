#!/bin/bash


#if grep "127.0.0.1" /etc/hosts; then

if [  $( grep -o "127.0.0.1" /etc/hosts ) ]; then

	echo "-everything is good-"

else

	echo "-localhost cannot be found inside /etc/hosts-"

fi


