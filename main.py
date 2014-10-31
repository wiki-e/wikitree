import subprocess
import os

BASE_URL = "http://en.wikipedia.org/wiki/"
def main():
	print("\n.: ",end="")
	read = input()
	read = BASE_URL+read.replace(' ', '_')
	if(os.name == "nt"):
		p = subprocess.Popen("python wt_finder.py " +read,shell=True)
	else:
		p = subprocess.Popen("python34 wt_finder.py "+read,shell=True)
	p.wait()

if(__name__ == "__main__"):
	main()