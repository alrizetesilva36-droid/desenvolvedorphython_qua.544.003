import os
import math

def limpar_terminal():
    """Limpa a tela do terminal de forma multiplataforma."""
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_potencia(base, expoente):
    """Retorna a base elevada ao expoente."""
    return base ** expoente

def calcular_raiz_quadrada(numero):
    """Retorna a raiz quadrada de um número. Retorna None se for negativo."""
    if numero < 0:
        return None
    return math.sqrt(numero)

def volume_paralelepipedo(comprimento, largura, altura):
    """Calcula o volume de um paralelepípedo (C x L x A)."""
    return comprimento * largura * altura

def volume_cilindro(raio, altura):
    """Calcula o volume de um cilindro (pi * r² * h)."""
    return math.pi * (raio ** 2) * altura


    