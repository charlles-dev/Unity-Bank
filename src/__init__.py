"""
Sistema Bancário Python
========================

Um sistema bancário completo implementado em Python com funcionalidades de:
- Criação e gerenciamento de contas
- Depósitos, saques e transferências
- Consulta de saldo e extrato
- Pagamento de contas
- Relatórios e estatísticas

Módulos:
    - conta: Classe ContaBancaria com operações individuais
    - banco: Classe SistemaBancario para gerenciar múltiplas contas
    - interface: Interface de usuário para interação
    - utils: Utilitários e helpers

Exemplo de uso básico:
    >>> from sistema_bancario import SistemaBancario
    >>> banco = SistemaBancario("Meu Banco")
    >>> conta = banco.criar_conta("João Silva", "123.456.789-00")
    >>> conta.depositar(1000.0)
    >>> print(f"Saldo: R$ {conta.obter_saldo():.2f}")
"""

from .conta import ContaBancaria
from .banco import SistemaBancario

__version__ = "1.0.0"
__author__ = "Sistema Bancário Python"
__all__ = ['ContaBancaria', 'SistemaBancario']