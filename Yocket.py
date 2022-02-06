from ast import Bytes
from concurrent.futures import thread
import time
import selenium as s
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
current_url = driver.current_url
driver.get("https://yocket.com/college-finder")

time.sleep(15)
driver.switch_to.frame("siqiframe")
driver.find_element_by_xpath("//div[@documentclick='min_iframe']").click()
time.sleep(3)
driver.switch_to.parent_frame()
driver.find_element_by_xpath('//a[@href="/college-finder/masters"]//button[@class="w-full sm:w-auto px-4 py-1 sm:px-10 text-xl text-white bg-orange-400 border border-transparent rounded-md shadow-sm hover:bg-orange-500 focus:outline-none "]').click()
time.sleep(3)
Country= driver.find_element_by_xpath("//input[@placeholder='Select Country']").send_keys("United States")
time.sleep(1)
Country= driver.find_element_by_xpath("//input[@placeholder='Select Country']").send_keys(Keys.ENTER)
time.sleep(3)
courseName= driver.find_element_by_xpath("//input[@placeholder='Select Major']").send_keys("MBA")
time.sleep(3)
courseName= driver.find_element_by_xpath("//input[@placeholder='Select Major']").send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element_by_xpath('//button[@class="px-6 py-2 sm:px-8 sm:py-1 text-sm font-medium text-white bg-orange-500 border border-transparent rounded-md shadow-sm hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"]').click()
time.sleep(3)
driver.switch_to.parent_frame()
#undergrad info
College=driver.find_element_by_xpath("//input[@placeholder='Select College']").send_keys("Prasanna Engineering And Technology")
time.sleep(3)
College=driver.find_element_by_xpath("//input[@placeholder='Select College']").send_keys(Keys.ENTER)
time.sleep(3)
Stream=driver.find_element_by_xpath("//input[@placeholder='Select Major']").send_keys("Computer Science")
time.sleep(3)
Stream=driver.find_element_by_xpath("//input[@placeholder='Select Major']").send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath("//input[@id='marks']").send_keys("8")
time.sleep(3)
driver.find_element_by_xpath('//button[@class="px-6 py-2 sm:px-8 sm:py-1 text-sm font-medium text-white bg-orange-500 border border-transparent rounded-md shadow-sm hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"]').click()
time.sleep(3)

#all exam scores
#TOEFL
driver.switch_to.parent_frame()
driver.find_element_by_xpath("//div[contains(@class,'text-sm') and text()='TOEFL']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='toefl_overall_score']").send_keys("110")
#gmat 
driver.find_element_by_xpath("//div[contains(@class,'text-sm') and text()='GMAT']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='total_gmat_score']").send_keys("730")
time.sleep(3)
driver.find_element_by_xpath('//button[@class="px-6 py-2 sm:px-8 sm:py-1 text-sm font-medium text-white bg-orange-500 border border-transparent rounded-md shadow-sm hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"]').click()
driver.find_element_by_xpath('//input[@class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full pl-7 pr-16 shadow-sm sm:text-sm border border-gray-200 rounded-md"]').click()
time.sleep(3)
#Project and Thesis Info
driver.switch_to.parent_frame()
driver.find_element_by_xpath('//input[@class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full pl-7 pr-16 shadow-sm sm:text-sm border border-gray-200 rounded-md"]').send_keys("20")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='project']").send_keys("2")
driver.find_element_by_xpath("(//div[@class='bg-white border border-gray-200 focus:outline-none py-2 px-4 shadow-sm rounded-md cursor-pointer flex justify-center items-center mt-2 text-gray-700'])[2]").click()
time.sleep(3)
driver.find_element_by_xpath('//button[@class="px-6 py-2 sm:px-8 sm:py-1 text-sm font-medium text-white bg-orange-500 border border-transparent rounded-md shadow-sm hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"]').click()
time.sleep(3)








