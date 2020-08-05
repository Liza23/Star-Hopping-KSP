import re
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from mpl_toolkits.basemap import Basemap
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.patches import Circle
from svgpath2mpl import parse_path


def telescope(fov, a):
    w = Canvas(root, width=2000, height=1000, highlightthickness=5)
    w.grid(row=10, rowspan=12, columnspan=25, sticky="NSEW", pady="2px")

    # stars below the limting magnitude of telescope, used for telescope plot
    # data_2 = file[file['V'] <= m_lim]
    # converting to celestial coordinates
    data_2 = file[(file['V'] <= m_lim) & (file['RAJ2000'] <= float(ra_in+fov)) & (file['RAJ2000'] >= float(ra_in - fov)) &
                  (file['DEJ2000'] <= float(dec_in+fov)) &
                  (file['DEJ2000'] >= float(dec_in-fov))]

    data_2['RAJ2000'] = [(360-i) if i >= 180 else (-i)
                         for i in data_2['RAJ2000']]

    RA_2 = np.array(data_2['RAJ2000'])
    DEC_2 = np.array(data_2['DEJ2000'])
    V_2 = np.array(data_2['V'])

    fig = plt.figure(figsize=(8, 8))
    ax1 = fig.add_subplot(111)
    ax1.set_facecolor('k')

    # to prevent error occuring while zooming in at the poles 2 conditions r used
    if (dec_in+fov < 80 and dec_in-fov > -80):
        m = Basemap(projection="stere",
                    llcrnrlon=ra_in-fov, llcrnrlat=dec_in-fov,
                    urcrnrlon=ra_in+fov, urcrnrlat=dec_in+fov,
                    resolution="i", lat_0=dec_in, lon_0=ra_in,
                    celestial=True, fix_aspect=False)

        m.drawparallels(range(-90, 90, 1), color='white',
                        labels=[1, 1, 0, 0], dashes=[1, 1], latmax=90)
        m.drawmeridians(range(0, 360, 1), color='white',
                        labels=[0, 0, 1, 1], dashes=[1, 1], latmax=90)
        if a == 0:
            plt.title('Field of view through eyepiece', pad=15, size=10)
        elif a == 1:
            plt.title('Field of view through finder scope', pad=15, size=10)

        ra_crc = 360-ra_in if ra_in > 180 else -ra_in
        dec_crc = dec_in
        x_crc, y_crc = m(ra_crc, dec_crc, inverse=False)
        s1 = m(ra_crc, dec_crc)
        s2 = m(ra_crc+1, dec_crc)
        r = (s1[0]-s2[0])*(fov/2)

        circle = Circle((x_crc, y_crc), r, color='r',
                        fill=False, ls='--', lw=2)
        ax1.add_patch(circle)

    else:
        popup("Field of view cannot be resolved near poles. It is the actual sky plot center at the point you aimed!")

        m = Basemap(width=2000000, height=2000000, projection="stere",
                    lat_0=dec_in, lon_0=ra_in, resolution="i", celestial=True)

        m.drawparallels(range(-90, 90, 3), color='white',
                        labels=[1, 1, 0, 0], dashes=[1, 1], latmax=90)
        m.drawmeridians(range(0, 360, 10), color='white',
                        labels=[0, 0, 0, 1], dashes=[1, 1], latmax=90)
        plt.title('Projection of sky at Pole', pad=15, size=10)

    m.drawmapboundary(color='white', linewidth=1, fill_color='k')

    x, y = m(RA_2, DEC_2)
    stars = m.scatter(x, y, color='white', s=500/2.5**V_2)

    lw = 0
    plw = 1

    x_m, y_m = m(np.array(oc_ms['RAJ2000']), np.array(oc_ms['DEJ2000']))
    ocms = m.scatter(x_m, y_m, color='yellow', marker="o", s=150,
                     linewidth=lw, label='clusters')

    x_m, y_m = m(np.array(gc_ms['RAJ2000']), np.array(gc_ms['DEJ2000']))
    gcms = m.scatter(x_m, y_m, color='black', marker="+", s=150,
                     zorder=2, linewidth=plw)

    x_m, y_m = m(np.array(gc_ms['RAJ2000']), np.array(gc_ms['DEJ2000']))
    gcms1 = m.scatter(x_m, y_m, color='yellow', marker="o", s=150,
                      edgecolor="grey",  linewidth=lw)

    x_m, y_m = m(np.array(ga_ms['RAJ2000']), np.array(ga_ms['DEJ2000']))
    gams = m.scatter(x_m, y_m, color='red', marker=ell, s=150,
                     linewidth=lw)

    x_m, y_m = m(np.array(nb_ms['RAJ2000']), np.array(nb_ms['DEJ2000']))
    nbms = m.scatter(x_m, y_m, color='green', marker="o", s=150,
                     zorder=2, linewidth=lw)

    x_m, y_m = m(np.array(nb_ms['RAJ2000']), np.array(nb_ms['DEJ2000']))
    nbms1 = m.scatter(x_m, y_m, color='white', marker="+",
                      s=400, linewidth=plw)

    x_m, y_m = m(np.array(ot_ms['RAJ2000']), np.array(ot_ms['DEJ2000']))
    otms = m.scatter(x_m, y_m, c='yellow', marker="^",
                     s=150, linewidth=plw)

    xcb, ycb = m(ra_cb, dec_cb)
    m.scatter(xcb, ycb, s=20, color='g', marker='_')
    plt.legend([ocms, (gcms1, gcms), (nbms, nbms1), gams, otms, stars],
               [" Open Cluster", "Globular Cluster", "Nebula", 'Galaxy',
                "Other Messier", "Tycho-1 Stars"], labelspacing=2, ncol=6,
               borderpad=.5, loc=8, facecolor='grey')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=2, columnspan=3)

    toolbarFrame = Frame(master=root)
    toolbarFrame.grid(row=9, columnspan=10, sticky="W")
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)


