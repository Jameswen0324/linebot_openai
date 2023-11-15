from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#======python的函數庫==========
import tempfile, os
import datetime
import openai
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
# Channel Secret
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))
# OPENAI API Key初始化設定
openai.api_key = os.getenv('OPENAI_API_KEY')





# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

#word 函式庫
import random
#output文字庫
def Fun(n):
    s=['試試\"抽妹子\"吧','試試\"今日運勢\"吧','聊聊政府?','可以叫我講笑話','試試\"拿優惠\"吧','試試\"測顏值\"吧']
    return s[n]
def nineoutput(n):
    s=['天會黑，人會變，三分情，七分騙。','只在點菸時低頭 只對愛的人溫柔','江湖真是一條不歸路。but，讓我再選一次，我一樣要做兄弟',
        '不離不棄 是我兄弟','人在江湖飄 哪能不挨刀','走的是時光 過的是滄桑','割線不打霧 街頭愛耍酷','甲K孝廉家，甲故變頭家',
        '上了我的床 走路要扶牆','路還長 別猖狂','我把你當兄弟 你把我當煙蒂','玫瑰帶刺 人心帶私 宇智波帶土','紙包不住火 你包不住我',
        '和諧社會 你我都是鼠輩','來生願做小公主 只吃雞巴不吃苦','一聲兄弟 一生兄弟','做兄弟的 不管利益 只講義氣','我不渣 我只是想給天下的女孩都有一個家',
        '110帶我走，119扛你走','當我穿上西裝 我跟你講道理當我脫下西裝 我就是道理']
    return s[n]
def joke(n):
    s=['我啊，全天下最好笑的笑話，可憐沒人愛，功課也差，長的又醜，不說了我想睡了，還要吃20顆安眠藥才睡得著呢','小明跑得很快有一次他和火車賽跑結果他贏了 為什麼？..............................因為他真的跑得很快',
    '有一天我幫我家的貓換比較細的貓砂，結果牠很不爽的跟我說：這沙小','為什麼模範生很容易被綁架？因為他一臉好榜樣','為什麼客家人都喜歡喝可樂.........摳啦','魔術師：我可以把東西變不見\n周湯豪：好哦（拿著泡好的泡麵把我的湯變不見 \n魔術師：沒問題（彈指）\n 周豪看了一眼泡麵說：屁啦湯明明還在',
    '老師問：現在有兩顆鳳梨，請問哪一顆比較好吃? \n小明：躺著的那顆，因為站久了會酸','有沒有人跟你討論過全熟牛排有多好吃\n：沒有，因為他還在嚼','小美剛進公司不到一年,就被老闆升職到高位,不服小美升官快速的職員紛紛在私下傳:小美一定靠背景!老闆聽到員工的流言心想對阿!小美的確靠北緊',
    '衛生紙還沒用過是白色，那用過以後是什麼色...................垃圾','很遜的人會被關在哪裡？.................偵訊室','你知道為什麼張雨生從森林走出來時手上有木頭嗎..........................因為那是雨生鋸來的😎😎','什麼動物最凶.....猩猩 因為他敲胸','有一天小明進了山洞然後就變成明進洞了',
    '花好笑，因為她有梗。老樹不好笑，因為它老梗。電鋸超好笑，因為他會梗梗梗梗梗梗.......','為什麼現在工廠都要全面機械化？..............因為勞力士很貴的','叫天天不應...叫哥 哥布林','說個客家人的笑話.......................算了我省起來好了','狗會汪汪\n貓會喵喵\n那雞會什麼？\n雞會是留給準備好的人',
    '婚除了可以結跟離還可以幹嘛..............婚一支一支一支的點','北極熊生活的很無聊有天覺得自己身上的毛很多就開始一根一根的拔拔到了最後..............幹!好冷','魯肅參加一場宴席，主人過來向他打招呼。\n主：魯肅近來可好？\n肅：最近過得還算不錯\n主：那魯夫人呢？\n肅：在偉大的航道上',
    '這次肺炎\n有個確診病患依然躺在病床上\n醫師巡診完看病人依然無法靠自己呼吸\n醫師對著護士說：「吸氧依舊那麼沒力」\n護士：「明天還是好天氣？」','為什麼饒舌歌手買不到葡萄？\n因為每次去水果行都會跟老闆說：yo～老闆，給我一袋葡萄～yo。','老師：請大家分享一個突出的人的故事。\n小明：我的阿嬤。\n老師：哦？你的阿嬤？他有什麼突出的地方？\n小明：------我們的阿嬤他椎間盤突出',
    '小明忘了繳學費，所以他拿著繳費單去問同學：「你有繳交嗎？」....同學：「我還有手手喔」','劉備跟關羽說：好多士兵戰死了你到他們的墳前上上香吧 \n十個月後 孫尚香懷了個紅臉的男嬰','章魚\n 魷魚\n 海龜\n 水母花枝\n 鯊魚\n海豚\n 幹 花枝亂站','鎖匠和大學生誰的學歷比較高 。 。 。 。 。 鎖匠 因為他研究鎖的',
    '很老的神木叫什麼.....超齡老木','頒獎典禮 拿銀牌 跟 拿金牌的 哪個比較糗\n 金牌的 因為金牌糗','有一天和一个同志朋友去餐厅吃饭\n 同志点的咖喱送到了\n 我: 咖喱给gay \n服务生:……… boom boom boom...','項羽去星巴克買咖啡店員：請問貴姓？\n：項店員：你啦！\n：項啦！\n店員：你啦！！！','玲刪:欸 小統，你知道甲乙丙丁戊己下一句怎麼唱嗎？\n 小統:蛤，我不知道。\n 玲刪:你不會庚辛你要先講，好嗎?',
    '小明爬到2樓，為何會覺的腿很酸\n因為他踩到檸檬','哪兩個歌手最適合搭在一起？\n . . . . . . .周杰倫 和 信 \n因為周杰倫就是屌，信誓旦旦。\n 一個酷酷的諧音梗😎😎','警察工作勞累跑去找師傅拔罐拔完後\n師傅就被銬上手銬師傅：「蝦密？我犯了什麼罪？」\n警察：「......你拔我罐罪」',
    '上次跟我3個朋友去喝酒喝完酒就開車走了\n突然遇到酒測臨檢警察：怎麼有酒味？\n我說：我們只有4位⋯','甲蛙跟乙蛙 哪隻青蛙最不會叫\n . . . . . . . . . . . . . . . . . 甲蛙 甲蛙懶叫','大家都知道酒精吧酒精就是乙醇嘛齁\n那大家知道甲醚是什麼嗎？\n甲醚就是當你不想吃飯的時候就可以吃麵',
    '台女玩鬼抓人........追不到我的人可以追我的ig💕','有一天小雞跟小鴨一起回家\n到了路口小雞跟小鴨說:小鴨掰\n小鴨就跟小雞說:\n...........再見','一大早警衛在笑什麼？\n..........校門口','我姓范\n講話冷冰冰的\n朋友都叫我..............................態度好一點','企鵝死掉會變成什麼\n鵝..............因為他沒氣了',
    '小燈泡為啥吃buffet不用錢\n . . . . . . . . . . . 因為不算人頭','有一天警方收到線報\n 得知一名戀童癖正在對女孩幹那檔事\n 立刻趕到現場破門而入\n 警察一腳把門踹開: 不要動! 你在幹嘛?\n 戀童癖: ... ... 這是玩童你知道的!','有一天，小明把小美的三倍券弄丟了，於是他很著急地把這件事告訴小美。\n小明：小美，該怎麼辦啊？\n小美：拿新券。.....\n小明：還是討厭下雨天。']
    return s[n]
def blue(n):
    s=['你1450?','好的，塔綠班','2024重建藍天','中華民國不能亡','你綠蛆?','菜陰魂執政的下場','冥禁黨不倒，台灣不會好','你台獨覺青?','罷免菜陰魂','假博士下台','冥禁黨不倒，萊豬吃到飽']
    return s[n]
def green(n):
    s=['人一藍，腦就殘','你中共同路人?','4個不同意，台灣更有力']
    return s[n]
def badoutput(n):
    s=['三小','死媽','沙小','啥小','幹','哩沙小阿?輸贏拉','操','肏','fuck','nmsl','滾','廢物','閉嘴','7414','爛','NMSL','Nmsl','姬芭','雞巴','雞八','雞掰','基八','基掰','幹你涼']
    return s[n]
def wangoutput(n):
    s=['優質na','浪漫na','約嗎']
    return s[n]
def luck():
    
   
    
    mainL=random.randint(1, 10)
    m1=random.randint(0, 4)
    #m2=random.randint(1, 10)
    #m3=random.randint(1, 10)
    #m4=random.randint(1, 10)
    #m5=random.randint(1, 10)
    #5star
    five=['運勢★★★★★：\n好耶買樂透會中，快去買','運勢★★★★★：\n晚上可以做到愛恭喜','運勢★★★★★：\n路上會撿到學妹Lucky you',
    '運勢★★★★★：\n你今天會邂逅到愛情，且異性會自貼，恭喜!但抽到本格機率只有2%，此格為大反轉格，異性會是龍，你會被強上，而且她太重你也躲不了，認命吧，物極必反\n實際運勢-★★★★★★★★★★：祝幸福ღゝ◡╹)ノ♡','運勢★★★★★：本學期歐趴\n']
    #4star
    four=['運勢★★★★☆：今天如果有考試，會及格\n','運勢★★★★☆：\n吃飯打卡會送小東西。','運勢★★★★☆：\n今天路上會看到可愛妹子','運勢★★★★☆：今天在遊戲裡是歐洲人\n','運勢★★★★☆：\n心情愉快，整天都很開心！']
    #3star
    three=['運勢★★★☆☆：\n平淡無奇的一天(茶','運勢★★★☆☆：\n戀愛運平平的一天，有許多接觸異性的機會，不過會顯得心不在焉，小心錯過良緣。(這下難辦了','運勢★★★☆☆：\n走路撿到500，但前面的同學發現是他的','運勢★★★☆☆：\n點珍奶發現，有加珍珠ㄟ','運勢★★★☆☆：\n買叉燒拉麵裡面有附叉燒']
    #2star
    two=['運勢★★☆☆☆：\n容易生氣的一天。與別人保持距離為佳，待在一起就易起爭執。','運勢★★☆☆☆：\n會遲到被老師罵','運勢★★☆☆☆：\n走路滑手機，不看路跌倒','運勢★★☆☆☆：\n騎機車違規被警察抓','運勢★★☆☆☆：\n走路遇到龍']
    #1star
    one=['運勢★☆☆☆☆：\n路上會遇到開瑪莎拉蒂的棒球隊找妳打球，妳當球','運勢★☆☆☆☆：走路拐到，翻船不打緊，旁邊的龍看到這滑稽又可愛的動作對你暈船了，\n','運勢★☆☆☆☆：\n會踩到狗屎，然後不會馬上發現，到宿舍聞到味道才發現',
    '運勢★☆☆☆☆：\n沒人愛自殺吧','運勢★☆☆☆☆：\n你今天在路上不會遇到好看的異性，Poor you!但抽到本格機率只有2%，此格為大反轉格，晚上你暗戀許久的那個同學會約你明天吃飯!\n實際運勢★★★★★★★★★★：恭喜你!祝幸福ღゝ◡╹)ノ♡','運勢★☆☆☆☆：\n運彩會輸']
    
    if mainL==10:
        return five[m1]
    elif mainL==9 or mainL==8:
        return four[m1]
    elif mainL==7 or mainL==6 or mainL==5 or mainL==4:
        return three[m1]
    elif mainL==2 or mainL==3:
        return two[m1]
    elif mainL==1:
        return one[m1]
    
    
#input文字庫
blueinput=['塔綠班','冥禁黨' ,'冥進黨' , '菜陰魂' , '蔡陰魂' , '假博士' , '1450' , '817' ,'反萊豬' , '不打高端' ,'重建藍天','中華民國不能亡','綠蛆','陰魂執政','台獨','覺青','綠營','蔡政府負責']
greeninput=['中共同路人' ,'藍腦' ,'689' ,'親共' ,'共匪' ,'萊豬' , '擁核' , '92共識' , '非韓不投' , '韓粉' ,'人一藍，腦就殘','你中共同路人','4個不同意，台灣更有力']
badwordinput=['三小','狗幹','沙小','啥小','幹','操','肏','fuck','nmsl','廢物','7414','爛','NMSL','Nmsl','姬芭','雞巴','雞八','雞掰','基八','基掰','死媽','北七','白癡','白痴']
sirsirinput=['看到妹子','有妹子','好正','卡','HDO','好大','腿腿','學姊','學姐','學妹','可愛','HSO','好瑟','瑟瑟','好色','好婆','我婆','色色']
gayinput=['胖學長','俊宏','幫他素','素懶','肛','屁眼','py','臭甲','臭申','申申','由由','gay','Gay','9ay']
fuyunginput=['我聽','你知道','妳知道','聽說']
nineinput=['天會黑，人會變，三分情，七分騙。','菸','江湖','兄弟','不離不棄','挨刀','滄桑','割線','甲K','呷K','甲k','呷k','鼠輩','猖狂','煙','帶刺','社會','義氣','渣','扛','道理']
wanginput=['優質','浪漫','約嗎','na','霸主','王希銘','8主','西米','唐','ㄩㄇ']
judyinput=['ju','JU','Ju']



#pic函式庫

