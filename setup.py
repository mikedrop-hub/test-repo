from setuptools import setup, find_packages

setup(
    name="my-expense-app",
    version="1.1",
    packages=find_packages(),
    py_modules=["app"],
    install_requires=[
        'wikipedia-api',
    ],
    entry_points={
        'console_scripts': [
            'budget=app:main',
        ],
    },
    author="Michael",
    author_email="michael@example.com",
    description="Top Tier Budgeting Program",
    long_description="A top tier budgeting program that the people absolutely love.",
)