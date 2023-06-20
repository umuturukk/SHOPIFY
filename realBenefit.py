from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep
import csv

print(40*"-")
print(10*" " + "Shopify İşlem Menüsü" + 10*" ")
print(40*"-")

print("1-) İstenilen Kara Göre Ürün Fiyatının Belirlenmesi\n2-) Reklam Performansına Göre Kar Miktarı")
sleep(0.5)
islem = input("İşlem Gir: ")

while True:
    if islem == "q":
        break
    elif islem == "1":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com/search?q=1+dolar+ka%C3%A7+pound&sxsrf=APwXEdevFFSVgGRMIOBETNI_Zry8t-fBdg%3A1687263708971&ei=3JmRZMHkOqa7xc8P6NGyaA&ved=0ahUKEwjBwo-Q69H_AhWmXfEDHeioDA0Q4dUDCA4&uact=5&oq=1+dolar+ka%C3%A7+pound&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIMCCMQigUQJxBGEIICMgYIABAWEB4yCAgAEBYQHhAPMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgjELADECc6CggAEEcQ1gQQsAM6CggAEIoFELADEEM6BwgjEIoFECc6CAgAEIAEELEDOgsIABCABBCxAxCDAToFCAAQgAQ6BwgjELACECc6CggAEA0QgAQQsQM6BwgAEA0QgAQ6BwgAEIAEEAo6CAgAEBYQHhAKSgQIQRgAUF5Y5xRg2xdoA3ABeAGAAdwBiAHRDpIBBjAuMTEuMZgBAKABAcABAcgBCg&sclient=gws-wiz-serp")
        
        usdToGbp = driver.find_element(By.XPATH, "//div[@id='knowledge-currency__updatable-data-column']/div[1]/div[2]/span").text # Id'ye göre arama.
        usdToGbp = usdToGbp.replace(",", ".")
        usdToGbp = float(usdToGbp)
        driver.close()
        
        urunMaliyeti = float(input("Ürün Maliyetini Giriniz(kargo dahil): "))
        reklamMaliyeti = float(input("Reklam Maliyetini Giriniz: "))
        tahminiSatisMiktari = int(input("Tahmini satış adedinizi giriniz: "))
        karMiktari = float(input("Yapmak istediğiniz kar miktarını giriniz: "))
        usd = float((((reklamMaliyeti/tahminiSatisMiktari) + urunMaliyeti + karMiktari)*10)/9)

        pound = usd*usdToGbp

        print("\n")
        print(f'İstediğiniz kar miktarına göre ürünün uygun satış fiyatı {usd:.2f} $')
        print(f'İstediğiniz kar miktarına göre Pound cinsinden satış fiyatı {pound:.2f} £')
        print("\n")
        sleep(2)
        print("İşlem Sonlandırıldı.")
        break
    
    elif islem == "2":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com/search?q=1+dolar+ka%C3%A7+pound&sxsrf=APwXEdevFFSVgGRMIOBETNI_Zry8t-fBdg%3A1687263708971&ei=3JmRZMHkOqa7xc8P6NGyaA&ved=0ahUKEwjBwo-Q69H_AhWmXfEDHeioDA0Q4dUDCA4&uact=5&oq=1+dolar+ka%C3%A7+pound&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIMCCMQigUQJxBGEIICMgYIABAWEB4yCAgAEBYQHhAPMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgjELADECc6CggAEEcQ1gQQsAM6CggAEIoFELADEEM6BwgjEIoFECc6CAgAEIAEELEDOgsIABCABBCxAxCDAToFCAAQgAQ6BwgjELACECc6CggAEA0QgAQQsQM6BwgAEA0QgAQ6BwgAEIAEEAo6CAgAEBYQHhAKSgQIQRgAUF5Y5xRg2xdoA3ABeAGAAdwBiAHRDpIBBjAuMTEuMZgBAKABAcABAcgBCg&sclient=gws-wiz-serp")

        usdToGbp = driver.find_element(By.XPATH, "//div[@id='knowledge-currency__updatable-data-column']/div[1]/div[2]/span").text
        usdToGbp = usdToGbp.replace(",", ".")
        usdToGbp = float(usdToGbp)

        driver.get("https://www.google.com/search?q=1+dolar+ka%C3%A7+tl&oq=1+dolar+ka%C3%A7+tl&aqs=chrome..69i57j0i512l9.8187j1j7&sourceid=chrome&ie=UTF-8")
        usdToTl = driver.find_element(By.XPATH, "//div[@id='knowledge-currency__updatable-data-column']/div[1]/div[2]/span").text
        usdToTl = usdToTl.replace(",", ".")
        usdToTl = float(usdToTl)
        
        driver.close()

        urunMaliyeti = float(input("Ürün maliyetini giriniz(kargo dahil): "))
        urunSatisFiyati = float(input("Ürün satış fiyatını giriniz: "))
        reklamMaliyeti = float(input("Günlük reklam maliyetini Giriniz: "))
        urunSatisAdedi = int(input("Üründen kaç adet sattığınızı giriniz(günlük): "))

        karUsd = urunSatisFiyati - ((urunSatisFiyati/10) + reklamMaliyeti/urunSatisAdedi + urunMaliyeti)

        pound = karUsd*usdToGbp
        tl = karUsd*usdToTl

        print(f'\nGüncel USD-GBP kuru: 1 $ = {usdToGbp} £')
        print(f'Güncel USD-TL kuru: 1 $ = {usdToTl} ₺')
        print("\n")
        print(f'Bu reklam performansına göre ürün başına düşen günlük karınız ---> {karUsd} $')
        print(f'Dolar cinsinden günlük kar miktarı ---> {karUsd*urunSatisAdedi} $')
        print(f'Bu reklam performansına göre ürün başına düşen günlük karınız(Pound cinsinden) ---> {pound}£')
        print(f'Pound cinsinden günlük kar miktarı ---> {pound*urunSatisAdedi} £')
        print(f'Bu reklam performansına göre ürün başına düşen günlük karınız(TL cinsinden) ---> {tl}₺')      
        print(f'TL cinsinden günlük kar miktarı ---> {tl*urunSatisAdedi} ₺')
        
        veriler = [[urunSatisAdedi, f"{karUsd:.2f}", f"{karUsd*urunSatisAdedi:.2f}", f"{pound:.2f}", f"{pound*urunSatisAdedi:.2f}", f"{tl:.2f}", f"{tl*urunSatisAdedi:.2f}", reklamMaliyeti, datetime.now().date()]]  
        with open("KAR_KAYIT.csv", "a", newline = '') as kar:
            odeme2 = csv.writer(kar)
            odeme2.writerows(veriler)

        print("\nVeriler başarıyla kaydedildi.\nİşlem sonlandırılıyor...")
        sleep(2)
        print("İşlem sonlandırıldı.")
        break
    
    else:
        print("Yanlış işlem numarasını girdiniz. Lütfen menüdeki numaralara uyunuz!")
        break