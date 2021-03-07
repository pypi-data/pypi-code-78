#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2019-11-05

@author: immoroz
'''

base = [
    ["щойно", "через мить"],
    ["%s секунду тому", "через %s секунду", "%s секунди тому", "через %s секунди", "%s секунд тому", "через %s секунд"],
    ["хвилину тому", "через хвилину"],
    ["%s хвилину тому", "через %s хвилину", "%s хвилини тому", "через %s хвилини", "%s хвилин тому", "через %s минут"],
    ["годину тому", "через годину"],
    ["%s годину тому", "через %s годину", "%s години тому", "через %s години", "%s годин тому", "через %s годин"],
    ["вчора", "завтра"],
    ["%s день тому", "через %s день", "%s дні тому", "через %s дні", "%s днів тому", "через %s днів"],
    ["тиждень тому", "через тиждень"],
    ["%s тиждень тому", "через %s тиждень", "%s тиждні тому", "через %s тиждні", "%s тижднів тому", "через %s тижднів"],
    ["місяць тому", "через місяць"],
    ["%s місяць тому", "через %s місяць", "%s місяці тому", "через %s місяці", "%s місяців тому", "через %s місяців"],
    ["рік тому", "через рік"],
    ["%s рік тому", "через %s рік", "%s роки тому", "через %s роки", "%s років тому", "через %s років"],
]


def generate(row, y):
    def formatting(time):
        if row % 2 == 0:
            return base[row][y]
        if time > 20: # for 21,32,43 but not for 11, 12, 13
            time = time % 10
        if time == 1:
            return base[row][y]
        elif time in (2, 3, 4):
            return base[row][y + 2]
        else:
            return base[row][y + 4]
    return formatting


LOCALE = generate
