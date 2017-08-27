#Miguel Toledano
#Para mi Chinita Bebé :v

from sys import argv
import urllib
from bs4 import BeautifulSoup
import datetime

def Help():
    print ("Instagram Image Downloader")
    print ("")
    print ("Uso: ")
    print ("")
    print ("Opciones: ")
    print ("-u [Instagram URL]\tDescargar una sola foto de la URL de Instagram")
    print ("-f [File Path]\t\tDescargar foto(s) usando una archivo de lista")
    print ("-h, --help\t\t Muestra un mensaje de ayuda")
    print ("")
    print ("Ejemplo: ")
    print ("python instaDownloader.py -u https://instagram.com/p/xxxxxx")
    print ("python instaDownloader.py -f /home/username/filelist.txt")
    print ("")
    exit()

def DownloadPhoto(fileURL):
    print ("Descargando imagen . . .")
    f = urllib.urlopen(fileURL)
    htmlSource = f.read()
    soup = BeautifulSoup(htmlSource, 'html.parser')
    metaTag = soup.find_all('meta', {'property':'og:image'})
    imgURL = metaTag[0]['content']
    fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ('.jpg')
    urllib.urlretrieve(imgURL, fileName)
    print ("Terminando. La image se guardo en el disco como: " + fileName)

if __name__ == '__main__':
    if len(argv) == 1:
        Help()

    if argv[1] in ('-h', '--help'):
        Help()

    elif argv[1] == ("-u"):
        instagramURL = argv[2]
        DownloadPhoto(instagramURL)

    elif argv[1] == "-f":
        filePath = argv[2]
        f = open(filePath)
        line = f.readline()
        while line:
            instagramURL = line.rstrip('\n')
            DownloadPhoto(instagramURL)

            line = f.readline()

        f.close()