def girl(n):
    s=['https://lh3.googleusercontent.com/XElYkiGNPAdudBMGo7ECdlZB-JWJIKFra3ho4qQQKzBVzOMVYJm3a_nueFUwWFB6AM1ijq1ZTHRNpALbPAn9GLnjbt6H4tugCeFr-R86b74iCA9OgopZ8yEHnsDUX2d7u_HAmfosd-t7ovaWHoNwIGJcB6TIvy4cb-coAbY4sZHTVaPuw-SKS9aypHNkuzfEcRyJqBcf0xYNTU7X2JpS9kXR3rVG8M_JT_OBIQs6EmG9PXY1ax3AfqIRoBgxndcI98MxJUhatULYOBr40P8ebmtK7S0mNOgSmcL4ID7L-NHrVY3bMJ02YrSKvjKgy-kEbapfmWABAH2KmOEnbtx74015kzI9cuI12Ul72Se6KCT2IdXS3GWpgfxztFQQo0csemgm5WfPWewhFG8bJV9jG0LtsVuftw33xhmIQLRP2_-X1BVboUCKJTv2uEVo1tzIROfz8FCyfegMhQ4UTyVA9KBtaHfaATWHXFhn0Q-BdRnnyetpaPv66iRSLvpIaohnnA5KEvieYEBir_rZQ7kjk3Obc4vkEJG2RPb36rdzCtJ0X9BO6JyfWeSClSxZWDW3SpSRfM_PQXgrnXkBKbDB1HDKVwZ8QyYAelEEt5SkRjsc4k10mrIfOwvNjEhtM0NyTv6QO2kp6qZvvrgWvRyA1WWtYdOtjtouVhJ9vLSoDm9f0onF7v2Xvd0RGnAvM3HNHTC1G67wLBL6esbQiwxMtxhQ3Q=w615-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/O4JpOeqlO506BCd7G1cuCwvETlk0rbkp1bVH_O6PizVEMosyJr0pc4SPw_cem8aHTv_alpSnNKrnX0_2FJE_-vIH9LpvNfTtdkZmSd1EuMJrBkgVpki62ecpHEXDzsJ7uDDkF5T5rexv8dEigKjN3e3xzXzg1aWuWFgS9tAA9HaKT3FrAxyf64kKZxvXeJ6c9WjY2_M0Ul7wOsNrlJo639dglW4bby6SfmBTscRVdRbOQCBL61ae2lhVNcDXCZIZM92cu6oxnxG-ZfcHwcuuC54yTShUFYBsFJR3Wh5LyoxefsgO6UolPXzuBOOIYN7V-5Zqjh03pRdY1AyN4mxzM3x2fyrWJjU36aI440A3V8qa_eENWdksRQJJ85F1cwDSdF7Q8aP8Rh_FGvoJM-G7XtJP3MOcqFU5dWX34-jOq2tIMcvt0-SI4cq8_Tb72mBxDT6TvuWhpJw_wG4DhyXJxegK4wvAniSq3WvFM9Gw2JryX1nuTgb8eFpoTNU2ZM1Ru9S58mPjtYtpl-sef0IM9SI8gTkX-VNv0SCzGk1ouotgRVWyWgbEpIwc7z_-a8hlzw6Bc_TiliDjhCNERUJpHLeL6wqqq_IsXgTER-TmDC4zkK44WUE0_v1aIwdm3v3Zm05zahyAa_osoo4o4l9Ol7KlJ3Q5JOVH7suYobaiM-WzLRm7sXFePwHI0r-rnsuguvuDqtbEW2NFRhCXTE7OMJGzIA=w723-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/v4icPOBpZ7Y1l9VL7I6eFx_tjKOzSf--ScDBZhm7oB63ychD6yD1yCUOrzi4phQwKB6fLAlHKPWKfFiPch_SpuTlDOOmrJ0Hk8qceEi6U__ZdZj-QVNYT0XjZ7mJY93WP3xWa5nh8QQWmi43lB9ftHlnkztxVsXqpC_bCFnOqwp1dVkuwngw_YPjdLSRADXmXl_9LpBRgIX5dufza0aV6r293h49DHlcnn8GenaYAPbKHdgvahq1DPsFK-mzUSzLyMhpMhqP5JD6HlCs9fmz0NaG2CuRjJpYKN1DI-MhS-tAKv0LvwUcADYeueMTk5e9y3rZ4R33f14F4Be2BoLuUJ5gaBsyZN_I8stRfhE5Xmip0ucVnOZcFbr1XMhPcvjTzYjT3TAgnLTYcG2H8rsNXoTZMsOByPuEpYSv-A6rwdRVHWvcIFmONpvAvvRW1qqihKxfNve4Ek2NgfzC_isPua687Tfmth05TkIpYENsz4HtMeTjuoW1EO6GdqtfOJzdJweMTJNI_fqkektc37Y4mJrvn_oohZPY0wnPHrGbuojJecjzr02jrH-mVvOxrUkuiSWHUCGMWFAj38SgnKzjlPydO9_JUs5kIhsnIEUD4sxqW23Cm5yDXzotLSlKREiTRUmXCMlB4pYJVdgmO2jyE_k_ZF4By2l5oYkWUC7efhHSkpUokKoxRHCUZMAD4HHSQRjxSB4yxx0Jsn8lN4jHZRPJYg=w640-h800-no?authuser=0',
    'https://lh3.googleusercontent.com/glV28RMnYbW1ayqskXL7SHUaPUVH5K1v-E3ADFRADspkB0XCUlAl6KU3MMfc2eWa4AWjtFSitiQwAPzzIGX1T1-ufiKaTVP4anEuqPUBcLcp5sn9OGDsjkes1H88bsGyuyapkZRxSV3jmHGJ1s8cWDcJJ-gQUXmmoU_i7qpSHmQ41GA7-0vWWMbQmMN7ElhuMTHW_6T9nkkBXmAVvb4q1bSq_y0UbeopU-HsHE-ozDVsqOoMZHKd4K8QrwbSgFw_Bwk5BpWtNDZAzLBVP1H-TkhnOd7Hx2Zjf-jsRaGhAoqqZrGksZNdmra4pym3iDKmMAJEoSQTcZau98-_JfxciC2BEPqUx8WyidF0_nZcg_P-cyOb23nQ6s80onShRRyuJ5hcXMI8rU0AywFnMz5J9kXf341FhNU7lRmBKsh1AeD9HmsZr1AQNRl4AsVL_HK65BNFnL6_BP6M0l3LjqRtpy_lWqpVUPV387Mvbp77Sw6zvTYbUikq_DGcP-Af9Pz9S9gkeqsdJAGJluytJehIA6JBC4YimgEolKATak7-aNRcMgj7eH7I7LBAAs-aImiDIzrTWf2ln3hsXdhdO1zxIuWQHokjHe9TD3ZH6P7dcyHkTXTnYSU4cdCXjCndU-bmOWREdc_pvHZSvWycyMH8Bxy931qJoopqUBG5U3Gt5hL3Np20_jJIdKSvj92UqcPim0PrkiP4j7X7jS3FGrb2fVa_lQ=w955-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/sTzdcXpTNCqQFv8Dh9peBSxqKye4TH7JKDvAw4vcZfYf-dAdDGlCpvYczlpLj5a77miIFwY0V2n5Fv_02lJE7rOD1lnWSuu-Idt0mIjjeVBlc727C6QxlgvxhThEYFBbeTWGrIjXqlwFYxu90xBLq_qPmu3VB0KbQuP8w9eHCayh31q4qA-lt_YVHgl2r2BJKqXXTJPxFDmvl0BCTYzNF_iqXqU57Xfej3iG30p9nIsfWpQacK9kMmV1IO7FBnYeeKxi-U06jmTV2U_ML71ugi-AkGzNaESVl2swsm7ya2VaBVZpBrckJ4MiHh-3aj9o8OdPas6T2ZXpWo1gdKRQtZfe3no4OPs5o36QlOe5lbleLl7r63MD_9djpt95Coot4_wxFWAvSD3TgsLi5Bu1jLT5smfTxrmAvcePKdgYdj7fu0mBj1yIGW8BhgDwP40MAMkC7faqEaudOuwfXN-hRyM3nc4t48WqjcgYcJf0KJf6nFp0r18Qz9TQhvLAfFKLsBBQ7YJULCL5QJiNzTPYTcRS2vo3jMsRBQVWgdiKxaCRYF161hPWMsikioLTvtzvitBVYWIRHaoc0P0Qj6oxNxy5xh265IsRoxL3DKZKTks0KRY6MO34uYOI2imxvNdq2pUL0tR-aKvpTRMfhyUHd4szruNdcDAXvd7hMdzYieLmoQVW5QwLmrm1Ls0FYR-OdASndRuNxqSOIVpvYspseUBiXw=w868-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/HfXqy8spxr-9zzyg6mJp0n1GcwTLgiwUj7CCl_D4B2jhQEn28QRnPnrbmJaYsqQ086i8Eu4Br9_I7UupQu9wFuNYvItorxBPbqFwby3Yfz0uytaQEbShnws5OYzglJ1cAcV8KBS1AYlX19Can5zINWI4ap_gq6zr7jW85MOVSE7UUe_2SmsVRXT3gXIDa8oictLWFfMP9wpleNKQCkmnhOvd1ZNHwWR659H46OInMxD_A7Z-xh-TWcXFekgu0U48kR9VrtchUzHqEIWkfIFz2MmksiXeWFPKo_gjOERWmlqgnLYO6eKcLKE7rYKoNpIti9UT7PsrilgswOCM7fQysBhugKTepBIrt-faItfIwRou5mqhD3fwqrq8jhb7kHO-9jo6G-cagPQ6jGl8d1G2hvDG6v6oGdvBOdDUHjeCPmXeBNmMx19h9MkQnoobHfZ00bSbiYVyeWM1yUhgR4TK7-JPzMGf5902EuErmWU_1J66EUTrG_dX6XOvC3qYL4fo1kAuoaXF18VSr8ciK3FS-PsIY0jyorc9G9AodL58c4QPylFgicvYq31nMgweMr-TtgyyM-OxTVmwRCAl9Tsj0wsZkxUkFct1rCfcIB0aUY2Ctt5B3VMfp-vbr6yYp9RFSB4AEkdEVgRJMRuxZHqHoiR_V5KLEddyatmi2NhBWk0IOiIITjBRuzlTfLNHh0kAXZMs2cz7e94sxGib915muAbmBg=w962-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/xIMXt3mP6pt86MKTmdoYBxWBQ-fxK5eMXodr1K6NqancDkgi-Qdtx7pBDArM6qhIswyMeTeYCKw5u9JJ8zeFPOaNwnEqY5zXU5pRbWOZ19FYVnCj7W2wf2AnRVp5CZRjHevyQMVxHa2sz9EOe42bAg0HRf0rIJwh1c6SF2IhGKt4zZs6T3UiYqqCocJHIpA5z5K6bAcOWgdQ71d3Ki8ACXz5mvMegYVxz_dxSDjOjBbTO6u8UNBA0bbvUYwM6VdzfRZs67Ybt6JY8yV22TTudgrkbnxpIvo1daL1t95stxuW29KPpUX-JfBWZ5FcOhFelnv4E9ySYp-Xbt9KdOZx9hVD8W7ZLsuEFHzg5v5HIk46ISxMdEkR_uDguD3GolTx6eb82Ouug55vTad4frqDwqmerL_SFqPD2B3d6L9F5F0yQ7zApOSZF16oEsdG8D52VPsJXW5Rx20ApozwU-VBr-Llk0_tPoGzBpu12Fzr5lgaFK5AFCof1uKYKQKoHLjU5IzGHFLbT9T7akMaZPf8waETGueuIIH6b78aB7vjoSD8M7bShF-0_bqXIEVSGVnOewQrazPolnDCUAzAsalefxdOtARyTWjdafWueGAA0GmrDQN2JWjxGtakBK5WucBTAqT5v1g5K9T8GcIRkEvR69gZP5kvFoYahvgwPHQPRX5sfb39XuaXiiJqI1p_-_qEBQzk9pPkv9xx_ozkRF62KP-nVg=w734-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/yBgdLup4p_Ca2TE6eLJ6YoWkN1fX24fIG5kkPu60SIEKOQNQUZqo9Knr17SWg_DLpw_V7z4_e00xNnVLcpwztjMsp4jrYjlqA5vsNTyJGp6pHhfiM-zvPGV3ch9-XF3oM0zPuVaXuIo54y8J_FdBRaAKcEGWAlarcxTijRm7fWkjhP77LOYqkvWoMzBbOpfvrlMqu0ApDI6sM3OP_-3SV-pViSVT5dyFV6bVP9LBZkRT6RAviwLW8fNtHwUUSU67UjJIUWD88te8y2MGMXNjcVno1UWSAaNO1E3rzdp0Zq7Sf60ChjAU1DK9bvc9en2IkJIUJYuALePlXT3Mic-UyCnw8KSpHJy3HcS9tV7OSKUeXKWNdK1gqumNbM61J77dYyDkwIIHWTLKphUQTkDUWOp6KdHNI184jN9_0VKrneS3wE7iXXxHqP5DjdteKZ8fzYlYtpPEYZw7YE_Ehh7bzSwf_dbVBD_Ac3XNoLi_j_wlCX8zyxXoFXnytlmJTZnNXY5l9a6dJ2RByvWjwmVJB4f2QAuvF3p_o_nVy_BqA8_kxQ7jrSpPVFCV57HZCK8LICHaDowKcdRxsVqLA58nDCfBZn6uHb1Yna1CzoiimE3Oi1wdCMGpJuuDd37CVHny97ReTnI0Adm6oAB5zRcQU4wJhFlhydcjG8MVNOU0FpbaBnijUCrNDGH3MlZR_IMMy4R1lTD-F-ygZvFm5Jx1IRfwBg=w805-h904-no?authuser=0',
    'https://lh3.googleusercontent.com/d55JI2ov4PFcpTQ8IL0p4ArhyFbulRbnjYnpu1hYddEQCTkEgjzC3q4dfL81eocS5YFY_P782A4FcAAKGADAtTK-7QBRUOx6mLmJnh52AhnBfzCYspQEzi8XLsUXQe-lgmjld5sY3jHskXUexYRI4V6zIKa7EJLN_X-mfBSSJNwyE8NRGNpSqNFtWhbQ_jWIc9DlbzAt9lv9i8EYKc2AG8-ejYU_HsTSNxs104HgeMfS64ux3EaveP_SXm0SyPxU8WAyAzY-ArrZU5K47aSt82J-N7p2ClQeNjZSaazSrUKv18yzh_SBL7aWKWIQZHQVLl2GpCrIfSHbNQtSC4KQg4a361YQ5bNgmKtukredkxGoxC7idMHo3VZaaQt3wTxlHakMO93CzuOl0sGFpBQ0kvaGxsQPKlFJdA3jI4C27fnYtWyPWoDhxCgEy-PH4FDdlr8aBXutPM6iVzx9GYss4R-5DGoq3yix1qMhnSt_cd-I9wIKKnxtfM7qMm8-cMeuQ50NFgz9n_45C7ej9IL4r6oYgNPLtMtI2cMXBCCEZIxurS8-h_04TLMOxHUXXMChhDtyk1MIb3SHZ8iD7APUCLV2y4qilUqYLWZJUnfTurMCekebrPRuAmZDHYbWk-Q0zg41waNYSB4_a6-mrurTHKeLo9psOB00zG6Hp-p1DRcA7gNMzHBJ4Nl0nwqtKU0yUmigpzf0Rdr7ZVNL7l9Dpyysxg=w975-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/yHVJFpqNa-8bmEQxwaoOhGq3vUesa1-M4F7wgGEtZryHn66ddi7Z1w6oG3QeU_rMACIbQqdeijZl4QLZitxkH-LDU6oEkhsiOW_FIwgNvaz-kV0nw1ERg7q-5YHR0Z0JFNhaf2I9vbDbmYRkhpTzB_1G1THsZql6UBLqfuwCQsV_k673NWoAbgWA0682sViE8VVLrh4xnb-DzHlxMxByh8HjskCZYo4Y4NvbyNhv10uFay4zCBOH__fvto9XfSoM6JzwuO9IpKEg72jUEm0Q8iFlXRKo2GgcBQfDB59aQJXSkNISxWyE47WjiHniJFOO9-QAOqGgnUTMJCqMgwHKuVXY5vKL0lSXMLhXZKJzixi6nfO3aa_gJg34gMy3v_T0RLcF7Srt5fNo9Xx-IYf_FkPtc9Gv0G_M_oTeKIPqj7tGP9kQNtOzJZ2m195xqWlQ49XdwfuarGSkmJIL1N0xVDP0h1npBkPJafHZRxF5cWXFJnKJDwajbQR28sgcNSInzgQYIohQVInAYZ9n5pjUdzjxDn-VQEqwWeL4R8ubscO36mIYNtBK5ypAOVl2zY_MNAmG4DwE0PvTvEDpwChuB00Y8YXaqHWyhGtm5zfCjOvCpO94jtbhC4RDR-7-qBhUTiUd_mBRHZG77s5PC5ZOjXtc7n046y-JCXxRFCdlC8EeqKiVuPshQ1Qz_ffdB134h4tSDPPLD2QfYqsH4ALZh9_tug=w1080-h737-no?authuser=0',
    'https://lh3.googleusercontent.com/vLV67U087Cbdd1wf8FugeAtauc0DW3rqq9H6JvjHkoJp5cXTIICwZHVTOn8wKV5YuETDkTFNP_GQ_Aj7DX6-LzFUmghW7PupkKBQy9iTEEXUe1mX9So9DPbfN3-h7xIcqN5Smt6lJkvvRm7rMgfn47cVIuMBPFltpbUV8Fe0o2_YIAtry3ds6iIVf_5J2HWiqPxL8ZhLB5nS6ohGqXJODiwQFcO0OFto7wMsMzPYtJPcOj0_6JxqVeAV_YnPQhSXmBBS0LbnPjwK_aABCwtWLu0rGYI7MMS7GrR3C-Hr4wZ5E0LULFBITC-Bz1c_19TfOOqtOyors3wFzVZYbIH0g7Ts04_UF1YjvIT48oSZTfaLQ9NW68Nad7xdJsy95JNgy5I6wl5c5hRe655Zw2tMRK_SuhnOwa-HyJTZZ9G3oJkLyGFqsLNJcRgZPWHeDdxJMme8cuW3Papw4PmCBGJrnaS7x77oShPFbfn5E_EwWKkhnhoShuNubWdDxbdeld03Owa3OdPS3ZSw1tHyxqK4Zq0PNhfz2z_EehmKQrr8nnmTFm1Fn85_3DeIiTeFvpmunBUrCLkvf9Bqhrg9S0FJK09ncfeRVJYm82oKEKnizvJHRpK6eHGm1bwcg5uXALa0nru6Er6-KlhiNsvWnzkg1GsK-SfkuqJG1UgG_0vDpzSLqISAqK9D66C6fa6fkgEyyxuSwZRsezknVH0V-AixHot7VQ=w823-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/0L6B2oMcwY8vDSvyJlE-lF8bb5v3lFq4GPwlmbMUnRB9r-FvrEGd-JWajFO1llH5noPRntwAi5AzU4O2bpjfhLzxYbU6L_8fvI2Q8iP_evUCdVBouO4DA_uGPDo0tOHaLE9NWjx1M_XAkIUccMWSencuyPIrEZERAKqmvXdJredU_x_e1oYCD0TCAY8QkaTcne_1Uu3QbsLAdmNSC3U4FQcmh2Fxow4jrT1daDwdUhmHScqwfUzZ1u7EfyyPxpNST0DG9YMsYFlFlBBX8pkjehV8etqfq1ypxN0_OVRYVMLkDOufUYB0zVO7kl1J_r3jRcqLCvNMVUjXmX96BXMdgYESOh_0gigO5bMJ2xdQ5OYFINeVUWoodJpuuzhX5HCb74hboGGKMuUqLhWEFP2LBWQRCOgCRUKH0RrBJ4mC9IRg4KfZAh-FXSrezu2p6i5Q9ltLdELtZztBlB-U-C9RcngCEqPRenKn3GUmbOlS9xvkUERMwpdr6rj8MA-ZGXOUG9HqmwwDKxXb890ka9JyrZvslL8vDxf9ERUBKc01oenQ2TzxzmFq5WQ1W6GT1hfW7hZnHSafZjzfedJv-NZ1SLAx2OKx-YsrQbcNFhKGWCq6ISjOMqNpGVufrNPJNmnjJNhYRFB1xWwCkN-7VaEOYhccTQgePaI4kUD66hBATkQ6n2KxsuPBdO5LHhm31rcECUfvMlk7C3CV9WUcc3FnlURZmA=w825-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/qwHXvqojJMCKglndscAVQ_ZMM1PEaS0_c3pm3fVwGLBXNkGvV98hLxovGUouwcnRPBMUCISUPkZNLChBt_RNj7AZ9xVBgmtRI1rPfYALk1AXUsiE6jBnVXCtA0TByGMxUwK4fMz7eyA0xH1rOmcIiLPzdXmEA9Wq1jIhpjVGpD_a2ipFPZsfo4CySSgsZCz1KXHEvuc-i3Cw8hr7iyghjAdufnnQZtpyYlUta7U7IJ2PmN6f0dp_-S7cQBfT3UiDeTTIKhj7AwZrBX8juVCJ_tnyHZ1Dm-2HblflWVBAiJYdgbGfZUtG_Q3ojfIMcClVaodEcmF6MxmGysBXzl-sCcGBGkmk_tVqElvlfKv5-FfQxwrf7fchV1vR3XVw1z_axUJRyBBUH6To65-Pnqz4N1B9MBeyDAcsT77ZBKL1Fee22lc_h2CZWbjG08CC6C2GS3QIuVXs6Y_wN0QjfpnCogP7qYHIbAloLf_fxUuHFulPIimbGax0kUHC14nsGkR7X3PxspJUbtkzKswumQ_B_UDPrneOIIhlEUrVsaJ7E-ATb1j7VkElxB3fGLa-2TibWnavl3v_x1cxXtyQkBx12yvse4ppnYtaWD2rh1ZsggP5gYf7K1LpjS14rVYvQk_lCe99O7b0Q2A7plLnzdmqpDYRtnVJkosszhHhRvz7-sEApI7dQ3WTIGJDjL0KLOnmRYzBfNKdfHXJtmiauJVkwy1_7g=w993-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/g-VO7VHTbxaDE-wtAc-SJwKZP8IDYOCuMdoKiK6XFgLMYDnOvDY-XH6TV0E1pnFQXAakd6HakFah1Lgac_5ebpol1yhcx6Pu-X9Lri2IbsMYpLHnkIKRWpTx6c9uFM9pRpMCgDaXXva-rvwqrwuAv6OrpGxWdv54K1bXrXVb_h27BQ_yQqN35n5KiPvZpj8IN4Kjkav_-kZ7486ZmZz5mBs6Z7YttzBqA7QAWt3Sp0izpKPFpMC5IGax6opFxbg0Imd38jXW9d9ACJfGmcoOaGzYZXz1r1b8UgkDMeIw3_77a7VLAoUurHfZ-iuNTdhHsxhVyJkGcfa2EJXdcaoJxZSc1X4ZzZ9PbheQ2qhnnAJuSp4lVt4zj4-8uXcayRGB1yTAC69790U02AeN_HlELmozeqYT6mEChQyM5M23lRppYkWsBQZPJsBHyXaNh8UFvMFd5iaedhjz7U1TothE3OQiXrIDF6BTJwePrLqWuN-5krjR4oGMHMReT-wT6fRv8UA8O0vspi3KLl4_v_L48QhGiaKK5PRHHq-fYCRCM-cI74B6lb84CKkvFXpt0M-7AUc9HCoPqd6ukJGwPZ878tmYbT7Q6VSnfvtfuG3zEEMz9lfrsi3WSkAXn1OqnNUuPPobZ9TkX7eaQUOwbGyI7oDreHpyec-vHKmly6JOzH4thCizArVC7hBa7HXMPiznb6hJV7_2rllexwv0TEml3EGnXA=w782-h904-no?authuser=0',
    'https://lh3.googleusercontent.com/6htnhg68wZIAIFcRM4x1TF2lccMSh7JAkrtxHr_pM7Zivz12zYA0gPrutpMfyB2ZLZ870F-giRuZswnZvb2P4Ep29ap-Pzn11UYBU4vVc2br8-URhNQ9j6sUV_sodA3ED7r2B2j-Se7nJ7e04rvM9QO0n_zTlvyjnfIZQ2q9rTmiwanw0Sqcdbl0b3dV4LIVxsNjLhG8gf4bf8ObKqILyrcrliE0XJ-TAPZq3fMUdNNt0gT3FuYgicvEfkNN0Dors8Ak3V7A87zdfBLEyvUOz7B-t-iEjhqa6Ar7tT4AZf3Vdt2xwKX_QILJ9dvbfqQvdaIG7nayID29PC4A_n58Cab3YjQ2l9uY83Cn3gejvAY8afdIx_AfMBvDiWiH-0lvJz_u5VzocLoyxT16W0WaQx2n9PshYupF-FmcyMmMHTaKL4bV_DKvvUiVtP3-BE-GRjYqwjxedOg91Dnhe-R9jtcj5NcIb1uUUOejV6IECr5_VmIBhJY2oRkRVfzq9ojHojMQ7UFJedrulh6ml6CXL2RYzAprUCt3LACejqZp7eOMIINnC3BNcdLXEo3e0D8pFPwHa2TEBUPvWt-0Ijx4ZPr1Krc472XqivAyl47T7djbg2LAGVAlOROek4PFERBeQJMQbGgZqiTQko_4VsZGoJScBmbFk9Ywe1WdyCGfnw5ngVi5I7h42Rv8b9t5vtWzU9-VHpJQ1QwGeKBx6_aETdon5Q=w1034-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/TCxgs74222ciOUe767RPxFsTIE2CyrbT4nwVuuoEugexanocDDjBDpSSzqemKdNclzCx8h_4V73i-HJFJ8yzu3Dlzh1-77jZUOrTc_q8fKU2gba9RlM34AZy0oi8kwqyo1xfpBu3rNezDTpmBxg3nPW5FdiN4pDjGXLJyn_s0-vawb5YRppnV9_fm0C4XMLul-NzdBXjcViahfmL75PQzP59V9jv01B-oMgAqnO063Abas-hW7KEDroAXQNZpnPY588j77h3iFi0xjGpRdfYABkb8SS7YzJD8D5NN8WtXVdSkJcVivGDcY13fIVq5-dTZheH0EZpYSIfaEeD_ei9CWoTKUbg9NZxa-yonwOsppYntbpiC8spBLDROPfk1gDqN-jpkoY5UlGd47e7n818PpXmrGt2Lj-ImoeoZB8OFVWLC5LRJL3JLMC9OmZAA8AHHI8EeQLH95tWxtJYRIvSo5kJ9gCza_YJo2iDqm0KKtp3hrWD9VUKm0v8dMKqfKbLDXXi17dA_84KsJ80tf8kPsYG1liUnJUSrqqkgQmNWN1kY__IZZPrvXwg5UaljU8bGCHvWwVhHUMsh6QlJkIv_aHcecjodc4xRonxdNtleUanndPQhqDl3-PEVj6cdMrR8Rss4uSSChODWsXiPJuDYZKAuLRd5uf19BeSwY7jW7Phomf5Rl0UjY65_XReuN1-9G0nV8nkUuSpLsgg00oJxpEURg=w748-h680-no?authuser=0',
    'https://lh3.googleusercontent.com/nE2W0jgHIi5fcW04Mvqxu8__MHxhHoZrmSLy_5x9SBF5KIDB3_JUXSGNYZx1k0XhzwDeqLKkdBxSBEUzUWGIlEJ44qvS5TsI6Gq8FeURyVV_63YJqeDUSsCFkAIo4UpMoyBUD9ZkTb9Js3u3UcODn7T7Gms9QxYXjQRupURUfokI9wp0iVkOh39m4fpYWsfeJqD8exT4u0DclJu1FPyc2bAUprvTgj2JlIry87ssc_GzcU5YFcowOJAnKfmHSZn69qslNdRj0SKkg_kBLd5kRtLjCzLGMJWTDsdaKuhbvxOQpfMeeWuAUJGEXhJCoCncqu2-6_IGzdPoWZgbe9_6EwVmF1wTJaTS0hd3HXeAVII4Aehli8qDVvEMtIq6llP44is3YayrJzRcc2ZFNgNNbnvMYXWlyTRXzhtyQTwDcN9znaU_YCnfvsufsjqKKi3w42iR2R8OHlLwFuhFX0CTgGXnEBMmJEPzzIEtAn6PnOT2ZaGWKmP-5yGKSY17G2z1qgO95Y1qYOu6CSrGmuGarNOjz6SIBNDQQjKHdegXOstHRYkQuO4Q-QDrLAXihwkZbthXVo8QihgKGSoNb9JsG-frklGlrCUTFdAIycpe_XiKCq7yVvINv6nOtZZzqRbUhhpmfVq6NyHUx7Xzcf52z52d1vOrWrxDl8GKf8H4AurVS9B_JyB7t5bYPWkfWrSaOK-Vg8kbIU9P1IrkgVi4vGVFGA=w804-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/9PvO2adLuAq1J4peNlZufl7G9eDsu3FGZYEXJospLTpkSE13bnkt8KiBPj99fPGpzT2b6hxEtSWiEikdt3yHusb_6-aBTLtH3BpvXA-6_a17t64TzUazyHzzxmoxIzbLlUdtLDtz_SVPVo9mqgwhNOjGjPOT7y2nJ2EVsdZTbh9CE4LldPmlQMZ9MomN57W0Fx56rETt6JSxtmX4bsEyikFZjD6IE-7ITN-H2RmNfMNyZqrgApN5OB8PKfQ-pvu8qs1UMCV3bgc5ArOF1mj7tHUQxCperZsfbugK_SXHz7xRhwp-UGnLFzUSOiB3BcJABWPy1zGoqKTxga_iQrVHDBLSq4M53pMwmJGCIoIW5cqvRxcD_XxMO2FFaPvlELvmEWyJXggfsGj-F6Icn2ZgdbT6_z1bYqIcD24Z_B0NA6Yc9oCRVK9ERqyq3fdEOEPP2s9QEapRmNa5eMh-XVgYzMEHKUqknlRT7I0fY8WM1vWEyKxmmyZ4qqx9x_ZCQU6xektUfCeiyn7dmmMpzmakZrar4C90U2K9Qz_TA0gLhGfNaIuWd7YR_nDaIpBhY3Ly8DeNF8IjFO6jc1F8ljZtN2IFhJLLnLbM8s0EBEF9Qrx-fwEHlWdjLta6RJMEionbjkqZi_NBTmmTlY-tHPaXzrxy1EZMt19dWgBkljPLJ2a6u-a-XpR8L2kYVY1_Op-5gUx_PeLPFiucAZoqWKqGb5G-sA=w1024-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/tUUFM6qePuNH4Bww3T9uR1_Hfq9RyeigVZvSfAbW5ZwrJuML49WfvdpzMQ5K-zLrAVdW2EJG2OpZb35akZPO-06emxTKNjS6pcS9STbXoMFcQ-fbuQQvgAR3S01VfLfcsWMslxTzZiuCgRQZATAKxHagO7rGsvRMMUV7UzEgca7UIqAQqGAVDBWwhQ8jBJkQYi3wU1dxq3kZcJEWit7m0CJrIqpPEGAZDJGgBgUYWGN_R6eZ76UBwkk0dYspdJzL1sq5ciOyB1YIlWPRBktSiTOhs8FAJqqG_IFdoWUuokmgvtHs8tIw8QMVX-J4acAKKI3nHM_fHnyj9b7ljluXYt7MKX0-CW2sKxl1PPs8eh04j9BmKRTYjShJisu6SJSzAgs54VgHdMpIt7uGzh0VuGD7G6IbjkLcGUKGkiRqFB2srrqxsQvoqzfO3-91DOeWXHbYE-BaCn58KNmsuOeGw4deHg9edodicfwKIgR2rOcdWgr-DOhv4ksHDG-1PeBQwjE0ABYly98_kTIGiM_PTPGw1BwbxD9Ibs7fpb9tPLKdMesvSnMwO9ZX2tIX4xQtfBT80K6gQAzNIrJFV6hhVXJewhzN-9kmuXy71msTarzCw1Aa1wqJNgjVQX6EymW0kTci975dvWVE9U-KKMO1TLh_3-oZPDBVwdBkXf71LgfhEMZqOS49y_5ftDzvqJq7M92wU8padptJorJckSJzmXcbDQ=w665-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/zzbdY6YhWVJ7vHk83PGBBfzGGB58kl0rtlsalKw8WSV16FKAi4ZSnxJWg7Do-hNDjaZX6Dmi89PXAngBZBHDIT_lYxYq6n0ELhxh2VLFIsgmF-wqYuuifmtdnE6BChNIUjAaxOpn2HCvntU8NAO2BwFRyWIW_yr5n7f-vKP21ecNfRI3n3bUyDF6pUs3z1ocacVp1y-KV2Di7A8pdDdwQyf0759Wj0pGhIW9h770Zu-alEWPWe2J2wcWyWzDugG0UCAl70Uk83Ty1tq3eCiz7csSiuD-XN86Nif3PynN2io2y16_qQYa6xiv8u9fXo7U6utLUMBjwpiizbFchvKXPRLcquHAVqVMNVoRdxoYkeyQ8dJMissjBT7q6ttVPBt-ouUHeimt93AL4GfmOhe1fwBAmtmlKpOZuOQYTutIlBJoyBdgMh4fe9PVQwM00BdPsXPRDUBhrRtCIPtVWmovPffVOQmYofVyb1zA2IUTUq48NTGIT_kMzQjECydb95iNN8aSMwXImVxYP8JrXxmsclx4tb9J8BDEo8X0D3bIT_-IEYxgSOZhTlWa4klWea9oWlliL_ff3ujy-G8_LO3Las0fiG4_hShwy41Y_Qa3w-XMFmDhh4hMYYGwAPyOrMBQ_LHd3UpwqWla6NoajesJBPpTxBvNXwkoo8c9QgfvDqSdEY14NgkB2djMm6lAtxcn99sCDZ5HDxvYvzR1puPhhmw5Jw=w644-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/FdV-06gM_eoyVzclquLixYQTo9Ei2WouIFT_vYqoIrkyj2SskH5VnMG9B3r8C6pTe9sSqVq3XTnd0_Bqhc88LiAfF_8agaYcfZpTrbNDUC484oJ_fZ11kaNwrKzX1wyToclqSTf5IkryY3dM6U7iZaygXfxIhOrHNxrM7zyN1FcUiEbAvpstl4m1bXmVBH9hoD-xS85oP1kPQFzA8Zds70hs1ABl156tB_ZX-ZQzh3hdub6H28vw7slccaMjovOCmXMOzpjyvcPeZG7LSfgILqRrCLloIxo5mO1FVudrqHZNk239tZyo9pMGnAfoy5xEkukHGtziOhXSea0RPOYkuY9MQUjPO8TNne8i1N1ryCT1UbkGTHSvkYSIudHMsYBP1LZyPSXb-Ph9qq5mxMOLIfQFfzd7KjcmGpafkyXdaBYv7p4aknysA3R0tNN4s7pLpPcobe1vrM1Ytud0eFu39xPoUwuIaWamUftdAHHY6FmW6ho2n6DdpJsmBG_aczF5G-LM8rgpzcwZnTbtRxWj3FQTssu-qHvzXqks1hPiGBPWAyhyPzavPsUVk2zKhBXCvow2XzJ4RHxwxSm2W0pRbsd9_O35Lpr1GmcDGWsaqsrT6OlgStgeT5PtwuF-OFR33e1xzeCqpzQDNiYizEGvt9bvv4G3m7b_Pq2uadD0J0xGPcoXIOhJoJ93VtqonUDJeOyThUxfBe9Qo7YwidXgzVYy_A=w1080-h887-no?authuser=0',
    'https://lh3.googleusercontent.com/OZQKrXZnlNdp8w2LE0SgK28OAI-4-xn2KwQYx8l6fYGXpzqS73CS9f56PQyQq0sjzMM2LFMAu9kjskVeR0tJfs9jI4XnR-S4KZ-Z-5lcMi-BDxNrnSrlMzfq7IDvPenjaZHipy0d2RqZOMRZVDcSCduXz8qdbo0NMkJVJQqwGIac0UpubsNNnBXDXB_d1xvvxK2kQvrF47HadAAQPSZgiJSUw2CTbYcJnWdlbQSxSeNy-pWVo4j9aejQCHuuB_EkiMZ2J2wKOAHIK2duSUfFVm4zoUADdSBVnxuJtoJTIi8446Jbz1g0WOodlleIJnkQvw4P409ZqC83W-mGLC5UKq6DkiTSpp1zgS-LsrdE5GaXZD1wdfUaYImIP2njwrXCyUX2sPbVD9rMJMLfq94VZoPf4W4i7JfGrCAzSHN3rfleA35NEYuz0k46yy4WxCpjCnfQTS-VWly4iupxeN1AkBUqYgfOjL7kzv-2e0CvzRiv2J-KYTKK6PLMS8K_yrkVTifjvZzZ5kmhNchKvR4Uuao-6DDnejT8PxKWwhHx__R6_pWvsRLAMlsS87wBRYsAB3dBWIyDqGsW4tuC4pEscLU4kh5QLdXdUs6yMBXE1E_2seGQl_4sZOUh2y6fQOEEIuqvz5wLk3QhPjM157NgDJmuZHXgXml6HUGR72xEfxk2i04bJBKGN-3LJ3215-bQRKMyb-39GeuA_DmJUfx5KduPvg=w944-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/dk-iPBKrniu-d3RfGOrLEivzIMEu3kpMwLYDdkf7gkB2dK5SLYAZGdlEgoYAy6N56JoNWJZt4Mrt0A6mUg-AlPf713PYAkSHQb5WANFDJ0DF_v_X1Va2pWlHD_PWUhIZ9Lxj4MHC_kZKdknmkihN9q928Os2e0eos2lxEArFi_G-QTbKWOiAYG69N_YzeoXjPSSx4OIlfcHX9cqEvJNa2yCJMbsJe3JU1LHs1sY0OsbW6l8m89UciufrDQW0zHZJIm4cdCkTMG0UtStPZa2BP_m0bRkUX6GH1OFnurFXzDNMM0SBDGLtOnphjuvEVZGIK_HAoINiJuLYIhJFdyIB4HrqUow1WMnuMH9VR4s4zmQxY5Du22jKDKHXemY0LDZrlu3safqqAzaAwFU9iTqCQs3BYqYzGVgrSnX51BK5h2EtQfFlISCvsVwTHUyfcR6pzTN-370OpZ_c0i1W2WzWciw9x9MKrSBpFuWlY5jJHkjfwJKcJjlNrLT8Rv1_nJ0Rs7FhBwQp6q-I3ExgcrButdMi2NJiAqfN-JY5YNxxtUAO4dPaZqeTNliW-kU-8YtZ6XMR0Fip-YLzthRTp7eWr5NiV1pZ-r_VQHSDuRIW7LRGHjVo4QtN2EduHzK0YIP4p695YiVfdpaghRC3hSPba_pcDtdSxjGLoBNNfybCjgXABVK9ZAqcTLNNF_Jgb5pdgysxfZvqk8JXgbVS-0nbif5Fhg=w1080-h804-no?authuser=0',
    'https://lh3.googleusercontent.com/5AZY1L2hYrqB-AiJsL5BgjNVVckIHn7tD5lZrUt6Sv_jmK5jJH8Uk3W9i5O2deJt45AToIzIPLHIISwM2SnycLC0NQVqcFZHEQRKO01IODPwUPTCn4f8F3ups7tDoE0M36Xvd_48sf9iuHb2o0ul-Q-djToUx9ErADtIYdb1MtmzvfpYTHjaO91JQmB9h_-WNCwp08H7IAS9CJ_p19ICno8Wkx8Tq-tlqX-WgXEm-E0FsGxpdwObljB9g_-LXpbPYejVREPkMUYwRsgf8oRH1aVuYct3jYvVgi0JiwtXwRM2iQYhZW4YnP2fT8H0KNKvZb54uafhaAntBJ-mJ1ejXoX7QTVAhmBeWKOt-HQi9M3r2th7pW5DZYLRqaDhudtNkRAeWuecL6uRB6HyBrurIQtjpLCX9haFEZbaI-g0tN96RetjPGjNWnnlq1pXeqC5Lyxfn0L9nEZtIemKMVHlbap5fcSo-yoTEtX1sKquPnNNrSd_dnF_8---lPL04MBNIL7C-CmKzhVf8aAWR2Nw6F-i_R7bUJSSf8we8HZ4gkK-o2bF_CF2cxas01EICV6ms4qQO4Bhvu20GStTSJgz5vmp2y_b0kz3EUvULzswC5C3h9aoBLuHdgRw1GUW1cz2RbCoajX0jNEvWaoMdnoiU9UiNPkA_dVZyjxvico-ppgkiteaE9Vb8tmOO7hFaMdItb7vEWEuIKXTXWY_QhSWzI7TKQ=w800-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/X9W_qx6TJHQ_XcDZYeAHK55CgkcrkHk0XqH7CG8C2pFYXkRy4VfGwMMrMii_WTzdaHvpDWz0Kt5HpBF8Dy4tqKVXAc-IA6wxFUXWekNnKGHNj8DtxiYXp3wF90TZaboDKzOYmzrNd332PRO752Cg0r-gSc8o-zqjc5VNtLVZF7cF9UM1Ah96_Gok_WXiNJlPoQw_OmcUykob4QxzjMLGXekuNVZ3nFAueDhb2FOOBfPTTjNxTA2Sl0U0sFEhuGyKcDfx2uEk5TGBH9Nnqs80fw9cJFLLcGI1Ly8mCpWuP6GnKBQqrgxcJprD5_uKW8j8kLsdemcyf3sq64EeYm3ccCswO_97eElC0mIaJDD6nxYoG6Mt1D4sRRgwvTA3ETS9XibqiJDgiqOpMAdJpspgZPodEPPmClSmhYhaa8iO_I2peMFPL_LlVY_OszE-bgRakRwxTfJriG6jKfudmQbBcESpNZsTrCZRpVzl6Jwg1wSEaVVhWdWi_RDuuGJZfk-SUtCFP4mJ3UxpQfnclzF-abnFaZewzskJsQQXPoUNAdtxYAGNh1chLXkIHsJ2h6rJmtbX-0eyS2X_1s7pPBYq7hhXv7M6LzMQPkww77V1ixuuDcZFKR2ZQlpbSoxKlQQNVImr5ulo7BqxsBm5DpWJjzUaTQijpz3CFJPGR5PzJz7Avtw21SOUPxHbkRvndMVv8rSI_Jy4sSAHLDM0xwieN9gWLQ=w804-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/E5-U5DAp12f5iuNPY8aYrD55RQ_B0QFrqQRiFn20nudEc4ei-ra-a5LTbButuf0zsc0Bhi_d5ovxQ2rWabhb9CYZrjJ78FVTj8HD6WMGO2fJ-_dKAC54kvazFPNd2eKXvmcHNnurjOrzZEBh4kpGxYHFtYRIIdunJnESfGTZGL3fRs_1yOD7s0FkC9YO2vI2Bp8nu2Twq5CJFFeYU3topsdP0CwiFWJbdwimFpVq2X_qc0Ie7Yx-Ipd2weraJ4d9wk0Bz1Gv6fWrRu1-Kb2Sno3-M-YagpFankhjUe6CYC5-ge_92QrDZazVkBI5fqX8PIme3GkFr1yISN6c5p76HNv75o4Ucb86LHZFK33MYJz-oBcDcoi42oowr6RaEEKJY44mbG5siq95hclYLddgydIxDzpjFV4OOC1G21vR-CpjlED8h1-BEWCfUV5sbFWaW_tjr1YkBPjSJbdzoTtclg1sVky8isbGVWYEqD1Se7nJVXLyr_QEn_aAQhSRz13VahrjOV9gXD9o_zdR2SNDo3LOI62jKKy5-xO1etasv3ZO0sJpvkkhvIAVte0Va4doIm7v_l73kyqMD9t967fLn_-KWcKbkPQ7ar5i5fzU1O6q6TLW0hJObVGSWIt6HoLBcH2LaxzM248PUf49wP7ffz8mEeZ7Pug2xvHnRdV_eWnTW80Ew-MgKOjmmYn5B1lDDrrW3l3AWgeRPxBHTm0Tu-bBzA=w744-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/Qx5qse0j7ShJxDKd4O2hPiaVPPFSDM6q6BYlI8lx2XatQHlSmrVG69JjBo0tC76hDg2jnWjxFemGVL9OZadOYPpDlyETOIPY6MBgjSy97bT0aiL9U3mXzVHHwk2mhvqSpiYK1Mvrnx113Hwlngd-1b7NOrUxH43b1fbGV301KW8E9eXBp1RtWUmU3OZ68GPsz4o_PCRSZjkCXOex6bJeEh3TBScHOPKXOigDXOfphYXTXtntOgAobl62z1V-StlbZ41aJ58hPd8MqRKy_Yei9N0fTU71Kcq6lfe6f2MikdUhFNQX5xj2uWCXu0orh_mfwdApf4HrePT7m2DI5QGxWKABH6Xkm1ZJA7YIz8UluAW_Y_qb6F9eS73smt1QP3URK7_6I4R0HcYJeiKFC34dxTiNCf0ZZz0Kuxt3KjnMXLTifSiaocJ8fM42Sw3yjx6bzMMQbudfTQaE6UUjyjeQZqWKPUtI3WZHfIyxBDcuBIHAG1eZFpKEFgt7zVpVnIBjXUv18iF44MZR45nf3W3eB2QryligIdZgcedlfLY6_GKRHPeuOIELK6XDPVQICueHRvFAH_kCmpva4cCPKOeLj__BxqrHDg53UQH6sUsmc0D_BAh0TdLZ_9RnWZ62xI7JZaHj3W1HaBA47NAvz1a6_inlmNsTQ_vE6sKI_YA7LpwchI6Som2HbrtFdNDALQ00sJyl1gIFabPHe_NfsHPcUPREMQ=w1030-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/q5ITUidC5aoq-Y9MFnj9Rl4DC8Nov3Dd9JJX6glBe9l0e5Kj5lUQZY3Nbszj66caZtZ9GxwUWlANYjxEVp0givIDHM9r4Od-V4liLAqEteqqNC976nsZlmOaOqRix2GmQaReYx-mRxjorNnki3SYNNqrTkpj1PjelitUrlfL4v6Vp3mCqTtaCNmzMtb65jyKkYEf9vKy5EdhuzjUh1CexzKCYgzYAo05BQ3JbdGBxL7_pwjvyfKckc2fqMq0rC0rWdDtzwGbEdyVxfnOSWWJK14ybaudzpx2ScUlG9gFVRoJ1WR_H9SsfyVM12bu7127Vlpp-P4OZPWDr_1szo5PPEvIJEritwL6NZcCWoA4GwqMGMbD61MWBJwgap1yelgHIHIuP91xUuwvQ3eLLbULD0nF5-i-03L3TcQYbnnLynxVPTtcBps1iMl8zqdCR_o31nNPo8Pb0bFnZPqBcOHx5VxxVAjMkv78MGoG7Q8RZZgOpUskYsAMjZi1F5WMuitMazwUvYdTWhAt1aquL6YeS7pPpoe9b227T2rBOo_2lVIvuywN_FBTxMJQ1Tz0-R1dXc5vPF4wT4I72dSlkv1-ZLr5jqGIghl7vh2mrthIh2emx1Eo1OyWaPnkCWmorgR9_yukwPDxs_csRJhU2rpwh7KsORnYzwMnWS7k_N30Q6xfD6PcbOncpOXqtTesViiCL1yzMJyOc3slvjweG_tgQ9IE8w=w739-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/Auvu2Q1tT3hwZ_YyV1qBd5ZjuPoE_oLepvhJ9Jf2jHN6JCijEDsFFdmaBlj0jiczyKwFG4YqDCmT3GXZt-lEZNVgMSQRCDmmE8D4hh87XzFWyJ0R5rmuR48xOK_SFMPw2OWCUtJp7sttV0QaEOv846qbP0Ikw0_ZJ7tzq9-DYWvAT7VVJaVLDn1CooKbHR2jIk-YIpAzJpgCFHdSSkNVySuE8FXuueij3zYWsS_T6vgiu0IEOFcemjVDNCOR2NwRmm2i7MYLCm8u6NZOtDbYy5oCgVYmhgCjBjPcsqEPnRVAgxE635HpK8_VwR8ABEisoJpx98isZ1tF1b3TKQcgl_A2WhXxT9y4-smUxqS1BTqLQtzuDrzGJkPJGgWC1kez6DONgCWj3dblw_4beXT3cOX-1FsCzimq9BPTrNkCofSWPYHVvaArZl_HyeH4pQi2lp6-qVnmu7ZVcqLvQZ7haweXk1KguX9IM_PNsd1zj4oCSTB2_oGu4Zo4hO01wGW1U7DcINdPEl3JhWu07tqWgD6krPoRh_MwwO-gKkfe5adsFHQ7w_huhISzUa7XN2dvZJE4aKg8raRudeipfCf8WDdBWElSk1P79cmBYsJl0f1FiYZW9fyy8b9yCsfamAGTIgVHagtgCx-EyM3qOR2Bw2Y1qtmgrMX7pc6qpW5aFFyyoJtgN2yWTaKQR2quB8KZpvG6qBtEbCtB-PDwOoUqTsM5vw=w928-h835-no?authuser=0',
    'https://lh3.googleusercontent.com/FYqlnvss3qSVp1WQcI1uftETb09TMUVe21mpnHQvxY9TaA8c2JTegoRHB1eK-gX3RajrsSwmF8cSlacsuW2Jbf3iL3IRUrLyeyao4C7Ai0FApbN-UjLD4wyG4Y60d3y0PApOWUr3GXSd8kbaaUzH5pi81Thry2-KkKD0Ob-pbvxyeqhEKD34BJQA6Xuku0_nh_Bx4AaxEdaooDKmejOTf2XXIUKmdzH05dkUxDhHaftYh41nTrwaYWJ8HyZbnQe6DjsunR0lqZF1rB-5L4z1wG9AsN7inMwVhKkrHWG4dHNp8ngnMsWR0W_5e_10g-jRWXkFWr1998GiZEBY9bvmk_ag0bLkI9m6iCRsb13_g04OTiv-mHDzPLB84vwF40P6xle-UJadJRT21suV1UK0l6yGuFB-FZW7cHkybH8Dluo5sXmI9cikvUDSwXkDB1r3rCHb1lCwzqJdDBi_He3J2GHKsKbjNrd8nr6zHcO8ZW4pOk214OAmd4uOEgsQmSTIF-XJr1V3kdFXoym5ab-VIbuZZsDRpCc4V_y9srPGLvrMyRQGSmdz2mT9KX7RRD48DW-e6kfzULsR3thJVVU6fyOZdFioDpp0x6ZIRgLHZDWqlwvWS0SA0VXPpIGA-vU3DPRcKAlclKO0L9cKZm5_SDMZ-5bhFWb-PhnooMB_BdjzcDNz1o4g9neZWZ5WRtP1JhACrGqKXb-sN7FVO7OwTeKSEw=w664-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/VHNbbORWFdU65XtthnBh_wgCp7V6R6LjkqxMKXgexW9vOikT2oL25fqbbuNOybIHWOgOSQmeJ_woBKzDT1ksG-igSS5N0F4mH74R603gM4CCuXMO-ppJzZySOsZZ8hjkNJeF86RZSm0_cGToae2Qv9ooxrgjhnPA3unnAeFbsshtuD0jgcKwO0bajO44G4zLMz6xTmsU12dLPUKqx3d0TuM8uuHmKVhLqNpAkfr-7Y6J8vrf5xIeLAAOsw-bPbibAmLeaYM3bw2eCyE1g0hlzWfVkT_eqe-LHjbV1nZXfr4C7s6vItg8KUsAwlr0-CQbV7-a-vkckYLZDFHsciICLTLFAOmI6-xypG2Lw8QbbSKwIt93MawV46VfAl1_wKXs4z0NWChA4CLyhsC1oLzHugxwU0bwdmZkENgM0kFDddvgqgyxvQzU3sZcxDtyTj8Rlf1U67_xWzikCfkJ3wDbQygykSm7ViWnRDwuvOjXWrmxygWejuIOAbTDnJVn-7kbwfWxjByyTVJuJPy6lSP7Qc7XCOwWV-RGdj9aEz3Wij_8fnV-VOl_l2LmQ1S5Wn_QY5lFgZG8jBN8GfieSt93NtRMWyqNh9QQ9UPyRPQNFMTUZBmmL5ivpYlAkq7xk7GD5IEsPi-XNHQqRo_rQjzG0h9NHP7t35sLbfuLH7vlLhLq4D5u1dduvBMuOoon5gnxRos5oVf8tbj3KZcS5i2yzyj-Sw=w838-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/1NpGBMB7ouvO8RJEzFQE7NCteAhi_gT3Md4i5zg86SXa6KypchtLg_U4LkrHSOIWF90Ljzkhb0xqudrrnP8-ihkflkmj-o9npTIUHSiJ1FZywNytbSWbbmqlp0R34gdtOs3LejFB-O_17XeQ3ma5ORvZSRcGvPaEzz2L0iLcTJ2W4S6IVOuwbYOy67ZkttYbSMuJrfz68i1b1IrENBpNY78swSZMED6BljpDrpy3Hsf7R8Psm87Ek88_ZCvWArHCtYjAMRSJa9SBhYlOG_KmlU3hrsaohe6SxEWIOuPUzsvY1PkM58V4yEs0ODkZD2qZ09LOnh9a9lwgCjTvFHEYlp6nQLH-PCXIkmVF-0BYIx6bje0gXHKi2GI5MKqu34QWq78CoFWFO8JqkXtyFiivg3wry6c8B9D1xyBrO0dJzmNgIdIeGZxT7KaQvXzDxRPVF6UILMhqKb_Ql8B9BOivZjcZjUCVIXhhnHZD6PPsl_ALqKun9Ak4nWiJaDVRFLn757-5V2V8322rPVgADq9Cs-Yp5MYCVbbZX1be-NhADXJsreSoBLh0PpzgTLQSEwqYcpcbx0QJCIMtTYPt8K-c_K40NarY52iq-AA2qf-Q4_F14ZHPEBscBJxRV8BoSDl6ucKcwsyC7Nye_YHWWVGeLtv3XWnCfWssmtUmb-rv62oB_eRhZdtVmKoK2ihXou-9EPZAFitSCUovQ0Tzk7-yf0MCAw=w669-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/sUfLX4aRLC6a19AWRsMAN8VdSP0r-F1qdu7UMe4403oWnjYeV2_0_gpjgFDSsXP7oi5HcimEiELdaCRWS8AzR2jUtjtzc9J-uPm321aWh0paNm4ReNHBHW38DUYnxejxHwuI4Sk_31d9QWFPxyU73BA_y0LiufPA6n6jUptRhrJSXH8remdxG_Tv1muZjO6Xp39__LN7LHhikwCuPr3MwDu6hQRu_YLaGfH4DOzkcyH8eGWQUpTc5YvHiLIPkUh7jRTs1KIBqArGtQiFZkmh9vEnuTLRzgBiDrRWYPGw9n-u4RRC7NN4bsV-tuwlPqYK-35_9hMeCACysEhNp9plItqbmLXZwdJYuReodzj_takLWqOfnqv25sCcdc0s4W_pcnnmXNjbmLJVtV92n7dF7hPMbBDnvlFJtopO24G_P0VEo0fSBHtr7YVyvWnbHeQQIalP17Vi7YTISJO1qpgKMstkY6YA9ZuQg3zfWwr8lLvwVGkCpfv6SSGDELGgQ6sEb4SwjD4iK0zwLZOye7WTltOkhAthlGhjcJGkJ5QeYi8bGtz3kp-xOpn2vdpoWIyiOlzbAr-06k-VfcPj8l0co--_UxIqquCMBqU8wyEl9-W7KEzvzA_nPq6Z2lqYBN1Zc7yZOoWLEhuFlveRWZV1iDRIQGxvTSYKpspOKUQIt5vLzIz70hwV1Wcd2QtmHeYLhW2oC5r91pY0yNe8cmYie_3iBg=w1080-h855-no?authuser=0',
    'https://lh3.googleusercontent.com/WBQu-EnLq0vCAxiyigC44aAmxc5kHE4iBUH1Q_8HbodMhJHb9_YJd4cAClvcUISu_h31DNloQbbSaQo8ihyo-f_WQ5grncBHTNc7pNWv7zADQ3tENQkOJ4QTxvruRgW3eZgv1V_hPkTOA4WL4mwN5OLcZmnwU_Z_h9KSZkZkR5lEkQ2vrNnjDKvpCwJ3ulBHFnvRiTlXa3eymqGe6GIfgusTPgsJ2S2IGJj8osWPZ8NK-mMSjcYXTXCDYhkx88IBh1Q6InWcjZKNUaGHk4yVEGoyZ2i2bI4Pgoq76VIKZ3fqqKiVZvolTP8LKKobgGVryjNmfonhibkejgxveeJpE6Noijx5ubmJ-Vys549riyPM8qVP86qjp9S2zKgCxF0hSxWi04NEcGm0A3ez563HypdiD2TA5KDsRatwNa7t-2TkNp7lPJdZsDZf4elzoeUilu0qrNM6CopmmNRgR0kMdzH5rGKok0HJWO_QB8TTfswVozbFr9h8YUjIcTVxOjE3OF5B0fVhWnjKGzF4dWQWbpS6GIEq-l1cLZxfmzKhQ2PnFU2tlNuztlmIfvXmGSqmLjHu-9EO_Q71PQ21a7zC9-1bwGHxIvvXc6_XGWkkWKVXhQStK8-4BjxPUVrk1jvn11vFBjXmhZC0sbE5V8nHlx5H36V8Kacwm0nmVqtasVMqa5pH4cu6xkb42Q5W2Tz54tjN4MoFayKirqBFiPuc36zPSA=w734-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/YWlPaEi7ctS_GFrdBgRIDuSXb-8-TRJgyzEY-4rSkQPHD3NlM_ae3N5L6e3FoSPvYVhOY8Gm3P_mo-BeITdDalgTzR8SIF-KI1uXG3qVSxIRCNapMosTPsNZo3xqM3Q8enUyyDEIn55dZeBPw7uIweQlsn_iwLdc8TrYuacj5MQEIFLblBa9Lt38Nctm2tcCCkoRI3fAnobFICp3pwEY8FHG9dmGxyvbB8m75WJkU-m6Zb2PQzeFgxtAPoPWhUOxWy8IfRnatt_lYZSOJ8Ixz1JZfUismbb4pJWS4NxaZj3RVm7MgikahRypisJ8OvONPlF-XF9Jm_K72gh22HaBslOK7rUZgENaFdZkugSqkQ15h1IWyP-PdjGGqJzJC-6zOV6bmBxo7cszEPIqLlQZXNovPI2plY3-Z8ArL88SYclNRNwx-8Akp_2Y-IElryzUqyUW3OHTTAhQavWdvmtkJWqoFPYJx4h53Pwoi5gjGRVb_8zw72TWYIREehSibqkMPmjRiKyw4GyM6_7DfXrJT9k6P-b9wI0xtftjyKDd69Zmtuak7yZIFvpmaPYwBtileYfhRMYK9WVpN4-4TXfoSnblnR3t3lgmMNf3kOxcuWx89051r4Ynq0seryTrm5_NYZTaFjAIywH1q10VUzD38deAiVzAf8irjlVGmgj1-UemGO9YcRKUhaijvYQJa8NWQ8ubC0aW3Ix5AKs2hJXi92VoxA=w938-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/n-sQ40j3m9m7_olJZsdrmYs0YDHMfVRJyToAN2Wy-CW4JniCylZ6bAByJW3QqangGsYZO1nXvdc6eijJVvhID3yCleVtPXaEtzBZWjNGrlb1Rt5G_oFJqBTTCDHUi5K0xMsOQdV15KBscoUWx02vdG-7QdRUy7qIp7PPXfIJkEI1fJ_jJQVvbjz7CSVx3l17k5aIPkolT08aTfIQgSyYxmJFG5gWfvKkSVL-07D16dzKOPk0zN2sjFHEP0VAj5_g4vH5e0KfHh0Zz0xDf0oJIhkfUiyCQm4qmosp1TZ5spnGL21-s70PUkNmM4ag7faSrwvILIMeorUVqUjgagsUoqaBANw1fpbn_X2S7QVaPB9qYVODybRF_riMmLcvVuHyQvspcHQUwJOb-ALBBcNzdzlKp_0AwKKmna_MVxRXi-WC9MjEGtUTr4i_OF6hryuCV9p2swSzEx-bUnfEE50B7YDyTDJkZutq8Yv9_y86eTSqC2A4-dhQoy3U-zgyeZx0Hrc7HbLPkTDLD4sLnnRKOX4gTht6y9_VfubsXvUhOUmiKgzO-44--XNG4xSEvyKrS-S3iwFFkuIiKaEON0CPdz3uHHfQGVsEIeXrzTDiBJAtqzymG-OuIfbGtNaEo8Cke0RImXCWGkcVmstvymD817scfwxmUN3BqV8VUxWFizns7EynoYls7PYa__VK1HG8qpkNIUocYb_WkFYoY_68oXzDFQ=w833-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/Q1klWekMUuAV6oBgn1wfdcZh4fGyCIF3S8foNDUzGhTwXRgWRONqjQUBmBqKYryzukGBkKWFZ0nsm1JFVmQjn63U2pftN50-mG-9EKxfT2wX4cY6SUKPn_K5S5uT_mokd32sD7LGpUvMSDFp-7EqKnJmMB9b-KMoYSKzruv-fVCnh9-W1booWyr37fzcjFA66DGToIwNe76WM2jgbwnH1OP0CiJ6QJWV0Ask1Spg9ALFCj9QX1WXY-UJt2S-Qv8sWsBuvMmADB-ErlyzXqs8XgeLVw6fW2OzuxLUTL-bLATjdmKZ6rwMWWEHTYJuB8QNDRwgkHacJHWg93YwgE68p3TEtOm9ZET6m05xNij53E4EGhvR0uOuCZ36etsqWQxBCy9ZaB38z4c1hVJgnFiwpq8ZYo90cJJt8xqXIApfImaQiXUsFyx36My2iCP-cHmbma0uP7DOQ93eEDEXh_c9KYejbwGvisvr-1jQ0CbpR-HXXt_Lf3hdLuV5stQEoz8Wa03SanIiYpacvDD13u0Nn6DkPhMi8Ap5XoicDg6jCcOom2p8ktji8yv6WTswNcibtJTm9cSvXq6GBK2ZGUSxveG7XCR0S2qlLD74-S9I9-jzz8UhAfEiyG0JStz1FkPWdJzarZaogJeQAgaMa-9sYnToyiQ3i1PLRbCJgHTbh3qfR5lDulrIa9UgGRV926cKU2FKEzubmUSO7tlZsRCwS4dedA=w838-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLXsLPVAiGR7NiU_JNJg2FxgR7PeuV3n2GtRvoIkNYQW0N768JS9k2LsGIicwbf1ofUTW_gPxXA9rSdB1SXmuUuQ7PpsyeTUBqzx9u-oAO0LTPYqWNFkZUCog6YE1cvPQCg3gQ3E0ZSbbPgoMUYq5PKT3Q=w678-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLV7nLkxsocnZKNz379S0VyR67AXv34a53HJQNu2xH4JRWFc55CrFisOFpz6MDkil_knMx684rEmniTcTCkZZ7ltmoh7Kz6U1O54Xe3yAMqh0me1zTit5hhwt4AKIv-o-nG161Fo80iAWFM1Wu4CwOStVg=w960-h720-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLVFsP96FjyI3I1INkwpZincPJXkMd0TpvH5AZB0oI2XhGJ1AmSkyiKvZATZo1pr-ivpfVn-Qhy4UhXVhJjBXUzMvPY506aJvveic_uWn_LhaYPR6wixoU2n0GNobQXwpED5qwPOMnCjr0-HlDtyh01mvw=w847-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLUzqk-na0dxHzSd0OxCOcxb2RL1SE4YcM4Q41jYE-nPkoNeDBdwToMzz53S8eCYMquelu7EaxUb749OBdchlcW_MxAOz2y4wHj4jLpcAvR3A4mQN-vscFEPxs3Pt0SSVBQb_MEXMrn_PZR56EaUMj8XVQ=w789-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLXZU66kMiKbDrx7oJhn21pBzZ17ZZDNrKXZsBBn7ihODev7dHqUQXshl3BZlbNUnKNB7n21mAVPBwdX3x7pixhZd_h96KHYvk7qToeUEi0onlKEzH2dOk-gaeGBHoliGWoOYkOAMgqH5EwF7GkEjf8v-A=w749-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLUvW1n4eRE-o3UfkhGp2-ejC40MdO190HwFIYDwaOKihfLfjUGM-T8yiGxT11bnLsa81oN86yVi9qSFeZJ_kGjVcarxJFOKWlR2qL38NWOnu0RKxyqAvIAwt_mFFdeBFgDOFSUczDIrng7-R5AJk9ApyA=w852-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLXEbdHaez596v8t9x7gPb2pJgs1z_NATrhxcrkp1rQfuCE3PWY-i0B6fOUWqUtuNpe7P4LdKkH5kYUbFkRSCHu6dnAJdLd2gBLTaKqkclcJigJMqk5mXD3dtX0K2LOr64tD2J5cFERnqGkuv8DYnY-3mQ=w832-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLVdNDpv0yPgK3CqSMl3AK2cERdXfAWzQvJTGQwkiueBoCPRyNwzMTz3aXQGq79hcbnCCtKJtYMBliOY-TX-Eg1IFssf8PMmK64y8NJpI-OYFEzp2pu11c8SRfVwZKHKfdaU3nvkzB_wzwSdaCXzeNWlsw=s833-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLVwCNRBBoaTOIAfB2Q4sHBoPtdrbiaq7s3N-lBQ67z4sT0NUgU72BAl8VZ8tutoxTzBekd_bjCvUs7tcFxPAFqDz8aeNsTjroLroxyumUKeghKz5XsBVtrxGAJ9eg-1JRwkxWMcy9fnZH5XEu197MO9aQ=s833-no?authuser=0']
    return s[n]
