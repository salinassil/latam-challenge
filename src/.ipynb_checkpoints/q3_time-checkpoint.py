from typing import List, Tuple
import json
from collections import Counter
import re

#Top 10 usuarios más influyentes en función de las menciones (@)
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    mention_counter = Counter()
    
    with open(file_path, 'r') as f:
        for line in f:
       
                tweet = json.loads(line)
                mentions = [mention['username'] for mention in tweet.get('mentionedUsers', [])]
                mention_counter.update(mentions)
       
    
    
    return mention_counter.most_common(10)