# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="my_date_creator", # the name that you will install via pip
    version="1.0",
    author="Corey Evitts",
    author_email="evitts1989@gmail.com",
    description="Creates new monthly/yearly columns from a date column",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/evitts1989/my_lambdata_ce",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)
