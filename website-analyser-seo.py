#Offensive Programming - week 5 - SEO Analyser 
import requests
from bs4 import BeautifulSoup
import re
import csv

def count_words(text):
    return len(re.findall(r'\w+', text))

def count_words_in_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    text = soup.get_text()
    
    return len(re.findall(r'\w+', text))

def count_words_in_elements(soup, elements):
    word_count = 0
    for element in soup.find_all(elements):
        words = re.findall(r'\w+', element.text)
        word_count += len(words)
    return word_count

def count_words_in_class_elements(soup, class_name):
    word_count = 0
    for element in soup.find_all(class_=class_name):
        words = re.findall(r'\w+', element.text)
        word_count += len(words)
    return word_count

def count_words_in_attributes(soup, attribute_name, attribute_value=None):
    word_count = 0
    if attribute_value:
        elements = soup.find_all(attrs={attribute_name: attribute_value})
    else:
        elements = soup.find_all(attrs={attribute_name: True})
    for element in elements:
        word_count += count_words(element.get(attribute_name, ''))
    return word_count

def write_visible_words_to_csv(visible_words):
    with open('visible.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Word'])
        csv_writer.writerows(visible_words)

def display_visible_words(soup):
    visible_words = []
    for element in soup.find_all(['div', 'span', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title', 'meta', 'link']):
        words = re.findall(r'\w+', element.text)
        visible_words.extend(words)
    return visible_words

print("\n\033[92m\033[1mSEO -- WORD & TEXT ANALYSER \033[1m\033[91m❤️\033[0m\033[1m\033[92m DutchJinn.com\033[0m\033[0m\n")
url = input("\n\033[95m\033[1mEnter the URL of the webpage: \033[0m")

response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

visible_words_count = count_words_in_html(html_content)
div_words_count = count_words_in_elements(soup, "div")
span_words_count = count_words_in_elements(soup, "span")
paragraph_words = count_words_in_elements(soup, "p")
headings_words = count_words_in_elements(soup, ["h1", "h2", "h3", "h4", "h5", "h6"])
class_words_count = count_words_in_class_elements(soup, "your-class-name")  

script_words_count = count_words_in_elements(soup, "script")
style_words_count = count_words_in_elements(soup, "style")
alt_text_words_count = count_words_in_attributes(soup, "alt")
redirect_to_words_count = count_words_in_attributes(soup, "redirectTo")
hidden_input_words_count = count_words_in_attributes(soup, "input", "hidden")
redirect_words_count = count_words_in_attributes(soup, "redirect")
div_words = count_words_in_elements(soup, "div")
span_words = count_words_in_elements(soup, "span")
hidden_elements_words_count = count_words_in_attributes(soup, "style", "display: none")
hidden_elements_words_count += count_words_in_attributes(soup, "style", "visibility: hidden")
meta_words_count = count_words_in_elements(soup, "meta")
attribute_words_count = count_words_in_attributes(soup, attribute_name="content")
javascript_generated_words_count = count_words_in_elements(soup, "script")
head_words_count = count_words_in_elements(soup, ["title", "meta", "link"])

non_visible_words_count = (script_words_count + style_words_count +
                           alt_text_words_count + redirect_to_words_count +
                           hidden_input_words_count + redirect_words_count +
                           meta_words_count + attribute_words_count + javascript_generated_words_count)

total_word_count = visible_words_count + non_visible_words_count

visible_words = display_visible_words(soup)

non_visible_words = []

for element in soup.find_all(["script", "style"]):
    words = re.findall(r'\w+', element.text)
    non_visible_words.extend(words)

def write_words_to_txt(file_name, words):
    with open(file_name, 'w') as txtfile:
        txtfile.write('\n'.join(words))
print(f"\nVisible Words in Divs: {div_words_count}")
print(f"Visible Words in Head: {head_words_count}")
print(f"Visible Words in Spans: {span_words_count}")

print(f"Hidden Elements Words: {hidden_elements_words_count}")
print(f"Java & Script Words: {script_words_count}")
print(f"Style Words: {style_words_count}")
print(f"Alt Text Words: {alt_text_words_count}")
print(f"RedirectTo Words: {redirect_to_words_count}")
print(f"Hidden Input Words: {hidden_input_words_count}")
print(f"Redirect Words: {redirect_words_count}\n")
print(f"Meta Words: {meta_words_count}")
print(f"Attribute Words: {attribute_words_count}\n")
print(f"hidden Elements Words: {hidden_elements_words_count}\n")
print(f"Visible Words in Paragraphs: {paragraph_words}")
print(f"Visible Words in Headings: {headings_words}\n")
print(f"Non-Visible Words: {non_visible_words_count}\n")
print(f"\033[1mVisible Words\033[0m: {visible_words_count}\n")
print(f"Total Word Count: {total_word_count}\n")
print("")
write_words_to_txt('visible-words.txt', visible_words)
write_words_to_txt('non-visible-words.txt', non_visible_words)
print("All visible words have been written to visible-words.txt")
print("All non-visible words have been written to non-visible-words.txt\n")

def write_visible_text_to_txt(file_name, visible_text):
    with open(file_name, 'w') as txtfile:
        txtfile.write(visible_text)

response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

visible_text = soup.get_text()

write_visible_text_to_txt('visible_text.txt', visible_text)
print("All visible text has been written to visible_text.txt\n")

print("\n\033[95m\033[1mCopyright 2024 DutchJinn.com\033[0m\033[0m\n")



