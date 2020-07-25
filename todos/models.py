from django.contrib.auth import get_user_model
from django.db import models


class Todos(models.Model):

    todo = models.CharField("TODO", max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='user')

    def __str__(self):
        return self.todo
