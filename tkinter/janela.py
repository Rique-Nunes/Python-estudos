import tkinter as tk

# instanciar janela
janela = tk.Tk()
janela.title("Primeiro App")
janela.geometry("300x100+20+20")

# criar e posicionar um label com a mensagem
lblmsg = tk.Label(janela, text="Ola mundo!")
lblmsg.pack()

# exibir janela
janela.mainloop()
