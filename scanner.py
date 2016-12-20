#coding:utf-8

"""
This is a beta version...May contain errors
"""
import subprocess
import re 
import os
import socket

print("[*]NetScan by Bl4ckRe4per and Rayxd15")
ipmax = input("Enter the max ip adress the program have to scan (max : 255) : ")
ipmax = int(ipmax)
hosts = []
ip = '192.168.1.'
x = 0
while x <= ipmax:
	p = subprocess.Popen('ping '+ ip + str(x) + " -n 1", stdout = subprocess.PIPE, shell = True)
	out, error = p.communicate()
	out = str(out)
	find = re.search("Destination host unreachable", out)
	if find is None: 
		hosts.append(ip + str(x))
		print("[!] New host found")
		x = x + 1
print("_____________________________________")
print("              Hosts Found            ")
print("_____________________________________")
for host in hosts:
	try:
		name, a, b = socket.gethostbyaddr(host)
	except:
		name = " Not found "
	print("[*/] " + host +" "+ name)
