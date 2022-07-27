from django.db import models

# Create your models here.
class wxUser(models.Model):
    openid = models.CharField(max_length=64, primary_key=True)
    session_key = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    avatar = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now_add=True)
    create_ip = models.CharField(max_length=64)
    token = models.CharField(max_length=64)

    def __str__(self):
        return self.nickname + ' (' + self.openid + ')'

class wxUserLog(models.Model):
    openid = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now_add=True)
    create_ip = models.CharField(max_length=64)
    action = models.CharField(max_length=64)
    action_detail = models.CharField(max_length=64)

    def __str__(self):
        return self.action + ' (' + self.openid + ')'

    def last_action(self):
        return self.objects.filter(openid=self.openid).order_by('-create_time')[0]
