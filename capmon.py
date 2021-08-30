from bot.botBase import BotBase as Bot
from bot.utils.envia_msg.envia_msg_chat import Envia_Msg

from bot.cogs.events.eventReady import EventReady

cogs = []
cogs.append(EventReady)

def prepare(bot: Bot, send_msg: Envia_Msg ,cogs: list):
    for cog in cogs:
        bot.add_cog(cog(bot, send_msg))

if __name__ == "__main__":
    bot = Bot()   
    send_msg = Envia_Msg(bot)
    prepare(bot, send_msg, cogs)
    bot.run()