def hop_sequence_plot(lon, lat, choice):

    fig2 = plt.figure(figsize=(20, 8))
    # RA values of hops are converted to the celestial coordinates
    lon = [(360-i) if i > 180 else (-i) for i in lon]
    ax2 = fig2.add_subplot(1, 1, 1)
    ax2.set_facecolor('k')

    n = Basemap(width=10000000, height=8000000, projection="stere",
                lat_0=dec_in, lon_0=ra_in, resolution="i", celestial=True, fix_aspect=False)

    # plt.title('Hops', size=10, pad=10)
    n.drawmapboundary(color='grey', linewidth=1, fill_color='k')

    x, y = n(RA, DEC)
    stars = n.scatter(x, y, color='white', s=200/2.5**V_1)

    lw = 0
    plw = 1

    x_m, y_m = n(np.array(oc_ms['RAJ2000']), np.array(oc_ms['DEJ2000']))
    ocms = n.scatter(x_m, y_m, color='yellow', marker="o", s=150,
                     linewidth=lw, label='clusters')

    x_m, y_m = n(np.array(gc_ms['RAJ2000']), np.array(gc_ms['DEJ2000']))
    gcms = n.scatter(x_m, y_m, color='black', marker="+", s=150,
                     zorder=2, linewidth=plw)

    x_m, y_m = n(np.array(gc_ms['RAJ2000']), np.array(gc_ms['DEJ2000']))
    gcms1 = n.scatter(x_m, y_m, color='yellow', marker="o", s=150,
                      edgecolor="grey",  linewidth=lw)

    x_m, y_m = n(np.array(ga_ms['RAJ2000']), np.array(ga_ms['DEJ2000']))
    gams = n.scatter(x_m, y_m, color='red', marker=ell, s=150,
                     linewidth=lw)

    x_m, y_m = n(np.array(nb_ms['RAJ2000']), np.array(nb_ms['DEJ2000']))
    nbms = n.scatter(x_m, y_m, color='green', marker="o", s=150,
                     zorder=2, linewidth=lw)

    x_m, y_m = n(np.array(nb_ms['RAJ2000']), np.array(nb_ms['DEJ2000']))
    nbms1 = n.scatter(x_m, y_m, color='white', marker="+",
                      s=400, linewidth=plw)

    x_m, y_m = n(np.array(ot_ms['RAJ2000']), np.array(ot_ms['DEJ2000']))
    otms = n.scatter(x_m, y_m, c='yellow', marker="^",
                     s=150, linewidth=plw)

    xcb, ycb = n(ra_cb, dec_cb)
    n.scatter(xcb, ycb, s=10, color='g')

    n.drawparallels(range(-90, 90, 10), color='white',
                    labels=[1, 1, 0, 0], latmax=90)
    n.drawmeridians(range(0, 360, 10), color='white',
                    labels=[0, 0, 1, 1], latmax=90)

    if choice == 0:
        draw_static_plot(n, lon, lat)

    elif choice == 1:
        draw_interactive_plot(n, lon, lat)

    # # adding star hops
    # for i in range(1, len(lon)):
    #     n.drawgreatcircle(lon[i-1], lat[i-1], lon[i], lat[i],
    #                       color='white', linewidth=1.9)

    # lon, lat = n(lon, lat)
    # n.scatter(lon, lat, color='dimgrey', s=100, marker='o')

    # adding prominenet star names.
    Ra, Dec = n(RA, DEC)
    for i in range(300):
        if name[i] != '-':
            ax2.text(Ra[i], Dec[i]+100000, name[i], fontsize=8,
                     fontweight='bold', color='deeppink').set_clip_on(True)

        else:
            ax2.text(Ra[i], Dec[i]+100000, name_bayer[i], fontsize=8,
                     fontweight='bold', color='deeppink').set_clip_on(True)

    # adding messier main id
    Ra, Dec = n(ra_m, dec_m)
    for i in range(len(ra_m)):
        ax2.text(Ra[i]+20000, Dec[i]-200000, name_m[i], fontsize=8,
                 fontweight='bold', color='yellow').set_clip_on(True)

    # adding constellation names with location manually found
    # that best suits the figure

    const_name = np.array(pd.unique(data_cb['Constellation']))
    # const_name=np.sort(const_name)
    ra_const = [-20, 18, -45, -60, -38, -20, 10, -140, -160, 160, 160, 100, 60, 95, 95, 128,
                155, 60, 20, -10, 20, 35, 85, 98, 95, 65, 44, 60, 76, 112, 100, 60, -45,
                -80, -100, -110, -130, -110, 138, 150, 160, 155, 180, 114, -74, -90, -88,
                -95, 10, 115, 100, -165, -122, -135, -110, -125, -112, 38, -150, -120, 170,
                123, 45, -30, -65, -45, -125, 72, 167, -175, 72, 41, -69, -110, 39, -80, -90,
                -61, -50, -20, 20, 33, -10, -160, 125, -20, -165, -140]
    dec_const = [43, 45, 65, 45, 32, 15, 20, 0, -35, -40, -80, -75, -65, -50, -65, -58,
                 -70, 0, -10, -30, -30, -20, -11, -8, 22, 18, 18, -35, -14, -52, -40, -50, 20,
                 25, 40, 70, 40, 20, 25, -5, 25, 35, 40, 30, -40, -65, -50, -40, 70, 70, 60,
                 20, 3, 25, -20, -28, -5, -40, -50, -60, -60, -32, 50, -10, -20, -30, -70, -40,
                 -20, -20, 40, 25, -65, -80, 5, 10, -20, -50, -75, -50, -42, -58, -65, 0, -20,
                 -89, 30, -30]
    ra_const, dec_const = n(ra_const, dec_const)

    for i in range(len(ra_const)):

        ax2.text(ra_const[i], dec_const[i], '  '.join(const_name[i]),
                 fontsize=8, fontweight='bold', alpha=0.5, color='white').set_clip_on(True)

    plt.gca().invert_xaxis()
    plt.legend([ocms, (gcms1, gcms), (nbms, nbms1), gams, otms, stars],
               [" Open Cluster", "Globular Cluster", "Nebula", 'Galaxy',
                "Other Messier", "Tycho-1 Stars"], labelspacing=5, ncol=6,
               borderpad=.5, loc=8, facecolor='grey')

    canvas = FigureCanvasTkAgg(fig2, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, rowspan=12, columnspan=25, sticky="NW")

    toolbarFrame = Frame(master=root)
    toolbarFrame.grid(row=9, columnspan=10, sticky="W")
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)


