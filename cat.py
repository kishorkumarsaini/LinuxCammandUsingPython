#!/usr/bin/python3
import sys

files=sys.argv[1:3]

#Source file

src_file=files[0]
f1=open(src_file)
src_data=f1.read()
print(src_data)
f1.seek(0,0)
f1.close()

