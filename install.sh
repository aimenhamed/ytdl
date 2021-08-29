#!/bin/bash

rc=$(echo $SHELL | sed "s/bin//g" | sed "s/\///g")

dir=$(pwd)

echo "ytdl () {
    python3 $dir/ytdl.py $1 $2 $3 $4 $5 $6 $7
}" >> $HOME/.${rc}rc 

