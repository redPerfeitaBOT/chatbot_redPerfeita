import telebot


CHAVE_API = "5971940889:AAGrltLY_AMm0Swwr-o8uaKmilhZsBJiM20"
bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["op1"])
def op1(mensagem):
    texto = """A redação é usada para produzir roteiros, criar relatórios, documentos, no jornalismo, entre outros. 
Sempre que se necessite apresentar um tema de forma estruturada e com mais descrição, a redação se faz essencial.
Desde que a escrita foi inventada que a redação se faz presente na cultura da civilização. 
E ela é considerada hoje como algo que faz parte do campo artístico literário.
    """
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["op2"])
def op2(mensagem):
    texto = """No Enem, a redação cobrada é do tipo dissertativo-argumentativo. 
    A diferença é que também é exigida a apresentação de uma proposta de intervenção social para solucionar o problema apresentado no tema.
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["op3"])
def op3(mensagem):
    texto = """ A redação dissertativa é um gênero caracterizado pela defesa de uma ideia. No Enem, o formato exigido é o dissertativo-argumentativo.
Isso significa que o candidato deve construir o texto pautado em dados e fatos. Por isso, é fundamental prestar muita atenção no enunciado e, principalmente, no tema da redação.
Uma redação do ENEM deve ter pelo menos 30 linhas, com isso, o ideal é que a sua redação tenha 4 parágrafos:
    >1 para introdução (com 7 linhas); 
    >2 para desenvolvimento (com 7 linhas cada); 
    >1 para conclusão (com 9 linhas)."""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["op4"])
def op4(mensagem):
    texto = """Veja estes vídeos e aprenda a fazer uma redação nota 1000:
    > https://youtu.be/eI8R8Eyv9vQ

    > https://youtu.be/MeKHJVPNV30


    Cursos gratuitos de redação:
    > https://youtube.com/playlist?list=PLhFNxzLJLH3vMVikOGLmorhohcG0Bk2ow

    > https://youtube.com/playlist?list=PLofmLAJWpYDfpURLqCNg4a4PjVcPpH1gE
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["op5"])
def op5(mensagem):
    texto = """ A estrutura de uma redação dissertativa-argumentativa é composta por três partes: introdução, desenvolvimento e conclusão.
O modelo de estrutura de redação que sugerimos aqui é de 4 parágrafos: um de introdução, dois de desenvolvimento e um de conclusão. 
Tanto a introdução quanto a conclusão necessitam sempre de apenas um parágrafo.
Enquanto isso, o desenvolvimento tem um número variável de parágrafos.
Não existe nenhuma regra que exija que sua redação tenha 4 parágrafos, mas essa é uma dica que a gente dá tendo em vista que a maior parte das redações nota mil do Enem apresentam dois parágrafos de desenvolvimento."""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["op6"])
def op6(mensagem):
    texto = """Não é sem razão que o primeiro parágrafo da estrutura de uma redação é chamado de introdução, pois é nessa parte do texto que você vai expor (apresentar) as principais questões a serem abordadas no restante do texto.
No primeiro parágrafo, o leitor terá uma dimensão geral do assunto e vai entender as razões pelas quais a discussão do problema é relevante.
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["argumentacao"])
def argumentos(mensagem):
    texto = """Argumento de Exemplificação:
    Ele pode ser usado para explicitar o argumento através de um exemplo. Em um tema como a persistência do racismo na sociedade brasileira o argumento de exemplificação que pode ser utilizado é o caso do músico negro que foi morto com 80 tiros disparados pelo exercito brasileiro no Rio de Janeiro.
    Esse argumento serve para embasar que o preconceito racial persiste na sociedade, visto a suspeita que um homem negro levantou porque foi confundido com criminosos.

Argumento de Autoridade:
    É a utilização da fala de uma figura reconhecida sobre o assunto, ou até mesmo o que essa personalidade representa para o tema em questão.
    Por exemplo, ainda dentro do tema sobre racismo, é cabível citar Nelson Mandela, visto que ele foi um advogado e militante importantíssimo para a superação dos preconceitos e da segregação racial na África do Sul.
    É ainda mais interessante citar uma frase que ele tenha dito sobre o assunto, como “Ninguém nasce odiando o outro pela cor de sua pele, ou por sua origem, ou sua religião." de seu livro Longo Caminho para a Liberdade.

