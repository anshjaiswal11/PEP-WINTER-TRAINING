from django.db import models
from django.contrib.auth.hashers import make_password, check_password, identify_hasher

class user(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  # password = models.CharField(max_length=255)
  def __str__(self):
    return f"{self.firstname} {self.lastname} {self.password}"
  


class formModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # last_modified = models.DateTimeField(auto_now=True)
    # img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    

class LoginUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password: str)->None:
       """hash raw pass"""
       self.password = make_password(raw_password)

    def check_password(self, raw_password: str)->bool:
        """check if the hash of the raw password matches the stored hash"""
        return check_password(raw_password, self.password)
    
    def save(self, *args, **kwargs):
       try:
          identify_hasher(self.password)
       except ValueError:
          self.set_password(self.password)
       super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} {self.password}"



class SignUp(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password: str)->None:
       """hash raw pass"""
       self.password = make_password(raw_password)

    def check_password(self, raw_password: str)->bool:
        """check if the hash of the raw password matches the stored hash"""
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
       try:
          identify_hasher(self.password)
       except ValueError:
          self.set_password(self.password)
       super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} {self.password} {self.email}"