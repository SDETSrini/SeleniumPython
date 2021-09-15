import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass


    def search(self):
        print("Searching with a keyword")