from faker import Faker

fake = Faker()

first_name = fake.first_name()
last_name = fake.last_name()

email = f"{first_name.lower()}.{last_name.lower()}@bowiestate.edu"

print(first_name, last_name)
print(email)
