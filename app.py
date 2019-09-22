import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.stackoverflow.com/questions")
soup = BeautifulSoup(response.text,"html.parser")

questions = soup.select(".question-summary")
for question in questions:
    print(question.select_one(".question-hyperlink").getText())