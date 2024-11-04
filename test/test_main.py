import unittest
import makesite
import os
import shutil
import json

from test import path


class MainTest(unittest.TestCase):
    def setUp(self):
        path.move('site', 'site.backup')
        path.move('params.json', 'params.json.backup')

    def tearDown(self):
        path.move('site.backup', 'site')
        path.move('params.json.backup', 'params')

    def testsite_missing(self):
        makesite.main()

    def testsite_exists(self):
        os.mkdir('site')
        with open('site/foo.txt', 'w') as f:
            f.write('foo')

        self.assertTrue(os.path.isfile('site/foo.txt'))
        makesite.main()
        self.assertFalse(os.path.isfile('site/foo.txt'))

    def test_default_params(self):
        makesite.main()

        with open('site/blog/proin-quam/index.html') as f:
            s1 = f.read()

        with open('site/blog/rss.xml') as f:
            s2 = f.read()

        shutil.rmtree('site')

        self.assertIn('<a href="/">Home</a>', s1)
        self.assertIn('<title>Proin Quam - Lorem Ipsum</title>', s1)
        self.assertIn('Published on 2018-01-01 by <b>Admin</b>', s1)

        self.assertIn('<link>http://localhost:8000/</link>', s2)
        self.assertIn('<link>http://localhost:8000/blog/proin-quam/</link>', s2)

    def test_json_params(self):
        params = {
            'base_path': '/base',
            'subtitle': 'Foo',
            'author': 'Bar',
            'site_url': 'http://localhost/base'
        }
        with open('params.json', 'w') as f:
            json.dump(params, f)
        makesite.main()

        with open('site/blog/proin-quam/index.html') as f:
            s1 = f.read()

        with open('site/blog/rss.xml') as f:
            s2 = f.read()

        shutil.rmtree('site')

        self.assertIn('<a href="/base/">Home</a>', s1)
        self.assertIn('<title>Proin Quam - Foo</title>', s1)
        self.assertIn('Published on 2018-01-01 by <b>Bar</b>', s1)

        self.assertIn('<link>http://localhost/base/</link>', s2)
        self.assertIn('<link>http://localhost/base/blog/proin-quam/</link>', s2)
