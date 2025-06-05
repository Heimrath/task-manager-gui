import customtkinter as ctk

lista_tarefas = []
frame_rolavel_tarefas = None


def adicionar_tarefa():
    texto_tarefa = campo_entry_tarefa.get().strip()
    texto_data = campo_entry_data.get().strip()

    global lista_tarefas

    if not texto_tarefa:
        resultado.configure(text="É necessário inserir uma tarefa.", text_color="red") # Configura uma mensagem de erro caso tarefa seja vazia
        return # Sai da função se a tarefa estiver vazia
    else:
        resultado.configure(text="Tarefa adiciona com sucesso!", text_color="green")

    tarefa_adicionada = f"{texto_tarefa}"
    if texto_data: # Adiciona a data apenas se ela foi fornecida
        tarefa_adicionada += f" - Data: {texto_data}"
    
    lista_tarefas.append(tarefa_adicionada)

    # Limpa os campos de entrada após adicionar a tarefa
    campo_entry_tarefa.delete(0, "end")
    campo_entry_data.delete(0, "end")

    campo_entry_tarefa.focus()

    atualizar_frame_tarefas()


def atualizar_frame_tarefas(): 
    global frame_rolavel_tarefas # Permite alterar a variavel global 

    # Remove todos os widgets (labels de tarefas antigas) de dentro do frame_rolavel_tarefas
    for widget in frame_rolavel_tarefas.winfo_children():
        widget.destroy()
    
    # Verifica se há tarefas na lista de taredas
    if not lista_tarefas:
        tarefas_vazias = ctk.CTkLabel(frame_rolavel_tarefas, text="Não há tarefas pendentes!", font=("Arial", 12))
        tarefas_vazias.pack(pady=(15,2), padx=20, fill="x")
    else:
        for i, item_lista in enumerate(lista_tarefas):
            mostrar_tarefas = ctk.CTkLabel(frame_rolavel_tarefas, text=f"{i+1}. {item_lista}", font=("Arial", 14))
            mostrar_tarefas.pack(pady=(15, 2), padx=20, anchor="w")


# --- Bind da tecla Enter para adicionar tarefa ---
# Cria uma função intermediária para chamar adicionar_tarefa_action
# pois o bind passa um argumento 'event' que nossa função pode ignorar.
def on_enter_key_pressed(event):
    adicionar_tarefa()

    
# Configuração da aparência
ctk.set_appearance_mode('dark')

# Criação da janela principal
app = ctk.CTk()
app.title("Gerenciador de tarefas")
app.geometry('500x500')

# Criação dos campos
# Label
campo_tarefa = ctk.CTkLabel(app, text="Tarefa*", font=("Arial", 14))
campo_tarefa.pack(pady=(15,2), padx=20, anchor="w")

# Entry
campo_entry_tarefa = ctk.CTkEntry(app, placeholder_text="Digite sua tarefa", font=("Arial", 14))
campo_entry_tarefa.pack(pady=(0,10), padx=20,fill="x")

# Label
campo_data = ctk.CTkLabel(app, text="Data", font=("Arial", 14))
campo_data.pack(pady=(15, 2), padx=20, anchor="w")

# Entry
campo_entry_data = ctk.CTkEntry(app, placeholder_text="Digite a data: DD/MM/AAAA", width=200, font=("Arial", 14))
campo_entry_data.pack(pady=(0,10), padx=20,fill="x")

# Button
botao_adicionar = ctk.CTkButton(app, text="Adicionar", command=adicionar_tarefa, font=("Arial", 14))
botao_adicionar.pack(pady=(0,10), padx=20,fill="x")

mensagem = ctk.CTkLabel(app, text="* campo obrigatório", font=("Arial", 10))
mensagem.pack(pady=(0,10), padx=20, anchor="w")

resultado = ctk.CTkLabel(app, text='', font=("Arial", 14))
resultado.pack(pady=(0, 2), padx=20)

# Bind que chama a função para adicionar a tarefa ao apertar Enter
campo_entry_tarefa.bind("<Return>", on_enter_key_pressed) 
campo_entry_data.bind("<Return>", on_enter_key_pressed)

# ----- Exibição da tarefas na parte de baixo ------
# Frame Rolável para exibir a lista de tarefas
frame_rolavel_tarefas = ctk.CTkScrollableFrame(app, height=200)
# fill="both" faz ocupar largura e altura, expand=True permite expandir se a janela crescer
frame_rolavel_tarefas.pack(pady=(0, 10), padx=20, fill="both", expand=True)

# Iniciar aplicação
atualizar_frame_tarefas()
app.mainloop()
