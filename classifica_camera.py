import tensorflow as tf, sys
from pyramid import pyramid
from sliding_window import sliding_window
import threading
import time
import cv2
import numpy as np

# persists graph from file
f = tf.gfile.FastGFile("retrained_graph.pb", 'rb')
graph_def = tf.GraphDef()
graph_def.ParseFromString(f.read())
graph1 = tf.import_graph_def(graph_def, name='')
sess = tf.Session()
softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

camera = cv2.VideoCapture(0)
ret, frame = camera.read()
cv2.imshow("Camera", frame)


def showVideo():
	
	while True:

		ret, frame = camera.read()
		cv2.imshow("Camera", frame)
		cv2.imwrite("imagem1.jpg",frame)
		#if score > 0.65:
		#	cv2.rectangle(frame, (x, y), (x + winW, y + winH), (0, 0,255), 2)
			
	
	
def classifica():
	
	#tamanho da janela de classificacao
	(winW, winH) = (256, 192)

	while True:
		copia = cv2.imread("imagem1.jpg")
		cv2.imwrite("imagem2.jpg",copia)
		image = cv2.imread("imagem2.jpg")
		#loop pyramid da imagem
		#time.sleep(5.0)
		for resized in pyramid(image, scale=1.5):
			#loop de sliding_window para cada pyramid da imagem
			for(x, y, window) in sliding_window(resized, stepSize=128, windowSize=(winW, winH)):
				#verifica se a window atende ao requisitos, senao, ignora
				if window.shape[0] != winH or window.shape[1] != winW:
					continue
		
				##codigo de processar janela e classificador
				clone = resized.copy()
				cropped_image = clone[y:y+winH, x:x+winW]
				cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
				cv2.imshow("TensorFlow", clone)
				cv2.waitKey(1)
				cv2.imwrite("imagem_cropped.jpg", cropped_image)
				image_path = ("imagem_cropped.jpg")
				image_data = tf.gfile.FastGFile(image_path, 'rb').read()
								
				label_lines = [line.rstrip() for line 
	 			           in tf.gfile.GFile("retrained_labels.txt")]
	  			        
				predictions = sess.run(softmax_tensor, \
	 					      {'DecodeJpeg/contents:0': image_data})
		
				top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
	
				for node_id in top_k:
					human_string = label_lines[node_id]
					score = predictions[0][node_id]
					if human_string == 'ignorar':
						break
					elif score > 0.85:
						cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 0,255), 2)
						cv2.imshow("Detected", clone)
						cv2.waitKey(5)
						print('%s (score = %.5f)' % (human_string, score))
						

			

threadVideo = threading.Thread(target = showVideo)
threadClassifica = threading.Thread(target = classifica)

threadVideo.start()
threadClassifica.start()
