from bs4 import BeautifulSoup
soup = BeautifulSoup("<html> <p> asdasdasd <strong> Hello <a > Hello </html>", "html.parser")
print(soup)
soup.prettify()
print(soup.prettify())
print(soup)

