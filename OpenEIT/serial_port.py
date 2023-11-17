import serial
import time
import array as arr
import numpy as np



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



arduino = serial.Serial('COM4', 9600,timeout=1)



while True:
    while arduino.inWaiting()==0:
        pass
    data = arduino.readline().decode('ascii')
    #data=str(data,'utf-8')
    #data=data.strip('\r\n')
    #for i in range(0,len(data)):
    a=convert_data_in(data)
    print("mang string la ",a)




