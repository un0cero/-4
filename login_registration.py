# from selenium import webdriver
# import time
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# my_acc_m = driver.find_element_by_tag_name('[href="http://practice.automationtesting.in/my-account/"]').click()
# reg_log = driver.find_element_by_id("reg_email")
# reg_log.click()
# reg_log.send_keys("JohnConnor@terminator.com")
# reg_pass = driver.find_element_by_id("reg_password")
# reg_pass.click()
# reg_pass.send_keys("Terminatorforever!$!$%")
# reg_btn = driver.find_element_by_tag_name('[value="Register"]').click()
# time.sleep(1)
# driver.quit()
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# my_acc_m = driver.find_element_by_tag_name('[href="http://practice.automationtesting.in/my-account/"]').click()
# log_log = driver.find_element_by_id("username")
# log_log.click()
# log_log.send_keys("JohnConnor@terminator.com")
# log_pass = driver.find_element_by_id("password")
# log_pass.click()
# log_pass.send_keys("Terminatorforever!$!$%")
# log_btn = driver.find_element_by_tag_name('[value="Login"]').click()
# logout_check = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//div[1]/nav/ul/li[6]/a')))
