from telegram import Update, ForceReply
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
import os
load_dotenv()

Token = os.getenv("Token")
Movie_api = os.getenv("Movie_api")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
     "Hi! Am a movie bot"
    + "What can I do?\n\nI  gives brief information about any movie from IMDb website "
    + "\nSend /rating movie_name to know the genre and rating of the movie.\nSend /search movie_name to"
    + "get the list of movies with a the same name.\nUse /help if you need any help."
    + "\nHave fun playing around")

 
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("This is a movie rating bot, But the bot isn't fully ready")



def rating(update: Update, context: CallbackContext):
    update.message.reply_text("hELLO")



def main():
    updater = Updater(Token)


    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))


    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, obtener))
    dispatcher.add_handler(CommandHandler("rating", rating))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()