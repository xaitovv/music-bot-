import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import yt_dlp
TOKEN = os.getenv8925715908:AAFDYc3JzU-IUSMS5Kq4hIOVuvceCZZOU24
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 Musiqa nomini yozing!")
async def search_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    await update.message.reply_text(f"🔍 '{query}' qidirilmoqda...")
    ydl_opts = {'format': 'bestaudio/best','noplaylist': True,'quiet': True,'outtmpl': '%(title)s.%(ext)s','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch1:{query}", download=True)
        if 'entries' in info: info = info['entries'][0]
        mp3 = ydl.prepare_filename(info).rsplit('.',1)[0] + ".mp3"
        with open(mp3, 'rb') as audio:
            await update.message.reply_audio(audio=audio, title=info.get('title', query))
        os.remove(mp3)
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_music))
app.run_polling()
