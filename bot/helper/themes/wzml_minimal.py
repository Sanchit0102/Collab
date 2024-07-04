#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'Silent Bot System'
    ST_BN1_URL = 'https://t.me/Silent_Bots'
    ST_BN2_NAME = 'Auto Bot'
    ST_BN2_URL = 'https://t.me/silentautobot'
    ST_MSG = '''<b>✨ Silent Team ➔ Mirror & Leech Bot</b>\n\nI Can Upload Files, Links, Torrents, etc. to Telegram, Google Drive, DDL Servers and Rclone Supported Sites!\n\n
<b>Type {help_command} to get a list of available commands</b>'''
    ST_BOTPM = '''<b>🕵️ Bot PM Initiated Successfully!\n\n I will send all your files and links here.</b>'''
    ST_UNAUTH = '''<b>⚠️ Access Denied!</b>'''
    OWN_TOKEN_GENERATE = '''<b>❌ Temporary Token is not Yours!</b>\n\n<i>Kindly Generate Your Own.</i>'''
    USED_TOKEN = '''<b>‼️ Temporary Token Already Used!</b>\n\n<i>Kindly Generate a New One.</i>'''
    LOGGED_PASSWORD = '''<b>✅ Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = '✅ Activate Temporary Token'
    TOKEN_MSG = '''<b><u>❕ Generated Temporary Login Token!</u></b>
<b>♻️ Temp Token:</b> <code>{token}</code>
<b>⏰ Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activated'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>✅️ Already Bot Login In!</b>'
    INVALID_PASS = '<b>❌ Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>✅️ Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>💫 Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = '📕 Basic'
    USER_BT = ' 👮🏻‍♀️ Users'
    MICS_BT = '🔧 Mics'
    O_S_BT = '⚙️ Owner & Sudos'
    CLOSE_BT = '🔐 Close'
    HELP_HEADER = "㊂ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor details.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''<b>🤖 <u>𝘽𝙤𝙩 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨</u></b>

<b>⏰ Bot Uptime :</b> {bot_uptime}

╭ ▸<b>💽 RAM</b>
┃ {ram_bar} » ({ram}%)
╰ ▸<b>U :</b> {ram_u} ┃ <b>F :</b> {ram_f} ┃ <b>T :</b> {ram_t}

╭ ▸<b>👒 SWAP</b>
┃ {swap_bar} » ({swap}%)
╰ ▸<b>U :</b> {swap_u} ┃ <b>F :</b> {swap_f} ┃ <b>T :</b> {swap_t}

╭ ▸<b>📦 DISK</b>
┃ {disk_bar} » ({disk}%)
┠ ▸<b>Total Disk Read :</b> {disk_read}
┠ ▸<b>Total Disk Write :</b> {disk_write}
╰ ▸<b>U :</b> {disk_u} ┃ <b>F :</b> {disk_f} ┃ <b>T :</b> {disk_t}

<a href="https://t.me/THE_SILENT_TEAMS"><b>♥️ ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 𝕊𝕚𝕝𝕖𝕟𝕥 𝕋𝕖𝕒𝕞</b></a>
    
    '''
    SYS_STATS = '''<b>🛠 <u>𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨</u></b>

╭ ▸<b>⏰ OS Uptime :</b> {os_uptime}
┠ ▸<b>☢️ OS Info :</b> {os_version}
╰ ▸<b>🔧 OS Arch :</b> {os_arch}

╭ ▸<b>📶 Network Stats</b>
┠ ▸<b>Upload Data:</b> {up_data}
┠ ▸<b>Download Data:</b> {dl_data}
┠ ▸<b>Pkts Sent:</b> {pkt_sent}k
┠ ▸<b>Pkts Received:</b> {pkt_recv}k
╰ ▸<b>Total I/O Data:</b> {tl_data}

╭ ▸<b>🖥️ CPU</b>
┠ ▸{cpu_bar} » ({cpu}%)
┠ ▸<b>Frequency :</b> {cpu_freq}
┠ ▸<b>Average Load :</b> {sys_load}
┠ ▸<b>P-Cores :</b> {p_core} ┃ <b>V-Cores :</b> {v_core}
┠ ▸<b>Total Cores :</b> {total_core}
╰ ▸<b>Usable CPUs :</b> {cpu_use}