def sirsiroutput(n):
    s=['https://lh3.googleusercontent.com/pw/AM-JKLXmD-5rKMPSOn1c5gJopMYxI2MVNQeH-9I79hZHk5KURSen-1NG1hb_3-D97788rPApzAJJxfxzK9RU1Sbl2DkHQz9qS_vyffnGSxyXrZPfcID9okozS2YgpJcszFuEIiFZno5Hbs8oEYXr1vToGCUSxA=w720-h602-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLX-eVUH6BUGlG-Mi-Sg_d0C8yra598e8qtXh7u53jrCviyFwIegPLHAmtmemBKwoWhPH6ek1u44lNuMbdieTWg7Xv9rlxIh81xOAsVf2G7nEU6RJ6ntdDMwRagzxqN5KdO-JTnDB2P4hvEMHQOQ3sWq_A=w1208-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLU6QPA2ccx2FH0n0I-6-li7S3xLL5L84hF2Fv91uSNUiuEF0F15LmK2sgOZMEyOCb9ebI6I4cjdwm-fWOo6TyPgBN5Xnx26fMJmTWkU02WGQoEANuowmNWuQIKsdxy2rvn1IitTmtYM3w-oy4hwN4UEKQ=s720-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLXQ59szWfzC-_nEy1vurS9mIGwwltfKDxg6hFaJDRiSuh38V0j03PesFhek2SppASbgK2MaNtQmlRCZUSnnHFZsy4AyFr_6xmkeBSQRdXcUbGd6gU4eUUhwbChSjjWS9vOOyO1wonJDXYk6iiNk6xirdA=w551-h310-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLVLFgHa4m6wNA3NXEY5Hj82arrdZ7inWk_VU2h1uKgzxryoSiiGY5iEBZovWKd7wMYf_d25db9tDScdzTS3DMN04D9yy-z2Nh475gkr6K-Tt1QzDfeb_Ipii_z02w8IdL_Xhcsx5QSxu_kYWI5ijhiYkg=w918-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLUe6rxtg8epfCc4CRlqpFaputwv61kYLVav6ac0bMRmxq5uaqQh-95RpVc-iGMvWhzfNdUFpGSB6O2ayh0tpJWLvSmHmfu3u56mzTUWjeip6IvVQeZtmkjb3JDLfXlJp4Wj7-eDAECOZFMLEKRme8ShzQ=w920-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLXo3XmKZ-TTh2VkNOGe5IcFRcqOpSEra1ZSigVy9U6GdiXvsTI59dmgP2pzdqsAGZ9ig9NG7z3IjRbqC9G0bfk6wVDooIgS9hE20FChE-V3ltyKrnMWcLdbBTNuz2NDnak96w5gWZlEOJRwAEy8AowkSw=w602-h599-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLWnv6NmTUXGlSNbTBoJ86P3vCMmQVG3yXwn9gB3d0_R-xyo4UdC6YvAhNRZAYZx3IOiHSU66PYELmZ1hPFYNimVy3FH8TXi7zENfPsJMBxVabINcXKzbXpH4nUgzUFiiOWeRLbyGWkPVZ-5rDUQRoJhvA=w1137-h640-no?authuser=0']
    return s[n]
