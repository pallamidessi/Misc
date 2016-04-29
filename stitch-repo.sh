#!/usr/bin/env sh
   
for entry in */
do
   echo $entry
   cd "$entry"
    rm .git-rewrite
    echo $command
    git filter-branch -f --index-filter "$command" HEAD
  cd ..
done
