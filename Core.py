from flask import send_from_directory, Blueprint

from Helpers.CtrlHelper import Succ, Fail
from Db.Db import Db

corebp = Blueprint('profile', __name__)


@corebp.route('/', defaults={'path': ''})
@corebp.route('/<path:path>')
def index(path):
    if path == '' or path == '/':
        return send_from_directory('ui', 'index.html')
    else:
        return send_from_directory('ui', path)


@corebp.route('/api/skills')
def skills():
    try:
        cmd = "select * from rbtlong.skills"
        return Db.Main().rows(Succ, cmd, ())

    except ConnectionError as dberr:
        print(f"[/api/skills] Failed: {dberr}")
        return Fail('db')


@corebp.route('/api/projects')
def projects():
    try:
        cmd = "select * from rbtlong.projects"
        return Db.Main().rows(Succ, cmd, ())

    except ConnectionError as dberr:
        print(f"[/api/projects] Failed: {dberr}")
        return Fail('db')

@corebp.route('/api/imgs/projects')
def imgs_tag():
    try:
        cmd = "select * from rbtlong.imgs where tags like '%projects%'"
        return Db.Main().rows(Succ, cmd, ())

    except ConnectionError as dberr:
        print(f"[/api/imgs/name_pronunciation] Failed: {dberr}")
        return Fail('db')
