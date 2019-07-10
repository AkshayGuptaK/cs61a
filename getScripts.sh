#!/bin/bash
for i in {1..37}
do
    curl https://inst.eecs.berkeley.edu/~cs61a/fa18/assets/slides/0$i.py -o $i.py
done