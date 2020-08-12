#!/usr/bin/python
# Default FOV is 10 

import matplotlib
import matplotlib.pyplot as plt, mpld3 
import pandas as pd 
from mpld3 import plugins
from mpld3 import utils
from matplotlib.patches import Circle
from svgpath2mpl import parse_path
import matplotlib.lines as mlines
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
    
# Input from the Editor
 
fov = 10 
def check_radec(rd):
    global radec
    if("/" in rd):
        radec = rd
    elif (rd == ''):
        radec = '0/0'
    else:
        print("Invalid format, Enter the RA/DEC again with '/' in between")
        radec = str(input())
        check_radec(radec)
        
def check_mag(magnitude):
    global mag
    if (magnitude.isdigit()):
        mag = int(magnitude)
    elif (magnitude == ''):
        mag = 25
    else:
        print('Incorrect magnitude entered, enter again')
        mag = str(input())
        check_mag(mag)

print("Enter the name of the Messier/Target object: ")
name = str(input())
print("Enter the RA/DEC of the Messier/Target object: ")
radec = str(input())
check_radec(radec)
ra = float(radec.split('/')[0])
dec = float(radec.split('/')[1])
print("Enter the limiting magnitude (positive integer only): ")
mag = str(input())
check_mag(mag)

# Class containing buttons and interactive options in the plot

