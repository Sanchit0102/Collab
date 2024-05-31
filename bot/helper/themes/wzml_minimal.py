#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '😎Oᴡɴᴇʀ'
    ST_BN1_URL = 'https://t.me/White_XYZ_7'
    ST_BN2_NAME = '💥 Uᴘᴅᴀᴛᴇs'
    ST_BN2_URL = 'https://t.me/RS_Movie'
    ST_MSG = '''<b>ℹ️ I Cᴀɴ Uᴘʟᴏᴀᴅ Fɪʟᴇs, Lɪɴᴋs, Tᴏʀʀᴇɴᴛs, ᴇᴛᴄ. ᴛᴏ Tᴇʟᴇɢʀᴀᴍ, Gᴏᴏɢʟᴇ Dʀɪᴠᴇ, DDL Sᴇʀᴠᴇʀs ᴀɴᴅ Rᴄʟᴏɴᴇ Sᴜᴘᴘᴏʀᴛᴇᴅ Sɪᴛᴇs.</b>
<b>Type {help_command} to get a list of available commands</b>'''
    ST_BOTPM = '''<b>Nᴏᴡ, Tʜɪs ʙᴏᴛ ᴡɪʟʟ sᴇɴᴅ ᴀʟʟ ʏᴏᴜʀ ғɪʟᴇs ᴀɴᴅ ʟɪɴᴋs ʜᴇʀᴇ. Sᴛᴀʀᴛ Usɪɴɢ...</b>'''
    ST_UNAUTH = '''<b>Yᴏᴜ Aʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀ!</b>'''
    OWN_TOKEN_GENERATE = '''<b>Tᴇᴍᴘᴏʀᴀʀʏ Tᴏᴋᴇɴ ɪs ɴᴏᴛ ʏᴏᴜʀs!</b>\n\n<i>Kɪɴᴅʟʏ ɢᴇɴᴇʀᴀᴛᴇ ʏᴏᴜʀ ᴏᴡɴ.</i>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = 'Aᴄᴛɪᴠᴀᴛᴇᴅ🚀'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Lᴏɢ Dɪsᴘʟᴀʏ'
    WEB_PASTE_BT = '📨 Wᴇʙ Pᴀsᴛᴇ (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Bᴀsɪᴄ'
    USER_BT = 'Usᴇʀs'
    MICS_BT = 'Mɪᴄs'
    O_S_BT = 'Oᴡɴᴇʀ & Sᴜᴅᴏs'
    CLOSE_BT = 'Cʟᴏsᴇ 🔐'
    HELP_HEADER = "㊂ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''<b>🤖 𝘽𝙤𝙩 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨 
⏰ 𝗕𝗼𝘁 𝗨𝗽𝘁𝗶𝗺𝗲 : {bot_uptime} 
┎💽 𝗥𝗔𝗠 
┠{ram_bar} » ({ram}%) 
┖U : {ram_u} | F : {ram_f} | T : {ram_t} 
┎👒 𝗦𝗪𝗔𝗣 
┠{swap_bar} » ({swap}%) 
┖U : {swap_u} | F : {swap_f} | T : {swap_t} 
┎📦 𝗗𝗜𝗦𝗞 
┠{disk_bar} » ({disk}%) 
┠𝗧𝗼𝘁𝗮𝗹 𝗗𝗶𝘀𝗸 𝗥𝗲𝗮𝗱 : {disk_read} 
┠𝗧𝗼𝘁𝗮𝗹 𝗗𝗶𝘀𝗸 𝗪𝗿𝗶𝘁𝗲 : {disk_write} 
┗U : {disk_u} | F : {disk_f} | T : {disk_t}</b>
     '''
    SYS_STATS = '''🛠 <b>𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨 
    ┏⏰ 𝗢𝗦 𝗨𝗽𝘁𝗶𝗺𝗲 : {os_uptime} 
    ┠☢️ 𝗢𝗦 𝗜𝗻𝗳𝗼 : {os_version} 
    ┗🔧 𝗢𝗦 𝗔𝗿𝗰𝗵 : {os_arch} 
    ┏🖥️ 𝗖𝗣𝗨 
    ┠{cpu_bar} » ({cpu}%) 
    ┠𝗙𝗿𝗲𝗾𝘂𝗲𝗻𝗰𝘆 : {cpu_freq} 
    ┠𝗔𝘃𝗲𝗿𝗮𝗴𝗲 𝗟𝗼𝗮𝗱 : {sys_load} 
    ┠𝗣-𝗖𝗼𝗿𝗲𝘀 : {p_core} 
    | 𝗩-𝗖𝗼𝗿𝗲𝘀 : {v_core} 
    ┠𝗧𝗼𝘁𝗮𝗹 𝗖𝗼𝗿𝗲𝘀 : {total_core} 
    ┗𝗨𝘀𝗮𝗯𝗹𝗲 𝗖𝗣𝗨𝘀 : {cpu_use} 
    ┏📶 𝗡𝗲𝘁𝘄𝗼𝗿𝗸 𝗦𝘁𝗮𝘁𝘀 
    ┠🔻𝗨𝗽𝗹𝗼𝗮𝗱 𝗗𝗮𝘁𝗮: {up_data} 
    ┠🔺𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗗𝗮𝘁𝗮: {dl_data} 
    ┠𝗣𝗸𝘁𝘀 𝗦𝗲𝗻𝘁: {pkt_sent}k 
    ┠𝗣𝗸𝘁𝘀 𝗥𝗲𝗰𝗲𝗶𝘃𝗲𝗱: {pkt_recv}k 
    ┗𝗧𝗼𝘁𝗮𝗹 𝗜/𝗢 𝗗𝗮𝘁𝗮: {tl_data}</b> 
    '''
    REPO_STATS = '''🧑‍💻 𝙍𝙚𝙥𝙤 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨 
    ┏♻️ 𝗕𝗼𝘁 𝗨𝗽𝗱𝗮𝘁𝗲𝗱 : {last_commit} 
    ┠🆔 𝗖𝘂𝗿𝗿𝗲𝗻𝘁 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 : {bot_version} 
    ┠🎈 𝗟𝗮𝘁𝗲𝘀𝘁 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 : {lat_version} 
    ┗📝 𝗖𝗵𝗮𝗻𝗴𝗲𝗹𝗼𝗴 : {commit_details} 💥 REMARKS : {remarks '''
    
    BOT_LIMITS = '''<b>❗𝘽𝙤𝙩 𝙇𝙞𝙢𝙞𝙩𝙨 :</b>
<b>┏🎯 𝗗𝗶𝗿𝗲𝗰𝘁 : {DL} GB 
┠🧲 𝗧𝗼𝗿𝗿𝗲𝗻𝘁 : {TL} GB 
┠☁️ 𝗚𝗗𝗿𝗶𝘃𝗲 : {GL} GB 
┠📺 𝗬𝗧-𝗗𝗟𝗣 : {YL} GB 
┠🎥 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁 : {PL} Videos 
┠Ⓜ️ 𝗠𝗲𝗴𝗮  : {ML} GB 
┠🎗️ 𝗖𝗹𝗼𝗻𝗲 : {CL} GB 
┗📂 𝗟𝗲𝗲𝗰𝗵 : {LL} GB 
┏🔑 𝗧𝗼𝗸𝗲𝗻 𝗩𝗮𝗹𝗶𝗱𝗶𝘁𝘆 : {TV} 
┠🐢 𝗧𝗶𝗺𝗲𝗼𝘂𝘁 : {UTI} 
┠👤 𝗨𝘀𝗲𝗿 𝗧𝗮𝘀𝗸𝘀 : {UT} 
┗🚧 𝗧𝗼𝘁𝗮𝗹 𝗧𝗮𝘀𝗸𝘀 : {BT}</b>
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Rᴇsᴛᴀʀᴛɪɴɢ...♡</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = ''' <b>♻️ Rᴇsᴛᴀʀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ!</b>
❀ <b>📅 𝗗𝗮𝘁𝗲:</b> {date}
❀ <b>⏰ 𝗧𝗶𝗺𝗲:</b> {time}
❀ <b>🌍 𝗧𝗶𝗺𝗲𝗭𝗼𝗻𝗲:</b> {timz}
❀ <b>🆔 𝗩𝗲𝗿𝘀𝗶𝗼𝗻:</b> {version}'''
    RESTARTED = '''√ <b><i> Boт Is Rᴇsтᴀʀтᴇᴅ!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<code>🙄 Sᴛᴀʀᴛɪɴɢ Pɪɴɢ...</code>'
    PING_VALUE = '<b>🏓 Pᴏɴɢ</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b>🚧 Tᴀsᴋ Sᴛᴀʀᴛᴇᴅ</b>
