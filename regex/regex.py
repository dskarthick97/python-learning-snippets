import re

pattern = re.compile("hello")
match = pattern.match("hello world")
print(match)

# Character classes
character_set_txt = """
The first season of Indian Premiere League (IPL) was played in 2008. 
The second season was played in 2009 in South Africa. 
Last season was played in 2018 and won by Chennai Super Kings (CSK).
CSK won the title in 2010 and 2011 as well.
Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017.
"""

# character_set_pattern = re.compile("[1-9][0-9][0-9][0-9]")
character_set_pattern = re.compile("[1-9]\d\d\d")
print(character_set_pattern.findall(character_set_txt))  # list of matched expressions

# character set negation -- excluding
# [^a-z] not between a to z
character_set_pattern_negation = re.compile("[^aeiou]")
print(character_set_pattern_negation.findall(character_set_txt))

# finding out all special symbols -- non-alpha numeric and non-whitespaces
special_symbol = re.compile("[^\w\s]")
print(special_symbol.findall(character_set_txt))

# Alteration
alteration_txt = """
the most common conjuctions are and, or and but.
"""

# finding all occurences of and, or, the
alteration_pattern = re.compile("and|or|the")
print(alteration_pattern.findall(alteration_txt))
