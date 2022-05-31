# Change Log

## [1.0.8] 2022-05-30
### Improvements

- Built with [Pixel Lite Generator](https://appseed.us/generator/pixel-bootstrap/)
  - Timestamp: `2022-05-31 08:12`

## [1.0.7] 2022-01-17
### Improvements

- Bump Flask Codebase to [v2.0.0](https://github.com/app-generator/boilerplate-code-flask/releases)
- Dependencies update (all packages) 
  - Flask==2.0.2 (latest stable version)
  - flask_wtf==1.0.0
  - jinja2==3.0.3
  - flask-restx==0.5.1

## [1.0.6] 2021-09-16
### Improvements

- Bump Flask Codebase to [v1.0.7](https://github.com/app-generator/boilerplate-code-flask/releases)
  - Rename model `User` to `Users` to avoid name conflict with ORACLE DBMS
    - Impacted files: `app/{model.py, util.py, viewws.py}`

## [1.0.5] 2021-09-16
### Improvements & Fixes

- Bump Flask Codebase to [v1.0.6](https://github.com/app-generator/boilerplate-code-flask/releases)
  - Dependencies update (all packages)
    - Use Flask==2.0.1 (latest stable version)
  - Better Code formatting
  - Improved Files organization
  - Optimize imports
  - Docker Scripts Update 

## [1.0.4] 2021-07-18
### Tooling

- Added scripts to recompile the SCSS files
    - `app/static/assets/` - gulpfile.js
    - `app/static/assets/` - package.json
- `Update README` - [Recompile SCSS](https://github.com/app-generator/flask-pixel-lite#recompile-css) (new section)

## [1.0.3] 2021-05-21
### Improvements

- Bump UI: [Jinja Pixel Lite](https://github.com/app-generator/jinja-pixel-lite) v1.0.2 / Pixel Lite v4.0.0
- Bump Codebase: [Flask Boilerplate](https://github.com/app-generator/boilerplate-code-flask) v1.0.5

## [1.0.2] 2020-03-25
### Improvements

- Bump [Flask Codebase(https://github.com/app-generator/boilerplate-code-flask) v1.0.4
- Freeze used versions in `requirements.txt`
    - flask_sqlalchemy = 2.4.4
    - sqlalchemy = 1.3.23

## [1.0.1] 2020-01-12
### Improvements

- Bump UI: [Pixel Lite](https://github.com/themesberg/pixel-bootstrap-ui-kit) v3.1.2
- Codebase: [Flask Boilerplate](https://github.com/app-generator/boilerplate-code-flask) v1.0.3

## [1.0.0] 2020-02-07
### Initial Release
