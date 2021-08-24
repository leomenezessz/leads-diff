from setuptools import setup, find_packages

setup(
    name="leads",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["pandas==1.3.1", "openpyxl==3.0.7", "click==8.0.1"],
    extras_require={"dev": ["pytest", "black==21.7b0"]},
    entry_points={
        "console_scripts": [
            "leads = leads.script:main",
        ],
    },
)
