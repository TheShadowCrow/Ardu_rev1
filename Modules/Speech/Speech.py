import subprocess 
if __name__ == "__main__":
	rec = subprocess.Popen("speech2text.sh", stdout=subprocess.PIPE)
	command = rec.stdout.readline()
	print command
