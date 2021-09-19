import pyautogui,sys,threading,time,win32api,win32con,mss,mss.tools,win32gui,os,operator,random,winsound,psutil,string
import numpy as np
from cv2 import matchTemplate, minMaxLoc, cvtColor, COLOR_RGB2BGR, TM_CCOEFF_NORMED, imread
from dearpygui.core import *
from dearpygui.simple import *
import Aurora_login

##########################################################
#
#   Login section
#
##########################################################

username_entry,password_entry,login_status = (Aurora_login.login())
License_days = (Aurora_login.login_verify_raw(username_entry,password_entry))[1]

if login_status != 1:   #extra layer of defense
    exit(1)

##########################################################
#
#   Variable initializing
#
##########################################################

#bobber image recognition initializing
screen_area_bobber_image_recognition = [(472, 31, 1024, 484), (1, 31, 552, 484), (1, 344, 552, 798), (472, 344, 1024, 798)] #releated with base_offset

#screen_area = x1,y1,x2,y2
#Coords for fishing spots
coords = []

#Current Bot State
STATE = "IDLE"

#Thread Stopper
stop_button = False

#Stuff for mouse events
state_left = win32api.GetKeyState(0x01)
state_right = win32api.GetKeyState(0x02)

#fish counters
fish_count = 0
total_time = 0
total_time_start = 0
bait_counter = 1
food_timer = 0
potion_round = 0
bait_flag = 0
potion_flag = 0
potion_round_refill = 0
effeciency = 0
TIME = 0
total = 0
valid = "FALSE"

stuck_allert = 0
long_cast = False

window_title_string = ( ''.join(random.choice(string.ascii_letters) for i in range(20)) ) #window name

##########################################################
#
#   These Functions handle bot state / minigame handling
#
##########################################################

