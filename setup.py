from setuptools import setup, find_packages

setup(
    name="openphoto",
    version="0.1.0",
    description="An open-source Photoshop alternative.",
    author="Vishwas",
    packages=find_packages(),
    install_requires=[
        "PyQt6>=6.5.0",
        "Pillow>=10.0.0",
        "numpy>=1.24.0"
    ],
    entry_points={
        "console_scripts": [
            "openphoto=openphoto.main:main",
        ],
    },
    python_requires=">=3.8",
)
