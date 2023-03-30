
import re
from collections import Counter

def solution(s):
    answer = []
    m = Counter(re.findall('\d+', s))
    values, _ = zip(*m.most_common())
    answer = list(map(int, list(values)))

    return answer