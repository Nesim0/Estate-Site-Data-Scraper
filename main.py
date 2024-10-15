from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get("https://www.emlakjet.com/satilik-konut/")

wait10 = 10
wait = WebDriverWait(browser, wait10)

elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._3qUI9q a")))
links = [element.get_attribute("href") for element in elements]

ilanlar_listesi = []

sayac =0
for i in links:
    browser.get(i)
    try:
        time.sleep(2)
        browser.fullscreen_window() #Since I can't click the accept cookie button, I make it full screen, otherwise I can't click the see more button!
        price = browser.find_element(By.CSS_SELECTOR,".R-RKDB").text
        locaiton = browser.find_element(By.XPATH,"//*[@id='harita']/div/div[2]/div/div[1]/p").text
        
        
        see_more = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".XoBBT3")))
        see_more.click()
        
        # İlan bilgileri 
        content = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "._3tH_Nw._3__dNM"))).text
        
        satirlar = content.strip().split("\n")
        
        ilan_bilgileri = {}
        
        for j in range(0, len(satirlar), 2):
            key = satirlar[j].strip() 
            value = satirlar[j + 1].strip()
            ilan_bilgileri[key] = value 
        
        ilan_bilgileri['Lokasyon'] = locaiton
        ilan_bilgileri['Fiyat'] = price
        ilan_bilgileri['Bağlantı'] = i
        ilanlar_listesi.append(ilan_bilgileri)
        print(str(sayac)+". İlan başarıyla eklendi!")
        sayac+=1
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

browser.close()

with open('emlak_bilgileri.json', 'w', encoding='utf-8') as f:
    json.dump(ilanlar_listesi, f, ensure_ascii=False, indent=4)

print("İlan bilgileri başarıyla kaydedildi.")

