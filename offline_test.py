"""

# Copyright (c) Mindseye Biomedical LLC. All rights reserved.
# Distributed under the (new) CC BY-NC-SA 4.0 License. See LICENSE.txt for more info.

	Read in a data file and plot it using an algorithm. 

"""

from __future__ import division, absolute_import, print_function
import numpy as np
import array as arr
import matplotlib.pyplot as plt
#from chart_studio import plotly
import OpenEIT.reconstruction 
import cv2
import argparse
import os
import serial
from tkinter import *
from tkinter import messagebox
def convert_data_in(s):
    data=s
    items=[]
    for item in data.split():
        item = item.strip()
        if not item:
            continue
        try:
            items.append(float(item))
        except ValueError:
            return None
    return np.array(items)

n_el = 16



file_data=open("tron.txt","r")
file_ref =open("ref_2.txt","r")

datas=file_data.readlines()
refs=file_ref.readlines()


#loop for print and  reconstruct data

for i in range(0,1):
        f1= convert_data_in(refs[0])
        g = OpenEIT.reconstruction.JacReconstruction(n_el=n_el)
        #data_baseline = convert_data_in(datas[i])
        data_baseline = convert_data_in(datas[i])
        #print ('size',len(data_baseline),len(f1))
        g.update_reference(data_baseline) 
        #baseline = g.eit_reconstruction(convert_data_in(datas[i]))
        baseline = g.eit_reconstruction(convert_data_in(datas[i]))
        difference_image = g.eit_reconstruction(f1)
        print (len(difference_image))
        print(len(baseline))
        mesh_obj = g.mesh_obj
        #print(mesh_obj)
        el_pos = g.el_pos
        ex_mat = g.ex_mat
        pts     = g.mesh_obj['node']
        tri = g.mesh_obj['element']
        #print(tri)
        x   = pts[:, 0]
        y   = pts[:, 1]
        # JAC OR BP RECONSTRUCTION SHOW # 
        fig, ax = plt.subplots(figsize=(11.76, 8.1))
        ax.plot(x[el_pos], y[el_pos], 'ro')
        ax.axis('equal')
        ax.set_title("graph")
        im = ax.tripcolor(x,y, tri, -difference_image,
                            shading='flat', cmap=plt.cm.gnuplot)


        for f, e in enumerate(el_pos):
                ax.text(x[e], y[e], str(f+1), size=12)


        fig.colorbar(im)
        fig.savefig(fname=str(i)+".png")
#plt.show()



