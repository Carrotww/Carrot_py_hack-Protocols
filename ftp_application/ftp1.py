from ftplib import FTP

# ftp = FTP(input("wr ip addr : "))
ftp = FTP('192.168.100.250')

print('banner:', ftp.getwelcome())
print('login:', ftp.login(user="anonymous", passwd="anonymous"))
print('LIST:', ftp.retrlines('LIST'))
# print(ftp.retrbinary('RETR ftp_test.txt', open('ftp_test.txt', 'wb').write))
print(ftp.retrbinary('RETR ftp_test.txt'))
