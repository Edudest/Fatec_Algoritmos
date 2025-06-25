usuariosCadastrados = []
senhasUsuarios = []


def login():
    print("Digite")
    print("1 - Realizar login")
    print("2 - Realizar cadastro ")
    acao = int(input("Digite aqui: "))
    match acao:
        case 1:
            usuario = input("Digite seu usuario aqui: ")
            validar(usuario)
        case 2:
            cadastrar()


def cadastrar():
    novoUsuario = input("Digite o usuario a ser cadastrado: ")
    usuariosCadastrados.append(novoUsuario)
    senhaNovoUsuario = input("Digite a senha seu usuario: ")
    senhasUsuarios.append(senhaNovoUsuario)
    print("Usuario e senha cadastrados")
    print("====================================")
    login()


def validar(usuario):
    if usuario in usuariosCadastrados:
        usuarioLogado = usuariosCadastrados.index(usuario)
        senha = input("Digite sua senha: ")
        while True:
            if senha == senhasUsuarios[usuarioLogado]:
                print("Login realizado com sucesso!")
                return
            else:
                print("Senha incorreta")
                senha = input("Digite sua senha: ")
    else:
        print("Usuario não encontrado")
        print("====================================")
        login()


login()
