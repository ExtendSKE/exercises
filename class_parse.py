#To count the number of classes present in java file. It excludes the commented out code

import re

fo=open("sample.java","r")
found_class=0
flag=0
for line in fo:
    if re.search('^#',line):
        continue
    if re.search('/\*',line):
        flag=1     
        continue
    if flag:
        if re.search('\*/',line):
            flag=0  
        else:
            continue
    if re.search('class|Class',line):
        found_class=found_class+1

  
print(found_class)
