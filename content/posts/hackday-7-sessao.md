Title: Hackday - sessão #7
Date: 2010-11-13 19:28
Author: camorim
Category: Blog
Tags: Hackday
Slug: hackday-7-sessao
Status: published
Image: 

Esta sessão inclui uma breve introdução ao GIT, a apresentação de nova actividade e várias tarefas do projecto.

**Hackathon**

As comunidades dedicadas à Transparência gostam de partilhar, por isso agendaram um evento super-original, uma maratona mundial dos trabalhos de Transparência. O RIcardo apresentou linhas gerais e modo de funcionamento e disse que ainda haveria um Hackday antes do evento para preparar ainda melhor o trabalho para a maratona.

-   Participantes - são uma série de [comunidades](http://www.opendataday.org/wiki/City_Events "OpenDataDay - comunidades por países") que estarão presentes
-   Condições - uso IRC; logística; temas; datasets para trabalhar. A ideia está muito bem explicada [aqui](http://www.opendataday.org/wiki/Running_a_Hackathon "Preparar a Hackathon").
-   Duração - sábado e domingo, com "noitada" (4 e 5 de Dezembro)
-   Objectivos - promover a comunicação e troca com núcleo do Brasil (S. Paulo) e outros núcleos. Focalização e concretização de alguns pontos (sprint)
    -   Usar técnica de scrapping mais sistemática e eficiente
    -   Criar backend com Django para os deputados e intervenções
    -   Desenvolver a documentação do projecto
    -   ... (temas mais específicos a definir)

**GIT**

O GIT foi criado por Linus Torvals e é de grande popularidade e utilidade. O Ricardo fez um pequeno tutorial de como instalar o GIT no Ubuntu, embora ainda vá ser retomado na próxima sessão. Haverá um tutorial na wiki sobre o Git e criação de chaves SSH.

Passo 1 - Instalar o GIT no local: sudo apt-get install git-core

Passo 2 - O repositório do GIT Transparência está em http://gitorious.org/transparencia-porto. Existe um help (?) com alguns comandos básicos.

Passo 3 - Cópia local usando o Git clone. No caso de ser uma sessão de trabalho de grupo, é possível fazer apenas um git clone local e todos os elementos acedem ao mesmo clone local. É óptimo sobretudo quando o repositório é grande.

-   Clicar "clone repository"
-   Usar comando: git clone git://gitorius.org/transparencia-porto/transparencia-porto.git

*Principais comandos*

-   git status - indica a estado do repositório
-   git add file - acrescenta ficheiro ao repositório localmente
-   History - guarda os ficheiros e toda a história de revisões
-   git commit - adiciona os repositório, ter o cuidado de pôr a info. Ex. git commit -m "Comentário entre aspas"
-   git diff - assinala as diferenças
-   git push origin master - vai buscar ficheiro que já existe no repositório

**Tarefas várias**

Ricardo - Colocou os textos das sessões parlamentares no Gitorius para se trabalhar. O volume é considerável 60MB. Para notificar erros detectados será criado um link na wiki, já que o Gitorious não tem Bug tracker.

Eduardo - Preparou a lista de links directos para os diários de república obtida com um script em python. Esse é um dos primeiros produtos do trabalho já realizado. O aspecto visual ainda não foi trabalhado, mas o conteúdo e a acessibilidade da solução já estão asseguradas.

Ana - Ocupou-se da criação da homepage para o projecto em Html com folha de estilos para começar a criar identidade e a "mostrar trabalho". A ideia é colocar a homepage na raiz transparencia.hacklaviva.net, deslocando o blog para transparencia.hacklaviva.net/blog. Da sessão já resultou uma página muito simples que vai ter informação básica do projecto. Esse trabalho está no Gitorious, bem o svg usado, para quem desejar fazer experiências e propor alterações. Ainda vai ser trabalhado um logo.

Victor - No parlamento.pt obtém-se o dado de nº de deputados por legislatura de cada um dos partidos. Porque não existe uma coincidência numérica entre o nº de deputados realmente eleitos e os deputados que exercem, procurou-se junto da CNE (Comissão nacional de Eleições) informação complementar que desse maior consistência na análise dos números do Parlamento. Assim, começou-se por criar um ficheiro com os resultados detalhados das legislativas (não inclui as últimas eleições legislativas), algo relativamente simples, porque a CNE tem essa informação em Excel . De seguida, recorreu-se aos Mapa oficial das eleições (em pdf!) que listam nominalmente os deputados eleitos. O objectivo desta recolha é identificar do total dos deputados que exerceram aqueles que foram realmente eleitos.

Cláudia + Tiago - Confirmado o funcionamento do Node import para criação de nodes dos deputados a partir de um único csv. Os campos a incluir são todos os respeitantes ao deputado (id, nome, profissão, distritos, legislaturas, partidos, cargos exercidos). Os campos multivalor são separados por \|.
