import os
import os.path
import hashlib

def check_for_hash_file(path, hash_storage):
    if os.path.isfile(path):
        with open(path, 'r') as open_hash_file:
            for line in open_hash_file:
                cleanup_line = line.strip()
                key_value = cleanup_line.split('\t')
                hash_storage[key_value[0]] = key_value[1]
        os.remove(path)

def identical_check(hash_storage, path, i, idfp):
    os.chdir(path)
    print('In ' + path + ' now')
    entities = os.listdir(os.getcwd())
    for entity in entities:
        if os.path.isfile(entity):
            with open(entity, 'rb') as src:
                by = src.read()
                ha = hashlib.sha1(by).hexdigest()
                if ha not in hash_storage:
                    hash_storage[ha] = str(os.path.abspath(entity))
                else:
                    with open(idfp, 'a', encoding = 'utf-8') as clash:
                        clash.write(hash_storage[ha] + '\t' + str(os.path.abspath(entity)) + '\n')
                    i = True
        else:
            new_path = os.path.join(path, entity)
            i = identical_check(hash_storage, new_path, i, idfp)
            os.chdir(path)
    return i

def main(p, h, i):
    a = dict()
    identical = False
    check_for_hash_file(h, a)
    identical = identical_check(a, p, identical, i)
    if len(a) == 0:
        pass
    else:
        print("Done with " + path + " with " + str(len(a)) + " entries")
        with open(h, 'a', encoding = 'utf-8') as hash:
            for b in iter(a.items()):
                c = '\t'.join(b) + '\n'
                hash.write(c)
    if identical:
        print("There are identical files. Go to " + str(path) + " for the record of identical files.")

path = 'C:\\Users\\gilbe\\OneDrive\\Pictures\\Internet'
hash_file_path = path + '\\hash.txt'
identical_file_path = path + '\\same.txt'
main(path, hash_file_path, identical_file_path)