class ClickInfo(plugins.PluginBase):
    """Plugin for getting info on click"""

    JAVASCRIPT = """
    mpld3.register_plugin("clickinfo", ClickInfo);
    ClickInfo.prototype = Object.create(mpld3.Plugin.prototype);
    ClickInfo.prototype.constructor = ClickInfo;
    ClickInfo.prototype.requiredProps = ["id"];
    ClickInfo.prototype.defaultProps = {labels:null};

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
    
    // 1. Create SAVE button
    var button = document.createElement("button");
    var body = document.getElementsByTagName("body")[0];
    var coords = body.getBoundingClientRect();
    button.style.cssText = "position:fixed; color: black";
    button.style.left = coords.left + "px";
    button.style.top = coords.bottom + "px";

    // 2. Append somewhere
    button.style.top = "100px";
    button.style.width = 70;
    button.style.height = 30;
    button.innerHTML = "Save Hops";
    body.appendChild(button);

    // 3. Add event handler
    button.addEventListener ("click", function() {
      var hop_info = window.prompt("Enter hop details : ");
      download(hop_info, 'hopinfo.txt', 'text/plain')
      download(hops_list, 'hopslist.txt', 'text/plain')
      alert("Downloaded Hops and it's Details ");
      hops_list = "" ;
      button2.innerHTML = "Deleted Hop: ";
      button4.innerHTML = "Click to see Hop List:" + hops_list;
      button1.innerHTML = "Last Hop: "
    });

    // 1. Create DELETED HOP button
    var button2 = document.createElement("button");
    var body2 = document.getElementsByTagName("body")[0];
    var coords2 = body2.getBoundingClientRect();
    button2.style.cssText = "position:static; color: black";
    button2.style.left = coords2.left + "300px";
    button2.style.width = 300;
    button2.style.height = 50;
    button2.innerHTML = "Deleted Hop: "

    // 2. Append somewhere
    button2.style.top = "350 px";
    body2.appendChild(button2);
    
    // 1. Create UNDO button
    var button = document.createElement("button");
    var body = document.getElementsByTagName("body")[0];
    var coords = body.getBoundingClientRect();
    button.style.cssText = "position:fixed; color: black";
    button.style.left = coords.left + "px";
    button.style.width = 70;
    button.style.height = 30;
    button.innerHTML = "Undo";

    // 2. Append somewhere
    button.style.top = "150px";
    body.appendChild(button);

    // 3. Add event handler
    button.addEventListener ("click", function() {
      var str = hops_list.split(" ");
      var del_hop = str[str.length - 1]
      hops_list = str.slice(0,str.length-1).join(' ');
      alert("Last Hop-Click Deleted " + del_hop);
      button2.innerHTML = "Deleted Hop: " + del_hop ; 
    });
    
    // 1. Create Target button
    var button = document.createElement("button");
    var body = document.getElementsByTagName("body")[0];
    var coords = body.getBoundingClientRect();
    button.style.cssText = "position:fixed; color: black";
    button.style.left = coords.left + "px";
    button.style.width = 70;
    button.style.height = 30;
    button.innerHTML = "Target object";

    // 2. Append somewhere
    var body = document.getElementsByTagName("body")[0];
    button.style.top = "200px";
    body.appendChild(button);

    // 3. Add event handler
    button.addEventListener ("click", function() {
      var object = window.prompt("Enter the name of target object: ");
      target = target + " " + object;
      //download(target, 'target.txt', 'text/plain')
      var filename = "target.txt"
      var blob = new Blob([target], {
       type: "text/plain;charset=utf-8"
      });
    });

    // 1. Create CLEAR ALL HOPS button
    var button = document.createElement("button");
    var body = document.getElementsByTagName("body")[0];
    var coords = body.getBoundingClientRect();
    button.style.cssText = "position:fixed; color: black";
    button.style.left = coords.left + "px";
    button.style.width = 70;
    button.style.height = 30;
    button.innerHTML = "Clear All";

    // 2. Append somewhere
    button.style.top = "250px";
    body.appendChild(button);

    // 3. Add event handler
    button.addEventListener ("click", function() {
      hops_list = "" ;
      alert("All Hops Deleted");
      button2.innerHTML = "Deleted Hop: ";
      button4.innerHTML = "Click to see Hop List:" + hops_list;
      button1.innerHTML = "Last Hop: "
    });
    
    // 1. Create LAST STORED HOP button
    var button1 = document.createElement("button");
    var body1 = document.getElementsByTagName("body")[0];
    var coords1 = body1.getBoundingClientRect();
    button1.style.cssText = "position:static; color: black";
    button1.style.left = coords1.left + "px";
    button1.style.right = coords1.right + "px";
    button1.style.width = 300;
    button1.style.height = 50;
    button1.innerHTML = "Last Hop: "

    // 2. Append somewhere
    // button1.style.top = "350px";
    body1.appendChild(button1);

    // 1. Create HOPS LIST button
    var button4 = document.createElement("button");
    var body4 = document.getElementsByTagName("body")[0];
    var coords4 = body4.getBoundingClientRect();
    button4.style.cssText = "position:static; color: black";
    button4.style.left = coords4.left + "px";
    button4.style.right = coords4.right + "px";
    button4.style.width = 800;
    button4.style.height = 50;
    button4.innerHTML = "Click to see Hop List:" + hops_list;

    // 2. Append somewhere
    // button4.style.top = "350px";
    body4.appendChild(button4);

    // 3. Add event handler
    button4.addEventListener ("click", function() {
      button4.innerHTML = "Hop List:" + hops_list;
      });

    // function to write to a text file
    function writeTextFile(afilename, output){
      var txtFile = new File(afilename);
      txtFile.writeln(output);
      txtFile.close();
    }
    
    ClickInfo.prototype.draw = function(){
        for(var i=0; i<this.props.id.length; i++){
            var obj = {};
            obj.label = this.props.labels[i];
            var element_id = this.props.id[i];
            mpld3_elements = [];
            
            for(var j=0; j<this.props.id.length; j++){
                var mpld3_element = mpld3.get_element(this.props.id[j], this.fig);

                // mpld3_element might be null in case of Line2D instances
                // for we pass the id for both the line and the markers. Either
                // one might not exist on the D3 side
                if(mpld3_element){
                    mpld3_elements.push(mpld3_element);
                }
            }
            
            obj.mpld3_elements = mpld3_elements;
            mpld3_element.elements().on("mousedown",
                              function(d, i){hops_list = hops_list + "  " +d ; 
                                                console.log(hops_list);
                                                alert("Hop-Stored");
                                                button1.innerHTML = "Last Hop: " + d;
                                                }
                              );
        }                   
    }  
    """
    
    def __init__(self, p, l):
        self.dict_ = {"type": "clickinfo",
                      "id": [utils.get_id(i) for i in p],
                      "labels": l
                      }
        print([utils.get_id(i) for i in p])

