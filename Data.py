#🪄🔎🔮💫♻️🚀🍁🎺🖥️⚔️🖌️🎧👻👹👨‍💻🧑‍💻👨‍✈️🕵️🤘👋🖐️🪄🎉✨🎞️🎀🎁♥️♦️🔊🎧🛠️🔒⚙️⛓️🔗📲📸📡🎥📷📹📼🔍🔍🔎📘📙📚🔖💵💶🪙💸💷💴

from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
🍁Hello {}

I m {}
Send /help Visit My Help Menu

🙈 For All Users 👇👇

🔥 Powered By mhmdwldnnnn ✓
☘️ Simple & Friendly BOT ✓
💥 Keep Original Appearance ✓
🎯 Group Supported ✓
⚡️ Fast Response ✓
✅ 24 Hour Active ✓
🤩 New OS ✓

▣————————————————————————▣

🚀Powerd By @mhmdwldnnnn

▣————————————————————————▣
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏛️ Return Home 🏛️", callback_data="home")],
        [InlineKeyboardButton("🔥 Dan Devolopers 🔥", url="https://t.me/mhmdwldnnnn")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("▣——————Subscribe——————▣", url="https://t.me/Disney_storeDan")],
        [
            InlineKeyboardButton("❔ How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🌺 About 🌺", callback_data="about")
        ],
        [InlineKeyboardButton("👨‍💻 Devoloper 👨‍💻", url="https://t.me/mhmdwldnnnn")],
        [InlineKeyboardButton("💬 Support 💬", url="https://t.me/musik_supportdan")],
    ]

    
    # Comming Soon

COMMING = "Song Plugin is Comming Soon.. \n Join [Update Channel](t.me/Disney_storeDan) And Get Updates"

COMMING2 = "Logo Plugin is Comming Soon.. \n Join [Update Channel](t.me/Disney_storeDan) And Get Updates"
    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -1002127258037` or `/forcesubscribe -1002111666674`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

🔅 **Available Commands** 🔅

⟫ /fsub - See current force subscribe chat
⟫ /fsub chat_id/username - Force users to join the particular chat
⟫ /settings - Change Group Settings
⟫ /id - Get the chat id of any group or channel
⟫ /about - About The Bot
⟫ /help - This Message
⟫ /start - Start the Bot
⟫ /hack - Hack Target Whatsapp Account
⟫ /song - Comming Soon..
⟫ /logo - Comming Soon..

📌**Note** - You can also use `/forcesubscribe` instead of `/fsub`
📌**Note** - Get All Updates [Here](t.me/Disney_storeDan)

🔥 Powerd By [Dan](t.me/mhmdwldnnnn)
    """

    # About Message
    ABOUT = """
**About This Bot** 

A Telegram Force Subscribing Bot by @fsubdanbot

🪄Powerd By : @mhmdwldnnnn

🍁Framework : [Pyrogram](docs.pyrogram.org)

🍁Language : [Python](www.python.org)

🍁Developer : @mhmdwldnnnn

🖥️ Host Sever : Unknow


    """
