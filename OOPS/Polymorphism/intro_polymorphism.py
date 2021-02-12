"""Polymorphism means having many forms. In programming, polymorphism
means same function name(but different signatures) being used for
different types.
Example of a built in type polymorphic function - len() function

print(len("geeks")) - len() used for string
print(len([1, 2, 3, 4])) - len() used for list
"""

# Polymorphism with class method
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_india = India()
obj_usa = USA()
for country in (obj_india, obj_usa):
    country.capital()
    country.language()
    country.type()
