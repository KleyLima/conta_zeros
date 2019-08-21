# coding: utf-8

import unittest
from source.conta_zero_kleyton import ContaZero


class TesteContaZero(unittest.TestCase):
    def test_conta_zero(self):
        self.assertEqual(ContaZero("01001000").conta_zeros(), 3)  # Sequencial, ultima sequência é a maior
        self.assertEqual(ContaZero("123456").conta_zeros(), 0)  # Não possui zero algum
        self.assertEqual(ContaZero("1230456").conta_zeros(), 1)  # Zero único, no meio da string
        self.assertEqual(ContaZero("00010").conta_zeros(), 3)  # Primeira ocorrência é a maior
        self.assertEqual(ContaZero("0100010010").conta_zeros(), 3)  # Ocorrência no meio da string é a maior
        self.assertEqual(ContaZero("00000").conta_zeros(), 5)  # String possui apenas zeros


if __name__ == '__main__':
    unittest.main()
