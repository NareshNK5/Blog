from django.db import models


class Tbluser(models.Model):
    username = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    contact_no = models.CharField(max_length=50, blank=True, null=True)
    mailid = models.CharField(max_length=50, blank=True, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)


class Tblpost(models.Model):
    author = models.ForeignKey("Tbluser", related_name='for_auther', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    images = models.FileField(upload_to='images/', max_length=100 , blank=True, null=True)
    content = models.TextField()
    is_active = models.IntegerField(default=0)
    publication_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

class Tblrate(models.Model):
    author = models.ForeignKey("Tbluser", related_name='for_auther_rate', on_delete=models.CASCADE)
    post = models.ForeignKey("Tblpost", related_name='for_post_rate', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    
    