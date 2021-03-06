Title: Hackday – sessão #5
Date: 2010-10-03 15:40
Author: camorim
Category: Blog
Tags: Hackday
Slug: hackday-sessao-5
Status: published

Sessão dedicada à discussão dos projectos, realização do ponto de situação e também à produção.

***Análise da "concorrência"***  
Um dos pontos abordados foi a discussão da pertinência do Transparência Hackday após o lançamento do projecto [Parlamento transparente](http://publico.pt/parlamento "Parlamento transparente"), iniciativa do jornal Público.  
Esta coincidência no tratamento do mesmo objecto, o sítio do parlamento.pt, e a associação à procura de maior transparência e proximidade dos cidadãos, não o é mais que na forma e intenção, porque as abordagens são distintas. Antes de mais, o grupo saudou a "concorrência" e reconhece que efectivamente o tema transparência está na moda. Analisando o trabalho do Público, verifica-se que é uma filtragem cirúrgica de alguns dados do Parlamento.pt e a criação de listas, cuja consulta em detalhe remete de novo para o Parlamento, com uma muito ligeira infografia e estatísticas.  
Discutiram-se os pontos comuns e encontraram-se várias características diferenciadoras que continuam a justificar o mesmo entusiasmo e pertinência do projecto Transparência Hackday delineado anteriormente.

-   Primeira: o grande trunfo do Transparência Hackday reside no facto de disponibilizar os datasets, algo que o jornal Público não faz nem é a guerra do jornalismo; a nossa meta principal é chegar aos dados e dar acesso para que as pessoas possam livremente usá-los e relacioná-los como entenderem;
-   Segundo: a cobertura retrospectiva não parece estar contemplada no projecto do Público, o que ocorre no Transparência Hackday;
-   Terceiro: a visualização de dados pretende ser uma das vertentes mais marcantes do Transparência;
-   Quarto: a leitura e o filtro dos dados no Público é a que o jornal decide, mas no Transparência, procura-se que os filtros sejam as pessoas que decidam. Para ilustrar a diferença de posicionamento, referiu-se mesmo o top dos deputados com mais propostas legislativas e mais intervenções. O Transparência não quer ficar por um mero número. Os números são importantes, mas dar a possibilidade de os cruzar com outros dados pode fazer toda a diferença. Ou seja, a quantidade pode não ser sinónimo de qualidade. Permitir essa leitura dupla é uma mais-valia do Transparência.

Em suma, o Parlamento transparente só vem confirmar a relevância do tema e mostrar que a recolha e tratamento dos dados da Assembleia dizem muito da actividade parlamentar.

***Futuro Transparência Hackday***  
Sobre o futuro do projecto Transparência, abordaram-se alguns aspectos:

-   *Alojamento*: embora sem premência imediata, é preciso ir preparando uma solução pois um serviço aberto pode estar sujeito a muitas requests. Numa fase anterior, optar-se-á por um servidor beta e cedência de password a um grupo de pessoas.
-   *Apoio institucional*: procurou-se o apoio da ANSOL, mas até à data não se obteve qualquer feedback. Portanto, esse esforço de contacto vai ser abandonado.
-   *Registo*: o registo dos datasets em domínio público ou com licença Creative Commons Share Alike é provavelmente a via mais recomendável para salvaguardar a neutralidade, abertura, acesso e reutilização dos dados no interesse da cidadania e participação dos cidadãos.
-   *Parcerias*: Transparência e Integridade, Associação Cívica contactou o Hacklaviva e mostrou-se interessada em conhecer pormenores dos planos na área da Transparência. O grupo saudou o interesse e forneceu informação, mas acha que é precoce estar a formalizar uma cooperação no imediato, já que a própria Associação Transparência e Integridade está ainda a criar o seu programa. A seu tempo poder-se-á concretizar aproximações num ou noutro ponto. A apresentação da associação na Universidade Lusófona em Novembro pode ser uma ocasião para estudar possíveis trabalhos em conjunto. Existe a possibilidade de disponibilizar servidor para o Transparência.
-   *Plataforma*: acerca do backend, o grupo tem a ideia muito bem definida - datasets, abertura, neutralidade. Acerca do Frontend, considera-se que não é desejável apontar uma única solução.

***Ponto de situação dos trabalhos***

-   *Tratamento das sessões parlamentares* - o Ricardo está na fase de corrigir os bugs do script para estender a sua aplicação a um corpus mais alargado de documentos. A Cláudia e a Ana já delinearam a próxima frente de trabalho, dar início ao tratamento temático ao material das sessões. O plano consiste em criar um ficheiro de palavras vazias que seja dado ao sistema no momento da indexação dos termos. Todas as palavras que se encontrem na lista vão ser rejeitadas e excluídas do índice. A estratégia será listar as palavras por categorias gramaticais, por forma a deixar como palavras nucleares e significativas do ponto de vista do conteúdo, os nomes e os verbos. Assim, preposições, advérbios, pronomes, nomes cujo uso repetido nas circunstâncias de um discurso, por si só não acrescentem à análise do tema abordado, ex. "senhor deputado", "afirmou", "disse", etc. A leitura atenta das transcrições de algumas sessões dará certamente mais pistas da melhor forma de criar o ficheiro de texto de palavras vazias.
-   *Visualização de dados* - o Victor afirmou ter estado a ver o potencial do mapping para o projecto. Continua a tratar dados para a visualização dos deputados por legislatura.
-   *Importação da informação dos deputados para Drupal -* depois de testes com módulos como o Feeds, Table Wizard e Node import, a Cláudia e o Tiago consideram que o sucesso do import depende dos csv e da relação entre as tabelas na origem. O ideal é que todas as tabelas na BD estejam interligadas entre si de modo a evitar esse esforço de junção posterior. Nesta sessão, editaram um csv que conjugou os campos de duas tabelas (portanto 2 csv) e a importação foi transparente e bem sucedida. Neste facto, pode estar a acontecer uma de duas situações: as queries para obter os csv à BD não estão a ser bem feitas, estando a retirar-se um csv por tabela, quando é possível fazer uma consulta na BD multi-tabela; a gestão de registos criados a partir de multi-tabelas e com campos multi-valor é perfeitamente possível ao nível do Drupal, mas requer uma expertise e solicita imenso o sistema, sobretudo se pensarmos nos milhares de nós com que o sistema tem de lidar. A percepção do Tiago e da Cláudia é a da que seria muito importante haver o máximo de flexibilidade na saída dos dados: resultados de uma tabela completa; resultados de alguns campos de uma tabela; resultados da combinação de tabelas.
-   *Documentação e diversos* - A Ana e o Daniel estiveram a acertar questões de configuração de ficheiros, encoding e a analisar a documentação do projecto. O Daniel criou um espaço no GitHub para que seja possível guardar aí código, sources, de forma mais clara e acessível. O endereço é: ﻿﻿http://github.com/idnael/transparenciapt
-   *Listagens a criar* - duas listas devem ser objecto da atenção dos elementos. Neste momento ninguém está a tratar disso...
    -   Fotografias dos deputados - o parlamento.pt não tem retratos. Fontes possíveis são a Wikipédia e o Parlamento transparente, embora esta última tenha o inconveniente de ser apenas referente à actual legislatura e poder tratar-se de fotos do arquivo do jornal e sujeito às leis de direito autoral.
    -   Nomes abreviados - no parlamento.pt a forma dos nomes é a forma completa. Porém, para a análise das sessões vai interessar ter a lista de todos os deputados pela forma abreviada, pela qual são designados e conhecidos. A Wikipédia tem as duas formas, sendo uma boa fonte para essa recolha. Nesse sentido, quem tiver meios e ideias para automatizar o processo, comunique a intenção e avance.

***Redes comunitárias wi-fi***  
O último tema tratado foram as redes comunitárias sem fios, tendo estado o Sérgio a inteirar-se da documentação relativa à Unimos.net e Guifi.net  
Em grupo, começou-se por referir os locais de instalação das antenas, todos eles altos, de acesso fácil e consentimento possível junto dos responsáveis. A saber: último andar de um prédio a 30 metros do Hacklaviva, espaço Musas (no Marquês), Alves Redol, edifício da Gest.  
O Sérgio, com bastantes conhecimentos nesta área, recomendou que se acrescentasse às fontes, o [Fórum Wireless.pt](http://wireless.com.pt/forum/ "Wireless.pt") que era (e pensa que ainda é) bastante dinâmico. Disse ainda que a sul, no Algarve, existem várias comunidades locais fervilhantes.  
O próximo passo consiste em montar algumas antenas para conseguir access points para testes. Nessa altura, vai ser mais fácil avaliar as necessidades de localização e se a topografia portuense afecta muito ou não o sucesso da empresa. Porque apesar do Porto não ser uma cidade muito dispersa geograficamente, tem prédios bastante altos e ruas muito estreitas que podem dificultar muito a chegada de sinal.  
O Ricardo contactou por email o José Monteiro da Unimos para agendar uma ligação Skype mais técnica. Foi criada uma página na [wiki](http://w.hacklaviva.net/Redes_comunit%C3%A1rias_wi-fi "Redes comunitárias na w.hacklaviva.net") do Hacklaviva para este projecto. Desta forma, fica mais fácil o acesso à informação e à edição da mesma sempre que se justifique.
