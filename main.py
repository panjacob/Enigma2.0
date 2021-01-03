from random_text_generator import RandomTextGenerator
from utilis import get_int, get_algorithm
from sha3_256 import Sha3_256
from sha3_512 import Sha3_512
from md5 import Md5
from blake2b import Blake2b
from blake2s import Blake2s

"""
Title
-----
    Selected encryption and decryption algorithms and hash functions
    
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
      
ELGAMAL - In cryptography, the ElGamal encryption system is an asymmetric key
          encryption algorithm for public-key cryptography which is based on the
          Diffie–Hellman key exchange. It was described by Taher Elgamal in 1985.
          ElGamal encryption is used in the free GNU Privacy Guard software, recent
          versions of PGP, and other cryptosystems. The Digital Signature Algorithm
          (DSA) is a variant of the ElGamal signature scheme, which should not be
          confused with ElGamal encryption.
          
DSA - The Digital Signature Algorithm (DSA) is a Federal Information Processing
      Standard for digital signatures, based on the mathematical concept of modular
      exponentiation and the discrete logarithm problem. DSA is a variant of the 
      Schnorr and ElGamal signature schemes. The National Institute of Standards
      and Technology (NIST) proposed DSA for use in their Digital Signature Standard
      (DSS) in 1991, and adopted it as FIPS 186 in 1994. Four revisions to the initial
      specification have been released. The newest specification is FIPS 186-4 from 
      July 2013.
      
      
Hash functions descriptions
---------------------------
MD5 - The MD5 message-digest algorithm is a widely used hash function producing a 128-bit hash value.
      Although MD5 was initially designed to be used as a cryptographic hash function, it has been
      found to suffer from extensive vulnerabilities. It can still be used as a checksum to verify
      data integrity, but only against unintentional corruption. It remains suitable for other
      non-cryptographic purposes, for example for determining the partition for a particular key
      in a partitioned database. MD5 was designed by Ronald Rivest in 1991 to replace an earlier
      hash function MD4, and was specified in 1992 as RFC 1321. 
      
SHA3 - (Secure Hash Algorithm 3) is the latest member of the Secure Hash Algorithm family of
       standards, released by NIST on August 5, 2015. Although part of the same series of standards,
       SHA-3 is internally different from the MD5-like structure of SHA-1 and SHA-2. SHA-3 is a subset
       of the broader cryptographic primitive family Keccak designed by Guido Bertoni, Joan Daemen,
       Michaël Peeters, and Gilles Van Assche, building upon RadioGatún. Keccak's authors have proposed
       additional uses for the function, not (yet) standardized by NIST, including a stream cipher,
       an authenticated encryption system, a "tree" hashing scheme for faster hashing on certain
       architectures, and AEAD ciphers Keyak and Ketje.

Blake - BLAKE is a cryptographic hash function based on Dan Bernstein's ChaCha stream cipher,
        but a permuted copy of the input block, XORed with round constants, is added before
        each ChaCha round. Like SHA-2, there are two variants differing in the word size.
        ChaCha operates on a 4×4 array of words. BLAKE repeatedly combines an 8-word hash
        value with 16 message words, truncating the ChaCha result to obtain the next hash
        value. BLAKE-256 and BLAKE-224 use 32-bit words and produce digest sizes of 256 bits
        and 224 bits, respectively, while BLAKE-512 and BLAKE-384 use 64-bit words and produce
        digest sizes of 512 bits and 384 bits, respectively. 
      
Sources of modules
------------------

Algorithms
----------
https://pypi.org/project/pycryptodome/
https://pypi.org/project/des/
https://pypi.org/project/elgamal/
https://pycryptodome.readthedocs.io/en/latest/src/public_key/dsa.html

Hash functions
--------------
https://docs.python.org/3/library/hashlib.html
"""

mode = get_int('mode: 1- encrypt | 2- decrypt: | 3- Hash | 4- Salting: ', 1, 4)
if mode == 1 or mode == 2:
    algorithm_number = get_int('algorithm: 1- DES | 2- 3DES | 3- AES | 4- ELGAMAL | 5- DSA: ', 1, 5)
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
    algorithm_number = get_int('algorithm: 1- SHA3_256 | 2- SHA3_512  | 3- MD5 | 4- Blake2b | 5- Blake2s: ', 1, 5)
    if algorithm_number == 1:
        algorithm = Sha3_256()
    elif algorithm_number == 2:
        algorithm = Sha3_512()
    elif algorithm_number == 3:
        algorithm = Md5()
    elif algorithm_number == 4:
        algorithm = Blake2b()
    else:
        algorithm = Blake2s()
    data = input('data: ')
    if mode == 4:
        rand = RandomTextGenerator
        length = get_int('salt length: ', 3, 30)
        salt = rand.generate_text(length)
        print(data)
        print(algorithm.encrypt(data).hexdigest())
        data = salt + data
        print(data)

    result = algorithm.encrypt(data).hexdigest()

print(result)