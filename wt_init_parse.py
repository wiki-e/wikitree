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

__QTYPE__DEFAULT = 0x111
__QTYPE__ATTR = 0x112

def getType(tagged):
	qtype = __QTYPE__DEFAULT
	#here comes type sorting 
	return qtype


if(len(arguments) > 1):
	# not including the file name
	# query = (" ").join(arguments[1:])
	str = ""
	for s in arguments[1:]:
		str+=" "+(s)
	query = nltk.word_tokenize(str)
	pos_tagged_query = nltk.pos_tag(query)
	print(pos_tagged_query, end="")
	qtype = getType(pos_tagged_query)
	
	'''
	uncomment when you can finish the if statement

	if(qtype == __QTYPE__DEFAULT ):
		#adandladas
		print("default: ", end="")
	elif (qtype == __QTYPE__ATTR):
		# get question attribute	
		print("search for attribute", end="")
	'''