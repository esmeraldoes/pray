import xml.etree.ElementTree as ET

def read_bible(version, book, chapter=None, verse=None):
    file_path = f'data/{version}.xml'
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Find the desired book
    book_element = None
    for biblebook in root.findall('BIBLEBOOK'):
        if biblebook.get('bname') == book:
            book_element = biblebook
            break
    if book_element is None:
        print(f"Book '{book}' not found in the Bible.")
        return

    # Retrieve the content based on chapter and verse
    if chapter is not None and verse is not None:
        chapter_element = book_element.find(f"CHAPTER[@cnumber='{chapter}']")
        if chapter_element is None:
            print(f"Chapter {chapter} not found in the book '{book}'.")
            return

        verse_element = chapter_element.find(f"VERS[@vnumber='{verse}']")
        if verse_element is None:
            print(f"Verse {verse} not found in Chapter {chapter} of the book '{book}'.")
            return

        print(f"{book} {chapter}:{verse}")
        print(verse_element.text)
    elif chapter is not None:
        chapter_element = book_element.find(f"CHAPTER[@cnumber='{chapter}']")
        if chapter_element is None:
            print(f"Chapter {chapter} not found in the book '{book}'.")
            return

        print(f"{book} {chapter}")
        for verse_element in chapter_element.findall('VERS'):
            print(f"{verse_element.get('vnumber')}: {verse_element.text}")
    else:
        print(f"{book}")
        for chapter_element in book_element.findall('CHAPTER'):
            chapter_number = chapter_element.get('cnumber')
            print(f"Chapter {chapter_number}")
            for verse_element in chapter_element.findall('VERS'):
                verse_number = verse_element.get('vnumber')
                print(f"{verse_number}: {verse_element.text}")


# Example usage
read_bible('Bible_English_AMP', 'Genesis', '3', '5')

























































# import os
# import xmltodict

# # Define the path to the XML files
# XML_FILES_PATH = os.path.join(os.path.dirname(__file__), 'data')

# # Read the XML file and parse it into a dictionary
# def read_bible(version, book, chapter, verse):
#     # Construct the XML file path based on the version
#     xml_file_path = os.path.join(XML_FILES_PATH, f'{version.lower()}.xml')
#     print(xml_file_path)

#     # Read the XML file
#     with open(xml_file_path, 'r') as file:
#         bible_data = file.read()

#     # Parse the XML into a dictionary
#     bible_dict = xmltodict.parse(bible_data)
#     print(bible_dict)

#     # Retrieve the requested verse
#     try:
#         verse_text = bible_dict['XMLBIBLE']['BIBLEBOOK'][book - 1]['CHAPTER'][chapter - 1]['VERS'][verse - 1]['#text']
#         print(verse_text)
#         return verse_text
#     except (KeyError, IndexError):
#         return None
    
# read_bible('Bible_English_AMP','Genesis','3','5')