def draw_static_plot(n, lon, lat):
    for i in range(1, len(lon)):
        print(type(lon[i]), lon[i])
        n.drawgreatcircle(lon[i-1], lat[i-1], lon[i], lat[i],
                          color='white', linewidth=1.9)
    lon, lat = n(lon, lat)
    n.scatter(lon, lat, color='dimgrey', s=100, marker='o')


interactive_i = 1


def draw_interactive_plot(n, lon, lat):
    global interactive_i
    if interactive_i < len(lon):
        for i in range(0, interactive_i):
            n.drawgreatcircle(lon[i+1], lat[i+1], lon[i], lat[i],
                              color='white', linewidth=1.9)
        interactive_i += 1
        finish_msg = tk.Label(root,
                              text="I'm hop " + str(interactive_i-1),
                              font="Times 12",
                              fg="black",
                              bg="white").grid(row=8, column=2)

    elif interactive_i == len(lon):
        draw_static_plot(n, lon, lat)
        finish_msg = tk.Label(root,
                              text="Hopping completed!!",
                              font="Times 12",
                              fg="green",
                              bg="white").grid(row=8, column=2)


# visual magnitude limit
v_mag = 6

# constellation borders
data_cb = pd.read_csv('constellation_borders.csv', encoding='latin1')
dec_cb = np.array(data_cb['DEJ2000'])
ra_cb = np.array(data_cb['RAJ2000'])
# converting the ra to celestial coordinate conventions.
ra_cb = [(360-i) if i >= 180 else (-i) for i in ra_cb]

