from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
print(options)

ch = webdriver.Chrome(chrome_options=options)
ch.get("https://www.facebook.com.tw")
#ch.get("https://www.google.com.tw")

email = ch.find_element("id","email")
password = ch.find_element("id","pass")

email.send_keys("example@gmail.com")
password.send_keys("12345678")