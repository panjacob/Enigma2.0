from utilis import get_int, get_algorithm

mode = get_int('mode: 1- encrypt | 2- decrypt: ', 1, 2)
algorithm_number = get_int('algorithm: 1- DES | 2- 3DES | 3- AES: ', 1, 3)
algorithm = get_algorithm(algorithm_number)
data = input('data: ')

if mode == 1:
    result = algorithm.encrypt(data)
else:
    result = algorithm.decrypt(data)

print(result)
