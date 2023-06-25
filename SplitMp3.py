from pydub import AudioSegment
import argparse
import os
import os.path

def split_audio(input_file, chunk_length):
    # 入力ファイル名から拡張子を除いたものを出力ディレクトリ名として利用
    output_directory = os.path.splitext(os.path.basename(input_file))[0]

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    audio = AudioSegment.from_mp3(input_file)
    total_length = len(audio)
    start_time = 0

    for i in range(0, total_length, chunk_length):
        end_time = start_time + chunk_length
        chunk = audio[start_time:end_time]
        chunk.export(os.path.join(output_directory, f"{output_directory}_{i//chunk_length:03d}.mp3"), format="mp3")
        start_time = end_time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split an MP3 file into smaller chunks")
    parser.add_argument("input_file", help="Path to input MP3 file")
    parser.add_argument("-l", "--length", type=int, default=400000, help="Length of each chunk in milliseconds (default: 400000)")
    args = parser.parse_args()

    input_file = args.input_file
    chunk_length = args.length

    split_audio(input_file, chunk_length)
