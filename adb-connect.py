import os
from easygui import *
import re

if (not os.path.exists('ip.txt')):
    open('ip.txt', 'w')
file = open('ip.txt', 'r+')

ip_file = ''
port_file = ''
new_ip_port = ''

regex = re.compile("([0-9.]+):(\d+)")
readfile = file.read()
if (bool(regex.match(readfile))):
    r = regex.search(readfile)
    ip_port = r.groups()
    ip_file = ip_port[0]
    port_file = ip_port[1]
fieldNames = ["IP","Port"]
fields = []
fields = multenterbox('Enter IP and Port', 'ADB Connect GUI', fieldNames, [ip_file, port_file])
ip = fields[0]
port = fields[1]

if (ip != ip_file or port != port_file):
    file.seek(0)
    new_ip_port = ip + ':' + port
    file.write(new_ip_port)
    file.close()
os.system('adb connect ' + new_ip_port)
os.system('adb shell')
os.system('adb kill-server')

def check_ip(ip):
    regex = re.compile("(\d+):(\d+):(\d+):(\d+)")
    r = regex.search(ip)
    for i in r.groups():
        if(not i.isdigit):
            return False
    return True
