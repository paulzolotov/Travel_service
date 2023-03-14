from locust import task, FastHttpUser, between
import random
import requests as r


available_categories = ['action', 'RPG']
available_games = ['cyberpunk_2077', 'the_witcher_3', 'gta_v', 'the_last_of_us', 'god_of_war']

# locust --master -f locust_.py
# locust --worker --master-host=0.0.0.0 -f locust_.py
# go to
# http://0.0.0.0:8089

base_url = 'http://127.0.0.1:8000'
response = r.post("/users/login/", {"username": "admin", "password": "1"})
print(response.status_code)


class ShopUser(FastHttpUser):
    """Имитированный пользователь/
    @task(4) - цифра обозначает количество переходов от пользователей на данную страницу
    between(1, 5) - """
    wait_time = between(1, 5)

    @task(4)
    def view_main(self):
        """Имитация загрузки главной страницы"""
        self.client.get('/shop/', name='view_main')

    @task(4)
    def view_categories(self):
        """Имитация загрузки страницы с категориями"""
        self.client.get('shop/categories/', name='view_categories')

    @task(4)
    def view_one_category(self):
        """Имитация загрузки страницы любой категории"""
        category = random.choice(available_categories)
        self.client.get(f'shop/{category}/', name='view_one_category')

    @task(4)
    def view_one_game(self):
        """Имитация загрузки страницы любой игры"""
        for _ in range(3):
            game = random.choice(available_games)
            self.client.get(f'shop/game/{game}/', name='view_one_game')

    @task(4)
    def login(self):
        """Имитация входа пользователем на ресурс"""
        self.client.post("users/login/", {"username": "admin", "password": "1"})

    @task(4)
    def logout(self):
        """Имитация выхода пользователем на ресурс"""
        self.client.post("users/logout/", {"username": "alex100", "password": "karate007"})
