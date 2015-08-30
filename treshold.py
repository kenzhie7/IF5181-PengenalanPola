import numpy as np
from scipy import misc
from PIL import Image


alamat = raw_input("pilih(tulis) gambar : ")
gambar = misc.imread(alamat)
tampil = Image.open(alamat)
tampil.show()

height = int(gambar.shape[0])
width = int(gambar.shape[1])

print "resolusi gambar ",width,"x",height," pixels"

batas = raw_input("Trace background, masukan ambang batas (0..255) ? =")
treshold = np.zeros((height,width,3), dtype=np.uint8)
for y in range(height):
	for x in range(width):
		z=(int(gambar[y,x][0])+int(gambar[y,x][1])+int(gambar[y,x][2]))/3
		if z < int(batas):
			treshold[y,x] = [255,255,255] #foreground
		else:
			treshold[y,x] = [255,40,80] #background
			
newgambar = Image.fromarray(treshold, 'RGB')
namafile = raw_input("simpan dengan nama (.jpg)? ")
newgambar.save(namafile)
newgambar.show()
