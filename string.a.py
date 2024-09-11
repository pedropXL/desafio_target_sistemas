def count_letter_a(string):
    lower_string = string.lower()
    
    count = lower_string.count('a')
    
    if count > 0:
        print(f"A palavra {palavra} possui a letra 'a' e ela aparece {count} vez(es) na string.")
    else:
        print("A palavra {palavra} não possui a letra 'a'.")

palavra = input("Digite uma string: ")

count_letter_a(palavra)
