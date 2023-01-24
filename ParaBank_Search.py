from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ParaBankSearch():
#----------------------#
    def __init__(self, driver):
        self.driver = driver
        self.user = 'username'
        self.password = 'password'
        self.login = '//*[@id="loginPanel"]/form/div[3]/input'
        self.open_account = '//*[@id="leftPanel"]/ul/li[1]/a'
        self.account_type = 'type'
        self.submit = 'button'
        self.overview = '//*[@id="leftPanel"]/ul/li[2]/a'
        self.account_number = '//*[@id="accountTable"]/tbody/tr[1]/td[1]/a'
        self.accountId = '//*[@id="accountId"]'  
        self.transfer = '//*[@id="leftPanel"]/ul/li[3]/a'
        self.amount = 'amount'
        self.trbuton = '//*[@id="rightPanel"]/div/div/form/div[2]/input'
        self.find = '//*[@id="leftPanel"]/ul/li[5]/a'
        self.find_ammount = 'criteria.amount'
        self.find_tran = '//*[@id="rightPanel"]/div/div/form/div[9]/button'
        self.update = '//*[@id="leftPanel"]/ul/li[6]/a'
        self.update_button = '//*[@id="rightPanel"]/div/div/form/table/tbody/tr[8]/td[2]/input'
        self.phone = 'customer.phoneNumber'
        self.loan = '//*[@id="leftPanel"]/ul/li[7]/a'
        self.loan_amount = 'amount'
        self.loan_payment = 'downPayment'
        self.loan_apply = '//*[@id="rightPanel"]/div/div/form/table/tbody/tr[4]/td[2]/input'
        self.billpayment = '//*[@id="leftPanel"]/ul/li[4]/a'
        self.payeename = '//*[@id="rightPanel"]/div/div[1]/form/table/tbody/tr[1]/td[2]/input'
        self.payeadress = 'payee.address.street'
        self.payeecity = 'payee.address.city'
        self.payeestate = 'payee.address.state'
        self.zipcode = '//*[@id="rightPanel"]/div/div[1]/form/table/tbody/tr[5]/td[2]/input'
        self.payeenumber = '//*[@id="rightPanel"]/div/div[1]/form/table/tbody/tr[8]/td[2]/input'
        self.payeverify = '//*[@id="rightPanel"]/div/div[1]/form/table/tbody/tr[9]/td[2]/input'
        self.payeamount = '//*[@id="rightPanel"]/div/div[1]/form/table/tbody/tr[11]/td[2]/input'
        self.sendpayment = '//*[@id="rightPanel"]/div/div[1]/form/table/tbody/tr[14]/td[2]/input'
        self.payephone = 'payee.phoneNumber'
    #--------------------------------------#    
    def customerLogin(self, item1, item2):
        self.driver.find_element(By.NAME, self.user).send_keys(item1)
        self.driver.find_element(By.NAME, self.password).send_keys(item2)
        self.driver.find_element(By.XPATH, self.login).click()
    
    def openAccount(self):
        self.driver.find_element(By.XPATH, self.open_account).click()
        drop = self.driver.find_element(By.ID, self.account_type)
        Select(drop).select_by_index(1)
        self.driver.find_element(By.CLASS_NAME, self.submit).click()
    
    def account_overview(self):
        self.driver.find_element(By.XPATH, self.overview).click()
        self.driver.find_element(By.XPATH, self.account_number).click()
    
    def transfer_funds(self, item):
        self.driver.find_element(By.XPATH, self.transfer).click()
        self.driver.find_element(By.ID, self.amount).send_keys(item)
        self.driver.find_element(By.XPATH, self.trbuton).click()
    
    def find_transfer(self, item):
        self.driver.find_element(By. XPATH, self.find).click()
        self.driver.find_element(By. ID, self.find_ammount).send_keys(item)
        self.driver.find_element(By. XPATH, self.find_tran).click()

    def update_info(self, item):
        self.driver.find_element(By. XPATH, self.update).click()
        self.driver.find_element(By. ID, self.phone).clear()
        self.driver.find_element(By. ID, self.phone).send_keys(item)
        self.driver.find_element(By. XPATH, self.update_button).click()
    
    def request_loan(self, item1, item2):
        self.driver.find_element(By. XPATH, self.loan).click()
        self.driver.find_element(By. ID, self.loan_amount).send_keys(item1)
        self.driver.find_element(By. ID, self.loan_payment).send_keys(item2)
        self.driver.find_element(By. XPATH, self.loan_apply).click()

    def bill_payment(self, item1, item2, item3, item4, item5, item6, item7, item8, item9):
        self.driver.find_element(By. XPATH, self.billpayment).click()
        self.driver.find_element(By. XPATH, self.payeename).send_keys(item1)
        self.driver.find_element(By. NAME, self.payeadress).send_keys(item2)
        self.driver.find_element(By. NAME, self.payeecity).send_keys(item3)
        self.driver.find_element(By. NAME, self.payeestate).send_keys(item4)
        self.driver.find_element(By. XPATH, self.zipcode).send_keys(item5)
        self.driver.find_element(By. NAME, self.payephone).send_keys(item6)
        self.driver.find_element(By. XPATH, self.payeenumber).send_keys(item7)
        self.driver.find_element(By. XPATH, self.payeverify).send_keys(item8)
        self.driver.find_element(By. XPATH, self.payeamount).send_keys(item9)
        self.driver.find_element(By. XPATH, self.sendpayment).click()
       #-------------------------------------------------------------#