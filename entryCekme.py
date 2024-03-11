import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# WebDriver'ı başlat
driver = webdriver.Chrome()

# URL'ye git
url = "https://eksisozluk.com/bitcoin--2462174?p="
sayfaSayisi=1
entries=[]
entryCount=1
while sayfaSayisi<=5:
    rastgeleSayi=random.randint(1,4093)
    yeniSayfa=url+str(rastgeleSayi)
    driver.get(yeniSayfa)
    time.sleep(1)
    sayfaSayisi+=1
#driver.get(url)

try:
    sayfaSayisi=1
    # Çerezlere izin ver butonunu bul ve tıkla
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='tümünü kabul et']"))).click()
    time.sleep(5)
    # Tüm entrylerin bulunduğu div elementini seç
    entrylerin_div = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "content")))
    # Entryleri yazdır
    with open("metinler.txt","w",encoding="UTF-8") as dosya:
        for entry in entrylerin_div:
         dosya.write(str(sayfaSayisi) + ".\n" + entry.text + "\n")
         dosya.write("-------------------------------------\n")
         sayfaSayisi+=1

finally:
    # WebDriver'ı kapat
    driver.quit()
