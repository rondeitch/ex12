MIN_WIDTH, MIN_HEIGHT = 550, 550

FONTS = {
    "primary": "Segoe UI",
    "secondary": "Calibri"
}

COLORS = {
    "white": "#FFFFFF",
    "black": "#000000",
    "blue": "#489FB5",
    "navy": "#16697A",
    "light_blue": "#8BD7D2",
    "red": "red"  # TODO: choose exact color
}

STYLES = {
    "root": {
        "bg": COLORS["white"],
    },
    "frame": {
        "start": {
            "bg": COLORS["white"],
            "padx": 30,
            "pady": 30
        },
        "play": {
            "bg": COLORS["white"],
            "padx": 30,
            "pady": 30
        }
    },
    "label": {
        "h1": {
            "font": (FONTS["primary"], 22),
            "bg": COLORS["white"],
            "fg": COLORS["black"],
            "pady": 10
        },
        "h2": {
            "font": (FONTS["primary"], 18),
            "bg": COLORS["white"],
            "fg": COLORS["black"],
            "pady": 10
        },
        "h3": {
            "font": (FONTS["primary"], 16),
            "bg": COLORS["white"],
            "fg": COLORS["black"],
            "pady": 10
        },
    },
    "button": {
        "default": {
            "font": (FONTS["primary"], 14),
            "padx": 20,
            "bg": COLORS["navy"],
            "fg": COLORS["white"],
            "borderwidth": 0,
        },
        "on_enter": {
            "bg": COLORS["light_blue"],
            "fg": COLORS["black"],
        },
    },
    "dice": {
        "default": {
            "width": 4,
            "height": 1,
            "font": (FONTS["primary"], 24),
            "bg": COLORS["white"],
            "fg": COLORS["navy"],
            "borderwidth": 0.3,
        },
        "on_enter": {
            "bg": COLORS["light_blue"],
            "fg": COLORS["black"],
        },
        "on_click": {
            "bg": COLORS["blue"],
            "fg": COLORS["white"],
        }
    },
    "clock": {
        "default": {
            "font": (FONTS["primary"], 25),
            "bg": COLORS["white"],
            "fg": COLORS["black"],
            "borderwidth": 0.3
        },
        "before_end": {
            "bg": COLORS["red"],
            "fg": COLORS["black"],
        }
    }
}
