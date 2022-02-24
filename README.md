# CubeSAT Satellite Dashboard

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

Make sure you have `python3`, `pip3`, `brew`, `yarn`, `node`, `npm`, and `nvm` installed

## API dependency

Map feature of this project is entirely dependent on Google and Bing map's API

Since our GitHub repo is public, to prevent accidental billing charges

Google Map API is hidden in a `.env` file and stored locally

[Getting a Google Map API key](https://developers.google.com/maps/documentation/javascript/get-api-key)

Go to the root directory of this project: `cd .../py-satellite-dashboard`

Create a hidden .env file: `touch .env`

Open .env file: `vi .env` or `open .env`

Paste this line: `REACT_APP_GOOGLE_MAP_API_KEY=<YOUR API KEY GOES HERE>`

## Installing prerequisite

Double check `Python3` and `Pip3` are installed

[Homebrew installation](https://brew.sh/)

`brew install node@14`

`brew install npm`

`brew install nvm`

## Connecting to our SQL Database

`brew install postgresql`

`pip install psycopg2`

A free SQL database was created on [elephantSQL](https://www.elephantsql.com/)

Connection Information using [DataGrip](https://www.jetbrains.com/datagrip/)
, can also work with other SQL database editor

```
Driver: PostgreSQL

Host: castor.db.elephantsql.com

User: omoglffn

Password: Ask for password

URL: jdbc:postgresql://castor.db.elephantsql.com/
```

ElephantSQL DB connection secret is hidden in a `.env` file and stored locally

Inside `/py-satellite-dashboard/.env`

Paste this line: `DB_URL=postgresql://omoglffn:<PASSWORD_GOES_HERE>@castor.db.elephantsql.com/omoglffn`

## Run Flask App

Setup `venv` virtualenv

`cd py-satellite-dashboard`

`python3 -m venv venv`

`. venv/bin/activate`

`pip install -r 'src/python/requirements.txt'`

Create a `.flaskenv` Flask config file

`touch .flaskenv`

Paste in

```
FLASK_DEBUG=1
FLASK_APP=src/python/app.py
FLASK_ENV=development
```

## Run React App

`git clone https://github.com/UCI-CubeSat/py-satellite-dashboard/`

`cd py-satellite-dashboard`

`npm install`

make sure Python requirements are all installed correctly

### Using PyCharm, open project and add

`app.py` and `npm start` in `Run/Debug Configuration`

### Using Command Line Interface

`cd py-satellite-dashboard`

`flask run`

`npm start`

and Open http://localhost:3000 in browser

## To dos

Add React UI library

Add React Animation library


## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

The basic of React file structure: [React documentation](https://www.cluemediator.com/create-react-application-multiple-components)

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
