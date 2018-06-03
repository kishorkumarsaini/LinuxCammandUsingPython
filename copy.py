#!/usr/bin/python3
import sys

files=sys.argv[1:3]
print(files)

print("*************************************************")
#Extracting the source file

src_file=files[0]
#Extracting the destination file
dest_file=files[1]

#open the source file
f1=open(src_file)
src_data=f1.read()
f1.close()
#creating the destinataion file
f2=open(dest_file,'w')
f2.write(src_data)
f2.close()
