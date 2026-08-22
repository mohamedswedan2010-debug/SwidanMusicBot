import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from yt_dlp import YoutubeDL

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 البوت شغال!")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "اكتب اسم الأغنية:\n/play Believer"
        )
        return

    song = " ".join(context.args)

    try:
        with YoutubeDL({
            "quiet": True,
            "extract_flat": True,
        }) as ydl:
            result = ydl.extract_info(
                f"ytsearch1:{song}",
                download=False
            )

        video = result["entries"][0]

        await update.message.reply_text(
            f"🎵 {video['title']}\n{video['url']}"
        )

    except Exception:
        await update.message.reply_text(
            "❌ حصل خطأ أثناء البحث."
        )

async def pause(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏸️ الإيقاف المؤقت غير متاح حاليًا.")

async def resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("▶️ الاستكمال غير متاح حاليًا.")

async def skip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏭️ التخطي غير متاح حاليًا.")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏹️ الإيقاف غير متاح حاليًا.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("play", play))
app.add_handler(CommandHandler("pause", pause))
app.add_handler(CommandHandler("resume", resume))
app.add_handler(CommandHandler("skip", skip))
app.add_handler(CommandHandler("stop", stop))

app.run_polling()
