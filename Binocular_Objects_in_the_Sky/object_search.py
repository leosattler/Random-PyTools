################################################################
# Programa para calcular Nascer e Ocaso de determinado astro,
# dadas sua ascencao reta e declinacao e data de interesse. 
# Desenvolvido para as atividades do GOD (OV, UFRJ).
# Copyleft (:p) 2015 Leonardo Sattler: leonardo10@astro.ufrj.br
#
# Leonardo Sattler Cassara, Jan 18, 2015
# Universidade Federal do Rio de Janeiro
# Nota: Programa em desenvlvimento. Nao ha correcao para horario
# de verao. Nessas condicoes, adicionar uma hora aos resultados.
# Outputs sao duracao do Dia, hora do crepusculo astronomico, 
# nascer e ocaso do Sol e do astro. A opcao de retornar 
# Julian Date, assim como o LST do dia as 00:00, esta 
# desativada por nao ser de interesse para as atividades 
# do GOD. Latitude usada nos calculos: do Rio de Janeir.o
#
################################################################

########## Importing Packages ##########
import time
import numpy as np
########## Date to JD ########## (Epoch 1 Jan 4713 BC)

date = raw_input('Digite a data dd/mm/aaaa: ')

#hour = raw_input('Digite a hora hh:mm: ')
hour = '00:00'

h = float(hour.split(':')[0])
min = float(hour.split(':')[1])

d_frac = h/24. + min/(60.*24.)  # calculating fraction of day (12:00 = 0.5)

d = float(date.split('/')[0]) 
m = float(date.split('/')[1])
y = float(date.split('/')[2])

if m in (1, 2):
    y_new = y - 1
    m_new = m + 12
else:
    y_new = y
    m_new = m

if y > 1582:
    A = int(y_new/100.)
    B = 2 - A + int(A/4.)
else: 
    if m <= 10 and d <= 15:
        B = 0.

if y_new < 0:
    C = int(365.25 * y_new - 0.75) 
else:
    C = int(365.25 * y_new)

D = int(30.6001 * (m_new + 1))

JD = B + C + D + d + 1720994.5

JD_precise = JD + d_frac

##############################################################
########## JD to LST ########## 

S = JD - 2451545.0

T = S/36525.0

T0 = 6.697374558 + (2400.051336 * T) + (0.000025862 * T**2)

if T0 < 0:
    T0 = T0 + (-int(T0/24.) + 1) * 24 
else:
    T0 = T0 - (int(T0/24.)) * 24 

LT = h + min / 60.  # Local Time in decimals

LT = LT * 1.002737909

lst = T0 + LT

if lst > 24:
    lst = lst - 24.
if lst < 0:
    lst = lst + 24.

S_h = int(lst)
S_min = int((lst - S_h) * 60.)
#S_sec = int(((lst - S_h) * 60. - S_min) * 60)  # Seconds not
                                                # important. 

if len(str(S_min)) == 1:
    LST = str(S_h) + ':0' + str(S_min) #+ ':' + str(S_sec)
else:
    LST = str(S_h) + ':' + str(S_min) #+ ':' + str(S_sec)
##############################################################
########## Sunrise and Sunset times for the date ##########

## Testing if y is leap year (Ano bissexto)
if y%4 != 0:
    leap_year = 'false'
else:
    if y%100 != 0:
        leap_year = 'true'
    else:
        if y%400 != 0:
            leap_year = 'false'
        else:
            leap_year = 'true'

## Calculating day of the year
a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
day_y = d
if m > 2:
    if leap_year == 'true':
        day_y = day_y + 29
    if leap_year == 'false':
        day_y = day_y + 28

for i in a:
    if i < m:
        day_y = day_y + 31

for i in b:
    if i < m:
        day_y = day_y + 30

## Calculating Sun's declination for the date
parcel_1 = 0.98565*(day_y + 10)

parcel_2 = 1.914 * np.sin(0.98565*(day_y - 2))

sun_dec = np.arcsin(0.39779 * np.cos((parcel_1 + parcel_2) * (np.pi/180.)))  # Answer in 
                                                                             # radians. Eq. for 
                                                                             # Southern Hemisphere.

## Calculating Sunset/Sunrise Hour Angle
Lat_of_place = '-22 deg 54 min 10 sec'  # Rio de Janeiro
phi = -(22 + 54/60. + 10/3600.) * (np.pi/180.)  # in radians

event = np.arccos(-np.tan(sun_dec)*np.tan(phi))  # answer in radians

sunset_H = event * 180./np.pi  # in degrees
sunrise_H = 360. - sunset_H  # in degrees

## Calculating Sunset/Sunrise times (sunset_time = sunrise_hour_angle/15)
sunrise_time_dec = sunset_H/15.  # in decimal hours
sunrise_hour = int(sunrise_time_dec) 
sunrise_min = int((sunrise_time_dec - int(sunrise_time_dec))*60)
if len(str(sunrise_min)) == 1:
    sunrise_time = str(sunrise_hour) + ':0' + str(sunrise_min)
else:
    sunrise_time = str(sunrise_hour) + ':' + str(sunrise_min)

