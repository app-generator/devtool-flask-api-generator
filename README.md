# Flask API Generator

The tool is able to generate APIs using Flask, Flask-RestX stack with a minimum effort. For newcomers, Flask is a leading backend framework used to code from simple websites and APIs to complex eCommerce solutions.

- 👉 Free [support](https://appseed.us/support/) via Email and [Discord](https://discord.gg/fZC6hup)
- 👉 More [Developer Tools](https://appseed.us/developer-tools/) - provided by AppSeed

<br />

## Video Presentation

https://user-images.githubusercontent.com/51070104/194278839-8ea8e6e1-5ce9-4c53-9b8a-442a208c46d3.mp4

<br />

## How It Works

This module helps to generate secure APIs using `Flask-restX` via a simple workflow: 

- Edit/add your model in `apps/models.py`
- Migrate the database:

```bash
$ flask db init     # this should be executed only once
$ flask db migrate  # Generates the SQL 
$ flask db upgrade  # Apply changes 
```

- Update Configuration:
  - `apps/config .py`, section `API_GENERATOR` 
- Generate the API code:
  - `$ flask gen_api`        # the new code is saved in `apps/api`
- Access the API in the browser:
  - `/api/MODEL_NAME/`

The API is secured using the JWT tocken provided by `/login/jwt/` request (username & password should be provided).  

- GET requests are public (GET all, get Item)
- Mutating requests are protected by token generated based on the user credentials (`username`, `pass`). 

> Two POSTMAN Collections are provided in the `media` directory: 

- [Books API](./media/api-books.postman_collection) - that uses PORT **5000* for the api
- [Books API 2](./media/api-books-docker.postman_collection) - that uses PORT **5085* for the api (default port in Docker)

In case both port are unusable in your environment, feel free to edit the files before POSTMAN import.

<br />

--- 
**Flask API Generator** - Developer tool provided by [AppSeed](https://appseed.us)
