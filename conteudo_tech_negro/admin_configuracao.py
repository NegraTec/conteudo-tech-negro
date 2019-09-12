from flask_admin import Admin, base
from flask_admin import helpers, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, login_user, logout_user
from wtforms import form, fields, validators
from werkzeug.security import check_password_hash
from flask import redirect, url_for, request

from conteudo_tech_negro import login_manager, db, app
from conteudo_tech_negro.service.user_service import UserService
from conteudo_tech_negro.store.models import Autora, Conteudo


def criar_usuaria_admin():
    UserService.criar_usuaria_admin()

# Create user loader function
@login_manager.user_loader
def load_user(usuaria_id):
    return UserService.obter_usuaria_por_id(usuaria_id)


# Define login and registration forms (for flask-login)
class LoginForm(form.Form):
    login = fields.StringField(validators=[validators.DataRequired()])
    password = fields.PasswordField(validators=[validators.DataRequired()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return UserService.obter_usuaria_por_login(self.login.data)


# Create customized model view class
class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated


# Create customized index view class that handles login & registration
class MyAdminIndexView(base.AdminIndexView):

    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login_user(user)

        if current_user.is_authenticated:
            return redirect(url_for('.index'))

        self._template_args['form'] = form

        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))


admin = Admin(app, name='Conteudo Tech Negro - Admin', index_view=MyAdminIndexView(), base_template='my_master.html')

admin.add_view(MyModelView(Autora, db.session))
admin.add_view(MyModelView(Conteudo, db.session))