Argumento histórico:
   É aquele que aconteceu em determinado momento da história - seja ele a nível mundial ou particular, como a Ditadura Militar brasileira. É comprovado por si só, visto que é de conhecimento geral.
   Um exemplo de argumento histórico para comprovar a persistência do racismo na sociedade brasileira - e de vários países do mundo - é o fato de que a escravidão, principalmente no século XIX com povos africanos, e a utilização dos mesmos como moeda de troca possibilitou que eles fossem vistos por algumas pessoas como inferiores a outras raças.

Argumento comparativo:
    A comparação é um excelente recurso que pode ser utilizado para deixar ainda mais evidente uma opinião sobre determinado assunto.
    Tratando-se de racismo, é coerente, ao realizar a argumentação, afirmar que a escravidão no Brasil ocorreu de forma velada enquanto que nos EUA ela foi muito evidente pela segregação até mesmo de bairros para negros e brancos.
    Lançando um olhar sob os dias de hoje, observa-se que o racismo no Brasil parece ainda mais fortificado enquanto que nos EUA muitas barreiras já foram superadas, visto que Barack Obama foi o primeiro presidente negro do país.

Fatos (dados estatísticos):
    O uso de informações retiradas de veículos de informação legitimados é um forte argumento para o embasamento da posição apresentada pelo candidato.
    Por exemplo, afirmar a persistência do racismo na sociedade brasileira e trazer a informação do Atlas da Violência de que 75% das vítimas de homicídio no país são negras fundamenta ainda mais o argumento de que o racismo é um problema que permanece na sociedade.
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["contextualizacao"])
def contextualizacao(mensagem):
    texto = """  A contextualização ou assunto é algo mais abrangente do que o tema, mas que está conectado a ele.
Por exemplo: o tema da redação de 2018 foi “a manipulação do usuário pelo controle de dados na internet”. 
Nesse caso, o contexto poderia ser sobre meios de comunicação, redes sociais, internet em geral, privacidade, entre outras possibilidades.
Além disso, o contexto é um bom lugar para você citar algum repertório sociocultural, como um livro, um filme, uma música, um dado histórico ou estatístico.
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["tema"])
def tema(mensagem):
    texto = """Depois de fazer a contextualização, você deve demonstrar como o contexto está ligado ao tema.
Tente não copiar o tema de forma literal. Em vez disso, tente escrever com suas palavras. 
Mas não esqueça de que todos os elementos do tema precisam estar presentes.
Utilizando o exemplo anterior, você deve lembrar de mencionar a “manipulação”, o “controle de dados” e a “internet”.
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["tese"])
def tese(mensagem):
    texto = """Em seguida, você não pode esquecer de escrever a sua tese. A tese ou objetivo do texto é aquilo que você pretende defender ao longo da redação. 
Essa é uma das partes mais importantes de toda a sua redação.
A fim de definir qual será a sua tese, você pode se perguntar: “o que eu acho sobre o tema?”. ]
Partindo da sua resposta, você vai conseguir formular o objetivo do seu seu texto, ou seja, sua tese.
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["perguntas"])
def perguntas(mensagem):
    texto = """ Outras perguntas que podem auxiliar na criação da sua tese e, mais à frente, podem fornecer ideias para os parágrafos de desenvolvimento e para a conclusão:
    1. Qual o problema?
    2. Por que se trata de um problema?
    3. Quais as causas para tal problema?
    4. Há alguma solução?
    5. Como e por que colocar tal solução em prática?
    6. Como essa proposta pode, de fato, resolver o problema?
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["naofazer"])
def naofazer(mensagem):
    texto = """O principal cuidado que você deve ter ao escrever a introdução do seu texto é não misturar os assuntos.
A pluralidade de ideias deixa o texto poluído e o leitor confuso. E ainda: não mencione nenhum fato na introdução que não será explorado ao longo do texto.
Foque na sua tese principal.
É recomendável evitar períodos longos no primeiro parágrafo.
O espaço para produzir orações mais longas é o desenvolvimento. E mesmo assim, esse recurso deve ser usado com bastante critério.
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["op7"])
def op7(mensagem):
    texto = """Componentes de uma introdução:
    /contextualizacao
    /tema
    /tese
    /perguntas
    /naofazer"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["op8"])
