# Simulating Racially Polarized Ranked Choice Voting

Copy and adapt `run_all_models_and_print_output.py` to cycle through all four models and all five scenarios. The results will be printed as rows of values separated by &s for easy input into LaTeX tables.

In the `docs` directory, the `template_table.tex` file contains a basic template for recording these results, including a very brief overview of the models and a blank table with headers.

## Getting started

The application was built using Python 3.7.5, and all dependent packages can be installed from the `requirements.txt` file by running the following:

```
pip install -r requirements.txt
```

## Running the RCV API Server

To run the Ranked Choice Vote API server, one need only run the `app.py` script:

```
python app.py
```

## Deploying the RCV API Server

As of 11/2020, the API server is deployed on Heroku. New versions of the server are automating deployed when code is pushed to the `heroku_prod` branch.

For a quick walkthrough on how the API Server is deployed through Heroku, review this article: https://stackabuse.com/deploying-a-flask-application-to-heroku/

For first-time users of Heroku who need to set up accounts and install the Heroku CLI, review this guide: https://devcenter.heroku.com/articles/getting-started-with-python#set-up

N.B. that heroku's auto-deploy will ignore the port used in the local flask app. This needs to be taken into account when connecting to the API via external web applications.
