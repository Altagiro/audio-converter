import sox


def convert_audio(input_filename="", output_filename=""):
    if not input_filename:
        print("No input filename provided!")
        return

    output_filename = "output_{}".format(input_filename) if not output_filename else output_filename

    tfm = sox.Transformer()
    tfm.convert(samplerate=8000, n_channels=1, bitdepth=16)
    tfm.build(input_filepath=input_filename, output_filepath=output_filename)

    print("File {} is converted.".format(input_filename))
    return
