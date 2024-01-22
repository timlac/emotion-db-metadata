import unittest

from nexa_coding_interpreter.code_modification import CodeModification


class TestCodeModification(unittest.TestCase):

    def test_fix_underscore_in_mix_proportions(self):
        filename = "A326_mix_fea_sad_70_30"

        cm = CodeModification(filename)

        self.assertEqual(cm.filename, "A326_mix_fea_sad_7030")


