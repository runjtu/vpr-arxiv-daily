import os
import json
import requests
from tqdm import tqdm
import argparse

def download_pdf(save_path, pdf_name, pdf_url):
    pdf_file_path = os.path.join(save_path, f'{pdf_name}.pdf')
    if os.path.exists(pdf_file_path):
        return 
    response = requests.get(pdf_url)
    with open(pdf_file_path, mode='wb') as file:
        file.write(response.content)
    print(f'{pdf_name}.PDF downloaded successfully!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download PDFs from arXiv.')
    parser.add_argument('--json_path', type=str, default='../docs/cv-arxiv-daily-web.json', help='Path to the JSON file with document IDs.')
    parser.add_argument('--saved_path', type=str, default='./results/raw_pdfs', help='Path where the PDFs will be saved.')
    args = parser.parse_args()

    with open(args.json_path, 'r') as file:
        data = json.load(file)
        for keyword in data.keys():
            print(f'{keyword}:')
            for doc_id in tqdm(data[keyword].keys(), desc='Downloading PDFs'):
                if '/' in doc_id: # skip too old papers
                    continue
                download_pdf(args.saved_path, doc_id, f'https://arxiv.org/pdf/{doc_id}.pdf')
