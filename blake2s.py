import hashlib
from algorithm import Algorithm

"""
Title
-----
    Blake2s Hash algorithm

Author
-------
    Rafał Kreft

Description
-----------

Blake2s -  is a cryptographic hash function defined in RFC 7693.
           BLAKE2s, optimized for 8- to 32-bit platforms and produces digests of any size between 1 and 32 bytes.

Source of encryption module
---------------------------
https://docs.python.org/3/library/hashlib.html
"""


class Blake2s(Algorithm):
    """
    A class to represents a Blake2s hash algorithm, inherits from Algorithm class.

    Attributes
    ----------
        Algorithm : Algorithm.class
            All algorithm abstract methods must be implemented by Blake2s class

    Methods
    -------
        encrypt(self, data):
            Creates blake2s hash value from input data
    """

    def encrypt(self, data):
        """
        Takes in user message, encodes it and creates hash value.

        Parameters
        ----------
            data : String
                User-specified input plain text message

        Returns
        -------
            hashlib.blake2s(encoded_data) : HashObject
                Result of blake2s hash function
        """
        encoded_data = data.encode()
        return hashlib.blake2s(encoded_data)

    def decrypt(self, data):
        pass
