from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

# Will be used for authentication only as AUTH_MODELS=User, will create a separate model for more information

class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Create and return a `User` with an email, username and password.
        """
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin=True
        user.save()

        return user


class User(AbstractBaseUser):

    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email_address',
        max_length=255,
        unique=True
        )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True


class user_data(models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=15)
    password=models.CharField(max_length=100)
    grad_year=models.IntegerField()
    course=models.CharField(max_length=10)


    def __str__(self):
        return self.email

class user_validation(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=15)
    password=models.CharField(max_length=100)
    grad_year=models.IntegerField()
    course=models.CharField(max_length=10)
    token=models.CharField(max_length=100)

    def __str__(self):
        return self.email

class user_forgot_password(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100,default=None)
    token=models.CharField(max_length=100)

    def __str__(self):
        return self.email