# Editor Interface Plot

ng = pd.read_csv('Database/NGC.csv')
ms = pd.read_csv('Database/messier_objects.csv')
cb = pd.read_csv('Database/constellation_borders.csv')
ty1 = pd.read_csv('Database/tycho-1.csv')
ty2 = pd.read_csv('Database/tycho-2.csv')


ga = parse_path("""M 490.60742,303.18917 A 276.31408,119.52378 28.9 0 1 190.94051,274.29027 276.31408,119.52378 28.9 0 1 6.8010582,36.113705 276.31408,119.52378 28.9 0 1 306.46799,65.012613 276.31408,119.52378 28.9 0 1 490.60742,303.18917 Z""")
ga.vertices -= ga.vertices.mean(axis=0)
# red

cl = parse_path("""M 541.64941,265.49102 A 270.8247,265.49102 0 0 1 270.82471,530.98205 270.8247,265.49102 0 0 1 0,265.49102 270.8247,265.49102 0 0 1 270.82471,0 270.8247,265.49102 0 0 1 541.64941,265.49102 Z""")
cl.vertices -= cl.vertices.mean(axis=0)
# yellow

pn2 = parse_path("""m 0,326.75709 v 18.09653 h 671.61069 v -18.09653 z m 326.7571,344.85359 h 18.0965 V 0 h -18.0965 z""")
pn2.vertices -= pn2.vertices.mean(axis=0)
# black

pl = parse_path("""m 65.722069,112.42727 v 2.87837 h 2.878368 v 0.87849 h -2.878368 v 2.87837 h -0.868162 v -2.87837 h -2.878368 v -0.87849 h 2.878368 v -2.87837 z""")
pl.vertices -= pl.vertices.mean(axis=0)      

cp = parse_path("""M 749.48177,361.96144 V 387.5203 H 0 V 361.96144 Z M 361.96144,0 h 25.55886 v 749.48177 h -25.55886 z m 239.5511,374.74089 A 226.77166,226.77166 0 0 1 374.74089,601.51254 226.77166,226.77166 0 0 1 147.96923,374.74089 226.77166,226.77166 0 0 1 374.74089,147.96923 226.77166,226.77166 0 0 1 601.51254,374.74089 Z""")
cp.vertices -= cp.vertices.mean(axis=0)  

pn4 = parse_path("""M 488,240 H 256 V 8 c 0,-4.418 -3.582,-8 -8,-8 -4.418,0 -8,3.582 -8,8 V 240 H 8 c -4.418,0 -8,3.582 -8,8 0,4.418 3.582,8 8,8 h 232 v 232 c 0,4.418 3.582,8 8,8 4.418,0 8,-3.582 8,-8 V 256 h 232 c 4.418,0 8,-3.582 8,-8 0,-4.418 -3.582,-8 -8,-8 z""")
pn4.vertices -= pn4.vertices.mean(axis=0)

def func(ra,dec,mag,fov):
    
# sorting objects under the user input of limiting magnitude

    mag_ng = ng[(ng["V"] <= mag)]
    mag_ms = ms[(ms['V'] <= mag)]
    mag_ty1 = ty1[(ty1['V'] <= mag)]
    mag_ty2 = ty2[(ty2['V'] <= mag)]
        
# breathing space around the fov circle in the plot
    xl = ra-fov/2-fov/10 
    xr = ra+fov/2+fov/10
    yb = dec-fov/2-fov/10
    yt = dec+fov/2+fov/10

    fig, ax = plt.subplots(figsize=(15,7))
    ax.set_xlabel('Right Ascension (degrees)', fontsize=20)
    ax.set_ylabel('Declination (degrees)', fontsize=20)
    ax.scatter(ra,dec,s=50,marker='P',color='yellow',zorder=10)
    
