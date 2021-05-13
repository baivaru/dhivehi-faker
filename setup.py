import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dhivehi-faker-baivaru',
    version='0.1.0',
    author="Baivaru",
    author_email="admin@baivaru.net",
    description="It's like Faker but Dhivehi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/baivaru/dhivehi-faker",
    project_urls={
        "Bug Tracker": "https://github.com/baivaru/dhivehi-faker/issues",
    },
    packages=setuptools.find_packages(where='src'),
    package_dir={"": "src"},
    package_data={'': ['*.json', 'data/*.json']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
    license="GPLv3",
)