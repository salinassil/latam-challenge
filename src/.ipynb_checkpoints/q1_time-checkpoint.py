from typing import List, Tuple
from datetime import datetime
from collections import Counter
import json

#Top 10 fechas con más tweets y el usuario con más publicaciones por día
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    
    with open(file_path, 'r') as f:
        tweets = [json.loads(line) for line in f]
    
    date_user_counter = Counter()
    
    for tweet in tweets:
      
            date = datetime.fromisoformat(tweet['date']).date()
            user = tweet['user']['username']
            date_user_counter[(date, user)] += 1
       
    
    
    
    date_counter = Counter()
    for (date, user), count in date_user_counter.items():
        date_counter[date] += count
    
    top_dates = date_counter.most_common(10)
    result = []
    for date, _ in top_dates:
        top_user = max([(user, count) for (d, user), count in date_user_counter.items() if d == date], key=lambda x: x[1])[0]
        result.append((date, top_user))
    
    return result