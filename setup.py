from setuptools import setup, find_packages

setup(
    name="create-flask-app",  # The name of your CLI tool
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "Click"
    ],
    entry_points={
        "console_scripts": [
            "create-flask-app = create_flask_app.scaffold_flask_app:scaffold_flask_app", 
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
