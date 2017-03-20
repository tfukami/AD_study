# coding: utf-8
import shelve
from datetime import datetime

from flask import Flask, request, render_template, redirect, escape, Markup

application = Flask(__name__)

DATA_FILE = 'guestbook.dat'

def save_data(name, comment, create_at):
    """save comments
    """
    # DB file open by shelve module
    database = shelve.open(DATA_FILE)
    # if there is no list make new one
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        # get data from DB
        greeting_list = database['greeting_list']
    # add comment data to the front of the list
    greeting_list.insert(0, {
        'name': name,
        'comment': comment,
        'create_at': create_at,
    })

    # renew DB
    database['greeting_list'] = greeting_list
    # close DB
    database.close()

def load_data():
    """return comment data
    """
    # open DB by shelve module
    database = shelve.open(DATA_FILE)
    # return greeting_list
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list

@application.route('/post', methods=['POST'])
def post():
    """URL for submit
    """
    # get submit data
    name = request.form.get('name')
    comment = request.form.get('comment')
    create_at = datetime.now()

    # save
    save_data(name, comment, create_at)

    return redirect('/')

@application.route('/')
def index():
    """view page by using template
    """
    greeting_list = load_data()
    return render_template('index.html', greeting_list=greeting_list)

@application.template_filter('nl2br')
def nl2br_filter(s):
    """replace \n to tr tag
    """
    return escape(s).replace('\n', Markup('<br>'))

@application.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
    """get datetime object to clear view
    """
    return dt.strftime('%Y/%m/%d %H:%M:%S')

if __name__ == '__main__':
    # exec app at 8000port of 127.0.0.1
    application.run('127.0.0.1', 8000, debug=True)
