import uuid
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def check_image(image):
    if image.size > 2 * 1024 * 1024:  # 限制最大 2MB
        raise ValidationError('文件大於2MB!')
    if not image.name.endswith(('.png', '.jpg', '.jpeg')):
        raise ValidationError('文件格式錯誤!')


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.title
    
class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(blank=True)
    user_picture = models.ImageField(upload_to='author_images/', blank=True)

    def __str__(self):
        return self.user.username
    
class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='tag_articles') # 反向查詢，藉由tags獲取article
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_articles') # 反向查詢，藉由author獲取article
    cover = models.ImageField(upload_to='cover/', validators=[check_image], blank=True)


    def __str__(self) -> str:
        return self.title