def op8(mensagem):
    texto = """O desenvolvimento da redação é uma das partes que compõem a estrutura do texto, sendo os outros a introdução e a conclusão. O desenvolvimento também é a parte com mais conteúdo da redação.
Isso porque é dentro dele que você precisa defender o seu ponto de vista sobre a problemática apresentada usando argumentos bem embasados.
O mais comum é que a introdução leve um parágrafo, o desenvolvimento seja apresentado em dois e que a conclusão amarre todo o texto em um parágrafo."""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["argumentacao"])
def argumentacao(mensagem):
    texto = """Conheça bem os tipos de argumentos:
É fundamental que você conheça os variados tipos de argumento para escolher aquele que for mais adequado ao tema e aos seus conhecimentos sobre o assunto. Abaixo você conhecerá cada um deles e encontrará exemplos práticos.

Argumento de Exemplificação:
   Ele pode ser usado para explicitar o argumento através de um exemplo. Em um tema como a persistência do racismo na sociedade brasileira o argumento de exemplificação que pode ser utilizado é o caso do músico negro que foi morto com 80 tiros disparados pelo exercito brasileiro no Rio de Janeiro. 
   Esse argumento serve para embasar que o preconceito racial persiste na sociedade, visto a suspeita que um homem negro levantou porque foi confundido com criminosos.

Argumento de Autoridade:
   É a utilização da fala de uma figura reconhecida sobre o assunto, ou até mesmo o que essa personalidade representa para o tema em questão.
   Por exemplo, ainda dentro do tema sobre racismo, é cabível citar Nelson Mandela, visto que ele foi um advogado e militante importantíssimo para a superação dos preconceitos e da segregação racial na África do Sul.
   É ainda mais interessante citar uma frase que ele tenha dito sobre o assunto, como “Ninguém nasce odiando o outro pela cor de sua pele, ou por sua origem, ou sua religião." de seu livro Longo Caminho para a Liberdade.

Argumento histórico:
   É aquele que aconteceu em determinado momento da história - seja ele a nível mundial ou particular, como a Ditadura Militar brasileira. É comprovado por si só, visto que é de conhecimento geral.
   Um exemplo de argumento histórico para comprovar a persistência do racismo na sociedade brasileira - e de vários países do mundo - é o fato de que a escravidão, principalmente no século XIX com povos africanos, e a utilização dos mesmos como moeda de troca possibilitou que eles fossem vistos por algumas pessoas como inferiores a outras raças.

Argumento comparativo:
   A comparação é um excelente recurso que pode ser utilizado para deixar ainda mais evidente uma opinião sobre determinado assunto.
   Tratando-se de racismo, é coerente, ao realizar a argumentação, afirmar que a escravidão no Brasil ocorreu de forma velada enquanto que nos EUA ela foi muito evidente pela segregação até mesmo de bairros para negros e brancos. 
   Lançando um olhar sob os dias de hoje, observa-se que o racismo no Brasil parece ainda mais fortificado enquanto que nos EUA muitas barreiras já foram superadas, visto que Barack Obama foi o primeiro presidente negro do país.

Fatos (dados estatísticos):
   O uso de informações retiradas de veículos de informação legitimados é um forte argumento para o embasamento da posição apresentada pelo candidato.
   Por exemplo, afirmar a persistência do racismo na sociedade brasileira e trazer a informação do Atlas da Violência de que 75% das vítimas de homicídio no país são negras fundamenta ainda mais o argumento de que o racismo é um problema que permanece na 
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["conectivos"])
def conectivos(mensagem):
    texto = """É fundamental que você conheça os conectivos e saiba utilizá-los de maneira adequada.
Além deles serem necessários para que você consiga 200 pontos na competência 4 do ENEM, os conectivos são capazes de trazer coesão e coerência à sua redação.
    """
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=["topicofrasal"])
def topicofrasal(mensagem):
    texto = """O tópico frasal é a ideia central do seu argumento, aquilo que você acredita ser a situação-problema relacionada ao tema e que será o foco de discussão do parágrafo.
