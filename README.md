# MP3 Splitter

This is a simple Python script that splits an MP3 file into smaller chunks. 

## Description

The script takes an MP3 file as an input and divides it into chunks of a specified length. By default, each chunk is 4 minutes long, but this can be adjusted using the `-l` or `--length` option when running the script. The resulting MP3 chunks are saved in a new directory named after the input file.

## Installation

This script requires Python 3 and the pydub library.

You can install pydub with pip:

```
pip install pydub
```

## Usage

```
python3 split_audio.py <input_file> --length <chunk_length_in_milliseconds>
```

<input_file>: Path to the input MP3 file.

<chunk_length_in_milliseconds>: Length of each chunk in milliseconds. Default is 400000 (4 minutes).

For example, to split a file named example.mp3 into 2-minute chunks, you would run:

```
python3 split_audio.py example.mp3 --length 120000
```

This will create a new directory named example, containing the MP3 chunks.

## License

This project is licensed under the terms of the MIT license.
