from setuptools import setup, find_packages

setup(
    name="copanzers",
    include_package_data=True,
    #package_data={"": ["*.png", "*.json", "*.py"]},
    package_dir={"copanzers": "copanzers"},
    packages=find_packages(),
    scripts=["bin/tanks"]
)
