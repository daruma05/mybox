import re

StringList = ["Abc_def","ghijkl","mnopq","rstu","vw_xyz","This-is-test","re_module","aabbccc"]

worker = re.compile("(?<=_)\w+")

for i in range(len(StringList)):
	m = worker.search(StringList[i])
	if m != None:
		print "Number %d in StringList matched" % i