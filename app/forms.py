from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from .models import User

#Validacion personalizada
def my_validator(form, field):
    if field.data == 'Julian':
        raise validators.ValidationError('El usuario no se puede llamar Julian')

class LoginForm(Form):
    username = StringField('UserName', [
        validators.length(min=4, max=50, message='Username fuera de rango')
    ])
    password = PasswordField('Password', [
        validators.Required()
    ])

class RegisterForm(Form):
    username = StringField('UserName', [
        validators.length(min=4, max=50, message='Username fuera de rango'),
        my_validator
    ])
    email = EmailField('Correo Electronico', [
        validators.length(min=6, max=100), 
        validators.Required('Email requerido'),
        validators.Email(message='Ingese un Email Valido')
    ])
    password = PasswordField('Password', [
        validators.Required('Password requerido'),
        validators.EqualTo('confirm_password', 'La contraseña no coincide')
    ])
    confirm_password = PasswordField('Confirm Password')
    accept = BooleanField(validators=[DataRequired(), ])

    #valida si existe usuario
    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('El usuario ya existe')

    #valida si existe email
    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('El email ya existe')

    #Manera de validar sobre escribiendo validate
    def validate(self):
        #llama a funciones ya registradas de los campos
        if not Form.validate(self):
            return False
        
        if len(self.password.data) < 3:
            self.password.errors.append('El password es muy corto')
            return False
        return True
    
class TaskForm(Form):
    title = StringField('Titulo', [
        validators.length(min=4, max=50, message='Titulo fuera de rango'),
        validators.DataRequired(message='El titulo es requerido')
    ])
    description = TextAreaField('Descripcion', [
        validators.DataRequired(message='La descripcion es requerida')
    ], render_kw={'rows' : 5})