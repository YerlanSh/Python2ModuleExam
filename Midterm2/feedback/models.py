from django.db import models

# Create your models here.
# Создание модели для хранения данных обратной связи, включая поля для имени пользователя,
# адреса электронной почты, сообщения и даты отправки.

class Feedback(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} - {self.date}'

# Модель для котов и собак

class Pet(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

