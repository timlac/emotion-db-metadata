from coding_interpreter.mappings import emotion_id_to_valence, emotion_abr_to_emotion_id, special_cases
from coding_interpreter.utils import name2list, get_digits_only


class Metadata(object):

    DEFAULT_INTENSITY_LEVEL = 1
    DEFAULT_VERSION = 1
    DEFAULT_SITUATION = 1

    # can be vocalization (v) or prosody (p)
    DEFAULT_MODE = "v"

    DEFAULT_PROPORTIONS = 0
    DEFAULT_EMOTION = None
    DEFAULT_MIX = 0
    # set it to some number not in the list
    DEFAULT_EMOTION_ID = 100
    DEFAULT_VALENCE = None

    DEFAULT_ERROR = 0

    def __init__(self,
                 filename):

        self.filename = filename
        self.name_list = name2list(filename)

        # e.g. A220
        self.video_id = self.name_list[0]

        self.mix = self.DEFAULT_MIX
        self.emotion_1 = self.DEFAULT_EMOTION
        self.emotion_1_id = self.DEFAULT_EMOTION_ID

        self.emotion_2 = self.DEFAULT_EMOTION
        self.emotion_2_id = self.DEFAULT_EMOTION_ID

        self.proportions = self.DEFAULT_PROPORTIONS
        self.mode = self.DEFAULT_MODE
        self.intensity_level = self.DEFAULT_INTENSITY_LEVEL
        self.version = self.DEFAULT_VERSION
        self.situation = self.DEFAULT_SITUATION
        self.emotion_1_valence = self.DEFAULT_VALENCE
        self.emotion_2_valence = self.DEFAULT_VALENCE

        self.error = self.DEFAULT_ERROR

        self.set_all_metadata(self.name_list)

    def set_mixed_emotions(self, name_list):
        """
        e.g. A220_mix_ang_disg_5050
        """
        self.mix = 1
        self.emotion_1 = name_list[2]
        self.emotion_2 = name_list[3]
        self.proportions = int(name_list[4])

    def set_neutral_emotion(self, name_list):
        """
        e.g. A220_neu_sit1_v
        or A55_neu_p_sit3
        Note: the coding of neutral emotions is inconsistent, it varies between the two alternatives above
        """
        self.emotion_1 = name_list[1]
        # remove all non-numeric characters from situation string, keep only the digit
        if len(name_list[2]) == 1:
            self.mode = name_list[2]
            self.situation = get_digits_only(name_list[3])
        elif len(name_list[2]) == 4:
            self.situation = get_digits_only(name_list[2])
            self.mode = name_list[3]

    def set_long_name(self, name_list):
        """
        e.g. A220_neg_sur_p_1
        """
        # concat the long name of the emotion
        self.emotion_1 = "_".join((name_list[1], name_list[2]))
        self.mode = name_list[3]
        self.intensity_level = int(name_list[4])

    def set_default_emotion(self, name_list):
        """
        e.g. A220_adm_p_1
        """
        self.emotion_1 = name_list[1]
        self.mode = name_list[2]
        self.intensity_level = int(name_list[3])

    def set_versioned_emotion(self, name_list):
        """
        e.g. A327_ang_v_1_ver1
        """
        self.emotion_1 = name_list[1]
        self.mode = name_list[2]
        self.intensity_level = int(name_list[3])
        self.version = get_digits_only(name_list[4])

    def set_error_file(self, name_list):
        """
        e.g. A438_emb_v_2_e
        """
        self.emotion_1 = name_list[1]
        self.mode = name_list[2]
        self.intensity_level = int(name_list[3])
        self.error = 1

    def set_emotion_ids(self):
        self.emotion_1_id = emotion_abr_to_emotion_id[self.emotion_1]

        if self.mix == 1:
            self.emotion_2_id = emotion_abr_to_emotion_id[self.emotion_2]

    def set_valence(self):
        self.emotion_1_valence = emotion_id_to_valence[self.emotion_1_id]
        if self.mix == 1:
            self.emotion_2_valence = emotion_id_to_valence[self.emotion_2_id]

    def set_all_metadata(self, name_list):
        if name_list[1] == special_cases["mixed_emotions"]:
            self.set_mixed_emotions(name_list)
        elif name_list[1] == special_cases["neutral_emotion"]:
            self.set_neutral_emotion(name_list)
        elif len(name_list) > 4:
            if name_list[4] == special_cases["error"]:
                self.set_error_file(name_list)
            elif name_list[4].startswith(special_cases["versioned"]):
                self.set_versioned_emotion(name_list)
            else:
                self.set_long_name(name_list)
        else:
            self.set_default_emotion(name_list)

        self.set_emotion_ids()
        self.set_valence()
