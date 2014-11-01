'''
========

Aim of this file is to stay in loop and keep asking for queries,
the answers will be of the form "Answer for query so and so is : " + Answer 
The user will not wait for each answer, he is free to type next queries
and the queries will be answered as they are finised processing.

========
'''

import subprocess
import os
import threading

def invoke_on_query(query):
	print (query)
	if(os.name == "nt"):		
		p = subprocess.Popen("python wt_init_parse.py " +query, shell=True, stdout=subprocess.PIPE)
		out, err = p.communicate()
	else:
		p = subprocess.Popen("python3.4 wt_init_parse.py "+query,shell=True, stdout=subprocess.PIPE)
		out, err = p.communicate()
	p.wait()
	print_answer(out, query)
	
def print_answer(answer, query):
	print("\n.: we conclude for query \""+str(query)+'"  ->  ' + str(answer))

def main():
	print("\n.: ",end="")
	while(1):
		query = input()
		t = threading.Thread(target = invoke_on_query, args = [query])
		t.daemon = True
		t.start()
		print("\n.: ",end="")
		
		
	

if(__name__ == "__main__"):
	main()