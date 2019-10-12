Title: Decifrando o Diário da Assembleia da República
Date: 2010-09-11 17:57
Author: ricardo
Category: Blog
Slug: decifrando-o-diario-da-assembleia-da-republica
Status: published
Image: http://transparencia.hacklaviva.net/wp-content/uploads/2010/09/dars.jpg

Um dos trabalhos que estamos a desenvolver no Transparência Hackday é o processamento do [Diário da Assembleia da República](http://www.parlamento.pt/DAR/Paginas/default.aspx).

Estamos, para já, a concentrar-nos na 1ª série do documento, que junta as transcrições de todas as sessões parlamentares desde 1998. Esta informação é um tesouro para cruzar informações e fazer vir ao de cima várias particularidades -- desde temas que foram discutidos, até expressões comuns. Queremos torná-la acessível através de uma base de dados simples, onde possamos cruzar as intervenções com as informações dos deputados.

O primeiro problema é que toda esta informação está disponível apenas em formato PDF no site do Parlamento, e não há forma de descarregar tudo de uma vez. Para isso, usámos a extensão [DownThemAll](https://addons.mozilla.org/firefox/addon/201) para o Mozilla Firefox de forma a poder baixar todos os links PDF que encontramos em cada página.

A partir daí, passámos a converter os ficheiros PDF para ficheiros de texto, com recurso ao comando **pdf2txt** (incluído na package poppler-utils no Ubuntu).

Depois, fizemos um script em Python para analisar os ficheiros que obtivemos, e criar um ficheiro CSV onde esteja identificado o orador, partido e o conteúdo de cada intervenção.

O script pode ser encontrado no repositório do Transparência [aqui](http://bitbucket.org/transparenciaporto/assembleia/src/tip/qdizem/).

Já existe um conjunto dos ficheiros CSV disponível [aqui](http://transparencia.hacklaviva.net/files/dar-csv.tar.bz2). Existirão ainda muitas inconsistências e erros na análise automática dos dados, já que ainda não testámos extensivamente os resultados -- testámos apenas com alguns documentos da XI Legislatura, por isso será aí o melhor sítio para começar. (Se nos quiseres ajudar, avisa-nos dos erros que encontrares nos ficheiros no [bug tracker](https://bitbucket.org/transparenciaporto/assembleia/issues/new) do Transparência.)

Agora o nosso esforço vai ser afinar pormenores no script de análise, ir actualizando o nosso arquivo de CSV's, e começar a fazer cruzamento de informação, bem como pensar em formas de análise linguística destes conteúdos.
