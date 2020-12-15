from des import DesKey
from algorithm import Algorithm

"""
Title
-----
    DES algorithms

Author
-------
    Jakub Kwiatkowski

Description
-----------

DES - is a block cipher algorithm that takes plain text in blocks of 64 bits 
      and converts them to ciphertext using keys of 48 bits. It is a symmetric
      key algorithm, which means that the same key is used for encrypting and 
      decrypting data.

3DES - Triple DES is a encryption technique which uses three instance of DES on
       same plain text. It uses there different types of key choosing technique
       in first all used keys are different and in second two keys are same and
       one is different and in third all keys are same.

Source of encryption module
---------------------------
https://pypi.org/project/des/
"""

# Example keys:
# "some key" - DES
# "a key for TRIPLE" - 3DES


class DesAlgorithm(Algorithm):
    """
    A class to represents a DES1/DES3 encryption and decryption functions, inherits from Algorithm class.

    Attributes
    ----------
        Algorithm : Algorithm.class
            All algorithm abstract methods must be implemented by DesAlgorithm class

    Methods
    -------
        encrypt(self, data):
            Encrypts and encodes data input

        decrypt(self, data):
            Decrypts and decodes encrypted data
    """

    def __init__(self, key):
        """
        Creates DesKey from given plain text

        Parameters
        ----------
            key : String
                User-specified plain text encryption key
        """
        self.key = DesKey(str.encode(key))

    def encrypt(self, data):
        """
        Takes in plain text data and encrypts it with DES/DES3 algorithm.

        Parameters
        ----------
            data : String
                User-specified plain text message

        Returns
        -------
            encrypted : bytes object
                DES-encrypted result
        """
        data_bytes = str.encode(data)
        encrypted = self.key.encrypt(data_bytes, padding=True)
        return encrypted.decode('latin-1')

    def decrypt(self, data):
        """
        Takes in plain text data and decrypts it with DES/DES3 algorithm.

        Parameters
        ----------
            data : String
                Encrypted input data

        Returns
        -------
            decrypted : bytes object
                DES-decrypted result
        """
        data_bytes = str.encode(data, 'latin-1')
        decrypted = self.key.decrypt(data_bytes, padding=True)
        return decrypted.decode('latin-1')


class Des1(DesAlgorithm):
    """
    An inner class for DES algorithm

    Parameters
    ----------
        DesAlgorithm: DesAlgorithm.class
            The class from which DES1 inherits
    """
    def __init__(self, key):
        super().__init__(key)
        assert self.key.is_single()


class Des3(DesAlgorithm):
    """
    An inner class for DES3 algorithm

        Parameters
    ----------
        DesAlgorithm: DesAlgorithm.class
            The class from which DES3 inherits
    """
    def __init__(self, key):
        super().__init__(key)
        assert self.key.is_triple()
