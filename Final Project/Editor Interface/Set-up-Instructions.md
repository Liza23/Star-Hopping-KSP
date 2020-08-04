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

- You need to set the value of `limit_range`, `max_stars`, `limiting_brightness` according to your dataset, you can read what these terms mean in the [documentation](to-be-updated). These need to changed only at one place i.e. *line 263* while calling the function `hop_func()`.
- We have a sample csv file as well named [M 1.csv]() in which we made the trial hopping sequence.
- You would either need to create your own blank csv file (we advice it to name as per the *Messier object* you're trying to hop) and change the name `hopping.csv` in the script in *line 272*.
- Or you can delete the contents of the file `hopping.csv` and let the code run. 


## Hopping stars on Interactive Plot

- Once the database is ready and the script is modified accordingly, you can try running the file `editor-interface.py` in the complier. A **mpld3** plot will open in your browser and you can click on the stars which you want to hop in correct sequence.
- You can use **Undo** button to delete a wrong hop and finally, click on **Save Hops** to download the file `hops.txt`.
- Make sure that you transfer the downloaded file to the **Editor Interface** folder and delete the already existing `hops.txt` file from the folder before you take any step further.
- **Very important step:** make sure to press `Ctrl+C` to stop server action and let the script run further. Be careful to not interrupt the entire running code, by pressing `Ctrl+c` more than once! You'll see a confirmation *stopping server...* message in the terminal.

## Post-hopping instrustions

- Once, you see the confirmation message, it will take some time to hop the stars which would be decided by the parameters you set in the **Pre-hopping instructions** and once the script ends, you can find your hopping sequence in the file!

> Happy hopping!

### Note
This version basically saw a major change in the hopping algorithm and hence the integration of the new algorithm with the editor interface in the previous version.
