from flask import Flask

from fjae import views


def create_app():
    app = Flask(
        __name__,
        template_folder='templates',
        static_folder='assets',
    )
    app.config.from_object('fjae.settings')
    app.debug = True
    app.add_url_rule(
        '/', view_func=views.select_vehicle, methods=['GET', 'POST'])
    app.add_url_rule(
        '/models/<int:make_id>/', view_func=views.ModelsAPI.as_view('models_api'),
        methods=['GET'])

    return app


def run_dev_server():
    app = create_app()
    app.run()
