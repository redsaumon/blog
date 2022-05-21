from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name, phone_number, password=None):
        """
        Creates and saves a User with the given information.
        """
        if not email:
            raise ValueError('must have email')
        if not name:
            raise ValueError('must have name')
        if not phone_number:
            raise ValueError('must have phone_number')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_number, password):
        """
        Creates and saves a superuser with the given email, password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            phone_number=phone_number,
            password=password
        )

        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(max_length=50, blank=False, unique=True)
    name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=100, blank=False, unique=True)
    is_active = models.BooleanField(default=True, verbose_name="active")
    is_staff = models.BooleanField(default=False, verbose_name="staff")
    is_admin = models.BooleanField(default=False, verbose_name="admin")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'name']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name