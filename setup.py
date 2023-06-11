from setuptools import setup
import re

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ''

extras_require = {
    "speedup": [
        "orjson>=3.7.11",
        "aiodns>=3.0.0",
        "Brotli",
        'cchardet==2.1.7<3; python_version < "3.10"',
    ],
}


setup(
    name="aiosurrealdb",
    version="0.1",
    description="aiohttp verison of the surrealdb python library",
    author="Chillymosh",
    author_email="chillymosh@gmail.com",
    url="https://github.com/your-username/your-repo",
    packages=["your_package"],
    install_requires=[
        "aiohttp",
        "pydantic",
    ],
    extras_require=extras_require,
)
