import pytest

TEXT_TABLE = [
    ('test_sherlock.txt', 'test_sherlock.txt')
]

CLEAN_TABLE = [
    ('\r\niuguhbugjb.', ' iuguhbugjb.')
]

DIC_TABLE = [
    ('Yo whattup? hi.'. {'Yo'})
]

MAKE_TABLE = [
    (8, {'dragons?, dragons': ['what'], 'dragons?': ['mine.']}, 1)
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
