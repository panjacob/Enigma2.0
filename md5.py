import hashlib
from algorithm import Algorithm


class Md5(Algorithm):
    def encrypt(self, data):
        encoded_data = data.encode()
        return hashlib.md5(encoded_data)

    def decrypt(self, data):
        pass

