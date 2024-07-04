from user_agents import parse  # Importa a função parse da biblioteca user_agents para analisar strings de user agent

# Função para identificar o navegador e a versão a partir de uma string de user agent
def identificar_navegador(user_agent_string):
    # Parseia o cabeçalho do agente do usuário
    user_agent = parse(user_agent_string)
    
    # Obtém o nome do navegador e sua versão
    navegador = user_agent.browser.family
    versao = user_agent.browser.version_string
    
    return navegador, versao  # Retorna o nome do navegador e sua versão

if __name__ == "__main__":
    # Cabeçalho do agente do usuário do Chrome atualizado
    user_agent_string = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36"
    
    # Chama a função identificar_navegador com a string de user agent fornecida
    navegador, versao = identificar_navegador(user_agent_string)
    
    # Imprime o nome do navegador e sua versão
    print("Navegador:", navegador)
    print("Versão:", versao)


