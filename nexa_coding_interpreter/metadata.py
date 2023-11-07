import warnings

from nexa_py_sentimotion_mapper.sentimotion_mapper import Mapper
from nexa_coding_interpreter.utils import name2list, get_digits_only

from nexa_coding_interpreter.constants import *


class Metadata(object):

    DEFAULT_INTENSITY_LEVEL = None
    DEFAULT_VERSION = None
    DEFAULT_SITUATION = None

    # can be vocalization (v) or prosody (p)
    DEFAULT_MODE = None

    DEFAULT_PROPORTIONS = None
    DEFAULT_EMOTION_ABR = None
    DEFAULT_MIX = 0
    # set it to some number not in the list
    DEFAULT_EMOTION_ID = 100

    DEFAULT_ERROR = 0

    def __init__(self,
                 filename):
        self.filename = filename
        self.name_list = name2list(filename)

        # e.g. A220
        self.video_id = self.name_list[0]

        self.mix = self.DEFAULT_MIX
        self.emotion_1_abr = self.DEFAULT_EMOTION_ABR
        self.emotion_1_id = self.DEFAULT_EMOTION_ID

        self.emotion_2_abr = self.DEFAULT_EMOTION_ABR
        self.emotion_2_id = self.DEFAULT_EMOTION_ID

        self.proportions = self.DEFAULT_PROPORTIONS
        self.mode = self.DEFAULT_MODE
        self.intensity_level = self.DEFAULT_INTENSITY_LEVEL
        self.version = self.DEFAULT_VERSION
        self.situation = self.DEFAULT_SITUATION

        self.error = self.DEFAULT_ERROR

        self.set_all_metadata(self.name_list)

    def set_mixed_emotions(self, name_list):
        """
        e.g. A220_mix_ang_disg_5050
        """
        assert name_list[1] == "mix"
        assert Mapper.get_id_from_emotion_abr(name_list[2]) is not None
        assert Mapper.get_id_from_emotion_abr(name_list[3]) is not None
        assert name_list[4].isdigit()

        self.mix = 1
        self.emotion_1_abr = name_list[2]
        self.emotion_2_abr = name_list[3]
        self.proportions = int(name_list[4])

    def set_neutral_emotion(self, name_list):
        """
        e.g. A220_neu_sit1_v
        or A55_neu_p_sit3
        Note: the coding of neutral emotions is inconsistent, it varies between the two alternatives above
        """
        assert Mapper.get_id_from_emotion_abr(name_list[1]) is not None
        assert len(name_list) == 4

        self.emotion_1_abr = name_list[1]

        if name_list[2] in modes.values():
            warnings.warn(f'{self.filename} has incorrect syntax. The correct syntax is something like A220_neu_sit1_v')

            self.mode = name_list[2]
            if name_list[3] in situations.values():
                self.situation = get_digits_only(name_list[3])

        elif name_list[2] in situations.values():
            self.situation = get_digits_only(name_list[2])
            if name_list[3] in modes.values():
                self.mode = name_list[3]
        else:
            raise ValueError(f'No condition matched for {self.filename}'
                             f'tried to set it as neutral emotion bur failed')

    def set_long_name(self, name_list):
        """
        e.g. A220_neg_sur_p_1
        """
        emotion_1_abr = "_".join((name_list[1], name_list[2]))

        assert Mapper.get_id_from_emotion_abr(emotion_1_abr) is not None
        assert name_list[3] in modes.values()
        assert int(name_list[4]) in intensity_levels.values()

        self.emotion_1_abr = emotion_1_abr
        self.mode = name_list[3]
        self.intensity_level = int(name_list[4])

    def set_default_emotion(self, name_list):
        """
        e.g. A220_adm_p_1
        """
        assert Mapper.get_id_from_emotion_abr(name_list[1]) is not None
        assert name_list[2] in modes.values()
        assert int(name_list[3]) in intensity_levels.values()

        self.emotion_1_abr = name_list[1]
        self.mode = name_list[2]
        self.intensity_level = int(name_list[3])

    def set_versioned_emotion(self, name_list):
        """
        e.g. A327_ang_v_1_ver1
        """
        self.set_default_emotion(name_list[:4])
        self.version = get_digits_only(name_list[4])

    def set_error_file(self, name_list):
        """
        e.g. A438_emb_v_2_e
        """
        self.set_default_emotion(name_list[:4])
        self.error = 1

    def set_emotion_ids(self):
        self.emotion_1_id = Mapper.get_id_from_emotion_abr(self.emotion_1_abr)
        if self.mix == 1:
            self.emotion_2_id = Mapper.get_id_from_emotion_abr(self.emotion_2_abr)

    def set_all_metadata(self, name_list):
        if len(name_list) == 4:
            if name_list[1] == neu:
                self.set_neutral_emotion(name_list)
            else:
                if Mapper.get_id_from_emotion_abr(name_list[1]) is not None:
                    self.set_default_emotion(name_list)
                else:
                    raise ValueError(f'No condition met for {self.filename}')
        elif len(name_list) == 5:
            if name_list[1] == mix:
                self.set_mixed_emotions(name_list)
            elif name_list[1:3] in [x.split("_") for x in long_emotion_names.values()]:
                self.set_long_name(name_list)
            elif name_list[4] == error:
                self.set_error_file(name_list)
            elif version.match(name_list[4]):
                self.set_versioned_emotion(name_list)
            else:
                raise ValueError(f'No condition matched for {self.filename}')

        self.set_emotion_ids()