# messier objects
data_m = pd.read_csv("messier_objects.csv", encoding='latin1')
data_m['RAJ2000'] = [(360-i) if i >= 180 else (-i) for i in data_m['RAJ2000']]

# globular clusters
gc_ms = data_m[(data_m["TYPE"] == 'GlC')]

# open clusters
oc_ms = data_m[(data_m["TYPE"] == 'OpC') | (data_m["TYPE"] == 'Cl*')]

# galaxies
ga_ms = data_m[(data_m["TYPE"] == 'G') | (data_m["TYPE"] == 'Sy2') |
               (data_m["TYPE"] == 'IG') | (data_m["TYPE"] == 'GiG') | (
    data_m["TYPE"] == 'GiP') | (data_m["TYPE"] == 'SyG') |
    (data_m["TYPE"] == 'SBG') | (data_m["TYPE"] == 'BiC') | (
    data_m["TYPE"] == 'H2G')]

# nebula and supernova remnant
nb_ms = data_m[(data_m["TYPE"] == 'PN') | (data_m["TYPE"] == 'RNe') |
               (data_m["TYPE"] == 'HII') | (data_m["TYPE"] == 'SNR')]

# other messiers
ot_ms = data_m[(data_m["TYPE"] == 'As*') | (data_m["TYPE"] == 'LIN') |
               (data_m["TYPE"] == 'mul') | (data_m["TYPE"] == 'AGN')]

ra_m = np.array(data_m['RAJ2000'])
dec_m = np.array(data_m['DEJ2000'])
name_m = np.array(data_m['ID (for resolver)'])

# star data
file = pd.read_csv('tycho-1.csv')

# stars below visual magnitude of 6, to be used for hop sequence
data_1 = file[(file['V'] <= v_mag)]
# converting to celestial coordinates
data_1['RAJ2000'] = [(360-i) if i >= 180 else (-i) for i in data_1['RAJ2000']]
RA = np.array(data_1['RAJ2000'])
DEC = np.array(data_1['DEJ2000'])
name = np.array(data_1['Name'])
V_1 = np.array(data_1['V'])
name_bayer = np.array(data_1['Bayer'])

ell = parse_path("""M 490.60742,303.18917 A 276.31408,119.52378 28.9 0 1 190.94051,274.29027 276.31408,119.52378 28.9 0 1 6.8010582,36.113705 276.31408,119.52378 28.9 0 1 306.46799,65.012613 276.31408,119.52378 28.9 0 1 490.60742,303.18917 Z""")
ell.vertices -= ell.vertices.mean(axis=0)

