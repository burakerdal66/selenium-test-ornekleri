import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

btcDegeri = '/html/body/section/div[1]/div[1]/div[5]/div/div/div[2]/div/table/tbody/tr[2]/td[3]'
degisimOrani = '/html/body/section/div[1]/div[1]/div[5]/div/div/div[2]/div/table/tbody/tr[2]/td[4]'
saat = '/html/body/section/div[1]/div[1]/div[5]/div/div/div[2]/div/table/tbody/tr[2]/td[5]'

driver = webdriver.Chrome()
url = "https://finans.mynet.com/kripto-para/"
driver.get(url)
wait = WebDriverWait(driver, 3)
driver.maximize_window()
# klavyede pageDown tuşu yai aşağı tuşunu for dögüsüyle 19 kere tekrarlatma yapıyoruz
for i in range(1,19):
    wait.until(EC.presence_of_element_located((By.TAG_NAME,"body"))).send_keys(Keys.ARROW_DOWN)

# Belirlenen değerlerin XPATH ini bulma
btc_element = wait.until(EC.element_to_be_clickable((By.XPATH, btcDegeri)))
degisim_element = wait.until(EC.element_to_be_clickable((By.XPATH, degisimOrani)))
saat_element = wait.until(EC.element_to_be_clickable((By.XPATH, saat)))

# Verilerin text değerlerine ulaşırız.
btc_degeri = btc_element.text
degisim_orani = degisim_element.text
saat = saat_element.text

# Verileri dosyaya yazma kısmı
with open("bilgiler.txt", "w") as dosya:
    for i, j, k in zip(range(1, 11), range(1, 11), range(1, 11)):
        genelBasliklar = f'/html/body/section/div[1]/div[1]/div[5]/div/div/div[2]/div/table/tbody/tr[{i}]/td[1]/div/strong/a'
        sonDeger = f'/html/body/section/div[1]/div[1]/div[5]/div/div/div[2]/div/table/tbody/tr[{j}]/td[3]'
        saat = f'/html/body/section/div[1]/div[1]/div[5]/div/div/div[2]/div/table/tbody/tr[{k}]/td[5]'

        row_element = wait.until(EC.visibility_of_element_located((By.XPATH, genelBasliklar)))
        row_element2 = wait.until(EC.visibility_of_element_located((By.XPATH, sonDeger)))
        row_element3 = wait.until(EC.visibility_of_element_located((By.XPATH, saat)))

        row_text = row_element.text
        row_text2 = row_element2.text
        row_text3 = row_element3.text

        dosya.write(row_text + " -----" + row_text2 + " -----" + row_text3 + "\n")

# Tarayıcıyı kapatma
driver.quit()
