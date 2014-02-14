import os
import platform as plat

if str(plat.system()) == "Windows":
	slash = "\\"
else:
	slash = "//"

loc = os.getcwd()
num = 0

print os.listdir(loc)

#for files, dirs, root in os.listdir(loc):
#	loc = os.getcwd()
#	print files
#	try:
#		print files.split(".")
#		ext = files.split(".")[0]
#		os.chdir(loc + files) #check if item is a 
#		print "here"
#	except Exception:
#		if files == "git":
#			continue

#		filename = "foo" + str(num) + "." + (ext)

#		if files[:3] != "foo":
#			print "foo " + files
		
#			try:
#				os.renames(files, filename)
#			except Exception:
#				pass
#		else:
#			num += 1

#for root, dirs, files in os.walk(loc):
for item in os.listdir(loc):
#	print dirs
#	print root
#	if dirs == ".git":
#		continue
	for file in item:
		files += file
	
	for file in files:
		foo = file
		if foo == ".git":
			continue
		else:

			ext = foo.split(".")[1]
			print ext

			filename = "foo" + str(num) + "." + str(ext)

			if foo[:3] != "foo":
				print "foo " + foo
				os.renames(foo, filename)
			else:
				num += 1

nuclear = u'\u2622'

Note = """>>> os.listdir(loc)
['foo.txt', 'foo2.txt']
>>> for files in os.listdir(loc):
	print files

	
foo.txt
foo2.txt
>>> for files in os.listdir(loc):
	print files
	if files != "foo2.txt":
		os.rename(files, "foo3.txt")

		
foo.txt
foo2.txt
>>> print files
foo2.txt
>>> for files in os.listdir(loc):
	print files
	if files != "foo2.txt":
		os.rename(files, "foo3.txt")"""