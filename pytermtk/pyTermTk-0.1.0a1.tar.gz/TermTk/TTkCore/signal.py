
#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2021 Eugenio Parodi <ceccopierangiolieugenio AT googlemail DOT com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''
ref: http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html
     https://github.com/ceccopierangiolieugenio/pyCuT/blob/master/cupy/CuTCore/CuSignal.py
'''

# dummy decorator
def pyTTkSlot(*args, **kwargs):
    def pyTTkSlot_d(func):
        # Add signature attributes to the function
        func._TTkslot_attr = args
        return func
    return pyTTkSlot_d

def pyTTkSignal(*args, **kwargs):
    return pyTTkSignal_obj(*args, **kwargs)

class pyTTkSignal_obj():
    '''
        ref: http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html#PyQt5.QtCore.pyqtSignal

        PyQt5.QtCore.pyqtSignal(types[, name[, revision=0[, arguments=[]]]])
            Create one or more overloaded unbound signals as a class attribute.

            Parameters:
            types - the types that define the C++ signature of the signal. Each type may be a Python type object or a string that is the name of a C++ type. Alternatively each may be a sequence of type arguments. In this case each sequence defines the signature of a different signal overload. The first overload will be the default.
            name - the name of the signal. If it is omitted then the name of the class attribute is used. This may only be given as a keyword argument.
            revision - the revision of the signal that is exported to QML. This may only be given as a keyword argument.
            arguments - the sequence of the names of the signal's arguments that is exported to QML. This may only be given as a keyword argument.
            Return type:
                an unbound signal
    '''
    __slots__ = ('_types', '_name', '_revision', '_connected_slots')
    def __init__(self, *args, **kwargs):
        self._types = args
        self._name = kwargs.get('name', None)
        self._revision = kwargs.get('revision', 0)
        self._connected_slots = []

    '''
        ref: http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html#connect

        connect(slot[, type=PyQt5.QtCore.Qt.AutoConnection[, no_receiver_check=False]]) -> PyQt5.QtCore.QMetaObject.Connection
            Connect a signal to a slot. An exception will be raised if the connection failed.

            Parameters:
            slot - the slot to connect to, either a Python callable or another bound signal.
            type - the type of the connection to make.
            no_receiver_check - suppress the check that the underlying C++ receiver instance still exists and deliver the signal anyway.
            Returns:
                a Connection object which can be passed to disconnect(). This is the only way to disconnect a connection to a lambda function.
    '''
    def connect(self, slot):
        if hasattr(slot, '_TTkslot_attr') and slot._TTkslot_attr != self._types:
            error = "Decorated slot has no signature compatible: "+slot.__name__+str(slot._TTkslot_attr)+" != signal"+str(self._types)
            raise TypeError(error)
        if slot not in self._connected_slots:
            self._connected_slots.append(slot)

    def disconnect(self, *args, **kwargs):
        for slot in args:
            self._connected_slots.remove(slot)

    def emit(self, *args, **kwargs):
        if len(args) != len(self._types):
            error = "func"+str(self._types)+" signal has "+str(len(self._types))+" argument(s) but "+str(len(args))+" provided"
            raise TypeError(error)
        for slot in self._connected_slots:
            slot(*args, **kwargs)
