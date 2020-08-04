# Setup Instructions

Follow these instructions in order to run editor interface and hop stars:

## Inital basic Setup for Database

- Download the folder **Editor Interface** in your PC.
- The script is written in Python with backend in JavaScript and a python compiler is needed to run the file. So, ensure that you've a python compiler in your PC.
- In our project, we're using all the 4 csv files inside [Database](https://github.com/Liza23/Star-Hopping-KSP/tree/master/Final%20Project/Editor%20Interface/Database) folder. So, download/ add the database folder in the same **Editor Interface** folder where you're working.  
- You must also download [requirements.txt](https://github.com/SahyadriDK/Hopping/blob/master/requirements.txt) file in the same folder, if not already present. 
- You can use your own database as well, but this database used here is the very exhaustively compiled and is compatible with the code. In case you want to use your own database, ensure that you change the code accordingly.

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
