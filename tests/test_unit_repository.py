import unittest
from unittest.mock import MagicMock
from Homework_13_2 import MyRepository

class TestMyRepository(unittest.TestCase):
    def setUp(self):
        # Ініціалізуємо мок об'єкт бази даних
        self.mock_db = MagicMock()
        self.repository = MyRepository(self.mock_db)

    def test_get_item_by_id(self):
        # Налаштовуємо мок для повернення значення
        self.mock_db.get.return_value = {'id': 1, 'name': 'Test Item'}

        # Викликаємо метод
        result = self.repository.get_item_by_id(1)

        # Перевіряємо результати
        self.mock_db.get.assert_called_once_with(1)
        self.assertEqual(result, {'id': 1, 'name': 'Test Item'})

    def test_add_item(self):
        # Тестовий об'єкт
        item = {'id': 2, 'name': 'New Item'}

        # Викликаємо метод
        self.repository.add_item(item)

        # Перевіряємо, що методи бази даних викликані правильно
        self.mock_db.add.assert_called_once_with(item)
        self.mock_db.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
