myFile = open("Me.txt","w+")

myText = '''Nama : Athaullah Mustafa Madjid
NIM : 122140191

Resolusi Saya di Tahun ini : 
1. Menguasai fundamental kotlin dan android 
2. Membuat project kecil android
3. IP diatas 3.3
4. Jadi lebih shaleh
'''

myFile.write(myText)
myFile.close()

# Read File
read_file = open("Me.txt","r")
print(read_file.read())