class searchObject(object):
	"""searchObject helps encapsulate data so we only worry about working
	with a single object rather than passing around multiple args"""
	def __init__ (self, searchString, replaceString, fileName):
		super(searchObject, self).__init__()
		self.searchString = searchString
		self.replaceString = replaceString
		self.fileName = fileName
		self.file = None

	def dump (self):
		print "searchString: " + self.searchString
		print "replaceString: " + self.replaceString
		print "fileName: " + self.fileName

	def open_file (self):
		self.file = open(self.fileName, 'r+')
		return self.file

	def close_file (self):
		self.file.close()

def find (searchObject):
	with searchObject.open_file() as f:
		count = 0
		for line in f:
			if searchObject.searchString in line:
				print "found @ line #", count, line
			count = count + 1 

def findReplaceInit ():
	searchReplace = searchObject ("thurgoodmarshal pword='kissmyass'", "thurgoodmarshal pword='HELLOWORLD'", "file.txt")
	# searchReplace.dump()

	searchReplace.open_file()

	find (searchReplace)

	searchReplace.close_file()

# allows for the program to be run either as a module plugin or as main
if __name__ == '__main__':
	import sys
	findReplaceInit()

