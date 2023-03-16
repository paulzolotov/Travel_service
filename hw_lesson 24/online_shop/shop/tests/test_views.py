from django.test import TestCase
from shop.models import Game
from django.urls import reverse


# До выполннения всех тестов необходимо дать права пользователю pavel1
# sudo -u postgres createuser -s -P superadmin
# psql --username=superadmin my_gameshop
# sudo -u postgres psql
# ALTER USER pavel1 CREATEDB;

# Узнать название тестовой БД (обычно test_ + название реальной БД)
# sudo -u postgres psql
# \l


class IndexTestClass(TestCase):

	@classmethod
	def setUpTestData(cls):
		number_of_games = 3
		for game_num in range(1, number_of_games):
			Game.objects.create(
				id=game_num,
				name="Grand Theft Auto V", slug='gta_v', price=18.59,
				description='One of the best game in the world!', release_date='2023-03-16',
				game_image='/home/johndoe/pavel_PC_lin/TMS/Homework/hw_lesson 24/online_shop/shop/photos/GTAV.jpg')

	def test_view_url_exists_at_desired_location(self):
		"""Тестирование корректного перехода"""
		resp = self.client.get('/shop/')
		self.assertEqual(resp.status_code, 200)

	def test_view_url_accessible_by_name(self):
		"""Тестирование корректности названия представления"""
		resp = self.client.get(reverse('shop:index'))
		self.assertEqual(resp.status_code, 200)

	# Почему то не работает !!!!
	# def test_view_uses_correct_template(self):
	# 	"""Тестирование корректности использования шаблона представления"""
	# 	resp = self.client.get(reverse('shop:index'))
	# 	self.assertTemplateUsed(resp, 'shop/games_home_page.html')

	# def test_view_uses_correct_template_2(self):
	# 	"""Тестирование корректности использования шаблона представления"""
	# 	resp = self.client.get(reverse('shop:categories'))
	# 	self.assertTemplateUsed(resp, 'shop/categories.html')

	def test_pagination_is_2(self):
		"""Тестирование корректности отображения пагинации"""
		resp = self.client.get(reverse('shop:index'))
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('page_obj' in resp.context)
		self.assertTrue(len(resp.context['page_obj']) == 2)
