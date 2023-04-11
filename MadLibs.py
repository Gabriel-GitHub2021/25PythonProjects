# Concatenação de String (Unir duas ou mais strings)
# Exemplo: "Se inscreva no canal _____________."
# youtuber = 'FreeCodeCamp'
# Algumas formas de fazê-lo;
# print("Inscreva-se no canal " + youtuber)
# print("Inscreva-se no canal {}".format(youtuber))
# print(f"Inscreva-se no canal {youtuber}")

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
famoso = input("Pessoa famosa: ")

madlib = f"Programação é tão {adj}! Programar me deixa animado o tempo inteiro porque " \
         f"eu amo {verbo1}. Se mantenha hidratado e {verbo2} como se você fosse um {famoso}!"

print(madlib)