sunset_time_dec = sunrise_H/15.  # in decimal hours
sunset_hour = int(sunset_time_dec) 
sunset_min = int((sunset_time_dec - int(sunset_time_dec))*60)
if len(str(sunset_min)) == 1:
    sunset_time = str(sunset_hour) + ':0' + str(sunset_min)
else:
    sunset_time = str(sunset_hour) + ':' + str(sunset_min)

## Length of day
length_hour = int((sunrise_H - sunset_H)/15.)
length_min = int(((sunrise_H - sunset_H)/15 - length_hour)*60)
if len(str(length_min)) == 1:
    length_day = str(length_hour) + ':0' + str(length_min)
else:
    length_day = str(length_hour) + ':' + str(length_min)

## Calculating Astronomical Twilight (total darkness, sun 14 deg below horizon)
alt_sun = -18 * np.pi/180  # Sun's altitude at 
                           # Astronomical twilight 
                           # (sky completely dark). 
                           # Answer in radians

parcel_1 = np.sin(alt_sun) / (np.cos(sun_dec)*np.cos(phi))
parcel_2 = -np.tan(sun_dec)*np.tan(phi)

twilight_H = (np.arccos(parcel_1 + parcel_2) * 180./np.pi) 

delta_H = (twilight_H - event*(180/np.pi)) / 15.
delta_H = delta_H * 0.9973

twilight_1_dec = sunrise_time_dec - delta_H  # twilight before sunrise in decimals

twilight_1_hour = int(twilight_1_dec) 
twilight_1_min = int((twilight_1_dec - int(twilight_1_dec))*60)
if len(str(twilight_1_min)) == 1:
    twilight_1 = str(twilight_1_hour) + ':0' + str(twilight_1_min)
else:
    twilight_1 = str(twilight_1_hour) + ':' + str(twilight_1_min)

twilight_2_dec = sunset_time_dec + delta_H  # twilight after sunset in decimals

twilight_2_hour = int(twilight_2_dec) 
twilight_2_min = int((twilight_2_dec - int(twilight_2_dec))*60)
if len(str(twilight_2_min)) == 1:
    twilight_2 = str(twilight_2_hour) + ':0' + str(twilight_2_min)
else:
    twilight_2 = str(twilight_2_hour) + ':' + str(twilight_2_min)
##############################################################
########## Object's rise and set ##########

o_alpha = raw_input('Ascencao reta do objeto (hour:min) ')
o_dec = raw_input('Declinacao do objeto (deg:min): ')

o_alpha_h = float(o_alpha.split(':')[0])
o_alpha_m = float(o_alpha.split(':')[1])

o_dec_h = float(o_dec.split(':')[0])
o_dec_m = float(o_dec.split(':')[1])

alpha_decimal = (o_alpha_h + o_alpha_m / 60.) # in degrees
dec_decimal = (o_dec_h + o_dec_m / 60.) * np.pi/180  # in radians

o_H = (np.arccos(-np.tan(phi)*np.tan(dec_decimal))) * (180/np.pi) / 15.  # Hour angle in decimals

LST_o = alpha_decimal  # (at meridian) LST at meridian = right ascention

## LST to Local Time
S = JD - 2451545.0

T = S/36525.0

T0 = 6.697374558 + (2400.051336 * T) + (0.000025862 * T**2)

if T0 < 0:
    T0 = T0 + (-int(T0/24.) + 1) * 24 
else:
    T0 = T0 - (int(T0/24.)) * 24 

LST_o = LST_o - T0
if LST_o > 24:
    LST_o = LST_o - 24.
if LST_o < 0:
    LST_o = LST_o + 24.

LT_o = LST_o * 0.9972695663  # Local Time when object is at meridian

LT_r = LT_o - o_H  # rises at LT (at meridian - o_H)
if LT_r > 24:
    LT_r = LT_r - 24.
if LT_r < 0:
    LT_r = LT_r + 24.
LT_r_h = int(LT_r)
LT_r_m = int((LT_r - LT_r_h) * 60.)
if len(str(LT_r_m)) == 1:
    Time_o_rise = str(LT_r_h) + ':0' + str(LT_r_m)
else:
    Time_o_rise = str(LT_r_h) + ':' + str(LT_r_m)

LT_s = LT_o + o_H  # sets at LT (at meridian + o_H)
if LT_s > 24:
    LT_s = LT_s - 24.
if LT_s < 0:
    LT_s = LT_s + 24.
LT_s_h = int(LT_s)
LT_s_m = int((LT_s - LT_s_h) * 60.)
if len(str(LT_s_m)) == 1:
    Time_o_set = str(LT_s_h) + ':0' + str(LT_s_m)
else:
    Time_o_set = str(LT_s_h) + ':' + str(LT_s_m)
##############################################################
########## Printing Results ##########

#print
#print 'JD for the date: ', JD  # Not used
#print
#print 'Local Sidereal Time (LST) at midnight: ', LST  # Not used
print
print 'Duracao do dia: ', length_day
print
print 'Crepusculo astronomico (Nascer do Sol): ', twilight_1
print
print 'Nascer do Sol: ', sunrise_time
print
print 'Por do Sol: ', sunset_time
print
print 'Crepusculo astronomico (Por do Sol): ', twilight_2
print
print 'Nascer do objeto: ', Time_o_rise
print 
print 'Ocaso do objeto: ', Time_o_set
