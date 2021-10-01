from telegram import Update, ForceReply
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
import os
from omdb import movie_infor

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



def ratings(update: Update, context: CallbackContext):
    movie_name = update.message.text
    movie_info =movie_infor(movie_name)

    message = ""

    if movie_info:
        rating_text = f"IMDb Rating: {movie_info['imdb_ratings']}\n"
        for rating in movie_info['ratings']:
            rating_text += f"{rating['Source']}: {rating['Value']}\n"

        message = (f"{movie_info['title']} ({movie_info['year']}): \n\n" +
                   f"Plot:\n{movie_info['plot']}\n\n" +
                   f"Starring:\n{movie_info['actors']}\n\n" +
                   f"Ratings:\n{rating_text}"
                   )
    else:
        message = f"Moive '{movie_name} not found on the omdb site, Please check you spelling errors and try again"

    update.message.reply_text(text=message)




def main():
    updater = Updater(Token)


    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    ratings_handler = MessageHandler(Filters.text, ratings)
    dispatcher.add_handler(ratings_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()