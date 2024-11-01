from faker import Faker
from pymongo import MongoClient
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

# Set up Faker and MongoDB client
fake = Faker()
client = MongoClient(os.getenv("URI"))
db = client[os.getenv("DB")]
col = db[os.getenv("COLLECTION")]

# Function to generate contract metadata
def generate_contract_metadata():
    contract_id = fake.uuid4()
    title = f"{fake.bs().title()} Contract"
    contract_type = random.choice(["Employment", "Non-Disclosure", "Service Agreement", "Sales", "Lease"])
    date_created = fake.date_between(start_date="-5y", end_date="today")
    date_signed = date_created + timedelta(days=random.randint(1, 30))
    expiry_date = date_signed + timedelta(days=random.randint(365, 1825))  # 1 to 5 years after signed date
    parties_involved = [
        {
            "party_id": fake.uuid4(),
            "name": fake.company() if random.choice([True, False]) else fake.name(),
            "type": "Organization" if random.choice([True, False]) else "Individual",
            "contact_information": {
                "email": fake.email(),
                "phone": fake.phone_number(),
                "address": fake.address()
            },
            "role": random.choice(["Client", "Vendor", "Employer", "Employee"])
        } for _ in range(random.randint(1, 3))  # 1 to 3 parties
    ]
    status = random.choice(["Active", "Expired", "Terminated"])

    print(type(date_created))

    return {
        "contract_id": contract_id,
        "title": title,
        "type": contract_type,
        "date_created": datetime.combine(date_created,datetime.min.time()),
        "date_signed": datetime.combine(date_signed,datetime.min.time()),
        "expiry_date": datetime.combine(expiry_date,datetime.min.time()),
        "parties_involved": parties_involved,
        "status": status
    }

# Populate the col with fake data
def populate_contract_metadata(n=100):
    contracts = [generate_contract_metadata() for _ in range(n)]
    col.insert_many(contracts)
    print(f"{n} contract records inserted into MongoDB.")

# Run the script to insert data
populate_contract_metadata(100)  # Change the number to your desired amount of records
