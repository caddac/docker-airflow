import os
from glob import glob

import yaml
from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint
from flask_admin import BaseView, expose


def get_data(file_path):
    with open(file_path) as file:
        config = yaml.load(file)

        return {
            'image': config.get('services').get('webserver').get('image'),
            'command': config.get('services').get('webserver').get('command'),
            'volumes': config.get('services').get('webserver').get('volumes'),
        }
    return {}

class TestView(BaseView):

    @expose('/')
    def test(self):
        print(os.getcwd())
        PATH = 'dags/in'
        file_paths = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.yml'))]
        print(file_paths)
        data = [get_data(fp) for fp in file_paths]
        print(data)
        # data = [{'column_a': 'Content',
        #          'column_b': '123',
        #          'column_c': 'Test'}]

        return self.render("test_plugin/test.html", data=data)


admin_view_ = TestView(category="Test Plugin", name="Test View")

blue_print_ = Blueprint("test_plugin",
                        __name__,
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='/static/test_plugin')
