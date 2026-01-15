from setuptools import setup, find_packages
from config import config_manager
import pathlib

cm = config_manager()
config = cm.getConfig

setup(
    name = config["setup"]["name"],
    version = config["setup"]["version"],
    description = config["setup"]["description"],
    long_description = config["setup"]["long_description"],
    long_description_content_type = config["setup"]["long_description_content_type"],
    url = config["setup"]["url"],
    download_url = config["setup"]["download_url"],
    author = config["setup"]["author"],
    author_email = config["setup"]["author_email"],
    classifiers = config["setup"]["classifiers"],
    keywords = config["setup"]["keywords"],
    package_dir = config["setup"]["package_dir"],
    packages = pathlib.find_packages(where="src"),
    package_data = config["setup"]["package_data"],
)