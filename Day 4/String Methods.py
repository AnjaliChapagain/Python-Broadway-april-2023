m = "hello world"
print(m.capitalize()) # Result-- Hello world
print(m.title()) # result -- Hello World
print(m.upper()) # result -- HELLO WORLD
print(m.lower()) # result --hello world

result = m.split() # result -- ["hello", "world'] . Splits from space
print(result)

result = m.split('e') # Splits from 'e'. Result ["h"' "llo world"]
print(result)
result = m.split('o') # splits from 'o'. result ["hell", " w", "rld"]
print(result)

message = ["Hello", "World"]
" ".join(message) # this joins the list with a space(" ") and returns "Hello World"
"+".join(message) # result 'Hello+World'

m = "Hello World"
result = m.find("Wo") # 'Wo' in the string is at 6th position. Result => 6
print(result)

result = m.find("Wooo") # 'Wooo' is not present in the list. result => -1
print(result)

m.replace("World", 'world') # Replace 'World' in the string to 'world'.
print(result)
# result "Hello world"


