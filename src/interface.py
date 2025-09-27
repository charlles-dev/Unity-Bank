"""
Sistema Bancário - Interface de Usuário
Implementação da interface de linha de comando para interação com o sistema.
"""

import os
import sys
from typing import Optional
from .banco import SistemaBancario
from .conta import ContaBancaria


class InterfaceBancaria:
    """
    Interface de usuário para o sistema bancário.
    
    Attributes:
        sistema (SistemaBancario): Instância do sistema bancário
        conta_atual (ContaBancaria): Conta atualmente logada
    """
    
    def __init__(self):
        """Inicializa a interface bancária."""
        self.sistema = SistemaBancario("🏦 Banco Digital Python")
        self.conta_atual: Optional[ContaBancaria] = None
    
    def limpar_tela(self):
        """Limpa a tela do terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def pausar(self):
        """Pausa a execução até o usuário pressionar Enter."""
        input("\n📱 Pressione Enter para continuar...")
    
    def exibir_cabecalho(self, titulo: str):
        """
        Exibe cabeçalho formatado.
        
        Args:
            titulo (str): Título a ser exibido
        """
        self.limpar_tela()
        print("=" * 60)
        print(f"🏦 {self.sistema.nome_banco}")
        print("=" * 60)
        print(f"📋 {titulo}")
        print("-" * 60)
    
    def obter_numero(self, mensagem: str, min_valor: float = 0) -> float:
        """
        Obtém um número do usuário com validação.
        
        Args:
            mensagem (str): Mensagem para solicitar entrada
            min_valor (float): Valor mínimo aceito
            
        Returns:
            float: Número válido digitado pelo usuário
        """
        while True:
            try:
                valor = float(input(mensagem))
                if valor <= min_valor:
                    print(f"❌ Valor deve ser maior que {min_valor}")
                    continue
                return valor
            except ValueError:
                print("❌ Digite um número válido")
            except KeyboardInterrupt:
                print("\n👋 Operação cancelada pelo usuário")
                return 0
    
    def obter_inteiro(self, mensagem: str, min_valor: int = 0) -> int:
        """
        Obtém um número inteiro do usuário com validação.
        
        Args:
            mensagem (str): Mensagem para solicitar entrada
            min_valor (int): Valor mínimo aceito
            
        Returns:
            int: Número inteiro válido digitado pelo usuário
        """
        while True:
            try:
                valor = int(input(mensagem))
                if valor < min_valor:
                    print(f"❌ Valor deve ser maior ou igual a {min_valor}")
                    continue
                return valor
            except ValueError:
                print("❌ Digite um número inteiro válido")
            except KeyboardInterrupt:
                print("\n👋 Operação cancelada pelo usuário")
                return 0
    
    def obter_texto(self, mensagem: str, obrigatorio: bool = True) -> str:
        """
        Obtém texto do usuário com validação.
        
        Args:
            mensagem (str): Mensagem para solicitar entrada
            obrigatorio (bool): Se o campo é obrigatório
            
        Returns:
            str: Texto digitado pelo usuário
        """
        while True:
            try:
                texto = input(mensagem).strip()
                if obrigatorio and not texto:
                    print("❌ Este campo é obrigatório")
                    continue
                return texto
            except KeyboardInterrupt:
                print("\n👋 Operação cancelada pelo usuário")
                return ""
    
    def menu_principal(self):
        """Exibe o menu principal do sistema."""
        while True:
            self.exibir_cabecalho("MENU PRINCIPAL")
            
            print("1️⃣  Acessar Conta Existente")
            print("2️⃣  Criar Nova Conta")
            print("3️⃣  Listar Todas as Contas")
            print("4️⃣  Estatísticas do Sistema")
            print("0️⃣  Sair do Sistema")
            
            opcao = input("\n🎯 Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.acessar_conta()
            elif opcao == "2":
                self.criar_conta()
            elif opcao == "3":
                self.listar_contas()
            elif opcao == "4":
                self.exibir_estatisticas()
            elif opcao == "0":
                print("\n👋 Obrigado por usar o Banco Digital Python!")
                sys.exit(0)
            else:
                print("❌ Opção inválida!")
                self.pausar()
    
    def acessar_conta(self):
        """Acessa uma conta existente."""
        self.exibir_cabecalho("ACESSAR CONTA")
        
        numero_conta = self.obter_inteiro("🔑 Digite o número da conta: ", 1000)
        if numero_conta == 0:
            return
        
        try:
            self.conta_atual = self.sistema.autenticar_conta(numero_conta)
            print(f"\n✅ Bem-vindo(a), {self.conta_atual.titular}!")
            self.pausar()
            self.menu_conta()
        except ValueError as e:
            print(f"\n❌ {e}")
            self.pausar()
    
    def criar_conta(self):
        """Cria uma nova conta."""
        self.exibir_cabecalho("CRIAR NOVA CONTA")
        
        titular = self.obter_texto("👤 Nome completo do titular: ")
        if not titular:
            return
        
        cpf_cnpj = self.obter_texto("📄 CPF ou CNPJ: ")
        if not cpf_cnpj:
            return
        
        try:
            nova_conta = self.sistema.criar_conta(titular, cpf_cnpj)
            print(f"\n✅ Conta criada com sucesso!")
            print(f"📊 Número da conta: {nova_conta.numero_conta}")
            print(f"👤 Titular: {nova_conta.titular}")
            print(f"💰 Saldo inicial: R$ {nova_conta.saldo:.2f}")
        except ValueError as e:
            print(f"\n❌ {e}")
        
        self.pausar()
    
    def menu_conta(self):
        """Menu de operações da conta logada."""
        while True:
            self.exibir_cabecalho(f"CONTA: {self.conta_atual.numero_conta} - {self.conta_atual.titular}")
            print(f"💰 Saldo atual: R$ {self.conta_atual.saldo:.2f}")
            print()
            
            print("1️⃣  Depositar")
            print("2️⃣  Sacar")
            print("3️⃣  Consultar Saldo")
            print("4️⃣  Visualizar Extrato")
            print("5️⃣  Transferir Dinheiro")
            print("6️⃣  Pagar Conta")
            print("7️⃣  Resumo da Conta")
            print("0️⃣  Voltar ao Menu Principal")
            
            opcao = input("\n🎯 Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.depositar()
            elif opcao == "2":
                self.sacar()
            elif opcao == "3":
                self.consultar_saldo()
            elif opcao == "4":
                self.visualizar_extrato()
            elif opcao == "5":
                self.transferir()
            elif opcao == "6":
                self.pagar_conta()
            elif opcao == "7":
                self.resumo_conta()
            elif opcao == "0":
                self.conta_atual = None
                break
            else:
                print("❌ Opção inválida!")
                self.pausar()
    
    def depositar(self):
        """Realiza depósito na conta."""
        self.exibir_cabecalho("DEPÓSITO")
        
        valor = self.obter_numero("💵 Valor do depósito: R$ ")
        if valor == 0:
            return
        
        descricao = self.obter_texto("📝 Descrição (opcional): ", False)
        if not descricao:
            descricao = "Depósito"
        
        try:
            self.conta_atual.depositar(valor, descricao)
            print(f"\n✅ Depósito realizado com sucesso!")
            print(f"💰 Novo saldo: R$ {self.conta_atual.saldo:.2f}")
        except ValueError as e:
            print(f"\n❌ {e}")
        
        self.pausar()
    
    def sacar(self):
        """Realiza saque da conta."""
        self.exibir_cabecalho("SAQUE")
        print(f"💰 Saldo disponível: R$ {self.conta_atual.saldo:.2f}")
        
        valor = self.obter_numero("💸 Valor do saque: R$ ")
        if valor == 0:
            return
        
        descricao = self.obter_texto("📝 Descrição (opcional): ", False)
        if not descricao:
            descricao = "Saque"
        
        try:
            self.conta_atual.sacar(valor, descricao)
            print(f"\n✅ Saque realizado com sucesso!")
            print(f"💰 Novo saldo: R$ {self.conta_atual.saldo:.2f}")
        except (ValueError, RuntimeError) as e:
            print(f"\n❌ {e}")
        
        self.pausar()
    
    def consultar_saldo(self):
        """Consulta o saldo da conta."""
        self.exibir_cabecalho("CONSULTA DE SALDO")
        
        print(f"👤 Titular: {self.conta_atual.titular}")
        print(f"🔢 Conta: {self.conta_atual.numero_conta}")
        print(f"💰 Saldo atual: R$ {self.conta_atual.saldo:.2f}")
        
        self.pausar()
    
    def visualizar_extrato(self):
        """Visualiza o extrato da conta."""
        self.exibir_cabecalho("EXTRATO BANCÁRIO")
        
        extrato = self.conta_atual.obter_extrato()
        
        if not extrato:
            print("📭 Nenhuma movimentação encontrada.")
        else:
            print(f"👤 Titular: {self.conta_atual.titular}")
            print(f"🔢 Conta: {self.conta_atual.numero_conta}")
            print()
            
            for transacao in extrato[:10]:  # Mostra últimas 10 transações
                data_hora = transacao['data_hora'].strftime("%d/%m/%Y %H:%M:%S")
                tipo = transacao['tipo']
                valor = transacao['valor']
                descricao = transacao['descricao']
                saldo_apos = transacao['saldo_apos']
                
                # Formatação colorida baseada no tipo
                if valor > 0:
                    valor_str = f"+R$ {valor:.2f} ✅"
                elif valor < 0:
                    valor_str = f"R$ {valor:.2f} ❌"
                else:
                    valor_str = f"R$ {valor:.2f} ℹ️"
                
                print(f"📅 {data_hora}")
                print(f"📝 {tipo}: {descricao}")
                print(f"💵 {valor_str}")
                print(f"💰 Saldo após: R$ {saldo_apos:.2f}")
                print("-" * 40)
            
            if len(extrato) > 10:
                print(f"... e mais {len(extrato) - 10} transações")
        
        self.pausar()
    
    def transferir(self):
        """Realiza transferência para outra conta."""
        self.exibir_cabecalho("TRANSFERÊNCIA")
        print(f"💰 Saldo disponível: R$ {self.conta_atual.saldo:.2f}")
        
        numero_destino = self.obter_inteiro("🎯 Número da conta destino: ", 1000)
        if numero_destino == 0:
            return
        
        # Verifica se a conta destino existe
        try:
            conta_destino = self.sistema.autenticar_conta(numero_destino)
            print(f"✅ Conta destino encontrada: {conta_destino.titular}")
        except ValueError as e:
            print(f"\n❌ {e}")
            self.pausar()
            return
        
        valor = self.obter_numero("💵 Valor da transferência: R$ ")
        if valor == 0:
            return
        
        descricao = self.obter_texto("📝 Descrição (opcional): ", False)
        if not descricao:
            descricao = "Transferência"
        
        try:
            self.conta_atual.transferir(conta_destino, valor, descricao)
            print(f"\n✅ Transferência realizada com sucesso!")
            print(f"💰 Novo saldo: R$ {self.conta_atual.saldo:.2f}")
        except (ValueError, RuntimeError) as e:
            print(f"\n❌ {e}")
        
        self.pausar()
    
    def pagar_conta(self):
        """Realiza pagamento de conta."""
        self.exibir_cabecalho("PAGAMENTO DE CONTA")
        print(f"💰 Saldo disponível: R$ {self.conta_atual.saldo:.2f}")
        
        descricao = self.obter_texto("📝 Descrição do pagamento: ")
        if not descricao:
            return
        
        valor = self.obter_numero("💸 Valor do pagamento: R$ ")
        if valor == 0:
            return
        
        try:
            self.conta_atual.pagar_conta(valor, descricao)
            print(f"\n✅ Pagamento realizado com sucesso!")
            print(f"💰 Novo saldo: R$ {self.conta_atual.saldo:.2f}")
        except (ValueError, RuntimeError) as e:
            print(f"\n❌ {e}")
        
        self.pausar()
    
    def resumo_conta(self):
        """Exibe resumo completo da conta."""
        self.exibir_cabecalho("RESUMO DA CONTA")
        
        resumo = self.conta_atual.resumo()
        
        print(f"🔢 Número da Conta: {resumo['numero_conta']}")
        print(f"👤 Titular: {resumo['titular']}")
        print(f"📄 CPF/CNPJ: {resumo['cpf_cnpj']}")
        print(f"💰 Saldo Atual: R$ {resumo['saldo']:.2f}")
        print(f"📅 Data de Criação: {resumo['data_criacao'].strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"📊 Total de Transações: {resumo['total_transacoes']}")
        
        self.pausar()
    
    def listar_contas(self):
        """Lista todas as contas do sistema."""
        self.exibir_cabecalho("TODAS AS CONTAS")
        
        contas = self.sistema.listar_contas()
        
        if not contas:
            print("📭 Nenhuma conta cadastrada no sistema.")
        else:
            print(f"📊 Total de contas: {len(contas)}")
            print()
            
            for conta in contas:
                print(f"🔢 Conta: {conta['numero']}")
                print(f"👤 Titular: {conta['titular']}")
                print(f"💰 Saldo: R$ {conta['saldo']:.2f}")
                print(f"📅 Criada em: {conta['data_criacao']}")
                print("-" * 40)
        
        self.pausar()
    
    def exibir_estatisticas(self):
        """Exibe estatísticas do sistema."""
        self.exibir_cabecalho("ESTATÍSTICAS DO SISTEMA")
        
        stats = self.sistema.obter_estatisticas()
        
        if stats['total_contas'] == 0:
            print("📭 Nenhuma conta cadastrada no sistema.")
        else:
            print(f"📊 Total de Contas: {stats['total_contas']}")
            print(f"💰 Saldo Total do Sistema: R$ {stats['saldo_total']:.2f}")
            print(f"📈 Saldo Médio: R$ {stats['saldo_medio']:.2f}")
            print()
            
            maior = stats['conta_maior_saldo']
            print(f"🏆 Maior Saldo:")
            print(f"   🔢 Conta: {maior['numero']}")
            print(f"   👤 Titular: {maior['titular']}")
            print(f"   💰 Saldo: R$ {maior['saldo']:.2f}")
            print()
            
            menor = stats['conta_menor_saldo']
            print(f"📉 Menor Saldo:")
            print(f"   🔢 Conta: {menor['numero']}")
            print(f"   👤 Titular: {menor['titular']}")
            print(f"   💰 Saldo: R$ {menor['saldo']:.2f}")
        
        self.pausar()
    
    def executar(self):
        """Inicia a execução da interface."""
        try:
            print("🚀 Inicializando Sistema Bancário...")
            self.menu_principal()
        except KeyboardInterrupt:
            print("\n\n👋 Sistema encerrado pelo usuário. Até logo!")
        except Exception as e:
            print(f"\n💥 Erro inesperado: {e}")
            print("🔧 Entre em contato com o suporte técnico.")


def main():
    """Função principal para executar a aplicação."""
    interface = InterfaceBancaria()
    interface.executar()


if __name__ == "__main__":
    main()