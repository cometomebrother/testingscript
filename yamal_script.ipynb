#pip install beautifulsoup4
#pip install lxml

import requests
from lxml import html
import time
from bs4 import BeautifulSoup

hdr = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',}
hdr2={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',}

url1='https://www.vesselfinder.com/vessels/CHRIS.-DE-MARGERIE-IMO-9737187-MMSI-212611000'
url2='https://www.vesselfinder.com/vessels/BORIS-VILKITSKY-IMO-9768368-MMSI-212654000'
url3='https://www.vesselfinder.com/vessels/VLADIMIR-RUSANOV-IMO-9750701-MMSI-477150100'
url4='https://www.vesselfinder.com/vessels/FEDOR-LITKE-IMO-9768370-MMSI-212660000'
url5='https://www.vesselfinder.com/vessels/EDUARD-TOLL-IMO-9750696-MMSI-311000548'
url6='https://www.vesselfinder.com/vessels/RUDOLF-SAMOYLOVICH-IMO-9750713-MMSI-311000627'
url7='https://www.vesselfinder.com/vessels/VLADIMIR-VIZE-IMO-9750658-MMSI-477194200'
url8='https://www.vesselfinder.com/vessels/GEORGIY-BRUSILOV-IMO-9768382-MMSI-212770000'
url9='https://www.vesselfinder.com/vessels/BORIS-DAVYDOV-IMO-9768394-MMSI-209356000'
url10='https://www.vesselfinder.com/vessels/NIKOLAY-ZUBOV-IMO-9768526-MMSI-209351000'
url11='https://www.vesselfinder.com/vessels/NIKOLAY-YEVGENOV-IMO-9750725-MMSI-311000631'
url12='https://www.vesselfinder.com/vessels/VLADIMIR-VORONIN-IMO-9750737-MMSI-311000632'
url13='https://www.vesselfinder.com/vessels/NIKOLAY-URVANTSEV-IMO-9750660-MMSI-477327300'
url14='https://www.vesselfinder.com/vessels/GEORGIY-USHAKOV-IMO-9750749-MMSI-311000633'
url15='https://www.vesselfinder.com/vessels/YAKOV-GAKKEL-IMO-9750672-MMSI-311000634'
url='https://www.vesselfinder.com/vessels/BORIS-VILKITSKY-IMO-9768368-MMSI-212654000'

list_of_urls=['https://www.vesselfinder.com/vessels/CHRIS.-DE-MARGERIE-IMO-9737187-MMSI-212611000',
              'https://www.vesselfinder.com/vessels/BORIS-VILKITSKY-IMO-9768368-MMSI-212654000',
              'https://www.vesselfinder.com/vessels/VLADIMIR-RUSANOV-IMO-9750701-MMSI-477150100',
              'https://www.vesselfinder.com/vessels/FEDOR-LITKE-IMO-9768370-MMSI-212660000',
              'https://www.vesselfinder.com/vessels/EDUARD-TOLL-IMO-9750696-MMSI-311000548',
              'https://www.vesselfinder.com/vessels/RUDOLF-SAMOYLOVICH-IMO-9750713-MMSI-311000627',
              'https://www.vesselfinder.com/vessels/VLADIMIR-VIZE-IMO-9750658-MMSI-477194200',
              'https://www.vesselfinder.com/vessels/GEORGIY-BRUSILOV-IMO-9768382-MMSI-212770000',
              'https://www.vesselfinder.com/vessels/BORIS-DAVYDOV-IMO-9768394-MMSI-209356000',
              'https://www.vesselfinder.com/vessels/NIKOLAY-ZUBOV-IMO-9768526-MMSI-209351000',
              'https://www.vesselfinder.com/vessels/NIKOLAY-YEVGENOV-IMO-9750725-MMSI-311000631',
              'https://www.vesselfinder.com/vessels/VLADIMIR-VORONIN-IMO-9750737-MMSI-311000632',
              'https://www.vesselfinder.com/vessels/NIKOLAY-URVANTSEV-IMO-9750660-MMSI-477327300',
              'https://www.vesselfinder.com/vessels/GEORGIY-USHAKOV-IMO-9750749-MMSI-311000633',
              'https://www.vesselfinder.com/vessels/YAKOV-GAKKEL-IMO-9750672-MMSI-311000634']

list_of_urls2=['https://www.vesselfinder.com/vessels/CHRIS.-DE-MARGERIE-IMO-9737187-MMSI-212611000',
              'https://www.vesselfinder.com/vessels/BORIS-VILKITSKY-IMO-9768368-MMSI-212654000',
              'https://www.vesselfinder.com/vessels/VLADIMIR-RUSANOV-IMO-9750701-MMSI-477150100',
              'https://www.vesselfinder.com/vessels/FEDOR-LITKE-IMO-9768370-MMSI-212660000',
              'https://www.vesselfinder.com/vessels/EDUARD-TOLL-IMO-9750696-MMSI-311000548',
              'https://www.vesselfinder.com/vessels/RUDOLF-SAMOYLOVICH-IMO-9750713-MMSI-311000627',
              'https://www.vesselfinder.com/vessels/VLADIMIR-VIZE-IMO-9750658-MMSI-477194200',
              'https://www.vesselfinder.com/vessels/GEORGIY-BRUSILOV-IMO-9768382-MMSI-212770000',
              'https://www.vesselfinder.com/vessels/BORIS-DAVYDOV-IMO-9768394-MMSI-209356000',
              'https://www.vesselfinder.com/vessels/NIKOLAY-ZUBOV-IMO-9768526-MMSI-209351000',
              'https://www.vesselfinder.com/vessels/NIKOLAY-YEVGENOV-IMO-9750725-MMSI-311000631',
              'https://www.vesselfinder.com/vessels/VLADIMIR-VORONIN-IMO-9750737-MMSI-311000632',
              'https://www.vesselfinder.com/vessels/NIKOLAY-URVANTSEV-IMO-9750660-MMSI-477327300',
              'https://www.vesselfinder.com/vessels/GEORGIY-USHAKOV-IMO-9750749-MMSI-311000633',
              'https://www.vesselfinder.com/vessels/YAKOV-GAKKEL-IMO-9750672-MMSI-311000634']

list_of_arc4_urls=['https://www.vesselfinder.com/vessels/YENISEI-RIVER-IMO-9629586-MMSI-538005072',
                   'https://www.vesselfinder.com/vessels/LENA-RIVER-IMO-9629598-MMSI-538005073',
                   'https://www.vesselfinder.com/vessels/CLEAN-PLANET-IMO-9637507-MMSI-538005351',
                   'https://www.vesselfinder.com/vessels/CLEAN-HORIZON-IMO-9655444-MMSI-256083000',
                   'https://www.vesselfinder.com/vessels/CLEAN-OCEAN-IMO-9637492-MMSI-538005350',
                   'https://www.vesselfinder.com/vessels/LNG-MEGREZ-IMO-9834325-MMSI-477345600',
                   'https://www.vesselfinder.com/vessels/LNG-DUBHE-IMO-9834296-MMSI-477327900',
                   'https://www.vesselfinder.com/vessels/LNG-MERAK-IMO-9834301-MMSI-477345800',
                   'https://www.vesselfinder.com/vessels/LNG-PHECDA-IMO-9834313-MMSI-477345700',
                   'https://www.vesselfinder.com/vessels/YAMAL-SPIRIT-IMO-9781920-MMSI-311000666'
                  ]

list_of_arc4_urls2=['https://www.vesselfinder.com/vessels/YENISEI-RIVER-IMO-9629586-MMSI-538005072',
                   'https://www.vesselfinder.com/vessels/LENA-RIVER-IMO-9629598-MMSI-538005073',
                   'https://www.vesselfinder.com/vessels/CLEAN-PLANET-IMO-9637507-MMSI-538005351',
                   'https://www.vesselfinder.com/vessels/CLEAN-HORIZON-IMO-9655444-MMSI-256083000',
                   'https://www.vesselfinder.com/vessels/CLEAN-OCEAN-IMO-9637492-MMSI-538005350', #NOT SHOWN
                   'https://www.vesselfinder.com/vessels/LNG-MEGREZ-IMO-9834325-MMSI-477345600',#NOT SHOWN
                   'https://www.vesselfinder.com/vessels/LNG-DUBHE-IMO-9834296-MMSI-477327900',
                   'https://www.vesselfinder.com/vessels/LNG-MERAK-IMO-9834301-MMSI-477345800',
                   'https://www.vesselfinder.com/vessels/LNG-PHECDA-IMO-9834313-MMSI-477345700', #NOT SHOWN
                   'https://www.vesselfinder.com/vessels/YAMAL-SPIRIT-IMO-9781920-MMSI-311000666'
                  ]


def vesselfinder(urlz):
    resp = requests.get(urlz,headers=hdr2)
    tree = html.fromstring(resp.content)
    vessel_name=tree.xpath('/html/body/div[1]/div/main/div/div[1]/div/div[2]/h1')
    #next_port = tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/a')
    #ETA_of_next_port=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div/span[1]')
    last_position_received_days_ago = tree.xpath('//*[@id="lastrep"]/span[1]')
    #last_port_of_call=tree.xpath('//*[@id="port-calls"]/div[1]/a')
    #ETA_of_last_port=tree.xpath('//*[@id="port-calls"]/div[1]/div/div[1]/div[2]')
    #ETD_of_last_port=tree.xpath('//*[@id="port-calls"]/div[1]/a') 
    Previous_port=tree.xpath('//*[@id="agr2"]/div/div[2]/a')
    previous_port_time=tree.xpath('//*[@id="agr2"]/div/div[2]/div')
    upcoming_port=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/a')
    #upcoming_port2=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div[1]')
    upcoming_port_time=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div/span[1]')
    #upcoming_port_time2=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div[2]/span[1]')
    year_of_build=tree.xpath('/html/body/div[1]/div/main/div/section[4]/table/tbody/tr/td[3]')
    
    for a,b,c,d,e,f,g in zip(vessel_name,Previous_port,previous_port_time,upcoming_port,upcoming_port_time,last_position_received_days_ago,year_of_build):
        print(a.text)
        print('Last port ',b.text,'',c.text)
        print('Upcoming port ',d.text,'',e.text)
        #print(d.text,'',e.text)
        print("Position received ",f.text)
        print('Year of delivery ',g.text)
        print('')
        
def vesselfinder2(urlz):
    resp = requests.get(urlz,headers=hdr2)
    tree = html.fromstring(resp.content)
    vessel_name=tree.xpath('/html/body/div[1]/div/main/div/div[1]/div/div[2]/h1')
    #next_port = tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/a')
    #ETA_of_next_port=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div/span[1]')
    last_position_received_days_ago = tree.xpath('//*[@id="lastrep"]/span[1]')
    last_port_of_call=tree.xpath('//*[@id="port-calls"]/div[1]/a')
    #ETA_of_last_port=tree.xpath('//*[@id="port-calls"]/div[1]/div/div[1]/div[2]') 
    #ETD_of_last_port=tree.xpath('//*[@id="port-calls"]/div[1]/a') 
    Previous_port=tree.xpath('//*[@id="agr2"]/div/div[2]/a')
    previous_port_time=tree.xpath('//*[@id="agr2"]/div/div[2]/div')
    #upcoming_port=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/a')
    upcoming_port2=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div[1]') #ONLY 3 VESSELS
    #upcoming_port_time=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div/span[1]')
    upcoming_port_time2=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div[2]/span[1]')#ONLY 3 VESSELS 
    #year_of_build=tree.xpath('/html/body/div[1]/div/main/div/section[4]/table/tbody/tr/td[3]')
                             
def vesselfinder3(urlz):
    resp = requests.get(urlz,headers=hdr2)
    tree = html.fromstring(resp.content)
    
    vessel_name=tree.xpath('/html/body/div[1]/div/main/div/div[1]/div/div[2]/h1')
    last_position_received_days_ago = tree.xpath('//*[@id="lastrep"]/span[1]')
    Previous_port=tree.xpath('//*[@id="agr2"]/div/div[2]/a')
    previous_port_time=tree.xpath('//*[@id="agr2"]/div/div[2]/div')
    upcoming_port=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/a')
    #upcoming_port2=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div[1]')
    upcoming_port_time=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div/span[1]')
    #upcoming_port_time2=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div[2]/span[1]')#ONLY 3 VESSELS
    year_of_build=tree.xpath('/html/body/div[1]/div/main/div/section[4]/table/tbody/tr[11]/td[2]')
    
    for a, b,c,d,e,f,g in zip(vessel_name,last_position_received_days_ago,Previous_port,previous_port_time,upcoming_port,upcoming_port_time,year_of_build):
        print(a.text)
        print('Position received ',b.text)
        print('Previous port ',c.text,'',d.text)
        print('Upcoming port ',e.text,'',f.text)
        print('Year of build ',g.text)
    print('')

def vesselfinder4(urlz):
    resp = requests.get(urlz,headers=hdr2)
    tree = html.fromstring(resp.content)
    
    vessel_name=tree.xpath('/html/body/div[1]/div/main/div/div[1]/div/div[2]/h1')
    last_position_received_days_ago = tree.xpath('//*[@id="lastrep"]/span[1]')
    Previous_port=tree.xpath('//*[@id="agr2"]/div/div[2]/a')
    previous_port_time=tree.xpath('//*[@id="agr2"]/div/div[2]/div')
    #upcoming_port=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/a')
    upcoming_port2=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div[1]')
    #upcoming_port_time=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div/span[1]')
    upcoming_port_time2=tree.xpath('/html/body/div[1]/div/main/div/section[1]/div/div[2]/div/div[1]/div[2]/div[2]/span[1]')#ONLY 3 VESSELS
    year_of_build=tree.xpath('/html/body/div[1]/div/main/div/section[4]/table/tbody/tr[11]/td[2]')
    
    for a, b,c,d,e,f,g in zip(vessel_name,last_position_received_days_ago,Previous_port,previous_port_time,upcoming_port2,upcoming_port_time2,year_of_build):
        print(a.text)
        print('Position received ',b.text)
        print('Previous port ',c.text,'',d.text)
        print('Upcoming port ',e.text,'',f.text)
        print('Year of build ',g.text)
    print('')




print('ARC 7 Yamal vessels')
print('')

for i in list_of_urls:
    vesselfinder4(i)

for i in list_of_urls:
    vesselfinder3(i)
print('')
print('arc-4')
print('')
for i in list_of_arc4_urls:
    vesselfinder3(i)
    
for i in list_of_arc4_urls:
    vesselfinder4(i)

print('done')

#TEST IF SCRIPT WORKS OR NOT
'''
resp = requests.get('https://www.vesselfinder.com/vessels/BORIS-VILKITSKY-IMO-9768368-MMSI-212654000',headers=hdr2)
tree = html.fromstring(resp.content)
    
vessel_name=tree.xpath('/html/body/div[1]/div/main/div/div[1]/div/div[2]/h1')

for i in vessel_name:
    print(i.text)
    '''
