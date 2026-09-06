from itertools import islice
from itertools import chain

group1 = [10, 20, 30]
group2 = [40, 50, 60]
group3 = [70, 80, 90]

result = chain(group1, group2, group3)

result = list(islice(result, 2, 6))

print(result)