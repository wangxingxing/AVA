import argparse
import os
import pandas as pd
import youtube_dl
import glob

def main(output_dir):
    file_path = os.path.dirname(os.path.realpath(__file__))
    train_csv = os.path.join(file_path, 'data', 'ava_train_v1.0.csv')
    test_csv = os.path.join(file_path, 'data', 'ava_test_v1.0.csv')
    for floder_name in ['', 'train', 'test']:
        path = os.path.join(output_dir, floder_name)
        if not os.path.exists(path):
            os.makedirs(path)

    for split in ['train', 'test']:
        ydl_opts = {
            'username': 'your google username',
            'password': 'your goole passwd',
            'ignoreerrors': True,
            'format': 'bestvideo+bestaudio',
            'outtmpl': os.path.join(output_dir, split, '%(id)s.%(ext)s')
        }
        list = eval('pd.read_csv(' + split + '_csv, header=None)')
        for youtube_id in list[0].unique():
            if not glob.glob(os.path.join(output_dir, split, youtube_id+'.*')) or glob.glob(os.path.join(output_dir, split, youtube_id+'*.part')):
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(['http://www.youtube.com/watch?v=' + youtube_id])

if __name__ == '__main__':
    p = argparse.ArgumentParser(description = 'Download ava')
    p.add_argument('output_dir', type = str)
    main(**vars(p.parse_args()))