É uma frase breve que sintetiza o argumento que você vai desenvolver ao longo do parágrafo.
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["problematizacao"])
def problematizacao(mensagem):
    texto = """ Depois de produzir um tópico frasal com o argumento, é hora de desenvolvê-lo.
Por isso, não esqueça que a redação do ENEM sempre trata de um problema e exige que o candidato se posicione diante dele.
Ofereça como exemplo informações como citações, dados estatísticos, entre outros e problematize, ou seja, lance um olhar crítico ao analisá-los.
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["contextualizacao"])
def contextualizacao(mensagem):
    texto = """Além de fazer a problematização do tema com argumentos, é muito importante que você contextualize, ou seja, traga um repertório sociocultural legitimado, pertinente e produtivo.
O repertório é o conhecimento que você adquiriu ao longo da vida escolar - em disciplinas como história, matemática, literatura, etc - ou pessoal, como filmes, livros e séries.
Mas não se esqueça: eles devem ter relação com o assunto abordado!"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["paragrafos"])
def paragrafos(mensagem):
    texto = """Conclua o parágrafo:
É fundamental que seu parágrafo, assim como a sua redação, apresente início, meio e fim. Por isso, faça a conclusão da ideia do parágrafo.
Se você apresentou seu argumento e trouxe um dado estatístico para comprová-lo, a conclusão é o momento em que você reafirma seu posicionamento e relaciona as duas informações, seu posicionamento através do argumento e a informação apresentada.

Faça conexões:
É muito importante que você não apresente somente um parágrafo, visto que a estrutura do seu texto deve ser a dissertativa-argumentativa.
Por isso, tente relacionar as informações do primeiro parágrafo com o segundo para demonstrar que você é organizado e possui um projeto de texto.
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["op9"])
def op9(mensagem):
    texto = """Componentes de um desenvolvimento:
    /argumentacao
    /conectivos
    /topicofrasal
    /problematizacao
    /contextualizacao
    /paragrafos  
    """
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["op10"])
def op10(mensagem):
    texto = """ A conclusão finaliza um texto, concentra as ideias e apresenta um resumo. 
Para saber como fazer a conclusão da redação Enem, entenda como apresentar uma proposta de intervenção com os elementos essenciais."""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["tiposconclusao"])
def tiposconclusao(mensagem):
    texto = """ São, na verdade, três técnicas de conclusão que podem ser usadas separadas ou juntas e vão facilitar a transmissão das ideias.
Conclusão por síntese:

    Isso nada mais é do que resumir. Escrever o mesmo conteúdo de forma reduzida ou sintetizada.
    Pense que deve ser possível a pessoa ler sua conclusão e se lembrar de todo o texto. Uma boa conclusão é memorável, no sentido de que a pessoa memoriza o seu conteúdo e consegue se recordar de todo o restante.
    Nesse fechamento, você retoma as teses que apresentou na introdução e que desenvolveu nos parágrafos de argumentação.
    O objetivo da conclusão é reafirmar a tese, fechar o ciclo do texto e mantê-lo coerente. 
    A função da conclusão de síntese na redação é relembrar o conteúdo, o ponto de vista tratado e convencer melhor o leitor.

Conclusão por solução:

    Esse tipo já existia, mas se popularizou com o Enem.
    Essa é a famosa proposta de intervenção, que nada mais é do que uma conclusão de redação com uma possível solução para o problema discutido no texto.
    Na conclusão da redação Enem, para uma nota 1000, devem estar presentes quatro elementos. Eles servem de guia.
    Responda a essas quatro perguntas no seu parágrafo final e você estará fazendo uma excelente conclusão por solução:

    1. O que é necessário para resolver o problema? (Explicação e Ação)
    2. Quem deve resolver o problema? (Agente social)
    3. Como o problema deve ser resolvido? (Meio ou modo)
    4. O que será conquistado com o fim do problema? (Finalidade)
    5. Detalhamento (explicação e exemplos) 

