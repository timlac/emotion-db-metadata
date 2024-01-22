import re

modes = {"prosody": "p",
         "vocalization": "v"}

situations = {"situation_1": "sit1",
              "situation_2": "sit2",
              "situation_3": "sit3",
              "situation_4": "sit4"
              }

# Compile the regex pattern
version = re.compile(r'^ver\d+$')

intensity_levels = {"below_medium": 1,
                    "medium": 2,
                    "high": 3,
                    "extremely_high": 4
                    }

long_emotion_names = {"positive_surprise": "pos_sur",
                      "negative_surprise": "neg_sur"}

error = "e"

mix = "mix"

proportions = ["30", "50", "70"]

neu = "neu"

