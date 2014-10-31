import subprocess
import os

def main():
	if(os.name == "nt"):
		p = subprocess.Popen("python wt_finder.py",shell=True)
	else:
		p = subprocess.Popen("python34 wt_finder.py",shell=True)
	p.wait()


if(__name__ == "__main__"):
	main()