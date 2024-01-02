import yfinance as yf
import pandas as pd
import customtkinter as ctk

def obter_dividendos():
    # Obtém o ticker da ação do campo de entrada
    acao_ticker_input = entry_acao.get()

    # Adiciona ".SA" ao final do ticker pois estava dando problema fazer sem
    acao_ticker = f"{acao_ticker_input}.SA"

    # Obtém informações da ação, incluindo dados de dividendos
    acao_info = yf.Ticker(acao_ticker)

    # Busca informações de dividendos
    dividendos = acao_info.dividends

    # Busca o ano selecionado pelo usuário
    ano_selecionado = combobox_anos.get()

    # Filtra dividendos para o ano selecionado
    dividendos_ano = dividendos.loc[f'{ano_selecionado}-01-01':f'{ano_selecionado}-12-31']

    # Calcula o valor total dos dividendos
    total_dividendos = dividendos_ano.sum()

    # Adiciona o valor total ao DataFrame
    total_dividendos_df = pd.DataFrame({'Date': [f'Total Dividends ({ano_selecionado})'], 'Dividends': [total_dividendos]})
    dividendos_ano = pd.concat([dividendos_ano.reset_index(), total_dividendos_df], ignore_index=True)

    # Atualiza a caixa de texto com as informações de dividendos
    resultado_text.delete(1.0, ctk.END)
    resultado_text.insert(ctk.END, f'Dividendos para {acao_ticker} em {ano_selecionado}:\n{dividendos_ano.to_string(index=False)}')

# Configuração da janela principal
root = ctk.CTk()
root.geometry('520x350')
root.title("Consulta de Dividendos - Java Nunca Mais!")

# Rótulo e campo de entrada para o ticker da ação
label_acao = ctk.CTkLabel(root, text="Digite o ticker da ação:")
label_acao.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_acao = ctk.CTkEntry(root)
entry_acao.grid(row=0, column=1, padx=10, pady=5)

# Combobox para escolher o ano
label_ano = ctk.CTkLabel(root, text="Escolha o ano:")
label_ano.grid(row=1, column=0, padx=10, pady=5, sticky="e")
anos_disponiveis = ['2020', '2021', '2022', '2023']
combobox_anos = ctk.CTkComboBox(root, values=anos_disponiveis)
combobox_anos.grid(row=1, column=1, padx=10, pady=5, sticky="w")
combobox_anos.set('2023')  # Ano padrão

# Botão para obter os dividendos
botao_obter_dividendos = ctk.CTkButton(root, text="Obter Dividendos", command=obter_dividendos)
botao_obter_dividendos.grid(row=1, column=2, padx=10, pady=5, sticky="w")

# Caixa de texto para exibir o resultado
resultado_text = ctk.CTkTextbox(root, height=200, width=260)
resultado_text.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

# Inicia o loop principal da interface gráfica
root.mainloop()