hops = pd.read_csv("hopping.csv")

Lon = hops['RAJ2000'].tolist()
Lat = hops['DEJ2000'].tolist()

# pass the longitude and latitude array of the hops created
# hop_sequence_plot(Lon,Lat)


root = tk.Tk()
root.resizable(True, True)

table = pd.read_csv('messier_objects_resolver.csv')
df = pd.DataFrame(table)
ident = np.array(df['ID (for resolver)'])
name_resolver = np.array(df['Common Name'])


def popup(msg):
    popup = tk.Tk()
    popup.wm_title("Message")
    label = tk.Label(popup,
                     text=msg,
                     font="Times 12",
                     fg="black",
                     bg="white")
    label.grid(row=0)
    popup.mainloop()


def get_input_values():
    global inp_in, ra_in, dec_in, fov, m_lim
    if user_input_true_fov.get() == '' or user_input_aperture.get() == '' or (user_input_apparent_fov == '' and user_input_true_fov == ''):
        popup("Please complete all the relevant input boxes!")

    elif user_input_true_fov.get() == '' and user_input_apparent_fov != '':
        apparent_fov = float(user_input_apparent_fov.get())
        magnification = float(user_input_mag.get())
        fov = float(apparent_fov/magnification)
    else:
        fov = float(user_input_true_fov.get())

    inp_in = user_input_name.get()
    aperture = float(user_input_aperture.get())
    m_lim = 2+5*np.log10(aperture)
    inp = str(inp_in)
    inp2 = inp.split()
    if all([x.isalpha() for x in inp2]):
        inp = inp.title()
        find_res = np.array([x.find(inp) for x in name_resolver])
        pos = np.where(find_res != -1)[0]
        ra_in, dec_in = df['RAJ2000'][pos].values, df['DEJ2000'][pos].values

    elif all([x.isalnum() for x in inp2]):
        inp = inp.title()
        inp = re.split('(/d+)', inp)
        inp[0] = inp[0].rstrip()
        inp = inp[:2]
        inp = ' '.join(inp)
        find_res = np.array([x.find(inp) for x in ident])
        pos = np.where(find_res != -1)[0]
        ra_in, dec_in = df['RAJ2000'][pos].values, df['DEJ2000'][pos].values

    if len(ra_in) == 0 or len(dec_in) == 0:
        popup("No such object exists. Try again!")

    if len(ra_in) > 1 or len(dec_in) > 1:
        popup("Many such object exists. Try something specific!")

    popup("Values submitted successfully!")


def next_prev():
    msg_box = tk.Label(root,
                       text="Controls for the Interactive Plot:",
                       font="Times 12",
                       fg="black",
                       bg="white").grid(row=8, column=0, sticky="W")

    next_button = tk.Button(root,
                            text="Next",
                            font="Times 10",
                            command=lambda: hop_sequence_plot(Lon, Lat, 1),
                            fg="purple",
                            bg="white").grid(row=8, column=2, sticky="W", pady="2px")

    full_button = tk.Button(root,
                            text="Show complete sequence",
                            font="Times 10",
                            command=lambda: hop_sequence_plot(Lon, Lat, 0),
                            fg="purple",
                            bg="white").grid(row=8, column=1, sticky="W", pady="2px")


width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{width}x{height}')

root.configure(bg="white")

# Hopping Title for interface
w = tk.Label(root,
             text="Hopping Stars",
             font="Times 24 bold",
             fg="#0D47A1",
             bg="white").grid(row=0, column=2)

# Hopping Subtitle for interface
w = tk.Label(root,
             text="Your complete hopping guide!",
             font="Times 12 bold",
             fg="#2962FF",
             bg="white").grid(row=1, column=2)

# Input box for getting Meesier object
tk.Label(root,
         text="Which Messier object you want to hop?",
         font="Times 12",
         fg="black",
         bg="white").grid(row=2, sticky="W")

user_input_name = tk.Entry(root)
user_input_name.grid(row=2, column=1, sticky="W")

