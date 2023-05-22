from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="𝚃𝙷𝙸𝚂 𝙸𝚂 𝚒𝚜 𝙿𝙴𝚁𝚂𝙾𝙽𝙰𝙻 𝚄𝚂𝙴 𝙱𝙾𝚃 🙏,\n𝙳𝙾 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝙰𝙽𝚈 𝙾𝚃𝙷𝙴𝚁 𝙱𝙾𝚃𝚂?\n👇 𝙲𝙻𝙸𝙲𝙺 𝚃𝙷𝙴 𝙱𝚄𝚃𝚃𝙾𝙽 𝙱𝙴𝙻𝙾𝚆 𝙰𝙽𝙳 𝙹𝙾𝙸𝙽 𝙱𝙾𝚃𝙷 𝙲𝙷𝙰𝙽𝙽𝙴𝙻."
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🤖 𝙾𝚃𝙷𝙴𝚁 𝙱𝙾𝚃𝚂 🤖", url="https://t.me/iPepkornBots")
        ],[
        InlineKeyboardButton("🎉 𝙱𝙴𝚂𝚃 𝙳𝙴𝙰𝙻𝚂 🎉", url="https://t.me/TrueDealsMaster")
    ]])
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"👋Hii {msg.from_user.mention}\n<b>𝙼𝚈𝚂𝙴𝙻𝙵 @SimpleRenameBot \n\n𝙸 𝙰𝙼 𝚂𝙸𝙼𝙿𝙻𝙴 𝚁𝙴𝙽𝙰𝙼𝙴 𝙱𝙾𝚃 𝚆𝙸𝚃𝙷 𝙿𝙴𝚁𝚂𝙾𝙽𝙰𝙻 𝚄𝚂𝙰𝙶𝙴,\n𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝙸𝚂 𝙼𝙰𝙳𝙴 𝙱𝚈 <b><a href=https://t.me/iPepkornBots>𝚒𝙿𝚊𝚙𝚔𝚘𝚛𝚗𝙱𝚘𝚝𝚜</a></b>"                                     
    button= [[
        InlineKeyboardButton("📢 𝙹𝙾𝙸𝙽 𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 📢", url="https://t.me/iPapkon")
        ],[
        InlineKeyboardButton("🤖 𝙱𝙾𝚃𝚂 🤖", url="https://t.me/iPepkornBots"),
        InlineKeyboardButton("🎉 𝙳𝙴𝙰𝙻𝚂 🎉", url="https://t.me/TrueDealsMaster")
        ],[
        InlineKeyboardButton("ℹ️ 𝙷𝙴𝙻𝙿 ℹ️", callback_data="help"),
        InlineKeyboardButton("💫 𝙰𝙱𝙾𝚄𝚃 💫", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "just send a file and /rename <new name> with replayed your file\n\n"
    txt += "send photo to set thumbnail automatic \n"
    txt += "/view to see your thumbnail \n"
    txt += "/del to delete your thumbnail"
    button= [[        
        InlineKeyboardButton("🚫 𝙲𝙻𝙾𝚂𝙴", callback_data="del"),
        InlineKeyboardButton("⬅️ 𝙱𝙰𝙲𝙺", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Master=f"<a href=https://t.me/iPepkornBots>𝚒𝙿𝚊𝚙𝚔𝚘𝚛𝚗𝙱𝚘𝚝𝚜</a>"  
    txt=f"<b>𝙱𝙾𝚃 𝙽𝙰𝙼𝙴 : {me.mention}\n𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 : <a href=https://github.com/MrMKN>MrMKN</a>\n𝙱𝙾𝚃 𝚄𝙿𝙳𝙰𝚃𝙴 : <a href=https://t.me/iPapkon>𝚒𝙿𝚊𝚙𝚔𝚘𝚛𝚗</a>\n𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 : {Master}"                 
    button= [[        
        InlineKeyboardButton("🚫 𝙲𝙻𝙾𝚂𝙴", callback_data="del"),
        InlineKeyboardButton("⬅️ 𝙱𝙰𝙲𝙺", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


