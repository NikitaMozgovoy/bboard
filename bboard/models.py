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
    title=models.CharField(verbose_name='Товар', max_length=250, null= False, blank = False, default = '', )
    content=models.TextField(verbose_name='Описание', null = False, blank = False, default='', )
    price = models.FloatField(verbose_name='Цена', null=False, blank = False, default=0)
    published = models.DateTimeField(auto_now_add = True, verbose_name='Опубликовано', db_index = True)
    rubric = models.ForeignKey('Rubric', verbose_name='Рубрика', null=True, blank = False, on_delete=models.PROTECT)
    author = models.CharField(max_length=30, verbose_name = "Автор", null=False, default="Пользователь")
    image = models.ImageField(upload_to='images/ads', editable=True, null = False, blank=False)
    phone = models.CharField(verbose_name="Мобильный телефон" ,max_length=20, null=True, blank=False)
    place = models.CharField(verbose_name="Адрес", max_length=80, null=True, blank=False)

    class Meta:
        verbose_name_plural="Объявления"
        verbose_name="Объявление"
        ordering=['-published']

    def __str__(self):
        return self.title


class Rubric(models.Model):
    name=models.CharField(max_length=20, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name_plural="Рубрики"
        verbose_name='Рубрика'
        ordering=['name']

    def __str__(self):
        return self.name

