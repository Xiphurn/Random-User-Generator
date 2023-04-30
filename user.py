"""Module to generate random users"""
import faker
import logging
from pathlib import Path

Base_dir = Path(__file__).resolve().parent
logging.basicConfig(filename=Base_dir/'user.log', level=logging.INFO)

fake = faker.Faker()

def get_user():
    """Randomly generate the first and last name of a user

    Returns:
        str: First name + " " + Last name
    """
    logging.info("Generating user.")
    return f"{fake.first_name()} {fake.last_name()}"

def get_users(n):
    """Generate a list of users

    Args:
        n (int): Number of users to generate

    Returns:
        list[str]: List of n users

    """
    
    logging.info(f"Generating {n} users.")
    return [get_user() for _ in range(n)]

if __name__ == "__main__":
    users = get_users(n=5)
    print(users)