<a href="https://t.me/THE_SILENT_TEAMS"><b>♥️ ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 𝕊𝕚𝕝𝕖𝕟𝕥 𝕋𝕖𝕒𝕞</b></a>
    '''
    REPO_STATS = '''<b>🧑‍💻 <u>𝙍𝙚𝙥𝙤 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨</u></b>

╭ ▸<b>♻️ Bot Updated :</b> {last_commit}
┠ ▸<b>🆔 Current Version :</b> {bot_version}
┠ ▸<b>🎈 Latest Version :</b> {lat_version}
╰ ▸<b>📝 ChangeLog :</b> {commit_details}

<b>💥 REMARKS :</b> <code>{remarks}</code>

<a href="https://t.me/THE_SILENT_TEAMS"><b>♥️ ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 𝕊𝕚𝕝𝕖𝕟𝕥 𝕋𝕖𝕒𝕞</b></a>
    '''
    BOT_LIMITS = '''<b>❗<u>𝘽𝙤𝙩 𝙇𝙞𝙢𝙞𝙩𝙨</u></b>

╭ ▸<b>🎯 Direct :</b> {DL} GB
┠ ▸<b>🧲 Torrent :</b> {TL} GB
┠ ▸<b>☁️ GDrive :</b> {GL} GB
┠ ▸<b>📺 YT-DLP :</b> {YL} GB
┠ ▸<b>🎥 Playlist :</b> {PL} Videos
┠ ▸<b>Ⓜ️ Mega :</b> {ML} GB
┠ ▸<b>🎗️ Clone :</b> {CL} GB
╰ ▸<b>📂 Leech :</b> {LL} GB

╭ ▸<b>🔑 Token Validity :</b> {TV}
┠ ▸<b>🐢 Timeout :</b> {UTI}
┠ ▸<b>👤 User Tasks :</b> {UT}
╰ ▸<b>🚧 Total Tasks :</b> {BT}

<a href="https://t.me/THE_SILENT_TEAMS"><b>♥️ ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 𝕊𝕚𝕝𝕖𝕟𝕥 𝕋𝕖𝕒𝕞</b></a>
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<b>🔄 Restarting...</b>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<b>♻️ Mai Jinda Huu 🎉</b>'''
    
    RESTARTED = '''<b>🔄 Bot Restarted!</b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<b>🙄 Starting Ping...</b>'
    PING_VALUE = '<b>🏓 Pong:</b> <code>{value}ms</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b>🤧 Task Started</b>

╭ ▸<b>💠 Mode:</b> {Mode}
╰ ▸<b>👤 User:</b> {Tag}\n\n"""
    LINKS_SOURCE = """╭ ▸<b>💡 Source:</b>
