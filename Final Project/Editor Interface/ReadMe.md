# Editor Interface
This is the editor interface that we've created to the hop stars. The picture below is how the [interface](example-images/interface.png) looks. It has various funationalities like zoom, save, undo, see the last hop, see the list of hops, etc. The interface backend is written in *Javascript*.

## Folder Structure
- The code for designing editor interface along with the algorithm is contained in `editor_interface_final.py` file.
- `hoplist.txt` and `hopinfo.txt` are the files that were downloaded while trying to hop M 37 as an example.
- `hops_M37.csv` is the final file that contains the hop sequence along with the hopping instructions.

## Working
The editor has to click at the point where he wants to hop the stars. In this process, it may also happen that the editor clicks at a false point by mistake, in such a case he can delete the hop using the button function avaialable. Once done, he has to click on the "Save Hops" button and he'll get an option to enter some information as text, which is optional. Finally, 2 files get downloaded, one is the `hoplist.txt` which contains the hop sequence and `hopinfo.txt` which contains the information that you've entered.

## High-level Code Overview
To understand the code fully, refer to the [coding documentation](). On a broader level, in the file `editor_interface_final.py`, *line 1-450* aims at making the plot and the editor interface and the rest deals with the hopping algorithm.

## Example Explaination
We've created sample hops for M-37. The entire hop information is present in file `hops_M37.csv`. It contains the stars in the hopping sequence along with the text that the editor have entered during the hopping. 

## Setup And Usage
Please read the Set-Up Instructions available [here]() to try hopping yourself as well.

> Happy Hopping
