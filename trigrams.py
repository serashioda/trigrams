import io
import sys
import random


def text_import(path):
    """Return imported text from desired path."""
    original = io.open(path)
    full_text = original.read()
    original.close()
    return full_text


def text_clean(full_text):
    """Return text without DOS characters."""
    clean = full_text.replace('\r\n', ' ').replace('  ', ' ')
    return clean


def create_dic(clean_text):
    """Return a dictionary of key value pairs."""
    lst = clean_text.split(' ')
    dic = {}
    for words in range(0, len(lst) - 2):
        couple = "{0} {1}".format(lst[words], lst[words + 1])
        value = lst[words + 2]
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


def main(num, path):
    """Print story of desired word length."""
    a = text_import(path)
    b = text_clean(a)
    c = create_dic(b)
    d = create_story(num, c)
    x = " "
    e = x.join(d)
    return e

if __name__ == '__main__':
    path = sys.argv[1]
    num = int(sys.argv[2])
    output = main(num, path)
    outfile = io.open('dummy_text.txt' 'w')
    outfile.write(output)
    outfile.close()