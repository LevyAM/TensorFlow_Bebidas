import imutils

def pyramid(image, scale=1.5, minSize=(30,30)):
	#chama imagem original	
	yield image
	
	#loop pyramid
	while True:
		#novas dimensoes da imagem e resize
		w = int(image.shape[1] / scale)
		image = imutils.resize(image, width=w)

		#verifica resize comparando com o minSize
		if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
			break

		#chama proxima imagem ate n ter mais nenhuma
		yield image
