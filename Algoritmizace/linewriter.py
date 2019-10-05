def writeTextToFile(Text):
  STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
  f = open('MyText.txt','w')
  f.write(STATICKY_TEXT + str(Text))
  f.close()
  return f.name








MyText ='And this is my terrible text'
print(writeTextToFile(MyText))
