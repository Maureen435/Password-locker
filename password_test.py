import unittest
from password import User,Credential
 
 class TestUser(unittest,TestCase):
     def setUp(self):
         self.new_user = user("Memzo","3245")
     def tearDown(self):
         User.user_list = []
         def test_init(self):
             self.assertEqual(self.new_user.name, "Memzo")
             self.assertEqual(self.new_user.user_password, "3245")
         def test_save_user(self):
             self.new_user.save_user()
             self.assertEqual(len(User.uset_list),1)
    