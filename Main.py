from selenium import webdriver
import time
import datetime
import os
import platform


path = os.path.dirname(os.path.abspath('Main.py'))
print(path)
chrome_driver = path + r"\chromedriver.exe"
print(chrome_driver)
url = r"http://mail.ru"
log_path = path + '\def.log'

def check_folders(): # функция проверяет наличие необходимых папок, при их отсутствии - создаёт
    for name in ['\Screen']:
        if not os.path.exists(path + name):
            os.makedirs(path + name)

def write_log(msg):
    f = open(r"def.log", "a")
    f.write(msg)
    f.close()

def save_screen_func(): # функция создаёт скриншот экрана и сохраняет по пути scrdir_today
    scrname = path + r'\\Screen' + r"\Screen" + time.strftime("%d.%m.%y_%H-%M-%S") + platform.node() + '.png'
    try:
        browser.save_screenshot(scrname)
        write_log("Скриншот ошибки сохранён" + '\n')
        #logging.log_info('Скриншот ошибки сохранён в %s' %scrname)
    except:
        write_log("Не удалось сохранить скриншот ошибки по пути")
    return
try:
   browser = webdriver.Chrome(chrome_driver)
   browser.maximize_window()
   browser.get(url)
   write_log("Тест запущен в " + time.strftime("%H.%M.%S") + '\n')
   time.sleep(2)
   if browser.find_element_by_xpath('//*[@id="ph_mail"]/span'):
       write_log('Страница загрузилась' +'\n')
   if browser.find_element_by_xpath('//*[@id="mailbox:login"]'):
       browser.find_element_by_xpath('//*[@id="mailbox:login"]').send_keys('test_testovich_tomsk')
       write_log('Ввод логина успешный' +'\n')
   if browser.find_element_by_xpath('//*[@id="mailbox:submit"]'):
        browser.find_element_by_xpath('//*[@id="mailbox:submit"]').click()
        write_log('Нажата кнопка Ввести пароль' + '\n')
   time.sleep(2)
   if browser.find_element_by_xpath('//*[@id="mailbox:password"]'):
       browser.find_element_by_xpath('//*[@id="mailbox:password"]').send_keys('1qaz@WSX3edc$RFV/')
       write_log('Введен пароль' + '\n')
       browser.find_element_by_xpath('//*[@id="mailbox:submit"]').click()
       write_log('Нажата кнопка Войти' + '\n')
   time.sleep(5)
   if browser.find_element_by_xpath('//*[@id="PH_logoutLink"]'):
        write_log('Успешный вход в почтовый ящик' + '\n')
        time.sleep(5)#Временная задержка, чтобы прогрузился список писем
        browser.find_element_by_xpath('//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div[1]/div/span').click()
        write_log('Открылось окно создания нового письма' + '\n')
        time.sleep(2)#Временная задержка, чтобы прогрузилась адресная книга
        browser.find_element_by_xpath('/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/label/div/div/input').send_keys('test_testovich_tomsk@mail.ru')  # Текст письма
        write_log('Ввод адресата письма' + '\n')
        browser.find_element_by_xpath('/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div/input').send_keys('Это тестовое письмо')# Тема письма
        write_log('Ввод темы письма' + '\n')
        browser.find_element_by_xpath('/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]').send_keys('Приветствую. Это тестовое письмо')# Кто
        write_log('Ввод текста письма письма' + '\n')
        browser.find_element_by_xpath('/html/body/div[15]/div[2]/div/div[2]/div[1]/span[1]/span/span').click()
        write_log('Нажатие кнопки "Отправить" ' + '\n')

except Exception as err:
   save_screen_func()
finally:
    #browser.close()
    #browser.quit()
    write_log("Тест завершен" + '\n')
