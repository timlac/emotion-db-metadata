from nexa_coding_interpreter.utils import name2list, get_digits_only
from nexa_coding_interpreter.constants import mix, proportions
from nexa_coding_interpreter.metadata import Metadata


class CodeModification:

    def __init__(self, filename):
        self.filename = filename
        self.name_list = name2list(filename)

        new_filename = self.fix_underscore_in_mix_proportions(self.name_list)

        meta = Metadata(new_filename)
        assert meta.mix == 1
        assert meta.emotion_1_id is not None
        assert meta.emotion_2_id is not None

        self.filename = new_filename

    def fix_underscore_in_mix_proportions(self, name_list):
        if len(name_list) == 6:
            if name_list[1] == mix:
                if name_list[4] in proportions and name_list[5] in proportions:
                    name_list[4] = "".join([name_list[4], name_list[5]])
                    del name_list[5]
        return "_".join(name_list)


