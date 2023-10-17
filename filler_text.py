import random
import string 

list_of_syllables = ['ing', 'er', 'a', 'ly', 'ed', 'i', 'es', 're', 'tion', 'in', 'e', 'con', 'y', 'ter', 'ex', 'al', 'de', 'com', 'o', 'di', 'en', 'an', 'ty', 'ry', 'u', 'ti', 'ri', 'be', 'per', 'to', 'pro', 'ac', 'ad', 'ar', 'ers', 'ment', 'or', 'tions', 'ble', 
'der', 'ma', 'na', 'si', 'un', 'at', 'dis', 'ca', 'cal', 'man', 'ap', 'po', 'sion', 'vi', 'el', 'est', 'la', 'lar', 'pa', 'ture', 'for', 'is', 'mer', 'pe', 'ra', 'so', 'ta', 'as', 'col', 'fi', 'ful', 'ger', 'low', 'ni', 'par', 'son', 'tle', 'day', 'ny', 'pen', 'pre', 'tive', 'car', 'ci', 'mo', 'on', 'ous', 'pi', 'se', 'ten', 'tor', 'ver', 'ber', 'can', 'dy', 'et', 'it', 'mu', 'no', 'ple', 'cu', 'fac', 'fer', 'gen', 'ic', 'land', 'light', 'ob', 'of', 'pos', 'tain', 'den', 'ings', 'mag', 'ments', 'set', 'some', 'sub', 'sur', 'ters', 'tu', 'af', 'au', 'cy', 'fa', 'im', 'li', 'lo', 'men', 'min', 'mon', 'op', 'out', 'rec', 'ro', 'sen', 'side', 'tal', 'tic', 'ties', 'ward', 'age', 'ba', 'but', 'cit', 'cle', 'co', 'cov', 'da', 'dif', 'ence', 'ern', 'eve', 'hap', 'ies', 'ket', 'lec', 'main', 'mar', 'mis', 'my', 'nal', 'ness', 'ning', "n't", 'nu', 'oc', 'pres', 'sup', 'te', 'ted', 'tem', 'tin', 'tri', 'tro', 'up', 'va', 'ven', 'vis', 'am', 'bor', 'by', 'cat', 'cent', 'ev', 'gan', 'gle', 'head', 'high', 'il', 'lu', 'me', 'nore', 'part', 'por', 'read', 'rep', 'su', 'tend', 'ther', 'ton', 'try', 'um', 'uer', 'way', 'ate', 'bet', 'bles', 'bod', 'cap', 'cial', 'cir', 'cor', 'coun', 'cus', 'dan', 'dle', 'ef', 'end', 'ent', 'ered', 'fin', 'form', 'go', 'har', 'ish', 'lands', 'let', 'long', 'mat', 'meas', 'mem', 'mul', 'ner', 'play', 'ples', 'ply', 'port', 'press', 'sat', 'sec', 'ser', 'south', 'sun', 'the', 'ting', 'tra', 'tures', 'val', 'var', 'vid', 'wil', 'win', 'won', 'work', 'act', 'ag', 'air', 'als', 'bat', 'bi', 'cate', 'cen', 'char', 'come', 'cul', 'ders', 'east', 'fect', 'fish', 'fix', 'gi', 'grand', 'great', 'heav', 'ho', 'hunt', 'ion', 'its', 'jo', 'lat', 'lead', 'lect', 'lent', 'less', 'lin', 'mal', 'mi', 'mil', 'moth', 'near', 'nel', 'net', 'new', 'one', 'point', 'prac', 'ral', 'rect', 'ried', 'round', 'row', 'sa', 'sand', 'self', 'sent', 'ship', 'sim', 'sions', 'sis', 'sons', 'stand', 'sug', 'tel', 'tom', 'tors', 'tract', 'tray', 'us', 'vel', 'west', 'where', 'writ']

all_letters = set(string.ascii_letters)
vowels = set("aeiouAEIOUyY")
vowels_no_Y = set("aeiouAEIOU")
consonants = all_letters - vowels


#define sets for controlling punctuation and spaces.
all_punctuation_characters = set("!()[]{}?.,'\";: ")
space_removal_punctuation = set("!?.,'\;: ")
space_character_pairs = {}

for punc in space_removal_punctuation:
    space_string = ' ' + str(punc)
    space_character_pairs[space_string] = str(punc)

space_punctuation_set = set(space_character_pairs.keys())


#some statistical info to help with generation
characters_per_word = 5.55
words_per_sentence = 16
sentences_per_paragraph = 6

characters_per_sentence = words_per_sentence * characters_per_word
characters_per_paragraph = characters_per_sentence * sentences_per_paragraph

