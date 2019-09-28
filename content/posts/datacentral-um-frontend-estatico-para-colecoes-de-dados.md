Title: Datacentral: um frontend estático para coleções de dados
Date: 2014-09-23 16:21
Author: ricardo
Category: Blog
Slug: datacentral-um-frontend-estatico-para-colecoes-de-dados
Status: published
Image: http://www.transparenciahackday.org/wp-content/uploads/2014/09/datacentral.png

\[Este post foi originalmente [publicado em inglês](http://okfnlabs.org/blog/2014/08/19/datacentral.html) na [OKFN Labs](http://okfnlabs.org), e traduzido pela Marta Pinto. É uma explicação técnica do software por trás do nosso mais recente projeto, a Central de Dados. Vamos brevemente publicar um novo post a explicar esse projeto em termos menos especializados.\] {#este-post-foi-originalmente-publicado-em-inglês-na-okfn-labs-e-traduzido-pela-marta-pinto.-é-uma-explicação-técnica-do-software-por-trás-do-nosso-mais-recente-projeto-a-central-de-dados.-vamos-brevemente-publicar-um-novo-post-a-explicar-esse-projeto-em-termos-menos-especializados. dir="ltr"}

Este texto explica as as questões com que nos deparámos em Portugal na frente sobre os dados abertos quando se trata de disponibilizar *datasets* em bruto de uma forma *standard* e fácil de processar. Vamos também apresentar a [Datacentral](http://github.com/datacentral/centraldedados), a nossa tentativa para dar uma solução a essas questões: uma ferramenta Python para gerar sites estáticos para as nossas data packages, que usamos para o nosso novo projeto [Central de Dados](http://centraldedados.pt).

Primeiro problema: ter um formato comum para arquivar os datasets {#primeiro-problema-ter-um-formato-comum-para-arquivar-os-datasets dir="ltr"}
-----------------------------------------------------------------

No[Transparência Hackday Portugal](http://transparenciahackday.org), tal como em qualquer outro grupo interessado em open data, trabalhamos com muitos datasets. Há algum tempo que um dos aspetos que nos tem atrasado é o facto de nunca termos tido uma solução centralizada para armazenamento de bases de dados: alguns estão em Google Docs, outros em repositórios Git, outros estão em servidores na web. Anterior a isto, outro aspeto era o formato dos dados: percebemos que estávamos perdidos entre ficheiros CSV ou JSON, bases de dados SQL, folhas de cálculo e ficheiros de texto. Converter estes ficheiros foi um trabalho que fomos fazendo ad hoc, e enfrentámos sempre o desafio de encontrar um formato comum, o que normalmente se esbarrava com diferentes preferências pessoais, e com as dificuldades que envolve a conversão em massa de coleções de dados heterogéneas.

Solução: Tabular data packages {#solução-tabular-data-packages dir="ltr"}
------------------------------

Cruzámo-nos quase acidentalmente com o standard[Data Package](http://data.okfn.org/standards). Foi uma revelação ver o quão elegante era esta solução para o nosso problema com os formatos: ao utilizar a especificação[Tabular Data Package](http://data.okfn.org/doc/tabular-data-package), podíamos avançar e converter os nossos datasets em CSV, a par com os seus metadados – o que é bastante fácil de gerar mantendo o uso de ferramentas para este trabalho. A partir, daí também desenvolvemos scripts para repescar e atualizar os datasets, assim como ferramentas de pós-processamento para gerar outros formatos a partir da data package.

Já existe muita informação disponível sobre Data Packages:

-   o manifesto [Frictionless Data vision](http://data.okfn.org/vision), onde são colocados de forma clara o problema e a proposta de workflow para lidar com os conjuntos de dados heterogéneos

-   [Data Packages](http://data.okfn.org/doc/data-package)

-   [Tabular Data Packages](http://data.okfn.org/doc/tabular-data-package) (o formato que usamos)

-   as especificações em linguagem corrente sobre [Data Packages](http://www.dataprotocols.org/data-packages/) e[Tabular Data Packages](http://www.dataprotocols.org/simple-data-format/)

-   muitas ferramentas para gerir e publicar pacotes de dados em[data.okfn.org/tools](http://data.okfn.org/tools)

Desta forma, o nosso problema sobre formatos comuns para os dados está agora resolvido. De seguida enfrentámos um outro aspeto: como publicar e distribuir estes datasets de uma forma simples e sem atrito.

Segundo problema: um sistema simples para publicar as data packages {#segundo-problema-um-sistema-simples-para-publicar-as-data-packages dir="ltr"}
-------------------------------------------------------------------

Ter um local central através da qual pudessemos distribuir os datasets era um dos aspetos que nos estava a faltar. Para alguns dos requisitos que tínhamos, seria necessário ter um site para agregar todas as nossas data packages:

-   tornaria mais facil hospedar workshops sobre dados, providenciando um acesso rápido aos dados em bruto, e assim evitar as pens USB, documentos Google e links da Dropbox.

-   daria mais visibilidade aos nossos esforços, agregando todo o nosso trabalho que está disperso e apresentá-lo de forma simples.

-   mais importante seria dar-nos um caminho mais fácil para apresentar o nosso trabalho de recolha e conversão dos dados, e um melhor argumento para apresentar às entidades públicas onde podem publicar os seus dados. Em vez de dizermos “Deem-nos os vossos dados para que possamos convertê-los e torná-los abertos”, podermos simplesmente dizer “Deem-nos os vossos dados para que possam estar acessíveis em FantasticoPortalDeDados.pt”. Ter uma “marca” separada facilita a explicação – e os assuntos sobre dados abertos já são complicados o suficiente para conseguirmos manter a atenção das pessoas.

Existem soluções como o [DataTank](http://thedatatank.com) ou, mais destacado, o[CKAN](http://ckan.org). Então por que é que o CKAN não é uma opção?

O CKAN é um enquadramento brilhante para alojamento, gestão e para lidar com grupos heterogéneos de datasets. Contudo, instalar o CKAN é um [processo complexo](http://docs.ckan.org/en/latest/maintaining/installing/index.html), e o seu poder tem o custo da manutenção de uma aplicação web completa: requer uma configuração cuidadosa do servidor, atualizações regulares, e assegurar que os recursos do servidor não estão acima do nível razoável. Como somos uma equipa pequena, não requeremos a maior parte dos requisitos avançados (como as permissões).

Finalmente, no Transparência Hackday já temos que gerir suficientes aplicações web, e a experiência levou-nos a procurar um design de aplicação mais simples.

Solução: Datacentral, um gerador de sites estáticos para coleções de data packages {#solução-datacentral-um-gerador-de-sites-estáticos-para-coleções-de-data-packages dir="ltr"}
----------------------------------------------------------------------------------

Propusemo-nos a criar uma aplicação simples que pudesse responder aos nossos objetivos. Os principais princípios de design são:

-   Permitir o acesso a conjuntos de dados em bruto. Um acesso fácil e direto aos ficheiros é o principal motivador desta implementação. Isto difere de uma API, que apesar de útil, iria requerer uma complexidade adicional.

-   Gerar um site HTML estático – Publicar datasets não necessita de uma aplicação web em tempo real para fazer queries aos dados. Apenas precisamos de atualizar o site diariamente, por isso não é necessária uma aplicação dinâmica.

-   Gerar localmente e fazer upload – A geração do site deve ocorrer localmente e não no servidor. Decidimos ter um dos nossos computadores a tratar da geração periódica dos ficheiros HTML, recorrendo ao rsync para os colocar num servidor que os aloja.

-   Baixa pegada de hardware – Local generation means that our system spec requirements are low. Gerar o site localmente significa que os nossos requisitos de sistema não são grandes. Não precisar de um hardware especializado significa que podemos usar um computador mais velho para esta tarefa. É o que estamos a fazer atualmente – a geração do site está a ser feita num portátil Sony Vaio de 2007 com um ecrã partido.

-   Separar os datasets do site – Alojando cada data package num repositório Git separado, o gerador local pode ir buscar isso e gerar novamente o site sem ter que alojar e gerir uma cópia separada da data package e correr o risco de ambas as versões deixarem de sincronizar. Percebemos que isto acontece frequentemente quando se cria uma aplicação web com base de dados. Ao separar as data packages e o interface web, os e as responsáveis pela manutenção das data packages podem trabalhar de forma independente nos dados, enquanto que o gerador atualiza periodicamente o site disponível ao público.

-   Controlado através da linha de comandos – Em nome da simplicidade, mas pagando o preço de perder a user-friendliness, optámos por um interface de configuração e controlo na linha de comandos. Percebemos que a gestão de um site destes deve ser sobretudo um processo automatizado, e uma forma eficaz de o fazer era a de restringir a aplicação a um conjunto de scripts que pudessem ser geridos através de Makefiles e executados através de cron jobs.

Contudo existem algumas desvantagens significativas.

-   Não existe uma API uma vez que tudo é HTML. Esta pode ser a desvantagem mais evidente numa abordagem estática.

-   Isto também significa que não há capacidade de pesquisa. Podemos considerar usar um motor de busca de terceiros, uma vez que o site é apenas HTML que pode ser processado pelo Google, DuckDuckGo e outros web crawlers.

-   Não existe suporte para conteúdo dinâmico, como num site ou blog. Listar feeds externas poderá ser feito através de widgets em JavaScript.

-   Como o interface se baseia na linha de comandos, não existe nenhum painel de administração que permita editar ou alterar pormenores no browser.

Como funciona {#como-funciona dir="ltr"}
-------------

O workflow faz-se da seguinte forma:

1.  As data packages são publicadas e atualizadas em repositórios individuais pelos respetivos responsáveis.

<!-- -->

1.  A aplicação Datacentral está configurada para identificar quais os repositórios que devem ser acompanhados.

2.  Na primeira vez que corremos o Datacentral, todos os repositórios são clonados, gerando as páginas HTML de cada data package.

3.  As páginas HTML individuais (Sobre, Contacto) são geradas a partir de ficheiros de texto formatados segundo a norma Markdown.

4.  Os ficheiros HTML resultantes podem ser publicados através de FTP ou rsync para um webserver público.

Na prática existe um script -- generate.py -- que inspeciona cada data package e usa a biblioteca[Jinja](http://jinja.pocoo.org) para preencher um conjunto de templates HTML. Os ficheiros HTML gerados são colocados no diretório \_output, que pode ser acedido com um webserver local ou enviado para uma VPS. Todas as ações, desde a instalação à geração e ao upload, podem ser levadas a cabo através de uma Makefile.

Se estiveres interessado em ler mais sobre o Datacentral e até experimentar (é simples),[é só ver o site do projeto](https://github.com/centraldedados/datacentral). Todo o feedback é bem recebido, por isso digam-nos se houver bugs, sugestões ou sugestões de novas funcionalidades no [issue tracker](https://github.com/centraldedados/datacentral/issues) do Datacentral. Podes também ver tudo isto em ação no nosso portal independente de dados (em desenvolvimento), a[Central de Dados](http://centraldedados.pt).
