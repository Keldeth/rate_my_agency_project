import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rate_my_agency_project.settings')

# commenting to test changes

import django
django.setup()
from rate_my_agency.models import City, Tenant, Agency, Rating, Comment

#Attempting to fix the whole user problem
from django.contrib.auth.models import User
'''
user1 = User.objects.create_user(username='11',email='1lennon@beatles.com',password='11')
user2 = User.objects.create_user(username='21',email='2lennon@beatles.com',password='21')
user3 = User.objects.create_user(username='31',email='3lennon@beatles.com',password='31')
user4 = User.objects.create_user(username='41',email='4lennon@beatles.com',password='41')
user5 = User.objects.create_user(username='51',email='5lennon@beatles.com',password='51')
'''

def populate():
	#same as "pages" in rango example
	#NOTE 'id' isn't the best description 
	#as they are actually user instances
	#but i've left it for simplicity of just populating
	'''
	glasgow_agencies = [
		{'name':'a1','id':user1},
		{'name':'a2','id':user2}]
	
	edinburgh_agencies = [
		{'name':'a3','id':user3}]
		
	dundee_agencies = [
		{'name':'a4','id':user4},
		{'name':'a5','id':user5}]
	'''
	#same as "cats" in rango example
	cities = ['Glasgow','Dundee','Edinburgh']
	'''
	{'Glasgow':{'agencies': glasgow_agencies},
			  'Edinburgh':{'agencies': edinburgh_agencies},
			  'Dundee':{'agencies': dundee_agencies}}
	'''
	for c in cities:
		add_cit(c)
		'''
		for a in cit_data['agencies']:
			add_agency(c, a['name'],a['id'])
		'''	
	#print out the cities we have added
	for c in City.objects.all():
		print (c)
			
'''
def add_agency(cit,name,id):
	#will need to add urls and things here
	a = Agency.objects.get_or_create(city=cit,user=id)
	a.save()
	return a
'''	
def add_cit(name):
	c = City.objects.get_or_create(name=name)[0]
	c.save()
	return c
	
	
#Main
if __name__ == '__main__':
	print('Starting rma population script')
	populate()
