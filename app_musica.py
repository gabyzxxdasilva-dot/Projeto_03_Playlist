import streamlit as st

musicas = {
    "Michael Jackson": {
        "Heaven can wait": "https://youtu.be/TDVlDUAIz5k?si=IZjlbS78RxItVBAV",
        "Thriller": "https://www.youtube.com/watch?v=4V90AmXnguw&list=RD4V90AmXnguw",
    },
    "Alee": {
        "Brenda": "https://www.youtube.com/watch?v=uQ_lWHy_q-Q",
        "Luz Cama e Ação": "https://www.youtube.com/watch?v=nqgUKAXlJ0k",
    },
    "Dfideliz": {
        "Mulher": "https://www.youtube.com/watch?v=XnobfnCsieA"
    },
}

st.sidebar.image("logo.png")
artista = st.sidebar.selectbox("Selecione o Artista", musicas.keys())
musicas_artistas = musicas[artista]
st.title(artista)
video,sobre = st.tabs(['video', 'sobre'])
with video:
    for musica in musicas_artistas.items():
        titulo, link = musica
        st.subheader(titulo)
        st.video(link)


with sobre: 
    if artista == "Michael Jackson":
        st.markdown("""
# Michael Jackson



## Quem foi Michael Jackson?

Michael Jackson (1958–2009) foi um cantor, compositor, dançarino e empresário norte-americano, amplamente reconhecido como o **"Rei do Pop"**. Sua influência transformou a música popular, a dança e a cultura pop em escala mundial. Ao longo de sua carreira, vendeu centenas de milhões de discos e tornou-se um dos artistas mais famosos da história da música.

## Início da Carreira

Michael começou sua trajetória artística ainda criança como integrante do grupo familiar **Jackson 5**, ao lado de seus irmãos. Seu talento vocal chamou atenção desde cedo, levando-o a iniciar uma carreira solo que rapidamente alcançou sucesso internacional.

## Principais Álbuns

### Off the Wall (1979)

Seu primeiro grande sucesso solo, misturando pop, disco e R&B.

### Thriller (1982)

Considerado o álbum mais vendido da história da música, com sucessos como:

- Billie Jean
- Beat It
- Thriller
- Human Nature

O álbum gerou sete singles de grande sucesso e revolucionou a indústria musical.

### Bad (1987)

Inclui clássicos como:

- Bad
- Man in the Mirror
- Dirty Diana
- The Way You Make Me Feel

O álbum estabeleceu diversos recordes de vendas e execuções nas rádios.

### Dangerous (1991)

Apresentou uma sonoridade mais moderna e trouxe sucessos como:

- Black or White
- Remember the Time
- Heal the World

O álbum consolidou ainda mais sua popularidade mundial.

## Contribuições para a Música

Michael Jackson revolucionou:

- Os videoclipes musicais;
- As performances ao vivo;
- As coreografias pop;
- A integração entre música, dança e espetáculo visual.

O videoclipe de **Thriller** é considerado um dos mais influentes da história.

## Danças Famosas

### Moonwalk

O passo de dança mais famoso de Michael Jackson, apresentado ao público em 1983 e imitado por artistas do mundo inteiro.

### Robot Dance

Movimentos mecânicos que ajudaram a definir seu estilo único de dança.

## Prêmios e Recordes

- Mais de uma dezena de prêmios Grammy.
- Recorde de 8 Grammys em uma única noite (1984).
- Álbum mais vendido da história com *Thriller*.
- Um dos artistas mais premiados e influentes de todos os tempos.

## Legado

Mesmo após sua morte em 25 de junho de 2009, Michael Jackson continua sendo uma das figuras mais influentes da música mundial. Suas canções, coreografias e videoclipes continuam inspirando artistas e fãs em todo o planeta.

## Curiosidades

- Seu apelido mais famoso era **King of Pop (Rei do Pop)**.
- O álbum *Thriller* continua sendo referência na indústria musical.
- Foi pioneiro na produção de videoclipes cinematográficos.
- Seu estilo de dança influenciou gerações de artistas em diversos países.

> **Frase marcante:** "A música é uma forma de unir as pessoas, independentemente de sua origem ou cultura."

---

### Meta descrição para SEO

*Michael Jackson foi um cantor, compositor e dançarino norte-americano conhecido como o Rei do Pop. Descubra sua história, carreira, álbuns, recordes e legado na música mundial.*
""", unsafe_allow_html=True)
    elif artista =="Alee":
        st.markdown("""
        # Alee

        ![Alee](https://portalrapmais.com/wp-content/uploads/2024/09/alee.jpg)

        ## Quem é Alee?

        **Alee**, nome artístico de **Alisson Vieira Silva**, é um rapper, cantor e compositor brasileiro nascido na Bahia. Considerado um dos principais nomes da nova geração do trap nacional, o artista ganhou destaque por misturar trap, R&B e hip-hop em músicas que abordam superação, ambição, relacionamentos e a realidade da juventude brasileira.

        Com milhões de reproduções nas plataformas digitais, Alee se consolidou como uma das vozes mais influentes da cena urbana atual.

        ## Início da Carreira

        Nascido em uma família de músicos, Alee teve contato com a música desde cedo. Seu pai é cantor, sua mãe trabalhou como backing vocal e seu tio é Denny Denan, vocalista da banda Timbalada.

        Antes de se dedicar à música, Alee praticou esportes como futebol e boxe. Sua aproximação com o rap aconteceu ainda na adolescência, influenciado por artistas internacionais e pela cultura hip-hop.

        Os primeiros lançamentos foram voltados para o R&B, mas com o passar do tempo ele encontrou sua identidade artística no trap.

        ## Ascensão no Trap Nacional

        Alee começou a ganhar notoriedade após participar de projetos importantes da cena underground, incluindo a mixtape **Jovens Pretos Milionários**.

        Seu estilo melódico, letras introspectivas e sonoridade moderna rapidamente conquistaram espaço entre os fãs do trap brasileiro.

        Atualmente, ele faz parte da gravadora **NADAMAL Records**, responsável por impulsionar diversos artistas da música urbana nacional.

        ## Principais Projetos

        ### Dias Antes do Caos (2024)

        Primeiro álbum de estúdio do artista.

        O projeto apresenta uma mistura de trap, R&B e elementos eletrônicos, explorando temas como:

        - Superação
        - Amor
        - Ambição
        - Crescimento pessoal
        - Realidade social

        O álbum alcançou milhões de reproduções poucos dias após o lançamento.

        ### Caos (2024)

        Sequência direta do projeto anterior.

        O álbum consolidou Alee como um dos grandes nomes do trap brasileiro, trazendo faixas que exploram sua trajetória, dificuldades e conquistas.

        **Destaques:**

        - PASSADO DE UM VILÃO
        - PARTY
        - ESTRESSE
        - ÚLTIMA VEZ

        ### CAOS DLX (2025)

        Versão expandida da trilogia "Caos".

        O projeto contou com participações de artistas importantes da cena nacional, incluindo:

        - MC Cabelinho
        - Filipe Ret
        - Klisman
        - Leviano

        O álbum acumulou mais de 100 milhões de reproduções nas plataformas digitais.

        ## Estilo Musical

        Alee combina diversos elementos musicais:

        - Trap Melódico
        - Hip-Hop
        - R&B
        - Emo Rap
        - Música Urbana Contemporânea

        Suas músicas costumam abordar:

        - Ascensão social
        - Saúde mental
        - Relacionamentos
        - Sonhos e ambições
        - Vivências da periferia

        Uma das características mais marcantes de seu trabalho é a mistura entre vulnerabilidade emocional e confiança pessoal.

        ## Influências

        Entre suas inspirações estão artistas nacionais e internacionais como:

        - Travis Scott
        - Juice WRLD
        - Djonga
        - Matuê
        - 50 Cent

        Essas referências ajudam a construir sua identidade sonora única dentro do trap brasileiro.

        ## Principais Músicas

        Alguns dos maiores sucessos de Alee incluem:

        - PASSADO DE UM VILÃO
        - PAGÃO
        - PARTY
        - TUDO DE NOVO
        - PANTHER
        - TAMBOR
        - ESTRESSE
        - GLOBAL

        ## Conquistas

        - Milhões de ouvintes nas plataformas de streaming.
        - Disco de Ouro com projetos da série "Caos".
        - Participação em grandes festivais nacionais.
        - Reconhecimento como uma das principais revelações do trap brasileiro.

        ## Curiosidades

        - Seu nome verdadeiro é **Alisson Vieira Silva**.
        - É sobrinho de Denny Denan, vocalista da Timbalada.
        - Começou a carreira musical cantando R&B.
        - É considerado uma das maiores apostas da música urbana brasileira.
        - Suas músicas acumulam centenas de milhões de reproduções.

        ## Legado e Impacto

        Mesmo sendo um artista jovem, Alee já possui grande influência na nova geração do trap nacional. Seu trabalho representa uma evolução do gênero no Brasil, misturando musicalidade, emoção e identidade cultural.

        Com uma carreira em constante crescimento, ele é visto como um dos artistas que estão moldando o futuro do hip-hop e do trap brasileiro.

        ---

        ### Meta descrição para SEO

        *Alee é um rapper, cantor e compositor brasileiro que se destacou no trap nacional com os álbuns Dias Antes do Caos, Caos e CAOS DLX. Conheça sua história, carreira, músicas e conquistas.*
        """, unsafe_allow_html=True)
    elif artista =="Dfideliz":
     st.markdown(""""
# DFideliz


## Quem é DFideliz?

**DFideliz**, nome artístico de **Daniel Fideliz**, é um rapper, cantor e compositor brasileiro que se tornou um dos principais nomes do trap nacional. Conhecido por suas letras marcantes, estilo autêntico e presença forte na cena urbana, o artista conquistou milhões de fãs em todo o Brasil.

Sua trajetória é marcada pela evolução constante dentro do rap e do trap, consolidando seu nome entre os artistas mais influentes da nova geração do hip-hop brasileiro.

---

## Início da Carreira

DFideliz começou sua carreira musical ainda jovem, influenciado pela cultura hip-hop e pelo rap nacional. Seus primeiros lançamentos chamaram a atenção do público underground por suas rimas criativas e seu estilo diferenciado.

Com dedicação e consistência, passou a ganhar destaque nas plataformas digitais, construindo uma base sólida de fãs e ampliando sua presença na cena musical brasileira.

---

## Ascensão no Trap Nacional

O crescimento de DFideliz ocorreu junto com a popularização do trap no Brasil. Suas músicas rapidamente alcançaram milhões de reproduções, tornando-o uma referência dentro do gênero.

Ao longo da carreira, colaborou com diversos artistas importantes da música urbana, fortalecendo ainda mais sua posição no cenário nacional.

---

## Estilo Musical

DFideliz combina elementos de diversos gêneros musicais:

- Trap
- Hip-Hop
- Rap
- R&B
- Música Urbana

Suas letras costumam abordar temas como:

- Superação
- Ambição
- Relacionamentos
- Realidade das ruas
- Conquistas pessoais
- Reflexões sobre a vida

---

## Principais Projetos

### Sou Rock'n Roll

Um dos projetos mais conhecidos de sua carreira, apresentando uma mistura de trap e rap moderno.

### Evolução Artística

Ao longo dos anos, DFideliz lançou diversos singles e projetos que demonstram sua evolução musical e versatilidade artística.

### Participações e Colaborações

O artista também participou de importantes colaborações com grandes nomes da cena urbana brasileira, ampliando seu alcance e relevância.

---

## Músicas de Destaque

Entre os maiores sucessos de DFideliz estão:

- Melhor Momento
- Sou Rock'n Roll
- Sem Neurose
- Oportunista
- Reflexos
- Pra Você
- Fases
- Te Encontrar

---

## Influências Musicais

DFideliz possui influências de diversos artistas nacionais e internacionais, incluindo:

- Racionais MC's
- Sabotage
- Travis Scott
- Future
- Kanye West

Essas referências ajudaram a moldar seu estilo único dentro da música urbana brasileira.

---

## Conquistas

- Milhões de reproduções nas plataformas digitais.
- Milhões de visualizações no YouTube.
- Presença em grandes festivais de música urbana.
- Reconhecimento como um dos principais nomes do trap brasileiro.
- Diversas colaborações com artistas de destaque nacional.

---

## Curiosidades

- Seu nome artístico é uma adaptação de seu sobrenome.
- É considerado um dos pioneiros da nova geração do trap brasileiro.
- Construiu sua carreira de forma independente nos primeiros anos.
- Possui uma base de fãs extremamente fiel nas redes sociais.
- É conhecido por seu estilo visual marcante e autenticidade artística.

---

## Legado

DFideliz desempenhou um papel importante no crescimento do trap nacional, ajudando a popularizar o gênero para um público cada vez maior. Sua trajetória inspira novos artistas e demonstra a força da música urbana brasileira.

Seu impacto na cultura do trap continua influenciando a nova geração de músicos e fãs em todo o país.

---

## Discografia em Destaque

| Ano | Projeto |
|------|----------|
| 2018 | Sou Rock'n Roll |
| 2019 | Singles e Colaborações |
| 2020+ | Novos Projetos e Participações |

---

> "A música é uma forma de transformar experiências em arte e conexão."

### Meta Descrição

*DFideliz é um rapper e cantor brasileiro reconhecido como um dos grandes nomes do trap nacional. Conheça sua história, carreira, músicas, álbuns, curiosidades e legado na música urbana brasileira.*
""", unsafe_allow_html=True)