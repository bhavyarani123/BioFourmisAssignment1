class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.women_button_link_text = "Women"
        self.dresses_button_xpath = "//a[@title='Dresses']"
        self.item_button_xpath = "//img[@src='http://automationpractice.com/img/p/8/8-home_default.jpg']"
        self.cart_button_xpath = "//div[@class='box-cart-bottom']//p[@id='add_to_cart']"
        self.proceedToCheckOut1_button_xpath = "//i[@class='icon-chevron-right right']"
        self.proceedToCheckOut2_button_xpath = "//span[text()='Proceed to checkout']"
        self.proceedToCheckOut3_button_xpath = "//span[text()='Proceed to checkout']"
        self.proceedToCheckOut4_button_xpath = "//span[text()='Proceed to checkout']"
        self.agree_Checkbox__id= "cgv"
        self.bankpayment_button_xpath= "//a[@class='bankwire']"
        self.confirmPayment_xpath = "//span[text()='I confirm my order']"

    def Shopping(self):
        self.women =self.driver.find_element_by_id(self.women_button_link_text)
        self.dresses = self.driver.find_element_by_xpath(self.dresses_button_xpath).click()
        self.driver.execute_script("arguments[0].click();arguments[1].click();", self.women, self.dresses)
        # time.sleep(5)
        self.driver.execute_script("window.scrollBy(0, 400);")

        self.item= self.driver.find_element_by_xpath(self.item_button_xpath).click()
        self.cart=self.driver.find_element_by_xpath(self.cart_button_xpath).click()
        self.driver.execute_script("arguments[0].click();arguments[1].click();", self.item, self.cart)

        # change to frame
        self.parent = self.driver.current_window_handle
        self.handles = self.driver.window_handles
        for i in self.handles:
            if (i not in self.parent):
                self.driver.switch_to.window(i)

        self.driver.find_element_by_xpath(self.proceedToCheckOut1_button_xpath).click()
        self.driver.switch_to.window(self.parent)
        self.driver.execute_script("window.scrollBy(0, 600);")

        self.driver.find_element_by_xpath(self.proceedToCheckOut2_button_xpath).click()
        self.driver.execute_script("window.scrollBy(0, 600);")

        self.driver.find_element_by_xpath(self.proceedToCheckOut3_button_xpath).click()
        self.driver.execute_script("window.scrollBy(0, 600);")

        self.driver.find_element_by_id(self.agree_Checkbox__id).click()
        self.driver.find_element_by_xpath(self.proceedToCheckOut4_button_xpath).click()
        self.driver.execute_script("window.scrollBy(0, 600);")

        self.driver.find_element_by_xpath(self.bankpayment_button_xpath).click()
        self.driver.find_element_by_xpath(self.confirmPayment_xpath).click()

        print("Order confirmed successfully")



