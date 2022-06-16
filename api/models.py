from django.db import models


class Post(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='blog/%Y/%m/', blank=True, null=True)
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    like = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'posts'
        ordering = ('update_dt',)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'