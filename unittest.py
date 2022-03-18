import unittest
from parameterized import parameterized
from main import check_document_existance, get_doc_owner_name, add_new_shelf,delete_doc,add_new_doc


TEST_1 = (["2207 876234", True],["11-2", True],["10006", True],["2011", False])
TEST_2 = (["2207 876234", "Василий Гупкин"], ["11-2", "Геннадий Покемонов"], ["10006", "Аристарх Павлов"], ["2031-05", "Антон Васильев" ])
TEST_3 = (['7', ('7', True)],['6', ('6', True)],['1', ('1', False)])


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @parameterized.expand(TEST_1)
    def test_check_document_existance(self, test, actual):
        self.assertEqual(check_document_existance(test), actual)

    @parameterized.expand(TEST_2)
    def test_get_doc_owner_name(self, test, actual):
        self.assertEqual(get_doc_owner_name(test), actual)

    @parameterized.expand(TEST_3)
    def test_add_new_shelf(self, test, actual):
        self.assertEqual(add_new_shelf(test), actual)


