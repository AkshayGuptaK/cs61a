#!/bin/bash
for i in {32..35}
do
    curl https://inst.eecs.berkeley.edu/~cs61a/fa18/assets/slides/$i.sql -o $i.sql
done