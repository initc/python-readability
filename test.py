from readability import Document

with open("test.html","r") as fp:
    text = fp.read()
doc = Document(text)
summary = doc.summary()
with open("sub_test.html","w") as f:
   f.write(summary)
