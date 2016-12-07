import sys
import io
import random

def create_dic(clean_text):
	"""Return {} with key value pairs"""
	first = clean_text.split(' ')
	dic = {}
	for words in range(0, len(first) - 2):
    	couple = "{0} {1}".format(first[words], first[words + 1])
        value = first[words + 2]
        dic.setdefault(couple, []).append(value)
    return dic

def import_text(path):
    """Return imported path text."""
    original = io.open(path)
    text = original.read()
    original.close()
    return text

def read_text():
	read = text.replace('\r\n', ' ').replace('  ', ' ')
    return read

def create_story():

def main(num, path):
    """Print story using functions to create a dictionary and import text from the path."""
    a = import_text(path)
    b = read_text(a)
    c = create_dic(b)
    d = create_story(num, c)
    x = " "
    e = x.join(d)
    return e

if __name__ == "__main__":
	user_input = sys.argv[1]