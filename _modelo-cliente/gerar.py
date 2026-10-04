#!/usr/bin/env python3
"""Gera a versão da LP do Zabaleta Milano personalizada para um cliente.

Uso:
    python3 _modelo-cliente/gerar.py "Doutor Fulano de Tal" Fulano caminho/da/foto.png

Cria a pasta <nome-do-cliente>/ na raiz do repositório com o index.html e a
foto do cliente na piscina (img/foto-cliente.jpg). Depois é só fazer commit
e push: o link fica em
https://rodrigomaysonnave.github.io/lancamento-zabaleta/<nome-do-cliente>/

A pasta _modelo-cliente/ começa com "_", então o GitHub Pages não a publica.
"""
import os, re, sys, unicodedata, urllib.parse

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)


def pasta_do_nome(nome):
    # "Doutor Fulano de Tal" -> "fulano-de-tal" (sem o tratamento na frente)
    nome = re.sub(r'^(doutora?|dra?\.?|senhora?|sra?\.?)\s+', '', nome.strip(), flags=re.I)
    nome = unicodedata.normalize('NFKD', nome).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', nome.lower()).strip('-')


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    nome, nome_curto, foto = sys.argv[1:]
    pasta = pasta_do_nome(nome)
    destino = os.path.join(RAIZ, pasta)
    if os.path.exists(destino):
        sys.exit(f'A pasta {pasta}/ já existe. Apague ou escolha outro nome.')

    html = open(os.path.join(AQUI, 'modelo.html'), encoding='utf-8').read()
    html = (html.replace('{{NOME_URL}}', urllib.parse.quote(nome))
                .replace('{{NOME_CURTO}}', nome_curto)
                .replace('{{NOME}}', nome)
                .replace('{{PASTA}}', pasta))
    assert '{{' not in html, 'sobrou marcador sem preencher no modelo'

    from PIL import Image  # pip install pillow
    os.makedirs(os.path.join(destino, 'img'))
    img = Image.open(foto).convert('RGB')
    if img.width > 1600:
        img = img.resize((1600, round(img.height * 1600 / img.width)))
    img.save(os.path.join(destino, 'img', 'foto-cliente.jpg'), quality=86, optimize=True, progressive=True)
    open(os.path.join(destino, 'index.html'), 'w', encoding='utf-8').write(html)

    print(f'Pronto: {pasta}/')
    print(f'Link: https://rodrigomaysonnave.github.io/lancamento-zabaleta/{pasta}/')


if __name__ == '__main__':
    main()
