import os
from pprint import pprint

output = {}

def main():
	""" Initialize the user inputs.


	Implementation:

	1. Get user inputs for target directory and target word
	
	Please remember that directory names and target words are case sensitive.

	Example: '/Users/gyang/Documents'

	2. Call searchTarget, a search function that recursively looks through a target folder and its subdirectories.

	3. Print the output in the form of a dictionary 
	"""

	print("Please remember to provide case sensitive answers:")
	

	while True:
		try:
			root_dir = input('What is your root dir? ')
			os.chdir(root_dir)
			break
		except:
			print("Please provide a proper root directory in the form of: '/Users/gyang/Documents'")
	keyword = input('What is your target keyword? ')

	searchTarget(root_dir, keyword)

	pprint(output)


def searchTarget(root_dir, keyword):
	""" Search for a keyword through a directory and recursively visit its subdirectories


	Implementation:

	1. I settled on using a queue to keep track of unvisited folders and to visit them in alphabetical order.

	2. For every file in our current directory:
		a ) If the file contains our keyword, add a count to our dictionary
		b ) If the file is a folder, add it to folderQueue so that we can recursively visit this folder later

	3. For every unvisited folder in folderQueue:
		Pop the folder off that queue and recursively call searchTarget on that folder.


	"""

	# 1.
	os.chdir(root_dir)
	output[root_dir] = 0
	folderQueue = []

	# 2.
	for file in os.listdir('.'):
		if keyword in file:
			output[root_dir] += 1
		if os.path.isdir(file):
			folderQueue += [file]

	# 3.
	while folderQueue:
		nextDir = root_dir + "/" + folderQueue.pop(0) 
		searchTarget(nextDir, keyword)

main()
