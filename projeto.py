import telebot

CHAVE_API = "5971940889:AAGrltLY_AMm0Swwr-o8uaKmilhZsBJiM20"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["op1"])
def op1(mensagem):
    texto = """
    A redação é usada para produzir roteiros, criar relatórios, documentos, no jornalismo, entre outros. Sempre que se necessite apresentar um tema de forma estruturada e com mais descrição, a redação se faz essencial.
    Desde que a escrita foi inventada que a redação se faz presente na cultura da civilização. E ela é considerada hoje como algo que faz parte do campo artístico literário.
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["op2"])
def op2(mensagem):
    texto = """No Enem, a redação cobrada é do tipo dissertativo-argumentativo. A diferença é que também é exigida a apresentação de uma proposta de intervenção social para solucionar o problema apresentado no tema.
"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["op3"])
def op3(mensagem):
    texto = """ A redação dissertativa é um gênero caracterizado pela defesa de uma ideia. No Enem, o formato exigido é o dissertativo-argumentativo.
     Isso significa que o candidato deve construir o texto pautado em dados e fatos. Por isso, é fundamental prestar muita atenção no enunciado e, principalmente, no tema da redação.
     Uma redação do ENEM deve ter pelo menos 30 linhas, com isso, o ideal é que a sua redação tenha 4 parágrafos:
     -1 para introdução (com 7 linhas); 
     -2 para desenvolvimento (com 7 linhas cada); 
     -1 para conclusão (com 9 linhas)."""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["op4"])
def op4(mensagem):
    texto = """Veja estes vídeos e aprenda a fazer uma redação nota 1000:
    https://youtu.be/eI8R8Eyv9vQ
    
    https://youtu.be/MeKHJVPNV30
    
    
    Cursos gratuitos de redação:
    https://youtube.com/playlist?list=PLhFNxzLJLH3vMVikOGLmorhohcG0Bk2ow
    
    https://youtube.com/playlist?list=PLofmLAJWpYDfpURLqCNg4a4PjVcPpH1gE
"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["op5"])
def op5(mensagem):
    texto = """ A estrutura de uma redação dissertativa-argumentativa é composta por três partes: introdução, desenvolvimento e conclusão.
   O modelo de estrutura de redação que sugerimos aqui é de 4 parágrafos: um de introdução, dois de desenvolvimento e um de conclusão. Tanto a introdução quanto a conclusão necessitam sempre de apenas um parágrafo.
   Enquanto isso, o desenvolvimento tem um número variável de parágrafos.
   Não existe nenhuma regra que exija que sua redação tenha 4 parágrafos, mas essa é uma dica que a gente dá tendo em vista que a maior parte das redações nota mil do Enem apresentam dois parágrafos de desenvolvimento."""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["op6"])
def op6(mensagem):
    texto = """Não é sem razão que o primeiro parágrafo da estrutura de uma redação é chamado de introdução, pois é nessa parte do texto que você vai expor (apresentar) as principais questões a serem abordadas no restante do texto.
    No primeiro parágrafo, o leitor terá uma dimensão geral do assunto e vai entender as razões pelas quais a discussão do problema é relevante.
"""
    bot.send_message(mensagem.chat.id, texto)


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
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["contextualizacao"])
def contextualizacao(mensagem):
    texto = """  A contextualização ou assunto é algo mais abrangente do que o tema, mas que está conectado a ele.
     Por exemplo: o tema da redação de 2018 foi “a manipulação do usuário pelo controle de dados na internet”. Nesse caso, o contexto poderia ser sobre meios de comunicação, redes sociais, internet em geral, privacidade, entre outras possibilidades.
     Além disso, o contexto é um bom lugar para você citar algum repertório sociocultural, como um livro, um filme, uma música, um dado histórico ou estatístico.
"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["tema"])
def tema(mensagem):
    texto = """Depois de fazer a contextualização, você deve demonstrar como o contexto está ligado ao tema.
    Tente não copiar o tema de forma literal. Em vez disso, tente escrever com suas palavras. Mas não esqueça de que todos os elementos do tema precisam estar presentes.
    Utilizando o exemplo anterior, você deve lembrar de mencionar a “manipulação”, o “controle de dados” e a “internet”.
"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["tese"])
def tese(mensagem):
    texto = """Em seguida, você não pode esquecer de escrever a sua tese. A tese ou objetivo do texto é aquilo que você pretende defender ao longo da redação. Essa é uma das partes mais importantes de toda a sua redação.
        A fim de definir qual será a sua tese, você pode se perguntar: “o que eu acho sobre o tema?”. Partindo da sua resposta, você vai conseguir formular o objetivo do seu seu texto, ou seja, sua tese.
"""
    bot.send_message(mensagem.chat.id, texto)


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
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["naofazer"])
def naofazer(mensagem):
    texto = """O principal cuidado que você deve ter ao escrever a introdução do seu texto é não misturar os assuntos.
    A pluralidade de ideias deixa o texto poluído e o leitor confuso. E ainda: não mencione nenhum fato na introdução que não será explorado ao longo do texto.
    Foque na sua tese principal.
    É recomendável evitar períodos longos no primeiro parágrafo.
    O espaço para produzir orações mais longas é o desenvolvimento. E mesmo assim, esse recurso deve ser usado com bastante critério.
