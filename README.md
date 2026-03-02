## create-flask-app

`create-flask-app` is a command-line tool for quickly scaffolding small to medium-sized Flask applications. Built in Python with Click, it generates a clean, opinionated project structure that removes repetitive setup and lets developers focus on application logic.

I designed and implemented the tool with speed, clarity, and scalability in mind. The generated architecture encourages best practices such as modular design, environment-specific configuration, and optional extensions for databases, testing, and templating.

By automating common setup tasks, `create-flask-app` improves developer flow and iteration speed. It reflects my focus on developer experience and on building maintainable, well-documented tools that support long-term work, not just quick starts. 

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
