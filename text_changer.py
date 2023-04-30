import obspython as obs

# Identify the name or ID of the text source



def change_text(new_text):
    source = obs.obs_get_source_by_name("Ratio win")
    # Retrieve a handle to the source
    if source is not None:
        # Create a new settings object
        data = obs.obs_data_create()

        # Set the text key to a new value
        obs.obs_data_set_string(data, "text", new_text)

        # Update the source settings
        obs.obs_source_update(source, data)

        # Release the settings object
        obs.obs_data_release(data)

        # Release the source handle
        obs.obs_source_release(source)
    else:
        print(f"Could not find source given")



#obs
def change_pressed(props, prop):
    change_text("bonjour")

#description shown in obs
def script_description():
    return "changes the text to a new value"

#
def script_properties():  # ui
    props = obs.obs_properties_create() # typically this is used to automatically generate user interface widgets
    obs.obs_properties_add_button(props, "button", "Change text value", change_pressed)
    return props
