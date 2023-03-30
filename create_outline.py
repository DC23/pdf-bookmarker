import click
import fitz
import re


pattern = r"(.*?)\.{2,}(\d*)"

def split_line(line):
    match = re.search(pattern, line)
    return match.groups()


def parse_toc(page:int, input_pdf:str):
    doc = fitz.open(input_pdf)
    toc_page = doc.load_page(page)
    for line in toc_page.get_text().split("\n"):
        # print(line)
        try:
            name, page = split_line(line)
            if name.find("PART") > -1:
                print(f"{name}: {page}")
            else: 
                print(f"\t{name}: {page}")
        except:
            print(line)


@click.command()
@click.option("--toc-page", type=click.INT, help="PDF page containing the table of contents")
@click.option("--input_pdf", help="The input PDF")
@click.option("--output_pdf", help="The output PDF")
def run(toc_page:int, input_pdf:str, output_pdf:str):
    parse_toc(toc_page, input_pdf)

if __name__ == '__main__':
    run()