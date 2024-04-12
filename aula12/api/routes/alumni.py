from typing import List
from fastapi import APIRouter, HTTPException
from faker import Faker
from api.model import Alumni
from api.client import get_alumni
import os

fake = Faker()

router = APIRouter(prefix="/alumni", tags=["Alumni"])


@router.get("")
def get_all_alumni() -> List[Alumni]:
    try:
        alumni_data = alumni_data_extraction()
        result = [Alumni(**alumni) for alumni in alumni_data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return result

def alumni_data_extraction():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_path = os.path.join(dir_path, "db.json")
    alumni_data = get_alumni(db=db_path)
    return alumni_data


# @router.get("/{alumni_id}")
# def get_alumni_by_id(alumni_id: str)-> Alumni:

#     return Alumni(
#         name=" ".join(fake.words(nb=2)),
#         id=alumni_id,
#         age=fake.random_int(min=18, max=50),
#         course=fake.job(),
#         graduated=True,
#         graduated_year=fake.year(),
#         gpa=fake.random_int(min=1, max=4)
#     )

# @router.get("/{alumni_name}")
# def get_alumni_by_name(alumni_name: str)-> Alumni:

#     return Alumni(
#         name=alumni_name,
#         id=fake.isbn10(),
#         age=fake.random_int(min=18, max=50),
#         course=fake.job(),
#         graduated=True,
#         graduated_year=fake.year(),
#         gpa=fake.random_int(min=1, max=4)
#     )

