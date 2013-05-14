"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.utils import unittest
from django.test import TestCase
from models import Author

class AuthorTestCase(TestCase):

	def setup(self):
		pass

	def tearDown(self):
		pass


	def test_author_sum(self):
		author = Author.objects.create(first_name="lala",last_name="lolo",email="teste@test.com")
		soma = author.soma()
		self.assertEqual(soma,4)

	def test_author_sum1(self):
		author = Author.objects.create(first_name="lala",last_name="lolo",email="teste@test.com")
		soma = author.soma()
		self.assertEqual(soma,3)

	def test_authot_sum2(self):
		"""
    	An Author know how sum two numbers
    	# Create an Author
    	>>> author = Author.objects.create(first_name="lala",last_name="lolo",email="teste@test.com")

	    #Make sum
    	>>> author.soma()
    	4
    	"""


