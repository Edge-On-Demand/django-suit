import django
try:
    # Django 1.9+
    django.setup()
except Exception:
    pass

from django.test.runner import DiscoverRunner as DjangoTestSuiteRunner

from suit.tests.templatetags.suit_menu import SuitMenuTestCase, \
    SuitMenuAdminRootURLTestCase, SuitMenuAdminI18NURLTestCase, \
    SuitMenuAdminCustomURLTestCase
from suit.tests.templatetags.suit_tags import SuitTagsTestCase
from suit.tests.templatetags.suit_list import SuitListTestCase
from suit.tests.templates.form_tabs import FormTabsTestCase
from suit.tests.config import ConfigTestCase, ConfigWithModelsTestCase
from suit.tests.widgets import WidgetsTestCase
from suit.tests.utils import UtilsTestCase



class NoDbTestRunner(DjangoTestSuiteRunner):
    """A test suite runner that does not set up and tear down a database."""

    def setup_databases(self):
        """Overrides DjangoTestSuiteRunner"""
        pass

    def teardown_databases(self, *args):
        """Overrides DjangoTestSuiteRunner"""
        pass


class SuitTestRunner(DjangoTestSuiteRunner):
    pass
