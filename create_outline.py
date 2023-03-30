import fitz
import re


pattern = r"(.*?)\.{2,}(\d*)"

def split_line(line):
    match = re.search(pattern, line)
    return match.groups()


def test_fitz():
    doc = fitz.open("input.pdf")
    toc_page = doc.load_page(2)
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



if __name__ == '__main__':
    test_fitz()