"""AnimeIconer
A tool to change windows folder icon(by using Desktop.ini) to a cover of the corresponding series.
Written by zertap"""
####CURRENTLY YOU NEED TO MANUALLY DOWNLOAD, CONVERT TO .ico AND PLACE THE COVER INTO AN ANIME FOLDER####
import os
import fnmatch
import updateicon
import re

for root, dirnames, filenames in os.walk('./'):
	for dirname in dirnames:
		fulldirname = os.path.join(root, dirname)
		if "folder.ico" not in os.listdir(fulldirname):
			print "folder.ico not found in " + fulldirname
			"""TODO --> Create the icon file if not found!"""
		else:
			print 'folder.ico found at: ' + fulldirname + '\n Setting it as the icon...'
			updateicon.seticon(fulldirname, fulldirname + '\\folder.ico', 0)
			"""TODO --> Update Desktop.ini to not use full path of the icon."""

