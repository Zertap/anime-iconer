"""
FolderIconer
A tool to change windows folder icon(by using Desktop.ini) to a custom icon (like a cover of a serie within the folder).
"""
import os
import fnmatch
import updateicon
import re

for root, dirnames, filenames in os.walk('./'):
	for dirname in dirnames:
		fulldirname = os.path.join(root, dirname)
		if "folder.ico" not in os.listdir(fulldirname):
			print "folder.ico not found in " + fulldirname
			#TODO --> Create the icon file from another format if not found!
		else:
			print 'folder.ico found at: ' + fulldirname + '\n Setting it as the icon...'
			updateicon.seticon(fulldirname, fulldirname + '\\folder.ico', 0)
			#TODO --> Update Desktop.ini to not use full path of the icon.