Ela é o oposto do primeiro tipo, que faz uma síntese. Ela não retoma as ideias anteriores, ela elabora uma consequência, a partir de tudo o que já foi dito.
Deduzir é extrair.
É um modelo mais difícil de se acertar, porque não pode deixar de fechar o texto e ainda mostra novas perspectivas para o futuro.
Ela é uma inferência também, afinal é o resultado do que vinha sendo construído. A partir das ideias e argumentos, tem-se um produto final: conclusão. 
Não se trata de apresentar ideias novas, mas de usar as mesmas ideias já tratadas, apontar, por dedução, o que pode acontecer se as coisas não mudarem ou se mudarem. 
De qualquer forma, o papel de uma conclusão é sempre melhorar a estratégia de convencimento do leitor. Deve sempre ser convincente e coerente.
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["dicas"])
def dicas(mensagem):
    texto = """Não use somente um dos tipos, você pode unir os estilos.
A conclusão, de certa forma, é a repetição da introdução, mas com palavras diferentes.
Cuidado para não repetir argumentos, isso não é necessário. O tempo da explicação deles já passou.
Você pode usar na conclusão algumas palavras chaves que usou no texto, as principais que definem sua ideia, ou sinônimos delas para não repetir.
"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["vocabulariochave"])
def vocabulariochave(mensagem):
    texto = """
-Logo
-Portanto  
-Pois
-Então
-Assim
-Por isso
-Por conseguinte
-De modo que
-Em vista disso
-Destarte"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["op11"])
def op11(mensagem):
    texto = """Componentes de uma conclusão:
        /tiposconclusao
        /dicas
        /vocabulariochave
        """
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que você quer? (Clique em uma opção)
    /op1 O que é uma redacao?
    /op2 Qual é o tipo de redação do enem?
    /op3 Como deve ser a estrutura de uma redaçao do enem?
    /op4 Como fazer uma redação?
    /op5 Como deve ser a estrutura de uma redação?
    /op6 O que é a introdução do enem?
    /op7 O que fazer na introdução do Enem?
    /op8 O que é o desenvolvimento?
    /op9 Como fazer desenvolvimento?
    /op10 Como fazer uma conclusão?
    /op11 O que fazer na conclusão?"""
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=["targumentativa"])
def targumentativa(mensagem):
    texto = """A tese nada mais é do que a sua opinião (o seu posicionamento) a respeito do tema e ela é a ideia principal da redação. 
    Em outras palavras: se você pudesse resumir a sua dissertação inteira (de 30 linhas, talvez) numa única frase, essa frase seria a tese (a ideia principal do texto).
    Afinal, nós devemos escrever uma dissertação inteira para comprovar a nossa tese.
    Existe uma maneira bem simples e prática de se fazer a tese da redação: pense quais serão as ideias principais de cada parágrafo de desenvolvimento. 
    Se a tese é a ideia principal da redação inteira, então a tese nada mais é do que a união das ideias principais de cada parágrafo de desenvolvimento. 
    Por exemplo: vamos supor que o tema proposto para a nossa redação seja "o papel da internet sobre a sociedade contemporânea". 
    Primeiro, se pergunte: quantos parágrafos de desenvolvimento eu vou escrever e quais serão as ideias principais de cada um? 
    Bem, uma dissertação geralmente tem dois ou três parágrafos de desenvolvimento (sendo que eu sou mais "fã" das dissertações com dois). 
    Então, vamos fazer uma redação com dois parágrafos de desenvolvimento, sendo que eu vou escrever o seguinte: no primeiro parágrafo de desenvolvimento, eu vou escrever que a internet é importante porque possibilita aos seus usuários a oportunidade de compartilharem o que quiserem para o mundo inteiro; 
    no segundo parágrafo, eu vou escrever que a internet globaliza as informações e que com ela é possível ter acesso ao conhecimento do mundo inteiro. 
    Ou seja: no primeiro parágrafo eu digo basicamente que uma pessoa pode "se abrir para o mundo" e no segundo parágrafo eu digo que o mundo pode "se abrir para uma pessoa".
    Então, com essas duas ideias (argumentos) em mente, eu construo a minha tese: "a internet tem o poder de não apenas possibilitar às pessoas a chance de compartilharem as suas ideias para o mundo inteiro, como também dá oportunidade aos seus usuários de terem acesso ao conteúdo do mundo todo". 
    Pronto: essa é a nossa tese. 
    Veja que a tese tem duas ideias (argumentos) e essas duas ideias darão origem aos parágrafos de desenvolvimento. Num parágrafo eu vou dizer que as pessoas podem se abrir para o mundo e no outro parágrafo eu vou dizer que o mundo se abre para as pessoas.
    Veja como poderia ficar a introdução:
    Inicialmente desenvolvida pelos militares, a internet ganhou o mundo e inaugurou uma nova cultura, fazendo parte do dia a dia das pessoas e conectando milhões de usuários ao redor do globo.
    Ela tem o poder de não apenas possibilitar às pessoas a chance de compartilharem as suas ideias em grande escala, como também dá oportunidade aos seus usuários de terem acesso ao conteúdo produzido a nível global.
    Isso significa que, com a internet, as pessoas se abrem para o mundo e o mundo se abre para elas."""
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=["modelos"])
def modelos(mensagem):
    texto = """ Modelos de redação são como mapas que te ajudam e agilizam no processo de criação da sua redação:
