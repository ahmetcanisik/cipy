from setuptools import setup, find_packages # type: ignore

setup(
    name="cipy",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "c=c.cli:main",
        ],
    },
    description="Basit bir Python CLI uygulaması",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ahmetcanisik/cipy",
    author="ahmetcanisik",
    author_email="contact@ahmetcanisik.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
