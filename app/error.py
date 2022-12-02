from flask import render_template
from flask_login import current_user


# 403 - Unauthorised error page
def error403(e):
    return render_template('403.html', current_user=current_user), 403


# 404 - Not found error page
def error404(e):
    return render_template('404.html', current_user=current_user), 404


# 500 - Server error error page
def error500(e):
    return render_template('500.html', current_user=current_user), 500
