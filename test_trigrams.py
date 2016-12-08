import pytest

TEXT_TABLE = [
    ('dummy_text.txt', 'help this is hard.')
]

CLEAN_TABLE = [
    ('\r\niuguhbugjb.', ' test test.')
]

DIC_TABLE = [
    ('this is', {'test?': ['lol'], 'test': ['it.']})
]

MAKE_TABLE = [
    (8, {'dragons?': ['what'], 'dragons?': ['mine.']}, 1)
]


@pytest.mark.parametrize('path, result', TEXT_TABLE)
def test_text_import(path, result):
    from trigrams import text_import
    assert text_import(path) == result


@pytest.mark.parametrize('full_text, result', CLEAN_TABLE)
def test_text_clean(full_text, result):
    from trigrams import text_clean
    assert text_clean(full_text) == result


@pytest.mark.parametrize('clean_text, result', DIC_TABLE)
def test_create_dic(clean_text, result):
    from trigrams import create_dic
    assert create_dic(clean_text) == result


@pytest.mark.parametrize('num, dic, result', MAKE_TABLE)
def test_create_story(num, dic, result):
    from trigrams import create_story
    assert len(create_story(num, dic)) == result