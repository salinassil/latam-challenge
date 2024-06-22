from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict, Counter

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:

    date_user_counter = defaultdict(Counter)
    
    with open(file_path, 'r') as f:
        for line in f:
            
                tweet = json.loads(line)
                date = datetime.fromisoformat(tweet['date']).date()
                user = tweet['user']['username']
                date_user_counter[date][user] += 1
         
    
    top_dates = sorted(date_user_counter.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]
    result = [(date, user_counts.most_common(1)[0][0]) for date, user_counts in top_dates]
    
    return result