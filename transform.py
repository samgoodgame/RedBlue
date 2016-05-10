import os
import bs4
import codecs

CORPUS_ROOT = "/Users/Goodgame/desktop/RedBlue/input_13apr/"
TARGET_ROOT = "/Users/Goodgame/desktop/RedBlue/output_13apr/"

def transform_corpus(source=CORPUS_ROOT, target=TARGET_ROOT):
    """
    Lists a directory for files, transforms them to extract the text,
    then writes each text document to its own file in the target.
    """
    for name in os.listdir(CORPUS_ROOT):
        # Figure out the input document and output name
        src = os.path.join(CORPUS_ROOT, name)
        dst = os.path.join(TARGET_ROOT, name + ".txt")

        # Transform this document
        transform_document(src, dst)

def transform_document(source, target):
    """
    Extracts all the paragraphs from an HTML source document and
    writes it to the target file for further processing.
    """
    # Open and read the source, parsing HTML
    with codecs.open(source, 'r', 'utf-8') as doc:
        soup = bs4.BeautifulSoup(doc.read(), "html.parser")

        # Open and read the target
        with codecs.open(target, 'w', 'utf-8') as txt:

            # Loop through all p tags and write to the txt file.
            for tag in soup.find_all('p'):
                txt.write(tag.text + u'\n\n')

transform_corpus()