from app import app
from argparse import ArgumentParser
from models.database import init_db
from flask import url_for

if __name__ == '__main__':
    print(" * Parsing command line arguments.")
    parser = ArgumentParser()
    parser.add_argument('--config', metavar='File', dest='config_file', default='config/setup.cfg', help='File used for getting application configuration')
    args = parser.parse_args()
    print(" * Configuring SmartVet web server.")
    # Setup Flask-Security
    with app.app_context():
        app.run(host='0.0.0.0', port=9292)


