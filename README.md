# FISCO BCOS Toolbox
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
FISCO BCOS Toolbox created by SUIBE-Blockchain-Team.

由上海对外经贸大学区块链技术与应用研究中心研发的针对 FISCO BCOS 的工具箱。

**DEMO:** <https://tools.doge.university/>

![](https://img.shields.io/badge/SUIBE--B-CopyRight-blue)
  [![Build Status](https://travis-ci.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox.svg?branch=master)](https://travis-ci.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox)
  ![](https://img.shields.io/badge/language-python-orange.svg)
  ![](https://img.shields.io/badge/license-MIT-000000.svg)

内容包括：

- FISCO BCOS 地址生成（已完成）
- SDK Config 在线生成 （已完成）
- 开发中的数据模拟（构建中）
- 智能合约案例合集（构建中）
- SDK 功能通过WEB页面调用（构建中）
……

环境变量文件见`.envrc`。

![](https://tva1.sinaimg.cn/large/007S8ZIlly1ge8j964uioj31j10u0470.jpg)

## Contributors

<!-- ALL-CONTRIBUTORS-LIST: START - Do not remove or modify this section -->
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/leeduckgo"><img src="https://avatars1.githubusercontent.com/u/12784118?v=4" width="100px;" alt=""/><br /><sub><b>李大狗</b></sub></a><br /><a href="https://github.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox/commits?author=leeduckgo" title="Code">💻</a></td>
    <td align="center"><a href="https://blog.csdn.net/qq_19381989"><img src="https://avatars3.githubusercontent.com/u/45918704?v=4" width="100px;" alt=""/><br /><sub><b>HuiFeng Tang</b></sub></a><br /><a href="https://github.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox/commits?author=99Kies" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/dengcheng6502"><img src="https://avatars0.githubusercontent.com/u/30894162?v=4" width="100px;" alt=""/><br /><sub><b>Mu Li</b></sub></a><br /><a href="https://github.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox/commits?author=dengcheng6502" title="Code">💻</a></td>
    <td align="center"><a href="http://cnmf.net.cn"><img src="https://avatars1.githubusercontent.com/u/42673461?v=4" width="100px;" alt=""/><br /><sub><b>肖越</b></sub></a><br /><a href="https://github.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox/commits?author=xiaoyue2019" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/lekko1988"><img src="https://avatars0.githubusercontent.com/u/19570787?v=4" width="100px;" alt=""/><br /><sub><b>lekko1988</b></sub></a><br /><a href="https://github.com/SUIBE-Blockchain/FISCO_BCOS_Toolbox/commits?author=lekko1988" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## Docker Quickstart

This app can be run completely using `Docker` and `docker-compose`. **Using Docker is recommended, as it guarantees the application is run using compatible versions of Python and Node**.

There are three main services:

To run the development version of the app

```bash
docker-compose up flask-dev
```

To run the production version of the app

```bash
docker-compose up flask-prod
```

The list of `environment:` variables in the `docker-compose.yml` file takes precedence over any variables specified in `.env`.

To run any commands using the `Flask CLI`

```bash
docker-compose run --rm manage <<COMMAND>>
```

Therefore, to initialize a database you would run

```bash
docker-compose run --rm manage db init
docker-compose run --rm manage db migrate
docker-compose run --rm manage db upgrade
```

A docker volume `node-modules` is created to store NPM packages and is reused across the dev and prod versions of the application. For the purposes of DB testing with `sqlite`, the file `dev.db` is mounted to all containers. This volume mount should be removed from `docker-compose.yml` if a production DB server is used.

### Running locally

Run the following commands to bootstrap your environment if you are unable to run the application using Docker

```bash
cd fisco_bcos_toolbox
pip install -r requirements/dev.txt
npm install
npm start  # run the webpack dev server and flask server using concurrently
```

You will see a pretty welcome screen.

#### Database Initialization (locally)

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration

```bash
flask db init
flask db migrate
flask db upgrade
```

## Deployment

When using Docker, reasonable production defaults are set in `docker-compose.yml`

```text
FLASK_ENV=production
FLASK_DEBUG=0
```

Therefore, starting the app in "production" mode is as simple as

```bash
docker-compose up flask-prod
```

If running without Docker

```bash
export FLASK_ENV=production
export FLASK_DEBUG=0
export DATABASE_URL="<YOUR DATABASE URL>"
npm run build   # build assets with webpack
flask run       # start the flask server
```

## Shell

To open the interactive shell, run

```bash
docker-compose run --rm manage db shell
flask shell # If running locally without Docker
```

By default, you will have access to the flask `app`.

## Running Tests/Linter

To run all tests, run

```bash
docker-compose run --rm manage test
flask test # If running locally without Docker
```

To run the linter, run

```bash
docker-compose run --rm manage lint
flask lint # If running locally without Docker
```

The `lint` command will attempt to fix any linting/style errors in the code. If you only want to know if the code will pass CI and do not wish for the linter to make changes, add the `--check` argument.

## Migrations

Whenever a database migration needs to be made. Run the following commands

```bash
docker-compose run --rm manage db migrate
flask db migrate # If running locally without Docker
```

This will generate a new migration script. Then run

```bash
docker-compose run --rm manage db upgrade
flask db upgrade # If running locally without Docker
```

To apply the migration.

For a full migration command reference, run `docker-compose run --rm manage db --help`.

If you will deploy your application remotely (e.g on Heroku) you should add the `migrations` folder to version control.
You can do this after `flask db migrate` by running the following commands

```bash
git add migrations/*
git commit -m "Add migrations"
```

Make sure folder `migrations/versions` is not empty.

## Asset Management

Files placed inside the `assets` directory and its subdirectories
(excluding `js` and `css`) will be copied by webpack's
`file-loader` into the `static/build` directory. In production, the plugin
`Flask-Static-Digest` zips the webpack content and tags them with a MD5 hash.
As a result, you must use the `static_url_for` function when including static content,
as it resolves the correct file name, including the MD5 hash.
For example

```html
<link rel="shortcut icon" href="{{static_url_for('static', filename='build/img/favicon.ico') }}">
```

If all of your static files are managed this way, then their filenames will change whenever their
contents do, and you can ask Flask to tell web browsers that they
should cache all your assets forever by including the following line
in ``.env``:

```text
SEND_FILE_MAX_AGE_DEFAULT=31556926  # one year
```
