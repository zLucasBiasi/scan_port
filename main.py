import socket


def scan(host, ports):
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        try:
            if client.connect_ex((host, port)) == 0:
                print("[+] {} open".format(port))
        except socket.error as error:
            print("Error scanning port {}: {}".format(port, error))
        finally:
            client.close()


def get_default_ports():
    return [20, 21, 22, 23, 80, 139, 445, 443, 3389, 5800, 5900]


if __name__ == "__main__":
    host = input(
        "Coloque o host que você deseja verificar as portas ou deixe vazio para o host padrão: "
    )
    if not host:
        host = "teste.com.br"

    print("Escaneando:", host)
    answer = input("Você deseja fazer o uso de algumas portas padrões? (y/n): ").lower()

    if answer == "y":
        ports = get_default_ports()
        print("Escaneando as portas:", ports)
    elif answer == "n":
        ports_input = input("Então coloque suas portas (separadas por espaço): ")
        ports = [int(port) for port in ports_input.split()]
        print("Escaneando {} porta(s)".format(len(ports)))
    else:
        print("Resposta inválida. Saindo.")
        exit(1)

    scan(host, ports)
    print("Scan finalizado.")
