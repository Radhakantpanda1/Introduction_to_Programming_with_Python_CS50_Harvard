

print("Hello World")
"""
 A function is like an action or a verb that
lets you do something in the program.
And generally speaking, any language comes with some predetermined set
of functions-- some very basic actions or verbs that the computer will already
know how to do for you, that the language, really,
will know how to do for you.
"""

"""
A bug is a mistake in a program and they can take so many forms.
"""

# ask user for their name and print hello 
user_name=input("Enter your name ")
# input function takes arguments from user then return it to the variable 
# for example here the value returned by the input functionn is stored inside user_name
print("Hello,", user_name)
print("Hello, "+ user_name) # -> + is used for concatenation

print("username, ",end='')
print(user_name)

print("username,",user_name ,sep='***')


# variable- it stores a value/ it is container for some value
# = is the assignment operator
"""
Comments are notes to yourself in your code
and you include comments by way of a special symbol-- in Python
it's going to be the hash symbol, typically--
and that allows you to write the equivalent
of a note to yourself but in a way that's not going to break your code.
The computer actually ignores your comment.
"""

"""

 print(*objects, sep=' ', end='\n', file=None, flush=False)


Print objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present, must be given as keyword arguments.

All non-keyword arguments are converted to strings like str() does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; they can also be None, which means to use the default values. If no objects are given, print() will just write end.
"""
# string - collection of characters

print("Hello, \"sinu\" ")

print(f"Hello,{user_name} ")