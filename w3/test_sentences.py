''' Extra Creativities:
1. Program includes a get_adjective and a  get_adverb function 
2. Test file includes a test_get_adjective or test_get_adverb function 
3. Program builds sentences that include two prepositional phrases 
4. Program includes some other additional functionality like adding more words to give the program more flexible choices so as to make a good sentence but it seems the sentences are not well structured '''



from sentences import get_determiner, get_noun, get_verb, get_adjective,  get_preposition, get_prepositional_phrase, get_adverb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]
    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)
        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)
        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners



def test_get_noun():
    # Define lists of single and plural nouns for testing
    single_nouns = ["bird", "boy", "car", "cat", "child",
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
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women",
                 "apples", "bicycles", "books", "cakes", "chairs",
                 "clouds", "computers", "doors", "elephants", "fish",
                 "flowers", "hats", "horses", "houses", "kites",
                 "leaves", "lions", "mountains", "movies", "pencils",
                 "phones", "puppies", "rivers", "roses", "schools",
                 "shoes", "snakes", "stars", "tables", "teachers",
                 "tigers", "trains", "trees", "umbrellas", "watches",
                 "waves", "windows", "zebras"]

    # Test single nouns
    for _ in range(len(single_nouns)):
        word = get_noun(1)
        assert word in single_nouns

    # Test plural nouns
    for _ in range(len(plural_nouns)):
        word = get_noun(2)
        assert word in plural_nouns



def test_get_verb():
    # Define lists of verbs for different tenses
    past_verbs = [
                  "drank", "ate", "grew", "laughed", "thought",
                  "ran", "slept", "talked", "walked", "wrote", "ate", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote", "jumped", "cried", "swam", "played", "climbed", "danced", "studied"
                  ]
    
    present_verbs = [
                     "drinks", "eats", "grows", "laughs", "thinks",
                     "runs", "sleeps", "talks", "walks", "writes", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes", "jumps", "cries", "swims", "plays", "climbs", "dances", "studies"
                     ]
    
    present_verbs_plural = [
                         "drink", "eat", "grow", "laugh", "think",
                         "run", "sleep", "talk", "walk", "write", "laugh", "think", "run", "sleep", "talk", "walk", "write", "jump", "cry", "swim", "play", "climb", "dance", "study"
                         ]
    
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                    "will think", "will run", "will sleep", "will talk",
                    "will walk", "will write", "will jump", "will cry", "will swim", "will play", "will climb", "will dance", "will study"]

    # Test past tense verbs
    for _ in range(len(past_verbs)):
        word = get_verb(1, "past")
        assert word in past_verbs
    
    for _ in range(len(past_verbs)):
        word = get_verb(2, "past")
        assert word in past_verbs

    # Test present tense verbs for singular and plural
    for _ in range(len(present_verbs)):
        word = get_verb(1, "present")
        assert word in present_verbs

    for _ in range(len(present_verbs_plural)):
        word = get_verb(2, "present")
        assert word in present_verbs_plural

    # Test future tense verbs
    for _ in range(len(future_verbs)):
        word = get_verb(1, "future")
        assert word in future_verbs

        # Test future tense verbs
    for _ in range(len(future_verbs)):
        word = get_verb(2, "future")
        assert word in future_verbs



def test_get_adjective():
    # Define lists of single and plural nouns for testing
    adjectives = ["happy", "sad", "tall", "short", "bright",
                  "dark", "noisy", "quiet", "friendly", "shy"]
    
    # Test single nouns
    for _ in range(len(adjectives)):
        word = get_adjective()
        assert word in adjectives


def test_get_preposition():
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]

    for _ in range(10):
        preposition = get_preposition()
        assert preposition in prepositions


def test_get_prepositional_phrase():
    for _ in range(10):
        quantity = 1  # Test with singular determiner and noun
        prepositional_phrase = get_prepositional_phrase(quantity)
        assert isinstance(prepositional_phrase, str)
        assert len(prepositional_phrase.split()) == 3

        quantity = 2  # Test with plural determiner and noun
        prepositional_phrase = get_prepositional_phrase(quantity)
        assert isinstance(prepositional_phrase, str)
        assert len(prepositional_phrase.split()) == 3



def test_get_adverb():
    # Define lists of single and plural nouns for testing
    adverbs = [
        "quickly", "slowly", "loudly", "softly", "carefully",
        "happily", "sadly", "quietly", "rapidly", "gently"
        ]
    
    # Test single nouns
    for _ in range(len(adverbs)):
        word = get_adverb()
        assert word in adverbs

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])