#number of chars in shortest and longest strings inside list of syllables
min_syllable_length = 1
max_syllable_length = len(max(list_of_syllables, key=len))
max_word_length = max_syllable_length * 7









#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def has_vowel(input_string, include_Y=True):
    '''Returns true if the given string contains a vowel.
    '''
    global vowels, vowels_no_Y
    my_vowels = vowels
    if not include_Y:
        my_vowels = vowels_no_Y

    for vowel in my_vowels:
        if vowel in input_string:
            return True
    return False

def remove_extra_spaces(input_string):
    '''Utility function that removes extra spaces, and weird punctuation from generated strings. 
    May have some utility outside of this script, but it was only designed for this script.'''
    global space_punctuation_set, space_character_pairs, space_removal_punctuation
    output_string = input_string

    if output_string[0] == ' ':
        output_string = output_string[1:]
    
    while output_string[0] in space_removal_punctuation:
        output_string = output_string[1:]

    for space_punctuation in space_punctuation_set:
        if space_punctuation in output_string:
            output_string = output_string.replace(space_punctuation, space_character_pairs[space_punctuation])

    return output_string

def remove_one_word(input_string):
    '''Utility function to randomly remove a single word from a string (favoring words near the middle of the string).'''
    boundary_characters = set({' ', '.', ',', '!', '?','\\'})

    random_index = int(random.gauss(len(input_string) / 2, len(input_string) / 4))
    random_index = max(min(len(input_string) - 1, random_index), 0)
    
    while input_string[random_index] in boundary_characters:
        random_index = random.randint(0,len(input_string))

    output_string = ""
    
    #search for start and end of word
    word_start_index = random_index
    at_start_edge = False
    word_end_index = random_index
    at_end_edge = False

    while not at_start_edge:
        if input_string[word_start_index - 1] in boundary_characters or word_start_index == 0:
            at_start_edge = True
        else:
            word_start_index -= 1

    while not at_end_edge:
        if word_end_index == len(input_string) - 1:
            at_end_edge = True
        elif input_string[word_end_index + 1] in boundary_characters:
            at_end_edge = True
        else:
            word_end_index += 1

    output_string = input_string[:word_start_index] + input_string[word_end_index + 1:]
    output_string = remove_extra_spaces(output_string)
    return(output_string)

def remove_random_characters(input_string, chars_to_remove, max_tries_for_good_matching=20):
    '''Utility function for cutting down a strings length by randomly removing letters in the middle of words.'''
    global all_letters, vowels
    #boundary_characters = set({' ', '.', ',', '!', '?','\\','"'})
    #banned_characters = set({'"'})
    output_string = input_string
    

    
    for n in range(0,chars_to_remove):
        valid_character = False
        random_index = 0
        num_tries = 0
        while not valid_character:
            #choose a new character
            random_index = int(random.gauss(len(output_string) / 2, len(output_string) / 4))
            random_index = max(min(len(output_string) - 2, random_index), 0)
            #is this a valid character?
            not_boundary = (output_string[random_index] in all_letters)
            not_end_of_word = (output_string[random_index + 1] in all_letters)
            not_start_of_word = (output_string[random_index - 1] in all_letters)
            not_upper = not output_string[random_index].isupper()
            not_import_vowel = not (  output_string[random_index] in vowels and ( output_string[random_index + 1] not in vowels and output_string[random_index - 1] not in vowels )  )
            if (not_boundary and not_end_of_word and not_start_of_word and not_upper and not_import_vowel) or (num_tries >= max_tries_for_good_matching):
                valid_character = True
                #print('Delete characters took', num_tries, 'tries to find a match')
                num_tries = 0
            else:
                num_tries += 1
                #so that we dont get stuck in an infinite loop
        
        output_string = output_string[:random_index] + output_string[random_index + 1:]
    
            

    #output_string = remove_extra_spaces(output_string)
    return(output_string)
    
    
