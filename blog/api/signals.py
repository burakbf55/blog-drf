# def save(self, *args, **kw):
#         if not self.id:
#             self.created = timezone.now()
#             self.slug = self.get_slug()
#         else:
#             orig = Post.objects.get(pk=self.pk)
#             if orig.title != self.title:
#                 self.slug = self.get_slug()
#         self.modified = timezone.now()

#         return super(Post, self).save(*args, **kwargs)


#  def get_slug(self):
#         slug = slugify(self.title.replace("ı", "i"))
#         unique = slug
#         number = 1
#         while Post.objects.filter(slug=unique).exists():
#             unique = '{}-{}'.format(slug, number)
#             number += 1
#         return unique

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.created = timezone.now()
#         self.modified = timezone.now()
#         self.slug = self.get_slug()

#         return super(Post, self).save(*args, **kwargs)
