from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg
from django.urls import reverse


# Create your models here.
class ShopInfoMixin(models.Model):
    """Класс Mixin, для повторяющихся полей, от которого затем наследуются классы с моделями"""
    slug = models.SlugField(max_length=50, verbose_name="Short Name")
    is_active = models.BooleanField(default=True, verbose_name="Is it active?")

    class Meta:
        abstract = True


class Category(ShopInfoMixin):
    """Класс для создания модели - Категория (игры)"""
    title = models.CharField(max_length=100, verbose_name="Category Title")
    description = RichTextField(verbose_name="Category Description")
    games_amount = models.IntegerField(
        default=0, verbose_name="Games Amount In Category"
    )

    @classmethod
    def get_default_category_pk(cls):
        """Необходим для значений по default"""
        category, created = cls.objects.get_or_create(
            title="Default",
            slug="default",
            description="default description",
            is_active=False,
        )
        return category.pk

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        """Возвращает удобочитаемую строку для каждого объекта.
        Эта строка используется для представления отдельных записей на сайте администрирования
        (и в любом другом месте, где нужно обратиться к экземпляру модели)"""
        return f"{self.title}"


class Game(ShopInfoMixin):
    """Класс для создания модели - Игра"""
    name = models.CharField(max_length=100, verbose_name="Game Name")
    pub_date = models.DateField(auto_now_add=True, verbose_name="Game publication date")
    release_date = models.DateField(auto_now_add=False, verbose_name="Release date")
    price = models.DecimalField(
        verbose_name="Game Price", max_digits=5, max_length=4, decimal_places=2
    )
    category = models.ForeignKey(
        Category,
        verbose_name="Game Category",
        on_delete=models.SET_DEFAULT,
        default=Category.get_default_category_pk,
        null=True,
    )
    description = RichTextField(verbose_name="Game Description")
    game_image = models.ImageField(verbose_name="Game Image", upload_to="shop")

    class Meta:
        """Добавил индексы для полей таблицы price и name"""
        verbose_name = "Game"
        verbose_name_plural = "Games"
        indexes = [
            models.Index(fields=["name"], name="name_asc_idx"),
            models.Index(fields=["-name"], name="name_desc_idx"),
            models.Index(fields=["-price"], name="price_asc_idx"),
            models.Index(fields=["price"], name="price_desc_idx"),
        ]

    def __str__(self):
        """Возвращает удобочитаемую строку для каждого объекта."""
        return f"{self.name}"

    def get_average_rating(self):
        """Функция для подсчета средней оценки игры по комментариям всех пользователей"""
        game_comments = self.comment_set.all()
        average_rating = game_comments.aggregate(Avg("rating"))
        return average_rating


class Comment(models.Model):
    """Класс для создания модели - Комментарий (для конкретной игры, от конкретного пользователя)"""
    text = models.CharField(max_length=300, verbose_name="Comment text")
    pub_date = models.DateField(
        verbose_name="Comment publication date", auto_now_add=True
    )
    rating = models.IntegerField(verbose_name="Comment rating")
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Возвращает удобочитаемую строку для каждого объекта."""
        return f"{self.text}"

    def get_absolute_url(self):
        """При изменении (добавлении или редактировании комментария) будет переход на страницу с игрой"""
        return reverse("shop:game", kwargs={"game_slug": self.game.slug})


class Log(models.Model):
    """Класс для создания модели - Лог (от конкретного пользователя)"""
    log_path = models.CharField(max_length=300, verbose_name="request path")
    log_user = models.CharField(max_length=100, verbose_name="request user")
    log_datetime = models.DateTimeField(
        verbose_name="Response datetime", auto_now_add=True
    )

    def __str__(self):
        """Возвращает удобочитаемую строку для каждого объекта."""
        return f"{self.log_path}"


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Basket creation datetime")

    def __str__(self):
        """Возвращает удобочитаемую строку для каждого объекта."""
        return f"Basket for {self.user} | Game: {self.game}"

    def total_sum(self):
        """Функция для подсчета общей суммы, которую необходимо заплатить за все игры в корзине"""
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.game.price for basket in baskets)

    def total_quantity(self):
        """Функция для подсчета общего количества всех игр в корзине"""
        baskets = Basket.objects.filter(user=self.user)
        return len(baskets)
