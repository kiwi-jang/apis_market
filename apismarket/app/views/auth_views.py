from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import UserCreateForm, UserLoginForm
from werkzeug.utils import redirect
from app import db

@bp.route('/login/', methods=('get', 'POST'))
def login():
  form = UserLoginForm()
  if request.method == 'POST' and form.validate_on_submit():
    error = None
    user = User.query.filter_by(username=form.username.data).first()
    if not user:
      error = "존재하지 않는 사용자입니다."
    elif not check_password_hash(user.password, form.password.data):
      error = "비밀번호가 올바르지 않습니다."
    if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form)    