#bobber on the water image recognition
def bobber_load():
    global bobber
    bobber = []
    bobber_temp_array = []

    #--------------QUARTER 1--------------#

    bobber_temp = imread(resource_path('bobber_1_a.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_1_b.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_1_c.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_1_d.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_1_e.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_1_f.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_1_g.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber.append(bobber_temp_array)
    bobber_temp_array = []

    # --------------QUARTER 2--------------#

    bobber_temp = imread(resource_path('bobber_2_a.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_2_b.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_2_c.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_2_d.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_2_e.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_2_f.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_2_g.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_2_h.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber.append(bobber_temp_array)
    bobber_temp_array = []

    # --------------QUARTER 3--------------#

    bobber_temp = imread(resource_path('bobber_3_a.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_3_b.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_3_c.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_3_d.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_3_e.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber.append(bobber_temp_array)
    bobber_temp_array = []

    # --------------QUARTER 4--------------#

    bobber_temp = imread(resource_path('bobber_4_a.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_4_b.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_4_c.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_4_d.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_4_e.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber.append(bobber_temp_array)
def bobber_load_low_quality():
    global bobber
    bobber = []
    bobber_temp_array = []

    # --------------QUARTER 1--------------#

    bobber_temp = imread(resource_path('bobber_1_a_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_1_b_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_1_c_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_1_d_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_1_e_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_1_f_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber.append(bobber_temp_array)
    bobber_temp_array = []

    # --------------QUARTER 2--------------#

    bobber_temp = imread(resource_path('bobber_2_a_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_2_b_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_2_c_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_2_d_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_2_e_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_2_f_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_2_g_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber.append(bobber_temp_array)
    bobber_temp_array = []

    # --------------QUARTER 3--------------#

    bobber_temp = imread(resource_path('bobber_3_a_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_3_b_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_3_c_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_3_d_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_3_e_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_3_f_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_3_g_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_3_h_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_3_i_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber.append(bobber_temp_array)
    bobber_temp_array = []

    # --------------QUARTER 4--------------#

    bobber_temp = imread(resource_path('bobber_4_a_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_4_b_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_4_c_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_4_d_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_4_e_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_4_f_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_4_g_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber_temp = imread(resource_path('bobber_4_h_lq.png'))
    bobber_temp = np.flip(bobber_temp[:, :, :3], 2)  # 1
    bobber_temp_array.append(bobber_temp)

    bobber.append(bobber_temp_array)

def quarter_recognition(mouse_pos):
    if mouse_pos[0] <= 512: #left side
        if mouse_pos[1] <= 384: #up side
            quarter = 1
        else:
            quarter = 2
    else: #right side
        if mouse_pos[1] <= 384: #upside
            quarter = 0
        else:
            quarter = 3
    return(quarter)
def bobber_scan():
    global quarter

    base_offset = [(472,31),(1,31),(1,344),(472,344)]   #releated with screen_area_bobber_image_recognition

    bobber_loc_array = []

    quarter = quarter_recognition(mouse_pos)

    #quarter of area loading
    base = np.array(mss.mss().grab(screen_area_bobber_image_recognition[quarter]))
    base = np.flip(base[:, :, :3], 2)  # 1

    #scanning for bobber for certain variant
    for variant in range(len(bobber[quarter])):
        result = matchTemplate(base, bobber[quarter][variant], TM_CCOEFF_NORMED)

        loc = np.where(result >= 0.7)
        for pt in zip(*loc[::-1]):
            bobber_loc_array.append(pt)

    for i in range(len(bobber_loc_array)):
        bobber_loc_array[i] = tuple(map(operator.add, bobber_loc_array[i], base_offset[quarter]))


    return(bobber_loc_array)
def bobber_scan_legacy(screen_area_bobber_image_recognition,quarter,variant):

    base = np.array(mss.mss().grab(screen_area_bobber_image_recognition))
    base = np.flip(base[:, :, :3], 2)
    result = matchTemplate(base, bobber[quarter][variant], TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = minMaxLoc(result)
    return(max_loc[1],max_val)
def bobber_image_recognition():
    global bobber_loc_array_initial

    bobber_loc_array = bobber_scan()

    offset_x = 24
    offset_y = 35

    # finding positions of new object
    if len(bobber_loc_array) > len(bobber_loc_array_initial):  # New bobber found
        for bobber_loc_initial in bobber_loc_array_initial:
            for bobber_loc in bobber_loc_array:
                if (bobber_loc_initial[0] + offset_x) > bobber_loc[0] > (bobber_loc_initial[0] - offset_x) and (
                        bobber_loc_initial[1] + offset_y) > bobber_loc[1] > (bobber_loc_initial[1] - offset_y):
                    bobber_loc_array.remove(bobber_loc)

    else:
        print("Couldn't detect bobber")
        return(1)

    # cheking if it find only 1 new object
    for bobber_loc in bobber_loc_array:
        for bobber_loc_parsing in bobber_loc_array:
            if (bobber_loc_parsing[0] + offset_x) > bobber_loc[0] > (bobber_loc_parsing[0] - offset_x) and (
                    bobber_loc_parsing[1] + offset_y) > bobber_loc[1] > (bobber_loc_parsing[1] - offset_y):
                pass
            else:
                print("Detected more then 1 new object")
                return(2)

    # choosing screen area of new bobber
    screen_area_bobber_image_recognition = (
    int(bobber_loc_array[0][0]), int(bobber_loc_array[0][1] - 14), int(bobber_loc_array[0][0] + offset_x),
    int(bobber_loc_array[0][1] + offset_y))

    # finding best bobber variant for certain object
    max_val_old = 0
    for variants in range(len(bobber[quarter])):
        base = np.array(mss.mss().grab(screen_area_bobber_image_recognition))
        base = np.flip(base[:, :, :3], 2)

        result = matchTemplate(base, bobber[quarter][variants], TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = minMaxLoc(result)

        if max_val > max_val_old:
            max_val_old = max_val
            variant = variants

    # checking if fish grab the bobber
    max_loc_old_array = bobber_scan_legacy(screen_area_bobber_image_recognition, quarter, variant)
    max_loc_old = max_loc_old_array[0]
    while (True):
        if stop_button == True: #stop button active
            return(3)
        time.sleep(0.02)  # slowing scan to catch pixel diffrence
        max_loc_array = bobber_scan_legacy(screen_area_bobber_image_recognition, quarter, variant)
        max_loc = max_loc_array[0]
        print("Bobber detection: ",round(max_loc_array[1],3)," Bobber loc: ",max_loc," Bobber ABS: ",abs(max_loc_old - max_loc))
        if abs(max_loc_old - max_loc) >= 2 and abs(max_loc_old - max_loc) <= 8:
            print("Fish detected!")
            return(0)
        max_loc_old = max_loc
#bobber on the water image recognition end

#random spot from spots array
def get_new_spot():
    return random.choice(coords)

#Runs the casting function
def cast_hook():
    global STATE,stop_button,mouse_pos,bobber_loc_array_initial,recognition_state,stuck_allert
    while 1:
        if (stop_button == False):
            if STATE == "CASTING" or STATE == "STARTED":
                time.sleep(1.6)
                bait_potion_counter()
                pyautogui.mouseUp()
                x, y = get_new_spot()
                mouse_pos = (int(x), int(y))
                pyautogui.moveTo(x, y, tween=pyautogui.linear, duration=0.2)

                bobber_loc_array_initial = bobber_scan()  # initial bobber scan before cast

                pyautogui.mouseDown()
                if long_cast == False:
                    time.sleep(random.uniform(0.4, 0.5))
                else:
                    time.sleep(random.uniform(0.8, 0.9))

                pyautogui.mouseUp()
                log_info(f"Rod casted!", logger="Information")
                time.sleep(1.5)
                if STATE != "STOPPED":
                    STATE = "CASTED"


            if (stop_button == False) and STATE == "CASTED":
                recognition_state = bobber_image_recognition()

                if recognition_state == 0:  # bobber found correctly
                    stuck_allert = 0
                    print("minigame")
                    do_minigame()

                if recognition_state == 1:  # Couldn't find bobber, major issue!
                    bobber_image_recognition()
                    log_info(f"Couldn't find a bobber, rescaning for the {stuck_allert} time",logger="Information")
                    stuck_allert = stuck_allert + 1

                    if stuck_allert > 20:
                        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
                        log_info(f"ERROR, COULDN'T FIND A BOBBER! RECASTING!",logger="Information")
                        STATE = "CASTING"
                        stuck_allert = 0

                if recognition_state == 2:  # Algorithm find more then 1 new bobber
                    log_info(f"More then 1 bobber in cast area, recasting", logger="Information")
                    STATE = "CASTING"

                if recognition_state == 3:  # Stop button active
                    STATE = "STOPPED"

                if recognition_state == 0:
                    break
        else:
            break

#Uses obj detection with OpenCV to find and track bobbers left / right coords
def do_minigame():
    global STATE,fish_count,bait_counter
    if STATE != "CASTING" and STATE != "STARTED" and STATE != "STOPPED":
        STATE = "SOLVING"
        log_info(f'Attempting Minigame',logger="Information")
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        #Initial scan. Waits for bobber to appear
        time.sleep(0.35)
        valid,location,size = Detect_Bobber()
        if valid == "TRUE":
            fish_count += 1
            bait_counter += 1
            while 1:
                valid,location,size = Detect_Bobber()
                if valid == "TRUE":
                    if location[0] < size * 0.8: #Solving minigame is faster if we stick to the right side, max is 0.8
                        pyautogui.mouseDown()
                    else:
                        pyautogui.mouseUp()
                else:
                    if STATE != "CASTING":
                        STATE = "CASTING"
                        pyautogui.mouseUp()
                        break
        else:
            if STATE != "STOPPED":
                STATE = "CASTING"

def bait_potion_counter():
    global bait_counter,potion_round,TIME,potion_round_refill

    if ((bait_counter % 10) == 0) and ((get_value("Use Bait")) == True):
        log_info(f'Using bait...', logger="Information")
        pyautogui.press("1")
        time.sleep(1)

    if ((int(TIME / 30)) > potion_round) and ((get_value("Use Potion")) == True):
        potion_round = potion_round + 1
        log_info(f'Using potion...', logger="Information")
        pyautogui.press("2")
        time.sleep(2)

    if ((bait_counter % 100) == 0) and ((get_value("Refill Bait")) == True):
        log_info(f'Refilling bait...', logger="Information")
        pyautogui.press("i")
        time.sleep(0.4)
        pyautogui.moveTo(789, 422, tween=pyautogui.linear, duration=0.3)
        pyautogui.mouseDown()
        pyautogui.moveTo(947, 287, tween=pyautogui.linear, duration=0.3)
        pyautogui.mouseUp()
        time.sleep(0.1)
        pyautogui.press("i")
        time.sleep(0.5)

    if ((int(TIME / 300)) > potion_round_refill) and ((get_value("Refill Potion")) == True):
        potion_round_refill = potion_round_refill + 1
        log_info(f'Refilling Potion...', logger="Information")
        pyautogui.press("i")
        time.sleep(0.4)
        pyautogui.moveTo(846, 422, tween=pyautogui.linear, duration=0.2)
        pyautogui.mouseDown()
        pyautogui.moveTo(820, 287, tween=pyautogui.linear, duration=0.2)
        pyautogui.mouseUp()
        time.sleep(0.1)
        pyautogui.press("i")
        time.sleep(0.5)

#Detects bobber in minigame box
def Detect_Bobber():
    global STATE,hook_manager
    start_time = time.time()
    with mss.mss() as sct:
        base = np.array(sct.grab(screen_area))
        base = np.flip(base[:, :, :3], 2)  # 1
        base = cvtColor(base, COLOR_RGB2BGR)
        bobber = imread(resource_path('bobber.png'))
        bobber = np.flip(bobber[:, :, :3], 2)  # 1
        bobber = cvtColor(bobber, COLOR_RGB2BGR)
        result = matchTemplate(base,bobber,TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = minMaxLoc(result)
        if max_val > 0.6:
            print(f"Bobber Found!. Match certainty:{max_val}")
            print("%s seconds to calculate" % (time.time() - start_time))
            return ["TRUE",max_loc,base.shape[1]]
        else:
            print(f"Bobber not found. Match certainty:{max_val}")
            print("%s seconds to calculate" % (time.time() - start_time))
            hook_manager = threading.Thread(target=cast_hook)
            hook_manager.start()
            return ["FALSE",max_loc,base.shape[1]]

def Detect_Bobber_support():
    global STATE,bobber,loaded_bobber_1920
    start_time = time.time()
    with mss.mss() as sct:
        base = np.array(sct.grab(screen_area))
        base = np.flip(base[:, :, :3], 2)  # 1
        base = cvtColor(base, COLOR_RGB2BGR)

        bobber = imread(resource_path('bobber_1920.png'))
        bobber = np.flip(bobber[:, :, :3], 2)  # 1
        bobber = cvtColor(bobber, COLOR_RGB2BGR)

        result = matchTemplate(base,bobber,TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = minMaxLoc(result)
        if max_val > 0.65:
            #print(f"Bobber Found!. Match certainty:{max_val}")
            #print("%s seconds to calculate" % (time.time() - start_time))
            return ["TRUE",max_loc,base.shape[1]]
        else:
            #print(f"Bobber not found. Match certainty:{max_val}")
            #print("%s seconds to calculate" % (time.time() - start_time))
            return ["FALSE",max_loc,base.shape[1]]

#Set resolution for minigame
def resolution_set():
    if get_value("Choose your resolution") == "1920x1080":
        screen_area = 839, 538, 1080, 566
        return(screen_area)

def bobber_quality():
    if get_value("Choose your game quality") == "Ultra":
        bobber_load()
    else:
        bobber_load_low_quality()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(r"C:\Users\Dawid\PycharmProjects\Aurora\images")

    return os.path.join(base_path, relative_path)


def screenshoter(): #not used
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    file_name = str(random.randint(0, 10000)) + "aurora.png"
    full_path = os.path.join(desktop, file_name)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(full_path)

##########################################################
#
#   These Functions are all Callbacks used by DearPyGui
#
##########################################################

#Move window game
def window_move(data,sender):
    hwnd = win32gui.FindWindow(None, "Albion Online Client")
    win32gui.SetWindowPos(hwnd,win32con.HWND_TOP, -7, 0, 1040, 807, True)    #1024,798

#Generates the areas used for casting
def generate_coords(sender,data):
    global coords,STATE,state_left
    coords = []
    amount_of_choords = get_value("Amount of fishing spots")
    for n in range(int(amount_of_choords)):
        n = n+1
        temp = []
        log_info(f'| Spot #{n} | Press Spacebar over the spot you want',logger="Information")
        while True:
            a = win32api.GetKeyState(0x20)
            if a != state_left:
                state_left = a
                if a < 0:
                    break
            time.sleep(0.001)
        x,y = pyautogui.position()
        temp.append(x)
        temp.append(y)
        coords.append(temp)
        if n != int(amount_of_choords):
            log_info(f'Spot Saved!',logger="Information")
        else:
            log_info(f'All spots saved, ready to start bot!', logger="Information")

#Starts the bots threads
def start(data,sender):
    global stop_button, STATE, total_time_start, screen_area, TIME, fish_count
    if STATE == "STOPPED" or STATE == "IDLE":
        STATE = "STARTING"
        TIME = 0
        fish_count = 0
        screen_area = 427, 413, 598, 433    #minigame area
        total_time_start = time.time()
        stop_button = False
        bobber_quality()

        hook_manager = threading.Thread(target = cast_hook)
        if stop_button == False:
            if len(coords) == 0:
                log_info(f'Please Select Fishing Coords first',logger="Information")
                return
            else:
                hook_manager.start()
                log_info(f'Bot Started',logger="Information")
        STATE = "STARTED"

#Stops the bot and closes active threads
def stop(data,sender):
    global stop_button,STATE
    STATE = "STOPPING"
    stop_button = True
    log_info(f'Stopping Hook Manager',logger="Information")
    pyautogui.mouseUp()
    STATE = "STOPPED"
    log_info(f'Stopped Bot',logger="Information")

#Title Tracking
def Setup_title():
    global bait_counter,potion_round,TIME,effeciency,License_days,stop_button
    scan = True
    while 1:
        total_time = time.time()
        TIME = round((total_time-total_time_start)/60)
        if TIME > 1000000:
            TIME = 0
        if TIME == 0:
            effeciency = 0
        else:
            effeciency = round((fish_count / ((total_time-total_time_start)/60)), 2)

        set_main_window_title(window_title_string)

        labels_update(0,0)

        if TIME % 2 == 0 and scan == True:
            scan = False
            License_data = (Aurora_login.login_verify_raw(username_entry, password_entry))
            License_status = License_data[0]
            License_days = License_data[1]
            if License_status == False:
                while(True):
                    labels_update(0, 0)
                    log_info(f'License Expired.', logger="Information")
                    log_info(f'Please contact Auror on discord!', logger="Information")
                    stop_button = True
                    time.sleep(5)

        if TIME % 2 != 0:
            scan = True

        time.sleep(5)


#Support mode
def support_mode(sender,data):
    global screen_area, valid, STATE
    if ((get_value("Support Mode")) == True) and (STATE == "IDLE" or STATE == "STOPPED"):
        log_info(f'Support mode on.',logger="Information")
        screen_area = resolution_set()
        while 1:
            old_valid = valid
            valid, location, size = Detect_Bobber_support()
            if valid == "TRUE":
                if location[0] < size * 0.8:  # Solving minigame is faster if we stick to the right side
                    pyautogui.mouseDown()
                else:
                    pyautogui.mouseUp()
            else:
                if old_valid == "TRUE" and valid == "FALSE":
                    pyautogui.mouseUp()
                time.sleep(0.3)
            if ((get_value("Support Mode")) == False):
                break
    else:
        log_info(f'Support mode off.', logger="Information")
        if (STATE != "IDLE" or STATE != "STOPPED"):
            log_info(f'Please stop the bot.', logger="Information")
        set_value("Support Mode",False)

def cast_setting(sender,data):
    global long_cast
    if get_value("Long cast (for ocean only)") == True:
        long_cast = True
    else:
        long_cast = False

#Exit from function
def exit(sender,data):
    for proc in psutil.process_iter():
        if "Aurora" in proc.name():
            proc.kill()

def labels_update(sender,data):
    global total,fish_count,TIME,effeciency,License_days
    fish_count_string = str(fish_count)
    TIME_string = str(TIME)
    effeciency_string = str(effeciency)
    License_days_string = str(License_days)
    set_value("##Caught fish: ", fish_count_string)
    set_value("##Bot uptime (minutes): ", TIME_string)
    set_value("##Fish caught per minute: ", effeciency_string)
    set_value("##Bot subscription expire in (days): ",License_days_string)


#Settings for DearPyGui window
set_main_window_size(500,500)
set_style_window_menu_button_position(0)
set_theme("Red")
set_global_font_scale(1)
set_main_window_resizable(False)

#Creates the DearPyGui Window
with window("AurorA Fishbot 1.6v",width = 500,height = 500, no_move = True):
    set_window_pos("AurorA Fishbot 1.6v",0,0)
    add_input_int("Amount of fishing spots",max_value=10,min_value=0,default_value=1,width= 70,tip = "Amount of Fishing Spots")
    add_same_line()
    add_button("Set location of fishing spots",callback=generate_coords,tip = "To select fishing spots press space")
    add_separator()
    add_button("Set game position",callback=window_move,tip="Sets game position in right place, works only in window mode")
    add_same_line()
    add_combo("Choose your game quality", items=["Low", "Ultra"], width=100, default_value="Ultra")
    add_separator()
    add_checkbox("Use Bait")
    add_same_line()
    add_checkbox("Use Potion")
    add_same_line()
    add_checkbox("Refill Bait")
    add_same_line()
    add_checkbox("Refill Potion")
    add_separator()
    add_checkbox("Long cast (for ocean only)", callback=cast_setting, tip="Use only for ocean where you need to cast rod in long range to make bobber visible")
    add_separator()
    add_checkbox("Support Mode", callback=support_mode, tip="Works only for 1920x1080, assist you at fishing")
    add_same_line()
    add_combo("Choose your resolution", items=["1920x1080", "2560x1440"], width=100, default_value="1920x1080")
    add_separator()
    add_button("Start Bot",callback=start,tip = "Starts the bot")
    set_item_color("Start Bot", mvGuiCol_Button, [0, 128, 0])
    add_same_line()
    add_button("Stop Bot",callback = stop,tip = "Stops the bot")
    set_item_color("Stop Bot", mvGuiCol_Button, [255, 100, 0])
    add_same_line()
    add_button("Exit Bot",callback = exit,tip = "Exit the bot")
    set_item_color("Exit Bot", mvGuiCol_Button, [255, 0, 0])
    add_separator()

    add_spacing(count=1)
    add_text("Bot subscription expire in (days):")
    add_same_line()
    add_label_text("##Bot subscription expire in (days): ", default_value="0")
    add_separator()

    add_text("AURORA FISHBOT STATISTIC:")
    add_spacing(count=3)

    add_text("Caught fish:")
    add_same_line()
    add_label_text("##Caught fish: ", default_value="0")
    add_spacing(count=1)

    add_text("Bot uptime (minutes):")
    add_same_line()
    add_label_text("##Bot uptime (minutes): ", default_value="0")
    add_spacing(count=1)

    add_text("Fish caught per minute:")
    add_same_line()
    add_text("##Fish caught per minute: ", default_value="0")
    add_spacing(count=1)

    add_separator()
    add_logger("Information",log_level=0,auto_scroll_button=False,copy_button=False,clear_button=False,filter=False)
    log_info(f'Aurora fishbot opened!',logger="Information")

threading.Thread(target = Setup_title).start()
start_dearpygui()

