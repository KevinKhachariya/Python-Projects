import os
import re
import string
import random

from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read() # string

        # for songs, we dont want [Chorus], [Verse] .... so we remove them 
        text = re.sub(r'\[(.+)\]', ' ', text)


        text = ' '.join(text.split()) # gets indentation and joins them with a single space
        text = text.lower()
        # This function can be made complex to handle things like punctuation and all that
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()
    return words

def make_graph(words):
    g = Graph()

    previous_word = None

    # for each word, we check if the word is in the graph, If not we add it
    for word in words:
        word_vertex = g.get_vertex(word)
    # when we come across a new word. We want to check the previous word if exists we increment its weight by 1
    #  else we make an edge with weight 1
        if previous_word:
            previous_word.increment_edge(word_vertex)
    
    # now set our word to previous word and then we iterate
        previous_word = word_vertex
    

    g.generate_probability_mappings()

    return g




def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length ):
        composition.append(word.value)
        word = g.get_next_word(word)
    
    return composition


def main(artist):
    # Note: I have not added songs and text you see in this code in this repo.
    # Please get them from Kylie Ying's original repo for this project
    # here -> https://github.com/kying18/graph-composer

    # step 1 get words from input text
    # words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    # for songs lyrics
    words = []
    for song_file in os.listdir(f'songs/{artist}'):
        if song_file == '.DS_Store': # This will throw error as its just a cache file
            continue
        song_words = get_words_from_text(f'songs/{artist}/{song_file}')
        words.extend(song_words)


    # step 2 make graph using the words

    g = make_graph(words)

    # step 3: get next word for x number of words (defined by user)

    # step 4: show the user
    composition = compose(g, words, 100)

    return ' '.join(composition) # returns a string instead of a list


if __name__ == '__main__':
    print(main('green_day'))