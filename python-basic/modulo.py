import biblioteca as bibi

if __name__ == "__main__":
    numero = int(input("digite um número: "))
    print(
        f"\n o número é {numero}, seu fatorial é {bibi.fatorial(numero)} e a sequencia de fibonacci é {bibi.fibo(numero)}")
