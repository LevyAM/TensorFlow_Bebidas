# TensorFlow_Bebidas

Este guia supõe que você tem uma versão do Linux superior a 12.04 instalada no seu computador.

Seguir o guia de instalação do Docker pela página
https://docs.docker.com/engine/installation/linux/ubuntulinux/

E seguir o guia do TensorFlow for poets pela página
https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0

Na parte 4 do guia do TensorFlow for Poets, ao invés de fazer o download da foto das flores com o comando
curl -O http://download.tensorflow.org/example_images/flower_photos.tgz
É necessário fazer o download dos arquivos
- Frames Video Antartica.rar
- Frames Video Brahma.rar
- Frames Video Skol.rar
- Frames Video Skolbeats.rar
- ignorar.zip

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

Espere o tempo de treinamento e saia do docker com o comando Ctrl+D.
