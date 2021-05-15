import socket
import fcntl
import struct
import requests
import socket
from time import sleep
import params
import datetime
from ping import ping

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def log_PS4isUp():
  local = pytz.timezone("Europe/Brussels")
  now = datetime.datetime.now()
  #print(str(now))
  local_dt = local.localize(now, is_dst=None)
  #print(str(local_dt))
  utc_dt = local_dt.astimezone(pytz.utc)

  print("local    : " + local_dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
  nowUTC = utc_dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

  msg = '{"@timestamp":"' + nowUTC + '", "host":{"PS4isUp":{"cpu": ' + str(1) + '}}}'
  print(msg)
  flog.write(msg + "\n")
  flog.flush()


myInterface = params.myInterface
sleep_IP = params.sleep_IP
hostname = socket.gethostname()
logfile = "/var/log/watchdog/PS4IsUp.log"
flog = open(logfile,"a")
sec = 0
while True:
  try:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(now)
    if sec % sleep_IP == 0:
      myIP = get_ip_address(myInterface)
      #print("hostname : " + hostname)
      #print("myIP : "+myIP)

      r = requests.get("http://192.168.0.147/monitor/getEvent.php?eventFct=add&host={0}&type=ip&text={1}".format(hostname,myInterface+":"+myIP))
      #print(r.json())

      #r = requests.get("http://192.168.0.147/monitor/getEvent.php?eventFct=getLastEventByType&host=hostname&type=ip")
      #print(r.json())
      print(now + " ip : " + myIP)

    if sec % 10 == 0:
      if ping("192.168.0.40"):
        log_PS4IsUp()


  except Exception as error:
    print("there was an exception : " + str(error))

  sec += 1
  sleep(1)
