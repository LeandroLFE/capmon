from bot.botBase import BotBase as Bot
from bot.cogs.events.eventReady import EventReady
from bot.cogs.events.eventJoin import EventJoin
from bot.cogs.envia_msg.envia_msg_chat import Envia_Msg
from bot.cogs.loop_hordas.geraHordas import GeraHordas
from bot.cogs.commands.bot_channel.capaventura import Capaventura
from bot.cogs.commands.user_channel.cap import Cap

cogs = []
cogs.append(EventReady)
cogs.append(EventJoin)
cogs.append(Envia_Msg)
cogs.append(GeraHordas)
cogs.append(Capaventura)
cogs.append(Cap)

def prepare(bot: Bot, cogs: list):
    for cog in cogs:
        bot.add_cog(cog(bot))

if __name__ == "__main__":
    bot = Bot()   
    prepare(bot, cogs)
    bot.run()