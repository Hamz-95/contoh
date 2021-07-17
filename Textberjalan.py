#!/bin/bash
#bar berjalan termux
BAR='WARNING: DO NOT USE IT TO ILLEGAL PURPOSES!! '
for i in {1..47}; do
 echo -ne "\r${BAR:0:$i}"  
sleep .1
  done
 sleep 1 clear
