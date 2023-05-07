# Introduction

This project seeks to make retrieving data from across different mastodon servers easier for the purposes of research.

# Project Structure

- Backend: A [flask](https://flask.palletsprojects.com/en/2.3.x/) application that leverages the official [mastodon api](https://docs.joinmastodon.org/api/) to get user, status and hashtag data for a given mastodon instance.
- Frontend: A [vue.js](https://vuejs.org/guide/introduction.html) app that makes it easier for a user to perform a search query and observe the results.

# Running the app
- Backend:
1. Check your terminal into the backend folder.
2. Install necessary pip packages. Run `pip install -r requirements.txt`.
3. Run your flask app by running `flask run --port <desired_port_number>`.

- Frontend:
1. Check your terminal into the frontend folder.
2. Install necessary npm packages. Run `npm i`.
3. Serve your vue app by running `npm run serve`.