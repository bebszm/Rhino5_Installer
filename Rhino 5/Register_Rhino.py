'''
######################################################################################################################################################
Title         Python automated form filler
Purpose:      Assist with RHino5 setup
Creator:      Matthew, Bebsz 
Version:      1.0
######################################################################################################################################################
www.rhino3d.com/register?email=test@gmail.com&cdkey=0000-0000-0000-0000-0000-0000
###################################################################################
[INFO]
Needs Chrome installed. 
$url = 'https://dl.google.com/chrome/install/latest/chrome_installer.exe'; $file = "$env:USERPROFILE\Downloads\chrome_installer.exe"; (New-Object Net.WebClient).DownloadFile($url, $file)
Start-Process -FilePath "$env:USERPROFILE\Downloads\chrome_installer.exe" -ArgumentList "/silent /install" -Wait

Needs Selenim and web-driver-manager installed
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

py -m pip install selenium
py -m pip install webdriver-manager

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

## VARIABLES ##

email_input = "YOUR_EMAIL"
cdkey_input = "0000-0000-0000-0000-0000-0000"
name_input = "YOUR_NAME"
organization_input = "YOUR_ORG"
address1_input = "123 elmo Rd"
city_input = "failyland"
state_input = "CA"
country_value = "123"
zip_input = "11111"
phone_input = "YOUR_PHONE_NUMBER"

#--------------------------------------------------------------------------------------------------------------------#
######################################################################################################################
###########################[ EDIT AT YOUR OWN RISK, EDIT AT YOUR OWN RISK, EDIT AT YOUR OWN ]#########################
######################################################################################################################
#--------------------------------------------------------------------------------------------------------------------# 

# Set up ChromeDriver
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# Open the registration page
browser.get("https://www.rhino3d.com/register/")

# Find the email and cdkey input fields on the first page
email = browser.find_element(By.ID, "email")
cdkey = browser.find_element(By.ID, "cdkey")

# Enter text into the input fields on the first page
email.send_keys(email_input)
cdkey.send_keys(cdkey_input)

# Find and click the "Next" button on the first page
next_button = browser.find_element(By.XPATH, "//input[@name='direction_next' and @value='Next >']")
next_button.click()

# Find the input fields on the second page and fill them
name = browser.find_element(By.ID, "name")
organization = browser.find_element(By.ID, "organization")
address1 = browser.find_element(By.ID, "address1")
city = browser.find_element(By.ID, "city")
state = browser.find_element(By.ID, "state")
country_dropdown = Select(browser.find_element(By.ID, "country"))
zip = browser.find_element(By.ID, "zip")
phone = browser.find_element(By.ID, "phone")

# Send user input to form
name.send_keys(name_input)
organization.send_keys(organization_input)
address1.send_keys(address1_input)
city.send_keys(city_input)
state.send_keys(state_input)
country_dropdown.select_by_value(country_value)
zip.send_keys(zip_input)
phone.send_keys(phone_input)

# Find and click the "Next" button on the second page
next_button = browser.find_element(By.XPATH, "//input[@name='direction_next' and @value='Next >']")
next_button.click()

# Find and click the "Next" button on the third page
next_button = browser.find_element(By.XPATH, "//input[@name='direction_next' and @value='Next >']")
next_button.click()

# Find and click the "Next" button on the fourth page
next_button = browser.find_element(By.XPATH, "//input[@name='direction_next' and @value='Next >']")
next_button.click()

# Wait for user input before closing the browser
input("Press Enter to close the browser...")

# Close the browser
browser.quit()
