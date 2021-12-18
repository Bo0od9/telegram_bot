import unittest
from unittest import mock
from unittest.mock import MagicMock
import main
from unittest.mock import ANY
from vigenere_chipher import char_to_index, index_to_char, decode, encode, main_encode, main_decode, \
    form_gamma_by_userkey
from caesar_chipher import caesar_encode, caesar_decode


class sumsTest(unittest.TestCase):
    def test_char_to_index_1(self):
        self.assertEqual(char_to_index('abcdefghijklmnopqrstuvwxyz'),
                         [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65,
                          66, 67, 68])

    def test_char_to_index_2(self):
        self.assertEqual(char_to_index('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                         [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                          40, 41, 42])

    def test_char_to_index_3(self):
        self.assertEqual(char_to_index('0123456789'), [7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_char_to_index_4(self):
        self.assertEqual(char_to_index(' .,?!:;'), [0, 1, 2, 3, 4, 5, 6])

    def test_char_to_index_5(self):
        self.assertEqual(char_to_index('jhkjhqocmjIOJMgiu768!knlkj;'),
                         [52, 50, 53, 52, 50, 59, 57, 45, 55, 52, 25, 31, 26, 29, 49, 51, 63, 14, 13, 15, 4, 53, 56, 54,
                          53, 52, 6])

    def test_char_to_index_6(self):
        self.assertEqual(char_to_index('Hello world! 0o0'), [24, 47, 54, 54, 57, 0, 65, 57, 60, 54, 46, 4, 0, 7, 57, 7])

    def test_char_to_index_7(self):
        self.assertEqual(char_to_index('In the midst of a conversation on political matters Anna Pavlovna burst out'),
                         [25, 56, 0, 62, 50, 47, 0, 55, 51, 46, 61, 62, 0, 57, 48, 0, 43, 0, 45, 57, 56, 64, 47, 60, 61,
                          43, 62, 51, 57, 56, 0, 57, 56, 0, 58, 57, 54, 51, 62, 51, 45, 43, 54, 0, 55, 43, 62, 62, 47,
                          60, 61, 0, 17, 56, 56, 43, 0, 32, 43, 64, 54, 57, 64, 56, 43, 0, 44, 63, 60, 61, 62, 0, 57,
                          63, 62]
                         )

    def test_index_to_char_1(self):
        self.assertEqual(index_to_char(
            [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]),
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z'])

    def test_index_to_char_2(self):
        self.assertEqual(index_to_char(
            [25, 56, 0, 62, 50, 47, 0, 55, 51, 46, 61, 62, 0, 57, 48, 0, 43, 0, 45, 57, 56, 64, 47, 60, 61, 43, 62, 51,
             57, 56, 0, 57, 56, 0, 58, 57, 54, 51, 62, 51, 45, 43, 54, 0, 55, 43, 62, 62, 47, 60, 61, 0, 17, 56, 56, 43,
             0, 32, 43, 64, 54, 57, 64, 56, 43, 0, 44, 63, 60, 61, 62, 0, 57, 63, 62]),
            ['I', 'n', ' ', 't', 'h', 'e', ' ', 'm', 'i', 'd', 's', 't', ' ', 'o', 'f', ' ', 'a', ' ', 'c',
             'o', 'n', 'v', 'e', 'r', 's', 'a', 't', 'i', 'o', 'n', ' ', 'o', 'n', ' ', 'p', 'o', 'l', 'i',
             't', 'i', 'c', 'a', 'l', ' ', 'm', 'a', 't', 't', 'e', 'r', 's', ' ', 'A', 'n', 'n', 'a', ' ',
             'P', 'a', 'v', 'l', 'o', 'v', 'n', 'a', ' ', 'b', 'u', 'r', 's', 't', ' ', 'o', 'u', 't'])

    def test_main_encode_1(self):
        self.assertEqual(main_decode('Hello world', 'key'), 'X n.3,53t.z')

    def test_main_encode_2(self):
        self.assertEqual(main_decode('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                         'JJJJJJJJJJJJJJJJJJJJJJJJJJ')

    def test_main_encode_3(self):
        self.assertEqual(main_decode('abcABC1234567890!,. :;',
                                     'ABCDEFA89Babcdefghijkl098 mnopqrstuvwxyz9CDEFGHIJKLMNOPQRSTUVWXYZGHIJKLMNOPQRSTUVWXYZ'),
                         'JJJxxxruutVVVVVLHECAEE')

    @mock.patch('main.bot')
    def test_main_encode_55(self, main_bot):
        chat = MagicMock(id=123)
        message = MagicMock(text="о боте", chat=chat)
        main.mess(message)
        main_bot.send_message.assert_called_with(123,
                                                 f'Бот умеет зашифровывать и расшифровывать текст на латинице с помощью шифра Цезаря и шифра Виженера. Бот создан в качестве итогового проекта по дисциплине АиП. Словарь допустимых символов: {main.get_dict()}')

    @mock.patch('main.bot')
    def test_main_encode_57(self, main_bot):
        chat = MagicMock(id=123)
        message = MagicMock(text="зашифровать сообщение", chat=chat)
        main.mess(message)
        main_bot.send_message.assert_called_with(123,'Выберите метод шифрования', parse_mode='html', reply_markup=ANY)

    @mock.patch('main.bot')
    def test_main_encode_58(self, main_bot):
        chat = MagicMock(id=123)
        message = MagicMock(text="зашифровать сообщение", chat=chat)
        main.mess(message)
        main_bot.send_message.assert_called_with(123,'Выберите метод шифрования', parse_mode='html', reply_markup=ANY)

if __name__ == "__main__":
    unittest.main()
