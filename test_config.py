"""
    This is a pytest module that contains simple assert
    statement to tests Flask_playground's configuration.
"""
from flask import current_app, has_app_context
import pytest

# The entry needs to be changed to the path of the
# flask_playground folder on your machine
db_path = ("sqlite:///C:\\path\\to_folder\\"
           "flask_playground\\data-test.sqlite")


@pytest.mark.usefixtures('app_session_for_module')
class TestFlaskApp:

    def test_flask_app_exists(self):
        assert current_app is not None

    def test_flask_app_has_app_context(self):
        assert has_app_context() is True

    def test_flask_app_name_is_app(self):
        assert current_app.name == 'app'


class TestTestConfig:

    def test_flask_env_is_testing(self):
        assert current_app.config['ENV'] == 'testing'

    def test_test_config_has_sql_db_uri(self):
        assert current_app.config['SQLALCHEMY_DATABASE_URI'] == db_path

    def test_test_config_has_testing(self):
        assert current_app.config['TESTING']

    def test_test_config_has_wtf_csrf_is_false(self):
        assert current_app.config['WTF_CSRF_ENABLED'] is False


class TestFlaskConfig:

    def test_flask_config_has_secret_key(self):
        assert current_app.config['SECRET_KEY']

    def test_flask_config_secret_key_is_string(self):
        assert isinstance(current_app.config['SECRET_KEY'], str)

    def test_flask_config_has_server_name(self):
        assert current_app.config['SERVER_NAME']

    def test_flask_config_server_name_is_string(self):
        assert isinstance(current_app.config['SERVER_NAME'], str)

    def test_flask_config_has_mail_server(self):
        assert current_app.config['MAIL_SERVER']

    def test_flask_config_mail_server_is_string(self):
        assert isinstance(current_app.config['MAIL_SERVER'], str)

    def test_flask_config_has_mail_port(self):
        assert current_app.config['MAIL_PORT']

    def test_flask_config_mail_port_is_string(self):
        assert isinstance(current_app.config['MAIL_PORT'], str)

    def test_flask_config_has_mail_username(self):
        assert current_app.config['MAIL_USERNAME']

    def test_flask_config_mail_username_is_string(self):
        assert isinstance(current_app.config['MAIL_USERNAME'], str)

    def test_flask_config_has_mail_password(self):
        assert current_app.config['MAIL_PASSWORD']

    def test_flask_config_has_mail_use_tls(self):
        assert current_app.config['MAIL_USE_TLS']

    def test_flask_config_has_mail_subject_prefix(self):
        assert current_app.config['MAIL_SUBJECT_PREFIX']

    def test_flask_config_has_mail_sender(self):
        assert current_app.config['MAIL_SENDER']

    def test_flask_config_has_admin(self):
        assert current_app.config['ILLUMINATE_ADMIN']

    def test_flask_config_has_not_sql_track_modifications(self):
        assert current_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] is False
