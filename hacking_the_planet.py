import requests, re
from colorama import Fore, Back, Style
print("""
 db   db  .d8b.   .o88b. db   dD d888888b d8b   db  d888b    d888888b db   db d88888b 
 88   88 d8' `8b d8P  Y8 88 ,8P'   `88'   888o  88 88' Y8b   `~~88~~' 88   88 88'     
 88ooo88 88ooo88 8P      88,8P      88    88V8o 88 88           88    88ooo88 88ooooo 
 88~~~88 88~~~88 8b      88`8b      88    88 V8o88 88  ooo      88    88~~~88 88~~~~~ 
 88   88 88   88 Y8b  d8 88 `88.   .88.   88  V888 88. ~8~      88    88   88 88.     
 YP   YP YP   YP  `Y88P' YP   YD Y888888P VP   V8P  Y888P       YP    YP   YP Y88888P 
                                                                                      
                                                                                      
                   d8888b. db       .d8b.  d8b   db d88888b d888888b 
                   88  `8D 88      d8' `8b 888o  88 88'     `~~88~~' 
                   88oodD' 88      88ooo88 88V8o 88 88ooooo    88    
                   88~~~   88      88~~~88 88 V8o88 88~~~~~    88    
                   88      88booo. 88   88 88  V888 88.        88    
                   88      Y88888P YP   YP VP   V8P Y88888P    YP    
                                                                             
                                        .                                    
                                        +                                    
==,.                                    +                                    
oo°o+==-,                    .o=.      .+                                    
o0ooo°oo+++-,.               ,°    ,--,=+..                                  
°oooooo°°°+--,.                  ,,     .  ,,  .                             
+°+ooo°°+=-..            ..-++-=o+    . .    ,                               
+o++°°°+=####################o0$o++oø00+,=+.  ,                              
+°++++++###################+  =,,-øøo°°o-.,+.                                
=++++++o##################,   .  -+ +- °  ,.+  .                             
=+++++=,.,. . . ++.,,,.## #. ,..-ø-- ,#++  ,-. .                             
=+==++=            ,--,#######o+-+-°#####. -=,,=,.                           
=+-=+++  ...,----=+++++#######- ,° .#####, -+  .                             
-====+++----  ..,--=+++########=-o +#  . .,+= ,.                             
,--=---++++°, . .,,,-=+########°o0##= ...,++  -                              
,-,,,,,-=====.,---=°+=+=,.##-.+-..-o+++°++-  -                               
.,..,,,,-,,-, ,.   .++++=-===,-o+.  -+++=  ,= .                              
.,.  .,,,.,,.    ,  +++====,+-,=°°=,..+-.-+=.,°-                             
.,.     ....   ,,--=++++++--#°=-,=++=+0°+-,. ,-.                             
...          .,-,,-===+==+=-°o+=-,,..,o-.....  ..                            
 ..          .,-,.-==-==----..,---,..,o,.,..,..,...                          
 .            ,. .,------,,-,,,,,,-,,=o,,,,,...,,,.                          
      ..    ..,   ,---,------,,,,---,,-.,,,,,,,.....                         
           .,.     ..,,,,,,-,,,-,,-,.,..,,....   .,.                         
          ..         .,.,,,,,,,,,,,,,,,,,,,.........  .                      
         .            ....,,.,.,,,,,,,,,--,.,,,,.  ..                        
                       ..,,.......,,,,,,,,..,....  ..                        
                           . ........,..,,,.....      .                      
                                        .,.  ....                                                                                      
(FOR MORE PRIVACY): Copy the IP open Them in The TOR Browser :)
""")
print("""\033[1;37m
====================================================================================================================================================================
 \033[1;35m[#] \033[1;37mCoded By : AnonNews_irc 
 \033[1;35m[#] \033[1;37mTelegram : https://t.me/addlist/iZfJw-LVfYthNzYx                                                                                   
============================================================================================================================================================================================
 \033[1;35m[1] \033[1;37mUnited States                              \033[1;35m[33] \033[1;37mFinland                                    \033[1;35m[65] \033[1;37mNicaragua
 \033[1;35m[2] \033[1;37mJapan                                      \033[1;35m[34] \033[1;37mGreece                                     \033[1;35m[66] \033[1;37mSingapore
 \033[1;35m[3] \033[1;37mTaiwan, Province Of                        \033[1;35m[35] \033[1;37mAustralia                                  \033[1;35m[67] \033[1;37mSaudi Arabia
 \033[1;35m[4] \033[1;37mItaly                                      \033[1;35m[36] \033[1;37mHungary                                    \033[1;35m[68] \033[1;37mPanama
 \033[1;35m[5] \033[1;37mRussian Federation                         \033[1;35m[37] \033[1;37mLatvia                                     \033[1;35m[69] \033[1;37mNigeria
 \033[1;35m[6] \033[1;37mKorea, Republic Of                         \033[1;35m[38] \033[1;37mArgentina                                  \033[1;35m[70] \033[1;37mLuxembourg
 \033[1;35m[7] \033[1;37mGermany                                    \033[1;35m[39] \033[1;37mUkraine                                    \033[1;35m[71] \033[1;37mPeru
 \033[1;35m[8] \033[1;37mFrance                                     \033[1;35m[40] \033[1;37mThailand                                   \033[1;35m[72] \033[1;37mBelarus
 \033[1;35m[9] \033[1;37mCzech Republic                             \033[1;35m[41] \033[1;37mIsrael                                     \033[1;35m[73] \033[1;37mTrinidad And Tobago
 \033[1;35m[10] \033[1;37mAustria                                   \033[1;35m[42] \033[1;37mMexico                                     \033[1;35m[74] \033[1;37mAngola
 \033[1;35m[11] \033[1;37mSwitzerland                               \033[1;35m[43] \033[1;37mLithuania                                  \033[1;35m[75] \033[1;37mAruba
 \033[1;35m[12] \033[1;37mUnited Kingdom                            \033[1;35m[44] \033[1;37mNew Zealand                                \033[1;35m[76] \033[1;37mPuerto Rico
 \033[1;35m[13] \033[1;37mCanada                                    \033[1;35m[45] \033[1;37mEstonia                                    \033[1;35m[77] \033[1;37mSaint Kitts And Nevis
 \033[1;35m[14] \033[1;37mPoland                                    \033[1;35m[46] \033[1;37mEcuador                                    \033[1;35m[78] \033[1;37mCayman Islands
 \033[1;35m[15] \033[1;37mNorway                                    \033[1;35m[47] \033[1;37mColombia                                   \033[1;35m[79] \033[1;37mHonduras
 \033[1;35m[16] \033[1;37mNetherlands                               \033[1;35m[48] \033[1;37mBosnia And Herzegovina                     \033[1;35m[80] \033[1;37mGeorgiam
 \033[1;35m[17] \033[1;37mRomania                                   \033[1;35m[49] \033[1;37mIceland                                    \033[1;35m[81] \033[1;37mAlgeria
 \033[1;35m[18] \033[1;37mSweden                                    \033[1;35m[50] \033[1;37mSlovenia                                   \033[1;35m[82] \033[1;37mNew Caledonia
 \033[1;35m[19] \033[1;37mSpain                                     \033[1;35m[51] \033[1;37mMalaysia                                   \033[1;35m[83] \033[1;37mMacao
 \033[1;35m[20] \033[1;37mViet Nam                                  \033[1;35m[52] \033[1;37mChina                                      \033[1;35m[84] \033[1;37mBarbados
 \033[1;35m[21] \033[1;37mBulgaria                                  \033[1;35m[53] \033[1;37mMoldova, Republic Of                       \033[1;35m[85] \033[1;37mGuadeloupe
 \033[1;35m[22] \033[1;37mDenmark                                   \033[1;35m[54] \033[1;37mChile                                      \033[1;35m[86] \033[1;37mGuam
 \033[1;35m[23] \033[1;37mIran, Islamic Republic                    \033[1;35m[55] \033[1;37mBangladesh                                 \033[1;35m[87] \033[1;37mAndorra
 \033[1;35m[24] \033[1;37mBelgium                                   \033[1;35m[56] \033[1;37mHong Kong                                  \033[1;35m[88] \033[1;37mCosta Rica
 \033[1;35m[25] \033[1;37mBrazil                                    \033[1;35m[57] \033[1;37mSyria                                      \033[1;35m[89] \033[1;37mLaos
 \033[1;35m[26] \033[1;37mTurkey                                    \033[1;35m[58] \033[1;37mKazakhstan                                 \033[1;35m[90] \033[1;37mTanzania
 \033[1;35m[27] \033[1;37mSerbia                                    \033[1;35m[59] \033[1;37mFaroe Islands                              \033[1;35m[91] \033[1;37mMalta
 \033[1;35m[28] \033[1;37mSlovakia                                  \033[1;35m[60] \033[1;37mMontenegro                                 \033[1;35m[92] \033[1;37mMadagascar
 \033[1;35m[29] \033[1;37mIreland                                   \033[1;35m[61] \033[1;37mArmenia                                    \033[1;35m[93] \033[1;37mMacedonia
 \033[1;35m[30] \033[1;37mIndia                                     \033[1;35m[62] \033[1;37mPortugal                                   \033[1;35m[94] \033[1;37mGuernsey
 \033[1;35m[31] \033[1;37mIndonesia                                 \033[1;35m[63] \033[1;37mCroatia                                    \033[1;35m[95] \033[1;37mParaguay
 \033[1;35m[32] \033[1;37mSouth Africa                              \033[1;35m[64] \033[1;37mTunisia
============================================================================================================================================================================================

""")

