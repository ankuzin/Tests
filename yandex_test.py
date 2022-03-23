import unittest
from yandex_api import create_folder,get_folder_info

folder_name = 'test'


class TestYandexAPI(unittest.TestCase):
    def test_create_folder(self):
        self.assertTrue(create_folder(folder_name) == 201, f'Папка {folder_name} несоздана на Яндекс Диске')
        print(f'Папка {folder_name} успешно создана на Яндекс Диске')
    def test_get_folder_info(self):
        self.assertTrue(get_folder_info(folder_name) == 200, f'Папка {folder_name} ненайдена на Яндекс Диске')
        print(f'Папка {folder_name} найдена на Яндекс Диске')

if __name__ == '__main__':
    unittest.main()