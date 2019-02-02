from airflow.plugins_manager import AirflowPlugin

from plugins.test_plugin import admin_view_, blue_print_


class AirflowTestPlugin(AirflowPlugin):
    name             = "test_plugin"
    admin_views      = [admin_view_]
    flask_blueprints = [blue_print_]