╰ ▸<b>⏰ Time:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "🤧 <b><u>Leech Started</u> :</b>\n\n<b>💡 Source :</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "🤧 <b><u>Leech Started</u> :</b>\n\n╭ ▸<b>👤 User :</b> {mention}┃ <b>🆔 ID :</b> <code>{uid}</code>\n╰ ▸<b>💡 Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '╭ ▸<b>🏷️ Name:</b> {Name}\n'
    SIZE =                  '┠ ▸<b>💾 Size: </b>{Size}\n'
    ELAPSE =                '┠ ▸<b>⌛ Elapsed: </b>{Time}\n'
    MODE =                  '┠ ▸<b>💠 Mode: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '┠ ▸<b>📂 Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '┠ ▸<b>💀 Corrupted Files: </b>{Corrupt}\n'
    L_CC =                  '╰ ▸<b>👤 User: </b>{Tag}\n\n'
    PM_BOT_MSG =            '<b><i>Files have been Sent Above!</i></b>\n'
    L_BOT_MSG =             '<b><i>Files have been Sent in Bot PM!</i></b>\n'
    L_LL_MSG =              '<b><i>Files have been Sent. Access via Links!</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '┠ ▸<b>📜 Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '┠ ▸<b>🗂️ SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '┠ ▸<b>📂 Files: </b>{Files}\n'
    RCPATH =                '┠ ▸<b>🚩 Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '╰ ▸<b>👤 User: </b>{Tag}\n\n'
    M_BOT_MSG =             '🏁 <b><i>Links have been Sent in DM!</i></b>\n'

    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📩 Save'
    RCLONE_LINK =     '®️ RClone Link'
    DDL_LINK =        '🚀 {Serv} Link'
    SOURCE_URL =      '💡 Source'
    INDEX_LINK_F =    '🚀 Index Link'
    INDEX_LINK_D =    '🚀 Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '🕵️ View in Bot PM'
    CHECK_LL =        '📦 View in Dump'
    MEDIAINFO_LINK =  '📜 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '╭ ▸<b>🏷️ Name: <i>{Name}</i></b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n┃ {Bar}'
    PROCESSED =         '\n┠ ▸<b>🔄 Process:</b> {Processed}'
    STATUS =            '\n┠ ▸<b>✨ Status:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' ┃ <b>ETA:</b> {Eta}'
    SPEED =             '\n┠ ▸<b>📶 Speed:</b> {Speed}'
    ELAPSED =                                     ' ┃ <b>Elapsed:</b> {Elapsed}'
    ENGINE =            '\n┠ ▸<b>⚙️ Engine:</b> {Engine}'
    STA_MODE =          '\n┠ ▸<b>💠 Mode:</b> {Mode}'
    SEEDERS =           '\n┠ ▸<b>🌱:</b> {Seeders} ┃ '
    LEECHERS =                                           '<b>🪢:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n┠ ▸<b>💾 Size:</b> {Size}'
    SEED_SPEED =     '\n┠ ▸<b>📶 Speed:</b> {Speed} ┃ '
    UPLOADED =                                     '<b>Uploaded:</b> {Upload}'
    RATIO =          '\n┠ ▸<b>🌀 Ratio:</b> {Ratio} ┃ '
    TIME =                                         '<b>Time:</b> {Time}'
    SEED_ENGINE =    '\n┠ ▸<b>⚙️ Engine:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n┠ ▸<b>💾 Size:</b> {Size}'
    NON_ENGINE =     '\n┠ ▸<b>⚙️ Engine:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n┠ ▸<b>👤 User:</b> {User}'
    ID =                                                        '┃<b>🆔 ID:</b> <code>{Id}</code>'
    BTSEL =          '\n┠ ▸<b>✂️ Select:</b> {Btsel}'
    CANCEL =         '\n╰ ▸<b>🚫 Stop:</b> {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '⚙️ <b><u>Bot Stats</u></b>\n'
    TASKS =  '╭ ▸<b>🚧 Tasks: <i>{Tasks}<i></b>\n'
    BOT_TASKS = '╭ ▸<b>🚧 Tasks: <i>{Tasks}/{Ttask} </i>┃ 👷 Available: <i>{Free}</i></b>\n'
    Cpu = '╭ ▸<b>🖥️ CPU: <i>{cpu}% </i> ┃ </b>'
    FREE =                      '<b>📭 Free: <i>{free}</i></b>'
    Ram = '\n┠ ▸<b>💿 RAM: <i>{ram}% </i> ┃ </b>'
    uptime =                     '<b>⏰ Uptime: <i>{uptime}</i></b>'
    DL = '\n╰ ▸<b>🔻 DL: <i>{DL}/s </i>┃ </b>'
    UL =                        '<b>🔺 UL: <i>{UL}/s </i></b>'

    ###--------BUTTONS-------
    PREVIOUS = '⏪'
    REFRESH = '📑 Page: {Page}'
    NEXT = '⏭️'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = '<b>🏷️ Name:</b> <code>{content}</code>\n<b>⚠️ This File/Folder is already available in Drive!</b>\n\n<b>📑 List Results:</b>'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>🎲 Counting:</b> <code>{LINK}</code>\n\n<b>⏳ Please Wait...</b>'
    COUNT_NAME = '╭ ▸<b>🏷️ Name:</b> <code>{COUNT_NAME}</code>\n'
    COUNT_SIZE = '┠ ▸<b>💾 Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┠ ▸<b>📜 Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┠ ▸<b>🗂️ SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '┠ ▸<b>📂 Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '╰ ▸<b>👤 User: </b>{COUNT_CC}\n\n<a href="https://t.me/THE_SILENT_TEAMS"><b>♥️ ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 𝕊𝕚𝕝𝕖𝕟𝕥 𝕋𝕖𝕒𝕞</b></a>'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>🔍 Searching:</b> <code>{NAME}</code>'
    LIST_FOUND = '<b>ℹ️ Found {NO} Results For</b> <code>{NAME}</code>'
    LIST_NOT_FOUND = '<b>☹️ No Results Found For</b> <code>{NAME}</code>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<b>💩 No Active Tasks!</b>

