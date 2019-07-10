#!/bin/bash
for i in {10..37}
do
    curl https://inst.eecs.berkeley.edu/~cs61a/fa18/assets/slides/$i.py -o $i.py
done