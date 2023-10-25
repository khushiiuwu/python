import docx
doc = docx.Document('C:/Practice/darkchocolate.docx')


all_words = doc.paragraphs

for para in all_words:
    print(para.text,end=" ")   