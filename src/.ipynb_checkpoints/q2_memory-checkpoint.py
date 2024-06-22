from typing import List, Tuple
import json
from collections import Counter
import re

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    
    emoji_counter = Counter()
    
    with open(file_path, 'r') as f:
        for line in f:
         
                tweet = json.loads(line)
                emojis = emoji_pattern.findall(tweet['content'])
                emoji_counter.update(emojis)
            
    
    
    return emoji_counter.most_common(10)