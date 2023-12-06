from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#Driver initialization
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

########################### Custom data #########################################
# WARNING - commands works only with ru interface !!!
link = 'https://preview.edvibe.com/'
email = 'test.qa.edvibe@gmail.com' #test.qa.edvibe@gmail.com / test.qa.shool@gmail.com
password = 'liveUT00mPE8CB7Z'
choose = '1' # '1' - Teacher, '2' - School
catalog_or_personal = '1' # '1' - filters in catalog materials, '2' - filters in personal materials
######################################################################################

#login actions and go to material page
driver.maximize_window()
driver.get(f'{link}Account/Login')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Email']"))).send_keys(email)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Password']"))).send_keys(password)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button"))).click()
if choose == '1':
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[.="Teacher\'s account"]'))).click()
    except:
        pass
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".main_preloader__wr")))
    driver.get(f'{link}TeacherAccount/materials/catalogue')
else:
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[.="Online school"]'))).click()
    except:
        pass
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".main_preloader__wr")))
    driver.get(f'{link}school/courses/catalogue')

###Set filters in catalog###
if catalog_or_personal == '1':
    pass
else:
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".main_preloader__wr")))
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Личные']"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-filter-button"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите язык']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='tag']/div[contains(.,'English')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите язык']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите возраст']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='scroll-content']/div[contains(.,'Подростки')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите возраст']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите уровень']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='scroll-content']/div[contains(.,'Pre-intermediate')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите уровень']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите тип']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='scroll-content']/div[contains(.,'Общий')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите тип']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите навык']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='scroll-content']/div[contains(.,'Говорение')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите навык']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите время']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='scroll-content']/div[contains(.,'60 минут')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите время']"))).click()
#From here driver choose first tag from available tags
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите грамматику']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='tag']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите грамматику']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите лексику']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='tag']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите лексику']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите функции']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='tag']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите функции']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите тег']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='tag']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Выберите тег']"))).click()

###Apply and asserts###
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-footer']/div[contains(.,'Применить')]"))).click()
#First assert
count_of_filters = driver.find_element(By.CSS_SELECTOR, ".count").text
assert count_of_filters == '10' # Check count of filters
print('Count filters - OK')
#Reset filters assert
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-filter-button"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".reset-button"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-footer']/div[contains(.,'Применить')]"))).click()
assert WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".count"))) #Check, that filters clear now
print('Reset filters - OK')