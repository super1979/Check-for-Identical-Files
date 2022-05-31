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
        os.remove(hash_file)

check_path = input('Enter the path to perform the script on: ')
hash_file_path = input('Enter the path the hash file is on.\nPress enter if there is no hash file: ')
if hash_file_path == '':
    hash_file_path = check_path
hash_file = hash_file_path + '\hash1.txt'
if os.path.exists(check_path) and os.path.exists(hash_file_path):
    a = dict()
    check_for_hash_file(hash_file, a)
    os.chdir(check_path)
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
    if len(a) == 0:
        pass
    else:
        print("Done with " + check_path + " with " + str(len(a)) + " entries")
        for b in iter(a.items()):
            with open(hash_file, 'a') as hash:
                c = '\t'.join(b) + '\n'
                hash.write(c)
else:
    print('Path does not exist')
