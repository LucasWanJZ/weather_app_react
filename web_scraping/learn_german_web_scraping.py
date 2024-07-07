import requests
from bs4 import BeautifulSoup
import openpyxl

# URL of the webpage
url = "https://storylearning.com/learn/german/german-tips/german-conjunctions"

# Fetch the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Function to extract conjunctions and examples
def extract_conjunctions(soup):
    conjunctions = []
    sections = soup.find_all("h3")  # Assumes conjunctions are listed under <h3> tags
    for section in sections:
        em_tag = section.find("em")
        if em_tag:
            german_conjunction = em_tag.get_text()
            english_translation = section.get_text().split('–')[-1].strip()
            example_sentences = section.find_next("ul")
            examples = [li.get_text() for li in example_sentences.find_all("li")] if example_sentences else []
            conjunctions.append({
                "German Conjunction": german_conjunction,
                "English Translation": english_translation,
                "Examples": "; ".join(examples)
            })

            print(german_conjunction)
            print(english_translation)
            print(examples)
    return conjunctions

# Extract conjunctions
conjunctions = extract_conjunctions(soup)

# Create a new Excel workbook and select the active worksheet
# workbook = openpyxl.Workbook()
# sheet = workbook.active
# sheet.title = "German Conjunctions"

# # Write the headers
# headers = ["German Conjunction", "English Translation", "Examples"]
# sheet.append(headers)

# # Write the data
# for conjunction in conjunctions:
#     sheet.append([conjunction["German Conjunction"], conjunction["English Translation"], conjunction["Examples"]])

# # Save the workbook
# workbook.save("German_Conjunctions.xlsx")

print("Data has been exported to German_Conjunctions.xlsx")
