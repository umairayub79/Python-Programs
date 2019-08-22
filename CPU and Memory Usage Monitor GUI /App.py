import PySimpleGUI as sg
import psutil

layout = [ [sg.Text('', size=(20,1), font='Helvetica 14', justification='center', key='_textCPU_')],
           [sg.Text('', size=(20,1), font='Helvetica 14', justification='center', key='_textMemory_')]]

window = sg.Window('CPU and Memory Meter').Layout(layout)

while True:
    button, values = window.Read(timeout=0, timeout_key='key')

    if button == 'Exit' or values is None:
        break

    cpu_percent = psutil.cpu_percent(interval=1)
    memoryUsed = psutil.virtual_memory().used
    memoryTotal = psutil.virtual_memory().total
    totaldMemoryInMBs = int (memoryTotal / 1048576)    
    usedMemoryInMBs = int (memoryUsed / 1048576)


    window.FindElement('_textCPU_').Update(f'CPU {cpu_percent:02.0f}%')
    window.FindElement('_textMemory_').Update(f'Memory {usedMemoryInMBs:02.0f}/{totaldMemoryInMBs}MB')

    
