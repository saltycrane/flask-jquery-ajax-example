import json

from flask import request, render_template, make_response
from flask.views import MethodView

from fjae.forms import VehicleForm


MAKE_LIST = (
    {'make_id': 1, 'name': 'Honda'},
    {'make_id': 2, 'name': 'Ford'},
    {'make_id': 3, 'name': 'BMW'},
)
MODEL_LIST = (
    {'model_id': 1, 'make_id': 1, 'name': 'Fit'},
    {'model_id': 2, 'make_id': 1, 'name': 'Civic'},
    {'model_id': 3, 'make_id': 1, 'name': 'Accord'},
    {'model_id': 4, 'make_id': 1, 'name': 'Pilot'},
    {'model_id': 5, 'make_id': 2, 'name': 'Mustang'},
    {'model_id': 6, 'make_id': 2, 'name': 'F-150'},
    {'model_id': 7, 'make_id': 2, 'name': 'Focus'},
    {'model_id': 8, 'make_id': 2, 'name': 'Escape'},
    {'model_id': 9, 'make_id': 3, 'name': '1-Series'},
    {'model_id': 10, 'make_id': 3, 'name': '3-Series'},
    {'model_id': 11, 'make_id': 3, 'name': '5-Series'},
    {'model_id': 12, 'make_id': 3, 'name': '7-Series'},
)


def select_vehicle():
    """
    Render a vehicle selection form and handle form submission
    """
    form = VehicleForm(request.form)
    form.make.choices = [('', '--- Select One ---')] + [
        (x['make_id'], x['name']) for x in MAKE_LIST]
    chosen_make = None
    chosen_model = None

    if request.method == 'POST':
        chosen_make = form.make.data
        chosen_model = form.model.data

    context = {
        'form': form,
        'chosen_make': chosen_make,
        'chosen_model': chosen_model,
    }
    return render_template('select_vehicle.html', **context)


class ModelsAPI(MethodView):
    def get(self, make_id):
        """
        Handle a GET request at /models/<make_id>/
        Return a list of 2-tuples (<model id>, <model name>)
        """
        data = [
            (x['model_id'], x['name']) for x in MODEL_LIST
            if x['make_id'] == make_id]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
        return response
