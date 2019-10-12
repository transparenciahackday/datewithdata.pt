Title: Hackday - sessão #1
Date: 2010-07-17 14:46
Author: admin
Category: Blog
Tags: Hackday
Slug: hello-world
Status: published

A primeira sessão de trabalho do hackday transparencia serviu para partilhar algumas coisas que cada um de nós já tinhamos feito e perceber de que forma nos podemos integrar nos diferentes projectos possíveis.

Neste momento há dois caminhos a ser explorados, ambos a partir da informação disponivel online no site da [assembleia da republica](http://www.parlamento.pt/).

O primeiro tem como objectivo disponibilizar de uma forma mais interessante os dados do Diario da Assembleia da Republica. Para quem não conhece este diário tem a transcrição de tudo quanto é dito na AR.  
A ideia é disponibilizar esses dados num formato não proprietário e acrescentar uma camada de informação que permita responder a perguntas como o que disse o deputado xxx sobre o tema yyy.  
Claro que depois se podem construir também algumas coisas giras como o medidor de muito bens (sim essas afirmações também estão nesse diário da assembleia da republica).

O segundo tem como objectivo permitir explorar a informação dos deputados e suas actividades, informação essa que está nestas páginas.  
Neste momento embora essa informação esteja toda online não existe nenhum interface que permita responder a questões como:  
– qual o deputado com mais intervenções?  
– como tem evoluido a representação das profissões ao longo das legislaturas, ou seja, provavelmente achamos que a a.r. é essencialmente constituida por pessoas ligadas à advocacia e similares mas será que é mesmo assim, e como tem variado?  
– qual a legislatura com a idade média dos deputados mais alta? como tem variado? será que neste orgão também se nota aquilo que se diz de as novas gerações não estarem interessadas na participação pública?

O ricardo que está a trabalhar no primeiro projecto já desenvolveu um script que descarrega um diário, converte-o de pdf para txt e “anota-o” com alguma informação especifica para percebermos por exemplo onde estão os nomes dos deputados.  
Falta-nos perceber ainda de que forma e que tipo de anotações vale a pena incluir nesse txt e se o convertemos para outro formato e claro saber depois como exploramos essa informação.  
Uma ideia interessante seria por exemplo ter uma coisa parecida com o verbatim para explorar as citações dos deputados.  
Esta área da exploração de texto livre é bastante desconhecida para mim que estou mais habituado a dados mais sistematizados como tabelas relacionais e afins por isso se quiserem contribuir com ideias estão à vontade.

Eu e a claudia estivemos a trabalhar no segundo projecto principalmente na parte da extracção de dados do site da a.r. Fizemos um pequeno scraper que aproveita o facto de as páginas da a.r. estarem construidas de tal forma que nem precisamos de nos perder em regular expressions e afins.  
É um script bem comportado que faz propositadamente um número reduzido de pedidos por minuto e que extrai essa informação uma base de dados MySQL.  
O objectivo é criar algo (feeds ou outros) que permita que outras equipas trabalhem essa informação.  
Ficou a ideia de explorar o yahoo pipes para tentar fazer o mesmo processo de uma forma mais simples.

O tiago e o victor estiveram a ver como se poderia utilizar plugins drupal para explorar a informação dos deputados do segundo projecto. A ideia é reinventar o menos possivel.

A ana para além de criar o blog esteve também a fazer umas primeiras experiências com os dados que já extraimos dos deputados. Para isso criou uma tagcloud com as profissões indicadas dos deputados. Percebemos que vamos ter que ter algum processo de limpeza ou normalização da própria informação para evitar por exemplo situações de profissões que aparecem em duplicado por causa da forma como estão escritas.
