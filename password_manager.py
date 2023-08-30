import secrets

def generate_password(length=12):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()_+-=[]{}|;:,.<>?~"
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def save_passwords(passwords):
    with open('passwords.txt', 'w') as file:
        for site, password in passwords.items():
            file.write(f"{site}: {password}\n")

def main():
    passwords = {}

    while True:
        print("Gerador de Senhas e Gerenciador")
        print('1. Gerar Senha')
        print("2. Armazenar Senha")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            length = int(input("Digite o comprimento da senha desejada: "))
            password = generate_password(length)
            print("Senha gerada:", password)

        elif choice == '2':
            site = input("Digite o nome do site ou serviço: ")
            password = input("Digite a senha a ser armazenada: ")
            passwords[site] = password
            save_passwords(passwords)
            print("Senha armazenada com sucesso")

        elif choice == '3':
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
