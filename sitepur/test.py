from django.test import TestCase
from user.models import User
from django.test import TestCase
from user.models import Order
# Класс для тестов модели пользователя
class OrderModelTest(TestCase):
    @classmethod
    # Создание тестового пользователя
    def setUpTestData(cls):
        User.objects.create(email='', phone='+79091239203', first_name='Ivan', last_name='Maximov')
    # Тестирование поля имени пользователя
    def test_first_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'Имя')

    # Тестирование поля почты пользователя
    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    # Тестирование максимальной длины поля имени пользователя
    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)

    # Тестирование двух полей пользователя
    def test_object_name_is_last_name_comma_first_name(self):
        user = User.objects.get(id=1)
        expected_object_name = 'test123@mail.ru'
        self.assertEquals(expected_object_name, str(user))
