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
3. Build the tool. This will install the tool on your machine.
   ```bash
   pip install --editable .
   ```
   To uninstall:
   ```bash
   pip uninstall create-flask-app
   ```
## Usage
To generate a Flask app with specified blueprints, run the following command:

  ```bash
  create_flask_app --app-name=your.app.name <blueprint1> <blueprint2> ...
  ```

  'blueprint1' 'blueprint2' ... is just a list of module/blueprint names to include in the app (e.g., users, products).

  After the app is done, you will see some messages in the terminal. To finish the creation process, type:
  ```bash
  cd (your.app.name.goes.here) && pip install -r requirements.txt && flask init-db && flask run
  ```


## Example
  ```bash
  create_flask_app --app-name=test users products locations
  ```
  This will generate a Flask app with users, products and locations blueprints in the `test` directory.

  Then, when the create process is finished:
  ```bash
  cd test && pip install -r requirements.txt && flask init-db && flask run
  ```
  This will finish the installation and start the app. Usually the app is available at:
  ```bash
  localhost:5000 OR 127.0.0.1:5000
  ```

## CI/CD
This app generates a basic GitHub Actions workflow file and a wsgi.py file. This should get you started on deploying the generated app.

## License
MIT License
