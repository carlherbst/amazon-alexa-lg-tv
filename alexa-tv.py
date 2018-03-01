""" fauxmo_minimal.py - Fabricate.IO

    This is a demo python file showing what can be done with the debounce_handler.
    The handler prints True when you say "Alexa, device on" and False when you say
    "Alexa, device off".

    If you have two or more Echos, it only handles the one that hears you more clearly.
    You can have an Echo per room and not worry about your handlers triggering for
    those other rooms.

    The IP of the triggering Echo is also passed into the act() function, so you can
    do different things based on which Echo triggered the handler.
"""
import urllib
import time
import fauxmo
import logging
import time
import os
from debounce_handler import debounce_handler

logging.basicConfig(level=logging.DEBUG)

class device_handler(debounce_handler):
    """Publishes the on/off state requested,
       and the IP address of the Echo making the request.
       Note: can use alexa smarthome groups for aliases!
    """
    TRIGGERS = {
                    "tv": 52000,
                    "playback": 52001,
                    "mute": 52002,                        
                    "plex":52003,
                    "x play":52004,
                    "youtube": 52005,
                    "netflix": 52006,
                    "receiver": 52007,                    
                    "home theater": 52008,
                    "gaming pc": 52009,
                    "playstation": 52010,
                    "chromecast": 52011,
                    "snes": 52012,
                    "switch": 52013,
                    "giant bomb": 52014,
                    "giant bomb TV": 52015,
                    "twitch": 52016,
                    "archive script": 52017,
               }


    def act(self, client_address, state, name):
        print "State", state, "on ", name, "from client @", client_address

        #func dict might be a bit slower, but sure is a lot easier to read/add to
        

#giant bomb tv
#lgtv.py openBrowserAt https://www.youtube.com/watch?v=bgGohC9jIl8

#giant bomb latest videos
#lgtv.py openBrowserAt https://www.giantbomb.com/videos/latest/



        def tvPower(self, state):
            if(state):
                print "Sending magic packet to turn on"                
                os.system("python lgtv.py on")
            else:
                print "Requesting TV to turn off turn off"                
                os.system("python lgtv.py off")
            return True
        
        def switchPlayback(self, state):
            if(state):
                os.system("python lgtv.py inputMediaPlay")
                print "Playback set to RESUME"
            else:
                os.system("python lgtv.py inputMediaPause")
                print "Playback set to PAUSE"
            return True

        def switchMute(self, state):
            os.system("python lgtv.py mute " + str(state))
            print "Mute set to " + str(state)
            return True
        

        def switchPlex(self, state):
            if(state):
                os.system("python lgtv.py startApp cdp-30")
                print "Launched Plex"
            else:
                os.system("python lgtv.py closeApp cdp-30")
                print "Closed Plex"
            return True

        def switchXplay(self, state):
            if(state):
                os.system("python lgtv.py startApp com.itkey.plexclient")
                print "Launched X Play"
            else:
                os.system("python lgtv.py closeApp com.itkey.plexclient")
                print "Closed X Play"
            return True
        
        def switchYoutube(self, state):
            if(state):
                os.system("python lgtv.py startApp youtube.leanback.v4")
                print "Launched Plex"
            else:
                os.system("python lgtv.py closeApp youtube.leanback.v4")
                print "Closed Plex"
            return True
            
        def switchNetflix(self, state):
            if(state):
                os.system("python lgtv.py startApp netflix")
                print "Launched Netflix"
            else:
                os.system("python lgtv.py closeApp netflix")
                print "Closed Netflix"
            return True

        def switchToReceiver(self, state):
            os.system("python lgtv.py setInput HDMI_2")
            print "TV input set to HDMI 2 (receiver)"
            return True
        
        def switchToHomeTheater(self, state):
            switchToReceiver(self, True)
            #sleep to wait?
            urllib.urlopen("http://10.0.1.91/MainZone/index.put.asp?cmd0=PutZone_InputFunction/SAT/CBL")
            print "Receiver Input set to SAT/CBL (htpc)"
            return True
        
        def switchToGamingPC(self, state):
            switchToReceiver(self, True)
            #sleep to wait?
            #urllib.urlopen("http://10.0.1.91/MainZone/index.put.asp?cmd0=PutZone_InputFunction/SAT/CBL")
            print "Receiver Input set to ??? (Gaming PC)"
            return True
        
        def switchToPlaystation(self, state):
            switchToReceiver(self, True)
            #sleep to wait?
            urllib.urlopen("http://10.0.1.91/MainZone/index.put.asp?cmd0=PutZone_InputFunction/GAME")
            print "Receiver input set to GAME (ps4)"
            return True

        def switchToChromecast(self, state):
            self.switchToReceiver(self, True)
            #sleep to wait?
            #urllib.urlopen("http://10.0.1.91/MainZone/index.put.asp?cmd0=PutZone_InputFunction/GAME")
            print "Receiver input set to ??? (Chromecast)"
            return True

        def switchToSNES(self, state):
            os.system("python lgtv.py setInput HDMI_1")
            print "TV input set to HDMI 1 (snes)"
            return True

        def switchToSwitch(self, state):
            os.system("python lgtv.py setInput HDMI_3")
            print "TV input set to HDMI 3 (switch)"
            return True

        def switchToGiantBomb(self, state):
            os.system("python lgtv.py openBrowserAt 'https://www.giantbomb.com/videos/latest'")
            print "Launched Giant Bomb Latest Videos"
            return True

        def switchToGiantBombTV(self, state):
            os.system("python lgtv.py openBrowserAt 'https://www.youtube.com/watch?v=LOSQgBEf5ac'")
            print "Launched Giant Bomb Latest Videos"
            return True

        def switchToTwitch(self, state):
            os.system("python lgtv.py startApp com.gamestreams.app")
            print "Launched Giant Bomb Latest Videos"
            return True

        def runArchiveScript(self, state):
            os.system("$ARCHIVE_SCRIPT")
            print "Called archive script"
            return True



        actions = {
            "tv": tvPower,
            "playback": switchPlayback,
            "mute": switchMute,               
            "plex":switchPlex,
            "x play":switchXplay,
            "youtube": switchYoutube,
            "netflix": switchNetflix,
            "receiver": switchToReceiver,
            "home theater": switchToHomeTheater,
            "gaming pc": switchToGamingPC,
            "playstation": switchToPlaystation,
            "chromecast": switchToChromecast,
            "snes": switchToSNES,
            "switch": switchToSwitch,
            "giant bomb": switchToGiantBomb,
            "giant bomb TV": switchToGiantBombTV,
            "twitch": switchToTwitch,
            "archive script": runArchiveScript
        }

        actions[name](self, state)
        return True


if __name__ == "__main__":
    # Startup the fauxmo server
    fauxmo.DEBUG = True
    p = fauxmo.poller()
    u = fauxmo.upnp_broadcast_responder()
    u.init_socket()
    p.add(u)

    # Register the device callback as a fauxmo handler
    d = device_handler()
    for trig, port in d.TRIGGERS.items():
        fauxmo.fauxmo(trig, u, p, None, port, d)

    # Loop and poll for incoming Echo requests
    logging.debug("Entering fauxmo polling loop")
    while True:
        try:
            # Allow time for a ctrl-c to stop the process
            p.poll(100)
            time.sleep(0.1)
        except Exception, e:
            logging.critical("Critical exception: " + str(e))
            break

