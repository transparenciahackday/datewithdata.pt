Title: Hackday – sessão #6
Date: 2010-11-01 09:11
Author: camorim
Category: Blog
Tags: Gitorious, Hackday
Slug: hackday-sessao-6
Status: published
Image: http://transparencia.hacklaviva.net/wp-content/uploads/2010/11/IMAG0009_a-300x179.jpg

Nesta sessão foram integrados novos elementos com competências que estavam a ser necessárias. Aliás, este reforço representa uma injecção de mais dinamismo e energia. Ricardo, Rizo, Rui, Zé, são das ciências de computação, manifestando interesse também pela inteligência artificial, algoritmia. Um outro elemento, Eduardo, está confortável na área do multimédia, cinema, mas lida também com o php e html, xml. O João, das matemáticas, está ligado mais ao software de gestão, mas pretende fazer incursões por campos mais alargados de aplicação da informática. A este conhecimento novo que chega ao grupo, tínhamos já dentro de portas pessoas que trabalham com o Drupal, processing, agora também com o contributo da Sara.

Queremos estar salvaguardada, em termos de equipa, as etapas mais próximas e futuras do projecto Transparência. Programação, processamento de dados, visualização, questionamento e distância crítica em relação aos dados, a que a experiência do João pode ajudar bem como alguma orientação para a pesquisa e localização de fontes prestada pelo recente TIAC Transparência Internacional Associação Cívica.

Feitas as apresentações e os objectivos gerais do projecto, inspirados em modelos como [They Work For You](http://www.theyworkforyou.com/ "They work for you") e [They Rule](http://www.theyrule.net/2004/tr2.php "They rule"), passou-se a fazer o ponto de situação em relação às duas linhas de projecto - Deputados e DAR.

#### ***Metodologia de trabalho***

-   Gitorius como repositório de código e controlo de versões
-   Organização em grupos de trabalho: grupos da programação, visualização, etc.

#### ***Linha de trabalho do DAR***

Melhoria do parsing das transcrições

-   correcção de datas e posição
-   teste a erros
-   outuput: csv  e xml

Análise das transcrições ao nível semântico, lexical

-   data mining
-   indexação automática
-   criação de ontologias, vocabulários
-   integrar sempre que possível RDF
-   identificação de temas abordados, incidências por deputado, partidos, distritos, legislaturas...
-   cruzamento com levantamento da parte legislativa no sentido de encontrar padrões, tendências

#### ***Linha de trabalho do DEPUTADOS***

-   Scraping total do site parlamento.pt em tempo recorde, uma a duas semanas de forma a criar um mirror local
-   Criação da base de dados local
-   Criação de relações e consultas
-   Listagem de possíveis relações de tabelas, campos, para obter certos outputs

#### ***Visualização ( ao serviço do DAR e Deputados)***

-   Solicitar queries pertinentes
-   Escolher as ferramentas adequadas para a visualização de determinados resultados e efeitos: gráficos, gráficos dinâmicos (chart motion), tags cloud, geolocalização, timelines, etc.
-   Avaliar eventuais efeitos perniciosos associados a uma visualização ou exploração de dados: não enveredar pela estatística simples e pura, procurando contextualizar sempre os resultados

Na própria sessão, ainda foi possível avançar nalgumas frentes. A tarefa do scraping ficou [![Vítor Silva explica o que já está feito](http://transparencia.hacklaviva.net/wp-content/uploads/2010/11/IMAG0009_a-300x179.jpg "Mãos à obra"){.size-medium .wp-image-57 .alignright width="300" height="179"}](http://transparencia.hacklaviva.net/wp-content/uploads/2010/11/IMAG0009_a.jpg)agendada e dividida por 6 participantes; o script em python está praticamente terminado e corrigidos os bugs para poder entrar em produção. Existe no Gitorius um exemplo de transcrição. O Eduardo num golpe de engenharia inversa descobriu como estão armazenados os pdf das transcrições. Isto permite descarregar em menos tempo as transcrições da 2ª série que ainda não tínhamos arquivadas localmente. Listas de organismos públicos está a ser criada para constituir parte dos vocabulários para análise e cruzamento de dados. Essa lista também vai ficar arquivada no Gitorius. Foram ainda criadas contas para todos no Gitorius e será feita uma breve introdução ao seu uso na próxima sessão de trabalho, agendada para 13 de Novembro.

NB *Esta longa sessão de trabalho começou com o projecto das redes comunitárias sem fios de que se dá conta na [wiki](http://w.hacklaviva.net/Redes_comunit%C3%A1rias_wi-fi#Sess.C3.B5es "Sessão 2 - redes comunitárias").*
