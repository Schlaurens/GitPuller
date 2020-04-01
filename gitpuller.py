#Author: Laurens Schiefelbein
#Version 2020-4-02

import glob
import os

#Path to your git directories. The the * represents all of your git repositories.
#Example: "/Users/Name/gitrepositories/*"

#If you have multiple directories with git repositories, add the paths to the array by using +=

list = glob.glob ("/Users/Name/gitrepositories/*") #<--- Path to your git directory.
#list += glob.glob ("/Users/Name/gitrepositories/*")

for i in list:
	os.chdir(i)
	os.system('git pull')