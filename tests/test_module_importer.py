from unittest import TestCase
import bespoke


class TestImport(TestCase):
    def setUp(self):
        self.module_path = '/Users/philae/Library/Python/2.7/lib/python/site-packages/enum/__init__.py'

        self.module_name = 'IntEnum'

    def test_correct_import(self):
        foo = bespoke.module_importer.ModuleImporter(
            MODULE_NAME=self.module_name, MODULE_PATH=self.module_path).module
        print(foo)
