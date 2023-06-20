"""
Bu program facebook tahminlerine göre minimum, ortalama ve maksimum durumları yazdırır ve csv dosyasına kaydeder.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep
import csv

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/search?q=1+dolar+ka%C3%A7+pound&sxsrf=APwXEdevFFSVgGRMIOBETNI_Zry8t-fBdg%3A1687263708971&ei=3JmRZMHkOqa7xc8P6NGyaA&ved=0ahUKEwjBwo-Q69H_AhWmXfEDHeioDA0Q4dUDCA4&uact=5&oq=1+dolar+ka%C3%A7+pound&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIMCCMQigUQJxBGEIICMgYIABAWEB4yCAgAEBYQHhAPMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgjELADECc6CggAEEcQ1gQQsAM6CggAEIoFELADEEM6BwgjEIoFECc6CAgAEIAEELEDOgsIABCABBCxAxCDAToFCAAQgAQ6BwgjELACECc6CggAEA0QgAQQsQM6BwgAEA0QgAQ6BwgAEIAEEAo6CAgAEBYQHhAKSgQIQRgAUF5Y5xRg2xdoA3ABeAGAAdwBiAHRDpIBBjAuMTEuMZgBAKABAcABAcgBCg&sclient=gws-wiz-serp")

usdToGbp = driver.find_element(By.XPATH, "//div[@id='knowledge-currency__updatable-data-column']/div[1]/div[2]/span").text # Id'ye göre arama.
usdToGbp = usdToGbp.replace(",", ".")
usdToGbp = float(usdToGbp)
    
driver.get("https://www.google.com/search?q=1+dolar+ka%C3%A7+tl&oq=1+dolar+ka%C3%A7+tl&aqs=chrome..69i57j0i512l9.8187j1j7&sourceid=chrome&ie=UTF-8")
usdToTl = driver.find_element(By.XPATH, "//div[@id='knowledge-currency__updatable-data-column']/div[1]/div[2]/span").text # Id'ye göre arama.
usdToTl = usdToTl.replace(",", ".")
usdToTl = float(usdToTl)
driver.close()

urunMaliyeti = float(input("Ürün maliyetini giriniz(kargo dahil): "))
urunSatisFiyati = float(input("Ürün satış fiyatını giriniz: "))
reklamMaliyeti = float(input("Günlük reklam maliyetini Giriniz: "))
minUrunSatisAdedi = int(input("Minimum satış tahminini giriniz: "))
ortUrunSatisAdedi = int(input("Ortalama satış tahminini giriniz: "))
maxUrunSatisAdedi = int(input("Maksimum satış tahminini giriniz: "))

minKarUsd = urunSatisFiyati - ((urunSatisFiyati/10) + reklamMaliyeti/minUrunSatisAdedi + urunMaliyeti)
minPound = minKarUsd*usdToGbp
minTl = minKarUsd*usdToTl

ortKarUsd = urunSatisFiyati - ((urunSatisFiyati/10) + reklamMaliyeti/ortUrunSatisAdedi + urunMaliyeti)
ortPound = ortKarUsd*usdToGbp
ortTl = ortKarUsd*usdToTl

maxKarUsd = urunSatisFiyati - ((urunSatisFiyati/10) + reklamMaliyeti/maxUrunSatisAdedi + urunMaliyeti)
maxPound = maxKarUsd*usdToGbp
maxTl = maxKarUsd*usdToTl

print(f'\nGüncel USD-GBP kuru: 1 $ = {usdToGbp} £')
print(f'Güncel USD-TL kuru: 1 $ = {usdToTl} ₺')

print("\n")
print(20*"*" + " Minimum Durum " + 20*"*")
print("\n")
print(f'Bu reklam performansına göre ürün başına düşen günlük karınız ---> {minKarUsd:.2f} $')
print(f'Bu reklam performansına göre ürün başına düşen günlük karınız(Pound cinsinden) ---> {minPound:.2f}£')
print(f'Bu reklam performansına göre ürün başına düşen günlük karınız(TL cinsinden) ---> {minTl:.2f}₺')
print(f'TL cinsinden günlük kar miktarı ---> {minTl*minUrunSatisAdedi:.2f} ₺')
print(f'Dolar cinsinden günlük kar miktarı ---> {minKarUsd*minUrunSatisAdedi:.2f} $')
print(f'Pound cinsinden günlük kar miktarı ---> {minPound*minUrunSatisAdedi:.2f} £')

print("\n")
print(20*"*" + " Ortalama Durum " + 20*"*")
print("\n")
print(f'Bu reklam performansına göre ürün başına düşen günlük karınız ---> {ortKarUsd:.2f} $')
print(f'Bu reklam performansına göre ürün başına düşen günlük karınız(Pound cinsinden) ---> {ortPound:.2f}£')
print(f'Bu reklam performansına göre ürün başına düşen günlük karınız(TL cinsinden) ---> {ortTl:.2f}₺')
print(f'TL cinsinden günlük kar miktarı ---> {ortTl*ortUrunSatisAdedi:.2f} ₺')
print(f'Dolar cinsinden günlük kar miktarı ---> {ortKarUsd*ortUrunSatisAdedi:.2f} $')
print(f'Pound cinsinden günlük kar miktarı ---> {ortPound*ortUrunSatisAdedi:.2f} £')

print("\n")
print(20*"*" + " Maksimum Durum " + 20*"*")
print("\n")
print(f'Bu reklam performansına göre ürün başına düşen günlük karınız ---> {maxKarUsd:.2f} $')
print(f'Bu reklam performansına göre ürün başına düşen günlük karınız(Pound cinsinden) ---> {maxPound:.2f}£')
print(f'Bu reklam performansına göre ürün başına düşen günlük karınız(TL cinsinden) ---> {maxTl:.2f}₺')
print(f'TL cinsinden günlük kar miktarı ---> {maxTl*maxUrunSatisAdedi:.2f} ₺')
print(f'Dolar cinsinden günlük kar miktarı ---> {maxKarUsd*maxUrunSatisAdedi:.2f} $')
print(f'Pound cinsinden günlük kar miktarı ---> {maxPound*maxUrunSatisAdedi:.2f} £')

minKar = minKarUsd*minUrunSatisAdedi
ortKar = ortKarUsd*ortUrunSatisAdedi
maxKar = maxKarUsd*maxUrunSatisAdedi
        
veriler = [[minUrunSatisAdedi, f"{minKar:.2f}", ortUrunSatisAdedi, f"{ortKar:.2f}", maxUrunSatisAdedi, f"{maxKar:.2f}", datetime.now().date()]]
with open("TAHMİNİ_KAR.csv", "a", newline = '') as kar:
    odeme2 = csv.writer(kar)
    odeme2.writerows(veriler)

sleep(2)
print("\nProgram sonlandırılıyor", end="")
sleep(1)
print(".", end="")
sleep(1)
print(".", end="")
sleep(1)
print(".")
print("Program sonlandırıldı.")