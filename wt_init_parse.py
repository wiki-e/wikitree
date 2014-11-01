'''
========

Aim of this file is to find the keywords and invoke 
wt_finder for each keyword as a separate process 
if 
	the length of keywords is below a certain limit
else
	send it to a different file? not sure
========
'''

import sys
import nltk

arguments = sys.argv

if(len(arguments) > 1):
	# not including the file name
	query = (" ").join(arguments[1:])
	
