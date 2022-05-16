from django.contrib.auth.base_user import BaseUserManager
from django.forms import ValidationError

class UserManager(BaseUserManager):

    def create_user(self, **extra_fields):

        try:
            email = extra_fields.pop('email')
        except:
            raise ValidationError('Email required field')

        try:
             password = extra_fields.pop('password')
        except:
            raise ValidationError('password required field')
        
        if not email:
            raise ValidationError('Email incorrect')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
        

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('email',email)
        extra_fields.setdefault('password',password)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(**extra_fields)