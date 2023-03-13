# My 30 days of python note 

### Regular Expression cheat sheet


* "."       - Any Character Except New Line
* "\d"      - Digit (0-9)
* "\D"      - Not a Digit (0-9)
* "\w"      - Word Character (a-z, A-Z, 0-9, _)
* "\W"      - Not a Word Character
* "\s"      - Whitespace (space, tab, newline)
* "\S"      - Not Whitespace (space, tab, newline)

* "\b"      - Word Boundary
* "\B"      - Not a Word Boundary
* "^ "      - Beginning of a String
* "$ "      - End of a String

* "[]"      - Matches Characters in brackets
* "[^" ]    - Matches Characters NOT in brackets
* "| "      - Either Or
* "( )"     - Group
## Quantifiers:

* "* "      - 0 or More
* "+ "      - 1 or More
* "? "      - 0 or One
* "{3}"     - Exact Number
* "{3,4}"   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

## Python example

```py sentence = 'Start a sentence and then 123 bring it to an end'

pattern = re.compile(r'start', re.IGNORECASE) #checks both upper or lower. capital I can also be used in place of IGNORECASE
matches = pattern.search(sentence)
print(matches) 

```

### Difference between dump and dumps in python json
 	
+ json.dump() method used to write Python serialized object as JSON formatted data into a file.
+ json.dumps() method is used to encodes any Python object into JSON formatted String. 