"""
author: Adam Micolich
Updated by Jakob Seidl

This module does the output handling for the USB-6216, which is effectively a pair of analog outputs
and a set of 8 analog inputs. The input handling is done by a separate .py. There is a settable option for 
where the voltage feedback comes from. The default feedback is internal, i.e., USB-6216 reads back what it
is putting out via an internal connection. The alternative is to T- off to a spare input (e.g., ai7) and 
direct read. 
"""

import pyneMeas.Instruments.Instrument as Instrument
import nidaqmx as nmx
import time
import numpy as np

@Instrument.enableOptions
class USB6216Out(Instrument.Instrument):
    # Default options to set/get when the instrument is passed into the sweeper
    defaultInput = "outputLevel"
    defaultOutput = "outputLevel"
    defaultFeedBack = "Int"

    def __init__(self, address,usbPort = 'Dev1'):
        super(USB6216Out, self).__init__()
        self.dev = address
        self.type ="USB6216"  #We can check each instrument for its type and react accordingly
        self.name = "myUSB6216"
        self.usbPort = usbPort
        if self.dev in [0, 1]:
            self.port = f"{self.usbPort}/ao{self.dev}"
            
        else:
            raise ValueError(
                f'Please insert a valid Input port for the NIDaQ ranging from 0 to 1. You entered {self.dev}')

    @Instrument.addOptionSetter("name")
    def _setName(self,instrumentName):
         self.name = instrumentName
         
    @Instrument.addOptionGetter("name")
    def _getName(self):
        return self.name

    @Instrument.addOptionSetter("outputLevel")
    def _setOutputLevel(self,outputLevel):
        if (10.0 >= outputLevel and outputLevel >= -10.0):
            self.output = outputLevel
            with nmx.Task() as task:
                task.ao_channels.add_ao_voltage_chan(self.port)
                task.write(outputLevel)
        else:
            raise ValueError("Output outside 10V range available".format(outputLevel))
                
    @Instrument.addOptionGetter("outputLevel")
    def _getOutputLevel(self):
        with nmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(self.fbp)
            outputLevel = task.read()
        return outputLevel
        
    @Instrument.addOptionGetter("feedBack")
    def _getScaleFactor(self):
        return self.feedBack

    @Instrument.addOptionSetter("feedBack")
    def _setFeedBack(self,feedBack):
        self.feedBack = feedBack
        
    @Instrument.addOptionGetter("extPort")
    def _getExtPort(self):
        return self.fbp
    
    @Instrument.addOptionSetter("extPort")
    def _setExtPort(self,extPort):
        self.extPort = extPort
        if self.feedBack == "Int":
            if self.dev == 0:
                self.fbp = f"{self.usbPort}/_ao0_vs_aognd"
            elif self.dev == 1:
                self.fbp = f"{self.usbPort}/_ao1_vs_aognd"
        elif self.feedBack == "Ext":
            if self.extPort == 0:
                self.fbp = f"{self.usbPort}/ai0"
            elif self.extPort == 1:
                self.fbp = f"{self.usbPort}/ai1"
            elif self.extPort == 2:
                self.fbp = f"{self.usbPort}/ai2"
            elif self.extPort == 3:
                self.fbp = f"{self.usbPort}/ai3"
            elif self.extPort == 4:
                self.fbp = f"{self.usbPort}/ai4"
            elif self.extPort == 5:
                self.fbp = f"{self.usbPort}/ai5"
            elif self.extPort == 6:
                self.fbp = f"{self.usbPort}/ai6"
            elif self.extPort == 7:
                self.fbp = f"{self.usbPort}/ai7"

    @Instrument.addOptionGetter("scaleFactor")
    def _getScaleFactor(self):
        return self.scaleFactor
    
    @Instrument.addOptionSetter("scaleFactor")
    def _setScaleFactor(self,scaleFactor):
        self.scaleFactor = scaleFactor
            
    def goTo(self,target,stepsize = 0.01,delay = 0.001): # Modified from usual as APM likes linspace better
        currentOutput = self.get("outputLevel")
        count = int(abs(target-currentOutput)/stepsize) + 1
        sweepArray = np.linspace(currentOutput,target,count,endpoint=True)
        if count < 3: #Option to avoid pointless sweeps, if you're close enough, just go direct
            with nmx.Task() as task:
                task.ao_channels.add_ao_voltage_chan(self.port)
                task.write(target)
        else:
            for point in sweepArray:
                with nmx.Task() as task:
                    task.ao_channels.add_ao_voltage_chan(self.port)
                    task.write(point)
                time.sleep(delay)
            with nmx.Task() as task:
                task.ao_channels.add_ao_voltage_chan(self.port)
                task.write(target)
            
    def close(self):
        pass