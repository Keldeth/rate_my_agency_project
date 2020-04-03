from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# City model with a unique name, and slug derived from that name
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


# Tenant model which has a one-to-one relationship with the User model, i.e. any one tenant represents one User
# Takes first and last names as fields
class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 30, null=True)
    last_name = models.CharField(max_length = 30, null=True)
    
    def __str__(self):
        return self.user.username

# Agency model, also has a one-to-one relationship with User. Contains a unique agencyName,
# any cities it is based in, a website URL, and a slug based on the agencyName
class Agency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agencyName = models.CharField(max_length = 30, unique=True)
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


# Image model which has a many-to-one relationship with a given agency, and stores one of the images the agency page will display
# These images are stored in the media folder, in a nested folder called agency_images
class Image(models.Model):
    image = models.ImageField(upload_to='agency_images/', blank=True, null=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    
# Rating model: the model of a rating left by one tenant on one agency's page. Has a many-to-one relationship with tenant and agency.
# The like field is true if the tenant clicked "like", and false if they clicked "dislike"
class Rating(models.Model):
    like = models.BooleanField()
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

# Comment model: the model of a comment left by one tenant on one agency's page. Has a many-to-one relationship with tenant and agency.
# Contains the text submitted by a user
class Comment(models.Model):
    commentText = models.CharField(max_length=300)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

