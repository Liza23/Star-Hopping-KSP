# Hopping
Repository containing work done in hopping project

In order to use this program, first obtain the entire folder called Database, available in this git repo.

The folder contains three files - IAU-CSN.csv which is the file containing star names, query_program_input.py which is the actual program, and requirements.txt.
Download these three files and keep them in the same folder/place.

In order to use the program, first download the prerquisite modules for the program. This can be done by creating a new conda environment and using the requirements.txt
file to generate the environments file. The instructions for this are given in requirements.txt.

After you have procurred the required packages via this method, you may use the program. Note this program has only one area of manual input - the tycho-1 catalogue download.
In order to ease the download, the program can download components of the tycho database in runs. This is done by the user by specifiying the visual magnitude as a criteria of search.
The required input will be asked for by the program. The recommended modes are:

1)generate the first file by leaving the minimum blank and maximum as 6
2)generate the second file by putting minimum as 6 and max 9.
3)third file same way from 9 to 10.5.

After this, the program will automatically procure the tycho-2 data between vmag 10.5 and 12

NOTE : These files will take some time to download, especially the last one which is quite large. If you dont want to run the last part, the option is available. At the 
end of each run the tycho download, the program will ask you if you'd like to proceed further. Once you are done simply tell the program you dont want to continue.

At the end of the program, the multiple files will be combined, which may also take time.

All the downloaded files will be in your working directory
