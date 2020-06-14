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

# ^ => Caret - The caret symbol ^ is used to check if a string starts with a certain character.

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

# $ => Dollar - The dollar symbol $ is used to check if a string ends with a certain character.

+------------+---------+---------------+
| Expression | String  | Matched Items |
+============+=========+===============+
|            | a       | 1 match       |
+------------+---------+---------------+
| a$         | formula | 1 match       |
+------------+---------+---------------+
|            | cab     | No match      |
+------------+---------+---------------+

# * => Star - The star symbol * matches "zero or more occurrences" of the pattern left to it.

+------------+--------+---------------+
| Expression | String | Matched Items |
+============+========+===============+
|            | mn     | 1 match       |
+------------+--------+---------------+
|            | man    | 1 match       |
+------------+--------+---------------+
| ma*n       | maaan  | 1 match       |
+------------+--------+---------------+
|            | main   | No match      |
+------------+--------+---------------+
|            | woman  | 1 match       |
+------------+--------+---------------+

# + => Plus - The plus symbol + matches "one or more occurrences" of the pattern left to it.

+------------+--------+---------------+
| Expression | String | Matched Items |
+============+========+===============+
|            | mn     | No match      |
+------------+--------+---------------+
|            | man    | 1 match       |
+------------+--------+---------------+
| ma+n       | maaan  | 1 match       |
+------------+--------+---------------+
|            | main   | No match      |
+------------+--------+---------------+
|            | woman  | 1 match       |
+------------+--------+---------------+

# ? => Question Mark - The question mark symbol ? matches "zero or one occurrence" of the pattern left to it.

+------------+--------+--------------------------------------+
| Expression | String |            Matched Items             |
+============+========+======================================+
|            | mn     | 1 match                              |
+------------+--------+--------------------------------------+
|            | man    | 1 match                              |
+------------+--------+--------------------------------------+
| ma?n       | maaan  | No match (more than one a character) |
+------------+--------+--------------------------------------+
|            | main   | No match                             |
+------------+--------+--------------------------------------+
|            | woman  | 1 match                              |
+------------+--------+--------------------------------------+

# | => Alternation - Vertical bar 'or' operator | is used for alternation.

+--------------+--------+---------------+
| * Expression | String | Matched Items |
+==============+========+===============+
|              | ade    | 1 match       |
+--------------+--------+---------------+
| a or b       | cde    | No match      |
+--------------+--------+---------------+
|              | acdbea | 3 matches     |
+--------------+--------+---------------+

"""
Here, a|b match any string that contains either a or b.
"""

# () => Group - Parentheses () is used to group sub-patterns.

+-----------------+-----------+----------------------------+
|   Expression    |  String   |       Matched Items        |
+=================+===========+============================+
|                 | ab xz     | No match (space before xz) |
+-----------------+-----------+----------------------------+
| (a or b or c)xz | abxz      | 1 match                    |
+-----------------+-----------+----------------------------+
|                 | axz cabxz | 2 matches                  |
+-----------------+-----------+----------------------------+

"""
Here, (a|b|c)xz match any string that matches either a or b or c followed by xz
"""

# \ => Backslash - Backlash \ is used to escape various characters including all metacharacters. 

"""
For example: '^a' is a valid pattern for string 'apple'. But if we put '\' in front of it then '\^a' is not considered as a regex pattern & is not interpreted by the RegEx engine.
"""
+------------+--------+---------------+
| Expression | String | Matched Items |
+============+========+===============+
| ^a         | apple  | 1 match       |
+------------+--------+---------------+
| \^a        | apple  | No match      |
+------------+--------+---------------+

## Concept: Special Sequences

"""
Special sequences make commonly used patterns easier to write. Here's a list of special sequences.
"""

# \A - Matches if the specified characters are at the start of a string.

+------------+------------+----------+
| Expression |   String   | Matched? |
+============+============+==========+
| \Athe      | the sun    | Match    |
+------------+------------+----------+
|            | In the sun | No match |
+------------+------------+----------+

# \b - Matches if the specified characters are at the beginning or end of a word.

