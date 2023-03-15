from django.test import TestCase

from shop.models import Comment


class TrialTests(TestCase):

	@classmethod
	def setUpTestData(cls):
		"""Выполняется перед запуском всех тестов конкретного класса"""
		cls.comment = Comment.objects.create(text="Good game! I recommend to everyone! ", rating=10)

	def setUp(self):
		"""Выполняется перед запуском каждого теста"""
		pass

	def tearDown(self):
		"""Выполняется после завершения каждого теста"""
		pass

	def test_text_verbose_name(self):
		"""Функция, проверяющая название параметра verbose_name атрибута Комментария - text"""
		real_verbose_name = getattr(self.text, 'verbose_name')  # У комментария есть атрибут text,
		# а у него есть параметр verbose_name - строчное название атрибута
		expected_verbose_name = "Comment text"
		self.assertEqual(real_verbose_name, expected_verbose_name)  # assertEqual - предполагает, что аргументы одинаковы

	def test_max_length(self):
		"""Функция, проверяющая длину параметра max_length атрибута Комментария - text"""
		real_max_length = getattr(self.text, 'max_length')
		self.assertEqual(real_max_length, 100)

	def test_rating_verbose_name(self):
		"""Функция, проверяющая название параметра verbose_name атрибута Комментария - text"""
		real_verbose_name = getattr(self.text, 'verbose_name')
		expected_verbose_name = "Comment text"
		self.assertEqual(real_verbose_name, expected_verbose_name)