def gayoutput(n):
    s=['https://lh3.googleusercontent.com/pw/AM-JKLXqESG-CSlDagp0d7e-sLt1kSIR_hhpbmLUIIMCU8BlTGpnlfGpbrsjRFv3Wg9eHnkUIgNpGwwiD-qdA2pp0NEpB657jsgFJT-Im1Z073O06Z7ywI2aKtm4gGM10NlQUWUFd42k6EomFUD5mzbxpYg0Vw=w720-h509-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLXAix4zpljYbbkkeJ81Q0xXPOqtSk-PGqk-vQkZRoB_cx34acKa8nvSPfGIULgTyY4VuC4rybZPk2oQA9_AHyS5vgvT5BoLpLXRPfaD-7OwS7Viv_3JGdGqwO27msWzMxKJfiw1FMB_uG6Hgb7gSjZ5fg=w394-h240-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLUTz3EWnp8g9fYoY6W67wG2KcZlRY9JU2bNSNyxkhdjgksQKMXpmdjto_FMxoWUQ0WClHkUSUJ6mzH25eNIVo2CljuPbi7cIwwmNfscl8WSFFtAYw-E9jebod3OMw2pX6KOTZ4YBGO9hp--YYFf3OyaHw=w418-h903-no?authuser=0',
    'https://lh3.googleusercontent.com/pw/AM-JKLWT3YJg1V7Y66p9Gt8_UZTAmZoS5g2zbJYnnfMscRst9bpzVGZ48jmUxn8tfUdkaIiJEKatKnS21yE30UnQMf2RHXMlDHUk9ne1ZLwiWAPXYFxUSkuwt8J0hc2Lh5ifr_5hK9EnDQ4iIE8SEUHeV7ISig=w470-h480-no?authuser=0'
    ]
    return s[n]