1° modelo: https://youtu.be/S0uT7UkCSSs

2° modelo: https://youtu.be/lUB55zMrsxM

3° modelo: https://youtu.be/cgVHKowutkE

4° modelo: https://youtu.be/9Ip7Q_R8f3o

5° modelo: https://youtu.be/Rs_Di73MWHM

6° modelo: https://youtu.be/wCwt18aNsQM

7° modelo: https://youtu.be/g2hs13geyDs

8° modelo: https://youtu.be/rgLH2YFWBWg

    
Temos também uma maravilhosa lista de temas de redação incríveis para você estudar!
> Acesse o link: https://drive.google.com/file/d/1bOe3ZsRcCWy8IVGIzUI8rTwyUaSUmKB-/view?usp=share_link """
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=["motivacional"])
def motivacional(mensagem):
    texto = """   Os textos motivadores devem ser lidos com muita atenção e, neste momento, palavras-chaves podem ser destacadas e usadas na redação, além do estabelecimento de relações entre todos eles ser fundamental, já que todos (de dois a três, geralmente) dizem respeito a um mesmo assunto (macro) e a um mesmo tema (micro).
Já que o ENEM afirma que cópias não são recomendadas (não só ele, como demais exames), a paráfrase (reescrever algo do seu modo, com as suas palavras, sem copiar propriamente) torna-se em recurso importante.
Um outro aspecto relevante dos textos motivadores do ENEM é a presença de textos não verbais nas propostas de redação.
-Charges (do francês charger, significa ação vigorosa ou ataque contra alguém ou a alguma coisa através de um desenho caricatural, com ou sem legenda, publicado em jornais, revistas, internet etc)
-Tirinhas (segmento de uma história em quadrinhos, normalmente com apenas três quadros), 
-Gráficos, infográficos, mapas e fotos são textos não verbais muito presentes não só no ENEM como em outras provas e a sua interpretação ajuda muito no momento de escrever, e neste sentido, no caso dos gráficos, infográficos e mapas, a matemática, a estatística, a geografia e a leitura de textos não verbais são essenciais.
    """
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """Escolha uma opção:
    /targumentativa - Como elaborar a tese argumentativa?
    /modelos - Indicação de modelos de redação
    /motivacional - Como ler textos motivadores?"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["textoc"])
def textoc(mensagem):
    texto = """Coesão e coerência são elementos textuais que andam juntos, porém não são a mesma coisa. Todo tipo de texto deve ser coeso e coerente. A coesão está relacionada à elementos gramaticais do texto, e será analisada e construída internamente; 
enquanto a coerência está relacionada à referências internas e externas, ou seja, ao conteúdo do texto.
Elementos de coesão podem ser identificados no texto, enquanto a coerência estará presente de forma global. Ou seja, é possível um texto pode estar coeso e incoerente.
Alguns pontos devem ser levados em conta para a escrita de um texto coeso, que vai facilitar a experiência do leitor. 
Em sua maioria, são referentes à gramática. A coesão tem a capacidade de auxiliar a memória do leitor. Ela permite que o texto esteja bem emendado.

