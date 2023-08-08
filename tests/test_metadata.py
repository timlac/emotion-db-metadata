import unittest
from pathlib import Path
import os

from metadata import Metadata


class TestMetadata(unittest.TestCase):

    def test_mixed_emotion(self):
        filename = "A404_mix_ang_disg_7030"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A404")
        self.assertEqual(metadata.mix, 1)
        self.assertEqual(metadata.emotion_1, "ang")
        self.assertEqual(metadata.emotion_2, "disg")
        self.assertEqual(metadata.emotion_1_id, 12)
        self.assertEqual(metadata.emotion_2_id, 35)
        self.assertEqual(metadata.emotion_1_valence, "neg")
        self.assertEqual(metadata.emotion_2_valence, "neg")
        self.assertEqual(metadata.intensity_level, 1)

        self.assertEqual(metadata.error, 0)
        self.assertEqual(metadata.mode, "v")
        self.assertEqual(metadata.version, 1)
        self.assertEqual(metadata.situation, 1)

    def test_neutral_emotion(self):
        filename = "A220_neu_sit2_v"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A220")
        self.assertEqual(metadata.mix, 0)
        self.assertEqual(metadata.emotion_1, "neu")
        self.assertEqual(metadata.emotion_2, None)
        self.assertEqual(metadata.emotion_1_id, 22)
        self.assertEqual(metadata.emotion_2_id, 100)
        self.assertEqual(metadata.emotion_1_valence, "neu")
        self.assertEqual(metadata.emotion_2_valence, None)
        self.assertEqual(metadata.proportions, 0)

        self.assertEqual(metadata.intensity_level, 1)

        self.assertEqual(metadata.error, 0)
        self.assertEqual(metadata.mode, "v")
        self.assertEqual(metadata.version, 1)
        self.assertEqual(metadata.situation, 2)


        filename = "A55_neu_p_sit3"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A55")
        self.assertEqual(metadata.mix, 0)
        self.assertEqual(metadata.emotion_1, "neu")
        self.assertEqual(metadata.emotion_2, None)
        self.assertEqual(metadata.emotion_1_id, 22)
        self.assertEqual(metadata.emotion_2_id, 100)
        self.assertEqual(metadata.emotion_1_valence, "neu")
        self.assertEqual(metadata.emotion_2_valence, None)
        self.assertEqual(metadata.proportions, 0)

        self.assertEqual(metadata.intensity_level, 1)

        self.assertEqual(metadata.error, 0)
        self.assertEqual(metadata.mode, "p")
        self.assertEqual(metadata.version, 1)
        self.assertEqual(metadata.situation, 3)

    def test_long_name(self):
        filename = "A220_neg_sur_p_1"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A220")
        self.assertEqual(metadata.mix, 0)
        self.assertEqual(metadata.emotion_1, "neg_sur")
        self.assertEqual(metadata.emotion_2, None)
        self.assertEqual(metadata.emotion_1_id, 11)
        self.assertEqual(metadata.emotion_2_id, 100)
        self.assertEqual(metadata.emotion_1_valence, "neg")
        self.assertEqual(metadata.emotion_2_valence, None)
        self.assertEqual(metadata.proportions, 0)

        self.assertEqual(metadata.intensity_level, 1)

        self.assertEqual(metadata.error, 0)
        self.assertEqual(metadata.mode, "p")
        self.assertEqual(metadata.version, 1)
        self.assertEqual(metadata.situation, 1)

    def test_default_emotion(self):
        filename = "A400_adm_p_1"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A400")
        self.assertEqual(metadata.mix, 0)
        self.assertEqual(metadata.emotion_1, "adm")
        self.assertEqual(metadata.emotion_2, None)
        self.assertEqual(metadata.emotion_1_id, 5)
        self.assertEqual(metadata.emotion_2_id, 100)
        self.assertEqual(metadata.emotion_1_valence, "pos")
        self.assertEqual(metadata.emotion_2_valence, None)
        self.assertEqual(metadata.proportions, 0)

        self.assertEqual(metadata.intensity_level, 1)

        self.assertEqual(metadata.error, 0)
        self.assertEqual(metadata.mode, "p")
        self.assertEqual(metadata.version, 1)
        self.assertEqual(metadata.situation, 1)

    def test_versioned_emotion(self):
        filename = "A327_ang_v_1_ver1"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A327")
        self.assertEqual(metadata.mix, 0)
        self.assertEqual(metadata.emotion_1, "ang")
        self.assertEqual(metadata.emotion_2, None)
        self.assertEqual(metadata.emotion_1_id, 12)
        self.assertEqual(metadata.emotion_2_id, 100)
        self.assertEqual(metadata.emotion_1_valence, "neg")
        self.assertEqual(metadata.emotion_2_valence, None)
        self.assertEqual(metadata.proportions, 0)

        self.assertEqual(metadata.intensity_level, 1)

        self.assertEqual(metadata.error, 0)
        self.assertEqual(metadata.mode, "v")
        self.assertEqual(metadata.version, 1)
        self.assertEqual(metadata.situation, 1)

    def test_error_file(self):
        filename = "A438_emb_v_2_e"
        metadata = Metadata(filename)

        self.assertEqual(metadata.video_id, "A438")
        self.assertEqual(metadata.mix, 0)
        self.assertEqual(metadata.emotion_1, "emb")
        self.assertEqual(metadata.emotion_2, None)
        self.assertEqual(metadata.emotion_1_id, 39)
        self.assertEqual(metadata.emotion_2_id, 100)
        self.assertEqual(metadata.emotion_1_valence, "neg")
        self.assertEqual(metadata.emotion_2_valence, None)
        self.assertEqual(metadata.proportions, 0)

        self.assertEqual(metadata.intensity_level, 2)

        self.assertEqual(metadata.error, 1)
        self.assertEqual(metadata.mode, "v")
        self.assertEqual(metadata.version, 1)
        self.assertEqual(metadata.situation, 1)

