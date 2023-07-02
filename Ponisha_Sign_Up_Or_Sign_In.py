# Librarys
# --------------------------------------------------------------------------------------------
from selenium import webdriver
from time import sleep
# --------------------------------------------------------------------------------------------
# Sign In Function
# --------------------------------------------------------------------------------------------
def Sign_In(inp_User,inp_Pas):
    driver.find_element_by_xpath('//*[@id="username"]').clear()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(inp_User)
    sleep(3)
    driver.find_element_by_xpath('//*[@id="password"]').clear()
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(inp_Pas)
    sleep(3)
    driver.find_element_by_xpath('//*[@id="login-btn"]').click()
    # UserName = '//*[@id="username"]'
    # PassWord = '//*[@id="password"]'
    # Sign_in = '//*[@id="login-btn"]'
# --------------------------------------------------------------------------------------------
# Sign Up Function
# --------------------------------------------------------------------------------------------
def Sign_Up(inp_User,inp_Pas,inp_Email,inp_FOK):
    driver.find_element_by_xpath('//*[@id="username"]').clear()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(inp_User)
    sleep(3)
    driver.find_element_by_xpath('//*[@id="email"]').clear()
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(inp_Email)
    sleep(3)
    driver.find_element_by_xpath('//*[@id="password"]').clear()
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(inp_Pas)
    sleep(3)
    if inp_FOK.lower() == "freelancer":
        driver.find_element_by_xpath('//*[@id="register"]/div/div/div/form/div[5]/div[1]/div').click()
    elif inp_FOK.lower() == "karfarma":
        driver.find_element_by_xpath('//*[@id="register"]/div/div/div/form/div[5]/div[2]/div').click()
    else:
        print("Invailed!")
    sleep(3)
    driver.find_element_by_xpath('//*[@id="register-btn"]').click()
    # UserName = '//*[@id="username"]'
    # Email = '//*[@id="email"]'
    # PassWord = '//*[@id="password"]'
    # sign_up = '//*[@id="register-btn"]'
    # Lable_Freelancer = '//*[@id="register"]/div/div/div/form/div[5]/div[1]/div'
    # Lable_karfarma = '//*[@id="register"]/div/div/div/form/div[5]/div[2]/div'
# --------------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------------
inp = input("Sign in or Sign Up? \n")
driver = webdriver.Chrome(executable_path=r"C:\Users\sepeh\Desktop\Selenium\chromedriver.exe")
driver.get("https://ponisha.ir/")
if inp.lower() == "sign up":
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/button").click()
    #inp_User1 = input("Please Enter A UserName :\n")
    inp_User1 = "sepehr123rt"
    #inp_Pas1 = input("Please Enter A PassWord :\n")
    inp_Pas1 = "0023959533@"
    #inp_Email = input("Please Enter A Email :\n")
    inp_Email = "emailkhodam1236@yahoo.com"
    #inp_FOK = input("Are You Freelancer Or Karfarma?\n")
    inp_FOK = "freelancer"
    Sign_Up(inp_User1,inp_Pas1,inp_Email,inp_FOK)
elif inp.lower() == "sign in":
    driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div[2]/div[1]/div/a').click()
    inp_User = input("Please Enter A UserName :\n")
    #inp_User = 'sepehrmohamad20@gmail.com'
    inp_Pas = input("Please Enter A PassWord :\n")
    #inp_Pas = '0023959533'
    Sign_In(inp_User,inp_Pas)
else:
    print("Please Enter vailed Text")
fin = input("Finish?!")
while(fin.lower() == "yes"):
    break
# --------------------------------------------------------------------------------------------