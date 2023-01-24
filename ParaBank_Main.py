import time
import unittest
from selenium import webdriver
from ParaBank_Item import ParaBankItem
from ParaBank_Search import ParaBankSearch
from selenium.webdriver.chrome.service import Service

class ParaBankEqual(unittest.TestCase):
#--------------------------------------#
    def setUp(self):
        self.driver_service = Service(executable_path='C:/WebDriver/chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm')
        self.driver.implicitly_wait(5)
        self.search = ParaBankSearch(self.driver)
        self.item = ParaBankItem(self.driver)
    #----------------------------------------#
    def test_login(self):
        self.search.customerLogin('john', 'demo')
        self.assertTrue('Accounts Overview' in self.item.banner())
            
    def test_new_account(self):
        self.search.customerLogin('john', 'demo')
        self.search.openAccount()
        self.assertTrue('ParaSoft Demo Website' in self.item.account_text())
            
    def test_accounts_overview(self):
        self.search.customerLogin('john', 'demo')
        self.search.openAccount()
        self.search.account_overview()
        self.assertTrue('Account Details' in self.item.account_overview())

    def test_transfer_funds(self):
        self.search.customerLogin('john', 'demo')
        self.search.transfer_funds('200')
        self.assertEqual(self.item.transfer_mount(), '200')
    
    def test_find_transaction(self):
        self.search.customerLogin('john', 'demo')
        self.search.transfer_funds('200')
        self.search.find_transfer('200')
        time.sleep(1)
        self.assertTrue('Transaction Results' in self.item.transaction_result())

    def test_update_info(self):
        self.search.customerLogin('john', 'demo')
        self.search.update_info('1100101101011')
        time.sleep(3)
        self.assertTrue('Profile Updated' in self.item.profile_update())

    def test_request_loan(self):
        self.search.customerLogin('john', 'demo')
        self.search.request_loan(100, 50)
        time.sleep(1)
        self.assertTrue('Loan Request Processed' in self.item.loan_request())

    def test_bill_payment(self):
        self.search.customerLogin('john', 'demo')
        self.search.bill_payment(
            'Krys',
            'NIN',
            'buenosaires',
            'capital',
            '0123',
            '1234567',
            '1111111',
            '1111111',
            '100'
        )
        time.sleep(1)
        self.assertTrue('Bill Payment Complete' in self.item.bill_pay())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()        
#--------------------------#        
if __name__ == '__main__':
    unittest.main()