def add_random_characters(input_string, chars_to_add, max_tries_for_good_matching=20):
    '''Utility function for sneaking extra characters into a string.'''
    global vowels, consonants, all_letters
    #boundary_characters = set({' ', '.', ',', '!', '?','\\','"'})
    output_string = input_string
    
    for n in range(0,chars_to_add):
        valid_character = False
        random_index = 0
        num_tries = 0
        while not valid_character:
            #choose a new character
            random_index = int(random.gauss(len(output_string) / 2, len(output_string) / 6))
            random_index = max(min(len(output_string) - 2, random_index), 0)
            #is this a valid character?
            not_end_of_word = (output_string[random_index] in all_letters)
            not_start_of_word = (output_string[random_index - 1] in all_letters)
            not_upper = not output_string[random_index - 1].isupper()
            not_start_or_end_string = (2) < random_index < (len(output_string) - 2)
            if (not_end_of_word and not_start_of_word and not_upper and not_start_or_end_string) or (num_tries >= max_tries_for_good_matching):
                valid_character = True
            else:
                num_tries += 1
                #so that we dont get stuck in an infinite loop

        # choose a random character to add. We are going to choose a vowel or consonant based on surrounding characters
        next_is_vowel = False
        prev_is_vowel = False
        if output_string[random_index] in vowels:
            next_is_vowel = True
        if output_string[random_index - 1] in vowels:
            prev_is_vowel = True

        gen_vowel = False
        if next_is_vowel and prev_is_vowel:
            gen_vowel = False
        elif not next_is_vowel or prev_is_vowel:
            gen_vowel = True
        else:
            gen_vowel = random.choice([True, False])

        our_letter = ''
        if gen_vowel:
            our_letter = str(random.choice(list(vowels)))
        else:
            our_letter = str(random.choice(list(consonants)))
        

        output_string = output_string[:random_index] + our_letter.lower() + output_string[random_index:]
    
            

    #output_string = remove_extra_spaces(output_string)
    return(output_string)







#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def gen_word(min_syllables = 1, max_syllables = 7, avg_syllables = 2, sigma = 1, generate_caps = True, avoid_early_apostrophe = True):
    '''Generates a single random word using a pool of english syllables and a little additional logic.
    '''
    global list_of_syllables
    syllable_count = random.gauss(avg_syllables,sigma)
    syllable_count = int(round(syllable_count))
    syllable_count = max( min(syllable_count, max_syllables), min_syllables)

    word_result = ''

    for i in range(0,syllable_count):
        one_syllable = random.choice(list_of_syllables)
        if i == 0 and avoid_early_apostrophe:
            while "'" in one_syllable:
                #print("removing spostrophe")
                one_syllable = random.choice(list_of_syllables)
        word_result = word_result + one_syllable
    
    while not has_vowel(word_result):
        word_result += random.choice(list_of_syllables)

    chance = random.random()
    if chance > 0.998 and generate_caps:
        word_result = word_result.upper()
    elif chance > 0.98:
        word_result = word_result[0].upper() + word_result[1:]
    
    if len(word_result) == 1 and chance > 0.1:
        word_result = word_result.upper()

    

    return word_result

def gen_sentence(min_words = 1, max_words = 32, avg_words = 16, sigma = 6, use_punctuation = True):
    '''Generate a gibberish sentence'''
    global list_of_syllables
    word_count = random.gauss(avg_words,sigma)
    word_count = int(round(word_count))
    word_count = max( min(word_count, max_words), min_words)

    sentence_result = ''

    for i in range(0,word_count):
        sentence_result = sentence_result + gen_word()
        if i != word_count - 1:
            chance = random.random()
            if chance > 0.92:
                sentence_result += ', '
            elif chance >= 0.99:
                sentence_result += '; '
            else:
                sentence_result += ' '

    sentence_result = sentence_result.capitalize()

    chance = random.random()
    if chance > 0.96 and use_punctuation:
        sentence_result += '!'
    elif chance > 0.92 and use_punctuation:
        sentence_result += '?'
    else:
        sentence_result += '.'

    return sentence_result