"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["op7"])
def op7(mensagem):
    texto = """Componentes de uma introdução:
    /contextualizacao
    /tema
    /tese
    /perguntas
    /naofazer"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["op8"])
def op8(mensagem):
    texto = """O desenvolvimento da redação é uma das partes que compõem a estrutura do texto, sendo os outros a introdução e a conclusão. O desenvolvimento também é a parte com mais conteúdo da redação.
   Isso porque é dentro dele que você precisa defender o seu ponto de vista sobre a problemática apresentada usando argumentos bem embasados.
   O mais comum é que a introdução leve um parágrafo, o desenvolvimento seja apresentado em dois e que a conclusão amarre todo o texto em um parágrafo.
   """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["argumentacao"])
def argumentacao(mensagem):
    texto = """Conheça bem os tipos de argumentos:

É fundamental que você conheça os variados tipos de argumento para escolher aquele que for mais adequado ao tema e aos seus conhecimentos sobre o assunto. Abaixo você conhecerá cada um deles e encontrará exemplos práticos.

Argumento de Exemplificação:

   Ele pode ser usado para explicitar o argumento através de um exemplo. Em um tema como a persistência do racismo na sociedade brasileira o argumento de exemplificação que pode ser utilizado é o caso do músico negro que foi morto com 80 tiros disparados pelo exercito brasileiro no Rio de Janeiro. Esse argumento serve para embasar que o preconceito racial persiste na sociedade, visto a suspeita que um homem negro levantou porque foi confundido com criminosos.

Argumento de Autoridade:

   É a utilização da fala de uma figura reconhecida sobre o assunto, ou até mesmo o que essa personalidade representa para o tema em questão.
   Por exemplo, ainda dentro do tema sobre racismo, é cabível citar Nelson Mandela, visto que ele foi um advogado e militante importantíssimo para a superação dos preconceitos e da segregação racial na África do Sul. É ainda mais interessante citar uma frase que ele tenha dito sobre o assunto, como “Ninguém nasce odiando o outro pela cor de sua pele, ou por sua origem, ou sua religião." de seu livro Longo Caminho para a Liberdade.

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
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["conectivos"])
def conectivos(mensagem):
    texto = """É fundamental que você conheça os conectivos e saiba utilizá-los de maneira adequada.
   Além deles serem necessários para que você consiga 200 pontos na competência 4 do ENEM, os conectivos são capazes de trazer coesão e coerência à sua redação."""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["topicofrasal"])
def topicofrasal(mensagem):
    texto = """   O tópico frasal é a ideia central do seu argumento, aquilo que você acredita ser a situação-problema relacionada ao tema e que será o foco de discussão do parágrafo.
   É uma frase breve que sintetiza o argumento que você vai desenvolver ao longo do parágrafo.
"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["problematizacao"])
def problematizacao(mensagem):
    texto = """ Depois de produzir um tópico frasal com o argumento, é hora de desenvolvê-lo.
    Por isso, não esqueça que a redação do ENEM sempre trata de um problema e exige que o candidato se posicione diante dele.
    Ofereça como exemplo informações como citações, dados estatísticos, entre outros e problematize, ou seja, lance um olhar crítico ao analisá-los.
"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["contextualizacao"])
def contextualizacao(mensagem):
    texto = """Além de fazer a problematização do tema com argumentos, é muito importante que você contextualize, ou seja, traga um repertório sociocultural legitimado, pertinente e produtivo.
    O repertório é o conhecimento que você adquiriu ao longo da vida escolar - em disciplinas como história, matemática, literatura, etc - ou pessoal, como filmes, livros e séries.
    Mas não se esqueça: eles devem ter relação com o assunto abordado!"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["paragrafos"])
def paragrafos(mensagem):
    texto = """Conclua o parágrafo:
    É fundamental que seu parágrafo, assim como a sua redação, apresente início, meio e fim. Por isso, faça a conclusão da ideia do parágrafo.
    Se você apresentou seu argumento e trouxe um dado estatístico para comprová-lo, a conclusão é o momento em que você reafirma seu posicionamento e relaciona as duas informações, seu posicionamento através do argumento e a informação apresentada.

    Faça conexões:
    É muito importante que você não apresente somente um parágrafo, visto que a estrutura do seu texto deve ser a dissertativa-argumentativa.
    Por isso, tente relacionar as informações do primeiro parágrafo com o segundo para demonstrar que você é organizado e possui um projeto de texto.
"""
    bot.send_message(mensagem.chat.id, texto)


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
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["op10"])
def op10(mensagem):
    texto = """ A conclusão finaliza um texto, concentra as ideias e apresenta um resumo. 
    Para saber como fazer a conclusão da redação Enem, entenda como apresentar uma proposta de intervenção com os elementos essenciais."""
    bot.send_message(mensagem.chat.id, texto)


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
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["dicas"])
def dicas(mensagem):
    texto = """Não use somente um dos tipos, você pode unir os estilos.
A conclusão, de certa forma, é a repetição da introdução, mas com palavras diferentes.
Cuidado para não repetir argumentos, isso não é necessário. O tempo da explicação deles já passou.
Você pode usar na conclusão algumas palavras chaves que usou no texto, as principais que definem sua ideia, ou sinônimos delas para não repetir.
"""
    bot.send_message(mensagem.chat.id, texto)


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
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["op11"])
def op11(mensagem):
    texto = """Componentes de uma conclusão:
        /tiposconclusao
        /dicas
        /vocabulariochave
        """
    bot.send_message(mensagem.chat.id, texto)


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
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, ")


@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu! mandou um abraço de volta")


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Noção de estrutura
     /opcao2 Construçãode argumentação
     /opcao3 Coesão e coerência
     /opcao4 Ortografia
     /opcao5 Repertório Sóciocultural
     /opcao6 Proposta de intervenção
     /outro
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)


bot.polling()
