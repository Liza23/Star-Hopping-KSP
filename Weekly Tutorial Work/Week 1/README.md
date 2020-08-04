# Overall
This week was more focused on the getting started with Star Hopping, getting familiar with the astronomical terms like field of view, surface brightness, etc. 

## Backend (Database+Scripting)
We will in general be dealing with more than stars and planets in the course of this project. The main objective of this first part is to get everybody acquainted with different types of deep-sky objects. 
Try to find out more about the following: 
1. Star Clusters (Open and Globular)
2. Nebulae (Several types)
3. Galaxies (Several types)
4. Double Stars (or Binary Stars)

Since we will focus on the observability of these objects, we must understand how to quantify brightness and resolution as well. Please find out more about the following concepts:
1. Visual Magnitude
2. Surface Brightness
3. How magnification affects the visibility of objects

## Star Hopping
Each Messier object would have what we call a marker star which would be the nearest bright star and from which we can find a reasonable enough hop to reach our desired object. The marker must not necessarily be the nearest star but it should be 
- One which one can make out unambiguously in the night sky like a significant star of a prominent constellation (Antares in Scorpion to hop to M4 globular cluster) or
- A lone/known star in the region (Vega(not so lonely) to reach the Ring Nebula) or
- A star easy to find using other constellation nearby ( eg: Sirius using Orion for hopping onto M41 star cluster in Canis Major)

Once these marker stars/objects are identified we need to find a track/path to the object. Strategic objects in the sky which are easy to keep track of and also help as a base for further hop on to the object. One by one, the observer will move from one object to the next until they come into a striking range of the object and Voila, they have the object in their telescope field of view. Our aim is to create these paths and guide the observer on his tryst to find the Messier object. 

We need to eliminate the unnecessary stars and keep only those of strategic importance while hopping and create a star by star guide for all Messier objects. It will take some time for you to get a hang of this as it is very easy to get lost in the sky but once you get a knack of it, you just have to let that inner explorer and navigator out on this voyage of Messiers.
Also, we need to take care of some technical details like the limit on the magnitude of stars at some places, the flipping of image in the telescope, the difference in the field of view at different magnifications and finally keeping it as simple as possible

## Interface
In the first week, we would be trying to fetch data from a repository, and display it inside a window. Then we would try to create a smaller window and then add buttons to move around the image. We can use either Tkinter or Pygame or pygui for this.
1. User Interface: 
   - Graphical User interface (GUI) to slid along the image
2. Admin/Editor Interface:
   - GUI to show a dotted image and whenever he clicks a point, we will change the color of the dot to some random color/ and a box to the color that they want it to change.
