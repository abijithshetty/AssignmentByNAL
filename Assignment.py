from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://petdiseasealerts.org/forecast-map/#/")
mapFrame = driver.find_element(By.XPATH,"//iframe[contains(@id, 'map-instance')]")
driver.switch_to.frame(mapFrame)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[name()='svg']//*[local-name()='g' and @class='region']")))
states = driver.find_elements(By.XPATH,"//*[name()='svg']//*[local-name()='g' and @class='region']")
stateCount=0
statesToBeClicked = ["california","maryland","new-york"]
for state in states:
    print(state.get_attribute("id"))
    if(str(state.get_attribute("id")) in statesToBeClicked):
        state.click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='map-component']/ul/li[1]/a")))
        driver.find_element(By.XPATH,"//*[@id='map-component']/ul/li[1]/a").click()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
             (By.XPATH, "//*[name()='svg']//*[local-name()='g' and @class='rpath']//*[local-name()='path']")))
    stateCount= 1+stateCount
print("No of states in the map = " + str(stateCount))

