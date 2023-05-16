__version__ = (1, 0, 0)
# ---------------------------------------------------------------------------------
# ( o.o )  🔓 Not licensed.
# ---------------------------------------------------------------------------------
# Commands:
# meta developer: @its_xuxanneynl
# scope: hikka_only
# ---------------------------------------------------------------------------------
import asyncio
from telethon.tl.types import Message
from .. import loader, utils

@loader.tds
class UsersTag(loader.Module):
    """Tagging modules"""
    strings = {
        "name": "UsersTag",

    }


    @loader.tag()
    async def usertagcmd(self, event: Message):
        """Легитно тегаем всех пользователей чата!"""
        await event.delete()
        global stop_tagging
        stop_tagging = False
        args = utils.get_args(event)
        if not args:
            deplay = 2
        else:
            deplay = float(args[0])

        if len(args) > 1:
            text = " ".join(args[1:])
        else:
            text = " "
        try:
            chat_id = event.chat_id
            participants = await self.client.get_participants(chat_id)
            for users in participants:
                if 'stop_tagging' in globals() and stop_tagging:
                    break  # exit the loop if stop_tagging is True
                if users.username:
                    if not users.bot:
                        try:
                            await event.respond(f"@{users.username} {text}")
                            await asyncio.sleep(deplay)
                        except Exception as e:
                            await event.respond(f"Error:"
                                            f"{e}")
                else:
                    try:
                        await event.respond(f'<a href="tg://user?id={users.id}">{users.first_name}</a> {text}')
                        await asyncio.sleep(deplay)
                    except Exception as e:
                        await event.respond(f"Error:"
                                            f"{e}")
                        pass
            await event.respond(f"Я усталь(.")
        except ValueError:
            pass

    async def stopcmd(self, event: Message):
        """Стопнуть цикл тега"""
        await event.delete()
        global stop_tagging
        stop_tagging = True
        await event.respond("Стопаю...")