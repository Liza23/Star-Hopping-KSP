# Documentation
- `main()` is the main function that drives the code. It takes input until no further input is given i.e. when the user wants to give no more input, they need to leave a blank space when asked for flag input.

- In each loop of input it first creates a Point object with the name click and coordinates of click as the input x and input y, then calls a function `list_stars()` to return a pandas data frame of only those stars that lie within the limiting square with click Point as the center.
Since, a lot of other information is stored along with the star it is good to return the data frame rather than some list containing only the stars coordinates.

- While returning such a list we also need to see that if we are returning all the brightest stars closer to the object; well this can be incorporated like if there are a lot of stars within the limiting square then only take the brightest (lets say) 50 stars and remove the other unnecessary faint stars.

- After this, we call the function `save_hops()` to save the hops which would then call a function `min_distance()` inside it, where `min_distance()` would return the star which is at the minimum distance from the clicked point. In `min_distance()` function we first need to create a list of Point object for the stars in the star catalogue with their ra values as x and with dec values as y, which can be used to give back the minimum distanced star. Here, we also take care of two exceptions which are if there is one star found inside the limiting square, which could happen if the user accidentally clicks at a boundary point IndexError would be raised in such a case. And, other exception could be if there are more than two stars inside the limiting square at same minimum distance, this time an **AssertionError** is raised. 

- Finally `save_hops` returns the latest hop and it gets appended in the hop data frame in the `main()` function.

- Initially I thought of including a way to check if the editor clicked on the star itself to reduce computation but then on observing closely, I found that the Time complexity of the algorithm is **O(n)** and wouldn't be affected on introducing new checking method. 

**Note:** Limiting star is the star with the center as the clicked point and its length being `2*limiting_value` of the length which can be decided as per conditions.

# Explanation of an example
1. x = 200 and y = 20
The Point lies on star 'b' which is returned.
2. x = 100 and y = 10
The Point lies on star 'a' which is returned.
3. x = 0 and y = 0
In this case a square with boundary points as (50, 50), (50, -50), (-50, 50) and (-50, -50) is created and we can see clearly that no star lies inside the limiting square and hence None value is returned.
4. x = 225 and y = 50 
In this case a square with boundary points as (275, 100), (275, 0), (175, 100) and (175, 0) is created and we can see clearly that only (200, 20) lies inside the limiting square and hence is returned.

**The Nan value can be removed finally if we want by a simple operation.**
