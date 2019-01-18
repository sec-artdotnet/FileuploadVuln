#!/usr/bin/python

import binascii
import sys

if len(sys.argv) != 2:
  print "Argument missing!"
  print "Usage : %s &lt;input_file&gt;" % sys.argv[0]
  sys.exit()

pngHeader = "89504e470d0a1a0a"
# use below header for jpg/jpeg files
jpgHeader = "FFD8FFE000104A464946000101"

fileName = sys.argv[1]
f1 = open(fileName, "rb")
dt1 = binascii.hexlify(f1.read())
dt2 = pngHeader + dt1
MainData = binascii.unhexlify(dt2)
newFile = fileName + ".png"
f2 = open(newFile, "wb")
f2.write(MainData)
f2.close()
print "File Successfully created : ", newFile
