import hashlib
from algorithm import Algorithm

"""
Title
-----
    MD5 Hash algorithm

Author
-------
    Jakub Kwiatkowski

Description
-----------

MD5 - The MD5 message-digest algorithm is a widely used hash function producing a 128-bit hash value.
      Although MD5 was initially designed to be used as a cryptographic hash function, it has been
      found to suffer from extensive vulnerabilities. It can still be used as a checksum to verify
      data integrity, but only against unintentional corruption. It remains suitable for other
      non-cryptographic purposes, for example for determining the partition for a particular key
      in a partitioned database. MD5 was designed by Ronald Rivest in 1991 to replace an earlier
      hash function MD4, and was specified in 1992 as RFC 1321. 

Source of encryption module
---------------------------
https://docs.python.org/3/library/hashlib.html
"""


class Md5(Algorithm):
    """
    A class to represents a MD5 hash algorithm, inherits from Algorithm class.

    Attributes
    ----------
        Algorithm : Algorithm.class
            All algorithm abstract methods must be implemented by Md5 class

    Methods
    -------
        encrypt(self, data):
            Creates md5 hash value from input data
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
            hashlib.md5(encoded_data) : HashObject
                Result of md5 hash function
        """
        encoded_data = data.encode()
        return hashlib.md5(encoded_data)

    def decrypt(self, data):
        pass
