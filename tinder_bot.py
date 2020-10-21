from selenium import webdriver
from time import sleep
import random
from datetime import datetime


from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(5)

        login_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        login_btn.click()

        sleep(2)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(5)

        self.driver.switch_to.window(base_window)

        try:
            popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_1.click()

            popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_2.click()
        except Exception as e:
            print(e)

    def like2(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike2(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()


    def auto_swipe(self):
        counter = 100
        while True:
            # datetime object containing current date and time
            now = datetime.now()
 
            # dd/mm/YY H:M:S
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("date and time now = ", dt_string)

            counter += 1
            if counter % 50 == 0:
                print("Sleeping for 10 minute")
                sleep(60 * 10)
            elif counter % 300 == 0:
                print("Sleeping for 1 hours")
                sleep(60 * 60 * 1)
            else:
                print("Sleeping for 3 seconds")
                sleep(10)

            p = [2, 1, 1, 1, 2, 1, 1, 1, 1, 2]
            try:
                r = random.randint(0, 9)
                print(r)

                if p[r] % 2 == 1:
                    print("Like")
                    self.like()
                else:
                    print("Dislike")
                    self.dislike()
            except Exception as e:
                try:
                    print(e)
                    self.close_popup()
                except Exception as e:
                    print(e)
                    self.close_match()

    def close_popup(self):
        try:
            popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
            popup_3.click()
        except Exception as e:
            print(e)

    def close_match(self):
        try:
            match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
            match_popup.click()
        except Exception as e:
            print(e)

bot = TinderBot()
bot.login()
sleep(10)
bot.auto_swipe()
