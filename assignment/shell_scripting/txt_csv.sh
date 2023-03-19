#!/bin/bash

#Downloading the required txt file from the url
wget -O NAVAll.txt http://www.amfiindia.com/spages/NAVAll.txt

#Extracting the required Data Fields
cat NAVAll.txt | cut -d ';' -f 4,5 > shell_output.csv

#Removing the .txt file 
rm NAVAll.txt
echo "Done. Results saved in shell_output.csv"
