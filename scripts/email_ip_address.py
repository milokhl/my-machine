import sys, os, time, datetime, time, socket
import netifaces as ni
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

def SendIpAddress(addr):
  """
  Sends an email with the IP address.
  """
  msg = MIMEText(time.ctime())
  msg["From"] = "mknowles@mit.edu"
  msg["To"] = "mknowles@mit.edu"

  hostname = socket.gethostname()
  msg["Subject"] = "%s booted at %s" % (hostname, str(addr))
  p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
  p.communicate(msg.as_string())
  print 'Sent email'

def QueryIpAddress():
  """
  Gets the current IP address of the Pi on whatever WIFI it's connected to.
  """
  interfaces = ni.interfaces()
  # wlan = ni.ifaddresses('wlp2s0') # For my Ubuntu 16.04 on Dell XPS
  wlan = ni.ifaddresses('wlan0') # For Raspberry Pi running MATE 16.04
  inet = wlan[2]
  ip = inet[0]['addr']
  return ip
            
if __name__ == '__main__':
  ip_addr = QueryIpAddress()
  print ip_addr

  SendIpAddress(ip_addr)
