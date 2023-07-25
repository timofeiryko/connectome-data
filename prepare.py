from bs4 import BeautifulSoup

def html_to_plain_text(html):
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # Get the plain text without any HTML tags
    plain_text = soup.get_text(separator=' ')
    
    # Remove extra whitespace and newlines
    plain_text = ' '.join(plain_text.split())

    return plain_text