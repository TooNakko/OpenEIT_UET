import serial
import serial
import Read_and_Write as RaW
import time
import random
import os

i = 0
while i<1000:
    message = round(float(random.random() * 10),5)
    RaW.WriteIntoSerialCom('COM2', str(message)+'\n')
    #print("Value {0} is written\n".format(message))
    time.sleep(0.05)                                    #Adjust this base on your device's spec so it's sync as much as possible
    i = i+1
print("Stop writing into COM!")

