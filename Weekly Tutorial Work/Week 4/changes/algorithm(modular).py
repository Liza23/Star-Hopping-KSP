import math
import pandas as pd

class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self,b):
    x_term = float(self.x) - float(b.x)
    y_term = float(self.y) - float(b.y)
    return math.sqrt((x_term * x_term) + (y_term * y_term))
  
  
  class hop_func():
  
  def __init__(self, limit_range, max_stars, limiting_brightness, x, y):
    # this value is used to avoid returning of hops even 
    # when there is no nearby star (e.g. editor clicking
    # somewhere near the borders).
    self.limit_range = limit_range
    
    # max_stars is the limit put to remove unnessecory 
    # faint stars from our star list
    self.max_stars = max_stars
    
    # limiting_brightness is the minimum brightness below 
    # which we consider a star to be faint
    self.limiting_brightness = limiting_brightness
    
    self.click = Point(x, y)
    

  # the function list_star() returns a list of stars that lie 
  # within the sqaure formed with the click as center
  def list_stars(self, data):
    stars_catalogue = pd.DataFrame(columns = ['star','ra','dec','brightness'])

    l_x_limit = float(self.click.x) - self.limit_range
    r_x_limit = float(self.click.x) + self.limit_range
    l_y_limit = float(self.click.y) - self.limit_range
    r_y_limit = float(self.click.y) + self.limit_range

    data = data.sort_values(by = ['ra', 'dec'])
  
    for i in range(len(data)):    
      while (data['ra'][i] > l_x_limit and data['ra'][i] < r_x_limit) and (data['dec'][i] > l_y_limit and data['dec'][i] < r_y_limit):
        stars_catalogue = stars_catalogue.append({'star': data['star'][i], 'ra': data['ra'][i], 'dec': data['dec'][i], 'brightness': data['brightness'][i]}, ignore_index=True)
        break

    if len(stars_catalogue) >= self.max_stars:
       stars_catalogue = stars_catalogue[stars_catalogue['brightness'] > self.limiting_brightness]

    return stars_catalogue

  
  # the function min_distance() will return the value of the nearest 
  # star to the clicks from the selected stars. 
  def min_distance(self, star_catalogue):
    star_name = None

    stars_point = []
    # star_point is list of Point objects with ra as 
    # the x and dec as the y values of the star.
    for i in range(len(star_catalogue)):
      x = star_catalogue['ra'][i]
      y = star_catalogue['dec'][i]
      p = Point(x,y)
      stars_point.append(p)
  
    try:
      min_val = self.click.distance(stars_point[0])
      min_star = stars_point[0]
  
      count = 0
      # to keep a track of stars which are at a same value from our click
  
      for i in range(0, len(stars_point)):
        if min_val >= self.click.distance(stars_point[i]):
          min_val = self.click.distance(stars_point[i])
          min_star = stars_point[i]
          star_name = star_catalogue['star'][i]

      for i in range(len(stars_point)):
        if min_val == self.click.distance(stars_point[i]):
          count += 1

      assert(count == 1)
      

      return min_star, star_name
  
    except AssertionError:
      print("Two or more stars found nearby! Try again")
      temp = Point(None, None)
      return temp, None
    
    except IndexError:
      print("No star found in the region you click! Try again")
      temp = Point(None, None)
      return temp, None

  # the function hop_near_click() returns the hopped star nearest to
  # clicked point with 
  
  def hop_near_click(self, star_catalogue, hops):
    star_point, star_name = self.min_distance(star_catalogue)
    hops = {'star': star_name, 'ra': star_point.x, 'dec': star_point.y}
    return hops
  
# Driver code with temp data
data = {'star': ['a', 'b', 'c', 'd'], 'ra': [100, 50, 400, 120], 'dec': [10, 20, 40, 20], 'brightness': [0.1, 0.2, 0.3, 0.4]}
df = pd.DataFrame (data, columns = ['star','ra','dec','brightness'])

# uncomment these lines to load data and add original url as well
# df = pd.read_csv('url')
# df.head()

def save_hops():
  hops = pd.DataFrame(columns = ['star','ra','dec'])
  flag = True
  while(flag):
    x = input("x = ")
    y = input("y = ")
    flag = input("flag = ")
    hop_stars = hop_func(50, 50 , 0.1, x, y)

    stars_catalogue = hop_stars.list_stars(df)
    hopped_star = hop_stars.hop_near_click(stars_catalogue, hops)
    hops = hops.append(hopped_star, ignore_index = True)

  return hops

print(save_hops())
