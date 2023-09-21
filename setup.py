from setuptools import find_packages, setup

with open("VERSION", "r") as f:
    VERSION = f.read().strip()

DESCIPTION = "Implementation of async axabc.uow pattern using pyredis"

with open("requirements.txt", "r") as requirements_file:
    REQUIREMENTS = requirements_file.readlines()


setup(
    name="async_redis_uow",
    version=VERSION,
    author="axdjuraev",
    author_email="<axdjuraev@gmail.com>",
    description=DESCIPTION,
    packages=find_packages(),
    install_requires=REQUIREMENTS,
)

