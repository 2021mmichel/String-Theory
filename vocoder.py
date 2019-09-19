# 1. Write a function called shout that takes in a string as an argument and returns it in all caps.

# def shout(string):
#     output = string.upper()
#     print(output)
#     return(output)

# a = shout("sleep")
# print(a)

# 2. Write a function called whisper that takes in a string as an argument and returns it in all lowercase.

# def whisper(string):
#     output = string.lower()
#     print(output)
#     return(output)

# a = whisper("hippo")
# print(a)

# 3. Write a function called how_many_letters that takes in a string as an argument and returns the number of letters in that string.

# def how_many_letters(string):
#     output = len(string)
#     print(output)
#     return(output)

# a = how_many_letters("giraffe")
# print(a)

# 4. Write a function called work_it that takes in a string as an argument and returns it backwards and with the first letter capitalized.
#    For example, work_it("I put my thing down flip it and reverse it") would return "Ti esrever dna ti pilf nwod gniht ym tup i"


# def work_it(txt):
#     output = txt.capitalize()
#     output = output [::-1]
#     print(output)
#     return(output)

# a = work_it("marco")
# print(a)

# 5. Write a function called repeat_it that takes in a word and a number, and returns the word that many times.
#    For example, repeat_it("Banana", 3) would return "BananaBananaBanana"

def repeat_it(txt):
    output = txt*3
    print(output)
    return(output)

a = repeat_it("marco")
print(a)

# 6. Write a function called will_it_nametag that takes in a name and a number, and tells you whether the name can be printed on a nametag that size.
#    For example, will_it_nametag("Peter", 10) will return True, but will_it_nametag("Peter", 4) will return False, because "Peter" is 5 letters long, and needs at least 5 spaces to fit on a nametag.

def will_it_nametag(x, y):
    length = len(x)
    if length <= y:
        return True
        else:
            return False

print(will_it_nametag("Peter", 6))


# 7. Write a function called add_liar that takes in two numbers and prints out a lie like "Sorry, I don't know how to add ___ and ___."
#    BUT even though it *prints* that it doesn't know the answer, have the function return the correct answer anyways.

def add_liar(num1, num2):
    print("Sorry I can't add")
    return num1+num2

print(add_liar(2,1))

# 8. CHALLENGE: Now that you've written all these functions, try combining them. what would happen if you tried to call repeat_it(work_it("Stressed"), 3) ?





# 9. MEGA CHALLENGE: Write a function called doubler that takes in a string and returns it with every letter doubled.
#    For example, doubler("Lost in the Woods") would return "LLoosstt iinn tthhee WWooooddss"


# 10. SUPER MEGA CHALLENGE: Head to https://codingbat.com/python/String-2 and attempt some of the challenges there!










# def will_it_nametag(txt):
#     output = len(txt)<=4
#     print(output)
#     return(output)

# a = will_it_nametag("bare")
# print(a)