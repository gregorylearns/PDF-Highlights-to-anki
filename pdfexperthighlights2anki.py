import re
import genanki
import argparse
import datetime
import random
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter



def replace_multiple(text):
    """
    Replace multiple strings in the text using a dictionary of find-and-replace pairs.

    Args:
        text (str): The input text where replacements will be performed.

    Returns:
        str: The text with replacements.
    """
    replace_dict = {
        "\n": "<br>",
        " ●": " <br>●",
        " ▪": " <br>▪",
        " ○": " <br>○"
    }
    
    for find, replace in replace_dict.items():
        text = text.replace(find, replace)
    return text


def extract_html(soup):
	# Extract the text per row class and preserve the tags
	formatted_text = ""

	for row in soup.find_all(class_=['row']):
	    row_text = ""
	    underline_flag = False
	 
	    # Extract and format the text
	    for element in row.find_all(class_=['highlight', 'highlight underline']):
	        text = element.get_text()

	        if 'underline' in element['class']:
	            if underline_flag:
	                row_text += f' {text}'
	            else:
	                row_text += f'${text}'
	            underline_flag = True
	        else:
	            if underline_flag:
	                row_text += f'$ {text}'
	                underline_flag = False
	            else:
	                # pass
	                row_text += f'{text}'
	    
	    if underline_flag: #fixed bug if last word is underlined kay di maapil sa cloze
	        row_text += f'$'
	        underline_flag = False


	        # Print the formatted text
	        # print(formatted_text)

	        
	        # row_text += text
	    
	    row_text = replace_multiple(row_text)
	    print(f"row_text:\n{row_text}")
	    formatted_text += row_text + "\n"
	    # print("formatted")
	    # print(formatted_text)

	# Print the formatted text
	# print(formatted_text)


	clozed_list = [x for x in formatted_text.split("\n") if x != ""]
	return(clozed_list)


def format_text_with_tags(text):
    # Define a regular expression pattern to match words within dollar signs
    pattern = r'\$(.*?)\$'
    
    # Use re.sub to find and replace matches in the text
    formatted_text = re.sub(pattern, r'{{c1::\1}}', text)

    # pattern_2 = r'\}} {{c1::'
    pattern_2 = r'}}\s+{{c1::'
    
    # Use re.sub to replace the pattern with an empty string
    cleaned_text = re.sub(pattern_2, ' ', formatted_text)
    
    return cleaned_text

def catch_for_no_cloze(text):
    #catch notes with no cloze and add something
    if "{{" not in text:
        text = "{{c1:: }}" + text
    return(text)


def generate_anki(final_clozed_list, deck_name):
	# Get the current date in the format "yyyymmdd"
	current_date = datetime.datetime.now().strftime("%Y%m%d")

	# Generate 5 random digits
	random_digits = ''.join(str(random.randint(0, 9)) for _ in range(5))

	# Combine the date and random digits
	result = current_date + random_digits

	deck_id = int(result)

	deck = genanki.Deck(deck_id, deck_name)

	for card in final_clozed_list:
	    note = genanki.Note(model=genanki.CLOZE_MODEL, fields=[card, f"<br>{deck_name}"])
	    deck.add_note(note)

	# Save the deck to an Anki package (*.apkg) file
	genanki.Package(deck).write_to_file(f'anki_converted/{deck_name}.apkg')



def main(file_path, deck_name):


	with open(file_path, encoding="utf-8") as fp:
	    soup = BeautifulSoup(fp.read(),features="lxml")

	clozed_list = extract_html(soup)

	final_clozed_list = [catch_for_no_cloze(format_text_with_tags(card)) for card in clozed_list]

	print(f"\nAdded {len(final_clozed_list)} Cards to {deck_name}!\n")
	for i in final_clozed_list: 
	    print(format_text_with_tags(i))

	generate_anki(final_clozed_list, deck_name)
	print(f"\n.apkg file saved to anki_converted/{deck_name}.apkg")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process file_path and deck_name")
    parser.add_argument("file_path", help="Path to the file")
    parser.add_argument("deck_name", help="Name of the deck")

    args = parser.parse_args()
    main(args.file_path, args.deck_name)