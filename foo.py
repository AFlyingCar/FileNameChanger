import os
import platform as plat
if str(plat.system()) == "Windows":
	slash = "\\"
else:
	slash = "//"
loc = os.getcwd()
fileli = []
filec = {}
num = -1
work = True
filenum = 0;
for root, dirs, files in os.walk(loc):
	for file in files:
		foo = file
		if loc + slash + ".git" in root:
			continue
		elif foo == "foo.py":
			continue
		elif foo[:3] == "foo":
			continue
		else:
			print "File " + root + slash + foo
			work = True
			try:
				num += 1
				ext = foo.split(".")[1]
				filename = root + slash + "foo" + str(num) + "." + str(ext)
				orig = root + slash + foo
				os.rename(orig, filename)
				work = False
				filenum += 1
				fileli.append(foo)
				filec[foo] = "foo" + str(num) + "." + str(ext)
			except Exception:
				num += 1
				print "> " + str(num)
				print "> File " + root + slash + foo + ' exists.'
print "\n" + str(filenum) + " files were changed."
print "Files: "
for item in fileli:
	print "\t" + item + " -->",
	print filec[item]
