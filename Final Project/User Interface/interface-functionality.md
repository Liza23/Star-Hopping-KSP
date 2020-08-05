# Complete Look
This is the first complete look of the interface of how it appears when the user tries to run the program for the first time. Let's try to under the functionality of everything one by one.
## Input Fields
### Name of the Messier Object
The first field asks "Which Messier object you want to hop?". Here the user have to give input of the name of messier object. The problem here was that different user will give different variations of input. **Ex:** For M31, the possible inputs could be M 31, m 31, Andromeda, andromeda galaxy, etc. Hence, we had to take care that whatever the user gives as input, we map it to the unique value of RA/DEC that corresponds to each of them. This problem was sorted by deploying a **Name Resolver** which is also written in *Python* and does the mapping work. 

**Some guidlines while giving an input:** Even though the Name resolver will map the input to the RA/DEC value of the messier object. It is advised to give input in any of the following forms: M x/ m x/ common-name. Don't try giving inputs like M-x/ m-x/ Mx, etc. Here, x is the Messier number of the object.

## Telescopic Details
### Aperture of the telescope
This is a necessary field and is used for calculating the limiting magnitude of the telescope using the formula:
> **m_lim = 2+5(log<sub>10</sub>(aperture))**

If you're new to astronomy and want to just test how the interface works, a value of 250 mm should a good to test value.

### Choose the telescopic view
Two radio buttons are provided for choosing the type of telescopic view i.e. either through the eyepiece or through the finder scope. 

### Field of view
Here the user is given an option to either enter the apparent field of view, along with the maginification of the telescope or enter the true field of view. In case he choose to the former, the true field of view is calculated by the formula:
> **true_fov = apparent_fov/magnification**

## Submit
This button is used to submit the values that you've entered as an input. If one doesn't press this, then the values will not be read.
- If all the values are entered successfully, then a pop-up message saying *"The values are submitted sucessfully."* comes. 
- If the user tries to press the submit button without filling all the fields, he gets an pop-up message saying *"Please complete all the relevant input boxes!"*.
- If the user enters the input of messier name as something random and too common like "galaxy", then he gets an pop-up message saying *"Many such object exists. Try something specific!"*
- If the user enters a messier object that doesn't exist, like "Liza", then he gets an pop-up message saying *"No such object exists. Try again!"*

## Hopping Plots 
After successfully submitting the values, the user has to chose the type of plot interaction, i.e. static or interactive. 
### Static Plot
If a user choose a static plot button, then he'll be able to see the entire hopping sequence in one go, which will appear as white lines on the sky plot. 

### Interactive Plot
If a user chooses an interactive plot, two more buttons will appear on the screen, one would be the "Next" button and other will be "Show full sequence" button. If a user will click on the next button, he would be able to see the hops one by one, in sequence along with the hopping text that would appear next to the next button. "Show full sequence" button can be used by the user anytime to see the full hopping sequence at any point of time.

## Telescopic Plots
Two telescopic plots can be generated as per user choice, on having field of view through eye piece and other through finder scope. 
