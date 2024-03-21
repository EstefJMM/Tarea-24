import requests, os, bs4

def valida(url):
    if url.startswith("http://") or url.startswith("https://"):
        return url
    else:
        return "http://" + url
    
def procesa(dameURL):
    os.makedirs('Image', exist_ok=True)
    os.makedirs('pdfs', exist_ok=True)
    print('Descarga de %s...' % dameURL)
    print('Comienza descarga...')
    res = requests.get(dameURL)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    
    imagenes = soup.find_all('img')
    if imagenes == []:
        print('Sin imagen.')
    else:
        for img in imagenes:
            imgUrl = img.get('src')
            if imgUrl.startswith("http"):
                print('Descarga %s...' % (imgUrl))
                response = requests.get(imgUrl)
                if response.status_code == 200:
                    imageFile = open(os.path.join('Image', os.path.basename(imgUrl)),'wb')
                    for chunk in response.iter_content(100000):
                        imageFile.write(chunk)
                    imageFile.close()
                    print('Fin de descarga de imagen')
            else:
                print('Descarga %s...' % (imgUrl))
                imgUrl = url_nueva + imgUrl
                response = requests.get(imgUrl)
                if response.status_code == 200:
                    imageFile = open(os.path.join('Image', os.path.basename(imgUrl)),'wb')
                    for chunk in response.iter_content(100000):
                        imageFile.write(chunk)
                    imageFile.close()
    
    vinculos = soup.find_all('a')
    with open("hipervinculos.txt", "w") as f:
        for hi in vinculos:
            link = hi.get("href")
            if link:
                f.write(link + "\n")
        print(' ')
        print(' ')
        print('Guardando Vinculos...')
        print("Vinculos guardados")
        print(' ')
    
    pdfs = soup.find_all('a')
    for p in pdfs:
        if ('.pdf' in p.get('href', [])):
            response = requests.get(p.get('href'))
            nombre = p.get('href')
            pdf = open(os.path.join('pdfs', os.path.basename(nombre)), 'wb')
            pdf.write(response.content)
            pdf.close()
            print("archivo ", nombre , " Fin de descarga de Pdf")
    print(' ')
    print("Pdfs guardados")
    






