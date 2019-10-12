Title: Hackday - sessão #2
Date: 2010-08-15 08:22
Author: camorim
Category: Blog
Tags: case studies, drupal, feeds, notícias, parsing, visualização, wiki
Slug: hackday-sessao-2
Status: published
Image: 

Mais uma sessão de hackerismo radical com muito afinco e algumas dificuldades.  
Passa-se a uma breve síntese do que cada elemento esteve a fazer e em que ponto ficou.

O Vítor Silva esteve a criar o ficheiro xml de feeds (escolheu o formato Atom) para automatizar o processo de disponibilização de dados a CMS. Os testes foram realizados com o [Drupal](http://drupal.org "Drupal"){.wpGallery} e com o [Managing News](http://managingnews.com "Managing News"){.wpGallery} (profile do Drupal). Detectaram-se alguns problemas de renderização de informação. Também se concluiu que o Feeds Importer com as configurações default se adequa mais a conteúdos news/ post, em que há title, description, link, published, author. Perante isto, há duas alternativas: adaptar o conteúdo a importar às tags existentes; pesquisar de que modo seria possível criar tags personalizadas e embebê-las no mapping do feed item. Existe a [indicação clara no blog](http://developmentseed.org/blog/2009/dec/15/importing-and-aggregating-stuff-feeds "Blog Development Seed - import regular do csv"){.wpGallery} do Development Seed em como é possível agendar importações regulares de csv.

O Victor Cardoso realizou uma experiência de visualização dinâmica da relação nº deputados por partido/ nº de círculos eleitorais ao longo do tempo, leia-se legislaturas. Usou para o efeito o Motion Chart do pacote de módulos de visualização da Dataviz. O teste foi realizado com um ficheiro .csv na plataforma do Dataviz, mas a ideia na futuro é instalar o dito pacote em Drupal ou gerar widgets para embeber onde se desejar. Fica aqui a amostra deste primeiro ensaio.

<iframe scrolling="no" width="100%" height="430px" src="http://www.dataviz.org/sites/default/files/gvs_embed/37/import_oportoem_datagovpt_c_0.html"></iframe>

Outra frente de trabalho foi a edição do ficheiro "deputados\_rede\_social.ods" que lista deputados que estão a usar redes sociais. Sendo o MPID (número de identificação unívoco os deputados na plataforma da AR) o único critério fiável para compilar dados, teve de ser associado cada deputado e respectivas redes a esse MPID, mediante consulta do website parlamento.pt  
O ficheiro ficou terminado no final da sessão para que a nova informação seja integrada à base de dados geral. Quem encontrar novos dados da rede social dos deputados deve comunicá-los ao Vítor Silva que os introduz na BD.

O Bernardo Santos iniciou a pesquisa de case studies de projectos ligados ao tema da Transparência. Explorou o [The Public Whip](http://www.publicwhip.org.uk/ "The Public Whip"){.wpGallery}, que foi referência para o próprio [They Work For You](http://www.theyworkforyou.com "Theyworkforyou.com"){.wpGallery}, um outro caso a analisar com cuidado. Este levantamento consiste em tentar perceber de que modo está organizada a informação, o que é matéria de interesse e formas de apresentar e explorar informação pública dos parlamentos e seus deputados, feitas as devidas salvaguardadas em relação às diferenças de estilo e funcionamento de parlamentos, no caso inglês e português.  
Está focado na identificação de categorias e critérios de pesquisa e formulação de queries aos dados compilados que possam ser transversais e estendidos à realidade portuguesa. Exemplos: políticas, empresas, organismos, etc. e efeitos de consenso ou clivagens que desencadeiam no universo e actividade parlamentares. A ideia é criar com as categorias, subcategorias e relações eventuais entre elas, uma estrutura, uma espécie de classificação de temas, que ajude na clarificação de linhas de acção e permita criar índices e listas de categorização dos conteúdos.

A Ana Carvalho dedicou o esforço desta sessão na actualização da wiki, precisamente na secção do Hacklaviva. O suporte documental e a traçabilidade de acções, ideias que vão sendo discutidas ou testadas exigiu para já uma mais efectiva estruturação da informação.  
A opção seguida foi a de listar na página inicial do Hacklaviva todos os projectos em curso a que serão adicionados futuros projectos. Cada projecto abre para uma nova página em que são listados tópicos tidos como essenciais para dar a ideia à comunidade participante. São eles:

-   o que se pretende (objectivos),
-   o que se está a fazer (tarefas),
-   de que forma se pensa fazer e se está fazer (ferramentas),
-   listas de recursos próprios, caso de ficheiros de parser, ficheiros .csv, etc., ou externos, como bibliografia, pessoas/ entidades com experiência, glossários, etc. (documentação).

Relacionada ainda com a documentação, o Bernardo defendeu o interesse de listar algumas fontes que expliquem o funcionamento da AR e do sistema parlamentar, para que seja possível questionar de forma mais inteligente e eficaz os dados.

O Ricardo Lafuente terminou o script em phyton que transforma os pdf dos Diários da Assembleia em ficheiros csv. O dito script foi testado com 1 pdf apenas, mas o passo seguinte será alargá-lo para um conjunto de pdf e por fim à totalidade das transcrições. Estas existem desde 2002 e por ano são criadas em média 100.

O Tiago Assis experimentou o import de feeds gerado pelo Vítor no sistema Managing News. Além disso, esteve a testar várias possibilidades desta ferramenta para o projecto. Há três pontos claros acerca do interesse e limitações desta ferramenta para o projecto:  
ideal para integrar deputados e/ou actividades com dados geográficos

-   possibilidade de associar notícias de agregadores (Google News, Yahoo News, etc.) de notícias a deputados
-   necessidade de criar listas de tópicos (categorias) que ajudem a relacionar de forma pertinente e significativa notícias a dados do projecto
-   estudo da exequibilidade de estender as tags por default do formato feeds a qualquer tag ou tipo de conteúdo que se deseje recolher e agregar.

A Cláudia Amorim apresentou uma instalação Drupal já com os nodes (registos individuais) de cada deputado, tendo utilizado para o efeito o ficheiro csv da identificação dos deputados. Recorreu-se ao módulo Feeds e à função Feeds importer/ node import. Com base no campo das profissões desse mesmo ficheiro, foi gerada automaticamente uma lista de vocabulário das profissões que com a dupla cumulus+tagadelic gerou uma nuvem dinâmica das tags. Também testou em ambiente Drupal o ficheiro de feeds atom criado pelo Vítor Silva.

Em relação a esta sessão, todos os elementos, que acharem que se justifica, são convidados a criar uma entrada com mais detalhes acerca do que conseguiram realizar e próximos passos.
