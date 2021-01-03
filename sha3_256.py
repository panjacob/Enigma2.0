import hashlib
from algorithm import Algorithm

"""
Title
-----
    SHA3_256 Hash algorithm

Author
-------
    Jakub Kwiatkowski

Description
-----------

SHA3_256 - SHA3-256 belongs to the SHA-3 family of cryptographic hashes, as specified in FIPS 202.
           The hash function produces the 256 bit digest of a message.
           (More info in main.py documentation)

Source of encryption module
---------------------------
https://docs.python.org/3/library/hashlib.html
"""


class Sha3_256(Algorithm):
    """
    A class to represents a SHA3_256 hash algorithm, inherits from Algorithm class.

    Attributes
    ----------
        Algorithm : Algorithm.class
            All algorithm abstract methods must be implemented by Sha3_256 class

    Methods
    -------
        encrypt(self, data):
            Creates Sha3_256 hash value from input data
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
            hashlib.sha3_256(encoded_data) : HashObject
                Result of Sha3_256 hash function
        """
        encoded_data = data.encode()
        return hashlib.sha3_256(encoded_data)

    def decrypt(self, data):
        pass
