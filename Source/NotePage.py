'''
NotePage.py
Copyright (C) 2015 - Bill Williams

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
'''

try:
	from Tkinter import *
except ImportError:
	from tkinter import *

from tkColorChooser import askcolor

import 	tkMessageBox
import 	ttk
from 	ttk import *
import 	tkFont

# Base CLass for all NotePad pages.
class BasicNotepage ( Frame ):
	def __init__(self, parent, camera ):
		Frame.__init__(self, parent,padding=(10,10,10,10))
		self.grid(sticky='NSEW')
		self.columnconfigure(0,weight=1)
		self.camera = camera
		self.BuildPage()
	def BuildPage ( self ): 		# Overide this!
		Label(self,text='UNDER CONSTRUCTION',font=('Arial',14,('bold')),
			anchor='center').grid(row=0,column=0,sticky='EW')
	def Reset ( self ):	pass # Override this if needed

