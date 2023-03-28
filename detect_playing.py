import obspython as S
import text_changer
import time
import get_game_state
import get_last_game_status


# might use events
# S.OBS_FRONTEND_EVENT_FINISHED_LOADING
# S.OBS_FRONTEND_EVENT_STREAMING_STARTED
# S.OBS_FRONTEND_EVENT_RECORDING_STARTING
# OBS_FRONTEND_EVENT_SCENE_CHANGED

print("script started")
last_playing_state = False
#start values at 0
win_amount = 0
lose_amount = 0
text_source = None #wait for program to load 
player_name = None
last_game_id = None

def get_last_game_id():
    return get_last_game_status.get_last_game_id(get_last_game_status.get_summoner_data(player_name)['puuid'])


def update_win_count():
    global last_playing_state
    global win_amount
    global lose_amount
    global text_source
    global player_name
    global last_game_id

    if get_game_state.is_playing():
        if player_name is None:
            player_name = get_game_state.get_active_player_name()
            last_game_id = get_last_game_id()
        print("game running")
        last_playing_state = True
    else:
        print("game not running")
        #if player is not playing and was playing it means game ended, so the win counter is changed
        #to make it more reliable checking if last game is a new game with api would be great
        if(last_playing_state):
            #check that a new game is found from the api
            new_game_id = get_last_game_id()
            #if a new game is found
            if(last_game_id != new_game_id):
                #upgrade counter
                if(get_last_game_status.is_last_game_won(player_name)):
                    win_amount += 1
                else:
                    lose_amount += 1
                text_changer.change_text(str(win_amount) + " - " + str(lose_amount))
                print("win number changed")
            else:
                print("No new game found")
        last_playing_state = False

def on_event(event):
    if event == S.OBS_FRONTEND_EVENT_FINISHED_LOADING and text_source is None:
        #get the source after it finished loading
        print("obs loaded")
        text_changer.change_text("0 - 0") #reset the counter
    if event == S.OBS_FRONTEND_EVENT_SCENE_CHANGED:
        update_win_count()

def script_load(settings):
    S.obs_frontend_add_event_callback(on_event)

def script_description():
    "Changes the win count"
