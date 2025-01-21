from nexa_sentimotion_filename_parser.metadata import Metadata

filename = "A438_emb_v_2_e"
metadata = Metadata(filename)

print(metadata.error)