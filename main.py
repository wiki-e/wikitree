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


def main():
	print("\n.: ",end="")
	query = input()
	if(os.name == "nt"):		
		p = subprocess.Popen("python wt_init_parse.py " +query, shell=True)
	else:
		p = subprocess.Popen("python3.4 wt_init_parse.py "+query,shell=True)
	p.wait()

if(__name__ == "__main__"):
	main()