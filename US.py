import os
import os.path
import hashlib

path_entered = input('Enter the path to perform the script on: ')
if os.path.exists(path_entered):
    a = dict()
    os.chdir(path_entered)
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
else:
    print('Path does not exist')
