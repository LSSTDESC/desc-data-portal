from flask import Flask
import json
from jinja_markdown import MarkdownExtension

from portal.database import Database

__author__ = 'Globus Team <info@globus.org>'

app = Flask(__name__)
app.config.from_pyfile('portal.conf')

app.jinja_env.add_extension('jinja_markdown.MarkdownExtension')

database = Database(app)

with open(app.config['DATASETS']) as f:
    datasets = json.load(f)

import portal.views
