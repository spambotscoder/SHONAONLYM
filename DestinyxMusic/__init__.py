from DestinyxMusic.core.bot import destiny
from DestinyxMusic.core.dir import dirr
from DestinyxMusic.core.git import git
from DestinyxMusic.core.userbot import Userbot
from DestinyxMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
# git()
dbb()
heroku()

app = destiny()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()