1 – Evitar a Repetição de Termos:
Usando pronomes, sinônimos e expressões é possível escrever um texto mais clean, sem a repetição de palavras que torna a leitura cansativa. 
Sempre revise o seu texto prestando atenção se não está usando um termo excessivamente.
Caso esteja escrevendo no computador, uma forma simples de fazer isso é usar a ferramenta de busca (atalho Ctrl+F no teclado) e procurar pela palavra que acha que está muito repetida. 
A máquina vai te mostrar o número de vezes que o termo aparece na página e aí vai do seu bom senso, compare o tamanho do texto com o tanto de aparições da palavra. O dicionário de sinônimos online é um grande ajudante nessa etapa. 
A elipse é um recurso que ajuda nesse momento, já que toda uma oração pode ser ocultada por ela — caso caiba no contexto.

2 – Fazer Ligações entre as Frases e Assuntos:
Ao usar conectivos as frases e parágrafos criam uma ligação entre si. Isso fará com que uma sequência seja criada no texto e, consequentemente, na memória do leitor, deixando explícito que naquele momento será retomado um conceito ou ideia falado anteriormente. 
Essas seriam palavras de transição.


COMO CONSTRUIR UM TEXTO COERENTE


1 – Escrita Clara, Simples, Objetiva e Concisa:
   Não adianta discorrer sobre um assunto por três parágrafos se em três linhas você já falou tudo que precisava. Lembre-se que o tempo é precioso, assim como as linhas do seu texto. Escrever de forma concisa e objetiva, sem usar muitos termos difíceis e deixando claro qual é o ponto principal, vai fazer com que o leitor aproveite muito mais do conteúdo.

2 – Planejamento de Ideias:
   É importante que você planeje suas ideias antes de começar a escrever, para que façam sentido e todo o pensamento seja apresentado de forma estruturada. 
   A criação de uma linha de raciocínio fará com que você esteja muito mais alinhado com os tópicos que irá abordar, vindo a dividir o texto em ideias principais e secundárias, dando ênfase nas partes e informações mais relevantes.

3 – Harmonia entre Ideias e Fatos:
   Imagine a situação: você está lendo um texto argumentativo que introduz um termo científico. 
   Você vai pesquisar mais sobre o termo e descobre que o que está escrito no texto não tem nada a ver com a realidade. 
   Um texto coerente não deixaria isso acontecer, por isso é importante que você harmonize as ideias e os fatos, construindo frases verdadeiras e claras. 
   Pesquise sobre o que está escrevendo, pegue o máximo de referências que conseguir para montar sua própria ideia.
   Além disso, não seja contraditório. Se você afirmou uma ideia na introdução do texto, deve mantê-la até o fim.

4 – Referência no Assunto:
   Mostrar que domina o assunto apresentado é importante. Mas como fazer isso sem colocar o currículo no texto? Discorra sobre o tema de forma segura, quando possível, dê um exemplo pessoal, fale de um caso que conhece. No caso de narrativas, mostre que conhece aquela história colocando detalhes, aumentando descrições. 
   É muito bom ler um texto em que você sente a segurança e a credibilidade do autor.
   Além disso, apresentar informações já conhecidas sem desenvolvê-las é um recurso que tornará o texto superficial. Aposte em trazer novas informações ao leitor, novas teses, propostas e informações imprevisíveis.
   Estabelecer um sentido no texto, tornando-o harmonioso e apresentar as ideias originais de forma natural e segura fará com que o seu projeto possua coesão e coerência, respectivamente. Seja ele argumentativo ou narrativo, as lógicas interna e externa devem estar bem estruturadas, proporcionando uma boa leitura e compreensão da obra.
"""
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    texto = """Escolha uma opção:
    /textoc - Como elaborar um texto coeso?"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["ortografia"])
