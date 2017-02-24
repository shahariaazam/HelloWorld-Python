import os

# Whether file is exists or not
print (os.path.exists("static_storage"))

# File list of a directory
print "\n== File list of directory =="

count = 0
for root, directories, filenames in os.walk('/tmp'):
    for filename in filenames:
        print os.path.join(root, filename)
        count += 1

print ("Total files %d" % (count))