# Sistema Bancário - Requisitos Funcionais

## 📋 Requisitos Funcionais Identificados

### 🏦 Funcionalidades Básicas de Conta

#### RF01 - Criação de Conta
- **Descrição**: O sistema deve permitir a criação de contas bancárias
- **Critério de Aceitação**: 
  - Cliente deve fornecer nome completo e documento (CPF/CNPJ)
  - Sistema deve gerar um número único de conta
  - Saldo inicial deve ser R$ 0,00
  - Cada conta deve ter um número único sequencial

#### RF02 - Autenticação de Cliente
- **Descrição**: O sistema deve autenticar clientes pelo número da conta
- **Critério de Aceitação**:
  - Cliente deve informar número da conta para acesso
  - Sistema deve validar se a conta existe
  - Acesso negado para contas inexistentes

### 💰 Operações Bancárias

#### RF03 - Depósito
- **Descrição**: O cliente deve poder depositar dinheiro em sua conta
- **Critério de Aceitação**:
  - Valor do depósito deve ser maior que zero
  - Saldo da conta deve ser atualizado imediatamente
  - Operação deve ser registrada no extrato
  - Sistema deve confirmar a operação com nova data/hora

#### RF04 - Saque
- **Descrição**: O cliente deve poder sacar dinheiro da conta
- **Critério de Aceitação**:
  - Valor do saque deve ser maior que zero
  - Cliente deve ter saldo suficiente para a operação
  - Saldo da conta deve ser atualizado imediatamente
  - Saque negado se saldo insuficiente
  - Operação deve ser registrada no extrato

#### RF05 - Consulta de Saldo
- **Descrição**: O cliente deve poder consultar o saldo atual da conta
- **Critério de Aceitação**:
  - Sistema deve exibir saldo atual formatado em reais
  - Informação deve estar sempre atualizada
  - Operação não deve alterar o saldo

#### RF06 - Extrato Bancário
- **Descrição**: O cliente deve poder consultar o histórico de transações
- **Critério de Aceitação**:
  - Sistema deve exibir todas as transações da conta
  - Cada transação deve mostrar: tipo, valor, data/hora e saldo após operação
  - Extrato deve estar em ordem cronológica (mais recentes primeiro)
  - Sistema deve informar se não há transações

### 🔄 Operações Avançadas

#### RF07 - Transferência Entre Contas
- **Descrição**: O cliente deve poder transferir dinheiro para outra conta
- **Critério de Aceitação**:
  - Conta de origem deve ter saldo suficiente
  - Conta de destino deve existir
  - Valor deve ser maior que zero
  - Ambas as contas devem ter seus saldos atualizados
  - Operação deve ser registrada no extrato de ambas as contas

#### RF08 - Pagamento de Contas
- **Descrição**: O cliente deve poder pagar contas utilizando o saldo da conta
- **Critério de Aceitação**:
  - Cliente deve ter saldo suficiente
  - Sistema deve permitir informar descrição do pagamento
  - Valor deve ser maior que zero
  - Operação deve ser registrada no extrato

### 🏪 Funcionalidades do Sistema

#### RF09 - Listagem de Contas
- **Descrição**: O sistema deve permitir visualizar todas as contas cadastradas
- **Critério de Aceitação**:
  - Lista deve mostrar número da conta, nome do titular e saldo atual
  - Sistema deve informar se não há contas cadastradas

#### RF10 - Encerramento de Sessão
- **Descrição**: O cliente deve poder encerrar sua sessão de forma segura
- **Critério de Aceitação**:
  - Sistema deve retornar ao menu principal
  - Dados da sessão devem ser limpos

### 🎛️ Funcionalidades de Controle

#### RF11 - Menu Principal
- **Descrição**: O sistema deve apresentar menu intuitivo de navegação
- **Critério de Aceitação**:
  - Menu deve listar todas as opções disponíveis
  - Sistema deve permitir navegação entre diferentes funcionalidades
  - Opção de saída do sistema deve estar disponível

#### RF12 - Validação de Entrada
- **Descrição**: O sistema deve validar todas as entradas do usuário
- **Critério de Aceitação**:
  - Valores monetários devem aceitar apenas números positivos
  - Sistema deve tratar entradas inválidas com mensagens claras
  - Não deve quebrar com entradas inesperadas

## 📊 Resumo dos Requisitos

**Total de Requisitos Funcionais**: 12

### Categoria de Requisitos:
- **Básicos de Conta**: 2 requisitos (RF01, RF02)
- **Operações Bancárias**: 4 requisitos (RF03-RF06) 
- **Operações Avançadas**: 2 requisitos (RF07, RF08)
- **Funcionalidades do Sistema**: 2 requisitos (RF09, RF10)
- **Controle**: 2 requisitos (RF11, RF12)

### Priorização:
- **Alta Prioridade**: RF01-RF06 (Funcionalidades essenciais)
- **Média Prioridade**: RF07-RF09 (Funcionalidades avançadas)
- **Baixa Prioridade**: RF10-RF12 (Funcionalidades de suporte)

---

*Este documento serve como base para o desenvolvimento do sistema bancário e deve ser usado em conjunto com o diagrama de casos de uso e a implementação em Python.*