try:
    print()
    countries = ["US", "JP", "TW", "IT", "RU", "KR", "DE", "FR", "CZ", "AT", "CH", "GB", "CA", "PL", "NO", "NL", "RO", "SE", "ES", "VN", "BG", "DK", "IR", "BE", "BR", "TR", "RS", "SK", "IE", "IN", "ID", "ZA", "FI", "GR", "AU", "HU", "LV", "AR", "UA", "TH", "IL", "MX", "LT", "NZ", "EE", "EC", "CO", "BA", "IS", "SI", "MY", "CN", "MD", "CL", "BD", "HK", "SY", "KZ", "FO", "ME", "AM", "PT", "HR", "TN", "NI", "SG", "SA", "PA", "NG", "LU", "PE", "BY", "TT", "AO", "AW", "PR", "KN", "KY", "HN", "GE", "DZ", "NC", "MO", "BB", "GP", "GU", "AD", "CR", "LA", "TZ", "MT", "MG", "MK", "GG", "PY","-"]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

# google dorks
  
    link =[
    "https://www.google.com/search?q=intitle:%22webcamxp%22%20%22Flash%20JPEG%20Stream%22"
    "https://www.google.com/search?q=inurl:mobile.html%20intitle:webcamXP"
    "https://www.google.com/search?q=intitle:%22Web%20Client%22%20inurl:%22webcamera.html%22"
    "https://www.google.com/search?q=intitle:%22HD%20IP%20Camera%22%20%22Remember%20me%22%20%22User%20name%22%20-.com%20-pdf"
    "https://www.google.com/search?q=intitle:%22IP%20Webcam%22%20inurl:%22/greet.html%22"
    "https://www.google.com/search?q=intitle:%22NetCamSC*%22"
    "https://www.google.com/search?q=intitle:%22NetCamXL*%22"
    "https://www.google.com/search?q=inurl:%22live/cam.html%22"
    ]

    num = int(input("Enter a number ---> "))
    print("""
    \033[1;35m
    [ Scraping IP Hosted Cameras... ]
    
    """)
    if num not in range(1, 21+1):
        raise IndexError
 #API
    country = countries[num-1]
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;35m[+] online camera :",ip)
except:
    pass
finally:
    print("\033[1;37m")
    exit()