# sorting objects in messier_objects.csv according to objects
    cl_ms = ms[(ms["TYPE"]=='OpC')|(ms["TYPE"]=='GlC')|(ms["TYPE"]=='Cl*')]
    pn_ms = ms[(ms["TYPE"]=='PN')]
    ga_ms = ms[(ms["TYPE"]=='G')|(ms["TYPE"]=='Sy2')|(ms["TYPE"]=='IG')|(ms["TYPE"]=='GiG')|(ms["TYPE"]=='GiP')|(ms["TYPE"]=='SyG')|(ms["TYPE"]=='SBG')|(ms["TYPE"]=='BiC')|(ms["TYPE"]=='H2G')]
    re_ms = ms[(ms["TYPE"]=='HII')|(ms["TYPE"]=='As*')|(ms["TYPE"]=='LIN')|(ms["TYPE"]=='mul')|(ms["TYPE"]=='RNe')|(ms["TYPE"]=='AGN')]

    print(f"Observing RA: {ra} deg, DEC: {dec} deg, FoV: {fov} deg, Limiting Magnitude: {mag}") 
    
    ax.set_axisbelow(True)
    ax.minorticks_on()
    ax.grid(which='major',alpha=0.3)
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black',alpha=0.3)
    ax.set_facecolor('teal')

# scatter messier
    mag = cl_ms["V"].fillna(1) 
    flux = 10**(-mag/2.5)
    p1 = ax.scatter(cl_ms['RAJ2000'],cl_ms['DEJ2000'],color='darkorange',s = 17, zorder=10, edgecolor="black")
    l1 = ["[RA {0:.5f} \v DEC {1:.5f} \v Constellation {2} \v Name {3}]".format(i,j,k,l,'.2f','.2f','%s','%s') for i,j,k,l in zip(cl_ms['RAJ2000'],cl_ms['DEJ2000'],cl_ms['Constellation'],cl_ms["Common Name"])]
    t1 = plugins.PointLabelTooltip(p1, l1)
    plugins.connect(fig, t1)

    mag = pn_ms["V"].fillna(1) 
    flux = 10**(-mag/2.5)
    p2 = ax.scatter(pn_ms['RAJ2000'],pn_ms['DEJ2000'],color='blue',s= 17, zorder=10,edgecolor="black")
    l2 = ["[RA {0:.5f} \v DEC {1:.5f} \v Constellation {2} \v Name {3}]".format(i,j,k,l, '.2f','.2f','%s','%s') for i,j,k,l in zip(pn_ms['RAJ2000'],pn_ms['DEJ2000'],pn_ms['Constellation'],pn_ms["Common Name"])]
    t2 = plugins.PointLabelTooltip(p2, l2)
    plugins.connect(fig, t2)

    mag = ga_ms["V"].fillna(1) 
    flux = 10**(-mag/2.5)
    p3 = ax.scatter(ga_ms['RAJ2000'],ga_ms['DEJ2000'],color='red',s= 17 ,zorder=20, edgecolor="black")
    l3 = ["[RA {0:.5f} \v DEC {1:.5f} \v Constellation {2} \v Name {3}]".format(i,j,k,l,'.2f','.2f','%s',"%s") for i,j,k,l in zip(ga_ms['RAJ2000'],ga_ms['DEJ2000'],ga_ms['Constellation'],ga_ms["Common Name"])]
    t3 = plugins.PointLabelTooltip(p3, l3)
    plugins.connect(fig, t3)

    mag = re_ms["V"].fillna(1) 
    flux = 10**(-mag/2.5)
    p4 = ax.scatter(re_ms['RAJ2000'],re_ms['DEJ2000'],c='darkmagenta',s= 17,edgecolor="black")
    l4 = ["[RA {0:.5f} \v DEC {1:.5f} \v Constellation {2} \v Name {3}]".format(i,j,k,l,'.2f','.2f','%s','%s') for i,j,k,l in zip(re_ms['RAJ2000'],re_ms['DEJ2000'],re_ms['Constellation'],re_ms["Common Name"])]
    t4 = plugins.PointLabelTooltip(p4, l4)
    plugins.connect(fig, t4)

