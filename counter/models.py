from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone



class ChartScannerReview(models.Model):
    nickname = models.CharField(max_length=50)  # 유저 닉네임
    comment = models.TextField()               # 리뷰 본문
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 일시 (자동 저장)

    def __str__(self):
        return f"{self.nickname} - {self.comment[:20]}"

# Create your models here.

class FileLog(models.Model):
    ip_address=models.GenericIPAddressField(default='0.0.0.0',null=True, blank=True) #default 추가
    timestamp=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    status=models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return f"{self.ip_address} - {self.status} at {self.timestamp}"

class review(models.Model):

    def __str__(self):
        return f"{self.ip_address} - {self.status}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='blog_images/',null=True, blank=True)
    comments_count = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):

        if not self.slug:

            base_slug = slugify(self.title)
            if not base_slug:
                base_slug = 'post'
            slug = base_slug
            num = 1
            while BlogPost.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        if not self.image:
            self.image = 'blog_images/default.jpeg'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})