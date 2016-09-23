#CS:GO Crosshair Generator
import random, string, shutil, os, datetime

#def copy2clip(text):  Not working atm
    #import subprocess
    #cmd = 'echo ' + text.strip() + '|clip'
    #return subprocess.check_call(cmd, shell = True)

    #try:
        #import Tkinter as tk
    #except ImportError:
        #import tkinter as tk
    #try:
        #root = tk.Tk()
        #root.withdraw()
        #root.clipboard_clear()
        #root.clipboard_append(text)
        #return True
    #except:
        #return False
    


players = {'get_right':'''\
cl_crosshair_drawoutline "0"
cl_crosshair_dynamic_maxdist_splitratio "0.35"
cl_crosshair_dynamic_splitalpha_innermod "1"
cl_crosshair_dynamic_splitalpha_outermod "0.5"
cl_crosshair_dynamic_splitdist "7"
cl_crosshair_outlinethickness "1"
cl_crosshairalpha "200"
cl_crosshaircolor "1"
cl_crosshaircolor_b "0"
cl_crosshaircolor_g "0"
cl_crosshaircolor_r "0"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairscale "0"
cl_crosshairsize "5"
cl_crosshairstyle "4"
cl_crosshairthickness "1.15"
cl_crosshairusealpha "1"
cl_fixedcrosshairgap "3"''',\
           'friberg':'''\
cl_crosshair_drawoutline "0"
cl_crosshair_dynamic_maxdist_splitratio "0.35"
cl_crosshair_dynamic_splitalpha_innermod "1"
cl_crosshair_dynamic_splitalpha_outermod "0.5"
cl_crosshair_dynamic_splitdist "7"
cl_crosshair_outlinethickness "1"
cl_crosshairalpha "99999"
cl_crosshaircolor "4."
cl_crosshaircolor_b "147"
cl_crosshaircolor_g "20"
cl_crosshaircolor_r "255"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairscale "1550"
cl_crosshairsize "2.3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"
cl_fixedcrosshairgap "3"''',\
           'pasha':'''\
cl_crosshair_drawoutline "0"
cl_crosshair_dynamic_maxdist_splitratio "0.35"
cl_crosshair_dynamic_splitalpha_innermod "1"
cl_crosshair_dynamic_splitalpha_outermod "0.5"
cl_crosshair_dynamic_splitdist "7"
cl_crosshair_outlinethickness "1"
cl_crosshairalpha "255"
cl_crosshaircolor "1"
cl_crosshaircolor_b "147"
cl_crosshaircolor_g "20"
cl_crosshaircolor_r "255"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairscale "1550"
cl_crosshairsize "4"
cl_crosshairstyle "5"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"
cl_fixedcrosshairgap "3"''',\
           'seang@res':'''\
cl_crosshair_drawoutline "0"
cl_crosshair_dynamic_maxdist_splitratio "0.0"
cl_crosshair_dynamic_splitalpha_innermod "1"
cl_crosshair_dynamic_splitalpha_outermod "0.300000"
cl_crosshair_dynamic_splitdist "5"
cl_crosshair_outlinethickness "1"
cl_crosshairalpha "255"
cl_crosshaircolor "1"
cl_crosshaircolor_b "0"
cl_crosshaircolor_g "255"
cl_crosshaircolor_r "0"
cl_crosshairdot "0"
cl_crosshairgap "-1.500000"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairscale "0"
cl_crosshairsize "4.500000"
cl_crosshairstyle "4"
cl_crosshairthickness "1.000000"
cl_crosshairusealpha "1"
cl_fixedcrosshairgap "3"''',\
            'summit1g':'''\
cl_crosshair_drawoutline "0"
cl_crosshair_dynamic_maxdist_splitratio "0.0"
cl_crosshair_dynamic_splitalpha_innermod "1"
cl_crosshair_dynamic_splitalpha_outermod "0.300000"
cl_crosshair_dynamic_splitdist "5"
cl_crosshair_outlinethickness "1"
cl_crosshairalpha "255"
cl_crosshaircolor "3"
cl_crosshaircolor_b "0"
cl_crosshaircolor_g "255"
cl_crosshaircolor_r "0"
cl_crosshairdot "0"
cl_crosshairgap "-1.500000"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairscale "0"
cl_crosshairsize "4.500000"
cl_crosshairstyle "0"
cl_crosshairthickness "1.000000"
cl_crosshairusealpha "1"
cl_fixedcrosshairgap "3"''',\
           'n0thing':'''\
cl_crosshair_drawoutline "0"
cl_crosshair_dynamic_maxdist_splitratio "0.35"
cl_crosshair_dynamic_splitalpha_innermod "1"
cl_crosshair_dynamic_splitalpha_outermod "0.5"
cl_crosshair_dynamic_splitdist "7"
cl_crosshair_outlinethickness "1"
cl_crosshairalpha "300"
cl_crosshaircolor "1"
cl_crosshaircolor_b "0"
cl_crosshaircolor_g "0"
cl_crosshaircolor_r "250"
cl_crosshairdot "0"
cl_crosshairgap "1.5"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairscale "0"
cl_crosshairsize "5"
cl_crosshairstyle "4"
cl_crosshairthickness "1.5"
cl_crosshairusealpha "1"
cl_fixedcrosshairgap "3"''',\
           'kennys':'''\
cl_crosshair_drawoutline "1"
cl_crosshair_outlinethickness "1"
cl_crosshairalpha "200"
cl_crosshaircolor "4"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'kioshima':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "800"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'nbk':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "200"
cl_crosshaircolor "4"
cl_crosshairdot "1"
cl_crosshairgap "-1.5"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "2"
cl_crosshairstyle "4"
cl_crosshairthickness "0"
cl_crosshairusealpha "1"''',\
           'apex':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "200"
cl_crosshaircolor "4"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "6"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'happy':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "8888"
cl_crosshaircolor "4"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "2"
cl_crosshairstyle "4"
cl_crosshairthickness "0.9"
cl_crosshairusealpha "1"''',\
           'pronax':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "1000"
cl_crosshaircolor "4"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "0.05"
cl_crosshairusealpha "1"''',\
           'olofmeister':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "800"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-2.5"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "4"
cl_crosshairstyle "4"
cl_crosshairthickness "0"
cl_crosshairusealpha "1"''',\
           'flusha':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "999"
cl_crosshaircolor "5"
cl_crosshairdot "0"
cl_crosshairgap "-3"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'jw':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "200"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "4"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'krimz':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "500"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-3"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'f0rest':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "999'"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "6"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'xizt':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "255"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "1.5"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3.5"
cl_crosshairstyle "4"
cl_crosshairthickness "0"
cl_crosshairusealpha "1"''',\
           'allu':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "800"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'device':'''\
cl_crosshair_drawoutline "1"
cl_crosshair_outlinethickness "1"
cl_crosshairalpha "800"
cl_crosshaircolor "2"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'xyp9x':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "200"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "0"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "5"
cl_crosshairstyle "4"
cl_crosshairthickness "0.5"
cl_crosshairusealpha "1"''',\
           'cajunb':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "800"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-3"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "4"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'dupreeh':'''\
cl_crosshair_drawoutline "1"
cl_crosshair_outlinethickness "1"
cl_crosshairalpha "255"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'karrigan':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "1000"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "0.5"
cl_crosshairusealpha "1"''',\
           'fns':'''\
cl_crosshair_drawoutline "1"
cl_crosshair_outlinethickness "1"
cl_crosshairalpha "999"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "0"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'cutler':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "999"
cl_crosshaircolor "4"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"''',\
           'jdm64':'''\
cl_crosshaircolor "3"
cl_crosshairstyle "1"
cl_fixedcrosshairgap "-4.5"
hud_showtargetid "0"''',\
           'hazed':'''\
cl_crosshair_drawoutline "1"
cl_crosshair_outlinethickness "1"
cl_crosshaircolor "5"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "2"
cl_crosshairstyle "4"
cl_crosshairthickness "0.75"''',\
           'tarik':'''\
cl_crosshaircolor "1"
cl_crosshairstyle "1"
cl_fixedcrosshairgap "-4.5"
hud_showtargetid "0"''',\
           'freakazoid':'''\
cl_crosshair_drawoutline "1"
cl_crosshair_outlinethickness "0.5"
cl_crosshaircolor "5"
cl_crosshairdot "0"
cl_crosshairgap "-0.5"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "2.5"
cl_crosshairstyle "4"
cl_crosshairthickness "1"''',\
           'skadoodle':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "200"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'shroud':'''\
cl_crosshair_drawoutline "1"
cl_crosshair_outlinethickness "1"
cl_crosshairalpha "255"
cl_crosshaircolor "4"
cl_crosshairdot "0"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "5"
cl_crosshairstyle "4"
cl_crosshairthickness "1.5"
cl_crosshairusealpha "1"''',\
           'twist':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "500"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-1.5"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3.5"
cl_crosshairstyle "4"
cl_crosshairthickness "0.5"
cl_crosshairusealpha "1"''',\
           'zeves':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "500"
cl_crosshaircolor "5"
cl_crosshaircolor_b "250"
cl_crosshaircolor_g "250"
cl_crosshaircolor_r "250"
cl_crosshairdot "0"
cl_crosshairgap "-3"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'zende':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "255"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairsize "2"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'rubino':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "9999"
cl_crosshaircolor "4"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "4"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'pimp':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "255"
cl_crosshaircolor "5"
cl_crosshaircolor_b "0"
cl_crosshaircolor_g "0"
cl_crosshaircolor_r "255"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "2"
cl_crosshairstyle "4"
cl_crosshairthickness "0"
cl_crosshairusealpha "1"''',\
           'msl':'''\
cl_crosshaircolor "1"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairdot "0"
cl_crosshairalpha "500"
cl_crosshairgap "-3"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"
cl_crosshair_drawoutline "0"''',\
           'tenzki':'''\
cl_crosshair_drawoutline "0"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-4"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "6"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'aizy':'''\
cl_crosshair_drawoutline "0"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "4"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshaircolor "4"''',\
           'kjaerbye':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "200"
cl_crosshaircolor "1"
cl_crosshairdot "1"
cl_crosshairgap "1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "2.3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'jkaem':'''\
cl_crosshairdot "0"
cl_crosshair_drawoutline "0"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "2"
cl_crosshaircolor "0"
cl_crosshairgap "-1"
cl_crossahairstyle "5"
cl_crosshairtickness "1"''',\
           'maikelele':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "255"
cl_crosshaircolor "1"
cl_crosshairdot "1"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "4"
cl_crosshairstyle "4"
cl_crosshairthickness "-1"
cl_crosshairusealpha "1"''',\
           'rain':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "250"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "2"
cl_crosshairstyle "4"
cl_crosshairthickness "0"
cl_crosshairusealpha "1"''',\
           'fox':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "200"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "0"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "2.5"
cl_crosshairstyle "5"
cl_crosshairthickness "0.5"
cl_crosshairusealpha "1"''',\
           'dennis':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "200"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "4"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'seized':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "200"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairsize "5.5"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'edward':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "999'"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "4"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'zeus':'''\
cl_crosshair_drawoutline "1"
cl_crosshair_outlinethickness "1"
cl_crosshairalpha "250"
cl_crosshaircolor "1"
cl_crosshairdot "1"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "4.7"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'flamie':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "999'"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "5"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'guardian':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "200"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "0"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "2"
cl_crosshairstyle "4"
cl_crosshairthickness "0.5"
cl_crosshairusealpha "1"''',\
           'hiko':'''\
cl_crosshair_drawoutline "1"
cl_crosshair_outlinethickness "0.5"
cl_crosshairalpha "200"
cl_crosshaircolor "4"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "4.5"
cl_crosshairstyle "4"
cl_crosshairthickness "1"
cl_crosshairusealpha "1"''',\
           'liquid_adren':'''\
cl_crosshair_drawoutline "1"
cl_crosshair_outlinethickness "1"
cl_crosshairalpha "250"
cl_crosshaircolor "4"
cl_crosshairdot "0"
cl_crosshairgap "0"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "1"''',\
           'nitr0':'''\
cl_crosshairstyle "5"
cl_crosshairsize "3.5"
cl_crosshair_drawoutline "1"
cl_crosshairthickness "1"
cl_crosshair_outlinethickness "0.4"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "1"''',\
           'fugly':'''\
cl_crosshairstyle "5"
cl_crosshairsize "3.5"
cl_crosshair_drawoutline "0"
cl_crosshairthickness "1.15"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "1"''',\
           'elige':'''\
cl_crosshaircolor "1"
cl_crosshairstyle "1"
cl_fixedcrosshairgap "-4.5"
hud_showtargetid "0"''',\
           'scream':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "255"
cl_crosshaircolor "4"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "1"
cl_crosshairstyle "4"
cl_crosshairthickness "0"
cl_crosshairusealpha "1"''',\
           'shox':'''\
cl_crosshair_drawoutline "0"
cl_crosshair_dynamic_maxdist_splitratio "0.35"
cl_crosshair_dynamic_splitalpha_innermod "1"
cl_crosshair_dynamic_splitalpha_outermod "0.5"
cl_crosshair_dynamic_splitdist "7"
cl_crosshairalpha "800"
cl_crosshaircolor "4"
cl_crosshairdot "0"
cl_crosshairgap "-2"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "2"
cl_crosshairstyle "2"
cl_crosshairthickness "1.15"
cl_crosshairusealpha "1"''',\
           'ex6tenz':'''\
cl_crosshair_drawoutline "0"
cl_crosshair_dynamic_maxdist_splitratio "0.35"
cl_crosshair_dynamic_splitalpha_innermod "1"
cl_crosshair_dynamic_splitalpha_outermod "0.5"
cl_crosshair_dynamic_splitdist "7"
cl_crosshairalpha "200"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "0"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "1"
cl_crosshairstyle "2"
cl_crosshairthickness "0.5"
cl_crosshairusealpha "1"''',\
           'rpk':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "200"
cl_crosshaircolor "1"
cl_crosshairdot "0"
cl_crosshairgap "0"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "5"
cl_crosshairstyle "4"
cl_crosshairthickness "1.15"
cl_crosshairusealpha "1"''',\
           'smithzz':'''\
cl_crosshair_drawoutline "0"
cl_crosshairalpha "255"
cl_crosshaircolor "4"
cl_crosshairdot "0"
cl_crosshairgap "-1"
cl_crosshairgap_useweaponvalue "0"
cl_crosshairsize "3"
cl_crosshairstyle "4"
cl_crosshairthickness "1.25"
cl_crosshairusealpha "1"''',\
           }

# ---------- MAIN PROGRAM ----------

writeConfig = False

print("This program contains CS:GO pro player crosshair configurations for you to use in-game.\n")

writeConfig = input("Would you like this program to write the crosshair configurations straight to your CS:GO config file? [Y/N]: ")

if writeConfig.lower() == 'y':
    writeConfig = True
    defaultPath = "C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\config.cfg"
    path = None
    while True:
        try:
            with open('CSGO_Config_Path.txt', 'r') as f:
                path = f.read()
                break
        except IOError:
            print("Existing CSGO path not found.\n")

        try:
            path = defaultPath
            with open(path, 'r') as test:
                test.read()
            break
        except IOError:
            print("CSGO path not found in drive C:\\.\n")
            path = None
            
        if path == None:
            path = input("Paste your CS:GO config folder path here (It should look something like \"... ...\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\"): ")
        
            if path[(len(path) - 4):] == '\cfg':
                path = path + '\config.cfg'
                break
            
        print("Incorrect path received.")

    with open('CSGO_Config_Path.txt', 'w') as f:
        f.write(path)

else:
    writeConfig = False

print("Players: ")

for playerName in list(players.keys()):  
    print("- {}".format(playerName))

print("="*80)

while True:
    playerName = input("Enter a player's name: ").lower()
    if playerName not in players.keys():
        print("Player not found. Please try again.\n")
        continue

    if writeConfig == False:
        consoleFriendly = input("Display a console-friendly version? [Y/N]: ")
        
        if consoleFriendly.lower() == 'y':
            rawData = players[playerName]
            crosshair = rawData.replace('\n', ';')
            print("You can paste this text directly into your CS:GO developer console.")
        else:
            crosshair = players[playerName]
            print("You cannot paste this text directly into the developer console. It'll have to be line-by-line or you'll need to create a config file.")
            
        print("\n" + crosshair + "\n")

        #Copy to clipboard using tkinter/subprocess not working. I'll try to fix this later on.
        #copy = input("Copy this text to your clipboard? [Y/N]: ")
        
        #if copy.lower() == 'y':
            #if copy2clip(crosshair):         
                #print("The text has been copied.")
            #else:
                #print("Something went wrong while trying to copy.")

    elif writeConfig == True:
        now = datetime.datetime.now()
        
        backupFileName = "CSGO_Config_Backup_" + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second) + '__' + str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ".cfg"
        shutil.copyfile(path, backupFileName)
        print("A backup file called \"{}\" has been created in \"{}\"".format(backupFileName, os.path.abspath("")))

        crosshair = players[playerName]
        print("\n" + crosshair + "\n")
            
        with open(path, 'a') as f:
            f.write(players[playerName])
            
        print("\nThe CS:GO config has been edited.")

    print("="*80)


















