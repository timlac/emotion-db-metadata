import os
from pathlib import Path

from nexa_sentimotion_filename_parser.metadata import Metadata


def main():
    directory = "example_data"

    for filename in os.listdir(directory):
        print("filename: ", filename)

        meta = Metadata(Path(filename).stem)

        print("video id: ", meta.video_id)
        print("emotion_1:", meta.emotion_1_abr)
        print("emotion_2:", meta.emotion_2_abr)
        print("emotion_1_id: ", meta.emotion_1_id)
        print("emotion_2_id: ", meta.emotion_2_id)
        print("situation: ", meta.situation)
        print("intensity_level: ", meta.intensity_level)
        print("version: ", meta.version)
        print("error: ", meta.error)
        print()


if __name__ == "__main__":
    main()