#!/usr/bin/env sh
   
for entry in ../*/
do
   echo $entry
   git pull $entry
done
