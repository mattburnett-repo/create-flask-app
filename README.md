# create-flask-app

This project provides a command-line tool to scaffold a Flask app with specified modules (blueprints). It is based on the [Click CLI toolkit](https://click.palletsprojects.com/en/stable/) . 

This project generates the core files and directories required to set up a basic Flask application with modular blueprints. Basic database tables are created for each blueprint, and CRUD functionality for each module / blueprint is provided. There is also a basic flash messaging system.

The goal here is to reduce the amount of boilerplate effort required to start working on a small to medium size Flask project. The idea is that you start with a baseline app structure, by generating it. Once that's done, any changes you want are made to the code for the generators, not the generated / output code. You can iterate through the development process a little faster this way.

This repo is the code for the CLI tool; you have to build it yourself, following the steps in the 'Installation' section, below (it's easy to do). 

The app structure of `create-flask-app` is really simple:
```bash
scaffold_flask_app.py    # Controller/driver script
/generators              # Directory of Python functions to generate the app files.
```

There are a few other helpful files after the app is generated:
```bash
.github/workflows/deploy-check.html     # Builds the app after push to main.
wsgi.py                                 # Helpful when deploying to a provider.

```

# Installation, Usage and Example

## Installation
1. Set up a `venv` environment:
   ```bash
   # In your project folder:
    python3 -m venv venv
    source venv/bin/activate
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/mattburnett-repo/create-flask-app
   cd <repository-directory>
    ```
3. Build the tool. This will install the tool on your machine.
   ```bash
   pip install --editable .
   ```
   To uninstall:
   ```bash
   pip uninstall create-flask-app
   sudo rm /usr/local/bin/create-flask-app
   ```
## Usage
To generate a Flask app with specified blueprints, run the following command:

  ```bash
  create_flask_app --app-name=your.app.name <blueprint1> <blueprint2> ...
  ```

  'your.app.name' should be a name you chose for the app.
  'blueprint1' 'blueprint2' ... is a list of module/blueprint names to include in the app (e.g., users, products).

  After the app is done, you will see some informational messages in the terminal. To finish the creation process, type:
  ```bash
  cd (your.app.name.goes.here) && pip install -r requirements.txt && flask init-db && flask run
  ```

  From here, you can refine the generated code to meet your needs. A lot of the setup work has been done for you.

## Example
  ```bash
  create_flask_app --app-name=test users products locations
  ```
  This will generate a Flask app with users, products and locations blueprints in the `test` directory.

  Then, when the create process is finished:
  ```bash
  cd test && pip install -r requirements.txt && flask init-db && flask run
  ```
  This will finish the installation and start the app. The app should be available at:
  ```bash
  localhost:5000 OR 127.0.0.1:5000
  ```

## CI/CD
This app generates a basic GitHub Actions workflow file and a wsgi.py file. This should get you started on deploying the generated app.

## License
MIT License
