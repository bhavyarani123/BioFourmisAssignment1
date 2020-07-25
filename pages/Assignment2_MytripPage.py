import time

class MytripPage():

    def __init__(self, driver):
       self.driver = driver

       self.fromCity_textbox_id = "fromCity"
       self.toCity_textbox_id = "toCity"
       self.departure_button_id = "departure"
       self.departDate_button_xpath = "//input[@id='departure']//p[text()='26']"
       self.return_button_id="return"
       self.returnDate_button_xpath = "//input[@id='return']//p[text()='29']"
       self.search_button_xpath = "//a[text()='search']"
       self.nonstop_checkbox_xpath = "//p[text()='IndiGo']"
       self.indigo_checkbox_xpath = "//p[text()='Non Stop']"
       self.flights_xpath = "//span[@class='airlineInfo-sctn']"


    def  Flight_booking(self, fromcity, tocity):
        self.driver.find_element_by_id(self.fromCity_textbox_id).sendkeys(fromcity)
        self.driver.find_element_by_id(self.toCity_textbox_id).sendkeys(tocity)
        self.driver.find_element_by_id(self.departure_button_id).click()
        self.driver.find_element_by_xpath(self.departDate_button_xpath).click()
        self.driver.find_element_by_id(self.departure_button_id).click()
        self.driver.find_element_by_id(self.return_button_id).click()
        self.driver.find_element_by_xpath(self.returnDate_button_xpath).click()
        self.driver.find_element_by_xpath(self.search_button_xpath).click()
        time.sleep(5)

        self.driver.find_element_by_xpath(self.nonstop_checkbox_xpath).click()
        self.driver.find_element_by_xpath(self.indigo_checkbox_xpath).click()
        flights = self.driver.find_elements_by_xpath(self.flights_xpath)

        totalFlights = len(flights)
        print("Total Number Of matching Flights", totalFlights)
