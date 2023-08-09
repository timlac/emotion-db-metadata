# emotionclips-coding-interpreter
Package to convert emotionclips coding to metadata objects

## Usage

get the filename without extension using the Path library or some other method:

```python
filename = Path(filepath).stem)
```

create metadata object:

```python 
metadata = Metadata(filename)
```

call the metadata object properties, e.g.:

```python 
print("filename: ", metadata.filename)
print("video id: ", metadata.video_id)
print("emotion 1:", metadata.emotion_1)
print("emotion_2:", metadata.emotion_2)
print("emotion_1_id: ", metadata.emotion_1_id)
print("emotion_2_id: ", metadata.emotion_2_id)
print("emotion_1_valence: ", metadata.emotion_1_valence)
print("emotion_2_valence: ", metadata.emotion_2_valence)
print("situation: ", metadata.situation)
print("intensity_level: ", metadata.intensity_level)
```
