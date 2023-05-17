# ---------------------------------------------------------------------------------
# ( o.o )  🔓 Not licensed.
# ---------------------------------------------------------------------------------
# Commands:
# meta developer: @its_xuxanneynl
# scope: hikka_only
# ---------------------------------------------------------------------------------
from telethon.tl.types import Message
from .. import loader, utils


@loader.tds
class TTdownloader(loader.Module):
    """Simple module to download tt videos"""

    strings = {
        "name": "TT-downloader",
        "caption": "",

    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "caption",
                "",
                "Подпись под видео"
            )
        )

    @loader.command()
    async def tt(self, message: Message):
        """{link} Скачиваем видео с помощью @TIKTOKDOWNLOADROBOT"""
        args = utils.get_args(message)
        if not args:
            await message.respond("Ссылка не найдена!\nИспользуйте .tt {link}")
            return
        await message.edit(f"Скачиваю✨")
        chat_bot = 1598492699
        try:
            link = args[0]
            async with self.client.conversation(chat_bot) as conversation:
                await conversation.send_message(link)
                response1 = await conversation.get_response()
                try:
                    await message.delete()
                    await self.client.send_file(entity=message.to_id, file=response1, caption=self.config["caption"])
                except Exception as e:
                    await message.respond(f"{e}")
        except Exception as e:
            await message.respond(str(e))