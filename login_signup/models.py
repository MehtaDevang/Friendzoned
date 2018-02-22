from django.db import models

# Create your models here.

class OurUsers(models.Model):
    name = models.CharField(max_length=30, null=False)
    dob = models.DateField(null=False)
    username = models.EmailField(max_length=50, primary_key=True, null=False)
    password = models.CharField(max_length=20, null=False)
    friends = models.ManyToManyField('self', null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return str(self.username)

class Friend_Requests(models.Model):
    request_from = models.OneToOneField(OurUsers, null=False)
    request_to = models.EmailField(max_length=50, null=False)

    def __str__(self):
        return str('{}-{}'.format(self.request_from, self.request_to))

class Message(models.Model):
    message_to = models.EmailField(max_length=50, null=False)
    message_from = models.ForeignKey(OurUsers, null=False)
    message = models.TextField(max_length=2000, null=False)
    message_time = models.DateTimeField()

    def __str__(self):
        return str('{}-{}'.format(self.message_from, self.message_to))

class Post(models.Model):
    post_id = models.IntegerField(auto_created=True, null=False, blank=False, primary_key=True, default=20)
    posted_by = models.OneToOneField(OurUsers, null=False)
    post = models.TextField(max_length=1000, null=False)
    post_time = models.DateTimeField()

    class Meta:
        db_table = 'Post'
        unique_together = ('posted_by', 'post_time')

    def __str__(self):
        return str('{}-{}'.format(self.posted_by, self.post_time))


class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    comment_time = models.DateTimeField()
    comment_by = models.EmailField(null=False)
    comment_id = models.IntegerField(primary_key=True, null=False, blank=False)

    def __str__(self):
        return str('{}-{}'.format(self.comment_by, self.comment_time))