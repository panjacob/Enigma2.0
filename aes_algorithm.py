import base64
from algorithm import Algorithm
from Crypto import Random
from Crypto.Cipher import AES

# lambda expressions for formatting encrypted and decrypted data
pad = lambda s: bytes(s + (16 - len(s) % 16) * chr(16 - len(s) % 16), 'utf-8')
un_pad = lambda s: s[0:-ord(s[-1:])]


# Example keys:
# "sixteen byte key"
# "mysecretpassword"

class Aes(Algorithm):
    """
    A class to represents a AES encryption and decryption functions, inherits from Algorithm class.

    Attributes
    ----------
        Algorithm : Algorithm.class
            All algorithm abstract methods must be implemented by Aes class

    Methods
    -------
        encrypt(self, data):
            Encrypts and encodes data input

        decrypt(self, data):
            Decrypts and decodes encrypted data
    """

    def __init__(self, key):
        """
        Turns user's encryption key into bytes object.

        Parameters
        ----------
            key : String
                User-specified plain text encryption key
        """
        self.key = bytes(key, 'utf-8')

    def encrypt(self, data):
        """
        Takes in plain text data and encrypts it with the AES algorithm.

        Parameters
        ----------
            data : String
                User-specified input plain text message

        Returns
        -------
            encrypted_data : bytes object
                AES-encrypted and Base64-encoded result
        """
        data = pad(data)
        init_vector = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, init_vector)
        encrypted_data = base64.b64encode(init_vector + cipher.encrypt(data))
        return encrypted_data

    def decrypt(self, data):
        """
        Takes byte object returned by encrypt method, decrypts and decodes it to plain text.

        Parameters
        ----------
            data : bytes object
                Encrypted and encoded input bytes object

        Returns
        -------
            decrypted_data : String
                AES-decrypted and Base64-decoded result
        """
        data = base64.b64decode(data)
        init_vector = data[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, init_vector)
        decrypted_data = un_pad(cipher.decrypt(data[16:])).decode('utf8')
        return decrypted_data
