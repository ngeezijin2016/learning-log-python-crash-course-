from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Entry, Topic


class TopicOwnershipTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.owner = user_model.objects.create_user(
            username='topic-owner', password='test-password'
        )
        self.other_user = user_model.objects.create_user(
            username='other-user', password='test-password'
        )
        self.topic = Topic.objects.create(text='Private topic', owner=self.owner)
        self.entry = Entry.objects.create(topic=self.topic, text='Private entry')

    def test_settings_requires_authentication(self):
        response = self.client.get(reverse('learning_logs:settings'))

        self.assertRedirects(
            response,
            f"{reverse('accounts:login')}?next={reverse('learning_logs:settings')}",
        )

    def test_other_user_cannot_view_topic(self):
        self.client.force_login(self.other_user)

        response = self.client.get(
            reverse('learning_logs:topic', args=[self.topic.id])
        )

        self.assertEqual(response.status_code, 404)

    def test_other_user_cannot_delete_topic(self):
        self.client.force_login(self.other_user)

        response = self.client.post(f'/delete_topic_ajax/{self.topic.id}/')

        self.assertEqual(response.status_code, 404)
        self.assertTrue(Topic.objects.filter(pk=self.topic.id).exists())

    def test_other_user_cannot_delete_entry(self):
        self.client.force_login(self.other_user)

        response = self.client.post(f'/delete_entry_ajax/{self.entry.id}/')

        self.assertEqual(response.status_code, 404)
        self.assertTrue(Entry.objects.filter(pk=self.entry.id).exists())
