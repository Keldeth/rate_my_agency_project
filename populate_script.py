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
        print("Adding 5 cities")
        for city in cities:
                add_city(city)
	
        #TENANTS
        '''######################'''
        #Create tenant users and add them to the database
        user0 = User.objects.get_or_create(username='jordyn',email='jordyn@gmail.com')[0]
        user1 = User.objects.get_or_create(username='john',email='john@gmail.com')[0]
        user2 = User.objects.get_or_create(username='emma',email='emma@gmail.com')[0]
        user3 = User.objects.get_or_create(username='jane',email='jane@gmail.com')[0]
        user4 = User.objects.get_or_create(username='sam',email='sam@gmail.com')[0]
        user5 = User.objects.get_or_create(username='tim',email='timmy@gmail.com')[0]
        user6 = User.objects.get_or_create(username='scott',email='scottie@gmail.com')[0]
        user7 = User.objects.get_or_create(username='sarah',email='sarahhh@gmail.com')[0]
	
        tenant_users = [user0, user1, user2, user3, user4, user5, user6, user7]
        tenants = []

        print("Adding 8 tenants")
        for tenant in tenant_users:
                tenant.set_password('11')
                tenant.save()
                tenants.append(add_tenant(tenant))
	
        #RATINGS
        '''######################'''
        # Ratngs are created per agency and then added at the same time as agencies are added to the DB (see lines 65-89)
        cairn_ratings = [{'like':True,'tenant':tenants[0]},
					 {'like':False,'tenant':tenants[1]},
					 {'like':True,'tenant':tenants[2]}]
					 
        letsDirect_ratings = [{'like':True,'tenant':tenants[0]},
						  {'like':False,'tenant':tenants[1]},
						  {'like':False,'tenant':tenants[2]}]
        letsrus_ratings = [{'like':True,'tenant':tenants[0]},
					   {'like':False,'tenant':tenants[1]},
					   {'like':True,'tenant':tenants[2]}]
        foleys_ratings = [{'like':False,'tenant':tenants[0]},
					  {'like':False,'tenant':tenants[1]},
					  {'like':True,'tenant':tenants[2]}]
        cairneys_ratings = [{'like':True, 'tenant':tenants[0]},
                            {'like':True, 'tenant':tenants[1]},
                            {'like':True, 'tenant':tenants[2]},
                            {'like':True, 'tenant':tenants[3]},
                            {'like':False, 'tenant':tenants[4]},
                            {'like':True, 'tenant':tenants[5]},
                            {'like':False, 'tenant':tenants[6]},
                            {'like':False, 'tenant':tenants[7]},]
        fontaine_ratings = [{'like':False, 'tenant':tenants[0]},
                            {'like':True, 'tenant':tenants[3]},
                            {'like':True, 'tenant':tenants[5]},
                            {'like':False, 'tenant':tenants[6]},
                            {'like':False, 'tenant':tenants[7]},]
        johnstone_ratings = [{'like':False, 'tenant':tenants[0]},
                             {'like':False, 'tenant':tenants[2]},
                             {'like':True, 'tenant':tenants[4]},
                             {'like':True, 'tenant':tenants[6]},]
        johnson_ratings = [{'like':True, 'tenant':tenants[0]},
                           {'like':True, 'tenant':tenants[1]},
                           {'like':True, 'tenant':tenants[2]},
                           {'like':False, 'tenant':tenants[3]},
                           {'like':True, 'tenant':tenants[4]},
                           {'like':True, 'tenant':tenants[6]},]
        

        #COMMENTS
        '''######################'''
        # Comments are created per agency and then added at the same time as agencies are added to the DB (see lines 65-89)
        cairn_comms = [{'text':'Great agency!','tenant':tenants[0]},
                       {'text':'Would definitely NOT recommend.','tenant':tenants[1]},
                       {'text':'Amazing!','tenant':tenants[2]},
                       {'text':'This company left me in crippling financial trouble', 'tenant':tenants[4]},
                       {'text':'Hope to rent with these folk again!', 'tenant':tenants[7]}]
					 
        letsDirect_comms = [{'text':'Bit annoying','tenant':tenants[0]},
                            {'text':'Not helpful.','tenant':tenants[1]},
                            {'text':'Incredibly helpful!', 'tenant':tenants[4]},
                            {'text':'Loved my place','tenant':tenants[2]},
                            {'text':'Great wee spot!', 'tenant':tenants[6]}]
        letsrus_comms = [{'text':'Very helpful','tenant':tenants[0]},
                         {'text':'Stay away from this agency!','tenant':tenants[1]},
                         {'text':'impressive','tenant':tenants[2]},
                         {'text':'muy interesante', 'tenant':tenants[5]},
                         {'text':'donde esta la biblioteca', 'tenant':tenants[5]}]
        foleys_comms = [{'text':'bravo','tenant':tenants[0]},
                        {'text':'Useless','tenant':tenants[1]},
                        {'text':'class man','tenant':tenants[2]},
                        {'text':'pure dead brilliant brer','tenant':tenants[7]},
                        {'text':'had a blast in my flat', 'tenant':tenants[3]},
                        {'text':'Well, at least the shower works', 'tenant':tenants[5]},
                        {'text':'ive never met a sweeter estate agent', 'tenant':tenants[4]},
                        {'text':'they stole my deposit :/', 'tenant':tenants[6]}]
        cairneys_comms = [{'text':'Not too shabby', 'tenant':tenants[5]},
                          {'text':'Decent business', 'tenant':tenants[7]},
                          {'text':'kinda liked it', 'tenant':tenants[3]},
                          {'text':'would not rent again', 'tenant':tenants[4]},
                          {'text':'would most certainly rent again', 'tenant':tenants[0]}]
        fontaine_comms = [{'text':'pretty standard', 'tenant':tenants[6]},
                          {'text':'place was a riot tbh', 'tenant':tenants[4]},
                          {'text':'is this teh comment section??', 'tenant':tenants[3]},
                          {'text':'anyone looking to organise a rent strike?', 'tenant':tenants[5]},
                          {'text':'rats, rats everywhere', 'tenant':tenants[2]}]
        johnstone_comms = [{'text':'Found quite a nice place here', 'tenant':tenants[1]},
                           {'text':'my place felt like a funeral home', 'tenant':tenants[2]},
                           {'text':'loved it here. except for the rats', 'tenant':tenants[6]},
                           {'text':'massive leak in my flat, but on the upside it meant i had some running water', 'tenant':tenants[3]},
                           {'text':'Land should not be owned privately.', 'tenant':tenants[0]},
                           {'text':'The lady that met with us was lovely :)', 'tenant':tenants[7]}]
        johnson_comms = [{'text':'Quite a cool wee place', 'tenant':tenants[7]},
                         {'text':'very interesting design', 'tenant':tenants[3]},
                         {'text':'They even provided us with board games!', 'tenant':tenants[5]},
                         {'text':'Normally quite hard to find a place for a family of 12, so this was a steal!', 'tenant':tenants[6]},
                         {'text':'Were the holes in the roof supposed to be skylights?', 'tenant':tenants[4]},
                         {'text':'A little insulation would have been nice...', 'tenant':tenants[2]},
                         {'text':'The doorframe was too small and I kept hitting my head', 'tenant':tenants[1]}]        
		
        #IMAGES
        '''######################'''
        cairn_imgs = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
        letsDirect_imgs = ['5.jpg', '6.jpg', '7.jpg', '8.jpg']
        letsrus_imgs = ['9.jpg', '10.jpg', '11.jpg', '12.jpg']
        foleys_imgs = ['13.jpg', '14.jpg', '15.jpg', '16.jpg']
        cairneys_imgs = ['17.jpg', '18.jpg', '19.jpg', '20.jpg']
        fontaine_imgs = ['21.jpg', '22.jpg', '23.jpg', '24.jpg']
        johnstone_imgs = ['25.jpg', '26.jpg', '27.jpg', '28.jpg']
        johnson_imgs = ['29.jpg', '30.jpg', '31.jpg', '32.jpg']
        
        
        #AGENCIES
        '''######################'''	
        #create agency users
        cairn_user = User.objects.get_or_create(username='cairn',email='cairn@gmail.com')[0]
        letsDirect_user = User.objects.get_or_create(username='letsDirect',email='letsdirect@gmail.com')[0]
        letsrus_user = User.objects.get_or_create(username='letsrus',email='letsrus@gmail.com')[0]
        foleys_user = User.objects.get_or_create(username='foleys',email='foleys@gmail.com')[0]
        cairneys_user = User.objects.get_or_create(username='cairneys',email='cairneys@gmail.com')[0]
        fontaine_user = User.objects.get_or_create(username='fontaine',email='fontaine@gmail.com')[0]
        johnstone_user = User.objects.get_or_create(username='johnstone',email='johnstone@gmail.com')[0]
        johnson_user = User.objects.get_or_create(username='johnson',email='johnson@gmail.com')[0]
        
	
        #Create and add the agencies, with different amounts of cities each
        agencies = [{'user':cairn_user, 'agencyName':'Cairn Letting', 'website':'www.cairn.co.uk', 'cities':[City.objects.get(name="Glasgow"),City.objects.get(name="Dundee")],'ratings':cairn_ratings, 'comments': cairn_comms, 'images':cairn_imgs},
				{'user':letsDirect_user, 'agencyName':'Lets Direct', 'website':'www.letsdirect.co.uk', 'cities':[City.objects.get(name="Edinburgh")],'ratings':letsDirect_ratings, 'comments': letsDirect_comms,'images':letsDirect_imgs},
				{'user':letsrus_user, 'agencyName':'Lets R Us', 'website':'www.letsrus.co.uk','cities':[City.objects.get(name="Aberdeen"),City.objects.get(name="Inverness")],'ratings':letsrus_ratings, 'comments': letsrus_comms,'images':letsrus_imgs},
				{'user':foleys_user, 'agencyName':"Foley's", 'website':'www.foleys.co.uk','cities':[City.objects.get(name="Glasgow")],'ratings':foleys_ratings, 'comments': foleys_comms,'images':foleys_imgs},
                                {'user':cairneys_user, 'agencyName':"Cairney's", 'website':'www.cairneys.co.uk','cities':[City.objects.get(name="Inverness")],'ratings':cairneys_ratings, 'comments': cairneys_comms,'images':cairneys_imgs},
                                {'user':fontaine_user, 'agencyName':"Fontaine Letting", 'website':'www.fontaineletting.co.uk','cities':[City.objects.get(name="Glasgow"),City.objects.get(name="Edinburgh")],'ratings':fontaine_ratings, 'comments': fontaine_comms,'images':fontaine_imgs},
                                {'user':johnstone_user, 'agencyName':"Johnstone Lets", 'website':'www.johnstonelets.co.uk','cities':[City.objects.get(name="Glasgow"),City.objects.get(name="Dundee")],'ratings':johnstone_ratings, 'comments': johnstone_comms,'images':johnstone_imgs},
                                {'user':johnson_user, 'agencyName':"Johnson Letting", 'website':'www.johnsonletting.co.uk','cities':[City.objects.get(name="Glasgow"),City.objects.get(name="Aberdeen"),City.objects.get(name="Inverness")],'ratings':johnson_ratings, 'comments': johnson_comms,'images':johnson_imgs}]

        print("Adding 8 agencies, 35 ratings, 46 comments and 32 images (this could take a while)")
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
        print("Done")

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
