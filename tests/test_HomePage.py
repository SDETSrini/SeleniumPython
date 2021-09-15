import pytest


# @pytest.mark.usefixtures("setup")
from core.BaseClass import BaseClass

# class TestHomePage():
class TestHomePage(BaseClass):

    # def test_HomePage(self, setup):
    def test_HomePageTitleValidation(self):
        expectedTitle = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
        actualTitle = self.driver.title

        # Code to verify the actual and Expected Title
        assert actualTitle == expectedTitle

    # def test_HomepageHeaderValidation(self, setup):
    def test_HomepageHeaderValidation(self):
        print("Code for Header validation")

  # def test_HomepageHeaderValidation(self, setup): - Sriraj
    def test_HomepageFooterValidation(self):
        print("Code for Footer validation")


 # def test_HomepageHeaderValidation(self, setup): - Rohit
    def test_HomepageFooter1Validation(self):
        print("Code for Footer1 validation")

# def test_HomepageHeader1Validation(self, setup): - Rohit
    def test_HomepageFooter2Validation(self):
        print("Code for Footer2 validation")

 # def test_HomepageHeader1Validation(self, setup): - Rohit
    def test_HomepageFooter3Validation(self):
            print("Code for Footer3 validation"

# def test_HomepageHeader1Validation(self, setup): - Rohit

    def test_HomepageFoote5Validation(self):
        print("Code for Footer5 validation")