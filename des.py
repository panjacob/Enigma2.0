

from des import DesKey

des1_key = DesKey(b"some key")  # for DES
des3_key = DesKey(b"a key for TRIPLE")  # for 3DES, same as "a key for TRIPLEa key fo"





class DesAlgorithm(Algorithm):
    def __init__(self, key):
        self.key = DesKey(str.encode(key))

    def encrypt(self, data):
        data_bytes = str.encode(data)
        encrypted = self.key.encrypt(data_bytes, padding=True)
        return encrypted.decode('latin-1')

    def decrypt(self, data):
        data_bytes = str.encode(data, 'latin-1')
        decrypted = self.key.decrypt(data_bytes, padding=True)
        return decrypted.decode('latin-1')


class Des1(DesAlgorithm):
    def __init__(self, key):
        super().__init__(key)
        assert self.key.is_single()


class Des3(DesAlgorithm):
    def __init__(self, key):
        super().__init__(key)
        assert self.key.is_triple()
