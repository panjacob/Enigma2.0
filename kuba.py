from des import DesKey

des_key = DesKey(b"some key")  # for DES
des3_key = DesKey(b"a key for TRIPLE")  # for 3DES, same as "a key for TRIPLEa key fo"


def des(mode, data):
    if mode == 1:
        data_bytes = str.encode(data)
        encrypted = des_key.encrypt(data_bytes, padding=True)
        return encrypted.decode('latin-1')
    if mode == 2:
        data_bytes = str.encode(data, 'latin-1')
        decrypted = des_key.decrypt(data_bytes, padding=True)
        return decrypted.decode('latin-1')


def des3(mode, data):
    if mode == 1:
        data_bytes = str.encode(data)
        encrypted = des3_key.encrypt(data_bytes, padding=True)
        return encrypted.decode('latin-1')
    if mode == 2:
        data_bytes = str.encode(data, 'latin-1')
        decrypted = des3_key.decrypt(data_bytes, padding=True)
        return decrypted.decode('latin-1')


encrypted = des(1, 'daskdjasl')
print(encrypted)
decrypted = des(2, encrypted)
print(decrypted)
