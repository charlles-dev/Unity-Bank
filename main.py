#!/usr/bin/env python3
"""
Sistema Bancário Digital - Aplicação Principal
==============================================

Um sistema bancário completo desenvolvido em Python seguindo princípios de
engenharia de software e modelagem UML.

Este projeto implementa:
- Requisitos funcionais bem definidos (RF01-RF12)
- Diagrama de casos de uso completo
- Implementação orientada a objetos
- Interface de usuário intuitiva
- Testes automatizados
- Documentação abrangente

Para executar:
    python main.py

Ou:
    python -m sistema_bancario.main

Autor: Charlles Augusto
Versão: 1.0.0
"""

import sys
import os

# Adiciona o diretório src ao path para permitir importações
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from src.interface import main
    
    if __name__ == "__main__":
        print("\n"
              "╔══════════════════════════════════════════════════════════════╗\n"
              "║                    🏦 SISTEMA BANCÁRIO DIGITAL               ║\n"
              "║                         Python Edition                       ║\n"
              "╠══════════════════════════════════════════════════════════════╣\n"
              "║  Desenvolvido seguindo princípios de Engenharia de Software  ║\n"
              "║                                                              ║\n"
              "║  ✅ Requisitos Funcionais Completos                          ║\n"
              "║  ✅ Diagrama de Casos de Uso                                 ║\n"
              "║  ✅ Implementação Orientada a Objetos                        ║\n"
              "║  ✅ Interface de Usuário Intuitiva                           ║\n"
              "║  ✅ Testes Automatizados                                     ║\n"
              "║  ✅ Documentação Técnica                                     ║\n"
              "╚══════════════════════════════════════════════════════════════╝\n"
              "\n"
              "🚀 Inicializando sistema...\n")
        main()
        
except ImportError as e:
    print(f"""
❌ Erro de Importação: {e}

🔧 Soluções:
1. Certifique-se de estar no diretório correto
2. Verifique se todos os arquivos estão presentes:
   - src/conta.py
   - src/banco.py
   - src/interface.py
   - src/__init__.py

📁 Estrutura esperada:
sistema_bancario/
├── main.py
├── src/
│   ├── __init__.py
│   ├── conta.py
│   ├── banco.py
│   └── interface.py
├── tests/
├── docs/
└── README.md
""")
    sys.exit(1)

except Exception as e:
    print(f"""
💥 Erro inesperado: {e}

🔧 Entre em contato com o suporte técnico ou verifique os logs.
""")
    sys.exit(1)