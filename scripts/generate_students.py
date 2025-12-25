from faker import Faker
import csv

fake = Faker()
Faker.seed(42)

NUM_RECORDS = 500

emails = set()
students = []

while len(students) < NUM_RECORDS:
    first = fake.first_name().lower()
    last = fake.last_name().lower()
    email = f"{first}.{last}@bowiestate.edu"

    if email in emails:
        continue

    emails.add(email)

    students.append({
        "first_name": first.capitalize(),
        "last_name": last.capitalize(),
        "email": email,
        "major": fake.random_element([
            "Computer Science",
            "Data Science",
            "Information Systems",
            "Cybersecurity"
        ]),
        "enrollment_year": fake.random_int(min=2019, max=2024)
    })

with open("data/students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "first_name",
            "last_name",
            "email",
            "major",
            "enrollment_year"
        ]
    )
    writer.writeheader()
    writer.writerows(students)

print("✅ students.csv regenerated successfully")
