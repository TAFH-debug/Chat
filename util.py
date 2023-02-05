from tkinter import *


def inherit_bg(self):
    self['bg'] = self.master['bg']
    return self

Widget.inherit_bg = inherit_bg
