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

    def __str__(self):
        return self.user.username

class Agency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Agencies'

    def __str__(self):
        return self.user.username
    
class AgencyProfile(models.Model):
    agency = models.OneToOneField(Agency, on_delete=models.CASCADE)
    url = models.URLField()

    #checking this one works:
    def __str__(self):
        #return self.agency.user.username
        return __str__(self.agency)

# I've written this as being one individual like/dislike rating, left by one person.
# Hence why it's linked through a foreign key to one agency profile; I thought we could
# average out all the individual ratings on the actual profile page rather than store a % in the DB?
class Rating(models.Model):
    like = models.BooleanField()
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    agency = models.ForeignKey(AgencyProfile, on_delete=models.CASCADE)

class Comment(models.Model):
    commentText = models.CharField(max_length=300)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    agency = models.ForeignKey(AgencyProfile, on_delete=models.CASCADE)

# Left out toStrings of rating and agency as unsure of syntax.
# Should they read "USER1 commented on AGENCY1"?
