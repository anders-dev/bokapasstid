import requests,time,sys
from bs4 import BeautifulSoup

s=requests.Session()
s.cookies.set('ASP.NET_VentusBooking_SessionId',sys.argv[1],domain="bokapass.nemoq.se")
s.cookies.set('ASP.NET_VentusBooking_SeqGUID','stockholm',domain="bokapass.nemoq.se")

url='https://bokapass.nemoq.se/Booking/Booking/Next/stockholm'

headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://bokapass.nemoq.se','DNT': '1', 'Connection':'keep-alive','Referer':'https://bokapass.nemoq.se/Booking/Booking/Index/stockholm','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1'}

data=f'FormId=1&NumberOfPeople=1&RegionId=0&SectionId=41&NQServiceTypeId=1&FromDateString={sys.argv[2]}&SearchTimeHour=12&TimeSearchButton=S%C3%B6k+tid'

failstring="Inga lediga tider kunde hittas denna vecka."


while True:
    r=s.post(url,headers=headers,data=data)
    html=r.text
    soup = BeautifulSoup(html, 'html.parser')
    fail=soup.find_all(string=failstring)
    if len(fail)==0:
        while True:
            print('Tid Finns\a')
    time.sleep(120)