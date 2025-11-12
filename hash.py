# import hashlib

# print(hashlib.algorithms_available)

# def  hash_string(text, algorithm="sha256"):
#     text_bytes = text.encode('utf-8')
#     if algorithm == "md5":
#         hash_obj = hashlib.md5(text_bytes)
#     if algorithm == "sha1":
#         hash_obj = hashlib.sha1(text_bytes)
#     if algorithm == "sha256":
#         hash_obj = hashlib.sha256(text_bytes)
#     if algorithm == "sha512":
#         hash_obj = hashlib.sha512(text_bytes)

#     return hash_obj.hexdigest()

# algorithms = ['md5', 'sha1', 'sha256', 'sha512']
# text=  "hello world"

# for al in algorithms:
#     print(hash_string(text, al))

import os
import hashlib
ALGORITHMS = ['md5', 'sha1', 'sha256', 'sha512']

def hash_file(filename,  algorithms = None, block_size =  65):
    if algorithms is None:
        algorithms =  ALGORITHMS

    if not os.path.exists(filename):
        print("file not exists")

    hash_objects = {}
    for algo in algorithms:
        hash_objects[algo] = hashlib.new(algo)

    with open(filename, 'rb') as f:
        while True:
            block = f.read(block_size)
            if not block:
                break
            for hash_obj in hash_objects.values():
                hash_obj.update(block)

        results = {}
        for algo, hash_obj in hash_objects.items():
            results[algo] =  hash_obj.hexdigest()

        return results

           
       

print(hash_file("sample.txt", ALGORITHMS))