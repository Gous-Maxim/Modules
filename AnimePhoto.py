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
class AnimePhoto(loader.Module):
    """Simple module to create photo into an anime style"""

    strings = {
        "name": "AnimePhoto",

    }


    @loader.command()
    async def pta(self, message: Message):
        """Обрабатываем картинки с помощью @qq_neural_anime_bot"""
        reply_msg = await message.get_reply_message()
        if not reply_msg or not reply_msg.photo:
            await message.respond("Ответ на фото не найден!")
            return
        await message.edit(f"Обрабатываю✨")

        chat_bot = 5894660331


        try:
            photo = await reply_msg.download_media()
            async with self.client.conversation(chat_bot) as conversation:
                await conversation.send_file(file=photo)

                response1 = await conversation.get_response()
                response2 = await conversation.get_response()
                response3 = await conversation.get_response()

                try:
                    await message.delete()
                    if response2.media and hasattr(response2.media, "photo") and response3.media and hasattr(
                            response3.media, "photo"):
                        await self.client.send_file(entity=message.to_id, file=response2.media)
                        await self.client.send_file(entity=message.to_id, file=response3.media)
                        dialog = await self.client.get_entity(chat_bot)
                        async for messages in self.client.iter_messages(dialog):
                            await self.client.delete_messages(dialog, messages)
                except Exception as e:
                    await message.respond(f"{e}")
        except Exception as e:
            await message.respond(str(e))
