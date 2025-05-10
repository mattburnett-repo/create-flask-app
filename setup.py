from setuptools import setup, find_packages

setup(
    name="create-flask-app",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "Flask",
        "Click"
    ],
    entry_points={
        "console_scripts": [
            "create-flask-app = scaffold_flask_app:scaffold_flask_app", 
        ],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)