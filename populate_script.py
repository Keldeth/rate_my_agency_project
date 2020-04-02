import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rate_my_agency_project.settings')

from django.core.files.images import ImageFile
# commenting to test changes

import django
django.setup()
from rate_my_agency.models import City, Tenant, Agency, Rating, Comment, Image
from django.contrib.auth.models import User

def populate():
        #Create a superuser out of laziness
        #User.objects.create_superuser(username="admin",email="admin@example.com",password="wad123")
        
        #CITIES
        '''######################'''
	#create and add the cities
        cities = ["Glasgow", "Edinburgh", "Dundee", "Aberdeen", "Inverness"]
        for city in cities:
                add_city(city)

        print("Added 5 cities")
	
        #TENANTS
        '''######################'''
        #Create tenant users and add them to the database
        user1 = User.objects.get_or_create(username='john',email='john@gmail.com')[0]
        user2 = User.objects.get_or_create(username='emma',email='emma@gmail.com')[0]
        user3 = User.objects.get_or_create(username='jane',email='jane@gmail.com')[0]
        user4 = User.objects.get_or_create(username='sam',email='sam@gmail.com')[0]
	
        tenant_users = [user1, user2, user3, user4]
        tenants = []
        
        
        for tenant in tenant_users:
                tenant.set_password('11')
                tenant.save()
                tenants.append(add_tenant(tenant))

        print("Added 4 tenants")
	
        #RATINGS
        '''######################'''
        # Ratngs are created per agency and then added at the same time as agencies are added to the DB (see lines 65-89)
        cairn_ratings = [{'like':True,'tenant':tenants[0]},
					 {'like':False,'tenant':tenants[1]},
					 {'like':True,'tenant':tenants[2]}]
					 
        letsDirect_ratings = [{'like':True,'tenant':tenants[0]},
						  {'like':False,'tenant':tenants[1]},
						  {'like':True,'tenant':tenants[2]}]
        letsrus_ratings = [{'like':True,'tenant':tenants[0]},
					   {'like':False,'tenant':tenants[1]},
					   {'like':True,'tenant':tenants[2]}]
        foleys_ratings = [{'like':True,'tenant':tenants[0]},
					  {'like':False,'tenant':tenants[1]},
					  {'like':True,'tenant':tenants[2]}]

        #COMMENTS
        '''######################'''
        # Comments are created per agency and then added at the same time as agencies are added to the DB (see lines 65-89)
        cairn_comms = [{'text':'Great agency!','tenant':tenants[0]},
					 {'text':'Not helpful.','tenant':tenants[1]},
					 {'text':'Amazing!','tenant':tenants[2]}]
					 
        letsDirect_comms = [{'text':'Great agency!','tenant':tenants[0]},
						  {'text':'Not helpful.','tenant':tenants[1]},
						  {'text':'Amazing!','tenant':tenants[2]}]
        letsrus_comms = [{'text':'Great agency!','tenant':tenants[0]},
					   {'text':'Not helpful.','tenant':tenants[1]},
					   {'text':'Amazing!','tenant':tenants[2]}]
        foleys_comms = [{'text':'Great agency!','tenant':tenants[0]},
					  {'text':'Not helpful.','tenant':tenants[1]},
					  {'text':'Amazing!','tenant':tenants[2]}]
		
        #IMAGES
        '''######################'''
        cairn_imgs = ['cairn_flat.jpg','cairn_flat2.jpg']
        letsDirect_imgs = ['letsDirect_flat.jpg']
        letsrus_imgs = ['letsrus_flat.jpg']
        foleys_imgs = ['foleys_flat.jpg']
        
        
        #AGENCIES
        '''######################'''	
        #create agency users
        cairn_user = User.objects.get_or_create(username='cairn',email='cairn@gmail.com')[0]
        letsDirect_user = User.objects.get_or_create(username='letsDirect',email='letsdirect@gmail.com')[0]
        letsrus_user = User.objects.get_or_create(username='letsrus',email='letsrus@gmail.com')[0]
        foleys = User.objects.get_or_create(username='foleys',email='foleys@gmail.com')[0]
        
	
        #Create and add the agencies, with different amounts of cities each
        agencies = [{'user':cairn_user, 'agencyName':'Cairn Letting', 'website':'www.cairn.co.uk', 'cities':[City.objects.get(name="Glasgow"),City.objects.get(name="Dundee")],'ratings':cairn_ratings, 'comments': cairn_comms, 'images':cairn_imgs},
				{'user':letsDirect_user, 'agencyName':'Lets Direct', 'website':'www.letsdirect.co.uk', 'cities':[City.objects.get(name="Edinburgh")],'ratings':letsDirect_ratings, 'comments': letsDirect_comms,'images':letsDirect_imgs},
				{'user':letsrus_user, 'agencyName':'Lets R Us', 'website':'www.letsrus.co.uk','cities':[City.objects.get(name="Aberdeen"),City.objects.get(name="Inverness")],'ratings':letsrus_ratings, 'comments': letsrus_comms,'images':letsrus_imgs},
				{'user':foleys, 'agencyName':"Foley's", 'website':'www.foleys.co.uk','cities':[City.objects.get(name="Glasgow")],'ratings':foleys_ratings, 'comments': foleys_comms,'images':foleys_imgs}]
	
        for agency in agencies:
                agency['user'].set_password('11')
                agency['user'].save()
                a = add_agency(agency['user'], agency['agencyName'], agency['website'])
                
                for city in agency['cities']:
                        a.cities.add(city)
                for rating in agency['ratings']:
                        add_rating(rating['like'],rating['tenant'],a)
                for comment in agency['comments']:
                        add_comment(comment['text'],comment['tenant'], a)
                for image in agency['images']:
                        add_image(image, a)
                        
        print("Added 4 agencies")
        print("Added 12 ratings")
        print("Added 12 comments")
        print("Added 5 images")


#ADD TO DATABASE FUNCTIONS	
'''########################################################'''
	
def add_rating(like,tenant,agency):
	r = Rating.objects.get_or_create(like = like, tenant = tenant, agency = agency)[0]
	r.save()
	return r

def add_comment(text, tenant, agency):
	comm = Comment.objects.get_or_create(commentText = text, tenant = tenant, agency = agency)[0]
	comm.save()
	return comm
	
def add_city(name):
	c = City.objects.get_or_create(name = name)[0]
	c.save()
	return c
	
def add_agency(user, agencyName, website):
	a = Agency.objects.get_or_create(user = user, agencyName = agencyName, website = website)[0]
	a.save()
	return a
	
def add_tenant(user):
	t = Tenant.objects.get_or_create(user = user)[0]
	t.save()
	return t

def add_image(picNAME, agency):
    i = Image.objects.create(agency = agency)
    i.image = ImageFile(open(os.path.join('populate_images',picNAME), 'rb'))
    i.save()
    return i


#Main
if __name__ == '__main__':
	print('Starting rma population script')
	populate()
