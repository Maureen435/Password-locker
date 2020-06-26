import unittest
from password import User,Credential
 
class TestUser(unittest.TestCase):
     def setUp(self):
         self.new_user = user("Memzo","3245")
     def tearDown(self):
         User.user_list = []
         def test_init(self):
             self.assertEqual(self.new_user.name, "Memzo")
             self.assertEqual(self.new_user.user_password, "3245")
         def test_save_user(self):
             self.new_user.save_user()
             self.assertEqual(len(User.user_list),1)
         def test_save_multiple_user(self):
             self.name_user.save_user()
             test_user = user("Morin", "1234")
             test_user.save_user()
             self.assertEqual(len(User.user_list), 2)
         def test_delete_user(self):
             self.new_user.save_user()
             test_user = user("Morin", "1234")
             test_user.save_user()

             self.new_user.delete_user()
             self.assertEqual(len(User.user_list), 1)
    
class TestCredential(unittest.TestCase):
         def setUp(self):
             self.new_credential = credential("facebook", "Babra", "12345")
         def tearDown(self):
             Credential.credential_list = []
         def test_init(self):
                 self.assertEqual(self.new_credential.account, "facebook")
                 self.assertEqual(self.new_credential.account_username, "Babra")
                 self.assertEqual(self.new_credential.account_password, "12345")
         def test_save_credential(self):
                 self.new_credential.save_credential()
                 self.assertEqual(len(Credential.credential_list), 1)
         def test_save_multiple_credential(self):
                 test_credential = credential("twitter", "Kemei", "0000")
                 test_credential.save_credential()
                 self.assertEqual(len(Credential.credential_list), 2)
         def test_delete_credential(self):
             self.new_credential.save_credential(self)
             test_credential = credential("twitter", "Kemei", "0000")
             test_credential.save_credential()

             self.new_credential.delete_credential()
             self.assertEqual(len(Credential.credential_list), 1)
    