from setuptools import setup

with open("README.md","r",encoding = "utf-8") as f:
     long_decription = f.read()

setup(
    name = "src",
    version = "0.0.1",
    author = "mdsaifk",
    description = "A small package for dvc ML pipleine demo",
    long_description= long_decription,
    url = "https://github.com/mdsaifk/dvc_ml_demo",
    author_email = "mdsaifkhan200@gmail.com",
    package_name= ["src"],
    license= "GNU",
    python_requires = ">=3.7",
    install_requires = ['dvc','pandas','scikit-learn']
)