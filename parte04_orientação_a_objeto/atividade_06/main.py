from models import Pessoa
from models import Conta

def main():
    print("=== INICIALIZANDO SISTEMA BANCÁRIO ===")
    
    # 1. Cria o titular da conta (Pessoa)
    titular_cliente = Pessoa(nome="João Silva", cpf="123.456.789-00")
    
    # 2. Cria a conta bancária associada ao titular
    # Passando os argumentos: titular, agencia, n_conta, saldo inicial
    conta_usuario = Conta(
        titular=titular_cliente, 
        agencia="0001", 
        n_conta="98765-4", 
        saldo="1000.0"
    )
    
    # 3. Exibe os dados iniciais na tela
    conta_usuario.consultar_dados()
    
    # 4. Realiza operações de teste
    print("\n--- Executando Movimentações ---")
    conta_usuario.depositar(500.00)
    conta_usuario.sacar(200.00)
    
    # 5. Consulta os dados atualizados pós-movimentação
    conta_usuario.consultar_dados()
    
    # 6. Gera o arquivo de texto (.txt) com o extrato (requisito do diagrama)
    conta_usuario.gerar_extrato()

if __name__ == "__main__":
     main()