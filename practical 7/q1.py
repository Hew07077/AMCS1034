def count_words(input_string):
    return len(input_string.split())
    
def count_vowels(input_string):
    return len([character for character in input_string if character.lower() in ["a","e","i","o","u"]])

def count_vowel_aeiou(input_string):
    input_string = input_string.lower()
    vowels = ["a","e","i","o","u"]
    
    a = input_string.count("a")
    e = input_string.count("e")
    i = input_string.count("i")
    o = input_string.count("o")
    u = input_string.count("u")
    frequency = [a,e,i,o,u]
    
    return dict(zip(vowels,frequency))

def calculate_average_word_length(input_string):
    
    total = 0
    for token in input_string.split():
        total += len(token)
    return (total/len(input_string.split()))

def main():
    text = input("Enter a string:").strip()
    
    print("\n No of words: ",count_words(text))
    
    print("Average word length: {:.2f}\n".format(calculate_average_word_length(text)))
    
    for vowel,frequency in count_vowel_aeiou(text).items():
        print("No of {}:{:d}".format(vowel,frequency))
        
main()