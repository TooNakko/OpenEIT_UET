"""

# Copyright (c) Mindseye Biomedical LLC. All rights reserved.
# Distributed under the (new) CC BY-NC-SA 4.0 License. See LICENSE.txt for more info.

	Read in a data file and plot it using an algorithm. 

"""
from __future__ import division, absolute_import, print_function
import numpy as np
import serial
import matplotlib.pyplot as plt
from chart_studio import plotly
import OpenEIT.reconstruction 
import time
import random
from datetime import datetime

def convert_data_in(s):
    data=s
    items=[]
    for item in data.split(' '):
        item = item.strip()
        if not item:
            continue
        try:
            items.append(float(item))
        except ValueError:
            print("\nValue error: {0} {1}, none returned!".format(items, type(items)))
            return None
    return np.array(items)
time_start_0 = float(time.time() % (24 * 3600))

reference_image_array  = ''
difference_image_array = ''
n_el = 16
NewFrameSearchFlag = 1
#arduino = serial.Serial('COM8', 115200,timeout=5)

while True:
    #while arduino.inWaiting()==0:
    #    print("waiting")
    #    pass
    #time_start_1 = float(time.time() % (24 * 3600))
    
    ## Read reference image f0:
    #for i in range (0, n_el):
    #    data = arduino.readline().decode('ascii')
    #    data=data.strip('\r\n')
    #    reference_image_array += data
    #    reference_image_array += ' '
    #    print("string: {0}".format(data))
    ##data=str(data,'utf-8')
    #print('\n===')
    ## Read difference image f1:
    #for i in range (0, n_el): 
    #    data = arduino.readline().decode('ascii')
    #    #skip until the empty line is found to catch the whole frame
    #    while(NewFrameSearchFlag == 1):
    #        if len(data) > 4:
    #            print("Seeking for new frame")
    #            data = arduino.readline().decode('ascii')
#
    #            continue
    #        else:
    #            print("New frame found!")
    #            data = arduino.readline().decode('ascii')
    #            NewFrameSearchFlag = 0
    #            break
    #            time.sleep(0.5)
    #    # Check if receiving enough data to avoid miss-matching
    #    #if len(data) < 68:
    #    #    data = arduino.readline().decode('ascii')
    #    data=data.strip('\r\n')
    #    difference_image_array += data
    #    difference_image_array += ' '
    #    print("string: {0}".format(data))
#
# Th#is is the baseline image.  
    text_file = open("UET_data/ref_data.txt", "r")
    lines = text_file.readlines()
    f0 = convert_data_in(lines[0]).tolist()

    #f0          = convert_data_in(lines[0]).tolist()  # input REF
    #f0          = convert_data_in(reference_image_array).tolist()

    #f1          = convert_data_in(lines[1]).tolist()
    text_file_2 = open("UET_data/diff_left_data.txt", "r")
    lines_2 = text_file_2.readlines()
    #f1          = convert_data_in(difference_image_array).tolist() 
    f1          = convert_data_in(lines_2[0]).tolist() 
    
    print("\nf0:\n")
    print(f0)
    print('\n')

    print("f1:\n")
    print(f1)

    """ Select one of the three methods of EIT tomographic reconstruction, Gauss-Newton(Jacobian), GREIT, or Back Projection(BP)"""
# This is the Gauss Newton Method for tomographic reconstruction. 
    print("\njac rescontructing\n")
    #g = OpenEIT.reconstruction.JacReconstruction(n_el=n_el)
    print("finished reconstructing")
# Note: Greit method uses a different mesh, so the plot code will be different.
# g = OpenEIT.reconstruction.GreitReconstruction(n_el=n_el)
# 
    g = OpenEIT.reconstruction.BpReconstruction(n_el=n_el)

    data_baseline = f0
    print ('f0',len(f0),len(f1))

    g.update_reference(data_baseline)

# set the baseline. 
    baseline = g.eit_reconstruction(f0)
    print("\n===========baseline==============\n")
    print (baseline)
    print('\n')
    print(len(baseline))
    print("\n============================\n")

# do the reconstruction. 
    difference_image = g.eit_reconstruction(f1)
    print("\n==========difference image=========\n")
    print(difference_image)
    print('\n')
    print (len(difference_image))
    print("\n============================\n")

    print(g)


    mesh_obj = g.mesh_obj
    el_pos = g.el_pos
    ex_mat = g.ex_mat
    pts     = g.mesh_obj['node']
    tri = g.mesh_obj['element']
    x   = pts[:, 0]
    y   = pts[:, 1]

    """ Uncomment the below code if you wish to plot the Jacobian(Gauss-Newton) or Back Projection output.
    Also, please look at the pyEIT documentation on how to optimize and tune the algorithms. 
    A little tuning goes a long way! """

    fig, ax = plt.subplots(figsize=(6, 4))
    im = ax.tripcolor(x,y, tri, difference_image,
                  shading='flat', cmap=plt.cm.gnuplot)
    ax.plot(x[el_pos], y[el_pos], 'ro')
    for i, e in enumerate(el_pos):
        ax.text(x[e], y[e], str(i+1), size=12)
    ax.axis('equal')
    fig.colorbar(im)
    break
time_end_0 = float(time.time() % (24 * 3600))
run_time_total = time_end_0 - time_start_0
print("\n\nTOTAL RUN TIME: {0}".format(run_time_total))
plt.show()


""" Uncomment the below code if you wish to plot the GREIT output. Also, please look at the pyEIT documentation on how to optimize and tune the algorithms. A little tuning goes a long way! """
# GREIT RECONSTRUCION IMAGE SHOW # 
#  new     = difference_image[np.logical_not(np.isnan(difference_image))]
# flat    = new.flatten()   
# av      = np.median(flat)
# total   = []
# for i in range(32):
#     for j in range(32):
#         if difference_image[i,j] < -5000: 
#             difference_image[i,j] = av

# print ('image shape: ',difference_image.shape)
# fig, ax = plt.subplots(figsize=(6, 4))
# #rotated = np.rot90(image, 1)
# im = ax.imshow(difference_image, interpolation='none', cmap=plt.cm.rainbow)
# fig.colorbar(im)
# ax.axis('equal')
# ax.set_title(r'$\Delta$ Conductivity Map of Lungs')
# fig.set_size_inches(6, 4)
# # fig.savefig('../figs/demo_greit.png', dpi=96)
# plt.show()