def ortografia(mensagem):
    texto = """Se você deseja ter uma boa ortografia veja o curso que encontramos para você:
Curso de ortografia:
Quer se aprimorar na escrita? Dê uma olhada nessa playlist de ortografia.
> https://youtube.com/playlist?list=PL5wMZazZQba8IWSuWIecdV66wupfSBfv7"""
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=["portugues"])
def portugues(mensagem):
    texto = """Curso de língua portuguesa:
Se você não é bom com a língua portuguesa, faça o seguinte curso para o seu aprimoramento. 
> https://youtube.com/playlist?list=PLfUYS8Z-l07wbRU_yot5O7E2TOKIL33kj """
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=["opcao4"])
def opcao4(mensagem):
    texto = """Escolha uma opção:
    /ortografia - Como ter uma boa ortografia?
    /portugues - Curso de língua portuguesa"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["repertorio"])
def repertorio(mensagem):
    texto = """Repertórios socioculturais são conhecimentos e referências adquiridos por meio de livros, frases, matérias, autores, pesquisas e muito mais.
Eles são usados em redações (e na vida) para apoiar opiniões e argumentações.
Desse modo, o repertório é usado para fundamentar, argumentar e fortalecer o que o candidato deseja defender. 
Além disso, são avaliados pelas bancas de correção de diversos vestibulares, como no Enem em que a Competência 3 avalia a capacidade do estudante de coerência e a plausibilidade entre as ideias apresentadas no texto, além da organização dos argumentos, apresentando o ponto de vista de forma clara e coerente.
Listamos uma série de repertórios coringas para você usar na sua redação:

Fonte: https://vestibulares.estrategia.com/portal/materias/redacao/repertorio-sociocultural-para-redacao-7-citacoes-coringa/#:~:text=bem%20na%20reda%C3%A7%C3%A3o-,O%20que%20%C3%A9%20Repert%C3%B3rio%20Sociocultural%3F,para%20apoiar%20opini%C3%B5es%20e%20argumenta%C3%A7%C3%B5es.
"""
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=["indicacao"])
def indicacao(mensagem):
    texto = """Aqui vai uma indicação de bons repertórios para melhorar sua redação:
    > https://youtu.be/GBv6WzFJpkw"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["opcao5"])
def opcao5(mensagem):
    texto = """Escolha uma opção:
    /repertorio - O que é repertório sociocultural?
    /indicacao - Indicação de repertórios coringas"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["proposta"])
def proposta(mensagem):
    texto = """A proposta de intervenção é a conclusão do texto dissertativo-argumentativo no Enem, em que o candidato deve apresentar uma solução para o problema discutido ao longo do texto.
Ela deve apresentar cinco elementos válidos. São eles: agente, ação, modo/meio, efeito/finalidade e detalhamento.
Para elaborar uma proposta de intervenção, é fundamental responder às seguintes questões: Quem vai realizar a ação? O que será feito? Como será feito? Por que será feito?
É importante ainda detalhar um desses elementos.
O texto dissertativo-argumentativo é um dos tipos de texto dissertativo e possui caráter persuasivo.
Na conclusão do texto dissertativo-argumentativo do Enem, a proposta de intervenção é obrigatória, enquanto nos demais textos argumentativos ela é uma das formas de concluir um texto.

Fonte: https://brasilescola.uol.com.br/redacao/proposta-intervencao-enem.htm

Veja este vídeo se quiser mais detalhes:
> https://youtu.be/21pDRrT_7hQ
"""
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=["opcao6"])
def opcao6(mensagem):
    texto = """Escolha uma opção:
    /proposta - Como elaborar proposta de intervenção"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["outro"])
def outro(mensagem):
    texto = """Não encontrou as respostas que procurava? 
    Acesse nosso link abaixo e envie sua dúvida:
    > https://forms.gle/zVxTRdfyRjE9kKxe8"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["comecar"])
def comecar(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Noção de estrutura
     /opcao2 Construção de argumentação
     /opcao3 Coesão e coerência
     /opcao4 Ortografia
     /opcao5 Repertório Sóciocultural
     /opcao6 Proposta de intervenção
     /outro"""
    bot.send_message(mensagem.chat.id, texto)


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """Olá! Seja Bem-Vindo(a).
Eu sou a Nayomi, para obter uma redação NOTA 1000 clique abaixo:
    /comecar"""
    bot.reply_to(mensagem, texto)


bot.polling()