# scatter ngc
    mag = mag_ng['V'].fillna(1)
    flux = 10**(-mag/2.5)
    p5 = ax.scatter(mag_ng['RAJ2000'], mag_ng['DEJ2000'], c='darkmagenta',s= 80*flux)
    l5 = ["[RA {0:.5f} \v DEC {1:.5f} \v Constellation {2} \v Name {3}]".format(i,j,k,l,'.2f','.2f','%s','%s') for i,j,k,l in zip(mag_ng['RAJ2000'],mag_ng['DEJ2000'],mag_ng['Constellation'],mag_ng['Name'])]
    t5 = plugins.PointLabelTooltip(p5,l5)
    plugins.connect(fig, t5)

# scatter tycho-1
    mag = mag_ty1['V'].fillna(1)
    flux = 10**(-mag/2.5)
    p6 = ax.scatter(mag_ty1['RAJ2000'], mag_ty1['DEJ2000'], c='white', s= 80*flux)
    l6 = ["[RA {0:.5f} \v DEC {1:.5f} \v Constellation {2} \v Name {3}]".format(i,j,k,l,'.2f','.2f','%s','%s') for i,j,k,l in zip(mag_ty1['RAJ2000'],mag_ty1['DEJ2000'],mag_ty1['Constellation'],mag_ty1['Name'])]
    t6 = plugins.PointLabelTooltip(p6,l6)
    plugins.connect(fig, t6)
    
# scatter tycho-2 
    # mag = mag_ty2['V'].fillna(1)
    # flux = 10**(-mag/2.5)
    # p7 = ax.scatter(mag_ty2['RAJ2000'], mag_ty2['DEJ2000'], c='white', s= 80*flux)
    # l7 = ["[RA {0:.5f} \v DEC {1:.5f} \v Constellation {2} ]".format(i,j,k,'.2f','.2f','%s') for i,j,k in zip(mag_ty2['RAJ2000'],mag_ty2['DEJ2000'],mag_ty2['Constellation'])]
    # t7 = plugins.PointLabelTooltip(p7,l7)
    # plugins.connect(fig, t7)
    
    points = [p1,p2,p3,p4,p5,p6]
    labels = [l1,l2,l3,l4,l5,l6]
    plugins.connect(fig, ClickInfo(points,labels))

# constellation borders
    for i in cb['Constellation'].unique():
        x = cb[(cb['Constellation']==i)]['RAJ2000']
        y = cb[(cb['Constellation']==i)]['DEJ2000']
        x1 = x.mean()
        y1 = y.mean()
        ax.scatter(x,y,color='darkgreen', s=20/fov)
        ax.annotate('%s'%i, (x1,y1),size = 13)
    
    ax.add_artist(plt.Circle((ra, dec), color='#00af08',zorder=1, alpha=0.5))
    # ax.set_xlim([xl,xr])
    # ax.set_ylim([yb,yt])
    
    cluster = mlines.Line2D([], [], color='darkorange', marker=cl, linestyle='None',
                              markersize=15, label='Clusters', markeredgecolor="black")
    planetary_neb = mlines.Line2D([], [], color='blue', marker=cl, linestyle='None',
                              markersize=15, label='Planetary Nebula',markeredgecolor="black")
    galaxy = mlines.Line2D([], [], color='Red', marker=cl, linestyle='None',
                              markersize=15, label='Galaxies',markeredgecolor="black")
    other = mlines.Line2D([], [], color='darkmagenta', marker=cl, linestyle='None',
                              markersize=15, label='Other NGC/Messier', markeredgecolor="black")
    stars = mlines.Line2D([], [], color='white', marker=cl, linestyle='None',
                              markersize=15, label='Stars', markeredgecolor="black")
    plt.legend(handles=[cluster,planetary_neb, galaxy, other, stars], labelspacing=2, ncol=5, borderpad=1, loc='lower center')

    mpld3.show()

