# Team_87_zuri_fetch_metadata

# Backend - Fetch Meta Data

## Setting up the Backend

### Install Dependencies

1. **Python 3.10** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies make sure you are on the `Team_87_zuri_fetch_metadata` directory then run the commands below:

- **Start and activate your virtual environment**

```bash
# Mac and Linux users

python3 -m venv env
source env/bin/activate

# Windows users
> py -3 -m venv env
> env\Scripts\activate

# Windows git bash users
python3 -m venv env
source env/bin/activate
```

Run This command to install the required project dependencies e.g Django

```bash
pip install -r requirements.txt
```

## Setting up Environment variables

```bash
pip install -r requirements.txt
```

\*\* If you have ran the above command successfully without errors then you have `django-environ` installed.

Inside your `/extractMetadata/` folder

- create a `.env` file
- go to your `extractMetadata/settings.py` and copy your Django `SECRET_KEY` and past it on your `.env` file
- see example below:
- Take note not to add spaces inbetween the `=`

```bash
SECRET_KEY='django-insecure-^4joa&mspske00-oaeoa-ei28ial-eej4h1m0b-@tldx9xq4va'

```

- Next go to your `extractMetadata/settings.py` and add this lines of code:

```bash
# imports django-environ
import environ

# assign the django-environ function to a variable named env
env = environ.Env()

# read the data from the .env file
environ.Env.read_env()

# change your SECRET_KEY to read the SECRET_KEY from .env file

SECRET_KEY = env("SECRET_KEY")

```

#### Key Pip Dependencies

- [Django](https://www.djangoproject.com/) Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

### Set up the Database

```bash
python manage.py migrate
```

### Run the Server

After successfully setting up and installing the dependencies and setting up the Database start your backend Django server by running the command below from the `/Team_87_zuri_fetch_metadata/` directory.

```bash
python manage.py runserver
```

