# sentimotion-filename-parser

Package to parse metadata from sentimotionDB filenames

## Installation

Either install directly from the repository

`pip install git+https://github.com/timlac/nexa-sentimotion-filename-parser.git`

Or clone the repository and enter the directory and run:

`pip install .`

## Update

`pip install --upgrade git+https://github.com/timlac/nexa-sentimotion-filename-parser.git`

## Usage

get the filename without extension using the Path library or some other method:

```python
from pathlib import Path

filename = Path(filepath).stem
```

create metadata object:

```python 
from nexa_sentimotion_filename_parser.metadata import Metadata

meta = Metadata(filename)
```

call the metadata object properties, e.g.:

```python 
print("filename: ", meta.filename)
print("video id: ", meta.video_id)
print("mode: ", meta.mode)
print("emotion 1:", meta.emotion_1_abr)
print("emotion_2:", meta.emotion_2_abr)
print("emotion_1_id: ", meta.emotion_1_id)
print("emotion_2_id: ", meta.emotion_2_id)
print("situation: ", meta.situation)
print("version: ", meta.version)
print("intensity_level: ", meta.intensity_level)
print("mix: ", meta.mix)
print("proportions: ", meta.proportions)
```
