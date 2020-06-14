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

# MetaCharacters

"""
Metacharacters are characters that are interpreted in a special way by a RegEx engine. 
Here's a list of metacharacters:
[] . ^ $ * + ? {} () \ |
"""

# [] - Square brackets
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

+------------+------+------+
| Expression | Tue  | Wed  |
+============+======+======+
| 田中       | (^^) | (xx) |
+------------+------+------+
| 鈴木       | (^^) | (^^) |
+------------+------+------+
| 鈴木       | (^^) | (^^) |
+------------+------+------+

+------+------+------+------+------+------+
| Mon  | Tue  | Wed  | Thu  | Fri  |      |
+======+======+======+======+======+======+
| 田中 | (^^) | (xx) | (xx) | ('') | (^^) |
+------+------+------+------+------+------+
| 鈴木 | (^^) | (^^) | ('') | (xx) | (^^) |
+------+------+------+------+------+------+
| Mon  | Tue  | Wed  | Thu  | Fri  |      |

