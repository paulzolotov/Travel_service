from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Category Title')
    slug = models.SlugField(max_length=50, verbose_name='Category Slug')
    description = models.TextField(verbose_name='Category Description')
    is_active = models.BooleanField(default=True, verbose_name='Category is active?')

    @classmethod
    def get_default_category_pk(cls):
        """Необходим для значений по default"""
        category, created = cls.objects.get_or_create(
            title='Default',
            slug='default',
            description='default description',
            is_active=False
        )
        return category.pk

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.title}"


class Game(models.Model):
    name = models.CharField(max_length=100, verbose_name='Game Name')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Game publication date')
    release_date = models.DateTimeField(auto_now_add=False, verbose_name='Release date')
    price = models.DecimalField(verbose_name='Game Price', max_digits=5, max_length=4, decimal_places=2)
    slug = models.SlugField(max_length=50, verbose_name='Game Slug')
    category = models.ForeignKey(Category, verbose_name='Game Category', on_delete=models.SET_DEFAULT,
                                 default=Category.get_default_category_pk, null=True)
    description = models.TextField(verbose_name='Game Description')
    game_image = models.ImageField(verbose_name='Game Image', upload_to='shop')
    is_active = models.BooleanField(default=True, verbose_name='Game is active?')

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        return f"{self.name}"
