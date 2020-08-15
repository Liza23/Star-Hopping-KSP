## Install all relevant packages
import matplotlib
import matplotlib.pyplot as plt, mpld3 
from mpld3 import plugins
from mpld3 import utils
import json 
import numpy as np
import pandas as pd
import math

## The class ClickInfo() is used for storing the clicks 
## in the interactive plot for hopping
class ClickInfo(plugins.PluginBase):
    """Plugin for getting info on click"""

    
    JAVASCRIPT = """
    mpld3.register_plugin("clickinfo", ClickInfo);
    ClickInfo.prototype = Object.create(mpld3.Plugin.prototype);
    ClickInfo.prototype.constructor = ClickInfo;
    ClickInfo.prototype.requiredProps = ["id"];
    function ClickInfo(fig, props){
        mpld3.Plugin.call(this, fig, props);
    };
    
    // Function to download the contents
    function download(content, fileName, contentType) {
    var a = document.createElement("a");
    var file = new Blob([content], {type: contentType});
    a.href = URL.createObjectURL(file);
    a.download = fileName;
    a.click();
    }
    
    var hops_list = "" ;
    var target = "";
    
    // 1. Create Save button
    var button = document.createElement("button");
    button.innerHTML = "Save Hops";

    // 2. Append somewhere
    var body = document.getElementsByTagName("body")[0];
    body.appendChild(button);

    // 3. Add event handler
    button.addEventListener ("click", function() {
      download(hops_list, 'hops.txt', 'text/plain')
      alert("Downloaded Hops");
    });
    
    // 1. Create Undo button
    var button = document.createElement("button");
    button.innerHTML = "Undo";

    // 2. Append somewhere
    var body = document.getElementsByTagName("body")[0];
    body.appendChild(button);

    // 3. Add event handler
    button.addEventListener ("click", function() {
      var str = hops_list.slice(0,-39);
      hops_list = str;
      alert("One Hop-Click Deleted");
    });
    
    // 1. Create Target Input button
    var button = document.createElement("button");
    button.innerHTML = "Enter Target";

    // 2. Append somewhere
    var body = document.getElementsByTagName("body")[0];
    body.appendChild(button);

    // 3. Add event handler
    button.addEventListener ("click", function() {
      var object = window.prompt("Enter the name of target object: ");
      target = target + " " + object;
      download(target, 'target.txt', 'text/plain')
      var filename = "target.txt"
      var blob = new Blob([target], {
       type: "text/plain;charset=utf-8"
      });
      //saveAs(blob, filename)
      
    });
    
    // function to write to a text file
    function writeTextFile(afilename, output){
      var txtFile = new File(afilename);
      txtFile.writeln(output);
      txtFile.close();
    }
              
    ClickInfo.prototype.draw = function(){
        var obj = mpld3.get_element(this.props.id);
        obj.elements().on("mousedown",
                          function(d, i){hops_list=hops_list+ "  " +d ; console.log(hops_list);}
                          );
                           
    }
    """
    
    def __init__(self, points):
        self.dict_ = {"type": "clickinfo",
                      "id": utils.get_id(points)}



## The class Point() is used to store a 2-dimensional 
## coordinate poin, here used for storing RA and DEC 
## value of stars and clicked points
class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self,b):
    x_term = float(self.x) - float(b.x)
    y_term = float(self.y) - float(b.y)
    return math.sqrt((x_term * x_term) + (y_term * y_term))



