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
        
a = dict()
path = 'C:\\Users\\gilbe\\OneDrive\\Pictures\\Internet\\116'
hash_file_path = 'C:\\Users\\gilbe\\OneDrive\\Pictures\\Internet\\hash.txt'
check_for_hash_file(hash_file_path, a)
os.chdir(path)
entities = os.listdir(os.getcwd())
for entity in entities:
    with open(entity, 'rb') as src:
        by = src.read()
        ha = hashlib.sha1(by).hexdigest()
        if ha not in a:
            a[ha] = str(os.path.basename(entity))
        else:
            with open('same.txt', 'a', encoding = 'utf-8') as clash:
                clash.write(a[ha] + '\t' + str(entity) + '\n')
if len(a) == 0:
    pass
else:
    print("Done with " + path + " with " + str(len(a)) + " entries")
    for b in iter(a.items()):
        with open(hash_file_path, 'a', encoding = 'utf-8') as hash:
            c = '\t'.join(b) + '\n'
            hash.write(c)
