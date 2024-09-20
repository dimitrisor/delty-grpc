from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="delty_grpc",
    version="0.1.2",
    author="Your Name",
    author_email="your.email@example.com",
    description="gRPC package for Delty project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dimitrisor/delty-grpc",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=[
        "grpcio",
        "protobuf",
    ],
)
