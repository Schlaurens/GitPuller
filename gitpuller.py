#Author: Laurens Schiefelbein
#Version 2019-12-23

import glob
import os

#Path to your git directories. The the * represents all of your git repositories.
#Example: "/Users/Name/gitrepositories/*"

#If you have multiple directories with git repositories, use multiple lists and for-loops. (there are additional loops that are commented out).

list = glob.glob ("/Users/Name/gitrepositories/*") #<--- Path to your git directory.

for i in list:
	os.chdir(i)
	os.system('git pull')


"""
list1 = glob.glob ("/Users/Name/gitrepositories/*") 

for i in list1:
	os.chdir(i)
	os.system('git pull')

"""

"""
list2 = glob.glob ("/Users/Name/gitrepositories/*") 

for i in list2:
	os.chdir(i)
	os.system('git pull')
"""

"""
list2 = glob.glob ("/Users/Name/gitrepositories/*") 

for i in list2:
	os.chdir(i)
	os.system('git pull')

"""