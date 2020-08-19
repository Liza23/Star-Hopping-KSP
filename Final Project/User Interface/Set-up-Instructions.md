# Setup Instructions

Follow these instructions in order to run user interface and see the beautiful star hops!

## Inital Setup

- Download the folder **User Interface** in your PC.
- The script is written in Python and a python compiler is needed to run the file. So, ensure that you've a python compiler in your PC.

## Libraries needed

There are some libraries which need to be installed for the `user_interface.py` code to run. So, make sure you install the below mentioned libraries before hand (most of these can be installed using the python `pip` command).

> tkinter, re, numpy, pandas, matplotlib and, basemap

For downloading basemap library, follow either of these link to download `basemap-1.2.0-cp37-cp37m-win_amd64.whl`, where `37` is used to match with the python version used, you can choose others according to the python complier version that you've locally:
- [Link 1](https://wheelhouse.openquake.org/v3/windows/py37/)
- [Link 2](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

You need to save the file download in the **User Interface** folder itself and then run the following command:

`pip install basemap-1.2.0-cp37-cp37m-win_amd64.whl` (change version accordingly)

**Note:** The local machine has the highest python version as 3.7 and hence used `basemap-1.2.0-cp37-cp37m-win_amd64.whl`. This file couldn't be uploaded due to larger file size.

## Downloading the Database.

- Within the editor interface folder lies the **Database** folder. This is where all the database csv files, once downloaded, will be placed.
- This folder contains three files - IAU-CSN.csv which is the file containing star names,`query_program_input.py` which is the program that will download the database, and requirements.txt.
- In order to use the program, first download the prerquisite modules for the program. This can be done by creating a new conda environment and using the requirements.txt file to generate the environments file. The instructions for this are given in requirements.txt.
- After you have procurred the required packages via this method, you may use the program. This program will automatically download the messier catalogue, NGC catalogue and the constellation borders.
- The download of the Tycho-1 stellar catalogue has been split into three runs - 1) from minimum till Vmag 6; 2) From Vmag 6 to 9; 3) From Vmag 9 to 10.5. Before each run the program will prompt if you want to proceed. This allows you to skip any of these runs if necessary. However, IT IS RECOMMENDED THAT YOU DOWNLOAD THE ENTIRETY OF THE TYCHO-1 DATABASE. The download will by default always download till Vmag 6.
- After the download of Tycho-1, the program will ask if you would like to download the tycho-2 csv. The download of this file is completely optional, given that it is a large file (~150 Mb) and covers Vmag 10.5 to 12. Choosing not to download this program will not affect usage of the interface.

For any other queries, please head to [this repository](https://github.com/SahyadriDK/Hopping). Make sure to read the ReadMe.md file in this repository before you actually move on to downloading the data files. 

## Using the interface

Once the set-up is done, you're ready to use the interface. For understanding how to give inputs to use the interface, follow [interface functionality](https://github.com/Liza23/Star-Hopping-KSP/blob/master/Final%20Project/User%20Interface/interface-functionality.md). 

> Happy Hopping!