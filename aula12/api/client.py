import json
from typing import List

def get_alumni(db: str) -> List[dict]:
    try:
        with open(db, 'r') as data:
            result = json.load(data)
    except FileNotFoundError:
        raise Exception("Database file not found.")
    except json.JSONDecodeError:
        raise Exception("Error decoding JSON from the database.")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")
    return result
