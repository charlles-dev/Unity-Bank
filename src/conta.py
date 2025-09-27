"""
Sistema Bancário - Módulo Conta
Implementação da classe Conta Bancária com todas as funcionalidades básicas.
"""

from datetime import datetime
from typing import List, Dict, Any


class ContaBancaria:
    """
    Classe que representa uma conta bancária com funcionalidades completas.
    
    Attributes:
        numero_conta (int): Número único da conta
        titular (str): Nome do titular da conta
        cpf_cnpj (str): Documento do titular (CPF ou CNPJ)
        saldo (float): Saldo atual da conta
        extrato (List[Dict]): Histórico de transações da conta
        data_criacao (datetime): Data/hora de criação da conta
    """
    
    # Contador estático para gerar números únicos de conta
    _proximo_numero = 1001
    
    def __init__(self, titular: str, cpf_cnpj: str):
        """
        Inicializa uma nova conta bancária.
        
        Args:
            titular (str): Nome completo do titular
            cpf_cnpj (str): CPF ou CNPJ do titular
        
        Raises:
            ValueError: Se titular ou CPF/CNPJ estiverem vazios
        """
        if not titular or not titular.strip():
            raise ValueError("Nome do titular é obrigatório")
        
        if not cpf_cnpj or not cpf_cnpj.strip():
            raise ValueError("CPF/CNPJ é obrigatório")
        
        self.numero_conta = ContaBancaria._proximo_numero
        ContaBancaria._proximo_numero += 1
        
        self.titular = titular.strip()
        self.cpf_cnpj = cpf_cnpj.strip()
        self.saldo = 0.0
        self.extrato: List[Dict[str, Any]] = []
        self.data_criacao = datetime.now()
        
        # Registra criação da conta no extrato
        self._registrar_transacao("CRIAÇÃO DE CONTA", 0.0, "Conta criada")
    
    def depositar(self, valor: float, descricao: str = "Depósito") -> bool:
        """
        Realiza um depósito na conta.
        
        Args:
            valor (float): Valor a ser depositado
            descricao (str): Descrição da transação
            
        Returns:
            bool: True se o depósito foi realizado com sucesso
            
        Raises:
            ValueError: Se o valor for inválido (menor ou igual a zero)
        """
        if valor <= 0:
            raise ValueError("Valor do depósito deve ser maior que zero")
        
        self.saldo += valor
        self._registrar_transacao("DEPÓSITO", valor, descricao)
        return True
    
    def sacar(self, valor: float, descricao: str = "Saque") -> bool:
        """
        Realiza um saque da conta.
        
        Args:
            valor (float): Valor a ser sacado
            descricao (str): Descrição da transação
            
        Returns:
            bool: True se o saque foi realizado com sucesso
            
        Raises:
            ValueError: Se o valor for inválido
            RuntimeError: Se não houver saldo suficiente
        """
        if valor <= 0:
            raise ValueError("Valor do saque deve ser maior que zero")
        
        if valor > self.saldo:
            raise RuntimeError(f"Saldo insuficiente. Saldo atual: R$ {self.saldo:.2f}")
        
        self.saldo -= valor
        self._registrar_transacao("SAQUE", -valor, descricao)
        return True
    
    def transferir(self, conta_destino: 'ContaBancaria', valor: float, 
                   descricao: str = "Transferência") -> bool:
        """
        Transfere dinheiro para outra conta.
        
        Args:
            conta_destino (ContaBancaria): Conta que receberá a transferência
            valor (float): Valor a ser transferido
            descricao (str): Descrição da transferência
            
        Returns:
            bool: True se a transferência foi realizada com sucesso
            
        Raises:
            ValueError: Se o valor for inválido ou conta destino for None
            RuntimeError: Se não houver saldo suficiente
        """
        if not conta_destino:
            raise ValueError("Conta destino é obrigatória")
        
        if valor <= 0:
            raise ValueError("Valor da transferência deve ser maior que zero")
        
        if valor > self.saldo:
            raise RuntimeError(f"Saldo insuficiente. Saldo atual: R$ {self.saldo:.2f}")
        
        # Realiza a transferência
        self.saldo -= valor
        conta_destino.saldo += valor
        
        # Registra nas duas contas
        self._registrar_transacao("TRANSFERÊNCIA ENVIADA", -valor, 
                                f"{descricao} - Para conta {conta_destino.numero_conta}")
        conta_destino._registrar_transacao("TRANSFERÊNCIA RECEBIDA", valor,
                                         f"{descricao} - De conta {self.numero_conta}")
        return True
    
    def pagar_conta(self, valor: float, descricao: str) -> bool:
        """
        Realiza pagamento de conta/serviço.
        
        Args:
            valor (float): Valor do pagamento
            descricao (str): Descrição do pagamento
            
        Returns:
            bool: True se o pagamento foi realizado com sucesso
            
        Raises:
            ValueError: Se o valor for inválido ou descrição vazia
            RuntimeError: Se não houver saldo suficiente
        """
        if valor <= 0:
            raise ValueError("Valor do pagamento deve ser maior que zero")
        
        if not descricao or not descricao.strip():
            raise ValueError("Descrição do pagamento é obrigatória")
        
        if valor > self.saldo:
            raise RuntimeError(f"Saldo insuficiente. Saldo atual: R$ {self.saldo:.2f}")
        
        self.saldo -= valor
        self._registrar_transacao("PAGAMENTO", -valor, descricao.strip())
        return True
    
    def obter_saldo(self) -> float:
        """
        Obtém o saldo atual da conta.
        
        Returns:
            float: Saldo atual da conta
        """
        return self.saldo
    
    def obter_extrato(self) -> List[Dict[str, Any]]:
        """
        Obtém o extrato completo da conta.
        
        Returns:
            List[Dict]: Lista de transações (mais recentes primeiro)
        """
        # Retorna uma cópia do extrato em ordem cronológica inversa
        return self.extrato[::-1]
    
    def _registrar_transacao(self, tipo: str, valor: float, descricao: str):
        """
        Registra uma transação no extrato da conta.
        
        Args:
            tipo (str): Tipo da transação
            valor (float): Valor da transação
            descricao (str): Descrição da transação
        """
        transacao = {
            'data_hora': datetime.now(),
            'tipo': tipo,
            'valor': valor,
            'descricao': descricao,
            'saldo_apos': self.saldo
        }
        self.extrato.append(transacao)
    
    def __str__(self) -> str:
        """Representação string da conta."""
        return (f"Conta {self.numero_conta} - {self.titular} "
                f"(Saldo: R$ {self.saldo:.2f})")
    
    def __repr__(self) -> str:
        """Representação técnica da conta."""
        return (f"ContaBancaria(numero={self.numero_conta}, "
                f"titular='{self.titular}', saldo={self.saldo:.2f})")
    
    def resumo(self) -> Dict[str, Any]:
        """
        Retorna um resumo da conta em formato dicionário.
        
        Returns:
            Dict: Informações principais da conta
        """
        return {
            'numero_conta': self.numero_conta,
            'titular': self.titular,
            'cpf_cnpj': self.cpf_cnpj,
            'saldo': self.saldo,
            'data_criacao': self.data_criacao,
            'total_transacoes': len(self.extrato)
        }