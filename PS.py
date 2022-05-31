import os
import os.path
import hashlib

a = dict()
path = 'C:/Users/gilbe/OneDrive/Pictures/Internet/Taiwan/FB_楊莉貞'
os.chdir(path)
entities = os.listdir(os.getcwd())
for entity in entities:
    with open(entity, 'rb') as src:
        by = src.read()
        ha = hashlib.sha1(by).hexdigest()
        if ha not in a:
            a[ha] = str(os.path.basename(entity))
        else:
            with open('same.txt', 'a') as clash:
                clash.write(a[ha] + '\t' + str(entity) + '\n')
print("Done with " + str(len(a)) + " entries")
