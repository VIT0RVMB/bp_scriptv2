#-*- coding:utf-8 -*-
import json
import requests
import unicodedata
import codecs
from keys import Keys



COUNT=0

def published(page,status, authtoken):
	url='http://api.buscape.com.br/product/search/?page='
	import ipdb; ipdb.set_trace()
	keys=Keys()
	custom_header={
		"auth-token":authtoken,
		"app-token":keys.app_token 
	}
	
	file=codecs.open(status+' - '+custom_header['auth-token']+'.txt', 'a+b', 'utf-8')
	request=requests.get(url+str(page), headers=custom_header)
	buscape=json.loads(str(request.content))

	for i in buscape['products']:
		if i['summary']['status']==status:
			
			# import ipdb; ipdb.set_trace()
			file.write("SKU: "+i['productDataSent']['sku']+'\n')
			file.write("Produto: "+i["productDataSent"]["title"]+'\n')
			file.write("Estoque: "+ str(i["productDataSent"]["quantity"])+'\n')

			file.write("__________________________________________\n")
			print i['productDataSent']['title']+'...'

			global COUNT
			COUNT+=1
	if(page<buscape["totalPages"]):
		published(page+1, status, authtoken)
	else:
		#import ipdb; ipdb.set_trace()
		file.write('TOTAL: '+ str(COUNT))
		file.close()



	
	
	
at=raw_input('Insira o auth-token da loja: ')
print 'Verificando Produtos publicados...'
published( 1, status='PUBLISHED', authtoken=at)
print 'TOTAL de produtos Publicados: '+str(COUNT)
print '_____________________________________________'
COUNT=0
print 'Verificando Produtos aguardando publicação...'
published(page=1, status='AWAITING_PUBLICATION', authtoken=at)
print 'TOTAL de produtos aguardando publicação: '+str(COUNT)
print '_____________________________________________'
COUNT=0
print 'Verificando Produtos não publicados...'
published(page=1, status='NOT_PUBLISHED', authtoken=at)
print 'TOTAL de produtos não publicados: '+str(COUNT)
COUNT=0
