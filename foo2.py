import os

loc = os.getcwd()
fileli = []
num = -1
work = True

for root, dirs, files in os.walk(loc):
	for file in files:
		foo = file
		if loc + "\\.git" in root:
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
				filename = "foo" + str(num) + "." + str(ext)
				os.rename(root + "\\" + foo, root + "\\" + filename)
				work = False
			except Exception:
				print num
				print file + ': exists'