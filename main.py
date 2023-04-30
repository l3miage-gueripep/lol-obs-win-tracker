import obspython as S
import text_changer
import get_game_state
import get_last_game_status


# might use events
# S.OBS_FRONTEND_EVENT_FINISHED_LOADING
# S.OBS_FRONTEND_EVENT_STREAMING_STARTED
# S.OBS_FRONTEND_EVENT_RECORDING_STARTING
# OBS_FRONTEND_EVENT_SCENE_CHANGED

print("script started")
was_playing = False
#start values at 0
win_amount = 0
lose_amount = 0
text_source = None #wait for program to load 
player_name = None
last_game_id = None

def get_last_game_id():
    return get_last_game_status.get_last_game_id(get_last_game_status.get_summoner_data(player_name)['puuid'])

def try_update_win_count():
    global player_name
    #check that a new game is found from the api
    new_game_id = get_last_game_id()
    #if a new game is found
    if(last_game_id != new_game_id):
        update_win_count()
    else:
        print("No new game found")

def update_win_count():
    global win_amount
    global lose_amount
    #update variables
    if(get_last_game_status.is_last_game_won(player_name)):
        win_amount += 1
    else:
        lose_amount += 1
    #update text
    text_changer.change_text(str(win_amount) + " - " + str(lose_amount))
    print("win number changed")
    S.timer_remove(try_update_win_count)

def find_game_end():
    global was_playing
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
        was_playing = True
    else:
        print("game not running")
        #if player is not playing and was playing it means game ended, so we start trying to update the win counter
        if was_playing:
            #adds a timer callback which triggers every 10 seconds.
            S.timer_add(try_update_win_count, 10000)
        was_playing = False

def on_event(event):
    if event == S.OBS_FRONTEND_EVENT_FINISHED_LOADING and text_source is None:
        #get the source after it finished loading
        print("obs loaded")
        text_changer.change_text("0 - 0") #reset the counter
    if event == S.OBS_FRONTEND_EVENT_SCENE_CHANGED:
        find_game_end()

def script_load(settings):
    S.obs_frontend_add_event_callback(on_event)

def script_description():
    "Changes the win count"
