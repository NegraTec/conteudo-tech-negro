
case "$1"
 in
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
 *)
    echo $"Usage: $0 {desencripta-env-yaml|encripta-env-yaml|configura-projeto-google}"
    exit 1
esac