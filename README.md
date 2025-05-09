# create-flask-app

**This project is currently WIP**

This project provides a command-line tool to scaffold a Flask app with specified blueprints. It generates the core files and directories required to set up a basic Flask application with modular blueprints. Basic database tables are created for each blueprint.

This is the code for the CLI tool; you have to build it yourself, following the steps in the 'Installation' section, below. After the tool works well, I'll upload a binary version to download from this repo.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
3. Build the tool
   ```bash
   ./build_dev.sh
   ```
## Usage
To generate a Flask app with specified blueprints, run the following command:

  ```bash
  python create_flask_app/scaffold_flask_app.py <blueprint1> <blueprint2> ... --output <output-directory>
  ```

  'blueprint1' 'blueprint2' ... 
  
  — List of blueprint names to include in the app (e.g., users, products).


  --output <output-directory> or -o 'output-directory' 
  
  — Optional. Specify the directory to generate the app in. Defaults to the current working directory.

## Example
  ```bash
  python create_flask_app/scaffold_flask_app.py users products -o my_flask_app
  ```

  This will generate a Flask app with users and products blueprints in the my_flask_app directory.

## License
MIT License
