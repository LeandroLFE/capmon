**Projeto Capmon - PT-BR**

# Bem vindos ao projeto Capmon!

O Capmon é um bot desenvolvido para ser um mini-game de chat na plataforma Twitch onde hordas ocorrem de tempos em tempos nos canais ativos, onde viewers, também chamados Capaventureiros possuem a capacidade de tentar capturar estas criaturas utilizando comandos especificos. Com base no armazenamento das informações das criaturas capturadas, o funcionamento do bot estende-se a novas funções tais como:

 - Acumulo de "capcoins"
 - Capshop onde o capaventureiro pode gastar os capcoins em troca de itens 
 - Hordas elementais com diversas criaturas disponíveis 
 - Seleção de uma criatura como parceira, o capbuddy 
 - Utilização dos capbuddies em batalhas contra outros viewers do chat
 - Os capbuddies também são utilizados nas Capraids, onde uma criatura lendaria aparece para o chat tentar derrotar, ganhando capcoins, a chance de capturar a criatura lendária e pode ter a sorte de ganhar um item chamado capmove. 

No canal do bot https://www.twitch.tv/capmon tem uma descrição mais detalhada de cada comando


## Desenvolvedor:

LeandroLFE https://www.twitch.tv/lfeplay


# Instalação

```
pip3 install -r requirements.txt
```

Necessário arquivo .env na raiz do projeto contendo:

```
CLIENT_ID=twitch_client_id
CLIENT_SECRET=twitch_client_secret
OAUTH_TOKEN=oauth:token

BOT_USERNAME=bot_username

DB_NAME=db_name
DB_LOCATION=db_location
```

Tutorial iniciante para obter Client_ID e Client_secret na Twitch (inglês) https://dev.twitch.tv/docs/api

Entendendo mais sobre autenticação e geração do OAUTH token (inglês) https://dev.twitch.tv/docs/authentication#registration

Escopos necessários:

 - chat:edit
 - chat:read
 - whispers:edit
 - whispers:read

* Para enviar whispers eu tive que enviar um formulário para aumentar o limite do que o bot pode fazer, cumprindo seus respectivos requisitos: https://dev.twitch.tv/limit-increase

Este projeto utiliza a biblioteca Twitchio v2.0.6 que realiza a comunicação com a Twitch.
Documentação (inglês) https://twitchio.readthedocs.io/en/latest/quickstart.html


# Execução

- Arquivo setup_db.py -> setup do banco de dados (executar apenas 1 vez)
- Arquivo app_bot.py -> execução do bot


**Capmon Project - English**

# Welcome to Capmon project!

Capmon is a bot developed to be a mini chat game on the Twitch platform where hordes occur from time to time on the active channels, where viewers, also called Capadventurers have the ability to try to capture these creatures using specific commands. Based on storing the information of the captured creatures, the functioning of the bot extends to new functions such as:

   - Accumulation of "capcoins"
   - Capshop where the Capadventurer can spend capcoins in exchange for items
   - Elemental hordes with different creatures available
   - Selection of a creature as a partner, the capbuddy
   - Use of capbuddies on condition against other chat viewers
   - Capbuddies are also used in Capraids, where a legendary creature appears and the chat try to defeat it, earning capcoins, a chance to capture the legendary creature and may be lucky enough to win an item called capmove.

In the bot channel https://www.twitch.tv/capmon there is a more detailed description of each command.


## Developer:

LeandroLFE https://www.twitch.tv/lfeplay


# Instalation

```
 pip3 install -r requirements.txt
```

.env file is needed in project root that contains:


```
CLIENT_ID=twitch_client_id
CLIENT_SECRET=twitch_client_secret
OAUTH_TOKEN=oauth:token

BOT_USERNAME=bot_username

DB_NAME=db_name
DB_LOCATION=db_location
```

Getting started to get Client_ID and Client_secret in Twitch https://dev.twitch.tv/docs/api

More about auth process and generating OAUTH token https://dev.twitch.tv/docs/authentication#registration

Scopes required:

 - chat:edit
 - chat:read
 - whispers:edit
 - whispers:read

*To be able to send whispers I had to fill this form, fulfilling their respective requirements : https://dev.twitch.tv/limit-increase

This project uses the Twitchio v2.0.6 library that communicates with Twitch.
Documentation https://twitchio.readthedocs.io/en/latest/quickstart.html


# Run

- File setup_db.py -> database setup (execute 1 time only) 
- File app_bot.py -> execute bot
