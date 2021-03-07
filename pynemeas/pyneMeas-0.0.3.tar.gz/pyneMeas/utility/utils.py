# -*- coding: utf-8 -*-
"""
VERSION 4.0
@author: Jakob Seidl
jakob.seidl@nanoelectronics.physics.unsw.edu.au
"""

import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askdirectory

import json
import numpy as np
import matplotlib


def array(start,target,stepsize,upDown = False):
    
    sign = 1 if (target>start) else -1
    sweepArray = np.arange(start,target+sign*stepsize,sign*stepsize)
    if upDown:
        sweepArrayBack = np.arange(target,start+-sign*stepsize,-sign*stepsize)
        sweepArray = np.concatenate((sweepArray,sweepArrayBack))
    return sweepArray

def targetArray(targetList,stepsize):
    arrayList = []
    stepsize = float(stepsize)
    for index, item in enumerate(targetList):

        if index == 0:
             pass
        elif index == 1:
            arrayList.append(array(targetList[index - 1], targetList[index], stepsize))
        elif (index > 1):
            arrayList.append(array(targetList[index-1],targetList[index],stepsize)[1:]) #in order to avoid doublicating numbers
    return np.concatenate((arrayList))

def fileDialog(initAd = "/"):
    root = tk.Tk()
    #root.lift()
    root.attributes('-topmost','true')   
    root.withdraw()
    fullPath = asksaveasfilename(initialdir = initAd)
    a = ''.join(fullPath).rfind("/")
    basePath = fullPath[0:a+1]
    fileName = fullPath[a+1:]
    return [basePath,fileName]

def runTest():
    import pyneMeas.Instruments as I
    import pyneMeas.utility as U
    T = I.TimeMeas()
    Noi = I.LinearNoiseGenerator()
    NoiSin = I.SineNoiseGenerator()

    Dct = {}
    Dct['basePath'] = "TempDat/"
    Dct['fileName'] = 'fileName'

    Dct['setters'] = {T: 'dummy'}

    Dct['readers'] = {T: 'time',
                      Noi: 'lin_noise',
                      NoiSin: 'sine_noise',
                      }

    Dct['sweepArray'] = range(100)
    df = U.sweep(
        Dct,
        delay=0.0,
        plotVars=[('time', 'lin_noise'),
                  ('time', 'sine_noise')
                  ],
        plotParams=[('o-', 'linear-linear')
            , ('go-', 'linear-linear')
                    ],
        saveCounter=100,
    )


def sendEmail(targetAddress, measurementName):
    """
    Sends and email from our group's shared account. Users that are not in our group will find these credentials empty. They need to be populated before the email can be sent.

    """
    import smtplib
    sent_from = 'enterEmail'
    password = 'enter Password'
    subject = 'Measurement finished'
    body = 'Eureka, your measurement >>>' + measurementName + '<<< has just finished!'
    email_text = """\  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, targetAddress, subject, body)
    mail = smtplib.SMTP('smtp.gmail.com:587')  # or 587
    mail.ehlo()
    mail.starttls()
    mail.login(sent_from, password)
    mail.sendmail(sent_from, targetAddress, email_text)
    print('Email sent to: ' + targetAddress)
    mail.close()