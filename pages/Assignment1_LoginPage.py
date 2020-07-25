class LoginPage():

    def __init__(self, driver):
       self.driver = driver

       self.username_textbox_id = "email"
       self.password_textbox_id = "passwd"
       self.login_button_xpath = "span[text()='Sign in']"


    def  login_App(self, username, password):
        self.driver.find_element_by_id(self.username_textbox_id).sendkeys(username)
        self.driver.find_element_by_id(self.password_textbox_id).sendkeys(password)
        self.driver.find_element_by_id(self.login_button_xpath).click()


