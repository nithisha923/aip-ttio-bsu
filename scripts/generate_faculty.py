from faker import Faker
import csv

fake = Faker()
Faker.seed(99)

NUM_RECORDS = 50

emails = set()
faculty_members = []

while len(faculty_members) < NUM_RECORDS:
    first = fake.first_name().lower()
    last = fake.last_name().lower()
    email = f"{first}.{last}@bowiestate.edu"

    if email in emails:
        continue

    emails.add(email)

    faculty_members.append({
        "first_name": first.capitalize(),
        "last_name": last.capitalize(),
        "email": email,
        "department": fake.random_element([
            "Computer Science",
            "Mathematics",
            "Engineering",
            "Business"
        ]),
        "hire_year": fake.random_int(min=2010, max=2023)
    })

with open("data/faculty.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "first_name",
            "last_name",
            "email",
            "department",
            "hire_year"
        ]
    )
    writer.writeheader()
    writer.writerows(faculty_members)

print("✅ faculty.csv regenerated successfully")