tk.Label(root,
         text="Lets enter some telescope details!",
         font="Times 12",
         fg="black",
         bg="white").grid(row=3, sticky="W")

tk.Label(root,
         text="Aperture of the telescope (in mm):",
         font="Times 12",
         fg="black",
         bg="white",
         ).grid(row=3, column=1, sticky="W")
user_input_aperture = tk.Entry(root)
user_input_aperture.grid(row=3, column=2, sticky="W")

telescope_msg = tk.Label(root,
                         text="Choose the telescope view: ",
                         font="Times 12",
                         fg="black",
                         bg="white",).grid(row=3, column=3, sticky="W")

radio_button_variable = IntVar()

tk.Radiobutton(root,
               text="Through eyepiece",
               font="Times 12",
               fg="black",
               bg="white",
               variable=radio_button_variable,
               value=0).grid(row=3, column=4, sticky="W")

tk.Radiobutton(root,
               text="Through finder scope",
               font="Times 12",
               fg="black",
               bg="white",
               variable=radio_button_variable,
               value=1).grid(row=3, column=5, sticky="W")

print(radio_button_variable)

tk.Label(root,
         text="Enter apparent field of view (in deg):",
         font="Times 12",
         fg="black",
         bg="white",
         ).grid(row=5, column=0, sticky="W")
user_input_apparent_fov = tk.Entry(root)
user_input_apparent_fov.grid(row=5, column=1, sticky="W")

tk.Label(root,
         text="Magnification of telescope:",
         font="Times 12",
         fg="black",
         bg="white",
         ).grid(row=5, column=2, sticky="W")
user_input_mag = tk.Entry(root)
user_input_mag.grid(row=5, column=3, sticky="W")

tk.Label(root,
         text="OR",
         font="Times 12",
         fg="red",
         bg="white",
         ).grid(row=5, column=3, sticky="E")

tk.Label(root,
         text="Enter true field of view (in deg):",
         font="Times 12",
         fg="black",
         bg="white",
         ).grid(row=5, column=4, sticky="W")
user_input_true_fov = tk.Entry(root)
user_input_true_fov.grid(row=5, column=5, sticky="W")

submit = tk.Button(root, text="Submit",
                   font="Times 10",
                   command=get_input_values,
                   fg="green",
                   bg="white",).grid(row=6, column=2, pady="5px")

msg = tk.Label(root,
               text="Choose the type of plot interaction: ",
               font="Times 12",
               fg="black",
               bg="white").grid(row=7, sticky="W")

interactive_button = tk.Button(root,
                               text="Interactive",
                               font="Times 10",
                               command=next_prev,
                               fg="blue",
                               bg="white",
                               borderwidth=2).grid(row=7, column=1, sticky="W")

static_button = tk.Button(root,
                          text="Static",
                          font="Times 10",
                          command=lambda: hop_sequence_plot(Lon, Lat, 0),
                          fg="blue",
                          bg="white",).grid(row=7, column=2, sticky="W")

telescope_button = tk.Button(root,
                             text="Telescope view",
                             font="Times 10",
                             command=lambda: telescope(
                                 fov, radio_button_variable.get()),
                             fg="orange",
                             bg="white",).grid(row=7, column=3, sticky="W")


w = Canvas(root, width=2000, height=1000, highlightthickness=5)
w.grid(row=10, rowspan=12, columnspan=25, sticky="NSEW", pady="2px")

# fov_finder_scope_button = tk.Button(root,
#                    text = "Field of view from Finder scope",
#                    font = "Times 11",
#                    command = lambda: telescope(fov_finder_scope,2)).grid(row = 12, column = 2)


# tk.Label(root,
#         text = "Enter the 'fov' value of finder scope: ",
#         font = "Times 12"   ).grid(row = 4, column = 2)
# user_input_fov_finder_scope = tk.Entry(root)
# user_input_fov_finder_scope.grid(row = 4, column = 3)


# tk.Label(root,
#         text = "Aperture of the telescope (in mm):",
#         font = "Times 12"   ).grid(row = 6)
# user_input_aperture = tk.Entry(root)
# user_input_aperture.grid(row = 6, column = 1)

root.mainloop()
