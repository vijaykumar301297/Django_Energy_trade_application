from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from company.models import Parent, Client


class AccountManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, email, username, role, password, **extra_fields):
        values = [email, username]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            role=role,
            # parent_role = parent_role,
            # client_role= client_role,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, username, role, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, username, role, password, **extra_fields)
    
    def create_superuser(self, email, username, role, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(email, username, role, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=50)
    parent_role = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='parent_id', null=True,
                                    default=False)
    client_role = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_data', null=True,
                                    default=False)
    password = models.CharField(max_length=400, null=True)
    # date_of_birth = models.DateField(blank=True, null=True)
    # picture = models.ImageField(blank=True, null=True)
    account_status = models.CharField(max_length=10, null=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)
    
    objects = AccountManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role']
    
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username.split()[0]
