# TensorFlow_Bebidas

Este guia supõe que você tem uma versão do Linux superior a 12.04 instalada no seu computador com OpenCV e os pacotes essentials e imutils.

Seguir o guia de instalação do Docker pela página
https://docs.docker.com/engine/installation/linux/ubuntulinux/

E seguir o guia do TensorFlow for poets pela página
https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0

Na parte 4 do guia do TensorFlow for Poets, ao invés de fazer o download da foto das flores com o comando
curl -O http://download.tensorflow.org/example_images/flower_photos.tgz
É necessário fazer o download dos arquivos
- Frames Video Antartica.rar
https://www.dropbox.com/s/efj10hczqfouj8d/Frames%20Video%20Antartica.rar?dl=0
- Frames Video Brahma.rar
https://www.dropbox.com/s/0q6x1kion4nclvf/Frames%20Video%20Brahma.rar?dl=0
- Frames Video Skol.rar
https://www.dropbox.com/s/ew69zdeyfy7jkq4/Frames%20Video%20Skol.rar?dl=0
- Frames Video Skolbeats.rar
https://www.dropbox.com/s/4izh95eaybomx1i/Frames%20Video%20Skolbeats.rar?dl=0
- ignorar.zip
https://www.dropbox.com/s/xhuxzdqjxd4okzn/ignorar.zip?dl=0

É necessário criar uma pasta com nome "beers" e extrair os arquivos para dentro da pasta criando novas pastas seguinte forma:
Frames Video Antartica.rar dentro de uma pasta com nome "antartica";
Frames Video Brahma.rar dentro de uma pasta com nome "brahma";
Frames Video Skol.rar dentro de uma pasta com nome "skol";
Frames Video Skolbeats.rar dentro de uma pasta com nome "skolbeatssense";
ignorar.zip dentro de uma pasta com nome "ignorar";

Com os arquivos baixados e separados pelas suas pastas dentro de tf_files, voltamos para o docker utilizando:
docker ps -aq (Este comando vai lhe retornar os container criado anteriormente)
Localize o container com TensorFlow e digite
docker start numero_do_container
docker run numero_do_container

Você deve executar o comando:
cd /tensorflow
git pull

Dentro do docker será necessário editar um arquivo com nano ou vim o comando para editar com nano é:
nano /tensorflow/tensorflow/examples/image_retraining/retrain.py

Na linha que mostra o DATA_URL, é necessário modificar a URL, pois o arquivo antigo está corrompido, então mude o DATA_URL para:
DATA_URL = 'http://download.tensorflow.org/models/image/imagenet/inception-v3-2016-03-01.tar.gz'

Agora você pode treinar sua máquina, digite os comandos:
cd /tensorflow
python tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=/tf_files/bottlenecks \
--how_many_training_steps 50000 \
--model_dir=/tf_files/inception \
--output_graph=/tf_files/retrained_graph.pb \
--output_labels=/tf_files/retrained_labels.txt \
--image_dir /tf_files/beers

Agora você deve colocar os arquivos python na pasta tf_files:
- classifica_camera.py
- pyramid.py
- sliding_window.py

Abrir o terminal com o comando Ctrl+Alt+T e usar os comando:
cd ~/tf_files
python classifica_camera.py

Daí o algoritmo deve capturar as imagens da camera usb e identificar as cervejas treinadas.
