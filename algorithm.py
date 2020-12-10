from abc import abstractmethod


class Algorithm:
    @abstractmethod
    def encrypt(self, data):
        pass

    @abstractmethod
    def decrypt(self, data):
        pass
