import requests 
from bs4 import BeautifulSoup 


for i in range (5,7):
    x=i
    y=i-2
    #x=somesensormeathod()
    url="http://localhost:5000/tippoffservice/"+str(x)+"/"+str(y)+"/wa"
    r=requests.get(url=url)
    soup=BeautifulSoup(r.text,'html.parser')
    for i in soup.findAll("p"):
        res=i.text
    l=res.split(" ")
    bollean=l[0]
    if(bollean=="False"):
        print("\a")
        print("\a")
        print("\a")
        #stopwheelsmethod()
        print("DO NOT CLIMB THIS SLOPE")
    else:
        print("You can climb the slope")
