import subprocess

def is_installed(command):
    return subprocess.call(f"type {command}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def run_commands(commands):
    for cmd in commands:
        subprocess.call(cmd, shell=True)

def update_or_install_standard(package, command):
    if is_installed(command):
        print(f"{package} está instalado. Tentando atualizar...")
        subprocess.call(f"sudo apt-get install --only-upgrade -y {command}", shell=True)
    else:
        print(f"{package} não está instalado. Instalando...")
        subprocess.call(f"sudo apt-get install -y {command}", shell=True)

def install_or_update_aws_cli():
    print("Verificando AWS CLI...")
    if is_installed("aws"):
        print("AWS CLI está instalado. Atualizando com instalador oficial...")
    else:
        print("AWS CLI não está instalado. Instalando com instalador oficial...")
    aws_commands = [
        'curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"',
        'unzip awscliv2.zip',
        'sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update',
        'sudo rm -rf awscliv2.zip'
    ]
    run_commands(aws_commands)

def install_or_update_azure_cli():
    print("Verificando Azure CLI...")
    if is_installed("az"):
        print("Azure CLI está instalado. Atualizando com repositório oficial...")
    else:
        print("Azure CLI não está instalado. Instalando com repositório oficial...")
    azure_commands = [
        'sudo apt-get update -y',
        'sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release',
        'sudo mkdir -p /etc/apt/keyrings',
        'curl -sLS https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /etc/apt/keyrings/microsoft.gpg > /dev/null',
        'sudo chmod go+r /etc/apt/keyrings/microsoft.gpg',
        'sudo apt-get update -y',
        'sudo apt-get install -y azure-cli'
    ]
    run_commands(azure_commands)

def install_or_update_docker():
    print("Verificando Docker...")
    if is_installed("docker"):
        print("Docker está instalado. Atualizando com repositório oficial...")
    else:
        print("Docker não está instalado. Instalando com repositório oficial...")
    docker_commands = [
        'for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove -y $pkg; done',
        'sudo apt-get update',
        'sudo apt-get install -y ca-certificates curl',
        'sudo install -m 0755 -d /etc/apt/keyrings',
        'sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc',
        'sudo chmod a+r /etc/apt/keyrings/docker.asc',
        'echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo ${UBUNTU_CODENAME:-$VERSION_CODENAME}) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null',
        'sudo apt-get update',
        'sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin'
    ]
    run_commands(docker_commands)

def install_or_update_tofu():
    print("Verificando OpenTofu...")
    if is_installed("tofu"):
        print("OpenTofu está instalado, Atualizando com repositório oficial...")
    else:
        print("OpenTofu não está instalado. Instalando com repositório oficial...")
    tofu_commands = [
        "curl --proto '=https' --tlsv1.2 -fsSL https://get.opentofu.org/install-opentofu.sh -o install-opentofu.sh",
        'chmod +x install-opentofu.sh',
        './install-opentofu.sh --install-method deb',
        'rm -f install-opentofu.sh'
    ]
    run_commands(tofu_commands)

def install_or_update_awscdk():
    print("Verificando AWS CDK...")
    if is_installed('aws_cdk'):
        print("AWS CDK está instalado, Atualizando com repositório oficial...")
    else:
        print("AWS CDK não está instalado, Instalando de acordo com a documentação oficial.")
    awscdk_commands =[
        'sudo apt install nodejs npm -y',
        'sudo npm install -g npm@latest',
        'npm install -g aws-cdk',
    ]
    run_commands(awscdk_commands)

# Pacotes padrão
standard_packages = {
    "Ansible": "ansible",
    "Python3": "python3",
    "kubectl": "kubectl"
}

for package, command in standard_packages.items():
    update_or_install_standard(package, command)

install_or_update_aws_cli()
install_or_update_azure_cli()
install_or_update_docker()
install_or_update_tofu()
install_or_update_awscdk()
