__author__ = 'Robert Donovan'


from setuptools import setup, find_packages

setup (
    name             = "App",
    version          = "0.1",
    description      = "Flask Python App.",
    packages         = find_packages(),
    install_requires = ["service_identity>=14.0.0",
                        "Flask>=0.10.1",
                        "Flask-Bcrypt>=0.6.0",
                        "Flask-HTTPAuth>=2.2.1",
                        "Flask-RESTful>=0.2.12",
                        "Flask-SQLAlchemy>=1.0",
                        "Flask-WTF>=0.10.0",
                        "Jinja2>=2.7.3",
                        "MarkupSafe>=0.23",
                        "SQLAlchemy>=0.9.7",
                        "SQLAlchemy-Utils>=0.26.9",
                        "WTForms>=2.0.1",
                        "WTForms-Alchemy>=0.12.8",
                        "WTForms-Components>=0.9.5",
                        "Werkzeug>=0.9.6",
                        "aniso8601>=0.83",
                        "decorator>=3.4.0",
                        "infinity>=1.3",
                        "intervals>=0.3.1",
                        "itsdangerous>=0.24",
                        "marshmallow>=0.7.0",
                        "py-bcrypt>=0.4",
                        "pytz>=2014.4",
                        "six>=1.7.3",
                        "validators>=0.6.0",
                        "wsgiref>=0.1.2"





                        ],
    entry_points     = {'console_scripts':
                        ['run-the-app = deployme:main']}
)
