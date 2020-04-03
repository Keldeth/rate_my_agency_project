from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length = 30, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Cities'
        
    def __str__(self):
        return self.name



class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 30, null=True)
    last_name = models.CharField(max_length = 30, null=True)
    
    def __str__(self):
        return self.user.username

class Agency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agencyName = models.CharField(max_length = 30)
    # no on_delete here, to make it work:
    cities = models.ManyToManyField(City)
    website = models.URLField(null = True)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.agencyName)
        super(Agency, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Agencies'

    def __str__(self):
        return self.user.username


class Image(models.Model):
    image = models.ImageField(upload_to='agency_images/', blank=True, null=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    

# I've written this as being one individual like/dislike rating, left by one person.
# Hence why it's linked through a foreign key to one agency profile; I thought we could
# average out all the individual ratings on the actual profile page rather than store a % in the DB?
class Rating(models.Model):
    like = models.BooleanField()
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

class Comment(models.Model):
    commentText = models.CharField(max_length=300)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)



# Left out toStrings of rating and agency as unsure of syntax.
# Should they read "USER1 commented on AGENCY1"?
