import json
from typing import List

def get_alumni(db: str) -> List[dict]: 
    result: List[dict] = []

    with open(db, 'r') as data:
        result = json.load(data)

    return result
