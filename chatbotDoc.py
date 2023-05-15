from docx import Document

document = Document('doc/Puebla.docx')
text = ''
for paragraph in document.paragraphs:
    text += paragraph.text + '\n'
response = str(chatbot.get_response(text))
print(response)
