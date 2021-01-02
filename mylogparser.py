import re
import urllib
from datetime import datetime



def read_log_parse_ip_dom(FILE_NAME):
   with open(FILE_NAME, "r+") as f:
    text = f.read()
    text = re.sub('255.255.255.255', 'myip[.]com', text)
    text = re.sub('azure.com', 'mydomain[.]com', text)
    f.seek(0)
    f.write(text)
    f.truncate()
def ip_location(ip):
    char_ip=str(ip).strip('[]')
 #   print char_ip
    char_clear_ip= char_ip.strip("'")
  #  print char_clear_ip
    url = 'https://ipinfo.io/'+char_clear_ip+'/?token='
    response = urllib.urlopen(url)
    lines=response.read()
    return lines
def string_ip_request(FILE_NAME):
    with open(FILE_NAME, "r+") as f:
        text = f.readlines()
        for line in text:
          ip = re.findall( r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
          data=line.split('"')
          #add ip location function
          loc= ip_location(str(ip))
          if loc.find("hostname")!=-1:
             hostname= loc.split(",")
     #        print hostname
             mainstr=str(ip).strip('[]')+" : "+str(data[1])+hostname[1]
          else:
            city= loc.split(",")
            if loc.find("city")!=-1:
                mainstr=str(ip).strip('[]')+" : " +str(data[1])+city[1]+city[4]+","+city[5]
            else:
                mainstr=str(ip).strip('[]')+" : " +str(data[1])
            item2=mainstr.find(".")
            mainstr2 = mainstr[:item2] + '[' + mainstr[item2:]
            item2+=2
            mainstr2 = mainstr2[:item2] +']'+ mainstr2[item2:]
          #print item
          #print mainstr[item+1]
            item=mainstr2.find("/")
            if mainstr2[item+1] !=' ':
                if len(mainstr2)>80 and len(mainstr2)<200:
                      print mainstr2
                else:
                 #if no small bots message
                      print mainstr2
read_log_parse_ip_dom("/var/log/access.log")
string_ip_request("/var/log/access.log")
