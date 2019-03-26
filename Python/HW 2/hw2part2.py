"""

Author: ALSENY SYLLA

This program deciphers a ciphered centence, and counts how many words in the deciphered sentence start with s, a, and c.

"""
def decipher(sentence):
    sentence = raw_input("Please enter a sentence ==> ")
    print sentence
    sentence = sentence.replace('rxr', ' a')
    sentence = sentence.replace('twt', 'o')
    sentence = sentence.replace('yyy', 'u')
    sentence = sentence.replace('xx', 'th')
    sentence = sentence.replace('he', 'an')
    sentence = sentence.replace('az az', 'e')
    sentence = sentence.replace('bb', 'he')
    return sentence
    
def letter(count_sentence, x):
    count_sentence = ' ' + count_sentence 
    x = ' ' + x
    count_sentence_1 = count_sentence.replace(x, ' ')
    count = len(count_sentence) - len(count_sentence_1)
    return count

sentence = decipher('')
print "Deciphered as ==> " + sentence

print "Number of words that start with s: " + str(letter(sentence, 's'))
print "Number of words that start with a: " + str(letter(sentence, 'a'))
print "Number of words that start with c: " + str(letter(sentence, 'c'))