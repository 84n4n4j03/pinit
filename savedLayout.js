{
    "buttons": [
        {
            "color": "yellow",
            "description": "",
            "name": "config",
            "type": "<class 'configbutton.ConfigButton'>"
        },
        {
            "color": "thistle",
            "description": "",
            "name": "save",
            "type": "<class 'savebutton.SaveButton'>"
        },
        {
            "color": "#78db66",
            "description": "",
            "name": "git",
            "submenu": {
                "buttons": [
                    {
                        "color": "yellow",
                        "description": "",
                        "name": "config",
                        "type": "<class 'configbutton.ConfigButton'>"
                    },
                    {
                        "cmd": "git status",
                        "color": "#78db66",
                        "description": "",
                        "name": "git status",
                        "type": "<class 'actionbutton.ActionButton'>"
                    },
                    {
                        "cmd": "git branch",
                        "color": "#78db66",
                        "description": "",
                        "name": "git branch",
                        "type": "<class 'actionbutton.ActionButton'>"
                    }
                ],
                "name": "git",
                "type": "<class 'pinmenu.PinMenu'>"
            },
            "type": "<class 'menubutton.MenuButton'>"
        }
    ],
    "name": "mainMenu",
    "type": "<class 'mainmenu.MainMenu'>"
}