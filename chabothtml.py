from bs4 import BeautifulSoup

with open('ejemplo.html', 'r') as file:
    html = file.read()
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()
response = str(chatbot.get_response(text))
print(response)
