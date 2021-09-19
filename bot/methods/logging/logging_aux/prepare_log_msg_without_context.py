#!/usr/bin/env python3

def prepare_log_msg_without_context(txt):
    txt = txt.replace("╔", "")
    txt = txt.replace("╗", "")
    txt = txt.replace("╠", "")
    txt = txt.replace("╣", "")
    txt = txt.replace("╚", "")
    txt = txt.replace("╝", "")
    txt = txt.replace("☆", "")
    txt = txt.replace("★", "")
    txt = txt.replace("✦✧✦✧✦", "")
    txt = txt.replace("─", "")
    txt = f"""Canal {txt[txt.find("#", 1)+1 :]}""" if txt.find("PRIVMSG")> -1 else txt
    txt = txt.strip()
    return txt

