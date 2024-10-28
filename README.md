# [Flask Pixel Lite](https://appseed.us/product/pixel-bootstrap/flask/)

`Open-Source` **[Flask App](https://appseed.us/apps/flask/)** crafted on top of a modern design. `Pixel` is a free and open-source `Bootstrap 5` UI Kit featuring over 80 fully coded UI elements and example pages that will help you prototype and build a website for your next project.

- 👉 [Flask Pixel Lite](https://appseed.us/product/pixel-bootstrap/flask/) - product page
- 👉 [Flask Pixel Lite](https://flask-pixel-lite.appseed-srv1.com/) - LIVE Deployment

<br /> 

## Start with `Docker`

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/flask-pixel.git
$ cd flask-pixel
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />  

## Manual Build 

> Download the code 

```bash
$ git clone https://github.com/app-generator/flask-pixel.git
$ cd flask-pixel
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ export FLASK_APP=run.py
$ export FLASK_DEBUG=True
```

<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ # CMD 
$ set FLASK_APP=run.py
$ set FLASK_DEBUG=True
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_DEBUG = "True"
```

<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

### 👉 Create Users

By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up: 

- Start the app via `flask run`
- Access the `registration` page and create a new user:
  - `http://127.0.0.1:5000/register`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:5000/login`

<br />

## CSS/SCSS Update

In order to customize the UI (primary/seconday colors), follow this setup:

- Navigate to `apps/static/assets`
- Edit SCSS files 
- Install dependencies using [PNPM](https://pnpm.io/)
  - `pnpm i`
- Recompile the SCSS files with Gulp
  - `gulp`

> NOTE: the above setup was tested using:

- Node `v16.15.0`
- Gulp CLI `2.3.0`, LOCAL `4.0.2`
- PNPM `v8.6.0`

<br />

## Codebase Structure

The project is coded using blueprints, app factory pattern, dual configuration profile (development and production) and an intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                           # A simple app that serve HTML files
   |    |    |-- routes.py                  # Define app routes
   |    |
   |    |-- authentication/                 # Handles auth routes (login and register)
   |    |    |-- routes.py                  # Define authentication routes  
   |    |    |-- models.py                  # Defines models  
   |    |    |-- forms.py                   # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>          # CSS files, Javascripts files
   |    |
   |    |-- templates/                      # Templates used to render pages
   |    |    |-- includes/                  # HTML chunks and components
   |    |    |    |-- navigation.html       # Top menu component
   |    |    |    |-- sidebar.html          # Sidebar component
   |    |    |    |-- footer.html           # App Footer
   |    |    |    |-- scripts.html          # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- index.html            # Index page
   |    |         |-- 404-page.html         # 404 page
   |    |         |-- *.html                # All other pages
   |    |    
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # App Dependencies
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

<br />

## PRO Version

> For more components, pages and priority on support, feel free to take a look at this amazing starter:

**Pixel PRO** is a premium design crafted by the `Themesberg` agency on top of Bootstrap 5 Framework. **Pixel** is a premium `Bootstrap 5 UI Kit` that provides 1000+ components, 50+ sections and 35 example pages including a fully fledged user dashboard.

- 👉 [Flask Pixel PRO](https://appseed.us/product/pixel-bootstrap-pro/flask/) - product page
- 👉 [Flask Pixel PRO](https://flask-pixel-pro.appseed-srv1.com/) - LIVE Demo

![Pixel Bootstrap PRO - Full-Stack Starter generated by AppSeed](https://user-images.githubusercontent.com/51070104/168760719-f0e45406-2b2a-43e0-badf-fa953edb62b8.png)

<br />

---
[Flask Pixel Lite](https://appseed.us/product/pixel-bootstrap/flask/) - Open-source Flask Starter provided by **[App Generator](https://app-generator.dev/)**.
