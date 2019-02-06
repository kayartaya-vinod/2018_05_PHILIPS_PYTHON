import re

html = 'This is heading 1 in html: <h1>Hello, world</h1> and this is heading 2: <h2>Welcome to Python</h2> in HTML'

# re.searh('<p>.*</p>', html)
# content inside the first <p> and the last </p>

# re.searh('<p>.*?</p>', html)
# content inside the first <p> and the first </p>

# greedy
match = re.search('<.*>', html)
print(match.group())

# non-greedy
match = re.search('<.*?>', html)
print(match.group())

# greedy
match = re.search('<h1>.*>', html)
print(match.group())

# non-greedy
match = re.search('<h1>.*?>', html)
print(match.group())

