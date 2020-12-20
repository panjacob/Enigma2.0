import unittest
from des_algorithm import Des1, Des3
from aes_algorithm import Aes
from elgamal_algorithm import ElgamalAlgorithm, PrivateKey, PublicKey


class TestAlgorithms(unittest.TestCase):

    def test_1des(self):
        original_message = 'Testujemy 1des!'
        des1 = Des1('some key')
        encrypted = des1.encrypt(original_message)
        decrypted = des1.decrypt(encrypted)

        self.assertEqual(decrypted, original_message)

    def test_3des(self):
        original_message = 'Testujemy 3des!'
        des3 = Des3('a key for TRIPLE')
        encrypted = des3.encrypt(original_message)
        decrypted = des3.decrypt(encrypted)

        self.assertEqual(decrypted, original_message)

    def test_aes(self):
        original_message = 'Test AES'
        aes = Aes('sixteen byte key')
        encrypted = aes.encrypt(original_message)
        decrypted = aes.decrypt(encrypted)

        self.assertEqual(decrypted, original_message)

    def test_elgamal(self):
        elgamal = ElgamalAlgorithm(p=17902191281122025399, g=7, y=66820913534799604363162835971702567696,
                                   x=599088883783335410)
        data = "Siemanko"
        encrypted_message = elgamal.encrypt(data).get()
        decrypted_message = elgamal.decrypt(encrypted_message)

        self.assertEqual(data, decrypted_message)


if __name__ == '__main__':
    unittest.main()
