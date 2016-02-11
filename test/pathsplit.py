# coding: UTF-8

import sys

argvs = sys.argv
path = argvs[1]

#print path

output = '/'

for i in path.split('/'):
    if i:
        output += i
    if i=='python':
        break
    if i:
        output += '/'

print output
