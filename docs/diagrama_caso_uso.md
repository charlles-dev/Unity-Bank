# Sistema Bancário - Diagrama de Casos de Uso

## 🎯 Visão Geral

Este documento descreve os casos de uso do Sistema Bancário, mostrando as interações entre os atores (usuários) e as funcionalidades do sistema.

## 👥 Atores Identificados

### 🙋‍♂️ Cliente
- **Descrição**: Usuário final que possui uma conta bancária
- **Responsabilidades**: 
  - Realizar operações bancárias em sua conta
  - Consultar informações da conta
  - Gerenciar suas transações

### 🏦 Sistema Bancário
- **Descrição**: Sistema computacional que gerencia as operações
- **Responsabilidades**:
  - Processar transações
  - Validar operações
  - Manter dados atualizados
  - Garantir integridade dos dados

## 📋 Casos de Uso Detalhados

### 🔐 UC01 - Acessar Sistema
**Ator Principal**: Cliente  
**Descrição**: Cliente acessa o sistema informando número da conta  
**Pré-condições**: 
- Cliente deve possuir conta cadastrada
- Sistema deve estar funcionando

**Fluxo Principal**:
1. Cliente informa número da conta
2. Sistema valida existência da conta
3. Sistema autentica cliente
4. Sistema apresenta menu de opções

**Fluxos Alternativos**:
- **2a. Conta não existe**: Sistema informa erro e retorna ao início

---

### 🏦 UC02 - Criar Conta
**Ator Principal**: Cliente  
**Descrição**: Criar nova conta bancária no sistema  
**Pré-condições**: Sistema deve estar funcionando

**Fluxo Principal**:
1. Cliente seleciona opção "Criar Conta"
2. Cliente informa nome completo
3. Cliente informa CPF/CNPJ
4. Sistema gera número único da conta
5. Sistema cria conta com saldo inicial R$ 0,00
6. Sistema confirma criação da conta

**Pós-condições**: Nova conta é criada no sistema

---

### 💰 UC03 - Realizar Depósito
**Ator Principal**: Cliente  
**Descrição**: Cliente deposita dinheiro em sua conta  
**Pré-condições**: 
- Cliente deve estar autenticado
- Cliente deve ter conta ativa

**Fluxo Principal**:
1. Cliente seleciona "Depositar"
2. Cliente informa valor do depósito
3. Sistema valida valor (deve ser > 0)
4. Sistema atualiza saldo da conta
5. Sistema registra transação no extrato
6. Sistema confirma operação

**Fluxos Alternativos**:
- **3a. Valor inválido**: Sistema solicita valor válido

**Pós-condições**: Saldo da conta é atualizado

---

### 💸 UC04 - Realizar Saque
**Ator Principal**: Cliente  
**Descrição**: Cliente retira dinheiro de sua conta  
**Pré-condições**: 
- Cliente deve estar autenticado
- Cliente deve ter saldo suficiente

**Fluxo Principal**:
1. Cliente seleciona "Sacar"
2. Cliente informa valor do saque
3. Sistema valida valor (deve ser > 0)
4. Sistema verifica saldo suficiente
5. Sistema debita valor da conta
6. Sistema registra transação no extrato
7. Sistema confirma operação

**Fluxos Alternativos**:
- **3a. Valor inválido**: Sistema solicita valor válido
- **4a. Saldo insuficiente**: Sistema informa erro e cancela operação

**Pós-condições**: Saldo da conta é atualizado

---

### 🔍 UC05 - Consultar Saldo
**Ator Principal**: Cliente  
**Descrição**: Cliente consulta saldo atual da conta  
**Pré-condições**: Cliente deve estar autenticado

**Fluxo Principal**:
1. Cliente seleciona "Consultar Saldo"
2. Sistema recupera saldo atual da conta
3. Sistema exibe saldo formatado para o cliente

**Pós-condições**: Informação é apresentada ao cliente

---

### 📋 UC06 - Visualizar Extrato
**Ator Principal**: Cliente  
**Descrição**: Cliente consulta histórico de transações  
**Pré-condições**: Cliente deve estar autenticado

**Fluxo Principal**:
1. Cliente seleciona "Extrato"
2. Sistema recupera histórico de transações da conta
3. Sistema exibe transações em ordem cronológica
4. Sistema mostra: tipo, valor, data/hora, saldo resultante

**Fluxos Alternativos**:
- **2a. Sem transações**: Sistema informa que não há movimentações

**Pós-condições**: Histórico é apresentado ao cliente

---

