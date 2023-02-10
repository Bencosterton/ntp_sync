import socket
    
#Windows ntp
try:
    win_ntp.gettime_ntp()
except:
    pass

#Unix ntp
#Will do it on it's own, becuase of unix magic

NAME = socket.gethostname()
T_IP = socket.gethostbyname(NAME)

#Welcome message
print("""\

 __          __           _  __          __         _     _                       _             _            _     _   _            _   _                  
 \ \        / /          | | \ \        / /        | |   | |                     | |           | |          | |   | | | |          | | (_)                 
  \ \  /\  / /____      _| |  \ \  /\  / /__  _   _| | __| |  _   _  ___  _   _  | | ___   ___ | | __   __ _| |_  | |_| |__   ___  | |_ _ _ __ ___   ___   
   \ \/  \/ / _ \ \ /\ / / |   \ \/  \/ / _ \| | | | |/ _` | | | | |/ _ \| | | | | |/ _ \ / _ \| |/ /  / _` | __| | __| '_ \ / _ \ | __| | '_ ` _ \ / _ \  
    \  /\  / (_) \ V  V /|_|    \  /\  / (_) | |_| | | (_| | | |_| | (_) | |_| | | | (_) | (_) |   <  | (_| | |_  | |_| | | |  __/ | |_| | | | | | |  __/_ 
     \/  \/ \___/ \_/\_/ (_)     \/  \/ \___/ \__,_|_|\__,_|  \__, |\___/ \__,_| |_|\___/ \___/|_|\_\  \__,_|\__|  \__|_| |_|\___|  \__|_|_| |_| |_|\___(_)
                                                               __/ |                                                                                       
                                                              |___/                                                                                            
""", NAME, T_IP,)

try:
    import win_ntp
except ImportError:
    import unix_ntp
