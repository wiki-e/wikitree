'''
========


Aim of this file is to understand the input query,
take steps for fetching and computing and output.
1. Find the tokens and tag parts of speech
2. Type of query: 
3. wt_finder for each token as a separate process and store wiki_data in temp
4. ...


========
'''

import sys
import nltk

arguments = sys.argv

__TYPE__DEFAULT = 0x111
__TYPE__Q_ATTR = 0x112
__TYPE__Q_PLACE = 0x113


if(len(arguments) > 1):
	# not including the file name
	# query = (" ").join(arguments[1:])
	str = ""
	for s in arguments[1:]:
		str+=" "+(s)
	query = nltk.word_tokenize(str)
	pos_tagged_query = nltk.pos_tag(query)
	print(pos_tagged_query)
	type = getType(pos_tagged_query)
	if(type == __TYPE__DEFAULT ):

	else if (type == __TYPE__Q_ATTR):
		# get question attribute	
	else if (type == __TYPE__Q_PLACE):


def getType(pos_tagged_query)
	type = __TYPE__DEFAULT
	
	#here comes type sorting 

	return type