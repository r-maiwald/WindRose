from setuptools import setup

setup(
    name="windrose",
    version="1.0",
    description="",
    author="Robert Maiwald",
    author_email="rmaiwald@iup.uni-heidelberg.de",
    packages=["windrose"],
    install_requires=[
        "matplotlib",
        "numpy",
        "pytest",

    ],  # external packages as dependencies
    scripts=[],
)
