from hashlib import md5

prefix = 'ckczppom'
current_i = 0
current_hash = md5((prefix + str(current_i)).encode('ascii'))

while current_hash.hexdigest()[:6] != '000000':
    current_i += 1
    current_hash = md5((prefix + str(current_i)).encode('ascii'))

print(current_i)
