import os
import sys
import argparse
import shutil
import zipfile
import random
import string

class Hack:

	def __init__(self,args):
		self.setPath(args)
		print self.tPath
		print self.cPath
		self.waitForInsertion()
		self.copyFiles()
		self.zipFiles()
		print 'Scan Complete!'

	def waitForInsertion(self):
		print 'Waiting for Drive Detection!'
		temp = os.getcwd()
		while(True):
			try:
				os.chdir(self.tPath)
				os.chdir(temp)
				break
			except:
				pass
		print 'Drive detected'

	def zipFiles(self):
		print 'Attempting compressing files'
		zipf = zipfile.ZipFile('Hack.zip','w',zipfile.ZIP_DEFLATED)
		for item in os.listdir(self.cPath):
			zipf.write(os.path.join(self.cPath,item))
		zipf.close()
		shutil.rmtree(self.cPath)
		print 'Compressing complete'

	def setPath(self,targetDrive):
		self.tPath = os.path.abspath(str(targetDrive)+'://')
		self.cPath = os.path.join(os.getcwd(),'Hack')

	def copyFiles(self):
		print 'Copying Files!'
		shutil.copytree(self.tPath,self.cPath)
		print 'Finished copying files'


def main():
	Hack(raw_input("Enter drive Name:"))

if __name__=="__main__":
	main()