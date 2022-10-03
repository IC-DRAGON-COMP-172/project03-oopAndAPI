import pytest

from poem import Poem


def test_creation():
    test_poem = Poem({"title": "poem1", "author": "author1", "lines": ["line1", "line2"]})
    assert test_poem.title == "poem1"
    assert test_poem.author == "author1"
    assert len(test_poem.lines) == 2
    test_poem = Poem({"title": "poem2", "author": "author1", "lines": ["line1", "line2", "line3"]})
    assert test_poem.title == "poem2"
    assert test_poem.author == "author1"
    assert len(test_poem.lines) == 3
    test_poem = Poem({"title": "poem4", "author": "author3", "lines": []})
    assert test_poem.title == "poem4"
    assert test_poem.author == "author3"
    assert len(test_poem.lines) == 0


def test_num_chars():
    test_poem = Poem({"title": "poem1", "author": "author1", "lines": ["line1", "line2"]})
    assert test_poem.num_chars() == 10
    test_poem = Poem({"title": "poem2", "author": "author1", "lines": ["line 1", "line2", " line3 "]})
    assert test_poem.num_chars() == 18
    test_poem = Poem({"title": "poem4", "author": "author3", "lines": []})
    assert test_poem.num_chars() == 0
