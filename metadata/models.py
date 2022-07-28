from django.db import models
from django.core.validators import MinLengthValidator


class Contact(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(
            2, "Name must be greater than 2 characters")]
    )
    email = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.text) < 15:
            return self.text
        return self.text[:11] + ' ...'
