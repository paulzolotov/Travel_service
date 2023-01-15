from django.db import models
from django.core.validators import RegexValidator, EmailValidator


class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    login = models.CharField(max_length=60, validators=[
        RegexValidator(
            regex=r'^\b\w{6,10}\b$',  # взял с hw13 ex3
            message='Введите корректный login',
        )])
    email = models.CharField(max_length=60, validators=[
        EmailValidator(
            message='Введите корректный email'
        )])
    register_date = models.DateTimeField(auto_now_add=True)  # При добавлении новой записи, записывается текущая дата, и
                                                             # потом уже не меняется

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    category_title = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.category_title}"


class Posts(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=30)
    data_created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)
    post_author_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title}/{self.data_created}/{self.post_category_id}"
