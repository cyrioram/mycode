#!/usr/bin/python3

#parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 #counter for fails

# open the file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

#convert text file into list [""] (which consumes mem)
keystone_file_lines = keystone_file.readlines()

#loop over the list of lines
for line in keystone_file_lines:
    #if this "fail patter' appears in the line...
    if "-----] Authorization failed" in line:
        loginfail += 1 #loginfail + 1
print("The number of failed log in attemps is", loginfail)
print(f"The formatted number of failed log in attempts is {loginfail}")
keystone_file.close() #Close the opened file
