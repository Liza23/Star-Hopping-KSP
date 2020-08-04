# Setup Instructions

Follow these instructions in order to run editor interface and hop stars:

## Inital Setup

- Download the folder **Editor Interface** in your PC.
- The script is written in Python with backend in JavaScript and a python compiler is needed to run the file. So, ensure that you've a python compiler in your PC.

## Downloading the Database.

- Within the editor interface folder lies the **Database** folder. This is where all the database csv files, once downloaded, will be placed.
- This folder contains three files - IAU-CSN.csv which is the file containing star names,`query_program_input.py` which is the program that will download the database, and requirements.txt.
- In order to use the program, first download the prerquisite modules for the program. This can be done by creating a new conda environment and using the requirements.txt file to generate the environments file. The instructions for this are given in requirements.txt.
- After you have procurred the required packages via this method, you may use the program. This program will automatically download the messier catalogue, NGC catalogue and the constellation borders.
- The download of the Tycho-1 stellar catalogue has been split into three runs - 1) from minimum till Vmag 6; 2) From Vmag 6 to 9; 3) From Vmag 9 to 10.5. Before each run the program will prompt if you want to proceed. This allows you to skip any of these runs if necessary. However, IT IS RECOMMENDED THAT YOU DOWNLOAD THE ENTIRETY OF THE TYCHO-1 DATABASE. The download will by default always download till Vmag 6.
- After the download of Tycho-1, the program will ask if you would like to download the tycho-2 csv. The download of this file is completely optional, given that it is a large file (~150 Mb) and covers Vmag 10.5 to 12. Choosing not to download this program will not affect usage of the interface.

For any other queries, please head to [this repository](https://github.com/SahyadriDK/Hopping). Make sure to read the ReadMe.md file in this repository before you actually move on to downloading the data files. 

## Pre-hopping instructions

- You need to set the value of `limit_range`, `max_stars`, `limiting_brightness` according to your dataset, you can read what these terms mean in the [documentation](). These need to changed only at one place i.e. *line 263* while calling the function `hop_func()`. Currently, `limit_range` is set to 10 currently, `max_stars` to 1000 and `limit_brightness` to 6. These work well with the current dataset and need not be changed if you continue to use the same database as used in this project.
- We have a sample csv file named [hops_M37.csv](https://github.com/Liza23/Star-Hopping-KSP/blob/master/Final%20Project/Editor%20Interface/hops_M37.csv) in which we captures the hopping sequence for M 37.
- You would have to create your own blank csv file with naming convention hops_Mx, where x would be the Messier object number you're trying to hop and save in the same directory where you're trying to run `editor_interface_final.py`.

## Hopping stars on Interactive Plot

- Once everything is ready, you can try running the file in the complier using command `python editor_interface_final.py`. A **mpld3** plot will open in your browser and you can click on the stars which you want to hop in correct sequence. The plot has various functionalities can be looked upto (here)[].
- Once, you're done hopping, click on **Save hops** and you'll see a pop-up where you can enter any information you want to enter along with the hops.
- **Important:** While giving the hopping text information, follow the following format:
  - Enter all information you're trying to give for one hop in the entire sequence in a single line. 
  - Use `Shft+Ctrl` to enter into new line and then give the information for the next hop.
  - Once done, press `Enter`.
- Two files will be download, `hopslist.txt` and `hopinfo.txt`.
- In case you do not want to give any hopping information, it's an optional step. `null` gets stored inside the `hopinfo.txt` file in that case.
- Make sure that you transfer the downloaded file to the **Editor Interface** folder and delete the already existing `hopslist.txt` and `hopinfo.txt` file from the folder **before** you take any step further.
- **Very important step:** make sure to press `Ctrl+C` to stop server action and let the script run further. Be careful to not interrupt the entire running code, by pressing `Ctrl+c` more than once! You'll see a confirmation *stopping server...* message in the terminal.

## Post-hopping instrustions

- It'll take a second or so to get hopping completed and you can check your sequence in the csv file that you created initially!

> Happy hopping!
