
#VALID SENTENCE CASES

#Starts with capital letter
#Even number of quotation marks
#ends with  . ? !
#No period characters other than last 
#Numbers below 13 are spelt in word form e.g one 


def check_first_letter(String):
    """Checks the first letter of the string to see if it 
    is uppercase and if it is True will be returned otherwise 
    False is returned"""

    #Looks at the first letter
    first_letter= String[0]
    
    #Checks if the first letter is uppercase
    if first_letter.isupper():
        return True
    return False

def check_quotations(String):
    """Checks through each letter in the string 
    to see if there are a even number
    of quotation marks in the string if there are then 
    True is returned otherwise False is returned"""

    #Counter to see how many quotation marks there were in the string
    quote_count=0
    for i in String:
        if i == '"':
            #Incrementing quote counter every time a quotation mark is found
            quote_count+=1
    #Checks if the quote count is even
    if quote_count%2 == 0:
        return True
    return False

def check_last_letter(String):
    """Checks if the last letter of the string is either . or ? or ! if the last letter
    is one of these letters then True is returned otherwise False is returned"""

    #The valid ending letters as a set
    valid_last_letters={'.' ,'?' ,'!'}

    #Getting the last letter of the string
    last_letter= String[len(String)-1]

    #Checking if the last letter matches one of the valid last letters
    if last_letter in valid_last_letters:
        return True
    return False

def check_for_period(String):
    """Checks if there are any periods in the string that are not the last letter if 
    there are then False is returned otherwise True is returned """
    #Making a substring of the string without the last letter to remove the trailing period
    adjusted_string= String[:-1]
    #Checks if there are any periods in the substring
    if '.' in adjusted_string:
        return False
    return True

def check_numbers(String):
    """Checks to see if there are numerical values under 13 in the string if 
    there are then False is returned otherwise False is returned"""

    #Spliting the string into a list
    string_list= String.split()

    #Looping through the string list
    for i in string_list:
        #Checks if the element is numeric and under 13 
        if i.isnumeric() and int(i) <  13:
            return False
        #Checks if the element contains any numerical values e.g in cases of "12,"
        elif any(char.isdigit() for char in i):
            numerical_value=i
            #Going through each character in the current string
            for y in i :
                #Removing non integers from the string
                if y.isdigit() == False:
                    numerical_value= numerical_value.replace(y,'')
            #Checking if the number is below 13 
            if int(numerical_value) < 13:
                return False 
    return True

def is_sentence_valid(String):
    """Checks if a sentence is valid based on a set of rules if valid then True is returned otherwise False is returned
    
    ALL VALID SENTENCES DOC TESTS
    >>> is_sentence_valid('The quick brown fox said “hello Mr lazy dog”.')
    True
    >>> is_sentence_valid('The quick brown fox said hello Mr lazy dog.')
    True
    >>> is_sentence_valid('One lazy dog is too few, 13 is too many.')
    True
    >>> is_sentence_valid('One lazy dog is too few, thirteen is too many.')
    True
    >>> is_sentence_valid('How many "lazy dogs" are there?')
    True

    All INVALID SENTENCES DOC TESTS
    >>> is_sentence_valid('The quick brown fox said "hello Mr. lazy dog".')
    False
    >>> is_sentence_valid('the quick brown fox said “hello Mr lazy dog".')
    False
    >>> is_sentence_valid('"The quick brown fox said “hello Mr lazy dog."')
    False
    >>> is_sentence_valid('One lazy dog is too few, 12 is too many.')
    False
    >>> is_sentence_valid('Are there 11, 12, or 13 lazy dogs?')
    False
    >>> is_sentence_valid('There is no punctuation in this sentence')
    False

    Inorder to run doc test run the command python -m doctest SentenceValidator.py
    """

    #Only returns True if all checks have been passed
    if check_first_letter(String) and check_quotations(String) and check_last_letter(String) and check_for_period(String) and check_numbers(String):
        return True
    return False




