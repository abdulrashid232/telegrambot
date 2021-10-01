from telegram import Update
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
    + "\nI  gives brief information about any movie from OMDb website."
    + "\nSend any movie name and get brief info about the year,actors, plot and ratings "
    + "from IMDb, Rotten Tomatoes, Metacritic and Internet Movie Database \nUse the command /help if you need any help."
    + "\nHave fun playing around")

 
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("This is a movie rating bot,"
    + "\nJust enter the  movie name and get brief info about the year,actors, plot and ratings. "
    + " For example 'ip man' and send to get info."
    + "\nHave fun playing around")



def search(update: Update, context: CallbackContext):
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
                   f"Poster:\n{movie_info['poster']}\n\n"
                   )
    else:
        message = f"Moive '{movie_name} not found on the omdb site, Please check you spelling errors and try again"

    update.message.reply_text(text=message)




def main():
    updater = Updater(Token)


    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    infor_handler = MessageHandler(Filters.text, search)
    dispatcher.add_handler(infor_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()