### 🔄 UC07 - Transferir Dinheiro
**Ator Principal**: Cliente  
**Descrição**: Cliente transfere dinheiro para outra conta  
**Pré-condições**: 
- Cliente deve estar autenticado
- Cliente deve ter saldo suficiente
- Conta destino deve existir

**Fluxo Principal**:
1. Cliente seleciona "Transferir"
2. Cliente informa número da conta destino
3. Sistema valida conta destino
4. Cliente informa valor da transferência
5. Sistema valida valor e saldo suficiente
6. Sistema debita da conta origem
7. Sistema credita na conta destino
8. Sistema registra transações em ambas as contas
9. Sistema confirma operação

**Fluxos Alternativos**:
- **3a. Conta destino inexistente**: Sistema informa erro
- **5a. Saldo insuficiente**: Sistema cancela operação
- **5b. Valor inválido**: Sistema solicita valor válido

---

### 💳 UC08 - Pagar Conta
**Ator Principal**: Cliente  
**Descrição**: Cliente realiza pagamento de contas  
**Pré-condições**: 
- Cliente deve estar autenticado
- Cliente deve ter saldo suficiente

**Fluxo Principal**:
1. Cliente seleciona "Pagar Conta"
2. Cliente informa descrição do pagamento
3. Cliente informa valor do pagamento
4. Sistema valida valor e saldo suficiente
5. Sistema debita valor da conta
6. Sistema registra pagamento no extrato
7. Sistema confirma operação

**Fluxos Alternativos**:
- **4a. Saldo insuficiente**: Sistema cancela operação
- **4b. Valor inválido**: Sistema solicita valor válido

---

### 📊 UC09 - Listar Contas
**Ator Principal**: Cliente  
**Descrição**: Visualizar todas as contas do sistema  
**Pré-condições**: Sistema deve ter contas cadastradas

**Fluxo Principal**:
1. Cliente seleciona "Listar Contas"
2. Sistema recupera todas as contas
3. Sistema exibe: número, titular, saldo atual

**Fluxos Alternativos**:
- **2a. Sem contas**: Sistema informa que não há contas cadastradas

---

### 🚪 UC10 - Encerrar Sessão
**Ator Principal**: Cliente  
**Descrição**: Cliente encerra sua sessão no sistema  
**Pré-condições**: Cliente deve estar autenticado

**Fluxo Principal**:
1. Cliente seleciona "Sair"
2. Sistema limpa dados da sessão
3. Sistema retorna ao menu principal
4. Sistema aguarda nova autenticação

**Pós-condições**: Sessão é encerrada com segurança

## 🔗 Relacionamentos entre Casos de Uso

### Inclusões (<<include>>)
- **UC03, UC04, UC07, UC08** incluem **Validação de Valor**
- **UC03, UC04, UC06, UC07, UC08** incluem **Registro no Extrato**
- **UC04, UC07, UC08** incluem **Verificação de Saldo**

### Extensions (<<extend>>)
- **Validação de Conta Destino** estende **UC07**
- **Formatação de Dados** estende **UC05, UC06, UC09**

### Generalizações
- **Operações Bancárias** generaliza **UC03, UC04, UC07, UC08**
- **Consultas** generaliza **UC05, UC06, UC09**

## 🎨 Representação Visual do Diagrama

```
    [Cliente] ────────────┐
         │                │
         │                ▼
         ├──── UC01: Acessar Sistema
         │
         ├──── UC02: Criar Conta
         │
         ├──── UC03: Realizar Depósito ◄──── <<include>> Validação
         │
         ├──── UC04: Realizar Saque ◄─────── <<include>> Verificação Saldo
         │
         ├──── UC05: Consultar Saldo
         │
         ├──── UC06: Visualizar Extrato
         │
         ├──── UC07: Transferir Dinheiro ◄── <<include>> Validação Conta
         │
         ├──── UC08: Pagar Conta
         │
         ├──── UC09: Listar Contas
         │
         └──── UC10: Encerrar Sessão
                      │
                      ▼
              [Sistema Bancário]
```

## 📈 Análise de Complexidade

### Casos de Uso por Complexidade:
- **Simples**: UC01, UC02, UC05, UC09, UC10 (5 casos)
- **Médios**: UC03, UC04, UC06, UC08 (4 casos)
- **Complexos**: UC07 (1 caso)

### Prioridade de Implementação:
1. **Fase 1**: UC01, UC02, UC05 (Básico)
2. **Fase 2**: UC03, UC04, UC06 (Operações essenciais)
3. **Fase 3**: UC07, UC08, UC09, UC10 (Funcionalidades avançadas)

---

*Este diagrama serve como guia para implementação e deve ser usado em conjunto com os requisitos funcionais e o código Python.*