# [Boierplate Code Flask](https://appseed.us/boilerplate-code/flask)

> Template [boilerplate code](https://appseed.us/boilerplate-code) used by [AppSeed](https://appseed.us) to generate simple web apps coded in [Flask](https://palletsprojects.com/p/flask/)

## Features

- UI-Ready, Jinja2 templating
- SQLite database, Flask-SQLAlchemy ORM
- Session-Based auth flow (login, register)
- UI Kit: **Paper Kit** by **Creative-Tim**
- MIT License
- Free support via **Github** issues tracker
- Paid 24/7 Live Support via [Discord](https://discord.gg/fZC6hup).

> Links

- LIVE Demo: [Boierplate Code Flask](https://boilerplate-code-flask.appseed.us/login.html)
- Product Page: [Boierplate Code Flask](https://appseed.us/boilerplate-code/flask)

<br />

![Boierplate Code Flask - Open-Source template project provided by AppSeed.](https://raw.githubusercontent.com/app-generator/boilerplate-code-flask/master/media/boilerplate-code-flask-screen.png)

<br />

## Build from sources

```bash
$ # Clone the sources
$ git clone https://github.com/app-generator/boilerplate-code-flask.git
$ cd boilerplate-code-flask
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install requirements
$ pip3 install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Run the application
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the app in browser: http://127.0.0.1:5000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## Code-base structure

The project has a super simple structure, represented as bellow:

```bash
< PROJECT ROOT >
    |
    |--- app/__init__.py
    |--- app/
    |     | --- <static/assets>
    |     |         |
    |     |         |--- <css>
    |     |         |--- <Js>
    |     |         |--- <img>
    |     |
    |     | --- <templates>
    |     |         |
    |     |         |---<includes>                     # Page chunks, components
    |     |         |       |
    |     |         |       | --- navigation.html      # Top bar
    |     |         |       | --- sidebar.html         # Left sidebar
    |     |         |       | --- scripts.html         # JS scripts common to all pages
    |     |         |       | --- footer.html          # The common footer
    |     |         |
    |     |         |---<layouts>                      # App Layouts (the master pages)
    |     |         |       |
    |     |         |       | --- base.html            # Used by common pages like index, UI
    |     |         |       | --- base-fullscreen.html # Used by auth pages (login, register)
    |     |         |
    |     |         |---<accounts>                     # Auth Pages (login, register)
    |     |         |       |
    |     |         |       | --- login.html           # Use layout `base-fullscreen.html`
    |     |         |       | --- register.html        # Use layout `base-fullscreen.html`  
    |     |         |
    |     |     index.html                             # The default page
    |     |     page-404.html                          # Error 404 page (page not found)
    |     |     page-500.html                          # Error 500 page (server error)
    |     |       *.html                               # All other pages provided by the UI Kit
    |
    |--- requirements.txt
    |
    |--- run.py
    |
    |-----------------------------
```

<br />

## Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The offcial website
- [Boilerplate Code](https://appseed.us/boilerplate-code) - Index provided by **AppSeed**
- [Boilerplate Code](https://github.com/app-generator/boilerplate-code) - Index published on Github

<br />

---
[Boierplate Code Flask](https://appseed.us/boilerplate-code/flask) - Provided by **AppSeed** [Web App Generator](https://appseed.us/app-generator).
