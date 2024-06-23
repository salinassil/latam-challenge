import json
from collections import Counter
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_counter = Counter()
    
    with open(file_path, 'r') as f:
        for line in f:
            try:
                tweet = json.loads(line)
                mentions = [mention['username'] for mention in tweet.get('mentionedUsers', [])]
                mention_counter.update(mentions)
            except (json.JSONDecodeError, KeyError, TypeError):
                continue  # Salta líneas malformadas o con claves faltantes
    
    return mention_counter.most_common(10)