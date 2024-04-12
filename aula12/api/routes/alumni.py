from typing import List

from fastapi import APIRouter, HTTPException
from faker import Faker

from api.model import Alumni
from api.client import get_alumni

fake = Faker()

router = APIRouter(prefix="/alumni", tags=["Alumni"])

def alumni_data_extraction():
    """
    Extracts alumni data from a JSON database.

    This function reads a JSON file located at "/workspace/db/db.json" which is expected to contain alumni data.
    It uses the `get_alumni` function to extract the data from the file and returns it.

    Returns:
        list: A list of dictionaries, where each dictionary contains data about an alumnus.
    """
    db_path = "/workspace/db/db.json"
    alumni_data = get_alumni(db=db_path)
    return alumni_data

@router.get("")
def get_all_alumni() -> List[Alumni]:
    try:
        alumni_data = alumni_data_extraction()
        result = [Alumni(**alumni) for alumni in alumni_data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return result

@router.get("/id/{alumni_id}")
def get_alumni_by_id(alumni_id: str)-> Alumni:
    try:
        alumni_data = alumni_data_extraction()
        alumni = next((alumni for alumni in alumni_data if alumni["id"] == alumni_id), None)
        if alumni is None:
            raise HTTPException(status_code=404, detail="Alumni not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return Alumni(**alumni)

@router.get("/name/{alumni_name}")
def get_alumni_by_name(alumni_name: str)-> Alumni:
    try:
        alumni_data = alumni_data_extraction()
        alumni = next((alumni for alumni in alumni_data if alumni["name"] == alumni_name), None)
        if alumni is None:
            raise HTTPException(status_code=404, detail="Alumni not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return Alumni(**alumni)