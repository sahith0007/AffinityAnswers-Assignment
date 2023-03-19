# Shell Script to Download and Extract Data Fields from NAVAll.txt File
This shell script is designed to download a text file from a given URL and extract the required data fields from the file. The extracted data is then saved in a CSV file and the original text file is removed.

## Prerequisites
* Linux or Unix-based operating system with Bash shell
* **`wget`** utility to download the text file from the URL
* **`cut`** utility to extract the required data fields
* Text editor (optional)
## Usage
1. Download the shell script file or create a new file with **`.sh`** extension.
2. Open the terminal and navigate to the directory where the script file is located.
3. Run the script using the following command: **`./script.sh`**
4. The script will download the text file from the specified URL, extract the required data fields, and save the results in a CSV file named **`shell_output.csv`.**
5. The original text file will be removed from the directory.
6. The script will display a message "`Done. Results saved in shell_output.csv`" indicating that the operation has been completed successfully.
## Script Explanation
The shell script consists of the following commands:

1. **`wget -O NAVAll.txt http://www.amfiindia.com/spages/NAVAll.txt`**: This command downloads the text file from the specified URL and saves it with the name NAVAll.txt.

2. **`cat NAVAll.txt | cut -d ';' -f 4,5 > shell_output.csv`**: This command extracts the required data fields from the downloaded text file using the cut utility. The -d option specifies the delimiter used in the text file, and the -f option specifies the fields to be extracted. The extracted data is then redirected to a CSV file named shell_output.csv.

## Note
The script can be modified to extract different data fields from the text file by changing the field numbers in the **`cut`** command.
