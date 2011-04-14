#!/usr/bin/env python
#-*- coding: utf-8 -*-
def LineCount(S):
	
	try:
		lines = (open(S,"r").readlines())
		return len(lines)
	except: 
		return -1

def main(args):
	files = ["file1.txt", "file2.txt", "file3.txt"]
	count = 0;
	for i in range(3):
		if (LineCount(files[i]) != -1):
			count += LineCount(files[i])
		else:
			print "ERROR (no such file: " + files[i] + ")"	
			exit(0)
	print count

if __name__ == '__main__':
    import sys
    main(sys.argv[:])

