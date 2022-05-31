import os
import os.path
import hashlib

def subdir(hash_storage, p, i, idfp2):
    os.chdir(p)
    entities = os.listdir(os.getcwd())
    for entity in entities:
        if os.path.isfile(entity):
            with open(entity, 'rb') as src:
                by = src.read()
                ha = hashlib.sha1(by).hexdigest()
                if ha not in hash_storage:
                    hash_storage[ha] = str(os.path.abspath(entity))
                else:
                    with open(idfp2, 'a') as clash:
                        clash.write(hash_storage[ha] + '\t' + str(os.path.abspath(entity)) + '\n')
                    i = True
        else:
            new_path = os.path.join(p, entity)
            i = subdir(hash_storage, new_path, i, idfp2)
            os.chdir(p)
    return i

def main(path, idfp):
    a = dict()
    identical = False
    identical_file_path = idfp + '\same.txt'
    identical = subdir(a, path, identical, identical_file_path)
    print("Done with " + str(len(a)) + " entries")
    if identical:
        print("There are identical files. Go to " + str(path) + " for the record of identical files.")

path_entered = input('Enter the path to perform the script on: ')
path2 = input('Enter the path where the result will be stored to: ')
if os.path.exists(path_entered) and os.path.exists(path2):
    main(path_entered, path2)
else:
    print('One of the paths provided does not exist.')
