str=input('Enter a Character :')
def is_vowel(str):
    if(str in 'aeiouAEIOU'):
        print(str,' is vowel')
    else:
        print(str,' is consonant')
is_vowel(str)
