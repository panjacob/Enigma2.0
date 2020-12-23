import hashlib
from algorithm import Algorithm


class Sha3_256(Algorithm):
    def encrypt(self, data):
        encoded_data = data.encode()
        return hashlib.sha3_256(encoded_data)

    def decrypt(self, data):
        pass
