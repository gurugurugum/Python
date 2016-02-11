# coding: UTF-8

import sys

argvs = sys.argv
path = argvs[1]

#print path

output = '/'
folderNames = path.split('/')
print folderNames

folderNames.reverse()
reversedFolderNames = folderNames[:len(folderNames)-1]
print reversedFolderNames

idx = len(reversedFolderNames)-1
for i in reversedFolderNames:
    if i[0:3] == 'cr7':
        break
    else:
        idx -= 1

print idx

#reversedFolderNames = ().reverse())[:len(path.split('/'))-1]
#idx = len(reversedFolderNames)-1

#print reversedFolderNames

#for i in reversedFolderNames:
#    if i[0:3] == 'cr7':
#        break
#    idx -= 1

#print idx
