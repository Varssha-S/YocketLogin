import selenium as s
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
current_url = driver.current_url
driver.get("http://www.netflix.com")
#enter user mail and password
signIn = driver.find_element_by_xpath('//a[@href="/login"]').click()
eMail = driver.find_element_by_id('id_userLoginId').send_keys('mail')
passWord = driver.find_element_by_id('id_password').send_keys('password')
signIn=driver.find_element_by_xpath('//button[@class="btn login-button btn-submit btn-small"][@type="submit"]').click()
WebDriverWait(driver, 15).until(EC.url_changes(current_url))

print("Choosing your profile")
profiles = driver.find_elements_by_class_name("profile")
for profile in profiles:
        name = profile.find_element_by_class_name("profile-name").text
        if name == 'profile-name':
            profile_link = profile.find_element_by_class_name("profile-link")
            profile_link.click()
            break
sleep(2)

# click my list
print("Finding your list")
current_url = driver.current_url
my_list = driver.find_element_by_link_text("My List")
my_list.click()
WebDriverWait(driver, 15).until(EC.url_changes(current_url))

    # scroll down my list to load all titles
logo = driver.find_element_by_class_name("logo")
for n in range(1, 10):
    print("Getting list of movies...")
    logo.send_keys(Keys.END)
    sleep(1)

# list of movies:
movies_div = driver.find_elements_by_class_name("title-card")
movie_titles = [div.find_element_by_css_selector('a').get_attribute("aria-label") for div in movies_div]
