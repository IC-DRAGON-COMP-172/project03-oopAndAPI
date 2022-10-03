import requests


class Poem:
    def __init__(self, poem_json):
        self.title = poem_json["title"]
        self.author = poem_json["author"]
        self.lines = poem_json["lines"]

    def __str__(self):
        the_string = self.title + " \t by: \t " + self.author + "\n------------\n"
        for line in self.lines:
            the_string += "\n" + line
        return the_string

    def __repr__(self):
        return self.author+": "+self.title

    def num_chars(self):
        total_chars = 0
        for line in self.lines:
            total_chars += len(line)
        return total_chars

    def contains(self, word):
        """:return: True if the poem contains the given word anywhere in the poem or title, False otherwise"""
        pass


def find_longest(poem_list):
    assert len(poem_list) > 0
    longest_poem = poem_list[0]
    for a_poem in poem_list:
        if a_poem.num_chars() > longest_poem.num_chars():
            longest_poem = a_poem
    return longest_poem


def main():
    response = requests.get("https://poetrydb.org/poemcount/3162")
    poems_json = response.json()

    poem_objects = []
    for poem_json in poems_json:
        poem_objects.append(Poem(poem_json))
    print(poem_objects)


if __name__== "__main__":
    main()
