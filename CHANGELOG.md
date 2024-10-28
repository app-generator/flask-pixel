# Change Log

## [1.0.17] 2024-10-28
### Changes

- Added `Deploy on Render` Button
  - [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

## [1.0.16] 2024-10-28
### Changes

- `SECRET_KEY`: remove the random string if not found
- Update Versions
- Fix for Python 13

## [1.0.15] 2024-05-18
### Changes

- Updated DOCS (readme)
  - [Custom Development](https://appseed.us/custom-development/) Section
  - [CI/CD Assistance for AWS, DO](https://appseed.us/terms/#section-ci-cd)

## [1.0.14] 2023-08-03
### Changes

- Docs Update (readme)
- Added infos for [Flask Pixel PRO](https://appseed.us/product/pixel-bootstrap-pro/flask/)
  - Added [LIVE Demo PRO](https://flask-pixel-enhanced.onrender.com/) powered by `Flask-Security-Too`

## [1.0.13] 2023-08-03
### Changes

- Update DOCS (readme)
  - SCSS/CSS procedure using PNPM

## [1.0.12] 2023-01-03
### Changes

- `DOCS Update` (readme)
  - [Flask Pixel Lite - Go LIVE](https://www.youtube.com/watch?v=VuJ2mt3kTmc) (`video presentation`)

## [1.0.11] 2023-01-03
### Changes

- Deployment-ready for Render (CI/CD)
  - `render.yaml`
  - `build.sh`
- `DB Management` Improvement
  - `Silent fallback` to **SQLite**

## [1.0.10] 2022-11-17
### Improvements

- Document the usage of [LIVE Deployer](https://appseed.us/go-live/) 
  - Added a video presentation on README
  
## [1.0.9] 2022-11-13
### Improvements

- Compatible with [LIVE Deployer](https://appseed.us/go-live/)
  - [Deploy Flask with Drag & Drop](https://youtu.be/InVMfrzEwBQ) - `video material`

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
