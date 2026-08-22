import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 البوت شغال!")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "🎵 اكتب اسم الأغنية بعد الأمر\nمثال:\n/play Believer"
        )
        return

    song = " ".join(context.args)
    await update.message.reply_text(f"🎵 جاري تشغيل: {song}")

async def pause(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏸️ تم إيقاف الأغنية مؤقتًا")

async def resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("▶️ تم استكمال الأغنية")

async def skip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏭️ تم تخطي الأغنية")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏹️ تم إيقاف التشغيل")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("play", play))
app.add_handler(CommandHandler("pause", pause))
app.add_handler(CommandHandler("resume", resume))
app.add_handler(CommandHandler("skip", skip))
app.add_handler(CommandHandler("stop", stop))

app.run_polling()
