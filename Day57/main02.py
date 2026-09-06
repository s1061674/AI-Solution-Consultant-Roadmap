from itertools import islice
from itertools import chain

groups = [
    ["Python", "AI"],
    ["Git", "SQL"],
    ["API", "Docker"]
]

result = chain.from_iterable(groups)

result = list(islice(result,4))

print(result)