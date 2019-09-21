Title: Hackday - sessão #9
Date: 2011-01-10 14:01
Author: camorim
Category: Blog
Slug: hackday-sessao-9
Status: published

Todo o passado sábado, dia 8 de Janeiro, foi dedicado a uma longa sessão do Transparência Hackday. Serviu o encontro para ponderar uma série de aspectos ligados ao projecto em curso e ainda avançar nalguns pontos.

**Legalidades**  
As questões de uso da informação do [parlamento.pt](http://parlamento.pt/) e logos dos partidos mereceu alguma troca de pontos de vista. No primeiro caso, a dúvida foi suscitada por eventuais restrições na distribuição. Porém, a situação não parece conter em si qualquer obstáculo, já que o copyright parece estar circunscrito a serigrafias e livros.  
Quanto aos logos dos partidos, poder-se-á substituir a exibição de logos por cores até haver autorização para o seu uso.

**Website**  
A plataforma que reúne informação já recolhida e permite a pesquisa e consulta já está bastante adiantada, tendo dado lugar a uma breve apresentação para comentar aspectos a melhorar e estudar novas melhorias.  
Uma das preocupações na sua construção foi a economia de cliques, daí o utilizador ter de fazer no máximo 3 cliques para chegar a informação substancial.

-   Notícias - Na página de cada deputado existe um quadro com as notícias referentes ao mesmo, tendo-se usado para o efeito a API do Google News. Acontece que alguns nomes são tão comuns que é complicado filtrar o que efectivamente diz respeito ao deputado. Face ao problema, o Vítor sugeriu que fosse testada a API do Destakes, uma base de dados de notícias já filtradas e pensadas para o universo nacional.
-   Tweets - Tal como as notícias, também são exibidos os últimos tweets dos deputados com recurso à API do Twitter.
-   Intervenções - Na visualização das intervenções, os aplausos e interrupções do discurso principal têm o mesmo protagonismo. Esta questão vai ser trabalhada e foi mesmo sugerido que o fundo da intervenção assumisse a cor do partido do deputado que está a intervir.
-   Conceitos/ Temas - para a análise das intervenções é prioritário. Já existe um ficheiro stopwords, mas é preciso criar por tema/ subtema um conjunto de termos que permitam posteriormente responder a questões do género: "quando ocorreu a primeira intervenção de uma deputada mulher sobre a interrupção voluntária da gravidez?"
-   Ainda utilizando técnicas simples, podem vir a ser disponibilizadas as intervenções mais hilariantes (usar os risos como marcador), ou as intervenções mais quentes (recorrer à concentração de pontos de exclamação, termos relacionados com acusações, insultos, exemplo, mentiroso)
-   Registo de interesses - Esta informação não foi carregada para o website, porque o preenchimento é muito irregular. Há deputados que o fazem, outros nunca o fizeram. Porém, o problema pode ser contornado com a disponibilização do pdf onde actualmente são colocados os registos de interesse.
-   Outras propostas - Um outro aspecto mencionado pelo Victor seria a possibilidade de do utilizador poder personalizar o dashboard, ou seja, ele escolhe em cada momento que widgets deseja ver, que dados pretende ter visíveis. Outro alvo em mira é a criação de uma app para Android baseada no Congress americano, de preferência por uma pessoa já versada na programação para Android que quisesse dar uma maõzinha, utilizando o código da Sunlight Foundation.

**Alojamento**  
O website vai ficar alojado no servidor da Nazaré cedido pela Unimos. Um terabyte disponibilizado pelo Pedro poderá ser de grande utilidade para guardar os ficheiros estáticos.  
Também uma série de optimizações de cache e outras, terão de ser efectuadas antes do lançamento.

**Divulgação**  
Não está posta de parte a eventualidade de contactar alguns jornais e dar-lhes acesso exclusivo 2 ou 3 dias antes do lançamento oficial.  
Para além dos media, crê-se que poderá haver interesse da parte das Universidades, o que poderia originar parcerias interessantes.  
O contacto de pessoas influentes no meio como Paulo Querido pode ser também um ponto a favor do projecto.  
O workshop sobre o uso da tecnologia por Associações e Partidos locais organizado pelo Vítor poderá servir também para apresentar o projecto.

**Prazos e tarefas urgentes**  
Em relação a prazos, está prevista uma beta private para Fevereiro e uma ou mais sessões públicas em finais de Março.  
Nos próximos dias, quem desejar pode ter acesso ao dump da BD e à instalação local do Django+python para testes e proposta de melhoria.  
Os trabalhos mais prementes prendem-se nesta fase com o ultimar das tarefas em curso, com os testes à plataforma e ainda com a criação dos vocabulários. Não vale a pena recolher mais informação.
