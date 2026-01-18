def add_setting(settings, settings_tuple):
    key = settings_tuple[0].lower()
    value = settings_tuple[1].lower()

    if key in settings:
        return "Setting '{key}' already exists! Cannot add a new setting with this name."
    
    else:
        settings[key] = value
        return "Setting '{key}' added with '{value}' successfully!"
    
def update_setting(settings, settings_tuple):
    key = settings_tuple[0].lower()
    value = settings_tuple[1].lower()

    if key in settings:
        settings[key] = value
        return "Setting '{key}' updated to '{value}' succesfully!"
    
    else:
        return "Setting '{key}' does not exist! Cannot update a non-existing setting."
    
def delete_setting(settings, key):
    key = key.lower()
    
    if key in settings:
        del settings[key]
        return "Setting '{key}' deleted successfully!"
    
    else:
        return "Setting not found!"
    
def view_settings(settings):
    if not settings:
        return "No settings available."
    
    result = "Current User Settings"

    for key, value in settings.items():
        result += f"\n{key.capitalize()}: {value}"
    result += "\n"
    return result

# Testing the logic
test_settings = {}

print(add_setting(test_settings, ('theme', 'dark')))
print(delete_setting(test_settings, 'theme'))
print(add_setting(test_settings, ('notifications', 'on')))
print(update_setting(test_settings, ('notifications', 'off')))
print(view_settings(test_settings))