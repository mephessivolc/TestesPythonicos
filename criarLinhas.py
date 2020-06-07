
with open('criarLinhas.txt', 'w') as file_txt:
    text = ""
    for i in range(1,81):
        text = text + "{}& & &  \\\\ \hline\n".format(i)

    file_txt.write(text)
