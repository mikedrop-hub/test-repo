from setuptools import setup, find_packages

setup(
    name="my-expense-app",
    version="1.1",
    packages=find_packages(),
    scripts=["app.py"],
    author="Michael",
    author_email="michael@example.com",
    description="Top Tier Budgeting Program",
    long_description="A top tier budgeting program that the people absolutely love.",
)