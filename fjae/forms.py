from flask.ext.wtf import Form, SelectField


class VehicleForm(Form):
    make = SelectField(u'', choices=())
    model = SelectField(u'', choices=())
