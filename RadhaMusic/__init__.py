from RadhaMusic.core.bot import AMBOTOP
from RadhaMusic.core.dir import dirr
from RadhaMusic.core.git import git
from RadhaMusic.core.userbot import Userbot
from RadhaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = AMBOTOP()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
