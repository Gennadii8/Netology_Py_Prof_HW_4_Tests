import unittest
from main import make_a_folder
from ya_token import ya_token


class TestAnswers(unittest.TestCase):

    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_make_a_folder_201(self):
        result = make_a_folder(ya_token)
        if result[0] != 201:
            print(f'Код ответа - {result[0]}')
            print('Папка не создана')
            print(f'Результат - {result[1]}')
        if not self.assertEqual(201, result[0]):
            print(f'Код ответа - {result[0]}')
            print('Папка успешно создана')
            print(f'Результат - {result[1]}')


if __name__ == '__main__':
    unittest.main()