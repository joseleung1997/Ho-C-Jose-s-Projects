from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# import self as self
# from utility_methods.utility_methods import *
# import urllib.request
# import os


class InstagramBot:

    def __init__(self, username, password):
        """
        Initializes an instance of the InstagramBot class.

        Call the login method to authenticate a user with IG.

        Args:
            username:str: The Instagram username for a user
            password:str: The Instagram password for a user

        Attributes:
            driver: Selenium.webdriver.Chrome: The Chromedriver used to automate browser actions
        """
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        # #boots up chrome
        self.driver = webdriver.Chrome(service=Service('chromedriver.exe'))

        self.login()


    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(1)
        self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(10)

    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))

    def find_buttons(self, button_text):
        ''' Allows user to find the appropriate button within instagram format, the argument in the XPATH
            locates all elements with text in equal to function input)
        '''
        buttons = self.driver.find_elements(By.XPATH, "//*[text()='{}']".format(button_text))
        return buttons

    def follow_user(self, user):
        self.nav_user(user)
        time.sleep(5)
        follow_buttons = self.find_buttons('Follow')
        for btn in follow_buttons:
            btn.click()


    def unfollow_user(self, user):
        self.nav_user(user)
        time.sleep(5)
        unfollow_btns = self.find_buttons('Following')

        if unfollow_btns:
            for btn in unfollow_btns:
                btn.click()
                time.sleep(1)
                unfollow_confirmation = self.find_buttons('Unfollow')[0]
                unfollow_confirmation.click()
        else:
            print('No {} buttons were found.'.format('Following'))

    def search_tag(self, tag):
        '''
        Searches for posts with specific tag on.
        '''
        self.driver.get('https://www.instagram.com/explore/tags/{}'.format(tag))

    def like_latest_posts(self, user, n_posts, like=True):
        """
        .Extend adds a list to an end of a list
        It then identifies each clickable element from the first n number of posts on the profile.
        Clicks through each posts one by one than clicks the like button if its is unliked, clicks unlike if its is liked
        """

        action = 'Like' if like else 'Unlike'

        self.nav_user(user)
        time.sleep(5)
        imgs = []
        imgs.extend(self.driver.find_elements(By.CLASS_NAME,'_9AhH0'))

        for img in imgs[:n_posts]:
            img.click()
            time.sleep(1)
            try:
                self.driver.find_element(By.XPATH,"//*[@aria-label='{}']".format(action)).click()
            except Exception as e:
                print(e)

            # self.comment_post('beep boop testing bot')
            self.driver.find_elements(By.CLASS_NAME,'ckWGn')[0].click()

    def comment_post(self, user, text):
        '''
        Navigates to a user and comments your desired comments onto their first post.
        '''
        self.nav_user(user)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_99"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article[1]/div/div/div[1]/div[1]/a/div').click()
        time.sleep(3)
        cmt = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button')
        cmt.click() self.driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(text)
        self.driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(Keys.ENTER)


if __name__ == '__main__':

    ig_bot = InstagramBot('jsneakrs_1','Iamnolose12')
    # ig_bot.follow_user('thenotoriousmma')
    # ig_bot.unfollow_user('thenotoriousmma')
    # ig_bot.search_tag('KSI')
    ig_bot.like_latest_posts('thenotoriousmma', 1)