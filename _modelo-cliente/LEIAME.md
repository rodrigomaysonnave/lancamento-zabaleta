# Modelo da LP personalizada por cliente

Layout aprovado no teste com o Doutor Marcos Zabaleta, em 04/10/2026. Esta
pasta não vai ao ar: o GitHub Pages ignora pastas que começam com `_`.

## O que a versão do cliente tem

- **Abertura** igual à da LP principal, já com o nome **Zabaleta Milano**.
- **Seção logo abaixo da abertura**, com "Apresentação exclusiva para", o nome
  do cliente em destaque e o texto: *"{nome curto}, preparamos esta
  apresentação para você conhecer o Zabaleta Milano antes do lançamento
  oficial. Você vai conhecer o que já está definido no projeto e uma surpresa
  que pensamos especialmente para você."*
- **Seção "Imaginamos esse momento para você"**, logo depois da galeria do
  empreendimento, com a foto do cliente na piscina do rooftop.
- **Botões do WhatsApp** com a mensagem "Olá Rodrigo, aqui é o {nome}…" e o
  formulário já preenchido com o nome.
- **Prévia do link** com a imagem aérea da abertura, para não revelar a foto
  antes da hora, e com o título "{nome}, o Zabaleta Milano foi apresentado
  primeiro a você".
- **Fora do Google** (`noindex`).

## Como gerar

```bash
python3 _modelo-cliente/gerar.py "Doutor Fulano de Tal" Fulano caminho/da/foto.png
git add fulano-de-tal && git commit -m "LP personalizada: Doutor Fulano de Tal" && git push
```

Para que a prévia saia atualizada no WhatsApp, mande o link com `?v=1` no final.
