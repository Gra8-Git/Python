
import time
import stat
import os
currenttime =time.asctime( time.localtime(time.time()) )
def filerename(filename, newfilename):
	os.rename(filename, newfilename)
def delfile(filename):
	os.remove(filename)
def fileInformation(filename):
	filestatus= os.stat(filename)
	return filestatus
def writeTofile(filename, mode, data, time=currenttime):
	f= open(filename, mode)
	f.write("[%s] : " % time)
	f.write("%s\r\n " %data)
	f.close()
def readFromfile(filename, mode):
	f= open(filename, mode)
	data = f.readline()
	f.close()
	return data
def appendTofile(filename, mode, data, time= currenttime):
	f= open(filename, mode)
        f.write("[%s] : " % time)
        f.write("%s\r\n " %data)
        f.close()



writeTofile("hello.md", "r+b","information about ip or system errors")
(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = fileInformation("hello.md")
print readFromfile("hello.md","r+b")
print "access rights to this file:%s" % oct(stat.S_IMODE(mode))
print "members to determine phisical location of the file:%s" % hex(ino)
print "members to determine phisical location of the file:%s" % hex(dev)
print "number of hard links to this file:%s" % nlink 
print "uid user indentifier: %s" % uid
print "gid group indentifier: %s" % gid
print "size: %s" % size
print "last modified: %s" % time.ctime(mtime)
print "last accsess: %s" % time.ctime(atime)
print "last time when information was changet: %s" % time.ctime(ctime)

