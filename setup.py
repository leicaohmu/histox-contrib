import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="histox-contrib",
    version="0.1.2",
    author="Lei Cao",
    author_email="caolei@hrbmu.edu.cn",
    description="Community contributions for HisToX",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leicaohmu/histox-contrib",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "histox",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
