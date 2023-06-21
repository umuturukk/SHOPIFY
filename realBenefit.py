from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep
import csv
from tkinter import messagebox
import pandas as pd

def print_hugy():
    letters = {
        'H': ['*   *', '*   *', '*****', '*   *', '*   *'],
        'U': ['*   *', '*   *', '*   *', '*   *', '*****'],
        'G': ['*****', '*    ', '*    ', '* ***', '*****'],
        'Y': ['*   *', '*   *', ' *** ', '  *  ', '  *  ']
    }
    
    for i in range(5):
        for letter in 'HUGY':
            print(letters[letter][i], end='  ')
        print()

def toplamKariHesapla():
    global toplamKar
    df = pd.read_csv("KAR_KAYIT.csv")
    toplamKar = df["Günlük TL Karı"].sum()
    gecenGun = len(df.index)
    print(f"Bugüne kadar geçen {gecenGun} günlük süre zarfında yapılan toplam Türk Lirası karınız: {toplamKar:.2f} ₺")
    return toplamKar

def toplamReklamMaliyetiHesapla():
    global toplamReklam
    df = pd.read_csv("KAR_KAYIT.csv")
    toplamReklam = df["Reklam Maliyeti"].sum()
    gecenGun = len(df.index)
    print(f"Bugüne kadar geçen {gecenGun} günlük süre zarfında yapılan toplam reklam harcamanız: {toplamReklam:.2f} ₺\nGünlük ortalama {toplamReklam/gecenGun} ₺ reklam harcamanız var.")

print_hugy()
print(26*"-")
print(3*" " + "Shopify İşlem Menüsü" + 3*" ")
print(26*"-")

print("1-) İstenilen Kara Göre Ürün Fiyatının Belirlenmesi\n2-) Reklam Performansına Göre Kar Miktarı\n3-) Günümüze Kadar Geçen Sürede Yapılmış Kar Miktarı\n4-) Günümüze Kadar Geçen Sürede Yapılan Reklam Harcaması Miktarı")
sleep(0.5)

while True:
    islem = input("İşlem Gir: ")

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

        tlKar = tl*urunSatisAdedi
        if tlKar > 3000:
            metin = f"Bravo Dostum! {datetime.now().date()} tarihindeki karın 3000 Türk Lirası'nın üstünde.\nBöyle devamm!"
            messagebox.showinfo("Güzel Kar", metin)

        messagebox.showinfo("Başarılı İşlem", "Veriler başarıyla '.csv' dosyasına kaydedildi.")
        break
    
    elif islem == "3":
        toplamKariHesapla()
        metin = f"Toplam kar başarıyla hesaplandı bugüne kadar geçen sürede yapmış olduğunuz TL karınız {toplamKar:.2f} ₺"
        messagebox.showinfo("Toplam Kar", metin)
        break 

    elif islem == "4":
        toplamReklamMaliyetiHesapla()
        metin = f"Toplam reklam maliyeti hesaplandı. Bugüne kadar geçen sürede yapmış olduğunuz reklam harcamanız {toplamReklam:.2f} ₺"
        messagebox.showinfo("Toplam Reklam Harcaması", metin)
        break

    elif islem == "q":
        break

    else:
        print("Yanlış işlem numarasını girdiniz.\nLütfen menüdeki numaralara uyunuz ve yeniden bir numara girmeyi deneyiniz.\nSistemden çıkmak istiyorsanız q'ya basınız.")