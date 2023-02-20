#!/usr/bin/python
import os
import re
import sys

def main():
	for line in sys.stdin:
		match = re.match("#",line)
		fields = line.strip().split(':') #strip any whitespace and split into an array

		if match or len(fields)!= 5:
			continue #the cont is for the For loop. If the line starts with a # or doesnt have the these 5 catagories (user,pass,last,first,group list) they will be skipped via continue
		username = fields[0]
		password = fields[1]

		gecos = "%s %s,,," % (fields[3],fields[2])

		groups = fields[4].split(',') # a user might be in multiple groups so we should take each group using split and make an array of groups, so we can now use that to add the user to each of the groups

		print("==> Creating account for %s..." % (username))
		cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
		print(cmd)

		os.system(cmd)	#executes the cmd in a subshell. when used the shell of the OS is opened and cmd is executed on it

		print("Setting password for %s..." %(username))

		cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
		print(cmd)
		os.system(cmd)

		for group in groups: #a user might be in multiple groups so that is why we must add the user to each get each group their in
			if group != '-': #if they are missing a group aka - then skip them
				print("==> Assigning %s to the %s group..." % (username, group))
				cmd = "usr/sbin/adduser %s %s" % (username, group)
				print(cmd)
				os.system(cmd)

if __name__ == '__main__':
	main()
