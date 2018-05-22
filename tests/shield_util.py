import unittest

from yangsutil import ShieldUtil


class ShieldUtilTestCase(unittest.TestCase):
    def setUp(self):
        self.PLAIN_TEXT = ' i!! tem 1234## test.. T//*&^%$#'
        self.KEY = '1234567890123456'
        self.IV = '1234567890123456'

    def test_1_encrypt_decrypt_test(self):
        encrypt_text = ShieldUtil.encrypt_aes(self.IV, self.KEY, self.PLAIN_TEXT)

        self.assertEqual(
            encrypt_text,
            'VTECxkj29rYc0na0AdaClaYhY3MqFX0uW1g4pxv539s=',
            msg='encrypt est'
        )

        self.assertEqual(
            ShieldUtil.decrypt_aes(self.IV, self.KEY, encrypt_text),
            self.PLAIN_TEXT,
            msg='decrypt test'
        )

    def test_2_random_encrypt_decrypt_test(self):
        encrypt_text = ShieldUtil.random_encrypt_aes(self.KEY, self.PLAIN_TEXT)

        self.assertEqual(
            ShieldUtil.random_decrypt_aes(self.KEY, encrypt_text),
            self.PLAIN_TEXT,
            msg='Encrypt Decrypt Test'
        )

    def test_3_hash_test(self):
        self.assertEqual(
            ShieldUtil.hash(self.PLAIN_TEXT, ShieldUtil.SHA224),
            '184c9b937d537faeb4fd4e1d52dce08cd39bbd6b3bbc386a290fb21f',
            msg='sha3_224 test'
        )

        self.assertEqual(
            ShieldUtil.hash(self.PLAIN_TEXT, ShieldUtil.SHA256),
            'db546b0a2c6dbacf0de00b8aad114b91f2b83d194f1ed06338ab75d79bd56899',
            msg='sha3_256 test'
        )
        self.assertEqual(
            ShieldUtil.hash(self.PLAIN_TEXT, ShieldUtil.SHA384),
            'afe1a571b1498ac4462d5bf31d028ea3439200f65b7f2a4daaeec4c149c2e206225136e70bcedda71112fd83fd3e8dc3',
            msg='sha3_384 test'
        )
        self.assertEqual(
            ShieldUtil.hash(self.PLAIN_TEXT, ShieldUtil.SHA512),
            '024104663ff3cf05b0c7dfc879b87beab943b002f12d17f0cbc709c81d0bc42fcaa2d6471ea6a7586f309e9c0f0d180a9db091369'
            'f84189f011c2b731bf9a8ba',
            msg='sha3_512 test'
        )
