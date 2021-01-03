import random
"""
Title
-----
    Simple random text generator

Author
-------
    Rafał Kreft

Description
-----------
    Random text generator module needed for salting example.
    
Sources
---------------------------
https://docs.python.org/3/library/random.html
"""


class RandomTextGenerator:

    def generate_text(length):
        """
        Generates random text basing on input data length

        Parameters
        ----------
            length : int
                User-specified text length

        Returns
        -------
            text : String
                Randomly generated text
        """
        text = ""
        for i in range(length):
            i = chr(random.randint(48, 122))
            text += i

        return text
