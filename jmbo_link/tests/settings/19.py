import os


xDATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "jmbo",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "skeleton.db", # Or path to database file if using sqlite3.
        "USER": "skeleton", # Not used with sqlite3.
        "PASSWORD": "skeleton", # Not used with sqlite3.
        "HOST": "", # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "", # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS = (
    "link",
    "jmbo",
    "jmbo_link",
    "photologue",
    "category",
    "ckeditor",
    "django_comments",
    "likes",
    "secretballot",
    "pagination",
    "preferences",
    "ultracache",
    "sites_groups",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "layers",
)

ROOT_URLCONF = "jmbo_link.tests.urls"

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware"
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.tz",
    "django.template.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.realpath(os.path.dirname(__file__)) + "/../templates/",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": TEMPLATE_CONTEXT_PROCESSORS,
        },
    },
]

SITE_ID = 1

STATIC_URL = "/static/"

SECRET_KEY = "SECRET_KEY"

CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'
