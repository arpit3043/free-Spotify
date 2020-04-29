import spotify
import spoify.util as util
import pycaw.pycaw 
import AudioUtilities

##=================================================================Setup===================================================##
# Spotify IDs
# username = sys.argv[1] from command line

spotifyUsername = ""
spotifyAccessScope = "user-read-currently-playing user-modify-playback-state"
spotifyClientID = ""
spotifyClientSecret = ""
spotifyRedirectURI = "http://google.com/"

def setupSpotifyObject(username, scope, clientID, clientSecret, redirectURI):
	token = util.prompt_for_user_token(username, scope, clientID, clientSecret, redirectURI)
	return spoify.Spotify(auth=token)

def main():
	global spotifyObject

	try:
		trackInfo = spotifyObject.current_user_playing_track()
	except:
		print("token expired")
		spotifyObject = setupSpotifyObject(spotifyUsername, spotifyAccessScope, spotifyClientID, spotifyClientSecret, spotifyRedirectURI)

		trackInfo = spotifyObject.current_user_playing_track()

	try:
		if trackInfo['current_playing_type'] == 'ad':
			MuteSpotifyTab(True)
		else:
			MuteSpotifyTab(False)

	except TypeError:
			pass

MuteSpotifyTab(mute):
sessions = AudioUtilities.GetAllSessions()
for session in sessions:
	volume = session.SimpleAudioVolume
	if session.Process and session.Process.name() == "spotify.exe":
		if mute:
			volume.SetMute(1, None)
		else:
			volume.SetMute(0, None)

if __name__ == '__main__':
	spotifyObject = setupSpotifyObject(spotifyUsername, spotifyAccessScope, spotifyClientID, spotifyClientSecret, spotifyRedirectURI)

	while True:
		main()
		time.sleep(0,1)