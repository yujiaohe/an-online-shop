from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, FloatField, URLField
from wtforms.validators import DataRequired, Optional, Email, URL, ValidationError


class RegisterForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("SIGN ME UP!")


class LoginForm(FlaskForm):
    email = EmailField("Email:", validators=[Email()])
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField("LOGIN!")


class ProductForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    price = FloatField("Price: ", validators=[DataRequired()])
    img_url = URLField("Image_url: ", validators=[URL()])
    submit = SubmitField("Add")


# class AtLeastOneEdited():
#     def __call__(self, form, field):
#         fields_edited = 0
#         for form_field in form:
#             print(form_field.name, form_field.data)
#             if form_field.name not in ('submit', 'csrf_token') and form_field.data:
#                 fields_edited += 1
#         print(f"{field.name}: {fields_edited}")
#         if fields_edited == 0:
#             raise ValidationError('At least one field must be edited.')


class ModifyProdForm(FlaskForm):
    def __init__(self, d_name, d_price, d_img_url):
        super().__init__()
        self.name.render_kw = {"placeholder": d_name}
        self.price.render_kw = {"placeholder": d_price}
        self.img_url.render_kw = {"placeholder": d_img_url}

    name = StringField("Name: ", validators=[Optional()])
    price = FloatField("Price: ", validators=[Optional()])
    img_url = URLField("Image_url: ", validators=[Optional()])
    submit = SubmitField("Modify")
