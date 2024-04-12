import json
from typing import List

def get_alumni(db: str) -> List[dict]:
    """
    Reads and decodes a JSON file to extract alumni data.

    This function opens a JSON file located at the path specified by the `db` parameter. 
    It then uses the `json.load` function to decode the JSON data into a Python object, 
    which is expected to be a list of dictionaries where each dictionary contains data about an alumnus.

    Args:
        db (str): The path to the JSON file containing the alumni data.

    Returns:
        list: A list of dictionaries, where each dictionary contains data about an alumnus.

    Raises:
        Exception: If the database file is not found, an error occurs while decoding the JSON data, 
                   or any other error occurs while reading the file.
    """
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
