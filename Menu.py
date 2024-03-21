import Codigo

def menu():
    url = input("Ingresa una URL: ")
    dameURL = Codigo.valida(url)
    html = Codigo.procesa(dameURL)
    print(html)
if __name__=='__main__':
    menu()
