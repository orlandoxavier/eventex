from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Orlando Xavier', cpf='12345678901',
                    email='cadastros@orlandoxavier.net', phone='83-99619-8699')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'eventex@orlandoxavier.net'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['eventex@orlandoxavier.net', 'cadastros@orlandoxavier.net']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Orlando Xavier',
            '12345678901',
            'cadastros@orlandoxavier.net',
            '83-99619-8699',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)