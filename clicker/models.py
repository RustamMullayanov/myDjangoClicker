from django.db import models
from django.contrib.auth.models import User


class Clicker(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    click_power = models.IntegerField(default=1)
    blood_score = models.IntegerField(default=0)
    user_level = models.IntegerField(default=0)

    def level_up(self):
        if self.blood_score > self.user_level:
            self.user_level += 1
            return True
        return False
