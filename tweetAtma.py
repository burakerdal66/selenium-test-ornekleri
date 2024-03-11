import time #zamanla ilgili işlemler için kullanılr
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

kul_adi = "kullanici_adiniz.com"
sifre = "Sifreniz"
yazmaYeri='/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
yazi = "Herkese merhaba bu bir selenium denemesidir."

ileri = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]'
giris = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
gonderiAt = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
sifreinput = '[autocomplete="current-password"]'
postTusu = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]'

tweetGirdisi='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div'
driver = webdriver.Chrome()
url = 'https://www.twitter.com/login'
homeUrl = 'https://www.twitter.com/home'
driver.get(url)
wait = WebDriverWait(driver, 3)
driver.maximize_window() # ekranı tam ekran yapıyor
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[autocomplete="username"]'))).send_keys(kul_adi)
time.sleep(3)
next_button = wait.until(EC.presence_of_element_located((By.XPATH, ileri))) #yukarıda ileri olarak tanımlı xpati entegre eder.
next_button.click()
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, sifreinput))).send_keys(sifre)

login_butonu = wait.until(EC.presence_of_element_located((By.XPATH, giris)))
login_butonu.click()

tweetTusu = wait.until(EC.presence_of_element_located((By.XPATH, gonderiAt)))
tweetTusu.click()

wait.until(EC.element_to_be_clickable((By.XPATH, yazmaYeri))).send_keys(yazi)

post_butonu = wait.until(EC.presence_of_element_located((By.XPATH, postTusu)))
post_butonu.click()