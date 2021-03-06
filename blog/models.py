# Create your models here.
from blogcore.utils import unique_slug_generator
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from taggit.managers import TaggableManager

# User = get_user_model()


class BaseContent(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    # Abstract Class'da class meta deyip abstract = True atamamız lazım.
    class Meta:
        abstract = True


class Post(BaseContent):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = RichTextField()
    image = models.ImageField(
        "Gorsel",
        upload_to="post_images",
        default="not_found.jpg",
        blank=True,
    )
    # STATUSES = Choices('new', 'verified', 'published', 'draft')
    # status = models.IntegerField(choice=STATUSES, default=STATUSES.draft)

    def __str__(self) -> str:
        return str(self.author)

    # SİGNAL KULLANARAK OLUŞTUR
    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "post"

        verbose_name_plural = "posts"


class Comment(models.Model):
    parent = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"
        ordering = ["-created", "-updated"]

    # ordering ekle


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Post)
