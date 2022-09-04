#buka file dalam yang ada di path "E:\VSCodeNetBeans\VisualStudioCode\Python\Text\rawText.txt" dengan mode read only
rawText = open(r"E:\VSCodeNetBeans\VisualStudioCode\Python\Text\rawText.txt", "r")
#baca file yang sudah dibuka tadi dan memasukanya kedalam variable text
text = rawText.read()
#close statement
rawText.close()

#Data cleaning untuk tulisan didalam file yang sudah dibuka tadi dengan menghapus tanda (",'-.;)
text = text.replace("\"", "").replace(",", "").replace("'", "").replace("-","").replace(".","").replace(";","")

#membuat file baru bernama cleanText.txt dengan mode write read dan membukanya
cleanTxt = open(r"E:\VSCodeNetBeans\VisualStudioCode\Python\Text\cleanText.txt", "w+")
#tulis file cleanText.txt dengan data yang sudah dibersihkan tadi
cleanTxt.write(text)
cleanTxt.close()

#baca file cleanText.txt dengan mode read
cleanText = open(r"E:\VSCodeNetBeans\VisualStudioCode\Python\Text\cleanText.txt", "r")
#masukan tulisan didalam file kedalam variable cleanData
cleanData = cleanText.read()
#hitung jumlah kata "Robert Zebrowski" yang keluar sebanyak berapa kali dan masukan kedalam variable jmlTo
jmlTo = cleanData.count("Robert Zebrowski")
#tampilkan variable jmlTo kedalam konsol
print(jmlTo)
