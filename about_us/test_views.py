from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import AboutUs

class TestAboutUsViews(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about = AboutUs(title="About us title", content="About content")
        self.about.save()

    def test_render_about_me_page_with_collaboration_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse(
            'about-us'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About us title", response.content)
        self.assertIn(b"About content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)
        
    def test_successful_collaboration_message_submission(self):
        """Test for posting a collaboration message on the about us page"""
        post_data = {
            'name': 'Name',
            'email': 'test@test.com',
            'message': 'Hello!'
        }
        response = self.client.post(reverse(
            'about-us'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )