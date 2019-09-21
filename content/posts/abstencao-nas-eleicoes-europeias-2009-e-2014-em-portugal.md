Title: Abstenção nas eleições europeias 2009 e 2014, em Portugal
Date: 2014-06-21 23:04
Author: Ana
Category: Blog
Tags: eleições, estatísticas oficiais, europa, infografia, portugal
Slug: abstencao-nas-eleicoes-europeias-2009-e-2014-em-portugal
Status: published

[![abstencao\_final-03](http://www.transparenciahackday.org/wp-content/uploads/2014/06/abstencao_final-03-e1403389307433-1010x1024.png){.alignnone .size-large .wp-image-672 width="584" height="592"}](http://www.transparenciahackday.org/wp-content/uploads/2014/06/abstencao_final-03.png)

No Hackday de maio formou-se um grupo de trabalho à volta das eleições europeias.  
A duas semanas das eleições, entre as campanhas dos partidos e as campanhas de apelo à participação, a [Sara](http://twitter.com/saritamoreira) lançou para a mesa uma ideia para uma infografia onde mostrássemos os resultados de 2009 e 2014, contabilizando e destacando a abstenção. Parte da motivação para esta infografia partia também da recolha de dados eleitorais que começamos no [Hackday de abril](http://www.transparenciahackday.org/2014/04/12-de-abril-especial-transparencia-hackday-dados-eleitorais/ "12 de Abril: Especial Transparência Hackday Dados Eleitorais"), dedicado ao tema das eleições e organizado em parceria com a [EPSIplatform](http://epsiplatform.eu/ "EPSI Platform").

O entusiasmo animou-nos. Era um projeto aparentemente rápido e descomplicado que lançaríamos uns dias depois das eleições, mal os resultados se encontrassem disponíveis.  
Criámos uma folha de cálculo colaborativa e começamos a recolher os resultados das eleições europeias de 2009 para os vários países da União Europeia, recalculando os valores para incluir a percentagem de abstenção.

Estavamos quatro com as mãos na massa: a Sara, a liderar a buscas de dados; eu, a ajudar com a recolha; o Bernardo, a harmonizar os dados e a criar um parser para recalcular os totais com a abstenção (facilitando o trabalho duro dos re-cálculos manuais); e a Mariana, a executar a infografia;

[![Screenshot from 2014-06-21 16:14:52](http://www.transparenciahackday.org/wp-content/uploads/2014/06/Screenshot-from-2014-06-21-161452-150x150.png){.alignleft .size-thumbnail .wp-image-656 width="150" height="150"}](http://www.transparenciahackday.org/wp-content/uploads/2014/06/Screenshot-from-2014-06-21-161452.png) Mais uma vez o problema da descentralização dos dados veio dar-nos uma bofetada de luva branca. Com uma dezenas de sites abertos acabamos por encontrar informação consistente, embora dispersa em páginas diferentes, no site do [Parlamento Europeu](http://www.europarl.europa.eu/aboutparliament/en/00082fcd21/Results-by-country-%282009%29.html?tab=22 "European Parliament, Election Results 2009") e, [as abstenções](https://en.wikipedia.org/wiki/European_elections,_2009#Results "European_elections 2009, Results"), na Wikipedia. Esperávamos recolher os dados dos resultados em Portugal no site da CNE mas, por uma razão que desconhecemos, o dataset das europeias 2009 não está disponível.

O template para a infografia foi desenhado enfatizando a abstenção (enorme) e com um layout compacto, pensado para a partilha do gráfico nas redes sociais. Tínhamos tudo a postos para, a seguir às eleições, recolher os dados, integrar os resultados na infografia e lançar. Quase um mês depois das eleições publicámos finalmente a infografia e algumas conclusões das desventuras do processo.

------------------------------------------------------------------------

**Dados em harmonia**

Recolher os resultados de 2014 e harmonizar a informação com a de 2009 revelou-se uma tarefa titânica. Qual foi então o entrave que nos levou a adiar? Bem, em primeiro gestão de trabalho coletivo à distância! Pois é, o Hackday é um espaço ótimo em que sabemos que temos um determinado número de horas em que nos podemos dedicar ao amor pelos dados abertos. Por experiência, sabemos que entre Hackdays é muito mais difícil encontrar o tempo para voltar aos projetos. A coordenação dos esforços, por email, também foi complicada. Não há nada como encontrar as pessoas e discutir tarefas frente a frente, com um bloco de notas e um café na mão.

Voltando aos dados, recorremos ao [site do Parlamento Europeu dedicado às eleições de 2014](http://www.resultados-eleicoes2014.eu/pt/election-results-2014.html "Eleições Europeias 2014 - EU"), como fonte primária e fiável. Encontramos um senão: os resultados que publicaram não incluiam os valores dos votos brancos e nulos. Disponibilizavam apenas as percentagens dos votos válidos, sem mostrar os números totais dos votos e da participação real nas eleições. Além disso, a nota "dados provisórios" e o facto de a soma das percentagens, por país, não perfazer os 100% exatos deixaram-nos incertos quanto à fiabilidade. Voltámos a deparar-nos com a falta de uniformidade dos dados —  alguns países não tinham informação disponível sobre a quantidade de votos brancos e nulos, outros tinham mas em conjunto, e outros em separado —  e a dificuldade de reunir um dataset de resultados completo e fidedigno.

Assim, decidimos voltar-nos novamente para a fiel Wikipedia e reduzir o âmbito desta infografia aos [resultados das europeias em Portugal](http://pt.wikipedia.org/wiki/Elei%C3%A7%C3%B5es_parlamentares_europeias_de_2014_%28Portugal%29#Resultados "Resultados das Eleições Parlamentares Europeias de 2014 Portugal"). A redução foi sobretudo uma decisão pragmática para podermos publicar a infografia e avançar com outras que temos em mente.

------------------------------------------------------------------------

**Visões dos resultados de 2014**

[![percentagens reais](http://www.transparenciahackday.org/wp-content/uploads/2014/06/percentagens-reais-150x150.jpg){.alignleft .size-thumbnail .wp-image-655 width="150" height="150"}](http://www.transparenciahackday.org/wp-content/uploads/2014/06/percentagens-reais.jpg) Logo depois das eleições vimos publicadas uma série de notícias sobre os resultados. Algumas falavam da [abstenção](http://sicnoticias.sapo.pt/especiais/europeias2014/2014-05-26-votos-brancos-e-nulos-somam-745-ligeira-subida-face-a-2009 "Votos brancos e nulos somam 7,45%, ligeira subida face a 2009 "), enorme e incontornável, mas nenhuma delas mostrava a visão dos dados que finalmente aqui publicamos (com exceção desta imagem que encontramos partilhada no facebook, menos completa, mas numa linha de pensamento próxima). Ao mesmo tempo, encontramos inconsistências nos resultados publicados. Aqui ficam, por exemplo, as análises do [Público](http://www.publico.pt/europeias-2014 "Público: Europeias 2014") e [Sic Notícias](http://sicnoticias.sapo.pt/Infografias/2014-05-25-eleicoes-europeias-resultados-nacionais "Eleições Europeias, Resultados Nacionais 2014").

Por esta altura o tema das eleições já perdeu o seu momentum, quer nos media e quer nas redes sociais. No entanto, se encaramos o assunto do ponto de vista dos dados abertos, a infografia continua a abordar dados interessantes para análise. O esforço levou-nos a reunir um dataset completo dos resultados das eleições europeias de 2009 e 2014, em Portugal, que não encontramos disponível em mais lado nenhum.

Aqui ficam os datasets da infografia: [portugal-europeias2009.csv](http://transparenciahackday.org/wp-content/uploads/2014/portugal-europeias2009.csv) e [portugal-europeias2014.csv](http://transparenciahackday.org/wp-content/uploads/2014/portugal-europeias2014.csv).

Que venham mais dados abertos e mais leituras sobre o tema das eleições!
