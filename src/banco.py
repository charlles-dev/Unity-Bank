"""
Sistema Bancário - Módulo Banco
Implementação da classe principal que gerencia múltiplas contas bancárias.
"""

from typing import Dict, List, Optional
try:
    from .conta import ContaBancaria
except ImportError:
    from conta import ContaBancaria


class SistemaBancario:
    """
    Classe principal que gerencia o sistema bancário completo.
    
    Attributes:
        contas (Dict[int, ContaBancaria]): Dicionário de contas por número
        nome_banco (str): Nome da instituição bancária
    """
    
    def __init__(self, nome_banco: str = "Banco Digital Python"):
        """
        Inicializa o sistema bancário.
        
        Args:
            nome_banco (str): Nome da instituição
        """
        self.contas: Dict[int, ContaBancaria] = {}
        self.nome_banco = nome_banco
    
    def criar_conta(self, titular: str, cpf_cnpj: str) -> ContaBancaria:
        """
        Cria uma nova conta bancária.
        
        Args:
            titular (str): Nome do titular
            cpf_cnpj (str): CPF ou CNPJ do titular
            
        Returns:
            ContaBancaria: Nova conta criada
            
        Raises:
            ValueError: Se titular ou CPF/CNPJ forem inválidos
        """
        # Valida se CPF/CNPJ já existe
        for conta in self.contas.values():
            if conta.cpf_cnpj == cpf_cnpj.strip():
                raise ValueError(f"Já existe conta para o CPF/CNPJ: {cpf_cnpj}")
        
        # Cria nova conta
        nova_conta = ContaBancaria(titular, cpf_cnpj)
        self.contas[nova_conta.numero_conta] = nova_conta
        
        return nova_conta
    
    def buscar_conta(self, numero_conta: int) -> Optional[ContaBancaria]:
        """
        Busca uma conta pelo número.
        
        Args:
            numero_conta (int): Número da conta
            
        Returns:
            ContaBancaria: Conta encontrada ou None se não existir
        """
        return self.contas.get(numero_conta)
    
    def autenticar_conta(self, numero_conta: int) -> ContaBancaria:
        """
        Autentica uma conta pelo número.
        
        Args:
            numero_conta (int): Número da conta
            
        Returns:
            ContaBancaria: Conta autenticada
            
        Raises:
            ValueError: Se a conta não existir
        """
        conta = self.buscar_conta(numero_conta)
        if not conta:
            raise ValueError(f"Conta {numero_conta} não encontrada")
        
        return conta
    
    def listar_contas(self) -> List[Dict]:
        """
        Lista todas as contas cadastradas no sistema.
        
        Returns:
            List[Dict]: Lista com informações das contas
        """
        if not self.contas:
            return []
        
        return [
            {
                'numero': conta.numero_conta,
                'titular': conta.titular,
                'saldo': conta.saldo,
                'data_criacao': conta.data_criacao.strftime("%d/%m/%Y %H:%M")
            }
            for conta in sorted(self.contas.values(), 
                              key=lambda c: c.numero_conta)
        ]
    
    def obter_estatisticas(self) -> Dict:
        """
        Obtém estatísticas gerais do sistema.
        
        Returns:
            Dict: Estatísticas do sistema bancário
        """
        if not self.contas:
            return {
                'total_contas': 0,
                'saldo_total': 0.0,
                'conta_maior_saldo': None,
                'conta_menor_saldo': None,
                'saldo_medio': 0.0
            }
        
        saldos = [conta.saldo for conta in self.contas.values()]
        conta_maior = max(self.contas.values(), key=lambda c: c.saldo)
        conta_menor = min(self.contas.values(), key=lambda c: c.saldo)
        
        return {
            'total_contas': len(self.contas),
            'saldo_total': sum(saldos),
            'saldo_medio': sum(saldos) / len(saldos),
            'conta_maior_saldo': {
                'numero': conta_maior.numero_conta,
                'titular': conta_maior.titular,
                'saldo': conta_maior.saldo
            },
            'conta_menor_saldo': {
                'numero': conta_menor.numero_conta,
                'titular': conta_menor.titular,
                'saldo': conta_menor.saldo
            }
        }
    
    def transferir_entre_contas(self, numero_origem: int, numero_destino: int,
                               valor: float, descricao: str = "Transferência") -> bool:
        """
        Realiza transferência entre duas contas do sistema.
        
        Args:
            numero_origem (int): Número da conta de origem
            numero_destino (int): Número da conta de destino
            valor (float): Valor a ser transferido
            descricao (str): Descrição da transferência
            
        Returns:
            bool: True se a transferência foi bem-sucedida
            
        Raises:
            ValueError: Se alguma conta não existir ou dados inválidos
            RuntimeError: Se não houver saldo suficiente
        """
        # Valida contas
        conta_origem = self.autenticar_conta(numero_origem)
        conta_destino = self.autenticar_conta(numero_destino)
        
        if numero_origem == numero_destino:
            raise ValueError("Não é possível transferir para a mesma conta")
        
        # Realiza transferência
        return conta_origem.transferir(conta_destino, valor, descricao)
    
    def buscar_contas_por_titular(self, nome_titular: str) -> List[ContaBancaria]:
        """
        Busca contas pelo nome do titular (busca parcial).
        
        Args:
            nome_titular (str): Nome ou parte do nome do titular
            
        Returns:
            List[ContaBancaria]: Lista de contas encontradas
        """
        nome_busca = nome_titular.lower().strip()
        contas_encontradas = []
        
        for conta in self.contas.values():
            if nome_busca in conta.titular.lower():
                contas_encontradas.append(conta)
        
        return sorted(contas_encontradas, key=lambda c: c.titular)
    
    def remover_conta(self, numero_conta: int) -> bool:
        """
        Remove uma conta do sistema (apenas se saldo for zero).
        
        Args:
            numero_conta (int): Número da conta a ser removida
            
        Returns:
            bool: True se a conta foi removida
            
        Raises:
            ValueError: Se conta não existir
            RuntimeError: Se conta tiver saldo
        """
        conta = self.autenticar_conta(numero_conta)
        
        if conta.saldo != 0:
            raise RuntimeError(
                f"Não é possível remover conta com saldo. "
                f"Saldo atual: R$ {conta.saldo:.2f}"
            )
        
        del self.contas[numero_conta]
        return True
    
    def __str__(self) -> str:
        """Representação string do sistema."""
        return f"{self.nome_banco} - {len(self.contas)} contas cadastradas"
    
    def __len__(self) -> int:
        """Retorna o número de contas no sistema."""
        return len(self.contas)