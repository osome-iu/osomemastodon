# Introduction

This Dashboard seeks to make retrieving data from across different mastodon servers easier for the purposes of research.
The dashboard currently processing these API's and visualize them in the frontend.

- Instance - Get Mastodon Instances API
- Status - Search by keyword API
- Status - Most recent by hashtag API
- Most recent for instance API
- Status - Single status by Id API
- Accounts - Search by keyword
- Accounts - Single Account by Id
- Get Hashtag metadata
  
# Project Structure

- Backend: A [flask](https://flask.palletsprojects.com/en/2.3.x/) application that leverages the official [mastodon api](https://docs.joinmastodon.org/api/) to retrieve data and manipulate the data.
- Frontend: A [vue.js](https://vuejs.org/guide/introduction.html) app that makes it easier for a user to perform a search query and observe the results. 

# How to run the project.
In order to run the project, please clone to project to your local machine. Then separately run the frontend and backend of the project as below.  

- Frontend:
1. Check your terminal into the frontend folder.
2. Install necessary npm packages. Run `npm i`.
3. Serve your vue app by running `npm run serve`.

- Backend:
1. Check your terminal into the backend folder.
2. Install necessary pip packages. Run `pip install -r requirements.txt`.
3. Run your flask app by running `flask run --port <desired_port_number>`.

## Note
- You can access the API documentation [here](https://github.com/osome-iu/osomemastodon/wiki)
- The Mastodon dashboard is live on [osome mastodon](https://osome.iu.edu/tools/mastodon)

# Docker

## Build
The Docker build sets `VUE_PUBLIC_PATH=/` so the built frontend assets are served at the container root (`/`) instead of `/tools/mastodon`.

If it needs to be served at `/tools/mastodon` in production, build the frontend with `VUE_PUBLIC_PATH=/tools/mastodon` and make sure the entry point routes that prefix to the container (e.g., Kubernetes Ingress, Service type `LoadBalancer`, gateway/service mesh, or a reverse proxy). This is typically configured in the Helm chart (set the image/tag to one built with the correct public path, and configure the path prefix on whatever routes external traffic).

```bash
docker build -t osomemastodon .
```

## Run (with config mounted)
The container expects `backend/mastodon.config` to be provided at runtime (for Kubernetes, this is typically a ConfigMap mounted at `/app/backend/mastodon.config`).

```bash
docker run --rm -p 8323:8323 \
  -v "$(pwd)/backend/mastodon.config:/app/backend/mastodon.config:ro" \
  osomemastodon
```

Then open `http://localhost:8323/`.
