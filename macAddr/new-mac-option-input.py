#!/usr/bin/env python3

import subprocess
import optparse

#interface = input('Interface: ')
#new_mac = input('new mac-address: ')

def change_mac(interface, new_mac):
    #subprocess.call("ifconfig "+ interface + " down ", shell=True)
    #subprocess.call("ifconfig "+ interface + " hw "+" ether "+ new_mac, shell=True)
    #subprocess.call("ifconfig "+ interface + " up ", shell=True)
    
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

parser = optparse.OptionParser()

parser.add_option('-i', '--interface', dest='interface', help='interface to change its mac address')
parser.add_option('-m', '--macaddress', dest='new_mac', help='new mac address')

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

change_mac(interface, new_mac)

