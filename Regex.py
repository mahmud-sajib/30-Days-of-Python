## Day 23: Python RegEx

## Concept: Regular Expression (RegEx)

"""
A Regular Expression (RegEx) is a sequence of characters that defines a search pattern. For example:

^a...s$

The above code defines a RegEx pattern. The pattern is- any five letter string starting with 'a' and ending with 's'.

e.g. 'alias is a valid pattern whereas 'Alias' is non-valid because of uppercase 'A'.
"""

# An example of using Regex
import re # 're' module allows us to work with RegEx in Python
pattern = '^a...s$'
test_string = 'Abyss'
result = re.match(pattern,test_string)

if result:
    print("The pattern is valid")
else:
    print("The pattern is invalid")

# output: The pattern is invalid

## Concept: MetaCharacters

"""
Metacharacters are characters that are interpreted in a special way by a RegEx engine. 
Here's a list of metacharacters:
[] . ^ $ * + ? {} () \ |
"""

# [] => Square brackets - Square brackets specifies a set of characters you wish to match.
"""
+------------+-----------+---------------+
| Expression |  String   | Matched Items |
+============+===========+===============+
|            | a         | 1 match       |
+------------+-----------+---------------+
| [abc]      | ac        | 2 matches     |
+------------+-----------+---------------+
|            | Hey Jude  | No match      |
+------------+-----------+---------------+
|            | abc de ca | 5 matches     |
+------------+-----------+---------------+
"""

"""
Here, [abc] will match if the string you are trying to match contains any of the a, b or c.
"""

"""
You can also specify a range of characters using - inside square brackets.

    [a-e] is the same as [abcde].
    [1-4] is the same as [1234].
"""

"""
You can complement (invert) the character set by using 'caret ^' symbol at the start of a square-bracket.

    [^abc] means any character except a or b or c.
    [^0-9] means any non-digit character.
"""

# . => Period - A period matches any single character (except newline '\n'). 
"""
+------------+--------+---------------+
| Expression | String | Matched Items |
+============+========+===============+
|            | a      | 1 match       |
+------------+--------+---------------+
| .          | ab     | 2 matches     |
+------------+--------+---------------+
|            | abc    | 3 matches     |
+------------+--------+---------------+
|            | \n     | No match      |
+------------+--------+---------------+
"""

# ^ => Caret - The caret symbol ^ is used to check if a string starts with a certain character.
"""
+------------+--------+---------------+
| Expression | String | Matched Items |
+============+========+===============+
|            | a      | 1 match       |
+------------+--------+---------------+
| ^a         | abc    | 1 match       |
+------------+--------+---------------+
|            | bac    | No match      |
+------------+--------+---------------+

+------------+--------+------------------------------------------------+
| Expression | String |                 Matched Items                  |
+============+========+================================================+
|            | abc    | 1 match                                        |
+------------+--------+------------------------------------------------+
| ^ab        | acb    | No match (starts with a but not followed by b) |
+------------+--------+------------------------------------------------+

"""


