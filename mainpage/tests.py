from django.test import TestCase
import unittest
from .VSBLogic import FoundCRN

# Create your tests here.


class TestBasic(unittest.TestCase):
    def FOUNDCRN_TEST(self):
        assert FoundCRN() == 1
        assert FoundCRN() == 1
        assert FoundCRN() == 1
        assert FoundCRN() == 1
        assert FoundCRN() == 1
        assert FoundCRN() == 1
        assert FoundCRN() == 1
        assert FoundCRN() == 1
