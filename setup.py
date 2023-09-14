from setuptools import setup

setup(
    name="HemoPy",
    version="1.0.0",
    description="Hemodynamic calculator",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/hedayatbehnam/hemoPynamic",
    author="Behnam Hedayat",
    author_email="bhedayat.thc@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["src"],
    include_package_data=True,
    install_requires=[
        "PyQt5", "PyQt5-Qt5","PyQt5-sip", ""
    ],
    entry_points={"console_scripts": ["HemoPy=src.main:App"]},
)
