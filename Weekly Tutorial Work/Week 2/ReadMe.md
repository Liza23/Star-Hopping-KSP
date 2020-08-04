# Overview
This week was more coding focused and we had to make our Minesweeper Game and had to figure out ways of making star plots.

## Backend (Database + Scripting)
Use the HYG v1.1 catalogue [here](http://www.astronexus.com/hyg). Write a function to take in an RA, Dec and Field of View, and return a plot showing the stars in the relevant field of view. The size of the markers should correspond to the brightness (i.e. Flux) of the star. Can you think of some way to include color in this as well? 

We would like to include in cuts on magnitude so that the field of view is representative of what we would be able to see. After you are done with the above task, find out how you can calculate the Field of View, and limiting magnitude given the Aperture of a telescope and the focal length of the objective and eyepiece. Change your function to have the parameters of the telescope as arguments instead of the Field of View. Also include the magnitude cuts. 

## Interface
Develop a [Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) game using pygame.

### User Interface: 
Initially uniform boxes, on clicking each box we should show the number of mines in surrounding boxes. 
There should be a counter for time and counter for number of flags and an emoji which should turn sad if user lands on mine and happy if he can flag every mine in the plot

### Admin Interface:
Here we should allow admin to add mines at random places on the plot. 

### Relevance to project:
The final aim of the interfaces part of the project is to create an user interface to show the hopping sequence from one stellar object to other with arrows and other admin interface is for creating these hopping sequences from the data we get from databases and scripting part of this project, where we would be clicking on the data to mark objects and their number in the sequence and finally creating a downloadable hopping guide by adding arrows in the order of the sequence. 

This sample project gives an insight into how to design the interfaces and what can be improved.
