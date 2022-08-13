# This function returns an array of vowels included in the input sentence, in the same order they occur in it.

def pick_out_vowels(sentence):
    vowels = "EeUuIiOoAa"
    result = [each for each in sentence if each in vowels]
    return result
