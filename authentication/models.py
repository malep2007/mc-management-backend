from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager, 
    PermissionsMixin
)

class UserManager(BaseUserManager):

    def create_user(self, username, email, password, *args, **kwargs):
        """
        overriding defaulr usermanager class and overiding 
        the create_user
        """
        if username is None:
            raise TypeError("Users must have a username")
        
        if email is None:
            raise TypeError('Users must have an email address')
        
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password):
        """
        Create and dreturn `User` with super user status
        """

        if password is None:
            raise TypeError('Superuser must have password')
        
        user = self.create_user(self, username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return "{0} {1} {2}".format(self.first_name, self.middle_name,self.last_name)
    
    @property
    def get_short_name(self):
        return self.first_name


# class MCLeader(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=12)
#     church = models.CharField(max_length=20)
   
    

# Create your models here.