+------------+------------+----------+
| Expression |   String   | Matched? |
+============+============+==========+
| \bfoo      | a football | Match    |
+------------+------------+----------+
|            | afootball  | No match |
+------------+------------+----------+

+------------+---------------+----------+
| Expression |    String     | Matched? |
+============+===============+==========+
| foo\b      | the afoo test | Match    |
+------------+---------------+----------+
|            | the afootest  | No match |
+------------+---------------+----------+

# \B - Opposite of \b. Matches if the specified characters are 'not' at the beginning or end of a word.

+------------+------------+----------+
| Expression |   String   | Matched? |
+============+============+==========+
| \Bfoo      | a football | No match |
+------------+------------+----------+
|            | afootball  | Match    |
+------------+------------+----------+

# \d - Matches any decimal digit. Equivalent to [0-9]

+------------+--------+-----------+
| Expression | String | Matched?  |
+============+========+===========+
| \d         | 12abc3 | 3 Matches |
+------------+--------+-----------+
|            | Python | No Match  |
+------------+--------+-----------+

# \D - Matches any non-decimal digit. Equivalent to [^0-9]

+------------+--------+-----------+
| Expression | String | Matched?  |
+============+========+===========+
| \D         | 12abc3 | 3 Matches |
+------------+--------+-----------+
|            | 123    | No match  |
+------------+--------+-----------+

# \s - Matches where a string contains any whitespace character.

+------------+---------+----------+
| Expression | String  | Matched? |
+============+=========+==========+
| \s         | The Sun | 1 Match  |
+------------+---------+----------+
|            | TheSun  | No match |
+------------+---------+----------+

# \S - Matches where a string contains any non-whitespace character.

+------------+--------+-----------+
| Expression | String | Matched?  |
+============+========+===========+
| \S         | a b    | 2 Matches |
+------------+--------+-----------+
|            |        | No match  |
+------------+--------+-----------+

# \w - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]. By the way, underscore _ is also considered an alphanumeric character.

+------------+----------+-----------+
| Expression |  String  | Matched?  |
+============+==========+===========+
| \w         | 12&": ;c | 3 Matches |
+------------+----------+-----------+
|            | %"> !    | No match  |
+------------+----------+-----------+

# \W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]

+------------+--------+----------+
| Expression | String | Matched? |
+============+========+==========+
| \W         | 1a2%c  | 1 Match  |
+------------+--------+----------+
|            | Python | No match |
+------------+--------+----------+

# \Z - Matches if the specified characters are at the end of a string.

+------------+---------------+----------+
| Expression |    String     | Matched? |
+============+===============+==========+
| \W         | I like Python | 1 Match  |
+------------+---------------+----------+
|            | Python is fun | No match |
+------------+---------------+----------+

## Concept: Python RegEx Methods

# re.findall() - returns a list of strings containing all matches.
import re

string = 'hello 12 hi 89. Howdy 34'

# matches all digits [0-9]
pattern = '\d+'

result = re.findall(pattern, string) 

print(result)
# output: ['12', '89', '34']

# re.split() - opposite of re.findall(). Skips the matches & returns the non-matcheds characters.
import re

string = 'hello 12 hi 89. Howdy 34'

# matches all digits [0-9]
pattern = '\d+'

result = re.split(pattern, string)

print(result)
# output: ['hello ', ' hi ', '. Howdy ', '']

# re.sub() - substitute a string with the given input
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

replace = '*'

new_string = re.sub(pattern, replace, string)

print(new_string)
# output: abc*12de*23*f45*6

# re.search()- looks for the first location where the RegEx pattern produces a match with the string.

import re

string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
    print("Pattern found in the string")
else:
    print("Pattern not found in the string")

# Output: Pattern found in the string

## Concept: Using 'r' prefix before RegEx

"""
When 'r' or 'R' prefix is used before a regular expression, it means raw string. 
For example: '\n' is a new line whereas r'\n' means two characters: a backslash \ followed by n.
Backlash '\' is used to escape various characters. However, using 'r' prefix makes '\' treat as a normal character.
"""

import re

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string) 

print(result)
# output: ['\n', '\r']
