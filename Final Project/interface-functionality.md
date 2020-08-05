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

