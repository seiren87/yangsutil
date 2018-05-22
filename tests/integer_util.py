import unittest

from yangsutil import IntegerUtil


class IntegerUtilTestCase(unittest.TestCase):

    def test_1_is_check(self):
        self.assertTrue(
            IntegerUtil.is_check(0),
            msg='normal, 0 test'
        )
        self.assertTrue(
            IntegerUtil.is_check(-1),
            msg='normal, -1 test'
        )
        self.assertTrue(
            IntegerUtil.is_check(1),
            msg='normal, 1 test'
        )
        self.assertTrue(
            IntegerUtil.is_check('0'),
            msg='normal, string 0 test'
        )
        self.assertTrue(
            IntegerUtil.is_check('1'),
            msg='normal, string 1 test'
        )
        self.assertTrue(
            IntegerUtil.is_check('-1'),
            msg='normal, string -1 test'
        )
        self.assertFalse(
            IntegerUtil.is_check('aaa'),
            msg='normal, string test'
        )

        self.assertTrue(
            IntegerUtil.is_check(0, IntegerUtil.POSITIVE),
            msg='POSITIVE, 0 test'
        )
        self.assertTrue(
            IntegerUtil.is_check(1, IntegerUtil.POSITIVE),
            msg='POSITIVE, 1 test'
        )
        self.assertFalse(
            IntegerUtil.is_check(-1, IntegerUtil.POSITIVE),
            msg='POSITIVE, -1 test'
        )

        self.assertTrue(
            IntegerUtil.is_check(0, IntegerUtil.NEGATIVE),
            msg='NEGATIVE, 0 test'
        )
        self.assertFalse(
            IntegerUtil.is_check(1, IntegerUtil.NEGATIVE),
            msg='NEGATIVE, 1 test'
        )
        self.assertTrue(
            IntegerUtil.is_check(-1, IntegerUtil.NEGATIVE),
            msg='NEGATIVE, -1 test'
        )

        self.assertFalse(
            IntegerUtil.is_check(0, IntegerUtil.POSITIVE_WITHOUT_ZERO),
            msg='POSITIVE_WITHOUT_ZERO, 0 test'
        )
        self.assertTrue(
            IntegerUtil.is_check(1, IntegerUtil.POSITIVE_WITHOUT_ZERO),
            msg='POSITIVE_WITHOUT_ZERO, 1 test'
        )
        self.assertFalse(
            IntegerUtil.is_check(-1, IntegerUtil.POSITIVE_WITHOUT_ZERO),
            msg='POSITIVE_WITHOUT_ZERO, -1 test'
        )

        self.assertFalse(
            IntegerUtil.is_check(0, IntegerUtil.NEGATIVE_WITHOUT_ZERO),
            msg='NEGATIVE_WITHOUT_ZERO, 0 test'
        )
        self.assertFalse(
            IntegerUtil.is_check(1, IntegerUtil.NEGATIVE_WITHOUT_ZERO),
            msg='NEGATIVE_WITHOUT_ZERO, 1 test'
        )
        self.assertTrue(
            IntegerUtil.is_check(-1, IntegerUtil.NEGATIVE_WITHOUT_ZERO),
            msg='NEGATIVE_WITHOUT_ZERO, -1 test'
        )
