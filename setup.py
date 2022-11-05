from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="dataclass-map-and-log",
    version="0.1.1",
    description="Map objects to dataclasses and log differencies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/namelivia/dataclass-map-and-log",
    author="José Ignacio Amelivia Santiago",
    author_email="jignacio.amelivia@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="dataclass, api",
    install_requires=["pydantic"],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    python_requires=">=3.8, <4",
    project_urls={
        "Bug Reports": "https://github.com/namelivia/dataclass-map-and-log/issues",
    },
)
