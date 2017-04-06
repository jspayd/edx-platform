"""
Assert that problems are rendered correctly
"""
import unittest

from edxmako.shortcuts import render_to_string


class ResetButtonTestCase(unittest.TestCase):
    """
    Assert that the Reset button is properly displayed
    """

    def setUp(self):
        """
        Initialize context and expectations
        """
        self.context = {
            'answer_available': True,
            'answer_notification_type': None,
            'answer_notification_message': '',
            'attempts_allowed': 2,
            'attempts_used': 0,
            'check_button': u'Submit',
            'demand_hint_possible': False,
            'end_time_to_display': None,
            'id': u'1',
            'problem': {
                'html': '',
                'name': u'Checkboxes',
                'weight': None,
            },
            'problem_is_timed': False,
            'reset_button': True,
            'save_button': True,
            'save_message': 'Saving...',
            'seconds_before_warning': 5,
            'short_id': 'foobar',
            'should_enable_submit_button': True,
            'start_time': None,
            'submit_button': 'Submit',
            'submit_button_submitting': 'Submitting',
            'total_seconds_left': 1,
        }
        self.reset_button_html = '<button type="button" class="reset'

    def _render(self, reset_button):
        """
        Render the problem template
        """
        self.context['reset_button'] = reset_button
        html = render_to_string('problem.html', self.context)
        return html

    def test_reset_button_shows(self):
        """
        Assert that the reset button is shown
        """
        html = self._render(reset_button=True)
        self.assertIn(self.reset_button_html, html)

    def test_reset_button_hides(self):
        """
        Assert that the reset button is hidden
        """
        html = self._render(reset_button=False)
        self.assertNotIn(self.reset_button_html, html)
