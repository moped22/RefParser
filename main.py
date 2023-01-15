# This is a scrapler html code from web page.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():

    url = "https://rabota.by/search/vacancy?area=1002&employment=full&employment=project&employment=probation&enable_snippets=true&experience=between1And3&items_on_page=100&label=not_from_agency&no_magic=true&order_by=publication_time&ored_clusters=true&professional_role=96&professional_role=156&professional_role=165&text=Python&search_period=7&hhtmFrom=vacancy_search_list"

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(url)
    driver.implicitly_wait(0.5)

    titles = driver.find_elements(by=By.CLASS_NAME, value='serp-item__title')
    for title in titles:
        print(title.text)
        print(title.get_property('href'), end='\n\n')


# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