#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def generate(number_of_characters, line_breaks = True, punctuation = True, special_punctuation = None, numbers = True, line_break_cost = 2, avg_sentences_in_paragraph = 6, sentence_sigma = 8):
    '''Generate a string which is a specific number of characters long.'''
    global characters_per_sentence, characters_per_paragraph, list_of_syllables, colors, color_index, all_letters
    if special_punctuation == None:
        special_punctuation = punctuation

    #we almost always overshoot, so we will aim for something a little smaller than the target number, to start.
    minimal_predicted_chars = max(number_of_characters * 0.8, number_of_characters - 400)

    predicted_chars = 0
    #len is the target number of paragraphs, value is how many sentances to expect per paragraph
    target_paragraphs_sentences = []
    #figure out how many sentences we need
    while predicted_chars < minimal_predicted_chars:

        num_sentences_in_paragraph = random.gauss(avg_sentences_in_paragraph,sentence_sigma)
        num_sentences_in_paragraph = int(round(num_sentences_in_paragraph))
        num_sentences_in_paragraph = max( min(num_sentences_in_paragraph, 24), 1)

        target_paragraphs_sentences.append(num_sentences_in_paragraph)

        if line_breaks:
            predicted_chars = sum(target_paragraphs_sentences) * characters_per_sentence + ((len(target_paragraphs_sentences) - 1) * line_break_cost)
        else:
            predicted_chars = sum(target_paragraphs_sentences) * characters_per_sentence

    #decimal representing the difference between current predicted chars and real target chars
    factor_predicted_target = number_of_characters / predicted_chars
    #how many characters do we actually need per sentance to make our generated text length equal the requested number of characters.
    target_characters_per_sentence = factor_predicted_target * characters_per_sentence


    # calculate the number of characters needed to reach in each sentence.
    # with 's[]' representing sentences, and 'p[]' representing paragraphs, this will be nested like:
    # [ p[ s[n_chars], s[n_chars] ], p[ s[n_chars], s[n_chars] ]
    target_chars_in_sentences_in_paragraphs = []

    for num_sentences_this_paragraph in target_paragraphs_sentences:
        this_paragraph_sentence_chars = []
        for i in range(0,num_sentences_this_paragraph):
            num_characters_this_sentence = random.gauss(target_characters_per_sentence, target_characters_per_sentence * .25)
            num_characters_this_sentence = min( max(num_characters_this_sentence,5), target_characters_per_sentence * 2)

            this_paragraph_sentence_chars.append(num_characters_this_sentence)
        target_chars_in_sentences_in_paragraphs.append(this_paragraph_sentence_chars)

    resulting_text = ''

    for each_paragraph in target_chars_in_sentences_in_paragraphs:

        paragraph_text = ''

        for each_sentence_num_characters in each_paragraph:

            sentence_text = ''

            while len(sentence_text) < round(each_sentence_num_characters):

                chance = random.random()
                if punctuation:
                    if chance > 0.999 and numbers:
                        sentence_text += str(random.randint(-100,1000)) + ' '
                    elif chance > 0.99:
                        sentence_text += gen_word() + '; '
                    elif chance > 0.95:
                        sentence_text += gen_word() + ', '
                    else: 
                        sentence_text += gen_word() + ' '
                else:
                    sentence_text += gen_word() + ' '

            
            while sentence_text[-1] in all_punctuation_characters:
                sentence_text = sentence_text[0:len(sentence_text) - 1]


            if special_punctuation:
                chance = random.random()
                if chance > 0.99:
                    sentence_text = '(' + sentence_text + ')'
                elif chance > 0.94:
                    sentence_text = '"' + sentence_text + '."'

            if special_punctuation:
                chance = random.random()
                if chance > 0.99 and sentence_text[-1] in all_letters:
                    sentence_text += ': \n'
                elif chance > 0.95 and sentence_text[-1] in all_letters:
                    sentence_text += '! '
                elif chance > 0.9:
                    sentence_text += '? '
                elif sentence_text[-1] in all_letters:
                    sentence_text += '. '
                else: 
                    sentence_text += ' '
            else:
                if punctuation:
                    sentence_text += '. '
                else:
                    sentence_text += ' '

            sentence_text = sentence_text[0].upper() + sentence_text[1:]
                

            paragraph_text += sentence_text
        
        if line_breaks:
            chance = random.random()
            if chance > 0.9:
                resulting_text += paragraph_text + '\n\n\n'
            elif chance > 0.5:
                resulting_text += paragraph_text + '\n\n'
            else:
                resulting_text += paragraph_text + '\n'
        else:
            resulting_text += paragraph_text + ' '

    #remove words until we are close to the right size
    remove_words_length = number_of_characters + max_word_length
    while(len(resulting_text) > remove_words_length):
        resulting_text = remove_one_word(resulting_text)
    #now, trim down further by removing individual characters
    if len(resulting_text) > number_of_characters:
        chars_to_remove = len(resulting_text) - number_of_characters
        resulting_text = remove_random_characters(resulting_text, chars_to_remove)

    #okay, sometimes we have fewer characters than we need, and we have to fix that too.
    if len(resulting_text) < number_of_characters:
        chars_to_add = number_of_characters - len(resulting_text)
        resulting_text = add_random_characters(resulting_text, chars_to_add)

    return resulting_text

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~









if __name__ == '__main__':
    from termcolor import colored, cprint

    cprint("~"*100, "white")
    cprint("~"*100, "grey")
    print()

    print()
    cprint('One word:', 'grey')
    print()
    cprint(gen_word().capitalize(),'cyan')
    print()

    print()
    cprint('One sentence:', 'grey')
    print()
    cprint(gen_sentence(), 'green')
    print()

    print()
    cprint('1000 characters:', 'grey')
    print()
    cprint(generate(1000), 'yellow')
    print()


    print()
    cprint("~"*100, "grey")
    cprint("~"*100, "white")
