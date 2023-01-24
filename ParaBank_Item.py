from selenium.webdriver.common.by import By

class ParaBankItem():
#--------------------#
    def __init__(self, driver):
        self.driver = driver
        self.result_banner = '//*[@id="rightPanel"]/div/div/h1'
        self.accountText = '//*[@id="rightPanel"]/h1'
        self.accountOverview = '//*[@id="rightPanel"]/div/div[1]/h1'
        self.transfer_complete = 'amount'
        self.value = 'value'
        self.trnsaction = '//*[@id="rightPanel"]/div/div/h1'
        self.profileup = '//*[@id="rightPanel"]/div/div/h1'
        self.loanrequest = 'title'
        self.billpayment = '//*[@id="rightPanel"]/div/div[2]/h1'
    #-----------------------------------------------------#                              
    def banner(self):
        return self.driver.find_element(By. XPATH, self.result_banner).text
    
    def account_text(self):
        return self.driver.find_element(By.XPATH, self.accountText).text
    
    def account_overview(self):
        return self.driver.find_element(By.XPATH, self.accountOverview).text

    def transfer_mount(self):
        return self.driver.find_element(By.ID, self.transfer_complete).get_attribute(self.value)

    def transaction_result(self):
        return self.driver.find_element(By. XPATH, self.trnsaction).text
    
    def profile_update(self):
        return self.driver.find_element(By. XPATH, self.profileup).text

    def loan_request(self):
        return self.driver.find_element(By. CLASS_NAME, self.loanrequest).text

    def bill_pay(self):
        return self.driver.find_element(By. XPATH, self.billpayment).text