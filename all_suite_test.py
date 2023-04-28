import unittest

from unittest.loader import makeSuite

from test_cases.framework import Test
from test_cases.add_a_player_to_database import TestAddAPlayer
from test_cases.change_language_to_polish import TestChangeLanguage
from test_cases.clear_add_a_player_form import TestClearAddAPlayer
from test_cases.go_to_add_a_player_form import TestGoToAddAPlayerForm
from test_cases.go_to_players_list import TestGoToPlayersList
from test_cases.log_out_of_the_system import TestLogOut
from test_cases.login_to_the_system import TestLoginPage

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestAddAPlayer))
   test_suite.addTest(makeSuite(TestChangeLanguage))
   test_suite.addTest(makeSuite(TestClearAddAPlayer))
   test_suite.addTest(makeSuite(TestGoToAddAPlayerForm))
   test_suite.addTest(makeSuite(TestGoToPlayersList))
   test_suite.addTest(makeSuite(TestLogOut))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(Test))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())