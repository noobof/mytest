import os
import argparse
import transformers
from datasets import load_dataset
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', help = 'directory to save data to', type= str, default='data')
    args = parser.parse_args()

    if not os.path.isdir(args.output_dir):
        os.makedirs(args.output_dir)

    dataset = load_dataset('squad', 'squad', cache_dir=args.output_dir, split='validation')