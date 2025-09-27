# 🏦 Unity Bank

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Testes](https://img.shields.io/badge/Testes-Pytest-green)](https://pytest.org)
[![Documentação](https://img.shields.io/badge/Docs-Completa-brightgreen)](#documentação)
[![Licença](https://img.shields.io/badge/Licença-MIT-yellow)](LICENSE)

Um sistema bancário completo implementado em Python seguindo princípios de **Engenharia de Software** e **modelagem UML**. Este projeto foi desenvolvido como uma atividade educacional abrangente que combina requisitos funcionais, casos de uso e implementação prática.

## 📋 Índice

- [Características Principais](#-características-principais)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação e Execução](#-instalação-e-execução)
- [Funcionalidades](#-funcionalidades)
- [Documentação Técnica](#-documentação-técnica)
- [Testes](#-testes)
- [Exemplos de Uso](#-exemplos-de-uso)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

## 🚀 Características Principais

### ✅ Engenharia de Software
- **Requisitos Funcionais Completos**: 12 requisitos bem documentados (RF01-RF12)
- **Casos de Uso Detalhados**: 10 casos de uso com fluxos principais e alternativos
- **Arquitetura Orientada a Objetos**: Classes bem estruturadas e separação de responsabilidades
- **Documentação Técnica**: Especificações completas e diagramas

### 🏗️ Implementação Robusta
- **Validação de Dados**: Entrada de usuário validada em todas as operações
- **Tratamento de Erros**: Exceções customizadas e mensagens informativas
- **Logging de Transações**: Extrato detalhado com histórico completo
- **Interface Intuitiva**: Menu interativo com emojis e formatação clara

### 🧪 Qualidade de Código
- **Testes Automatizados**: Cobertura completa com pytest
- **Testes de Integração**: Cenários complexos e casos extremos
- **Código Limpo**: PEP 8, documentação e type hints
- **Modularidade**: Arquitetura facilmente extensível

## 📂 Estrutura do Projeto

```
sistema_bancario/
├── 📄 main.py                      # Aplicação principal
├── 📁 src/                         # Código fonte
│   ├── 🐍 __init__.py             # Módulo principal
│   ├── 🏦 conta.py                # Classe ContaBancaria
│   ├── 🏪 banco.py                # Classe SistemaBancario
│   └── 🖥️ interface.py            # Interface de usuário
├── 📁 tests/                      # Testes automatizados
│   ├── 🧪 test_conta.py           # Testes unitários da conta
│   ├── 🧪 test_banco.py           # Testes unitários do sistema
│   └── 🧪 test_integracao.py      # Testes de integração
├── 📁 docs/                       # Documentação técnica
│   ├── 📋 requisitos_funcionais.md # Especificação de requisitos
│   └── 📊 diagrama_caso_uso.md    # Casos de uso detalhados
├── 📁 diagrams/                   # Diagramas UML (opcional)
└── 📖 README.md                   # Este arquivo
```

## 🛠️ Instalação e Execução

### Pré-requisitos
- Python 3.8 ou superior
- Pytest (para executar testes)

### Instalação

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd sistema_bancario
   ```

2. **Instale as dependências** (opcional para testes):
   ```bash
   pip install pytest pytest-cov
   ```

### Execução

**Executar o sistema bancário**:
```bash
python main.py
```

**Executar os testes**:
```bash
# Todos os testes
python -m pytest tests/

# Testes com cobertura
python -m pytest --cov=src tests/

# Teste específico
python -m pytest tests/test_conta.py
```

## 💰 Funcionalidades

### 🏦 Gerenciamento de Contas
- ✅ **Criação de Contas**: Cadastro com validação de CPF/CNPJ único
- ✅ **Autenticação**: Acesso por número da conta
- ✅ **Listagem**: Visualização de todas as contas do sistema
- ✅ **Estatísticas**: Relatórios e métricas do sistema

### 💸 Operações Bancárias
- ✅ **Depósitos**: Adição de valores com descrição personalizada
- ✅ **Saques**: Retirada com validação de saldo suficiente
- ✅ **Transferências**: Entre contas do mesmo sistema
- ✅ **Pagamentos**: Contas e serviços com descrição

### 📊 Consultas e Relatórios
- ✅ **Consulta de Saldo**: Visualização do saldo atual
- ✅ **Extrato Detalhado**: Histórico completo de transações
- ✅ **Resumo da Conta**: Informações consolidadas
- ✅ **Busca por Titular**: Localização de contas por nome

### 🔒 Segurança e Validação
- ✅ **Validação de Entrada**: Todos os inputs são validados
- ✅ **Tratamento de Erros**: Mensagens claras e recuperação
- ✅ **Integridade de Dados**: Consistência em todas as operações
- ✅ **Auditoria**: Log completo de todas as transações

## 📚 Documentação Técnica

### 📋 Requisitos Funcionais
Veja: [`docs/requisitos_funcionais.md`](docs/requisitos_funcionais.md)

**Resumo dos Requisitos**:
- **RF01-RF02**: Criação e autenticação de contas
- **RF03-RF06**: Operações básicas (depósito, saque, consulta, extrato)
- **RF07-RF08**: Operações avançadas (transferência, pagamento)
- **RF09-RF12**: Funcionalidades do sistema (listagem, controles)

### 📊 Casos de Uso
Veja: [`docs/diagrama_caso_uso.md`](docs/diagrama_caso_uso.md)

**Casos de Uso Implementados**:
- **UC01**: Acessar Sistema
- **UC02**: Criar Conta
- **UC03-UC04**: Realizar Depósito/Saque
- **UC05-UC06**: Consultar Saldo/Extrato
- **UC07-UC08**: Transferir/Pagar
- **UC09-UC10**: Listar Contas/Encerrar Sessão

## 🧪 Testes

O projeto inclui uma suíte completa de testes:

### 🔬 Testes Unitários
- **`test_conta.py`**: 20+ testes da classe ContaBancaria
- **`test_banco.py`**: 15+ testes da classe SistemaBancario
- **Cobertura**: Todas as funcionalidades principais

### 🔗 Testes de Integração
- **`test_integracao.py`**: Cenários completos de uso
- **Testes de Robustez**: Casos extremos e recuperação de erros
- **Validação de Consistência**: Integridade dos dados

### 📊 Executar Testes
```bash
# Testes básicos
python -m pytest tests/ -v

# Com relatório de cobertura
python -m pytest --cov=src --cov-report=html tests/

# Testes específicos
python -m pytest tests/test_conta.py::TestContaBancaria::test_deposito_valido
```

## 💡 Exemplos de Uso

### 🔧 Uso Programático

```python
from src.banco import SistemaBancario

# Criar sistema bancário
banco = SistemaBancario("Meu Banco")

# Criar contas
conta_joao = banco.criar_conta("João Silva", "123.456.789-00")
conta_maria = banco.criar_conta("Maria Santos", "987.654.321-00")

# Operações bancárias
conta_joao.depositar(1000.0, "Salário")
conta_joao.sacar(200.0, "Compras")
conta_joao.transferir(conta_maria, 100.0, "Empréstimo")

# Consultas
print(f"Saldo João: R$ {conta_joao.obter_saldo():.2f}")
print(f"Saldo Maria: R$ {conta_maria.obter_saldo():.2f}")

# Extrato
for transacao in conta_joao.obter_extrato():
    print(f"{transacao['tipo']}: R$ {transacao['valor']:.2f}")
```

### 🖥️ Interface de Usuário

```
╔══════════════════════════════════════════════════════════════╗
║                    🏦 SISTEMA BANCÁRIO DIGITAL               ║
║                         Python Edition                       ║
╠══════════════════════════════════════════════════════════════╣
║  ✅ Requisitos Funcionais Completos                          ║
║  ✅ Diagrama de Casos de Uso                                 ║
║  ✅ Implementação Orientada a Objetos                        ║
╚══════════════════════════════════════════════════════════════╝

MENU PRINCIPAL
──────────────────────────────────────────
1️⃣  Acessar Conta Existente
2️⃣  Criar Nova Conta
3️⃣  Listar Todas as Contas
4️⃣  Estatísticas do Sistema
0️⃣  Sair do Sistema

🎯 Escolha uma opção:
```

## 🎓 Valor Educacional

Este projeto é ideal para:

### 📖 **Estudantes de Engenharia de Software**
- Aplicação prática de requisitos funcionais
- Modelagem UML com casos de uso reais
- Implementação orientada a objetos

### 🐍 **Aprendizado de Python**
- Classes, herança e encapsulamento
- Tratamento de exceções
- Testes automatizados com pytest
- Boas práticas de código

### 🏦 **Compreensão de Sistemas Bancários**
- Operações financeiras básicas
- Validação e auditoria
- Consistência de dados
- Interface de usuário

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. **Push** para a branch (`git push origin feature/MinhaFeature`)
5. **Abra** um Pull Request

### 📋 Diretrizes de Contribuição
- Mantenha o código limpo e documentado
- Adicione testes para novas funcionalidades
- Siga as convenções de nomenclatura existentes
- Atualize a documentação quando necessário

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Autores

**Sistema Bancário Python** - *Desenvolvimento inicial*:
- [Charlles-dev](https://github.com/charlles-dev)
- [Weidyzk](https://github.com/Weidyzk)
## 🙏 Agradecimentos

- Inspirado em princípios de Engenharia de Software
- Documentação baseada em padrões UML
- Interface de usuário focada na experiência do usuário
- Testes seguindo boas práticas da comunidade Python

---

**📱 Unity Bank - Transformando conceitos em código prático!** 🚀

*Desenvolvido com ❤️ em Python para fins educacionais e demonstrativos.*