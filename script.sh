#!/bin/bash
script=("python youtube.py  2 youtubeLinks.txt 50 184") #Todo
counter=1
echo $script
while [ $counter -le 10 ] # Replace 10 with Number of Times You'd like for the Script to Repeat
do
	 $script
	((counter++))
done
echo "Done" # Echos Done after Script is ran X times
