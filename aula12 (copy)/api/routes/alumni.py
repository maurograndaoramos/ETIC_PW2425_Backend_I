from typing import List
from fastapi import APIRouter
from faker import Faker
from api.model import Alumni
from api.client import get_alumni

fake = Faker()

router= APIRouter(prefix="/alumni", tags=["Alumni"])


@router.get("")
def get_all_alumni()-> List[Alumni]:
    result = [
        Alumni(**alumni)
        for alumni in get_alumni(db="./db/db.json")
    ]
    return result 

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

