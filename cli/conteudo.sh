
case "$1"
 in
 constroe-projeto)
	sudo docker-compose build
 ;;
 roda-projeto)
	sudo docker-compose up --build
 ;;
 testes)
	echo "Construa a imagem antes de executar este comando."
	sudo docker run --rm -it -v "$PWD":/usr/src/app -w /usr/src/app -e TESTES=True conteudo-tech-negro_web pytest -W ignore::DeprecationWarning
 ;;
 configura-projeto-google)
	echo "Logue com suas credenciais do Google Cloud"
	sudo docker run -v "$PWD":/root/.config -w /root/.config -ti google/cloud-sdk:latest gcloud auth login

	echo "Configura o projeto Google conteudo-negro-tech"
  	sudo docker run -v "$PWD":/root/.config -w /root/.config -ti google/cloud-sdk:latest gcloud config set project conteudo-negro-tech
 ;;
 desencripta-env-yaml)
	echo "Você precisa está logado no Google Cloud."
	echo "Configura o projeto Google encrypted-keys"
	sudo docker run -v "$PWD":/root/.config -w /root/.config -ti google/cloud-sdk:latest gcloud config set project encrypted-keys

	echo "Desencripta env.yaml.encrypted para o arquivo env.yaml"
	sudo docker run -v "$PWD":/root/.config -w /root/.config -ti google/cloud-sdk:latest gcloud kms decrypt --location global --keyring storage --key mykey --plaintext-file env.yaml --ciphertext-file env.yaml.encrypted

	echo "Configura o projeto Google conteudo-negro-tech"
  	sudo docker run -v "$PWD":/root/.config -w /root/.config -ti google/cloud-sdk:latest gcloud config set project conteudo-negro-tech
 ;;
 encripta-env-yaml)
	echo "Você precisa está logado no Google Cloud."
	echo "Configura o projeto Google encrypted-keys"
	sudo docker run -v "$PWD":/root/.config -w /root/.config -ti google/cloud-sdk:latest gcloud config set project encrypted-keys

	echo "Encripta env.yaml para o arquivo env.yaml.encrypted"
	docker run -v "$PWD":/root/.config -w /root/.config -ti google/cloud-sdk:latest gcloud kms encrypt --location global \
  --keyring storage --key mykey \
  --plaintext-file env.yaml \
  --ciphertext-file env.yaml.encrypted

	echo "Configura o projeto Google conteudo-negro-tech"
  	sudo docker run -v "$PWD":/root/.config -w /root/.config -ti google/cloud-sdk:latest gcloud config set project conteudo-negro-tech
 ;;
 build-travis-cli) 
	sudo docker build -t travis-cli --file Dockerfile-travis-cli .
 ;;
 testes-func)
	sudo docker run --rm -it -v "$PWD":/usr/src/app -w /usr/src/app -e TESTES=True conteudo-tech-negro_web behave
 ;;
 *)
    echo $"Usage: $0 {desencripta-env-yaml|encripta-env-yaml|configura-projeto-google|testes|roda-projeto|constroe-projeto|build-travis-cli|encripta-gae-credenciais}"
    exit 1
esac