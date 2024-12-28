from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import OWNER_ID

class Data:
    generate_single_button = [InlineKeyboardButton("★彡[ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ]彡★", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ", callback_data="home")]
    ]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ ᴀɴᴅ ᴍᴏʀᴇ ʙᴏᴛꜱ", url="https://t.me/Helpdesk_Chatsbot")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ❔", callback_data="help"),
            InlineKeyboardButton("★彡[ᴀʙᴏᴜᴛ]彡★", callback_data="about")
        ],
        [
            InlineKeyboardButton("sᴏᴜʀᴄᴇ", url="https://t.me/Tech_Shreyansh2"),
            InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/Tech_Shreyansh29")
        ],
        [InlineKeyboardButton("ᴍᴏʀᴇ ᴀᴍᴀᴢɪɴɢ ʙᴏᴛꜱ", url="https://t.me/Tech_Shreyansh2")],
    ]

HELP = """
✨ **Available Commands** ✨

/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/help - This Message
/about - About The Bot

For further assistance, feel free to reach out to the Developer!
"""

ABOUT = """
**🤖 About This Bot** 

Welcome to the **String Session Generator Bot**! 🎉

This bot allows you to generate Pyrogram and Telethon string sessions easily.

**Features:**
- 🔥 **Fast and Efficient**: Generate sessions quickly.
- 📚 **Open Source**: The source code is available for everyone to explore.
- 🌐 **Multi-Platform**: Works seamlessly across different platforms.

**Information:**
- **Source Code**: [Click Here](https://github.com/techyshreyansh/STRING-SESSION)
- **Framework**: [Pyrogram](https://docs.pyrogram.org)
- **Language**: [Python](https://www.python.org)
- **Developer**: [@ᴛᴇᴄʜ ꜱʜʀᴇʏᴀɴꜱʜ](https://t.me/Helpdesk_Chatsbot)
"""

# Filter function for commands
def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

# Start command
@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention}🦋,

Tʜɪs ɪs {me2},
Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.
ᴊɪsᴋᴇ ᴊᴀɪʙ ᴍᴇ ɢᴀɴᴅʜɪ  ᴄʜᴏʀɪ ᴜsᴋᴇ ᴘʏᴀᴀʀ ᴍᴇ ᴀᴀɴᴅʜɪ 🖤.

Mᴀᴅᴇ ᴡɪᴛʜ ❤ ʙʏ : [ᴛᴇᴄʜ ꜱʜʀʏᴀɴꜱʜ](https://t.me/Helpdesk_Chatsbot) !""",
        reply_markup=InlineKeyboardMarkup(Data.buttons),  # Use the full set of buttons
        disable_web_page_preview=True,
    )

# Help command
@Client.on_message(filters.command("help") & filters.private)
async def help_command(bot: Client, msg: Message):
    await msg.reply(
        text=HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )

# About command
@Client.on_message(filters.command("about") & filters.private)
async def about_command(bot: Client, msg: Message):
    await msg.reply(
        text=ABOUT,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )

# Handle button callbacks
@Client.on_callback_query(filters.regex("generate"))
async def handle_generate_callback(bot: Client, query: CallbackQuery):
    await query.message.reply("Session generation process started...")

@Client.on_callback_query(filters.regex("help"))
async def handle_help_callback(bot: Client, query: CallbackQuery):
    await query.message.reply(
        text=HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )

@Client.on_callback_query(filters.regex("about"))
async def handle_about_callback(bot: Client, query: CallbackQuery):
    await query.message.reply(
        text=ABOUT,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )

# Handle home button callback
@Client.on_callback_query(filters.regex("home"))
async def handle_home_callback(bot: Client, query: CallbackQuery):
    me2 = (await bot.get_me()).mention
    await query.message.reply(
        text=f"""Hᴇʏ {query.from_user.mention}🦋,

Tʜɪs ɪs {me2},
Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.
ᴊɪsᴋᴇ ᴊᴀɪʙ ᴍᴇ ɢᴀɴᴅʜɪ  ᴄʜᴏʀɪ ᴜsᴋᴇ ᴘʏᴀᴀʀ ᴍᴇ ᴀᴀɴᴅʜɪ 🖤.

Mᴀᴅᴇ ᴡɪᴛʜ ❤ ʙʏ : [ᴛᴇᴄʜ ꜱʜʀʏᴀɴꜱʜ](https://t.me/Helpdesk_Chatsbot) !""",
        reply_markup=InlineKeyboardMarkup(Data.buttons),  # Return to the main menu
        disable_web_page_preview=True,
    )