func(ra,dec,mag,fov)

'''Hopping Algorithm begins here'''

# The class Point() is used to store a 2-dimensional
# coordinate poin, here used for storing RA and DEC
# value of stars and clicked points
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, b):
        x_term = float(self.x) - float(b.x)
        y_term = float(self.y) - float(b.y)
        return math.sqrt((x_term * x_term) + (y_term * y_term))


# The class hop_func() contain all the functions used
# for finding hops and then saving them in a csv file.
class hop_func():

    def __init__(self, limit_range, max_stars, limiting_brightness, x, y):
        self.limit_range = limit_range
        self.max_stars = max_stars
        self.limiting_brightness = limiting_brightness
        self.click = Point(x, y)

    # the function list_star() returns a list of stars that lie
    # within the sqaure formed with the click as center
    def list_stars(self, data):
        stars_catalogue = pd.DataFrame(
            columns=['name', 'RAJ2000', 'DEJ2000', 'V'])

        l_x_limit = float(self.click.x) - self.limit_range
        r_x_limit = float(self.click.x) + self.limit_range
        l_y_limit = float(self.click.y) - self.limit_range
        r_y_limit = float(self.click.y) + self.limit_range

        stars_catalogue = data[(data['RAJ2000'] > l_x_limit) & (data['RAJ2000'] < r_x_limit) & (
            data['DEJ2000'] > l_y_limit) & (data['DEJ2000'] < r_y_limit)]

        if len(stars_catalogue) >= self.max_stars:
            stars_catalogue = stars_catalogue[stars_catalogue['V']
                                              > self.limiting_brightness]

        return stars_catalogue

    # the function min_distance() will return the value of the nearest
    # star to the clicks from the selected stars.

    def min_distance(self, star_catalogue):
        star_name = None

        stars_point = []
        # star_point is list of Point objects with ra as
        # the x and dec as the y values of the star.
        for i in range(len(star_catalogue)):
            x = star_catalogue['RAJ2000'].iloc[i]
            y = star_catalogue['DEJ2000'].iloc[i]
            p = Point(x, y)
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
                    star_name = star_catalogue['Name'].iloc[i]

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
        hops = {'Name': star_name, 'RAJ2000': star_point.x,
                'DEJ2000': star_point.y}
        return hops


clicks = open("hopslist.txt")
store_clicks = []
for x in clicks:
    x = x.strip()
    store_clicks = x.split("  ")

# This function calls all the functions to be used for hopping
def save_hops():
    hops = pd.DataFrame(columns=['Name', 'RAJ2000', 'DEJ2000', 'text'])
    for elem in store_clicks:
        elem = elem.split(",")
        x = float(elem[0])
        y = float(elem[1])
        
        # limit_range is set to 10, max_stars to 1000 and limit_brightness to 6
        hop_stars = hop_func(10, 1000, 6, x, y)
        stars_catalogue = hop_stars.list_stars(
            ty.filter(items=['Name', 'RAJ2000', 'DEJ2000', 'V']))
        hopped_star = hop_stars.hop_near_click(stars_catalogue, hops)
        hops = hops.append(hopped_star, ignore_index=True)

    hop_text = open("hopinfo.txt")
    hop_text_store = []

    for x in hop_text:
        x = x.strip()
        hop_text_store.append(x)    

    hops['text'] = pd.Series(hop_text_store)
    return hops


# final hop sequence gets saved to a csv file
final_hop_sequence = save_hops()
final_hop_sequence.to_csv("hops_M37.csv")
