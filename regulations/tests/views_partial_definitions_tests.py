from unittest import TestCase
from django.template import loader


class PartialDefinitionTests(TestCase):
    urls = 'regulation.urls'

    def test_partial_definition_with_children(self):
        t = loader.get_template('regulations/partial-definition.html')

        node = {
            'part': '102',
            'section_id': '4',
            'label_id': '202-2-a',
            'children': [{'label_id': '202-2-a-1'}]}

        context_dict = {'node': node, 'version': '2012-1223'}
        response = t.render(context_dict)
        best_viewed = 'This definition is best viewed in its original location'
        self.assertTrue(best_viewed in response)

    def test_partial_definition_no_children(self):
        t = loader.get_template('regulations/partial-definition.html')

        node = {
            'part': '102',
            'section_id': '4',
            'label_id': '202-2-a',
            'marked_up': 'This term is defined carefully'}

        context_dict = {'node': node, 'version': '2012-1223'}
        response = t.render(context_dict)
        carefully = 'This term is defined carefully'
        self.assertTrue(carefully in response)
