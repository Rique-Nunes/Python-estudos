#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de Terminal em Python
Autor: Assistente IA
Versão: 1.0
"""

import math
import sys


class Calculadora:
    """Classe principal da calculadora com operações matemáticas."""
    
    def __init__(self):
        self.historico = []
        self.resultado_anterior = 0
    
    def adicionar_historico(self, operacao, resultado):
        """Adiciona operação ao histórico."""
        self.historico.append(f"{operacao} = {resultado}")
        self.resultado_anterior = resultado
    
    def somar(self, a, b):
        """Soma dois números."""
        resultado = a + b
        self.adicionar_historico(f"{a} + {b}", resultado)
        return resultado
    
    def subtrair(self, a, b):
        """Subtrai dois números."""
        resultado = a - b
        self.adicionar_historico(f"{a} - {b}", resultado)
        return resultado
    
    def multiplicar(self, a, b):
        """Multiplica dois números."""
        resultado = a * b
        self.adicionar_historico(f"{a} × {b}", resultado)
        return resultado
    
    def dividir(self, a, b):
        """Divide dois números."""
        if b == 0:
            raise ValueError("Erro: Divisão por zero não é permitida!")
        resultado = a / b
        self.adicionar_historico(f"{a} ÷ {b}", resultado)
        return resultado
    
    def potencia(self, base, expoente):
        """Calcula potência."""
        resultado = base ** expoente
        self.adicionar_historico(f"{base}^{expoente}", resultado)
        return resultado
    
    def raiz_quadrada(self, numero):
        """Calcula raiz quadrada."""
        if numero < 0:
            raise ValueError("Erro: Raiz quadrada de número negativo!")
        resultado = math.sqrt(numero)
        self.adicionar_historico(f"√{numero}", resultado)
        return resultado
    
    def porcentagem(self, numero, porcentagem):
        """Calcula porcentagem de um número."""
        resultado = (numero * porcentagem) / 100
        self.adicionar_historico(f"{porcentagem}% de {numero}", resultado)
        return resultado
    
    def fatorial(self, numero):
        """Calcula fatorial."""
        if numero < 0:
            raise ValueError("Erro: Fatorial de número negativo!")
        if numero > 170:
            raise ValueError("Erro: Número muito grande para calcular fatorial!")
        resultado = math.factorial(int(numero))
        self.adicionar_historico(f"{numero}!", resultado)
        return resultado
    
    def seno(self, angulo):
        """Calcula seno (em graus)."""
        radianos = math.radians(angulo)
        resultado = math.sin(radianos)
        self.adicionar_historico(f"sen({angulo}°)", resultado)
        return resultado
    
    def cosseno(self, angulo):
        """Calcula cosseno (em graus)."""
        radianos = math.radians(angulo)
        resultado = math.cos(radianos)
        self.adicionar_historico(f"cos({angulo}°)", resultado)
        return resultado
    
    def tangente(self, angulo):
        """Calcula tangente (em graus)."""
        radianos = math.radians(angulo)
        resultado = math.tan(radianos)
        self.adicionar_historico(f"tan({angulo}°)", resultado)
        return resultado
    
    def logaritmo(self, numero, base=10):
        """Calcula logaritmo."""
        if numero <= 0:
            raise ValueError("Erro: Logaritmo de número não positivo!")
        if base <= 0 or base == 1:
            raise ValueError("Erro: Base inválida para logaritmo!")
        resultado = math.log(numero, base)
        self.adicionar_historico(f"log{base}({numero})", resultado)
        return resultado
    
    def mostrar_historico(self):
        """Mostra o histórico de operações."""
        if not self.historico:
            print("📝 Histórico vazio.")
            return
        
        print("\n📝 HISTÓRICO DE OPERAÇÕES:")
        print("=" * 40)
        for i, operacao in enumerate(self.historico[-10:], 1):  # Últimas 10 operações
            print(f"{i:2d}. {operacao}")
        print("=" * 40)
    
    def limpar_historico(self):
        """Limpa o histórico."""
        self.historico.clear()
        print("🗑️  Histórico limpo!")


def mostrar_menu():
    """Exibe o menu principal da calculadora."""
    print("\n" + "="*50)
    print("🧮 CALCULADORA DE TERMINAL")
    print("="*50)
    print("OPERAÇÕES BÁSICAS:")
    print("1️⃣  Soma (+)")
    print("2️⃣  Subtração (-)")
    print("3️⃣  Multiplicação (×)")
    print("4️⃣  Divisão (÷)")
    print("\nOPERAÇÕES AVANÇADAS:")
    print("5️⃣  Potência (^)")
    print("6️⃣  Raiz Quadrada (√)")
    print("7️⃣  Porcentagem (%)")
    print("8️⃣  Fatorial (!)")
    print("\nFUNÇÕES TRIGONOMÉTRICAS:")
    print("9️⃣  Seno")
    print("🔟 Cosseno")
    print("1️⃣1️⃣ Tangente")
    print("1️⃣2️⃣ Logaritmo")
    print("\nOUTRAS OPÇÕES:")
    print("📝 h - Mostrar histórico")
    print("🗑️  c - Limpar histórico")
    print("❓ help - Ajuda")
    print("🚪 q - Sair")
    print("="*50)


def obter_numero(prompt, permitir_anterior=True):
    """Obtém um número do usuário com validação."""
    while True:
        try:
            entrada = input(prompt).strip().lower()
            
            if entrada == 'ans' and permitir_anterior:
                return calc.resultado_anterior
            elif entrada == 'q':
                print("👋 Saindo da calculadora...")
                sys.exit(0)
            else:
                return float(entrada)
        except ValueError:
            print("❌ Erro: Digite um número válido ou 'ans' para usar o resultado anterior!")
        except KeyboardInterrupt:
            print("\n👋 Saindo da calculadora...")
            sys.exit(0)


def mostrar_ajuda():
    """Mostra informações de ajuda."""
    print("\n" + "="*50)
    print("❓ AJUDA DA CALCULADORA")
    print("="*50)
    print("• Digite números normalmente (ex: 3.14, -5, 100)")
    print("• Use 'ans' para usar o resultado da operação anterior")
    print("• Use 'q' a qualquer momento para sair")
    print("• Ctrl+C também sai do programa")
    print("\nEXEMPLOS:")
    print("• Para calcular 2 + 3: escolha opção 1, digite 2, depois 3")
    print("• Para calcular 50% de 200: escolha opção 7, digite 200, depois 50")
    print("• Para usar resultado anterior: digite 'ans' quando solicitado")
    print("="*50)


def main():
    """Função principal da calculadora."""
    global calc
    calc = Calculadora()
    
    print("🎉 Bem-vindo à Calculadora de Terminal!")
    print("💡 Digite 'help' para ver a ajuda ou 'q' para sair")
    
    while True:
        try:
            mostrar_menu()
            opcao = input("\n🔢 Escolha uma opção: ").strip().lower()
            
            if opcao == 'q':
                print("👋 Obrigado por usar a calculadora! Até logo!")
                break
            elif opcao == 'h':
                calc.mostrar_historico()
                continue
            elif opcao == 'c':
                calc.limpar_historico()
                continue
            elif opcao == 'help':
                mostrar_ajuda()
                continue
            
            # Operações básicas
            if opcao == '1':  # Soma
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = calc.somar(a, b)
                print(f"✅ Resultado: {a} + {b} = {resultado}")
            
            elif opcao == '2':  # Subtração
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = calc.subtrair(a, b)
                print(f"✅ Resultado: {a} - {b} = {resultado}")
            
            elif opcao == '3':  # Multiplicação
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = calc.multiplicar(a, b)
                print(f"✅ Resultado: {a} × {b} = {resultado}")
            
            elif opcao == '4':  # Divisão
                a = obter_numero("Digite o dividendo: ")
                b = obter_numero("Digite o divisor: ")
                resultado = calc.dividir(a, b)
                print(f"✅ Resultado: {a} ÷ {b} = {resultado}")
            
            elif opcao == '5':  # Potência
                base = obter_numero("Digite a base: ")
                expoente = obter_numero("Digite o expoente: ")
                resultado = calc.potencia(base, expoente)
                print(f"✅ Resultado: {base}^{expoente} = {resultado}")
            
            elif opcao == '6':  # Raiz quadrada
                numero = obter_numero("Digite o número: ")
                resultado = calc.raiz_quadrada(numero)
                print(f"✅ Resultado: √{numero} = {resultado}")
            
            elif opcao == '7':  # Porcentagem
                numero = obter_numero("Digite o número: ")
                porcentagem = obter_numero("Digite a porcentagem: ")
                resultado = calc.porcentagem(numero, porcentagem)
                print(f"✅ Resultado: {porcentagem}% de {numero} = {resultado}")
            
            elif opcao == '8':  # Fatorial
                numero = obter_numero("Digite o número: ")
                resultado = calc.fatorial(numero)
                print(f"✅ Resultado: {int(numero)}! = {resultado}")
            
            elif opcao == '9':  # Seno
                angulo = obter_numero("Digite o ângulo em graus: ")
                resultado = calc.seno(angulo)
                print(f"✅ Resultado: sen({angulo}°) = {resultado}")
            
            elif opcao == '10':  # Cosseno
                angulo = obter_numero("Digite o ângulo em graus: ")
                resultado = calc.cosseno(angulo)
                print(f"✅ Resultado: cos({angulo}°) = {resultado}")
            
            elif opcao == '11':  # Tangente
                angulo = obter_numero("Digite o ângulo em graus: ")
                resultado = calc.tangente(angulo)
                print(f"✅ Resultado: tan({angulo}°) = {resultado}")
            
            elif opcao == '12':  # Logaritmo
                numero = obter_numero("Digite o número: ")
                base = obter_numero("Digite a base (Enter para base 10): ")
                if not base:
                    base = 10
                resultado = calc.logaritmo(numero, base)
                print(f"✅ Resultado: log{base}({numero}) = {resultado}")
            
            else:
                print("❌ Opção inválida! Digite um número de 1 a 12, ou use as opções especiais.")
            
            input("\n⏸️  Pressione Enter para continuar...")
            
        except ValueError as e:
            print(f"❌ {e}")
            input("\n⏸️  Pressione Enter para continuar...")
        except KeyboardInterrupt:
            print("\n👋 Saindo da calculadora...")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            input("\n⏸️  Pressione Enter para continuar...")


if __name__ == "__main__":
    main()