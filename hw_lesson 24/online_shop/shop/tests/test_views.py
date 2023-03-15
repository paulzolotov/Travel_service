from django.test import TestCase
from shop.models import Game
from django.urls import reverse


class IndexTestClass(TestCase):

	@classmethod
	def setUpTestData(cls):
		number_of_games = 3
		for game_num in range(number_of_games):
			Game.objects.create(text="game", price=10.5, description='One of the best game in the world!')

	def test_view_url_exists_at_desired_location(self):
		"""Тестирование корректного перехода"""
		resp = self.client.get('/shop/')
		self.assertEqual(resp.status_code, 200)

	def test_view_url_accessible_by_name(self):
		"""Тестирование корректности названия представления"""
		resp = self.client.get(reverse('shop:index'))
		self.assertEqual(resp.status_code, 200)

	def test_view_uses_correct_template(self):
		"""Тестирование корректности использования шаблона представления"""
		resp = self.client.get(reverse('shop:index'))
		self.assertTemplateUsed(resp, 'shop/games_home_page.html')

	def test_pagination_is_2(self):
		"""Тестирование корректности отображения пагинации"""
		resp = self.client.get(reverse('shop:index'))
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('page_obj' in resp.context)
		self.assertTrue(len(resp.context['page_obj']) == 2)
