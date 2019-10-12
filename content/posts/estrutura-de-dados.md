Title: Estrutura de dados
Date: 2010-08-12 18:36
Author: vsilva
Category: Blog
Slug: estrutura-de-dados
Status: published
Image: http://transparencia.hacklaviva.net/wp-content/uploads/2010/08/schema.png

Por enquanto estamos a recolher a informação para 3 tabelas:

-   MP
-   Caucus
-   Facts

Dados base dos deputados. o campo occupation, considerando que por vezes pode incluir mais do que uma profissão não deverá ser usado, preferindo o valor calculado que existe na tabela facts  
CREATE TABLE IF NOT EXISTS \`MP\` (  
\`ID\` int(11) NOT NULL auto\_increment,  
\`MPID\` int(11) NOT NULL,  
\`Name\` varchar(255) collate latin1\_general\_ci NOT NULL,  
\`DateOfBirth\` varchar(50) collate latin1\_general\_ci NOT NULL,  
\`Occupation\` varchar(255) collate latin1\_general\_ci default NULL,  
\`CreatedOn\` datetime NOT NULL,  
PRIMARY KEY  (\`ID\`)  
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COLLATE=latin1\_general\_ci AUTO\_INCREMENT=15703 ;

Dados base das legislaturas. é simplesmente a copia da tabela html com a indicação de todas as legislaturas em que um deputado participou e mais alguma informação especifica dessa legislatura.  
o campo dates tem sempre a indicação do periodo de vigencia da legislatura  
os campos hasActivity e hasRegistoInteresses podem servir para posteriormente saber quais os deputados que têm essa informação para a ir buscar  
CREATE TABLE IF NOT EXISTS \`Caucus\` (  
\`ID\` int(11) NOT NULL auto\_increment,  
\`MPID\` int(11) NOT NULL,  
\`CaucusID\` varchar(10) collate latin1\_general\_ci default NULL,  
\`Dates\` varchar(250) collate latin1\_general\_ci default NULL,  
\`Constituency\` varchar(255) collate latin1\_general\_ci default NULL,  
\`Party\` varchar(255) collate latin1\_general\_ci default NULL,  
\`HasActivity\` bit(1) NOT NULL,  
\`HasRegistoInteresses\` bit(1) NOT NULL,  
\`CreatedOn\` datetime NOT NULL,  
PRIMARY KEY (\`ID\`)  
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1\_general\_ci AUTO\_INCREMENT=13590 ;

Atributos dos Deputados. Como se resume essencialmente a um par nome, valor achei que seria suficiente por agora ter uma estrutura deste género  
CREATE TABLE IF NOT EXISTS \`Facts\` (  
\`ID\` int(11) NOT NULL auto\_increment,  
\`MPID\` int(11) NOT NULL,  
\`FactType\` varchar(50) collate latin1\_general\_ci NOT NULL,  
\`Value\` varchar(500) collate latin1\_general\_ci NOT NULL,  
\`CreatedOn\` datetime NOT NULL,  
PRIMARY KEY  (\`ID\`),  
KEY \`FactType\` (\`FactType\`)  
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COLLATE=latin1\_general\_ci AUTO\_INCREMENT=23342 ;  
Facts

