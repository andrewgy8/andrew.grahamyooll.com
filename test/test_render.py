import unittest
import bakesite

class RenderTest(unittest.TestCase):
    """Tests for render() function."""

    def test_oneline_template(self):
        tpl = 'foo {{ key1 }} baz {{ key2 }}'
        out = bakesite.render(tpl, key1='bar', key2='qux')
        self.assertEqual(out, 'foo bar baz qux')

    def test_multiline_template(self):
        tpl = 'foo {{ key1 }}\nbaz {{ key1 }}'
        out = bakesite.render(tpl, key1='bar')
        self.assertEqual(out, 'foo bar\nbaz bar')

    def test_repeated_key(self):
        tpl = 'foo {{ key1 }} baz {{ key1 }}'
        out = bakesite.render(tpl, key1='bar')
        self.assertEqual(out, 'foo bar baz bar')

    def test_multiline_placeholder(self):
        tpl = 'foo {{\nkey1\n}} baz {{\nkey2\n}}'
        out = bakesite.render(tpl, key1='bar', key2='qux')
        self.assertEqual(out, 'foo bar baz qux')
