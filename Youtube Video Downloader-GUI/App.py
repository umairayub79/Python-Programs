import PySimpleGUI as sg
import pafy
import os
import sys


def downloadVid(url, dest):
    video = pafy.new(url)
    best = video.getbest()
    best.download(quiet=False, filepath=dest)


layout = [  [sg.Image(r'/home/umair/Desktop/Python/Video Downloader/youtube.png')],
            [sg.Text('Enter Video Url', size=(20,1), justification='center'), sg.InputText(key='_url_')],
            [sg.Text('Enter File Destination', size=(20,1), justification='center'), sg.InputText(key='_dest_')],
            [sg.Text('', key='_downloading_', justification='center')],
            [sg.Button('Download Video'), sg.Exit()]]

window = sg.Window('Youtube Video Downloader', layout)



while True:
    button, values = window.Read(timeout=0, timeout_key='key')

    
    if button == 'Exit' or values is None:
        break
    if button == 'Download Video':
        url = window.FindElement('_url_').Get()
        dest = window.FindElement('_dest_').Get()
        if url != '' and dest != '':
            window.FindElement('_downloading_').Update('Downloading...')
            downloadVid(url,dest)
            
            
        



