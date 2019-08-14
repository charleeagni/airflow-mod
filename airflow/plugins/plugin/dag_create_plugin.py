import os
from airflow import configuration as conf
from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint
from flask_admin.base import MenuLink
from flask_appbuilder.security.manager import AUTH_DB
from flask_admin import BaseView, expose
from flask_appbuilder import BaseView as AppBuilderBaseView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from flask_appbuilder import SimpleFormView, ModelView
from flask_babel import lazy_gettext as _

from airflow.utils.db import create_session, provide_session
# from . import appbuilder, db
from airflow.models.base import Base, ID_LEN
from sqlalchemy import Column, Integer, String, Text, Index, Boolean
from airflow.models.costum_model_2 import someDataBase

from jinja2 import Template

class TestView(BaseView):
    @expose('/')
    def test(self):
        # in this example, put your test_plugin/test.html template at airflow/plugins/templates/test_plugin/test.html
        return self.render("test.html", content="Hello galaxy!")
v = TestView(name='av new', category='lol')

bp = Blueprint(
    "test_plugin", __name__,
    template_folder='templates', # registers airflow/plugins/templates as a Jinja template folder
    static_folder='static',
    static_url_path='/static/test_plugin')

ml = MenuLink(
    category='Test Plugin',
    name='Test Menu Link',
    url='https://airflow.apache.org/')

# Creating a flask appbuilder BaseView
# AppBuilderBaseView
class TestAppBuilderBaseView(ModelView):
    datamodel = SQLAInterface(someDataBase)
    template_folder = '/root/miniconda/lib/python3.7/site-packages/airflow/www_rbac/templates/airflow/'
    search_columns = ['dag_name']
    show_fieldsets = [
        (
            'Summary',
            {'fields': ['dag_name', 'delay']}
        )
    ]

    def post_add(self, arg):
        print("added", arg.dag_name)
        self.render_dag(arg.dag_name, {"time": arg.delay} )
        return

    def render_dag(self,name, params):
        home_dir = "/root/"
        temp = open(home_dir + "/airflow/dag_templates/template-simple.py", "r").read()
        template = Template(temp)
        with open(home_dir + "/airflow/dags/" + name + ".py", "w") as p:
            rendered = template.render(name=name, time= params['time'])
            p.writelines(rendered)


    # @expose("/asdf")
    # def list(self):
    #     # with create_session() as session:
    #     #     usntr = User(username='uniku', email='chandy@gmail.com')
    #     #     session.add(usntr)
    #     #     session.commit()
    #     print('lol')
    #     return self.render_template("dags.html", content="Hello galaxy!")




v_appbuilder_view = TestAppBuilderBaseView()
v_appbuilder_package = {"name": "Test View",
                        "category": "Test Plugin",
                        "endpoint" : "plugin",
                        "view": v_appbuilder_view}

# Creating a flask appbuilder Menu Item
appbuilder_mitem = {"name": "Google",
                    "category": "Search",
                    "category_icon": "fa-th",
                    "href": "https://www.google.com"}

# Defining the plugin class
class AirflowTestPlugin(AirflowPlugin):
    name = "test_plugin"
    # operators = [PluginOperator]
    # sensors = [PluginSensorOperator]
    # hooks = [PluginHook]
    # executors = [PluginExecutor]
    # macros = [plugin_macro]
    admin_views = [v]
    flask_blueprints = [bp]
    menu_links = [ml]
    appbuilder_views = [v_appbuilder_package]
    appbuilder_menu_items = [appbuilder_mitem]
    # global_operator_extra_links = [S3LogLink(),]
