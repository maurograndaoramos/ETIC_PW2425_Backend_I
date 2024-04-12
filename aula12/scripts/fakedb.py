from faker import Faker
import json

fake = Faker()

if __name__ == '__main__':


    total_rows = 20

    result = [
        dict(
            name=fake.name(),
            id=fake.uuid4(),
            age=fake.random_int(min=18, max=60),
            course=fake.job(),
            graduated=fake.boolean(),
            graduated_year=fake.year(),
            gpa=fake.random_int(min=1, max=4)
        )
        for _ in range(total_rows)
    ]

    with open("db/db.json","w") as file:
        file.writelines(json.dumps(result, indent=2))