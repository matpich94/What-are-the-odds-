from wtforms import Form, FloatField, validators, StringField

class InputForm(Form):
    path_millenium_falcon = StringField('Indicate the path to the millenium-falcon.json file', [validators.Length(min=1, max=10000)])
    path_empire = StringField('Indicate the path to the empire.json file', [validators.Length(min=1, max=10000)])