## The class hop_func() contain all the functions used 
## for finding hops and then saving them in a csv file.
class hop_func():
  
  def __init__(self, limit_range, max_stars, limiting_brightness, x, y):
    self.limit_range = limit_range
    self.max_stars = max_stars
    self.limiting_brightness = limiting_brightness
    self.click = Point(x, y)

  # the function list_star() returns a list of stars that lie 
  # within the sqaure formed with the click as center
  def list_stars(self, data):
    stars_catalogue = pd.DataFrame(columns = ['name','ra','dec','mag'])

    l_x_limit = float(self.click.x) - self.limit_range
    r_x_limit = float(self.click.x) + self.limit_range
    l_y_limit = float(self.click.y) - self.limit_range
    r_y_limit = float(self.click.y) + self.limit_range

    stars_catalogue = data[(data['ra'] > l_x_limit) & (data['ra'] < r_x_limit) & (data['dec'] > l_y_limit) & (data['dec'] < r_y_limit)]

    # for i in range(len(data)):  
    #   if float((data['ra'].iloc[i]) > l_x_limit and float(data['ra'].iloc[i]) < r_x_limit) and ((data['dec'].iloc[i]).astype(float) > l_y_limit and (data['dec'].iloc[i]).astype(float) < r_y_limit):
    #     stars_catalogue = stars_catalogue.append({'star': data['id'].iloc[i], 'ra': data['ra'].iloc[i], 'dec': data['dec'].iloc[i], 'mag': data['mag'].iloc[i]}, ignore_index=True)
        

    if len(stars_catalogue) >= self.max_stars:
       stars_catalogue = stars_catalogue[stars_catalogue['mag'] > self.limiting_brightness]

    return stars_catalogue


  # the function min_distance() will return the value of the nearest 
  # star to the clicks from the selected stars.  
  def min_distance(self, star_catalogue):
    star_name = None

    stars_point = []
    # star_point is list of Point objects with ra as 
    # the x and dec as the y values of the star.
    for i in range(len(star_catalogue)):
      x = star_catalogue['ra'].iloc[i]
      y = star_catalogue['dec'].iloc[i]
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
          star_name = star_catalogue['name'].iloc[i]

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
    hops = {'name': star_name, 'ra': star_point.x, 'dec': star_point.y}
    return hops


'''Reading the Star Catalogue Dataset'''
#reading catalog and dropping nan values
star_cat = pd.read_csv("tycho-1.csv",nrows=5031)
star_cat = star_cat.dropna(subset=["mag"])

#reading columns
ra = star_cat["ra"]
dec = star_cat["dec"]
#spect = star_cat["spect"]
star_cat['Bayer'] = star_cat['Bayer'].fillna('-')
mag = star_cat["mag"]
flux = (10**(-mag/2.5))*0.1
ident = [star_cat['name'][i] if star_cat['name'][i]!='-' else star_cat['Bayer'][i] for i in range(len(ra))]

# Get Saved clicked points
clicks = open("hops.txt")
store_clicks = []
for x in clicks:
	x = x.strip()
	store_clicks = x.split("  ")

## Plotting the Graph
fig, ax = plt.subplots(figsize=(20,12))
points = ax.scatter(ra,dec,s=1e4*flux,color="white")
#mes_points = ax.scatter(mes_ra,mes_dec,s=10,color="red")
labels = ["[RA {} \v DEC {} \v Name {}]".format(ra[i],dec[i],ident[i]) for i in range(len(ra))]
#mes_labels = ["[RA {} \v DEC {} \v Name {}]".format(mes_ra[i],mes_dec[i],mes_ident[i]) for i in range(len(mes_ra))]
tooltip = plugins.PointLabelTooltip(points, labels)
#mes_tooltip = plugins.PointLabelTooltip(mes_points, mes_labels)
plugins.connect(fig, tooltip)
plugins.connect(fig, ClickInfo(points))
#plugins.connect(fig, mes_tooltip)
#plugins.connect(fig, ClickInfo(mes_points))

ax.set_facecolor('skyblue')
ax.grid(alpha=0.3)
ax.set_xlabel("RA", size =20)
ax.set_ylabel("DEC", size =20)
#plt.savefig("test1.png")

mpld3.show()


## This function calls all the functions to be used for hopping
def save_hops():
  hops = pd.DataFrame(columns = ['name','ra','dec'])
  for elem in store_clicks:
  	elem = elem.split(",")
  	x = float(elem[0])
  	y = float(elem[1])

  	hop_stars = hop_func(10, 5, 5, x, y)
  	stars_catalogue = hop_stars.list_stars(star_cat.filter(items=['name', 'ra','dec','mag']))
  	hopped_star = hop_stars.hop_near_click(stars_catalogue, hops)
  	hops = hops.append(hopped_star, ignore_index = True)

  return hops

## final hop sequence gets saved to a csv file
final_hop_sequence = save_hops()
final_hop_sequence.to_csv("hopping.csv")
