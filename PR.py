import os
import os.path
import hashlib

def subdir(hash_storage, p, i, idfp):
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
                    with open(idfp, 'a') as clash:
                        clash.write(hash_storage[ha] + '\t' + str(os.path.abspath(entity)) + '\n')
                    i = True
        else:
            new_path = os.path.join(p, entity)
            i = subdir(hash_storage, new_path, i, idfp)
            os.chdir(p)
    return i

a = dict()
path = 'F:\Main'
identical_file_path = path + '\same.txt'
identical = False
identical = subdir(a, path, identical, identical_file_path)
print("Done with " + str(len(a)) + " entries")
if identical:
    print("There are identical files. Go to " + str(path) + " for the record of identical files.")

