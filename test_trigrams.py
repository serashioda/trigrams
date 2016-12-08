import pytest

TEXT_TABLE = [
    ('test_sherlock.txt', """One night--it was on the twentieth of March, 1888--I was
returning from a journey to a patient (for I had now returned to
civil practice), when my way led me through Baker Street. As I
passed the well-remembered door, which must always be associated
in my mind with my wooing, and with the dark incidents of the
Study in Scarlet, I was seized with a keen desire to see Holmes
again, and to know how he was employing his extraordinary powers.
His rooms were brilliantly lit, and, even as I looked up, I saw
his tall, spare figure pass twice in a dark silhouette against
the blind. He was pacing the room swiftly, eagerly, with his head
sunk upon his chest and his hands clasped behind him. To me, who
knew his every mood and habit, his attitude and manner told their
own story. He was at work again. He had risen out of his
drug-created dreams and was hot upon the scent of some new
problem. I rang the bell and was shown up to the chamber which
had formerly been in part my own.
""" )
]

CLEAN_TABLE = [
    ('\r\niuguhbugjb.', ' iuguhbugjb.')
]

DIC_TABLE = [
    ('what up? Double it.', {'what up?': ['Double'], 'up? Double': ['it.']})
]

MAKE_TABLE = [
    (6, {'what up?': ['mario'], 'it? mario': ['it.']}, 6)
]


@pytest.mark.parametrize('path, result', TEXT_TABLE)
def test_import_text(path, result):
    from trigrams import import_text
    assert import_text(path) == result


@pytest.mark.parametrize('full_text, result', CLEAN_TABLE)
def test_read_text(full_text, result):
    from trigrams import read_text
    assert read_text(full_text) == result


@pytest.mark.parametrize('clean_text, result', DIC_TABLE)
def test_create_dic(clean_text, result):
    from trigrams import create_dic
    assert create_dic(clean_text) == result


@pytest.mark.parametrize('num, dic, result', MAKE_TABLE)
def test_create_story(num, dic, result):
    from trigrams import create_story
    assert len(create_story(num, dic)) == result