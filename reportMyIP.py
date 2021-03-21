import socket
import fcntl
import struct
import requests
import socket
from time import sleep



def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


while True:
  myInterface = 'wlan0'
  myIP = get_ip_address(myInterface)
  hostname = socket.gethostname()

  #print("hostname : " + hostname)
  #print("myIP : "+myIP)

  r = requests.get("http://192.168.0.147/monitor/getEvent.php?eventFct=add&host={0}&type=ip&text={1}".format(hostname,myInterface+":"+myIP))
  #print(r.json())

  #r = requests.get("http://192.168.0.147/monitor/getEvent.php?eventFct=getLastEventByType&host=hostname&type=ip")
  #print(r.json())
  sleep(60*60)

