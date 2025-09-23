# Script de Instalação Automática de Ferramentas de Desenvolvimento

Este script Python automatiza a instalação e atualização de ferramentas essenciais de desenvolvimento e DevOps em sistemas Ubuntu/Debian.

## 📋 Ferramentas Incluídas

O script instala e atualiza automaticamente as seguintes ferramentas:

### Ferramentas Padrão (via apt)

- **Ansible** - Ferramenta de automação e gerenciamento de configuração
- **Python3** - Linguagem de programação Python
- **kubectl** - Cliente de linha de comando do Kubernetes

### Ferramentas com Instaladores Oficiais

- **AWS CLI v2** - Interface de linha de comando da Amazon Web Services
- **Azure CLI** - Interface de linha de comando do Microsoft Azure
- **Docker** - Plataforma de containerização
- **OpenTofu** - Ferramenta de Infrastructure as Code (fork do Terraform)
- **AWS CDK** - Kit de desenvolvimento de nuvem da AWS

## 🚀 Como Usar

### Pré-requisitos

- Sistema Ubuntu/Debian
- Python 3 instalado
- Acesso sudo
- Conexão com a internet

### Execução

```bash
# Tornar o script executável (opcional)
chmod +x my_stuff.py

# Executar o script
python3 py_install.py
```

## 🔧 Funcionalidades

### Verificação Inteligente

- O script verifica se cada ferramenta já está instalada
- Se instalada: tenta atualizar para a versão mais recente
- Se não instalada: realiza instalação completa

### Instalação Segura

- Usa repositórios oficiais sempre que possível
- Remove versões conflitantes do Docker antes da instalação
- Configura chaves GPG e repositórios adequadamente
- Instala Node.js via NodeSource para compatibilidade com AWS CDK

### Feedback em Tempo Real

- Mostra o status de cada operação
- Informa se está instalando ou atualizando cada ferramenta

## 📁 Estrutura do Código

### Funções Principais

- `is_installed(command)` - Verifica se um comando está disponível no sistema
- `run_commands(commands)` - Executa uma lista de comandos sequencialmente
- `update_or_install_standard(package, command)` - Instala/atualiza pacotes via apt
- `install_or_update_aws_cli()` - Gerencia instalação do AWS CLI
- `install_or_update_azure_cli()` - Gerencia instalação do Azure CLI
- `install_or_update_docker()` - Gerencia instalação do Docker
- `install_or_update_tofu()` - Gerencia instalação do OpenTofu
- `install_or_update_awscdk()` - Gerencia instalação do AWS CDK

## ⚠️ Considerações Importantes

### Permissões

- O script requer privilégios sudo para instalação de pacotes
- Certifique-se de ter as permissões adequadas antes de executar

### Tempo de Execução

- A primeira execução pode demorar vários minutos
- Depende da velocidade da internet e do número de ferramentas a instalar

### Compatibilidade

- Testado em Ubuntu (versões recentes)
- Pode funcionar em outras distribuições baseadas em Debian

### AWS CDK - Correções Implementadas

- Instala Node.js via NodeSource para garantir compatibilidade de versão
- Usa `sudo` para instalação global do npm
- Corrige problemas de permissão e incompatibilidade de versão

## 🛠️ Personalização

Para adicionar novas ferramentas ao script:

1. **Para pacotes apt padrão**: Adicione ao dicionário `standard_packages`
2. **Para instaladores customizados**: Crie uma nova função seguindo o padrão das existentes

Exemplo:

```python
# Adicionar nova ferramenta via apt
standard_packages = {
    "Ansible": "ansible",
    "Python3": "python3",
    "kubectl": "kubectl",
    "Nova Ferramenta": "nome-do-pacote"  # Adicione aqui
}
```

## 🔍 Verificação Pós-Instalação

Após a execução, você pode verificar se as ferramentas foram instaladas corretamente:

```bash
# Verificar versões instaladas
ansible --version
python3 --version
kubectl version --client
aws --version
az --version
docker --version
tofu --version
cdk --version
```

## 🐛 Solução de Problemas

### Erro de Permissão npm

Se encontrar erros de permissão com npm, o script já foi corrigido para:

- Instalar Node.js via NodeSource (versão compatível)
- Usar `sudo` para instalações globais

### Erro de Versão Node.js

O script instala automaticamente a versão LTS do Node.js via NodeSource, resolvendo problemas de compatibilidade.

## 📝 Log de Execução

O script fornece feedback em tempo real durante a execução, mostrando:

- Quais ferramentas estão sendo verificadas
- Se cada ferramenta será instalada ou atualizada
- Status de progresso das operações

## 🤝 Contribuições

Para contribuir com melhorias:

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Implemente as mudanças
4. Teste em ambiente Ubuntu/Debian
5. Submeta um pull request

## 📄 Licença

Este script é fornecido como está, para uso educacional e de desenvolvimento.

---

**Nota**: Sempre revise scripts que requerem privilégios sudo antes de executá-los em ambientes de produção.
