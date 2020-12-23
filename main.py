from utilis import get_int, get_algorithm
from sha3_256 import Sha3_256
from sha3_512 import Sha3_512
from md5 import Md5

"""
Title
-----
    Selected encryption and decryption algorithms
    
Authors
-------
    Jakub Kwiatkowski
    Rafał Kreft
    
Algorithms descriptions
-----------------------
DES - is a block cipher algorithm that takes plain text in blocks of 64 bits 
      and converts them to ciphertext using keys of 48 bits. It is a symmetric
      key algorithm, which means that the same key is used for encrypting and 
      decrypting data.
      
3DES - Triple DES is a encryption technique which uses three instance of DES on
       same plain text. It uses there different types of key choosing technique
       in first all used keys are different and in second two keys are same and
       one is different and in third all keys are same.

AES - The AES algorithm (also known as the Rijndael algorithm) is a symmetrical
      block cipher algorithm that takes plain text in blocks of 128 bits and 
      converts them to ciphertext using keys of 128, 192, and 256 bits. 
      Since the AES algorithms considered secure, it is in the worldwide
      standard.
      
Sources of encryption modules
-----------------------------
https://pypi.org/project/pycryptodome/
https://pypi.org/project/des/
"""

mode = get_int('mode: 1- encrypt | 2- decrypt: | 3- Hash: ', 1, 3)
if mode == 1 or mode == 2:
    algorithm_number = get_int('algorithm: 1- DES | 2- 3DES | 3- AES: | 4- ElGamal: ', 1, 5)
    algorithm = get_algorithm(algorithm_number, mode)
    if algorithm_number == 4 and mode == 2:
        a = int(input('a: '))
        b = int(input('b: '))
        data = (a, b)
    else:
        data = input('data: ')
    if mode == 1:
        result = algorithm.encrypt(data)
    else:
        result = algorithm.decrypt(data)
else:
    algorithm_number = get_int('algorithm: 1- SHA3_256 | 2- SHA3_512  | 3- MD5: ', 1, 3)
    if algorithm_number == 1:
        algorithm = Sha3_256()
    elif algorithm_number == 2:
        algorithm = Sha3_512()
    else:
        algorithm = Md5()
    data = input('data: ')
    result = algorithm.encrypt(data).hexdigest()

print(result)
