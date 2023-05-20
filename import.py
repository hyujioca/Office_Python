from docx import Document
document = Document()
f = open('samle.docx', 'r')
lines = f.readlines()
for c in lines:
    print(len(c))
f.close
document.add_picture("download.jpg")
document.save('sample_answer.docx')