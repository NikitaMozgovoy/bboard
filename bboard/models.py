from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db.models.fields import EmailField

class UserManager(BaseUserManager):
    """
    Django требует, чтобы кастомные пользователи определяли свой собственный
    класс Manager. Унаследовавшись от BaseUserManager, мы получаем много того
    же самого кода, который Django использовал для создания User (для демонстрации).
    """

    def create_user(self, username, email, password=None):
        """ Создает и возвращает пользователя с имэйлом, паролем и именем. """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50, verbose_name='Никнейм', unique=True, db_index = True)
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    email=models.EmailField(max_length=64,verbose_name = "E-mail")
    password = models.CharField(max_length=30, verbose_name='Пароль')
    is_active = models.BooleanField(default = True, verbose_name='Онлайн')
    phone = models.CharField(max_length=30, verbose_name="Телефон", default="Номер не указан")
    is_superuser = models.BooleanField(default=False, null=False)
    is_staff = models.BooleanField(default=False, null=False)

    USERNAME_FIELD = "username"
    EmailField = "email"

    REQUIRED_FIELDS = ['email', 'password']

    objects=UserManager()

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
    phone = models.CharField(verbose_name="Мобильный телефон" , max_length=20, null=False, blank=False)
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

