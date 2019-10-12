Title: Como usar o serviço informacaoDeputado
Date: 2010-08-08 14:47
Author: vsilva
Category: Blog
Tags: deputados, opendata, opengov, portugal, recursos, transparência
Slug: como-usar-o-servico-informacaodeputado
Status: published

Por enquanto o serviço informacaoDeputado está disponivel em <http://www.oportoemconversa.com/datagovpt/informacaoDeputado.php> e permite obter ficheiros CSV com a informação que é disponibilizada no site da Assembleia da República na página referente à [biografia dos deputados](http://www.parlamento.pt/DeputadoGP/Paginas/Biografia.aspx?BID=4202).

Para conseguirem executar os exemplos seguintes têm que [me contactar](http://twitter.com/vitorsilva) para eu vos fornecer uma chave de acesso.

Para já temos 5 opções principais:

-   **MP** – informação base sobre os deputados
-   **Caucus** – indicação de todas as legislaturas [AR](http://www.transparenciahackday.org/2010/07/%ef%bb%bf%ef%bb%bf%ef%bb%bf%ef%bb%bfestatisticas-da-ar/) a que um deputado pertenceu
-   **CaucusInfo** – ids [cheap nfl jerseys](http://www.cheapjerseysgest.com) das legislaturas. necessario [Rights](http://dundalksimon.ie/human-rights/) para saber o que colocar em alguns filtros
-   **FactsType** – tipos de factos [PROTEIN](http://lemonbody.com/protein-how-much-do-i-really-need/) disponiveis. necessario para saber o [Choice](http://www.mrhomiec.com/e3-playstation-4-launch-game-of-choice/) que colocar em alguns filtros
-   **Facts** – informação base sobre os “factos” dos deputados

**CaucusInfo**

-   devolve os ids das legislaturas e as datas de vigência
-   http://www.oportoemconversa.com/datagovpt/informacaoDeputado.php?key=aTuaChave&opcao=CaucusInfo

![](http://transparencia.hacklaviva.net/wp-content/uploads/2010/08/CaucusInfo.png "CaucusInfo")

**FactsType**

-   devolve os nomes dos tipos de factos que podemos usar
-   http://www.oportoemconversa.com/datagovpt/informacaoDeputado.php?key=aTuaChave&opcao=FactsType

![](http://transparencia.hacklaviva.net/wp-content/uploads/2010/08/factstype.png "factstype")


**MP**

-   devolve a informação base do deputado, [cheap jerseys](http://www.sanfrancisco49ersjerseyspop.com) id, nome, data de nascimento, profissão
-   Filtros: legislatura – se não quisermos todos os deputados podemos indicar a legislatura que pretendemos
-   http://www.oportoemconversa.com/datagovpt/informacaoDeputado.php?key=aTuaChave&opcao=MP
-   http://www.oportoemconversa.com/datagovpt/informacaoDeputado.php?key=aTuaChave&opcao=MP&legislatura=XI

![](http://transparencia.hacklaviva.net/wp-content/uploads/2010/08/mp.png "mp")


**Caucus**

-   devolve a [cheap nfl jerseys](http://www.cheapjerseysgests.com) informação [cheap nfl jerseys](http://www.cheapnfljerseyslan.com) das legislaturas [Post](http://www.bkgr.se/art/slider-post/) a que um deputado pertenceu: id, id legislatura, [–](http://www.transparenciahackday.org/2010/07/hello-world/) data legislatura, distrito pelo qual concorreu, partido pelo qual concorreu, indicação se tem informação de actividade e de registo de interesses
-   Filtros: legislatura – se não quisermos todos os [resposta](http://www.transparenciahackday.org/2010/07/perguntas-a-que-dar-resposta/) deputados podemos indicar a legislatura que pretendemos
-   http://www.oportoemconversa.com/datagovpt/informacaoDeputado.php?key=aTuaChave&opcao=Caucus
-   http://www.oportoemconversa.com/datagovpt/informacaoDeputado.php?key=aTuaChave&opcao=Caucus&legislatura=XI

![](http://transparencia.hacklaviva.net/wp-content/uploads/2010/08/caucus.png "caucus")

**Facts**

-   os factos representam a informação dos deputados, por exemplo habilitações [cheap nba jerseys](http://www.cincinnatibengalsjerseyspop.com) literárias
-   Filtros: legislatura – se não quisermos todos os deputados podemos indicar a legislatura que pretendemos; mpid – se não quisermos a informação de todos os deputados
-   http://www.oportoemconversa.com/datagovpt/informacaoDeputado.php?key=aTuaChave&opcao=Facts
-   http://www.oportoemconversa.com/datagovpt/informacaoDeputado.php?key=aTuaChave&opcao=Facts&legislatura=I
-   http://www.oportoemconversa.com/datagovpt/informacaoDeputado.php?key=aTuaChave&opcao=Facts&legislatura=I&mpid=18

<div>

![](http://transparencia.hacklaviva.net/wp-content/uploads/2010/08/facts.png "facts")


