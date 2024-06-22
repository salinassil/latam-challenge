from typing import List, Tuple
import json
from collections import Counter
import re

#Top 10 emojis más usados con su respectivo conteo
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    
    with open(file_path, 'r') as f:
        tweets = [json.loads(line) for line in f]
    
    emoji_counter = Counter()
    
    for tweet in tweets:
      
            emojis = emoji_pattern.findall(tweet['content'])
            emoji_counter.update(emojis)
       
    
    
    return emoji_counter.most_common(10)