from abc import abstractmethod


class Algorithm:
    """
    A class with methods to be implemented

    Methods
    -------
        encrypt(self, data):
            Input data encryption method

        decryption(self, data):
            Input data decryption method
    """
    @abstractmethod
    def encrypt(self, data):
        pass

    @abstractmethod
    def decrypt(self, data):
        pass
