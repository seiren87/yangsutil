import os
import shutil
import unittest

from yangsutil import FileUtil


class FileUtilTestCase(unittest.TestCase):
    def setUp(self):
        self.DIRECTORY = 'file'
        self.FILE_NAME = 'test.log'
        self.CONTENTS = 'I Love Jellicle'

    def test_1_file_read_write(self):
        file_path = os.path.join(self.DIRECTORY, self.FILE_NAME)

        FileUtil.save_file(
            file_path=file_path,
            string_contents=self.CONTENTS
        )

        self.assertTrue(
            os.path.isfile(file_path),
            msg='file generate'
        )

        self.assertEqual(
            FileUtil.read_file(file_path),
            'I Love Jellicle',
            msg='file read'
        )

    def test_2_json_read_write(self):
        file_path = os.path.join(self.DIRECTORY, 'test.json')

        self.assertIsNone(
            FileUtil.read_json_file(file_path),
            msg='json file return None'
        )

        FileUtil.save_json_file(
            file_path=file_path,
            dict_contents={'a': 'b'}
        )
        self.assertDictEqual(
            FileUtil.read_json_file(file_path),
            {'a': 'b'},
            msg='json file contents'
        )

    def test_3_save_csv_file(self):
        file_path = os.path.join(self.DIRECTORY, 'test.csv')

        self.assertTrue(
            FileUtil.save_csv_file(
                file_path=file_path,
                dict_list=[
                    {'a': 1, 'b': 'asdf'},
                    {'a': 2, 'b': 'qwer'},
                ]),
            msg="csv save"
        )

    def test_4_read_yml_file(self):
        file_path = '%s/test.yml' % self.DIRECTORY

        FileUtil.save_file(
            file_path=file_path,
            string_contents="""a list:
- 1
- 42
- 3.141
- 1337
- help
a string: bla
another dict:
  foo: bar
  key: value
  the answer: 42
"""
        )

        yml_data = FileUtil.read_yml_file(file_path=file_path)

        self.assertDictEqual(
            yml_data,
            {
                'a list': [1, 42, 3.141, 1337, 'help'],
                'a string': 'bla',
                'another dict': {
                    'foo': 'bar',
                    'key': 'value',
                    'the answer': 42
                }
            },
            msg="yaml read"
        )

    def tearDown(self):
        if os.path.isdir(self.DIRECTORY) is True:
            shutil.rmtree(self.DIRECTORY)
