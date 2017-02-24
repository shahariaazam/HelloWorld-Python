import os

# Whether file is exists or not
print (os.path.exists("static_storage"))
print (os.path.isfile("static_storage"))

try:
    file = open("static_storage/hello_world.txt", "r")
    print file.read()

    info = os.stat("static_storage/hello_world.txt")
    print info
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)

# File list of a directory
print "\n== File list of directory =="
for file in os.listdir("/var/www"):
    print file

print "\n== File list of directory with extension =="
for file in os.listdir("/var/www"):
    try:
        filetype = ''
        if file.split(".")[1]:
            filetype = file.split(".")[1]
        print (file + " is %s type" % (filetype))
    except:
        print "Can't determine filetype"
