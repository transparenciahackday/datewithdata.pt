Title: Hackday – sessão #10
Date: 2011-02-26 23:21
Author: camorim
Category: Blog
Slug: hackday-sessao-10
Status: published

Depois de um longo período silencioso com arrumações do espaço à mistura para a mudança a realizar em Março, decorreu mais uma sessão Hackday.

Foi dada prioridade à revisão e reestruturação do layout do website com a informação do Parlamento pela mão da Ana e do Ricardo.

A Cláudia e o Victor dedicaram-se à questão do vocabulário/ corpus necessário ao processamento da linguagem para os discursos dos deputados na Assembleia. Depois da consulta de dois títulos e de uma conversa entre os quatro, ficou decidido utilizar o tesaurus do Eurovoc como base da categorização do conteúdo.

O que foi conseguido nesta sessão foi o download dos pdf de cada uma das áreas temáticas do Eurovoc, e à consequente conversão para html com recurso ao pdftohtml, usando o encoding UTF-8. Na linha de comandos:

```
pdftohtml ficheiro.pdf -stdout enc UTF-8 \> ficheiro.html
```

O Eurovoc está disponível quer na versão pdf quer SKOS/XML (requer registo e pedido por escrito). Cobre todas as áreas de interesse de discussão num Parlamento, serve à categorização dos textos da União Europeia e é recomendada para a indexação dos documentos dos Parlamentos nacionais. Visto tratar-se de um tesaurus, possui relações entre os descritores: termos genéricos, específicos de nível 1 e 2, termos relacionados.

No futuro próximo, iremos utilizar este vocabulário para atribuir o(s) tópico(s) adequado(s) a cada intervenção no Parlamento de forma automática. Também verificar a ocorrência de termos segundo vários critérios (ao longo do tempo, de uma legislatura, por bancada parlamentar). Os textos em pdf e html encontram-se na Dropbox na pasta transparencia.

O Victor descobriu um link que poderá vir a interessar explorar: o projecto [Projecto de Processamento de Linguagem, Text Mining & Visualização](http://pattie.fe.up.pt "Pattie, FEUP") da FEUP.

#### Títulos

-   Natural Language Processing with Python, Bird, Klein & Loper, O’Reilly, 2009
-   Python Text Processing with NLTK 2.0 Cookbook, Packt Publishing, 2010
