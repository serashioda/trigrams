import sys
import io
import random
import re


def import_text(path):
    """Return imported path text."""
    original = io.open(path)
    text = original.read()
    original.close()
    return text

def read_text(text):
    text = text.replace('\r\n', ' ').replace('  ', ' ')
    text = text.replace('\n', ' ').replace(' ', ' ')
    return text


def create_dic(text):
    """Return {} with key value pairs"""
    first = text.split(' ')
    dic = {}
    for words in range(0, len(first) - 2):
        couple = "{0} {1}".format(first[words], first[words + 1])
        value = first[words + 2]
        dic.setdefault(couple, []).append(value)
    return dic

def create_story(num, dic):
    """Return a story by passing in a number and a dictionary."""
    key_list = list(dic.keys())
    first_words = key_list[random.randint(0, len(key_list) - 1)]
    story = first_words.split(" ")
    while len(story) < num:
        new_key = "{0} {1}".format(story[-2], story[-1])
        if new_key in dic:
            temp_val = random.choice(dic[new_key])
            story.append(temp_val)
        else:
            temp_val = key_list[random.randint(0, len(key_list) - 1)]
            temp_val = temp_val.split(" ")
            story = story + temp_val
    story = story[0:num]
    return story

def main(path, num=20):
    """Print story using functions to create a dictionary and import text from the path."""
    a = import_text(path)
    b = read_text(a)
    c = create_dic(b)
    d = create_story(num, c)
    e = " ".join(d)
    # return e
    print (e)

if __name__ == "__main__":
    path = sys.argv[1]
    num = int(sys.argv[2])
    main(path, num)