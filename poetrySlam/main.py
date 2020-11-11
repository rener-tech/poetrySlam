"""
Irene Lunt
CSCI 3725
M6: Poetry Slam
Last Updated: 10 November 2020

This system scrapes an inspiring set of poems from the web and uses them to
create a n-gram. Using this n-gram, the system writes poems, evaluates the poems,
measuring spookiness, and reads aloud the poem deemed the spookiest.
"""
import glob
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import random
import textwrap
import os

site = 'https://www.poetryfoundation.org/collections/142010/halloween-poems'  # site to be scraped for inspiring set


class Poem:
    def __init__(self):
        """ Initializes poem object. """
        self.text = []
        self.title = " "

    def __str__(self):
        """ Returns formatted string representation of poem. """
        print('\n' + self.title)
        poem = repr(self)
        return textwrap.fill(poem, 25)

    def __repr__(self):
        """ Returns unformatted string representation of poem. """
        poem = " ".join(self.text)
        return poem

    def generate_text(self, ngram):
        """ Takes in an n-gram and uses it to generate a poem. """
        poem_text = self.text
        # randomly selects the starting sequence of words from the n-gram
        current_seq = random.choice(list(ngram))
        for word in current_seq:
            poem_text.append(word)
        index = 0
        # constructs poem from n-gram
        for i in range(100):
            if current_seq not in ngram.keys():
                break
            next_word_choices = ngram[current_seq]
            next_word = next_word_choices[random.randrange(len(next_word_choices))]
            poem_text.append(next_word)
            index += 1
            current_seq = tuple(poem_text[index:index+2])
        return poem_text

    def title_poem(self):
        """ Gives the poem a title. """
        title_index = random.randint(0, len(self.text))  # randomly selects index in poem
        # constructs poem using a 3-word sequence starting at the randomly selected index
        for i in range(3):
            self.title += self.text[title_index].upper() + " "
            title_index += 1


def get_and_parse_url(url):
    """ Gets and parses a given URL to be scraped. """
    header = {'User-Agent': 'Chrome'}
    request = Request(url, headers=header)
    page = urlopen(request)
    soup = BeautifulSoup(page, 'html.parser')
    return soup


def find_poems(url):
    """ Finds and writes in the poems from site we are scraping. """
    soup = get_and_parse_url(url)
    poems = soup.find('div', class_='c-tier-content')
    file_num = 1
    # loops through all poem hyperlinks, opens them, and scrapes the poem text from each
    for link in poems.find_all('a'):
        poem_soup = get_and_parse_url(link.get('href'))
        poem = poem_soup.find(class_='c-feature-bd')
        poem_text = poem.get_text(separator='\n', strip=True)
        # save each poem as its own file
        file = open("/Users/irenelunt/PycharmProjects/poetrySlam/poems/poem%d.txt" % file_num, "w+")
        file.write(poem_text)
        file.close()
        file_num += 1


def build_bigram(text):
    """ Takes in some text and constructs a bi-gram. """
    bigram = {}
    words = 2
    # loops through text and creates a key that is a tuple storing a 2-word sequence
    for i in range(len(text) - words):
        sequence = tuple(text[i:i + words])
        if sequence not in bigram.keys():
            bigram[sequence] = []
        # if sequence already in bi-gram, appends the next word to that sequence's list of subsequent words
        bigram[sequence].append(text[i + words])
    return bigram


def get_bigram(folder):
    """ Creates a list of all words in the inspiring set and creates a bi-gram from that list. """
    inspiring_set = build_inspiring_set(folder)
    all_text = []
    for poem in inspiring_set:
        poem_text = get_raw_text(poem)
        for word in poem_text:
            all_text.append(word)
    bigram = build_bigram(all_text)
    return bigram


def get_raw_text(text):
    """ Takes text and makes it more uniform and readable (i.e., raw text). """
    text_list = []
    # strips text, makes it lowercase, and removes special characters
    for i in range(len(text)):
        for word in text[i].split():
            word = re.sub(r'[^A-Za-z.a]', '', word)
            text_list.append(word.lower())
    return text_list


def build_inspiring_set(folder):
    """ Builds inspiring set from given folder. """
    inspiring_set = []
    for filename in glob.glob(folder):
        # reads and stores each poem as a list, then adds list to inspiring set
        open_recipe = open(filename)
        poem = open_recipe.readlines()
        poem_holder = []
        for line in poem:
            poem_holder.append(line)
        inspiring_set.append(poem_holder)
    return inspiring_set


def check_substring(string, substring):
    """ Determines whether or not a substring is present in a given string. """
    if string.find(substring) == -1:
        return False
    else:
        return True


def evaluate_fitness(poem):
    """ Takes a poem and evaluates its fitness. """
    spooky_words = ["goblin", "ghost", "witch", "grave", "dead", "skull", "dark"]  # list of spookiest words
    fitness = 0
    # for each spooky word that appears, fitness increments
    for word in spooky_words:
        if check_substring(poem, word):
            fitness += 1
    return fitness


def choose_poem():
    """ Generates 10 poems and chooses and returns the "spookiest" of them all! """
    bigram = get_bigram("poems/*")  # creates bi-gram using inspiring set of poems
    best_poem = Poem()
    score = -1
    for poem in range(10):
        some_poem = Poem()
        some_poem.generate_text(bigram)
        some_poem.title_poem()
        fitness = evaluate_fitness(repr(some_poem))
        # keeps track of the poem with the highest fitness
        if fitness >= score:
            best_poem = some_poem
            score = fitness
            best_poem.title = some_poem.title
    return best_poem


def main():
    # find_poems(site)
    my_poem = choose_poem()
    print(my_poem)
    os.system('say -v Alex -r 140' + repr(my_poem))


if __name__ == "__main__":
    main()
