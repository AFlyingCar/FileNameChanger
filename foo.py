import os
import platform as plat
if str(plat.system()) == "Windows":
	slash = "\\"
else:
	slash = "//"
loc = os.getcwd()
fileli = []
num = -1
work = True
for root, dirs, files in os.walk(loc):
	for file in files:
		foo = file
		if loc + slash + ".git" in root:
			continue
		elif foo == "foo.py":
			continue
		elif foo[:3] == "foo":
			continue
		print dirs
		print foo
		print root
		work = True
		while work:
			try:
				num += 1
				ext = foo.split(".")[1]
				filename = root + slash + "foo" + str(num) + "." + str(ext)
				orig = root + slash + foo
				os.rename(orig, filename)
				work = False
			except Exception:
				print num
				print file + ': exists'