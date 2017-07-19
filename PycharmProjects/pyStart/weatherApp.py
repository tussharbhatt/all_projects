import requests
import bs4
import commonHeader
import collections
weatherReport=collections.namedtuple("weatherRep",'location,Temp,deg')
def main():
    commonHeader.print_header()
    get_pincode()



def get_pincode():
    pinCode=None
    pinCode=input("enter name of your region..  ")
    pinCode=pinCode.lower().strip()
    get_html_from_web(pinCode)

def get_html_from_web(pinCode):
    #TODO try to send data to search feild and then act on page
    #url="https://www.wunderground.com/"
    url="https://www.wunderground.com/cgi-bin/findweather/getForecast?query={}".format(pinCode)
    result=requests.get(url)
    #print(result.status_code)
    #print(result.text)
    tppl=parse_html(result.text)
    print("the weather in {} is {} {}".format(tppl.location.strip(),tppl.Temp,tppl.deg))


def parse_html(result):
    soup=bs4.BeautifulSoup(result,'html.parser')
    #print(soup)

    loc=soup.find(id='location').find('h1').get_text()
    currTemp=soup.find(id='curTemp').find(class_='wx-value').get_text()
    degree = soup.find(id='curTemp').find(class_='wx-unit').get_text()
    weather=soup.find(id='curCond').find(class_='wx-value').get_text()
    #wind=soup.find(id='wind-dir').find(class_='wx-value').get_text()
    tupl=weatherReport(location=loc,Temp=currTemp,deg=degree)
    return tupl
    #print(currTemp)
    '''print(loc.strip())
    print(currTemp.strip()+degree.strip())
    print("weather : {}".format(weather))
    #print("wind from : {}".format(wind))

    print()
    print()

    choice=input("do you want to check for another location y/n..\n ")
    choice=choice.lower().strip()
    if choice=='y':
        get_pincode()
    else:
        print("good bye..")'''



main()