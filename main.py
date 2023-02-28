import requests
from bs4 import BeautifulSoup


url = "https://www.scholaro.com/db/Countries/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
ul_element = soup.find("ol", {'id': 'countriesList'})
li_elements = ul_element.find_all("li")
countries=[li.text.strip() for li in li_elements]

for country in countries:
    base_url = f"https://www.scholaro.com/db/Countries/{country}/Grading-System/"
    print("\n")
    print("Scraping data from:", country)

    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.findAll("div", {'class': 'col-md-6 mb-4'})
    for tab in table:
        college = tab.find("h2").text
        header = tab.find_all("th")
        header_row = [th.text.strip() for th in header]

        data_rows = tab.find_all("tr")
        table_data = []
        for row in data_rows:
            cells = row.find_all("td")
            row_data = [cell.text.strip() for cell in cells]
            table_data.append(row_data)

        print("\n")
        print(college)
        print(header_row)
        for row in table_data:
            print(row)
