from django.db import models


# class FAQ(models.Model):
#     question_uz = models.TextField(max_length=1000, null=True, blank=True)
#     question_ru = models.TextField(max_length=1000, null=True, blank=True)
#     question_en = models.TextField(max_length=1000, null=True, blank=True)
#     answer_uz = models.TextField(max_length=1000, null=True, blank=True)
#     answer_ru = models.TextField(max_length=1000, null=True, blank=True)
#     answer_en = models.TextField(max_length=1000, null=True, blank=True)

    
class About(models.Model):
    about_uz = models.TextField(max_length=2000, null=True, blank=True)
    about_ru = models.TextField(max_length=2000, null=True, blank=True)
    about_en = models.TextField(max_length=2000, null=True, blank=True)
    link = models.URLField(null=True)
    

# class Gallery(models.Model):
#     photo = models.ImageField(null=True)
#     video = models.FileField(null=True)


# class Blog(models.Model):
#     name_uz = models.CharField(max_length=200, null=True, blank=True)
#     name_ru = models.CharField(max_length=200, null=True, blank=True)
#     name_en = models.CharField(max_length=200, null=True, blank=True)
#     text_uz = models.TextField(max_length=2000, null=True, blank=True)
#     text_ru = models.TextField(max_length=2000, null=True, blank=True)
#     text_en = models.TextField(max_length=2000, null=True, blank=True)
#     photo = models.ImageField(null=True)
#     date = models.DateField(auto_now_add=False, null=True)
#     author = models.CharField(max_length=200, null=True, blank=True)
    

# class Rate(models.Model):
#     class Priorities(models.IntegerChoices):
#         LOW = 1, '⭐️'
#         EASY = 2, '⭐️⭐️'
#         MEDIUM = 3, '⭐️⭐️⭐️'
#         HIGH = 4, '⭐️⭐️⭐️⭐️'
#         URGENT = 5, '⭐️⭐️⭐️⭐️⭐️'
        
#     comment_uz = models.CharField(max_length=200, null=True, blank=True)
#     comment_ru = models.CharField(max_length=200, null=True, blank=True)
#     comment_en = models.CharField(max_length=200, null=True, blank=True)
#     rate = models.IntegerField(default=Priorities.URGENT, choices=Priorities.choices)
#     author = models.CharField(max_length=200, null=True, blank=True)
#     image = models.ImageField(null=True, blank=True)


class Slider(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    background = models.ImageField(null=True, blank=True)


class Infographic(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    number = models.IntegerField(default=0)


class ReviewClient(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    text_uz = models.CharField(max_length=200, null=True, blank=True)
    text_ru = models.CharField(max_length=200, null=True, blank=True)
    text_en = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now_add=False)
  
    
class ReviewFamous(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    text_uz = models.CharField(max_length=200, null=True, blank=True)
    text_ru = models.CharField(max_length=200, null=True, blank=True)
    text_en = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now_add=False)


class Partner(models.Model):
    image = models.ImageField(null=True)



class News(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True)
    image = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    views = models.IntegerField(default=True)


class Blog(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    

#class Partner(models.Model):
#    name_uz = models.CharField(max_length=200, null=True, blank=True)
#    name_ru = models.CharField(max_length=200, null=True, blank=True)
#    name_en = models.CharField(max_length=200, null=True, blank=True)
 #   image = models.ImageField(null=True, blank=True)
