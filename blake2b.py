import hashlib
from algorithm import Algorithm

"""
Title
-----
    Blake2b Hash algorithm

Author
-------
    Rafał Kreft

Description
-----------

Blake2b -  is a cryptographic hash function defined in RFC 7693.
           BLAKE2b, optimized for 64-bit platforms and produces digests of any size between 1 and 64 bytes.

Source of encryption module
---------------------------
https://docs.python.org/3/library/hashlib.html
"""


class Blake2b(Algorithm):
    """
    A class to represents a Blake2b hash algorithm, inherits from Algorithm class.

    Attributes
    ----------
        Algorithm : Algorithm.class
            All algorithm abstract methods must be implemented by Blake2b class

    Methods
    -------
        encrypt(self, data):
            Creates blake2b hash value from input data
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
            hashlib.blake2b(encoded_data) : HashObject
                Result of blake2b hash function
        """
        encoded_data = data.encode()
        return hashlib.blake2b(encoded_data)

    def decrypt(self, data):
        pass
