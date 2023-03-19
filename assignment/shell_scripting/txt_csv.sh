wget -O NAVAll.txt http://www.amfiindia.com/spages/NAVAll.txt
cat NAVAll.txt | cut -d ';' -f 4,5 > shell_output.csv
rm NAVAll.txt
echo "Done. Results saved in shell_output.csv"
