from algorithm import Algorithm
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

"""
Title
-----
    DSA algorithm

Author
-------
    Rafał Kreft

Description
-----------

DSA - The Digital Signature Algorithm (DSA) is a Federal Information Processing
      Standard for digital signatures, based on the mathematical concept of modular
      exponentiation and the discrete logarithm problem. DSA is a variant of the 
      Schnorr and ElGamal signature schemes. The National Institute of Standards
      and Technology (NIST) proposed DSA for use in their Digital Signature Standard
      (DSS) in 1991, and adopted it as FIPS 186 in 1994. Four revisions to the initial
      specification have been released. The newest specification is FIPS 186-4 from 
      July 2013.

Source of encryption module
---------------------------
https://pycryptodome.readthedocs.io/en/latest/src/public_key/dsa.html
"""


class Dsa(Algorithm):
    """
        A class to represents a DSA algorithm, inherits from Algorithm class.

        Attributes
        ----------
            Algorithm : Algorithm.class
                All algorithm abstract methods must be implemented by Dsa class

        Methods
        -------
            encrypt(self):
                Creates digital signature based on generated public key and input data

            decrypt(self):
                Checks if digital signature matches public key
        """

    def encrypt(self):
        """
        Takes in user message and generates random public key in file public_key.pem.
        Based on those things creates digital signature in signature.txt file.

        Parameters
        ----------
            self : String
                User-specified input plain text message

        Returns
        -------
            "Saved signature: " + str(signature) + " to signature.txt file." : String
                Information about saved digital signature in signature.txt
        """
        key = DSA.generate(2048)
        f = open("public_key.pem", "wb")
        f.write(key.publickey().export_key())
        f.close()

        message = self.encode()
        hash_obj = SHA256.new(message)
        signer = DSS.new(key, 'fips-186-3')
        signature = signer.sign(hash_obj)
        fs = open("signature.txt", "wb")
        fs.write(signature)
        fs.close()
        return "Saved signature: " + str(signature) + " to signature.txt file."

    def decrypt(self):
        """
        Takes in user message and checks if it matches earlier created digital signature.

        Parameters
        ----------
            self : String
                User-specified input plain text message

        Returns
        -------
            "The message is authentic." : String
                If message provided by the user matches digital signature.
            "The message is not authentic." : String
                If message provided by the user does not matches digital signature.
        """
        fs = open("signature.txt", "rb")
        signature = fs.read()
        fs.close()
        fk = open("public_key.pem", "rb")
        key = DSA.import_key(fk.read())
        fk.close()
        hash_obj = SHA256.new(self.encode())
        verifier = DSS.new(key, 'fips-186-3')
        try:
            verifier.verify(hash_obj, signature)
            return "The message is authentic."
        except ValueError:
            return "The message is not authentic."
