import time
from selenium import webdriver

def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    print(log_text)
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()

global_delay = 0.5
driver = webdriver.Chrome()
log('Bu program Can Tarafından Yapılmıştır.')
log('https://fastuptime.com ve https://speedsmm.com üzerinden bize ulaşabilirsiniz.')
log('Program başlatıldı')

urun_url = 'https://www.trendyol.com/trendypassion/sirt-pusula-baskili-tshirt-p-260271556' # Ürün URL NOT SONUNA / KOYMAYIN

try:
    driver.get(urun_url + "/yorumlar")
    time.sleep(5)
    kac_yorum_var = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/div[1]/div/div[2]/span[2]').text
    kac_yorum_var = kac_yorum_var.replace(" Yorum", "")
    log('Toplam ' + kac_yorum_var + ' yorum var.')
    for i in range(int(kac_yorum_var)):
        try:
            yorum = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/div[3]/div[4]/div[' + str(i) + ']/div[1]/div/p').text
            log('Yorum: '+ yorum)
            yorum_file = open("yorumlar.txt", "a", encoding='utf-8')
            yorum_file.write(yorum + "\n")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(global_delay)
        except:
            continue
except Exception as e:
    log('Hata: ' + str(e))
    log('Program sonlandı')
    driver.quit()
    exit()