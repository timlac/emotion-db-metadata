import unittest
from nexa_py_sentimotion_mapper.sentimotion_mapper import Mapper
from nexa_coding_interpreter.metadata import Metadata


class TestMetadata(unittest.TestCase):

    def test_mixed_emotion(self):
        filename = "A404_mix_ang_disg_7030"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A404")
        self.assertEqual(metadata.mix, 1)
        self.assertEqual(metadata.emotion_1_abr, "ang")
        self.assertEqual(metadata.emotion_2_abr, "disg")
        self.assertEqual(metadata.emotion_1_id, 12)
        self.assertEqual(metadata.emotion_2_id, 35)

        self.assertEqual(metadata.proportions, 7030)

    def test_neutral_emotion(self):
        filename = "A220_neu_sit2_v"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A220")
        self.assertEqual(metadata.mix, 0)
        self.assertEqual(metadata.emotion_1_abr, "neu")
        self.assertEqual(metadata.emotion_2_abr, None)
        self.assertEqual(metadata.emotion_1_id, 22)
        self.assertEqual(metadata.emotion_2_id, 100)


        self.assertEqual(metadata.mode, "v")
        self.assertEqual(metadata.situation, 2)


        filename = "A55_neu_p_sit3"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A55")
        self.assertEqual(metadata.mix, 0)
        self.assertEqual(metadata.emotion_1_abr, "neu")
        self.assertEqual(metadata.emotion_2_abr, None)
        self.assertEqual(metadata.emotion_1_id, 22)
        self.assertEqual(metadata.emotion_2_id, 100)

        self.assertEqual(metadata.mode, "p")
        self.assertEqual(metadata.situation, 3)

    def test_long_name(self):
        filename = "A220_neg_sur_p_1"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A220")
        self.assertEqual(metadata.mix, 0)
        self.assertEqual(metadata.emotion_1_abr, "neg_sur")
        self.assertEqual(metadata.emotion_2_abr, None)
        self.assertEqual(metadata.emotion_1_id, 11)
        self.assertEqual(metadata.emotion_2_id, 100)
        self.assertEqual(metadata.proportions, None)

        self.assertEqual(metadata.intensity_level, 1)

        self.assertEqual(metadata.error, 0)
        self.assertEqual(metadata.mode, "p")

    def test_default_emotion(self):
        filename = "A400_adm_p_1"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A400")
        self.assertEqual(metadata.mix, 0)
        self.assertEqual(metadata.emotion_1_abr, "adm")
        self.assertEqual(metadata.emotion_2_abr, None)
        self.assertEqual(metadata.emotion_1_id, 5)
        self.assertEqual(metadata.emotion_2_id, 100)
        self.assertEqual(metadata.intensity_level, 1)

        self.assertEqual(metadata.mode, "p")

    def test_versioned_emotion(self):
        filename = "A327_ang_v_2_ver1"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A327")
        self.assertEqual(metadata.mix, 0)
        self.assertEqual(metadata.emotion_1_abr, "ang")
        self.assertEqual(metadata.emotion_2_abr, None)
        self.assertEqual(metadata.emotion_1_id, 12)
        self.assertEqual(metadata.emotion_2_id, 100)

        self.assertEqual(metadata.intensity_level, 2)

        self.assertEqual(metadata.mode, "v")
        self.assertEqual(metadata.version, 1)

    def test_error_file(self):
        filename = "A438_emb_v_2_e"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A438")
        self.assertEqual(metadata.mix, 0)
        self.assertEqual(metadata.emotion_1_abr, "emb")
        self.assertEqual(metadata.emotion_2_abr, None)
        self.assertEqual(metadata.emotion_1_id, 39)
        self.assertEqual(metadata.emotion_2_id, 100)
        self.assertEqual(metadata.proportions, None)

        self.assertEqual(metadata.intensity_level, 2)

        self.assertEqual(metadata.error, 1)
        self.assertEqual(metadata.mode, "v")

    def test_versioned_neutral_emotion(self):
        filename = "A326_neu_sit2_v_ver1"

        metadata = Metadata(filename)
        self.assertEqual(metadata.video_id, "A326")
        self.assertEqual(metadata.mix, 0)
        self.assertEqual(metadata.emotion_1_abr, "neu")
        self.assertEqual(metadata.emotion_2_abr, None)
        self.assertEqual(metadata.emotion_1_id, 22)
        self.assertEqual(metadata.emotion_2_id, 100)
        self.assertEqual(metadata.proportions, None)

        self.assertEqual(metadata.mode, "v")
