from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class ShopInfoMixin(models.Model):
    slug = models.SlugField(max_length=50, verbose_name='Short Name')
    is_active = models.BooleanField(default=True, verbose_name='Is it active?')

    class Meta:
        abstract = True


class Category(ShopInfoMixin):
    title = models.CharField(max_length=100, verbose_name='Category Title')
    description = RichTextField(verbose_name='Category Description')
    games_amount = models.IntegerField(default=0, verbose_name='Games Amount In Category')

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


class Game(ShopInfoMixin):
    name = models.CharField(max_length=100, verbose_name='Game Name')
    pub_date = models.DateField(auto_now_add=True, verbose_name='Game publication date')
    release_date = models.DateField(auto_now_add=False, verbose_name='Release date')
    price = models.DecimalField(verbose_name='Game Price', max_digits=5, max_length=4, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name='Game Category', on_delete=models.SET_DEFAULT,
                                 default=Category.get_default_category_pk, null=True)
    description = RichTextField(verbose_name='Game Description')
    game_image = models.ImageField(verbose_name='Game Image', upload_to='shop')

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        indexes = [models.Index(fields=['name'], name='name_asc_idx'),
                   models.Index(fields=['-name'], name='name_desc_idx'),
                   models.Index(fields=['-price'], name='price_asc_idx'),
                   models.Index(fields=['price'], name='price_desc_idx')]

    def __str__(self):
        return f"{self.name}"
