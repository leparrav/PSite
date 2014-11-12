from django.db import models

class Tag(models.Model):
	word = models.CharField(max_length=36)
	views = models.PositiveIntegerField(default=0)
	def __unicode__(self):
		return self.word

class Category(models.Model):
	title = models.CharField(max_length=36)
	views = models.PositiveIntegerField(default=0)
	def __unicode__(self):
		return self.title

class Post(models.Model):
	title = models.CharField(max_length=128)
	text = models.TextField()
	date = models.DateField()
	pic = models.ImageField(upload_to="post_images") # For top banner only, text can have image with markdown
	views = models.PositiveIntegerField(default=0)
	tag = models.ManyToManyField(Tag)
	category = models.ForeignKey(Category)
	def __unicode__(self):
		return self.title

class Comment(models.Model):
	author = models.CharField(max_length=36)
	text = models.CharField(max_length=512)
	date = models.DateField()
	def __unicode__(self):
		return self.author

class Comment_response(models.Model):
	author = models.CharField(max_length=36)
	text = models.CharField(max_length=512)
	date = models.DateField()
	comment = models.ForeignKey(Comment)
	def __unicode__(self):
		return self.author

class Quote(models.Model):
	author = models.CharField(max_length=72)
	text = models.TextField()
	def __unicode__(self):
		return self.author