┏💠 Mᴏᴅᴇ: {Mode}
┗👤 User: {Tag}\n\n"""
    LINKS_SOURCE = """💡 <b> Sᴏᴜʀᴄᴇ:</b>
❀ <b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "❀ <b><u>Task Started :</u></b>\n❈\n❈ <b>Link:</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "❀ <b><u>Leech Started :</u></b>\n❈\n❈ <b>User :</b> {mention} ( #ID{uid} )\n❈ <b>Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><i>{Name}</i></b>\n\n'
    SIZE =                  '❀ <b>Size: </b>{Size}\n'
    ELAPSE =                '❀ <b>Elapsed: </b>{Time}\n'
    MODE =                  '❀ <b>Mode: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '❀ <b>Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '❀ <b>Corrupted Files: </b>{Corrupt}\n'
    L_CC =                  '❀ <b>By: </b>{Tag}\n\n'
    PM_BOT_MSG =            '❀ <b><i>File(s) have been Sent above</i></b>'
    L_BOT_MSG =             '❀ <b><i>File(s) have been Sent to Bot PM (Private)</i></b>'
    L_LL_MSG =              '❀ <b><i>File(s) have been Sent. Access via Links...</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '❀ <b>Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '❀ <b>SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '❀ <b>Files: </b>{Files}\n'
    RCPATH =                '❀ <b>Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '❀ <b>By: </b>{Tag}\n\n'
    M_BOT_MSG =             '❀ <b><i>Link(s) have been Sent to Bot PM (Private)</i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '⎙ Fɪʟᴇ Iɴ Bᴏᴛ Pᴍ ⎙'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b><i>{Name}</i></b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n❀ {Bar}'
    PROCESSED =         '\n❀ <b>Processed:</b> {Processed}'
    STATUS =            '\n❀ <b>Status:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' ❀ <b>ETA:</b> {Eta}'
    SPEED =             '\n❀ <b>Speed:</b> {Speed}'
    ELAPSED =                                     ' ❀ <b>Elapsed:</b> {Elapsed}'
    ENGINE =            '\n❀ <b>Engine:</b> {Engine}'
    STA_MODE =          '\n❀ <b>Mode:</b> {Mode}'
    SEEDERS =           '\n❀ <b>Seeders:</b> {Seeders} ❀ '
    LEECHERS =                                           '<b>Leechers:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n❀ <b>Size: </b>{Size} ❀'
    SEED_SPEED =     '\n❀ <b>Speed: </b> {Speed} ❀ '
    UPLOADED =                                     '<b>Uploaded: </b> {Upload}'
    RATIO =          '\n❀ <b>Ratio: </b> {Ratio} ❀ '
    TIME =                                         '<b>Time: </b> {Time}'
    SEED_ENGINE =    '\n❀ <b>Engine:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n❀ <b>Size: </b>{Size}'
    NON_ENGINE =     '\n❀ <b>Engine:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n❀ <b>User:</b> <code>{User}</code> ❀ '
    ID =                                                        '<b>ID:</b> <code>{Id}</code>'
    BTSEL =          '\n❀ <b>Select:</b> {Btsel}'
    CANCEL =         '\n❀ {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '❀ <b><i>Bot Stats</i></b>\n'
    TASKS =  '❀ <b>Tasks:</b> {Tasks}\n'
    BOT_TASKS = '❀ <b>Tasks:</b> {Tasks}/{Ttask} ❀ <b>AVL:</b> {Free}\n'
    Cpu = '❀ <b>CPU:</b> {cpu}% ❀ '
    FREE =                      '<b>F:</b> {free} [{free_p}%]'
    Ram = '\n❀ <b>RAM:</b> {ram}% ❀ '
    uptime =                     '<b>UPTIME:</b> {uptime}'
    DL = '\n❈ <b>DL:</b> {DL}/s ❀ '
    UL =                        '<b>UL:</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '⫷◉'
    REFRESH = '𒊹︎︎︎❖ Rᴀsʜᴍɪᴋᴀ Lᴇᴇᴄʜ ❖𒊹︎︎︎ ™\n{Page}'
    NEXT = '◉⫸'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n❈\n'
    COUNT_SIZE = '❀ <b>Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '❀ <b>Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '❀ <b>SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '❀ <b>Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '❀ <b>By: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>No Active Downloads!</i>
    
❀ <b><i>Bot Stats</i></b>
❀ <b>CPU:</b> {cpu}% ❀ <b>F:</b> {free} [{free_p}%]
❀ <b>RAM:</b> {ram} ❀ <b>UPTIME:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>User Settings :</u></b>
        
❀<b> Name :</b> {NAME} ( <code>{ID}</code> )
❀<b> Username :</b> {USERNAME}
❀<b> Telegram DC :</b> {DC}
❀<b> Language :</b> {LANG}

❀ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg'''

    UNIVERSAL = '''㊂ <b><u>Universal Settings : {NAME}</u></b>

❀<b> YT-DLP Options :</b> <b><code>{YT}</code></b>
❀<b> Daily Tasks :</b> <code>{DT}</code> per day
❀<b> Last Bot Used :</b> <code>{LAST_USED}</code>
❀<b> User Session :</b> <code>{USESS}</code>
❀<b> MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
❀<b> Save Mode :</b> <code>{SAVE_MODE}</code>
❀<b> User Bot PM :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''㊂ <b><u>Mirror/Clone Settings : {NAME}</u></b>

❀<b> RClone Config :</b> <i>{RCLONE}</i>
❀<b> Mirror Prefix :</b> <code>{MPREFIX}</code>
❀<b> Mirror Suffix :</b> <code>{MSUFFIX}</code>
❀<b> Mirror Remname :</b> <code>{MREMNAME}</code>
❀<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
❀<b> User TD Mode :</b> <i>{TMODE}</i>
❀<b> Total User TD(s) :</b> <i>{USERTD}</i>
❀<b> Daily Mirror :</b> <code>{DM}</code> per day'''

    LEECH = '''㊂ <b><u>Leech Settings for {NAME}</u></b>

❀<b> Daily Leech : </b><code>{DL}</code> per day
❀<b> Leech Type :</b> <i>{LTYPE}</i>
❀<b> Custom Thumbnail :</b> <i>{THUMB}</i>
❀<b> Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
❀<b> Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
❀<b> Media Group :</b> <i>{MEDIA_GROUP}</i>
❀<b> Leech Caption :</b> <code>{LCAPTION}</code>
❀<b> Leech Prefix :</b> <code>{LPREFIX}</code>
❀<b> Leech Suffix :</b> <code>{LSUFFIX}</code>
❀<b> Leech Dumps :</b> <code>{LDUMP}</code>
❀<b> Leech Remname :</b> <code>{LREMNAME}</code>'''
