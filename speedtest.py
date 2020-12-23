from des_algorithm import Des1, Des3
from aes_algorithm import Aes
from elgamal_algorithm import ElgamalAlgorithm
import datetime
import matplotlib.pyplot as plt


def test_1des(message):
    des1 = Des1('some key')
    encrypted = des1.encrypt(message)
    decrypted = des1.decrypt(encrypted)


def test_3des(message):
    des3 = Des3('a key for TRIPLE')
    encrypted = des3.encrypt(message)
    decrypted = des3.decrypt(encrypted)


def test_aes(message):
    aes = Aes('sixteen byte key')
    encrypted = aes.encrypt(message)
    decrypted = aes.decrypt(encrypted)


def test_elgamal(message):
    elgamal = ElgamalAlgorithm(p=17902191281122025399,
                               g=7,
                               y=66820913534799604363162835971702567696,
                               x=599088883783335410)
    encrypted_message = elgamal.encrypt(message).get()
    decrypted_message = elgamal.decrypt(encrypted_message)


repeat = 10000
message_to_test = "Hello"

des1_start = datetime.datetime.now()
for i in range(0, repeat):
    test_1des(message=message_to_test)
des1_end = datetime.datetime.now()
des1_result = des1_end - des1_start

des3_start = datetime.datetime.now()
for i in range(0, repeat):
    test_3des(message=message_to_test)
des3_end = datetime.datetime.now()
des3_result = des3_end - des3_start

aes_start = datetime.datetime.now()
for i in range(0, repeat):
    test_aes(message=message_to_test)
aes_end = datetime.datetime.now()
aes_result = aes_end - aes_start

elgamal_start = datetime.datetime.now()
for i in range(0, repeat):
    test_elgamal(message=message_to_test)
elgamal_end = datetime.datetime.now()
elgamal_result = elgamal_end - elgamal_start

names = ['1des', '3des', 'aes', 'elgamal']
values = [des1_result.microseconds, des3_result.microseconds, aes_result.microseconds, elgamal_result.microseconds]
plt.subplot(133)
plt.title('10000 repeats, message="Hello"')
plt.ylabel('microseconds')
plt.xlabel('algorithm')
plt.bar(names, values)


plt.show()
