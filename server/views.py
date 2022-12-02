from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from server.app import db

views = Blueprint('views', __name__)


# Home page
@views.route('/')
def home():
    if current_user.is_authenticated:
        return render_template("index.html", current_user=current_user, page="home")
    else:
        return redirect(url_for('auth.login'))


# Example page
@login_required
@views.route('/example')
def example_page():
    return render_template("example.html", current_user=current_user, page="example")


# ──────────────────────────────────────── CODE SNIPPETS ────────────────────────────────────────
# ──────────────────── GENERAL ────────────────────
# Redirect to page                                              redirect(url_for('views.page'))
# Requires login decorator (redirects to 403 page)              @login_required
# Check if current user is authenticated                        if current_user.is_authenticated:
# Route with parameters                                         @views.route('/withparams/<param>')
#                                                               def paramroute(param):
# Cancel request with error code (in this case 403)             abort(403)

# ──────────────────── DATABASE ────────────────────
# Get all records                                               Table.query.all()
# Query a table with filter options and return first match      Table.query.filter_by( <QUERY OPTIONS> ).first()
#                                                                   <QUERY OPTIONS> id=123 name='test'
# Query a table and sort by descending id (last record first)   Table.query.order_by(Table.id.desc())
# Get a linked record from a user                               current_user.linkedtable
# Create a new record                                           new_record = Record(field=data, field2=data2)
# Update a record                                               new_record.field3 = data3
# Delete a record                                               db.session.delete(new_record)
# Add a record to the database                                  db.session.add(new_record)
# Commit changes (done after all operations are complete)       db.session.commit()

# ──────────────────── REQUESTS ────────────────────
# Route with both GET and POST methods                          @views.route('/path', methods=['GET', 'POST'])
# Check if request method is post                               if request.method == 'POST':
# Get data from form for regular inputs                         request.form.get('input name')
# Get data from form for common input names                     request.form.getlist('common input name')

# ──────────────────── FLASHING MESSAGES ────────────────────
# Flash a normal message                                        flash('Flashed message content')
# Flash a message with a category                               flash('Flashed message content', category='success')

# ──────────────────── TEMPLATE SNIPPETS (FOR USE IN .html TEMPLATE FILES) ────────────────────
# Link a static file                                            {{ url_for('static', filename='path/to/file.txt') }}

# Flashed messages without categories:
#       {% with messages = get_flashed_messages() %}
#           {% if messages %}
#               {% for message in messages %}
#                   <div class="alert mb-10" role="alert">
#                       <button class="close" data-dismiss="alert" type="button" aria-label="Close">
#                           <span aria-hidden="true">&times;</span>
#                       </button>
#                       {{ message }}
#                   </div>
#               {% endfor %}
#           {% endif %}
#       {% endwith %}

# Flashed messages with categories:
#       {% with messages = get_flashed_messages(with_categories=true) %}
#           {% if messages %}
#               {% for category, message in messages %}
#                   <div class="alert alert-{{ category }} mb-10" role="alert">
#                       <button class="close" data-dismiss="alert" type="button" aria-label="Close">
#                           <span aria-hidden="true">&times;</span>
#                       </button>
#                       {{ message }}
#                   </div>
#               {% endfor %}
#           {% endif %}
#       {% endwith %}

