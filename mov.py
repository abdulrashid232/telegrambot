from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
import os
load_dotenv()

Token = os.getenv("Token")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
     "Hi! Am a movie bot"
    + "What can I do?\n\nI  gives brief information about any movie from IMDb website "
    + "\nSend /rating movie_name to know the genre and rating of the movie.\nSend /search movie_name to"
    + "get the list of movies with a the same name.\nUse /help if you need any help."
    + "\nHave fun playing around")

 
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("This is a movie rating bot, But the bot isn't fully ready")


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def search(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("This is a command used to search for movies. NB: still in working progress.......")

def rating(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("This a command use to get movie ratings from imdb. NB: still in working progress.......")

def main() -> None:
    updater = Updater(Token)


    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dispatcher.add_handler(CommandHandler("search", search))
    dispatcher.add_handler(CommandHandler("rating", rating))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()