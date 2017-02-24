import os.path as path

# Whether file is exists or not
print (path.exists("static_storage"))
print (path.isfile("static_storage"))

try:
    file = open("static_storage/hello_worlds.txt", "r")
    print file.read()
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
