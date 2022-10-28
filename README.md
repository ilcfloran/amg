# Dev-ops interview

In this task you are given two projects - a frontend and a backend.

The backend is a simple python REST API build using [FastAPI](https://fastapi.tiangolo.com/).
The frontend is a simple [Next.js](https://nextjs.org/) application that connects to the backend API and provides a UI to it.

Our API implements the familiar foobar problem - given a number `n`, return `foobar` is divisible by either 3 and 5, `foo` if divisible by 3, `bar` if divisible by 5, and `n` otherwise.

## Getting Started

Let's start by creating local instances of the two servers.

### Backend

Start by creating a python virtual environment:

```bash
python3 -m venv venv
```

and activate it:

```bash
source venv/bin/activate
```

You can now install the project and its dependencies. We use [poetry](https://python-poetry.org/) as our package management tool so you can install the project by running:

```bash
pip install poetry
cd backend
poetry install
```

You can now run the server by running:

```bash
uvicorn backend.app:app --host 0.0.0.0 --port 8000
```

You can verify that everything works ok by visiting [http://localhost:8000/docs](http://localhost:8000/docs) in your browser. You should see something like the following:
![Backend API](./screenshots/fastpi.png)

Feel free to explore the API and try out the `foobar` endpoint.

The backend also includes a simple test suite. You can run it by running:

```bash
pytest
```

### Frontend

Start by installing the project dependencies:

```bash
cd frontend
npm install
# or
yarn install
```

You can now run the development server:

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You should see something like the following:
![Frontend](./screenshots/nextjs.png)

You can make a build of the project by running:

```bash
npm run build
# or
yarn build
```

Alright ready to go!

## Tasks

We do not expect you will necessarily complete all the tasks! How you complete these tasks is entirely up to you.

1. Create a git repository and push the frontend/backend projects to it. Any code/config changes you make should be committed to this repository.
2. Create a Dockerfile for each of the backend and frontend projects. The Dockerfile should be able to build a production ready image for each project.
3. In the root folder of the project create configuration that will allow you to run the backend and frontend servers. You can use any tool you like, but we recommend [docker-compose](https://docs.docker.com/compose/). Feel free to choose differently though.

Note: The frontend server connects to the backend server by default on `http://localhost:8000`. You can change this by setting the `NEXT_PUBLIC_API_URL` environment variable.

4. Create a CI pipeline that will build and test the backend project. You can use Github, Gitlab or any other CI tool you like.

For every step document the steps a senior developer would need to follow to run your solution. Add that documentation in `/docs` folder and include it in the git repository.

Good luck!
