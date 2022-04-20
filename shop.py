# from selenium import webdriver
# import time
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
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# book_html5 =driver.find_element_by_tag_name('[src="http://practice.automationtesting.in/wp-content/uploads/2017/01/Mastering-HTML5-Forms-300x300.jpg"]').click()
# book_html5_name = driver.find_element_by_tag_name('[itemprop="name"]')
# book_html5_name_text = book_html5_name.text
# assert "HTML5 Forms" in book_html5_name_text


# from selenium import webdriver
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
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# html_btn = driver.find_element_by_tag_name('[href="http://practice.automationtesting.in/product-category/html/"]').click()
# items_3_checked = driver.find_elements_by_css_selector(".attachment-shop_catalog.size-shop_catalog.wp-post-image")
# if len(items_3_checked) == 3:
#     print("3")
# else:
#     print("Не 3")
#
#
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
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
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# defolt_sel = driver.find_element_by_class_name("orderby")
# select=Select(defolt_sel)
# sel_def = select.select_by_value("menu_order")
# defolt_sel_checked = defolt_sel.get_attribute("selected")
# print("Выбрано ли по умолчанию? ")
# if sel_def == defolt_sel_checked:
#     print("Да")
# else:
#     print("Нет")
# def_select2 = select.select_by_value("menu_order")
# select2 = Select(defolt_sel)
# price_desc = select2.select_by_value("price-desc")
# defolt_sel = driver.find_element_by_class_name("orderby")
# price_desc2 = defolt_sel.get_attribute("selected")
# print("Выбрано ли по убыванию? ")
# if price_desc == price_desc2:
#     print("Да")
# else:
#     print("Нет")
# driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.implicitly_wait(3)
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
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# android_book = driver.find_element_by_tag_name('[src="http://practice.automationtesting.in/wp-content/uploads/2017/01/Android-Quick-Start-Guide-300x300.png"]').click()
# old_price = driver.find_element_by_css_selector(".price > del > span")
# old_price_text = old_price.text
# assert old_price_text == "₹600.00"
# new_price = driver.find_element_by_css_selector(".price >ins >span")
# new_price_text = new_price.text
# assert new_price_text == "₹450.00"
# img_andr = driver.find_element_by_tag_name('[src="http://practice.automationtesting.in/wp-content/uploads/2017/01/Android-Quick-Start-Guide-600x600.png"]').click()
# img_android = WebDriverWait(driver,3).until(
#     EC.presence_of_element_located((By.ID, "fullResImage")))
# esc_window = WebDriverWait(driver,3).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "pp_close")))
# esc_window2 = driver.find_element_by_class_name("pp_close").click()
# driver.quit()




# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# html5_book = driver.find_element_by_tag_name('[src="http://practice.automationtesting.in/wp-content/uploads/2017/01/HTML5-Web-Application-Development-Beginners-guide-300x300.jpg"]').click()
# add_to_cart = driver.find_element_by_class_name("single_add_to_cart_button").click()
# time.sleep(1)
# tabs_cat_price = driver.find_element_by_css_selector("span.amount:nth-child(3)")
# tabs_cat_text = tabs_cat_price.text
# tabs_cat_qua = driver.find_element_by_class_name("cartcontents")
# tabs_cat_qua_text = tabs_cat_qua.text
# assert tabs_cat_text == "₹180.00" and tabs_cat_qua_text == "1 Item"
# cart = driver.find_element_by_class_name("wpmenucart-contents").click()
# subtotal_opt = WebDriverWait(driver, 4).until(
#     EC.text_to_be_present_in_element((By.XPATH, "//div/div/table/tbody/tr[1]/td/span[1]"), "₹180.00"))
# total_opt = WebDriverWait(driver, 4).until(
#     EC.text_to_be_present_in_element((By.XPATH, "//strong"), "₹189.00"))
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# html5_book = driver.find_element_by_tag_name('[src="http://practice.automationtesting.in/wp-content/uploads/2017/01/HTML5-Web-Application-Development-Beginners-guide-300x300.jpg"]').click()
# add_to_cart = driver.find_element_by_class_name("single_add_to_cart_button").click()
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, 700);")
# JS_book = driver.find_element_by_tag_name('[src="http://practice.automationtesting.in/wp-content/uploads/2017/01/Learning-JavaScript-Data-Structures-and-Algorith-300x300.jpg"]').click()
# add_to_cart2 = driver.find_element_by_class_name("single_add_to_cart_button").click()
# cart = driver.find_element_by_class_name("wpmenucart-contents").click()
# time.sleep(1)
# remove_book = driver.find_element_by_xpath('//tbody/tr[1]/td[1]/a')
# remove_book.click()
# time.sleep(1)
# undo_btn = WebDriverWait(driver, 3).until(
#     EC.element_to_be_clickable((By.XPATH, '//div[2]/div/div/div/div/div[1]/div[1]/a')))
# undo_btn.click()
# quantity_JS = driver.find_element_by_tag_name('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# quantity_JS.click()
# quantity_JS.clear()
# quantity_JS.send_keys("3")
# update_basket = driver.find_element_by_tag_name('[value="Update Basket"]').click()
# quantity_JS_checked = quantity_JS.get_attribute("value")
# assert quantity_JS_checked == "3"
# time.sleep(1)
# apply_coupon = driver.find_element_by_tag_name('[value="Apply Coupon"]').click()
# time.sleep(1)
# prompt_script = driver.execute_script("prompt('Please enter a coupon code.');")
# prompty = driver.switch_to.alert
# prompty.send_keys("H32dsfvv")
# time.sleep(1)
# prompty.accept()



# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# driver.execute_script("window.scrollBy(0, 300);")
# html5_book = driver.find_element_by_tag_name('[href="/shop/?add-to-cart=182"]').click()
# time.sleep(1)
# cart = driver.find_element_by_class_name("wpmenucart-contents").click()
# checkpoint = WebDriverWait(driver,3).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
# checkpoint.click()
# first_name_waiting = WebDriverWait(driver,8).until(
#     EC.element_to_be_clickable((By.ID, "billing_first_name")))
# first_name_waiting.send_keys("John")
# last_name = driver.find_element_by_id("billing_last_name")
# last_name.send_keys("Connor")
# email = driver.find_element_by_id("billing_email")
# email.send_keys("JohnConnor_official@terminator.com")
# phone_num = driver.find_element_by_id("billing_phone")
# phone_num.send_keys("81234567890")
# time.sleep(1)
# selector = driver.find_element_by_id("s2id_billing_country").click()
# selector2 = driver.find_element_by_id("s2id_autogen1_search")
# selector3 = selector2.send_keys("Georgia")
# selector_georgia = driver.find_element_by_class_name("select2-match").click()
# address = driver.find_element_by_id("billing_address_1")
# address.send_keys("Jonh Connor street building 70436")
# city_town = driver.find_element_by_id("billing_city")
# city_town.send_keys("New York")
# state_county = driver.find_element_by_id("billing_state")
# state_county.send_keys("Brooklyn")
# zip = driver.find_element_by_id("billing_postcode")
# zip.send_keys("697Ne245")
# driver.execute_script("window.scrollBy(0,600);")
# time.sleep(2)
# check_payments = driver.find_element_by_id("payment_method_cheque").click()
# place_order = driver.find_element_by_id("place_order").click()
# received = WebDriverWait(driver, 8).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "woocommerce-thankyou-order-received")))
# payment_checked = WebDriverWait(driver, 8).until(
#     EC.presence_of_element_located((By.XPATH, "//li[4]/strong")))
# driver.quit()