from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Safari() 
        self.username = username
        self.password = password
        self.followers = []
    
    def signin(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        self.browser.find_element(By.NAME, "username").send_keys(self.username)
        self.browser.find_element(By.NAME, "password").send_keys(self.password)
        self.browser.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        time.sleep(10)

    def followUser(self, username):
        self.browser.get("https://www.instagram.com/" + username + "/")
        time.sleep(5)
    def unfollowUser(self, username):
        self.browser.get("https://www.instagram.com/" + username + "/")
        time.sleep(5)
        
        try:
            follow_button = self.browser.find_element(By.TAG_NAME, "button")
            if follow_button.text == "Following" or follow_button.text == "Takiptesin":
                follow_button.click()
                time.sleep(2)
            
                unfollow_confirm = self.browser.find_element(By.XPATH, "//button[text()='Unfollow' or text()='Takipten Çık']")
                unfollow_confirm.click()
                
                print(f"{username} takipten çıkarıldı.")
                time.sleep(5)
            else:
                print(f"Zaten {username} kullanıcısını takip etmiyorsun.")
        except:
            print(f"{username} için takipten çıkma butonu bulunamadı.")
        try:
            follow_button = self.browser.find_element(By.TAG_NAME, "button")
            
            current_text = follow_button.text
            
            if current_text == "Follow" or current_text == "Takip Et":
                follow_button.click()
                print(f"{username} takip edildi!")
                time.sleep(5)
            else:
                print(f"Zaten {username} kullanıcısını takip ediyorsun. (Buton: {current_text})")
        except:
            print(f"{username} için takip butonu bulunamadı.")


instgrm = Instagram("KULLANICI_ADIN", "SIFREN")
instgrm.signin() 
instgrm.followUser("")
user_list = [""]
for user in user_list:
    instgrm.followUser(user)