# Build a User Configuration Manager
# In this lab, you will build a User Configuration Manager that allows users to manage their settings such as theme, language, and notifications. You will implement functions to add, update, delete, and view user settings.
#
# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.
#
# User Stories:
#
# You should define a function named add_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair.
#
# The add_setting function should:
#
# Convert the key and value to lowercase.
# If the key exists, return Setting '[key]' already exists! Cannot add a new setting with this name.
# If the key doesn't exist, add the key-value pair to the given dictionary of settings and return Setting '[key]' added with value '[value]' successfully!
# The messages returned should have the key and value in lowercase.
# You should define a function named update_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair.
#
# The update_setting function should:
#
# Convert the key and value to lowercase.
# If the key exists, update its value in the given dictionary of settings and return Setting '[key]' updated to '[value]' successfully!
# If the key doesn't exist, return Setting '[key]' does not exist! Cannot update a non-existing setting.
# The messages returned should have the key and value in lowercase.
# You should define a function named delete_setting with two parameters representing a dictionary of settings and a key.
#
# The delete_setting function should:
#
# Convert the key passed to lowercase.
# If the key exists, remove the key-value pair from the given dictionary of settings and return Setting '[key]' deleted successfully!
# If the key does not exist, return Setting not found!
# The messages returned should have the key in lowercase.
# You should define a function named view_settings with one parameter representing a dictionary of settings.
#
# The view_settings function should:
#
# Return No settings available. if the given dictionary of settings is empty.
# If the dictionary contains any settings, return a string displaying the settings. The string should start with Current User Settings: followed by the key-value pairs, each on a new line and with the key capitalized, and the string should end with a newline character after the last setting. For example, view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}) should return:
# Current User Settings:
# Theme: dark
# Notifications: enabled
# Volume: high
#
# For testing the code, you should create a dictionary named test_settings to store some user configuration preferences.
#
# Tests:
# Passed:1. You should create a dictionary named test_settings and add some values to it.
# Passed:2. You should define a function named add_setting.
# Passed:3. The add_setting function should have two parameters.
# Passed:4. add_setting should convert the key to lowercase.
# Passed:5. add_setting should convert the value to lowercase.
# Passed:6. add_setting({'theme': 'light', 'language': 'English'}, ('THEME', 'dark')) should return the error message Setting 'theme' already exists! Cannot add a new setting with this name.
# Passed:7. add_setting({'theme': 'light'}, ('volume', 'high')) should add a new key-value pair and return the success message Setting 'volume' added with value 'high' successfully!
# Passed:8. add_setting should correctly add the given key-value pair to the dictionary.
# Passed:9. You should define a function named update_setting.
# Passed:10. The update_setting function should have two parameters.
# Passed:11. The update_setting function should convert the key to lowercase.
# Passed:12. The update_setting function should convert the value to lowercase.
# Passed:13. update_setting({'theme': 'light', 'language': 'English'}, ('theme', 'dark')) should update an existing key and return the success message Setting 'theme' updated to 'dark' successfully!
# Passed:14. update_setting({'theme': 'light'}, ('volume', 'high')) should return the error message Setting 'volume' does not exist! Cannot update a non-existing setting. when the key doesn't exist.
# Passed:15. update_setting should correctly update the given key-value pair in the dictionary.
# Passed:16. You should define a function named delete_setting.
# Passed:17. The delete_setting function should have two parameters.
# Passed:18. delete_setting should convert the key to lowercase.
# Passed:19. delete_setting({'theme': 'light', 'language': 'English'}, 'theme') should remove the existing key and return the success message Setting 'theme' deleted successfully!
# Passed:20. delete_setting should return the error message Setting not found! when the key doesn't exist.
# Passed:21. delete_setting should correctly remove the given key from the dictionary.
# Passed:22. You should define a function named view_settings.
# Passed:23. The view_settings function should have one parameter.
# Passed:24. view_settings should return the message No settings available. if the given dictionary is empty.
# Passed:25. view_settings should return formatted settings for a non-empty dictionary.
# Passed:26. view_settings should capitalize the first letter of each setting name.
# Passed:27. view_settings should display the correct results and end with a newline character.

test_settings = {
    "theme":"dark",
    "language":"english"
}

def add_setting(dictionary, tupple):
    key, value = tupple
    key = key.lower()
    value = value.lower()
    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dictionary, tupple):
    key, value = tupple
    key = key.lower()
    value = value.lower()
    if key in dictionary:
        dictionary[key] = value
        return f"Setting '{key}' updated to 'dark' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary, string):
    string = string.lower()
    if string in dictionary:
        dictionary.pop(f'{string}')
        return f"Setting '{string}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(setting):
    if len(setting) == 0:
        return "No settings available."
    else:
        result = "Current User Settings:\n"
        for key, item in setting.items():
            result = result + key.capitalize() + ": " + item +"\n"
        return result
print(add_setting({'theme': 'light'}, ('volume', 'high')))
print(update_setting({'theme': 'light', 'language': 'English'}, ('theme', 'dark')))
print(delete_setting({'theme': 'light', 'language': 'English'}, 'THEME'))
print(view_settings({'theme': 'dark', 'language': 'English', 'notifications': 'enabled', 'volume': 'high'}))
