import argparse, os, json, re
from pipeline import pipeline
import markdown
from pdfminer.high_level import extract_text

def get_json_response(pdf_dir, saved_path, parsed_type, rich_markdown_host, rich_markdown_port):
    
    os.makedirs(saved_path, exist_ok=True)
    for pdfname in os.listdir(pdf_dir):
        if not pdfname.endswith('.pdf'):
            continue
        print(pdfname)
        pdf_file_path = os.path.join(pdf_dir, pdfname)
        pdfname_short, _ = os.path.splitext(pdfname)

        file_size = os.path.getsize(pdf_file_path)
        file_type = "text/plain"
        
        if parsed_type == 'raw_text':
            saved_file_path = os.path.join(saved_path, pdfname_short + ".txt")
            if os.path.exists(saved_file_path):
                continue
            # change from PyPDF2 to pdfminer.six due to some errors in JSON decoding
            file_content = extract_text(pdf_file_path)

            string_encode = file_content.encode("ascii", "ignore")
            file_content = string_encode.decode()

            file_content = re.sub("-\n", "", file_content)
            file_content = file_content.replace("\n", "")
        else:
            saved_file_path = os.path.join(saved_path, pdfname_short + ".md")
            if os.path.exists(saved_file_path):
                continue
            xml_tmp_path = os.path.join(saved_path, 'xml_tmp')
            os.makedirs(xml_tmp_path, exist_ok=True)
            xml, md = pipeline(xml_tmp_path, pdf_file_path, rich_markdown_host, rich_markdown_port)
            file_content = markdown.markdown(md, extensions=['tables']).replace("<s>", "")
            
            # import pdb;pdb.set_trace()
        
        with open(saved_file_path, "w") as f:
            f.write(file_content)

                
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse PDF documents.')
    parser.add_argument('--pdf_dir', type=str, default='./results/raw_pdfs', help='Path to the raw PDF files.')
    parser.add_argument('--saved_path', type=str, default='./results/text_parsed/rich_markdown/',  help='Path where the parsed documents will be saved.')
    parser.add_argument('--parsed_type', type=str, default='rich_markdown', choices=['raw_text', 'rich_markdown'],  help='The type of parsing to perform.')
    # when using rich_markdown option, you are required to install grobid: https://github.com/kermitt2/grobid
    parser.add_argument('--rich_markdown_host', type=str, default='192.168.1.73', help='Host.')
    parser.add_argument('--rich_markdown_port', type=str, default='8070', help='Port.')
    args = parser.parse_args()
    
    get_json_response(args.pdf_dir, args.saved_path, args.parsed_type, args.rich_markdown_host, args.rich_markdown_port)
    
    # Your code to perform the parsing would go here
    # This is where you would use args.raw_pdf_path, args.parsed_path, and args.parsed_type