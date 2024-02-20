import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def log_admin():
    """_summary_

    Returns:
        _type_: _description_
    """
    driver = webdriver.Chrome()

    driver.get("http://localhost:8000/admin/login/?next=/admin/")

    time.sleep(5)

    username_input = driver.find_element(By.NAME,"username")
    password_input = driver.find_element(By.NAME,"password")

    username_input.send_keys("root")
    password_input.send_keys("root")

    submit_button = driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div/form/div[3]/input")
    submit_button.click()
    time.sleep(5)

    current_url = driver.current_url

    driver.close()
    return current_url

def lenght_base():
    """_summary_

    Returns:
        _type_: _description_
    """
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/")

    time.sleep(5)
    
    len_base = driver.find_element(By.NAME,"count")

    lenght = len_base.text

    driver.close()

    return lenght

class Test_clubs(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def setUp(self) -> None:
        return None

    def test_log_admin(self):
        """_summary_
        """
        self.assertEqual(log_admin(), "http://localhost:8000/admin/")

    def test_lenght_base(self):
        """_summary_
        """
        count = lenght_base()
        self.assertEqual(count,"117389")



if __name__ == "__main__":
    unittest.main()