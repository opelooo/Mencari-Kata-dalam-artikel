rawText = open(r"E:\VSCodeNetBeans\VisualStudioCode\Python\Text\rawText.txt", "r")
text = rawText.read()
rawText.close()
text = text.replace("\"", "").replace(",", "").replace("'", "").replace("-","").replace(".","").replace(";","")

cleanTxt = open(r"E:\VSCodeNetBeans\VisualStudioCode\Python\Text\cleanText.txt", "w+")
cleanTxt.write(text)
cleanTxt.close()

cleanText = open(r"E:\VSCodeNetBeans\VisualStudioCode\Python\Text\cleanText.txt", "r")
cleanData = cleanText.read()
jmlTo = cleanData.count("Robert Zebrowski")
print(jmlTo)