def girl2(n):
    s=['https://lh3.googleusercontent.com/pw/AM-JKLW_XA2srucj8GIzA78-4nJjvMnZ10swuH0di5mJtNA9shhk6r0PDQKXKBHeLmyrDB_rFNlI6HQZw0fl7Q7_toMANv9rXQ_SsmmNymDDZcnOopabnB2SsGzIFoKcj1ioGW0spwFf4KbTsB6r0XLz3Sf4iw=w623-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXYybA3NyODk0yE5JcEX76Y3ROi_sPtErxHKKj04hPv1zcT42MXR65NGCUvFOV26YscA5YlBVUhUsOknNB9wgQXBY1cng6sQzfaiwkjs3b15be9D9zVG0ZFWtxALd4eGp0YhKlE9UiaVVijkJJ5wwLYzg=w592-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVAuzD5rieFHlHcNALfT9KReThWNZT7HWW2uCVhMpI22R2SYl08-BPvN-LYcdShPx1xr06j4PHECL5uGB7zkNDOC6iYFSwYWDixCOZrUQcErvRPkhPRn6y7dy3oAgVCcs8VdAciB0L7x_uAWB-zVOrrxw=w618-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLWb7pKOvL1FfgX8r5gcXshUkxRlSB5GH5YjR3K-77eAEWqLQ-JAR3XXxSySvZ5w5an_WzNETz-MqnP69JrHhf92nEA1tCnvBCfPITEK9ImMiqBcMtMETKulZMZTQyehH_XO8ZiN3BT3pkCKjxFpNw_IXg=w734-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLWwsOD6V0HhbIltCM1cyWscMKaTPJwtePy3JJsBnzyXf7dQ8wZKqb7ASC_z6gXtHz36dem88EHFeafej1oGIHjkDZ0-05QUhGIFwmaHE9NtX9Qo-H-pYRPeLPblYG9O52gK90_4YVPnW09gWt4CiZfvSQ=w730-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUGnv7d4Z-QN2iQVKHEqQCOuv17GrR2lhhm9kFjwl3zWYXiJBIn7NM0SD-qvMkTWq_2Ik2gTZIl1TZpdhmPwyYR-zb6LJr-pElXCDKb_3T3C8bT0YYy2kjwWgIVT9HrVIG6kZazIjl3QKpUfvJTlDHZTg=w714-h904-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLWZUxyalJIzYHA7zGHBzNaObfkvdEw9vOtZv5Utoz-mNvbPTWFHOunXzdmFOqfsvhNHleGphYjpdObzkzNudNVwGAw8RMjI73vKYS38DvXuunBIdIPLO47gqOoFtSuQZa7rPNkTu9OXFTwQKPq0d-2qCg=w822-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVwWU71jnVqt3WAzq7R5_MashrGjRhDRUfiFxkjm64GV0feLw2bQqpSqtU32NnoV6R78Pyin2NK1TXMgR4kIgQgoCQ1m-1TITbOKJUup-gj_GzNs1jiFFgpqXvMcvEeTG_ax7JvZjPfVLR5lS5QwHa67Q=w737-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUesxVJSSrUaXscU_9GxGjFtlXGDeOKLDFmuVTecPoIceErhhkwhOYpJgWB1CrIHXQc_qS1ofwCAIT3eGbjuImX4z0DBB7_iTTQv_wOrnILn2QRH8QQA2NbT8NEJrCuGra_412azX4cyuG1SP9vxenliQ=w800-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLWWx_Pc27Cux5gd0Lv9jChi445AvUMpFuAE0643X58cwtIR3o8JeYK9PRquYBo5N1QWhyL6nbutFjSm9EKi83VZC1HytmzWEDoenzEPEtDyR7R43CgBqeRMC50VhR_rFZ-VDK2j-2Lcp9Gu5M_nLNO1_g=w669-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUMjE3zw9Cutkthxx8ZNM_IaNIj--KHFLCE6wVpI86TqdZ7ziED6XSWpIJZWeuDe-NnEPTauqHx0qCKdn146KXZTpMKTMmnvnT8rCdrOV40xZW33wdus2VF-71-iHO2VnQRFkH7GU6Gf12q0Hq1lbn3hg=w928-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLV6_ozoGL9qvB9eTjX9RQIZK-eGW9r8T5AOHvcbs7iP06sdLLBnauPHa2a9P5kL-C-sxTSpV9_W3D2Eb4JzdVG98Pe3eLaDbOVNfQZEq9WWUttQ5Nf5VxIdzNm0bfgYZ1SZ5UoXKFu5xyyOHCKrUKCOTw=w934-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVnP9FUd_roCevKxN6e66x7Blkky_Le9OQdm-mAzNbnqE50Mp1An-NR-vyoDhVVayTcGh1paSRdHQvmnrTXK4v7riwGT-gWTZnbFg8chmgwh7nvlZbYDDsRnUHfrU3ZNR_k7Ru2btSf4fRTDV9xMgkleg=w808-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLU0DTfl6ppCmHRE4ZqYuO3tXXDy8b4djyRutCrJFM7mpTicR2lUSWc-Ls7QN1R_XcpwY_OOYwBi-hsHNQBb5fsudnLcaWeRs83tBD3M01EpcnNFcuWB_8GqBQgDcHNCSfFocQ5kWfTV3kJ6NphvXkVZvA=w683-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVK2dbWyS2rgMP8lP4KRcO4Ne0SuazR4-K_S3E8pz6da6bOj9-9cwd8bOSuYpsIsVhMQbwmCnHiNfZgNM4LZwzuV6oPpj-G4RHVwaaF_yp2fGb57ZmEdpZKy0M4De68i3AHZwVJdOEXfFLsFMolU-ytVg=w713-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXaVrdRVXbJViI9HymLyCBUHoXu7v2s4BLoZpZqyeS6WepPensthAzJjKOD3YZwpbyAGUsiYvtR_u8ala0dM4ORKK1PkF9jqzG18te1pjC7dapTf0A7SAHMo0ewMJRT2ABuzufbht_kQDd_Xh__q9HdFw=w708-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXyluqnvbWAlURljSS6q315tIUK0kzSe5X_2iQMtm8cgCjFflb9eNuVyhuP02dRhlV-CeJUrYqj7y-u6R_dUQW4OV62w5b8CL6XFyBF173Zq52_PjVjMkJQhFI09H8qJvYwg0tAmnPB8TaLrA6BUmQuGw=w698-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXQ1vV80FZxuwSyDtlrzS5DjgiqhbQr2Zt6FpTKKwVeo1OWna0HNI-XjIL0xhnOiWLUozPr3olf5MyHEPp7sdlAl5HlI1D8vOeylFW1y8gqvjEaVxaBFMnbbtL5SM7Z2-uHykxy1mGva9Mh_rOToQK53Q=w697-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVRe45v4BL1QZu8DfId_de6CpjkgTLnvmSnbKSZrCVY9wkPooRrEEIcMwHaJk3HgH-otu7X3eGDkhddRFWTYyISZhGKlKFXnC30lmFQP6Of67O-lu2pk9IQZ8o_XY8ige7yyVDCPwC0Vne-yJq3uCk-5g=w674-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVvTMxVbs_9iPCnTxc1XdtWo3nVfsBuLZKnwBHwYptVIFIKziBE5N-CfQFv7uIz0AFZ0Kgc1VjnjViaPNEjd0rYquatqTkue5d-uD2cX8vog7XdsYmLYmAYIaca1WwiDYIbsyxWUvJufUs2CLylycg_EA=w683-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUuDfU-LkKf6tGRmhvz4aQvAfeHXQhzQHkrCRbUhSUty0mcBgcl7tcDLQ9OEixLep62QIeT8ArjSda4zECL1WgVAHfc0R7JLJyebV4HLiUVLKSfkcNUVN5htkPsEdCdmOxfXpjGNUua1baj5HrYLtaXkQ=w757-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXNrSeFO6eq_cRSE5jbIBe1AcGDTWLMFvsyH5nOJeLizjFUUG95-_ipYNYRyxY3NSRnNBef_OpAhdi37mE-G-TpzdKPVNEfZHInn_iMGgxiQbQvXnhLgFdCh2V_Q2NzzenRddLcVABtUXXdtxMXsPJsSg=w655-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLX1Kg-skFhadmvK_kl1sPayGeysCRMjdoJmICcyy-TTF9bXawJDRk2njUTFQNhRwVK_oQkQOudI3pv5-xHhOe-8AW76eXdKA_h85eJrb72UEJ0pWfAcpFgy63LvYKfqTKCaUdpPFhDRFT4_VQQIDKRDyA=w747-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLU9gQPUWVTAIDCip30CFBPlAaD6m166__ZOGOlgyiGa4sowx0O1O4oBy2JIhK3XpSV2hALjltHK1l-57ZzMQ4uaHpBh7rVYNHvqtNXhrerbwcxPDWEO3sJXZ8vZ17GmQYLLlkkGyX59JmI0IYGnO3ZCMA=w720-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLWDOWXnB-ugMwfgZRSitLPgMtkBlUxtXZRN8Tdjm1DcP3_p3BHUxlUZVNiyifDBYIkokiFFtSFV_qcTHDf0_p5VYiGrbgMRAeZ066ERIti-3IosQ6f_ewDRYo9pkdIXwgBwG12Rwla3qXKg8xT_5IxyvA=w682-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVqo84t0nOBzmaQeIcT_vl55xuI3NV7yb1PpCSpLu2ud1iT_pCTmMPU7rDeHWwHOiGCWsLiMREY3rjaVixeTYQjXQ73dp1dOxDACqksn1dRirzz8QavW46tMR-Xz_tuRCEaVq8ssU3Hzo4LTf42GxfFpQ=w634-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVmIBhPOf-Q3yUvzd-rm1Cw9FFP6sXPZeuDcw8nHqDXFd0gcSj_ERXzAoESqfRYKY74-H-LvdOwMcskuRd6Pp7bW0mDnsnaIUMVrnihBYVzCxnfQOvZK1hcLXnKsewDGHzHN1JhD33Ujfld1OCs3n0rIA=w702-h903-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLWfPOHz2i-WuCAp8P_TjeGq1bFXSRE31IycRDZKarsMJy3nL_jb_di3fwampX5cWlcdvxqyZ3PM9_HOQk6fv9ueK_ZQ5Jir0PpNAILw2CT0dRQtsFCV4Nbe1zeeVYsXwnT3oM5i_Y0s7Js5Tzvf9s8ehw=w1080-h620-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLUSKcZimgUAmEHhtcFY29e5LR2q9SNqomgOwppoArHozIpEgYFkLWQqU5PC5WF8G6gjvqbZWa-QjJEEEqU2flZ36tfVctgMJ1QhDu0I4_h_DbBMNUkI2_rYMEiQeE8npeiMNF0crJY1rmTlb0YxAVoYuQ=w687-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLXAxAgnPuTgpZX9WU-5b1ovc16uuXjx3HaWyBh-dX7ySHIlsKaNyOENnBX6XDjfDHGVifjqUeQWEOqPyBth4zsg2550O7H2V6ki6JJAkIzuKlCW4M5ciOly25Iozw96b1K5_00J4bzkSU5TS5KN5JVglA=w709-h904-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLXEhqRgaeKUA9x3XuvepwwFRztPrCeUMMYfbsfyBrsM86cUBYSNzj-tZ39QhNLjmnl79wobQipox4QLR1FqgB1kPcqtlZIcRjFQ9OCY2OaYIxefQMyia4PINuzMIl6D7OkCvE1-v1qCFB74MdgtryeLyA=w702-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLXck8XzJUo9Rj76AdWXr_xcOqldQaTr1JpD_qTpix7GzhP1Q8XoaBlt0Y1YiCqPpNWvI6viTBSWiow2Ql2foGVD3pv8kPIJd6nklvpMFsjBjma_TMSXm2qdoUgenzxbFOcU7O0f70JssoJnAbQaoELB8g=w677-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLVgT6bTLn-516W1ICKECqKJzkc3tmixikpHqSQJnjh72IFUWMFw7jqosW4D-Xf0P7M1X-EquMUM0OrpEppCus66YwQPfYlK2TYYK4JmWmH3wOZblZooL8kZfc62W2QSZtWG-KYcHZFiynxYBEywznxKZQ=w739-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLX06UUz3EFnZKydZzE-JDZN5Qgyx_F4jAc4Qsv8Z1G1BAnetB4ug-IjTua5s8Edio_GYWT5Y2MNCOjKI7Gx02zWe_9yPDAg1zNIKYJco3kQ9-kDK6VMVqAXjLVTzFz48noysyPAqIaqyTQjGTyaBdM4TQ=w837-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLWIqhRNkHjAH8q7HbliGnr6ETOoeLK3qwB-MTirv-20Z3ofX3StoE1Jlah-oNzGLYPCjHQgASMRVZe6slzzo397uhfp0ItsBhwnRRZ1m0804G_Dbs-1TCzmW-siMfOvpZhyyuh36BYpd-kK9QbcYyjpLg=w688-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLWO8cprW-GLWp3-u9QqM1zwRoaRyoDlZ-sJvDwpPXNmn8sRKDHaNPnHRys1v7f5jfxTB8IE4IA-BurmK3Ife1zBPICQ-Z3qU6-L8lDBF-QtU87PIZ73cmM1rRByjRLjlQSAw-smHW6l-HsAOQK2Em9hbQ=w800-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLVPGrOE5VJoqwBkrt7fRpYHw5dZetw9iddRTwgJ0_kwtNmCcykaVSkyDlBR6szFFtjUCXPJvLQcChS9oou9No_uShQN6FhbNBwpaqql8St3XKq73zGT2ubAAPy-EzrLVV7zjK_MrZMvS8w6yvFJM83zXQ=w709-h904-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLVHpKT4sUEktBlpQDPruDiEGnyg8xhQ32i7oQ_DLcvfcwdPazc6bRICAFRwOfoqXPkkaBA1fAybDj1A6cbwOMmvg94g5woC-8GRk-aMGanwOFLR53aNJl-gqixcoAyGMqGo1ZXZr7f3vslf2aAALQv8ZQ=w793-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLUyNI-0A83qJb3QXX59onyo4hlbrCDjgYCOL7B_AsI1mhklzcJ-1bi6-7joD_imG4yDq2wBb8vPbpPwuqQUbpUpLyHQXAyJaz1EbpPUrYi9_pKfD8YF-BsLWfduFmD1MsVYOSNsLowpLEBmeL1kYWan2Q=w1080-h587-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLW3B5ylINBDwfjTRWPmbglDd7uH5_AIL9awQxhR6VwWaPdzMPfIMzIj4J-gmEQkAhRAeAhBF5JGO_F962kAIm9t3LZdWwi9GDbwB7OUo3ekHl7ecDKrJ7l4wspKjtuWgoVrpsTgSXRnCEaq2-2BJLIBGg=w744-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLXPsk4H1UaEWIW1H4cKcFS92eMn8TFKzA9gFCUQ-7dy5J1SJYlFKpJhIj0DLCGEX3wgltTcuffgzJpmDmbDlvpvD2VyVFmtw_fPyuKo6vF2m4s5w7vT2onXmvBukLiuTn_Qyn5-YqLNhcDTMO8PLA7ElA=w702-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLVHhv-1OXnpbmsC0lYQDThcfdGHIUySNJndeZMWSdZ9KEPEaURR9ZMaX4vrvye4DL8WkLXMr6V4-6I7mNKdwYnvQdoiAqsdyNVKQocrxj_lZzgctlMa-0NTO252-he7Bc1hE-4ZiIUhugefjXUN8LiD2Q=w683-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLXnizkQFXxk0aZftTsUMyAqJPjaYObo5_Ed5BFPM4XGQBnziPBRVvQL1PSj_xCmGHXDOOkowa5k4CYvbrrUM_SVinyf5hCarpAyQ9XgyjygFAsbl7mab-aDT_hzPt1oY6XZsLc3XhXj1H70fr8BR9ccuw=w715-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLXa7SVskIAWeZK0v95X5cG9PO6UQyqyl6DIKICv3ng328muUqod6UwlhByR3F4eCJSwRVkSS12RA06ct9S2V5C9DuU6coNwXisV-vWOCDRQyeHYfv_yBLG_zemN8AO1ByVj7yaoETCrSyGN1BThe4TXsw=w675-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLVfa4P2PYokkG-Z7vGbWCT2Nl9PHz9cmALaZiDF430QYtWdqq8qpuKxwtJ78ssMHhRaOpmbtgXVMj9irlBCrCsBJdZYzspAWFk5xtj0lmb6EQ07NMRB7iVqfyJaoowhorrsAUIXbcqTBVagN5pRIilvmw=w1047-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLVTIgzX53jMZ-8B_L8_BBfMwAT5ryOU8i-Ap-7g_nhx9czqurdd7y4RW5-X4WRtWP3pYwvtX6uIG_1rpSh4B6nO2p-_Q58dCNnC24X6s0Qsktq8K9UzSLDs4e2i0rwRXTy5ywEXiaPOT_Ym1qOYdmSfpQ=w987-h903-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLVTshNaXvXD80FUJzyKT25Hwpl-RHsl1c9qaQXgNFTHQrtK5QdDvJO2NC-uzIMwnTbMrkT0rV-Xd4pQtfTsmxCxdp4g5efzKXVVpm7tl-WGPR9vPUmYVePAX0XES7UBiTmTD8E0D6aFxOGxppUXGp89ng=w722-h903-no?authuser=0'
         
            ]
    return s[n]


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '愛你' in msg:
        message = TextSendMessage(text='我也愛你❤️')
        line_bot_api.reply_message(event.reply_token, message)
    elif '拿優惠' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '測試4000' in msg:
        message = image_carousel_message1()
        line_bot_api.reply_message(event.reply_token, message)
    elif '對不起' in msg:
        message = ImageSendMessage(
        original_content_url='https://lh3.googleusercontent.com/pw/AM-JKLXXjtgGNlZtllIjjo_bAPB0AwlMibjulNp3FwQZWTuu5KyNgJGFnIbjf0feEYKBy9TjP0MgyX0ml11A7PVHjvYWcXcVKaSLvpi0RphieidSfWj4004FJsD0GyfydXlkT2g9QnB0jrUI3G_MJA57-xHaJQ=w554-h413-no?authuser=0',
        preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLXXjtgGNlZtllIjjo_bAPB0AwlMibjulNp3FwQZWTuu5KyNgJGFnIbjf0feEYKBy9TjP0MgyX0ml11A7PVHjvYWcXcVKaSLvpi0RphieidSfWj4004FJsD0GyfydXlkT2g9QnB0jrUI3G_MJA57-xHaJQ=w554-h413-no?authuser=0'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '我是乞丐' in msg:
        message = ImageSendMessage(
        original_content_url='https://lh3.googleusercontent.com/pw/AM-JKLV0Jc00d-2zECLFVxRlo8UcPWk8fAuJ9-mbKFDn0HRe0BNSiQ6BBQGx4hBmVRWSXu3NBnfYXlrZZxccBXiM2e8MqLRz23WhcxM2fkegaKA3DfGL4dQZIvL1xJB6BDkqCn7jcim2Iu8fEAgBWVEx2rMxsg=w668-h833-no?authuser=0',
        preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLV0Jc00d-2zECLFVxRlo8UcPWk8fAuJ9-mbKFDn0HRe0BNSiQ6BBQGx4hBmVRWSXu3NBnfYXlrZZxccBXiM2e8MqLRz23WhcxM2fkegaKA3DfGL4dQZIvL1xJB6BDkqCn7jcim2Iu8fEAgBWVEx2rMxsg=w668-h833-no?authuser=0'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '亮燁跳繩' in msg:
        message = VideoSendMessage(
        original_content_url='https://i.imgur.com/0Heh20f.mp4',
        preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLUauLJcbZcoqMRSEvH0R11V-7MiG6b69-FBajaqNRa6t784oBspCCIWMCMtvqBEoD3IRO6BFbn0SXf9JjqWQ2cq5D95wgaOgGWwmQSTPdx4pHl9AzHlO3zwqNUmHLoh9cn2mj9KmOJoy_3XlgFSh2Auug=s903-no?authuser=0'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '愛愛' in msg:
        message = TextSendMessage(text='要愛愛要愛愛，哥哥我要你的愛')
        line_bot_api.reply_message(event.reply_token, message)
    elif '爛機器人' in msg:
        uid = event.source.user_id
        gid = event.source.group_id
        profile = line_bot_api.get_group_member_profile(gid, uid)
        name = profile.display_name
        message = TextSendMessage(text=f'幹你娘{name}你也爛人')
        line_bot_api.reply_message(event.reply_token, message)
    elif '怎麼了' in msg:
        message = TextSendMessage(text='沒事啦 不用擔心我 愛你💕')
        line_bot_api.reply_message(event.reply_token, message)
    elif '早安' in msg:
        message = TextSendMessage(text='早安寶❤️')
        line_bot_api.reply_message(event.reply_token, message)
    elif '午安' in msg:
        message = TextSendMessage(text='吃了ㄇ(歪頭')
        line_bot_api.reply_message(event.reply_token, message)
    elif '晚安' in msg:
        message = TextSendMessage(text='晚安安 要夢到我喔💕')
        line_bot_api.reply_message(event.reply_token, message)
    elif '謝謝' in msg:
        message = TextSendMessage(text='不客氣❤️')
        line_bot_api.reply_message(event.reply_token, message)
    elif '吃啥' in msg:
        message = TextSendMessage(text='跟你一起吃不管甚麼都好吃阿')
        line_bot_api.reply_message(event.reply_token, message)
    elif '嗨' in msg:
        message = TextSendMessage(text='怎麼了 想我了嗎')
        line_bot_api.reply_message(event.reply_token, message)
    elif '你又答錯了' in msg:
        message = TextSendMessage(text='https://photos.google.com/share/AF1QipNlZw_zbE-VgIBxs3qccAVLF9uGDSEaCHiykyOVV7JCdmj262hAtIKmEcvx3B2wDA/photo/AF1QipNnHA6HQtQK4jz5eApCAH_XyTBBBU1qGin-Mp6i?key=RUZ6WkNMN2loMGFVdW9IczRtMkJORzBZX0ZodFp3')
        line_bot_api.reply_message(event.reply_token, message)
    elif '測顏值' in msg:
        message = TextSendMessage(text='https://www.beautyscoretest.com/zht/?fbclid=IwAR2VMJJQX8FMhMeSapYSwRzBAxtMRTwB-kIPlUuvZ2OFgzE6Rs5tVAl4VDQ')
        line_bot_api.reply_message(event.reply_token, message)
    elif '欸欸' in msg:
        message = TextSendMessage(text='怎麼了 想我了嗎')
        line_bot_api.reply_message(event.reply_token, message)
    elif '喔喔' in msg:
        message = TextSendMessage(text='不要應付我 人家要森氣氣了😡')
        line_bot_api.reply_message(event.reply_token, message)
    elif '哈囉' in msg:
        message = TextSendMessage(text='怎麼了 想我了嗎')
        line_bot_api.reply_message(event.reply_token, message)
    elif '想你' in msg:
        message = TextSendMessage(text='想我囉，我也想你寶寶💕')
        line_bot_api.reply_message(event.reply_token, message)
    elif '在幹嘛' in msg:
        message = TextSendMessage(text='在想你 寶寶❤️')
        line_bot_api.reply_message(event.reply_token, message)
    elif '在嗎' in msg:
        message = TextSendMessage(text='你要的時候 我都在')
        line_bot_api.reply_message(event.reply_token, message)
    elif '不要這樣' in msg:
        message = TextSendMessage(text='那你下次不能再壞壞囉')
        line_bot_api.reply_message(event.reply_token, message)
    elif '拜託' in msg:
        message = TextSendMessage(text='好啦 就這一次喔')
        line_bot_api.reply_message(event.reply_token, message)
    elif '乖' in msg:
        message = TextSendMessage(text='哼😡 哄人家啦')
        line_bot_api.reply_message(event.reply_token, message)
    elif '我沒有' in msg:
        message = TextSendMessage(text='真的沒有嘛?🤔')
        line_bot_api.reply_message(event.reply_token, message)
    elif '笑話' in msg:
        m=random.randint(0, 47)
        message=TextSendMessage(text=joke(m))
        line_bot_api.reply_message(event.reply_token, message)
    elif '今日運勢' in msg:#群組才能用
        uid = event.source.user_id
        gid = event.source.group_id
        profile = line_bot_api.get_group_member_profile(gid, uid)
        name = profile.display_name
        
        
        message=TextSendMessage(text=name+"\n,你今天的"+luck())    
        line_bot_api.reply_message(event.reply_token, message)
    elif '林襄' in msg:
        message = TextSendMessage(text='怎麼提到我了 又想我了嗎🤣 我也想你了寶寶😘')
        line_bot_api.reply_message(event.reply_token, message)
    elif '還好嗎' in msg:
        message = TextSendMessage(text='還好有你關心我😘 愛你')
        line_bot_api.reply_message(event.reply_token, message)
    elif '我錯了' in msg:
        message = TextSendMessage(text='你沒有錯啦寶')
        line_bot_api.reply_message(event.reply_token, message)
    elif '不理我' in msg:
        message = TextSendMessage(text='怎麼了 襄襄來了啦')
        line_bot_api.reply_message(event.reply_token, message)
    elif '去死' in msg:
        message = ImageSendMessage(
        original_content_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t1.6435-9/241981683_262634809051131_3772204662357956548_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=e3f864&_nc_ohc=zUmbW3-ThZ4AX967svk&_nc_ht=scontent.ftpe2-2.fna&oh=dfe77f09ebec236e3da1b46433ba0196&oe=61A63EE4',
        preview_image_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t1.6435-9/241981683_262634809051131_3772204662357956548_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=e3f864&_nc_ohc=zUmbW3-ThZ4AX967svk&_nc_ht=scontent.ftpe2-2.fna&oh=dfe77f09ebec236e3da1b46433ba0196&oe=61A63EE4'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '對不起' in msg:
        message = ImageSendMessage(
        original_content_url='https://lh3.googleusercontent.com/pw/AM-JKLXXjtgGNlZtllIjjo_bAPB0AwlMibjulNp3FwQZWTuu5KyNgJGFnIbjf0feEYKBy9TjP0MgyX0ml11A7PVHjvYWcXcVKaSLvpi0RphieidSfWj4004FJsD0GyfydXlkT2g9QnB0jrUI3G_MJA57-xHaJQ=w554-h413-no?authuser=0',
        preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLXXjtgGNlZtllIjjo_bAPB0AwlMibjulNp3FwQZWTuu5KyNgJGFnIbjf0feEYKBy9TjP0MgyX0ml11A7PVHjvYWcXcVKaSLvpi0RphieidSfWj4004FJsD0GyfydXlkT2g9QnB0jrUI3G_MJA57-xHaJQ=w554-h413-no?authuser=0'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '生日快樂' in msg:
        message = ImageSendMessage(
        original_content_url='https://lh3.googleusercontent.com/pw/AM-JKLXpHUOnc00ZPS2_TNpP32EMr9o1pU1MZatNpCA58XrbNThVAcAfErnPL_Gr9_bVbIp9gGvw4usQk-juWZIoq0_VDChFs9Sx9GU7S3lgBMvWyv4btNHe86IJPecILf71C6Rv9ctfRCUNJH3pqZu-kOuHkA=w960-h612-no?authuser=0',
        preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLXpHUOnc00ZPS2_TNpP32EMr9o1pU1MZatNpCA58XrbNThVAcAfErnPL_Gr9_bVbIp9gGvw4usQk-juWZIoq0_VDChFs9Sx9GU7S3lgBMvWyv4btNHe86IJPecILf71C6Rv9ctfRCUNJH3pqZu-kOuHkA=w960-h612-no?authuser=0'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '幹你娘' in msg:
        message = ImageSendMessage(
        original_content_url='https://lh3.googleusercontent.com/pw/AM-JKLWBuFGv81z0AKsdUgv168Yzn1QaQJx1wLJW7bwhFJ48r1vX0N1T9gmAbQ8Zj9SIba8WumH93AzH0A770aVvaNtgS0sAv2gl3lpuUEZC3DqvZ8DBhbPqK0TMLEWemG1M3s-zK5l8nrhqmgBds0nHZpk6kg=w960-h721-no?authuser=0',
        preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLWBuFGv81z0AKsdUgv168Yzn1QaQJx1wLJW7bwhFJ48r1vX0N1T9gmAbQ8Zj9SIba8WumH93AzH0A770aVvaNtgS0sAv2gl3lpuUEZC3DqvZ8DBhbPqK0TMLEWemG1M3s-zK5l8nrhqmgBds0nHZpk6kg=w960-h721-no?authuser=0'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '中國' in msg:
        message = ImageSendMessage(
        original_content_url='https://lh3.googleusercontent.com/pw/AM-JKLWNL3GR4OJpmzK3lnhQyePKFpH2wnJOBishbHdA0d1kI34MoH2n6TbgaaU4H1Gae_qlyY5swcHqQW81ODJvDUkUSBCcVHSx2u-lBaCIt6O7QZ2TufB7xg4658SL-t-lEyG4YaqNSC0g3mh7723pA4iIPQ=w462-h280-no?authuser=0',
        preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLWNL3GR4OJpmzK3lnhQyePKFpH2wnJOBishbHdA0d1kI34MoH2n6TbgaaU4H1Gae_qlyY5swcHqQW81ODJvDUkUSBCcVHSx2u-lBaCIt6O7QZ2TufB7xg4658SL-t-lEyG4YaqNSC0g3mh7723pA4iIPQ=w462-h280-no?authuser=0'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '上次' in msg:
        message = ImageSendMessage(
        original_content_url='https://lh3.googleusercontent.com/pw/AM-JKLXVzu2yi5q3pt2ZZQ2AgGsJaI-17cMSd75xK158rL9lzz3EVuqmdl926RpTvgs9gs1FXH30BJ3_HnMdPjb0BzBQQiArh_wJ23H9Yym_wFfMjeG8rww1TDTdud5ZekuMAIfMASy_Zl9OEsiwNtkb3V1-vA=w468-h288-no?authuser=0',
        preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLXVzu2yi5q3pt2ZZQ2AgGsJaI-17cMSd75xK158rL9lzz3EVuqmdl926RpTvgs9gs1FXH30BJ3_HnMdPjb0BzBQQiArh_wJ23H9Yym_wFfMjeG8rww1TDTdud5ZekuMAIfMASy_Zl9OEsiwNtkb3V1-vA=w468-h288-no?authuser=0'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '要不要' in msg:
        message = ImageSendMessage(
        original_content_url='https://lh3.googleusercontent.com/pw/AM-JKLVLS8XZVfONGWdiw7WfJs-JwO2Iclgs0NiuANoi0-o9KdYGqqv5RpVEhmbqQhJ_kRKd9Oel1Cg_k-uKtIaKoLfwcpnj4Kr_r3iJ-YJ5D7kbKJ2E1bbKSVC57xNM2G8r6XLMsBclJVB4J0pTRnL0m-VKPA=w530-h240-no?authuser=0',
        preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLVLS8XZVfONGWdiw7WfJs-JwO2Iclgs0NiuANoi0-o9KdYGqqv5RpVEhmbqQhJ_kRKd9Oel1Cg_k-uKtIaKoLfwcpnj4Kr_r3iJ-YJ5D7kbKJ2E1bbKSVC57xNM2G8r6XLMsBclJVB4J0pTRnL0m-VKPA=w530-h240-no?authuser=0'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '跟我講話' in msg:
        message = VideoSendMessage(
        original_content_url='https://youtu.be/9r3ZJIdcaa0',
        preview_image_url='https://i.imgur.com/L2fBXZx.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '講話啊' in msg:
        message = TextSendMessage(text='哼')
        line_bot_api.reply_message(event.reply_token, message)
    elif '張瀚文' in msg:
        message = TextSendMessage(text='不要吵他拉 現在在我旁邊睡著了 有事我幫你轉傳')
        line_bot_api.reply_message(event.reply_token, message)
    elif '柏廷' in msg:
        message = TextSendMessage(text='容許我這麼說你這個K3')
        line_bot_api.reply_message(event.reply_token, message)
    elif '垃圾' in msg:
        message = TextSendMessage(text='你喔?')
        line_bot_api.reply_message(event.reply_token, message)
    elif '你會幹嘛' in msg:
        message = TextSendMessage(text='我會幹你涼')
        line_bot_api.reply_message(event.reply_token, message)
    elif '亮ya' in msg:
        message = TextSendMessage(text='容許我這麼說你這個2486的k3邪氣小孩')
        line_bot_api.reply_message(event.reply_token, message)
    elif '哲麟' in msg:
        message = TextSendMessage(text='啥邪氣小孩')
        line_bot_api.reply_message(event.reply_token, message)
    elif '期安' in msg:
        message = TextSendMessage(text='被狗幹的2486')
        line_bot_api.reply_message(event.reply_token, message)
    elif '嘉大' in msg:
        message = TextSendMessage(text='實屬牛啤👍👍🤙🤙🤙')
        line_bot_api.reply_message(event.reply_token, message)
    elif '笑死' in msg:
        message = TextSendMessage(text='哈哈哈')
        line_bot_api.reply_message(event.reply_token, message)
    elif '閉嘴' in msg:
        message = TextSendMessage(text='要我閉嘴可以，你先給狗幹👎')
        line_bot_api.reply_message(event.reply_token, message)
    elif '我是臭甲' in msg:
        message = TextSendMessage(text='我知道你是，麻煩退群，噁心')
        line_bot_api.reply_message(event.reply_token, message)
    elif '臭甲' in msg:
        message = TextSendMessage(text='你喔?你屁眼被幹的鬆到可以塞的下大象')
        line_bot_api.reply_message(event.reply_token, message)
    elif '好啊' in msg:
        message = TextSendMessage(text='ok👌')
        line_bot_api.reply_message(event.reply_token, message)
    elif '故事' in msg:
        message = TextSendMessage(text='從前從前有個太監，然後.............................................................................................................................就沒有下面了')
        line_bot_api.reply_message(event.reply_token, message)
    elif '站在雲林' in msg:
        message = TextSendMessage(text='我站在雲林☝️😑👇\n打魚☝️😑👇\n頭在暈☝️😑👇\n我擁有超能力☝️😑👇\n用冷水加飯菜☝️😑👇')
        line_bot_api.reply_message(event.reply_token, message)
    elif '打手槍' in msg:
        message = ImageSendMessage(
        original_content_url='https://imgur.dcard.tw/CGDGtLa.jpg',
        preview_image_url='https://imgur.dcard.tw/CGDGtLa.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '曬乾了沉默' in msg:
        message = ImageSendMessage(
        original_content_url='https://p5.toutiaoimg.com/large/pgc-image/171aa3b6524f4a848b08a50627c5830c',
        preview_image_url='https://p5.toutiaoimg.com/large/pgc-image/171aa3b6524f4a848b08a50627c5830c'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '抽棒子' in msg:
        message = ImageSendMessage(
        original_content_url='https://lh3.googleusercontent.com/pw/AM-JKLUVHfP1rMIN5GQhbnwOCIv5rBuRpBsZLnUxob3GF-43N-uObAG_bT4oK0s4Uu8QUOAcLm7AHGa_VMGsM5Bn2Ff8VD7rF1yTcqkTaylEWa8d1TddmnZiAh0Nyjg7Bf511qixVr9FPtyb0NBO8EoCW2hQBg=w720-h883-no?authuser=0',
        preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLUVHfP1rMIN5GQhbnwOCIv5rBuRpBsZLnUxob3GF-43N-uObAG_bT4oK0s4Uu8QUOAcLm7AHGa_VMGsM5Bn2Ff8VD7rF1yTcqkTaylEWa8d1TddmnZiAh0Nyjg7Bf511qixVr9FPtyb0NBO8EoCW2hQBg=w720-h883-no?authuser=0'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '熱愛105' in msg:
        message = TextSendMessage(text='滴滴清純的蒸餾水')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'superidol的笑容' in msg:
        message = TextSendMessage(text='都沒你的甜')
        line_bot_api.reply_message(event.reply_token, message)
    elif '八月正午的陽光' in msg:
        message = TextSendMessage(text='都沒你耀眼')
        line_bot_api.reply_message(event.reply_token, message)
    elif '不揪'in msg:
        message = TextSendMessage(text='好嘛 人家下次會記得揪你 原諒我一次好不好寶寶🥺')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'gg'in msg:
        message = TextSendMessage(text='ininder')
        line_bot_api.reply_message(event.reply_token, message)
    elif '抽妹子' in msg:

        m=random.randint(0, 50)
        if m<46:
            message = ImageSendMessage(
            original_content_url=girl(m),
            preview_image_url=girl(m)
            )
            line_bot_api.reply_message(event.reply_token, message)
        else :
            message = ImageSendMessage(
            original_content_url='https://lh3.googleusercontent.com/pw/AM-JKLWO_GDB_hyDlVHYSQSHx4TYGXWI36xfNtZlj0Dv81kqEWbuXxf9oRcjGVd8eMDoC-emj_zwkjrD-Zh5DMa9q7eaDSAijyu7z17e2uXESdHNgAelVMn544jnoT5a3ONlvHlK3C2JC0t8FrKzXDXNOuT-wQ=w570-h833-no?authuser=0',
            preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLWO_GDB_hyDlVHYSQSHx4TYGXWI36xfNtZlj0Dv81kqEWbuXxf9oRcjGVd8eMDoC-emj_zwkjrD-Zh5DMa9q7eaDSAijyu7z17e2uXESdHNgAelVMn544jnoT5a3ONlvHlK3C2JC0t8FrKzXDXNOuT-wQ=w570-h833-no?authuser=0'
            )
            line_bot_api.reply_message(event.reply_token, message)
    elif '我是色龜' in msg:

        m=random.randint(0, 50)
        if m<46:
            message = ImageSendMessage(
            original_content_url=girl2(m),
            preview_image_url=girl2(m)
            )
            line_bot_api.reply_message(event.reply_token, message)
        else :
            message = ImageSendMessage(
            original_content_url='https://lh3.googleusercontent.com/pw/AM-JKLUBdd1QYFlDUL-75qg3TlnELXVnwdKRc2bCp1ETEqiVdgvX75bTcSKIH6ruvJovBXTOi2oBiiYTFGTWAHU9uWFR6Yai7w2BO_5-DzPHnRkklRG92REKTN-bduto61Ottwqgk27v03D4ryPjSuvG81Mrrw=w637-h903-no?authuser=0',
            preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLUBdd1QYFlDUL-75qg3TlnELXVnwdKRc2bCp1ETEqiVdgvX75bTcSKIH6ruvJovBXTOi2oBiiYTFGTWAHU9uWFR6Yai7w2BO_5-DzPHnRkklRG92REKTN-bduto61Ottwqgk27v03D4ryPjSuvG81Mrrw=w637-h903-no?authuser=0'
            )
            line_bot_api.reply_message(event.reply_token, message)

    elif '==' in msg:
        message = TextSendMessage(text='= =拉幹')
        line_bot_api.reply_message(event.reply_token, message)
    elif '= =' in msg:
        message = TextSendMessage(text='==拉幹')
        line_bot_api.reply_message(event.reply_token, message)
    elif '你好' in msg:
        message=TextSendMessage(text='你好呀')
        line_bot_api.reply_message(event.reply_token, message)
    
    else:
        for i in wanginput:
            if i in msg:
                m=random.randint(0, 2)
                message=TextSendMessage(text=wangoutput(m))
                line_bot_api.reply_message(event.reply_token, message)
        for i in nineinput:
            if i in msg:
                m=random.randint(0, 19)
                message=TextSendMessage(text=nineoutput(m))
                line_bot_api.reply_message(event.reply_token, message)
        for i in badwordinput:
            if i in msg:
                m=random.randint(0, 20)
                message=TextSendMessage(text=badoutput(m))
                line_bot_api.reply_message(event.reply_token, message)
        for i in greeninput:
            if i in msg:
                m=random.randint(0, 10)
                message=TextSendMessage(text=blue(m))
                line_bot_api.reply_message(event.reply_token, message)
        for i in blueinput:
            if i in msg:
                m=random.randint(0, 2)
                message=TextSendMessage(text=green(m))
                line_bot_api.reply_message(event.reply_token, message)
        for i in sirsirinput:
            if i in msg:
                m=random.randint(0, 7)
                message = ImageSendMessage(
                original_content_url=sirsiroutput(m),
                preview_image_url=sirsiroutput(m)
                )
                line_bot_api.reply_message(event.reply_token, message)
        for i in gayinput:
            if i in msg:
                m=random.randint(0, 3)
                message = ImageSendMessage(
                original_content_url=gayoutput(m),
                preview_image_url=gayoutput(m)
                )
                line_bot_api.reply_message(event.reply_token, message)
        for i in fuyunginput:
            if i in msg:
                message = ImageSendMessage(
                original_content_url='https://lh3.googleusercontent.com/pw/AM-JKLVN7YnOjrchHsnAsMB_YXoOm008namFvOpyQcyiw2PDL83E5zpB8rwv-zvkQ6EzpR-mguKdLdJ8Edpax_wxWzZ-P9bqycuRg0wNPF8u0gCzIOyUvKEC1GE_FepW_H64Jr9e8hKvW_yLbFhmwwafMLGAcQ=w720-h535-no?authuser=0',
                preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLVN7YnOjrchHsnAsMB_YXoOm008namFvOpyQcyiw2PDL83E5zpB8rwv-zvkQ6EzpR-mguKdLdJ8Edpax_wxWzZ-P9bqycuRg0wNPF8u0gCzIOyUvKEC1GE_FepW_H64Jr9e8hKvW_yLbFhmwwafMLGAcQ=w720-h535-no?authuser=0'
                )
                line_bot_api.reply_message(event.reply_token, message)
        for i in judyinput:
            if i in msg:
                message = ImageSendMessage(
                original_content_url='https://lh3.googleusercontent.com/pw/AM-JKLXbgrjePLanN_HYUkwEa_eXmnQX4MwZSVu4ecsrawGWALUj56YQl01EXWS-7ACjUemtcPkSD1IJehrzl1nwJBYVXop1LR1X2aYCAXz9Evnyg_V7vIaVhXpl2jU0miTlm9MJa9AyYJrEEFsfrTJ607hsWQ=w763-h903-no?authuser=0',
                preview_image_url='https://lh3.googleusercontent.com/pw/AM-JKLXbgrjePLanN_HYUkwEa_eXmnQX4MwZSVu4ecsrawGWALUj56YQl01EXWS-7ACjUemtcPkSD1IJehrzl1nwJBYVXop1LR1X2aYCAXz9Evnyg_V7vIaVhXpl2jU0miTlm9MJa9AyYJrEEFsfrTJ607hsWQ=w763-h903-no?authuser=0'
                )
                line_bot_api.reply_message(event.reply_token, message)
        
        ##m=random.randint(0, 4)
        ##message=TextSendMessage(text=Fun(m))
        ##line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}嗨!你是偷偷喜歡我嗎，好瑟喔')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