<a href="https://t.me/THE_SILENT_TEAMS"><b>♥️ ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 𝕊𝕚𝕝𝕖𝕟𝕥 𝕋𝕖𝕒𝕞</b></a>

⌬ <b><u>Bot Stats</u></b>
╭ ▸<b>🖥️ CPU: <i>{cpu}% </i>┃ 💿 RAM: <i>{ram}% </i></b>
╰ ▸<b>📭 Free: <i>{free}</i> ┃ ⏰ Uptime: <i>{uptime}</i></b> 
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''👩🏻‍🚀 <b><u>User Settings</u></b>
        
╭ ▸<b>👤 Name :</b> {NAME}
┠ ▸<b>🔖 Username :</b> {USERNAME}
┠ ▸<b>🆔 ID :</b> <code>{ID}</code>
┠ ▸<b>🔮 DC :{DC}</b>
╰ ▸<b>🗣️ Language :</b> {LANG}

➲ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg\n\n<a href="https://t.me/THE_SILENT_TEAMS"><b>♥️ ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 𝕊𝕚𝕝𝕖𝕟𝕥 𝕋𝕖𝕒𝕞</b></a>'''

    UNIVERSAL = '''㊂ <b><u>Universal</u></b>

╭ ▸<b>📺 YT-DLP Options :</b> <code>{YT}</code>
┠ ▸<b>🚧 Daily Tasks :</b> {DT} per day
┠ ▸<b>🟢 Last Used :</b> {LAST_USED}
┠ ▸<b>👮🏻 User Session :</b> <i>{USESS}</i>
┠ ▸<b>📜 Media Info :</b> <i>{MEDIAINFO}</i>
┠ ▸<b>🕵️ Bot PM :</b> <i>{BOT_PM}</i>
╰ ▸<b>📩 Save Mode :</b> <i>{SAVE_MODE}</i>

<a href="https://t.me/THE_SILENT_TEAMS"><b>♥️ ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 𝕊𝕚𝕝𝕖𝕟𝕥 𝕋𝕖𝕒𝕞</b></a>'''

    MIRROR = '''㊂ <b><u>Mirror/Clone : {NAME}</u></b>

╭ ▸<b>☁️ Daily Mirror :</b> {DM} per day</i>
┠ ▸<b>Ⓟ Prefix :</b> <code>{MPREFIX}</code>
┠ ▸<b>Ⓢ Suffix :</b> <code>{MSUFFIX}</code>
┠ ▸<b>🌈 Remname :</b> <code>{MREMNAME}</code>
┠ ▸<b>🧿 DDL Server(s) :</b> <i>{DDL_SERVER}</i>
┠ ▸<b>🎀 RClone :</b> <i>{RCLONE}</i>
┠ ▸<b>📮 User TD :</b> <i>{TMODE}</i>
╰ ▸<b>📝 TD Info:</b> <i>{USERTD}</i>

<a href="https://t.me/THE_SILENT_TEAMS"><b>ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 𝕊𝕚𝕝𝕖𝕟𝕥 𝕋𝕖𝕒𝕞</b></a>'''

    LEECH = '''💫 <b><u>Leech Settings - {NAME}</u></b>

╭ ▸<b>📂 Daily Leech : </b>{DL} per day
┠ ▸<b>⚙️ Leech Type :</b> <i>{LTYPE}</i>
┠ ▸<b>🖼️ Thumbnail :</b> <i>{THUMB}</i>
┠ ▸<b>♈ Split Size :</b> <code>{SPLIT_SIZE}</code>
┠ ▸<b>♐ Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
┠ ▸<b>♒ Media Group :</b> <i>{MEDIA_GROUP}</i>
┠ ▸<b>📄 Caption :</b> <code>{LCAPTION}</code>
┠ ▸<b>Ⓟ Prefix :</b> <code>{LPREFIX}</code>
┠ ▸<b>Ⓢ Suffix :</b> <code>{LSUFFIX}</code>
┠ ▸<b>📦 Dump :</b> <code>{LDUMP}</code>
╰ ▸<b>🌈 Remname :</b> <code>{LREMNAME}</code>

<a href="https://t.me/THE_SILENT_TEAMS"><b>♥️ ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 𝕊𝕚𝕝𝕖𝕟𝕥 𝕋𝕖𝕒𝕞</b></a>'''
