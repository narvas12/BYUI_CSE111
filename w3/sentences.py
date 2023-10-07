''' Extra Creativities:
1. Program includes a get_adjective and a  get_adverb function 
2. Test file includes a test_get_adjective or test_get_adverb function 
3. Program builds sentences that include two prepositional phrases 
4. Program includes some other additional functionality like adding more words to give the program more flexible choices so as to make a good sentence but it seems the sentences are not well structured '''


import random

from pip import main


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word



def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman",
                 "apple", "book", "chair", "cloud", "computer",
                 "hat", "horse", "leaf", "lion", "mountain",
                 "pen", "river", "snake", "star", "table",
                 "teacher", "tiger", "train", "tree", "umbrella",
                 "watch", "wave", "window", "zebra", "flower",
                 "house", "kite", "door", "fish", "phone",
                 "puppy", "rose", "school", "shoe", "elephant",
                 "bicycle", "cake", "movie", "pencil", "mountain",
                 "carrot", "guitar", "ocean", "volcano", "moon",
                 "planet", "sun", "ship", "rocket", "robot"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women",
                 "apples", "bicycles", "books", "cakes", "chairs",
                 "clouds", "computers", "doors", "elephants", "fish",
                 "flowers", "hats", "horses", "houses", "kites",
                 "leaves", "lions", "mountains", "movies", "pencils",
                 "phones", "puppies", "rivers", "roses", "schools",
                 "shoes", "snakes", "stars", "tables", "teachers",
                 "tigers", "trains", "trees", "umbrellas", "watches",
                 "waves", "windows", "zebras"]
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == 'past':
        words = ["drank", "ate", "grew", "laughed", "thought",
                  "ran", "slept", "talked", "walked", "wrote", "ate", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote", "jumped", "cried", "swam", "played", "climbed", "danced", "studied"]
    elif tense == 'present':
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
                     "runs", "sleeps", "talks", "walks", "writes", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes", "jumps", "cries", "swims", "plays", "climbs", "dances", "studies"]
        else:
            words = ["laugh", "think", "run", "sleep", "talk", "walk", "write", "jump", "cry", "swim", "play", "climb", "dance", "study"]
    elif tense == 'future':
        words = ["will eat", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write", "will jump", "will cry", "will swim", "will play", "will climb", "will dance", "will study"]



    word = random.choice(words)
    return word


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    return random.choice(prepositions)


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or plural.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase


def get_adjective():
    """Return a randomly chosen adjective.
    This function returns one of these ten adjectives:
        "happy", "sad", "tall", "short", "bright",
        "dark", "noisy", "quiet", "friendly", "shy"

    Return: a randomly chosen adjective.
    """
    adjectives = ["happy", "sad", "tall", "short", "bright",
                  "dark", "noisy", "quiet", "friendly", "shy"]

    word = random.choice(adjectives)
    return word


def get_adverb():
    """Return a randomly chosen adverb.
    This function returns one of these ten adverbs:
        "quickly", "slowly", "loudly", "softly", "carefully",
        "happily", "sadly", "quietly", "rapidly", "gently"

    Return: a randomly chosen adverb.
    """
    adverbs = [
        "quickly", "slowly", "loudly", "softly", "carefully",
        "happily", "sadly", "quietly", "rapidly", "gently"
    ]

    return random.choice(adverbs)

def main():
    num_sentences = 6

    for _ in range(num_sentences):
        quantity = random.choice([1, 2])
        tense = random.choice(["past", "present", "future"])
        determiner = get_determiner(quantity)
        noun = get_noun(quantity)
        verb = get_verb(quantity, tense)
        adjective = get_adjective()
        prepositional_phrase = get_prepositional_phrase(quantity)
        adverb = get_adverb()


        if quantity == 1:
            print(f"{determiner.capitalize()} {adjective} {noun} {verb} {adverb} {prepositional_phrase}.")
        else:
            print(f"{determiner.capitalize()} {adjective} {noun} {verb} {adverb} {prepositional_phrase}.")

if __name__ == "__main__":
    main()

