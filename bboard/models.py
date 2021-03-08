from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, verbose_name='Никнейм', unique=True, db_index = True)
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    password1 = models.CharField(max_length=30, verbose_name='Пароль_1')
    password2 = models.CharField(max_length=30, verbose_name='Пароль_2')
    is_active = models.BooleanField(default = True, verbose_name='Онлайн')

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name_plural="Пользователи"
        verbose_name='Пользователь'
        ordering=['username']

    def create(self, validated_data):
        user=get_user_model().objects.create(
        username = validated_data['username']
    )

        user.set_password(validated_data['password'])
        user.save()
        return user

        
class Bb(models.Model):
    title=models.CharField(max_length=250, verbose_name='Товар')
    content=models.TextField(null = True, blank = True, verbose_name='Описание')
    price = models.FloatField(null=True, blank = True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add = True, db_index = True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, blank = True, on_delete=models.PROTECT, verbose_name='Рубрика')
    author = models.ForeignKey('CustomUser', null = True, blank = True, on_delete=models.PROTECT, verbose_name = "Автор", editable = False, auto_created= True, to_field="username")

    class Meta:
        verbose_name_plural="Объявления"
        verbose_name="Объявление"
        ordering=['-published']

    def __str__(self):
        return self.title

    # def save(self, request,  commit=True):
    #     bb = super().save(commit=False)
    #     if not bb.pk:
    #         bb.author = get_user(self.request)
    #     if commit:
    #         b.save()
    #         self.save_m2m()
    #     return bb

class Rubric(models.Model):
    name=models.CharField(max_length=20, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name_plural="Рубрики"
        verbose_name='Рубрика'
        ordering=['name']

    def __str__(self):
        return self.name

