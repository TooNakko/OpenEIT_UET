import serial
import time
import os


def WriteIntoSerialCom(port, content):
    serial_com = serial.Serial(port)
    serial_com.write(content.encode('utf-8'))

    

def ReadFromSerialCom(port, timeout_value):
    serial_com = serial.Serial(port,timeout=timeout_value)
    message = serial_com.readline().decode()

    return message

def NewFolder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def GetPathOfText(folder_name,text_file_name):
    
    for index in range (0,100):
        text_file_path = os.path.join(folder_name, text_file_name)
        if os.path.exists(text_file_path) == False:
            text_file_name = 'log_data_' + str(index) + '.txt'
            text_file_path = os.path.join(folder_name, text_file_name)
            break
        else:
            text_file_name = 'log_data_' + str(index+1) + '.txt'
            continue
    return text_file_path
    