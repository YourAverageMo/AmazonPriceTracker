import lxml
import requests
from bs4 import BeautifulSoup

# --------------- SCRAP AMAZON URL ---------------


def scrape():
    """asks user for an amazon url to scrap for price->

    Returns:
        scrap_dump.text: web scrap data saved into local dir 
    """
    url = input(
        "What is the URL of the Amazon product you want to scrap for price?\n")
    headers = {
        "User-Agent": "Defined",
        "Accept-Language": "en-US,en;q=0.9",
    }
    scrape_data = requests.get(url, headers=headers).text
    return scrape_data


# --------------- SOUP ---------------
def get_price(scrape_data):
    soup = BeautifulSoup(scrape_data, "lxml")

    raw_data = soup.find(name="div",
                         class_="a-section a-spacing-none aok-align-center")
    price_str = raw_data.find(name="span", class_="a-offscreen").getText()
    price = float(price_str.split("$")[1])
    print("")
    print(price)


get_price(scrape())

# again same thing with the email im leaving this project here with no notification functionality because of the security issues.