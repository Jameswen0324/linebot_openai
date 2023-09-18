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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '愛你' in msg:
        message = TextSendMessage(text='失去的不會再回來 錯過的終究不會再遇見 大概不打擾才是最後的溫柔 我比誰都喜歡你 但是沒有用啊 每天沉淪在明明知道沒希望還要無盡的等待整夜失眠 愛而不得的感受真的太難受了 以前老是說會保護你會給你安全感 後來你說我不是你想要的 感謝你出現再我的生命中 跟你在一起的那些時間我真的特別的開心 謝謝你')
        line_bot_api.reply_message(event.reply_token, message)
    elif msg[0:3]=='測試1000':
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '測試1000' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Yf4AhVUx5QKHb7tDF8Q2' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '今日確診145000人 ，好誇張。政府沒在做事? 陳死忠還想選北市。。。' in msg:
        message = TextSendMessage(text='300萬，已截圖舉報。民進黨政府感謝您對國庫的貢獻')
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
        message = TextSendMessage(text='這裡不能迴轉拉，怎麼了')
        line_bot_api.reply_message(event.reply_token, message)
    elif '早安' in msg:
        message = TextSendMessage(text='早你媽來做愛')
        line_bot_api.reply_message(event.reply_token, message)
    elif '午安' in msg:
        message = TextSendMessage(text='喔，我跟你很熟嗎')
        line_bot_api.reply_message(event.reply_token, message)
    elif '晚安' in msg:
        message = TextSendMessage(text='痾，臭甲==')
        line_bot_api.reply_message(event.reply_token, message)
    elif '謝謝' in msg:
        message = TextSendMessage(text='什麼時候這麼有禮貌?')
        line_bot_api.reply_message(event.reply_token, message)
    elif '吃啥' in msg:
        message = TextSendMessage(text='吃我懶覺')
        line_bot_api.reply_message(event.reply_token, message)
    elif '嗨' in msg:
        message = TextSendMessage(text='結婚嗎?')
        line_bot_api.reply_message(event.reply_token, message)
    elif '你又答錯了' in msg:
        message = TextSendMessage(text='https://photos.google.com/share/AF1QipNlZw_zbE-VgIBxs3qccAVLF9uGDSEaCHiykyOVV7JCdmj262hAtIKmEcvx3B2wDA/photo/AF1QipNnHA6HQtQK4jz5eApCAH_XyTBBBU1qGin-Mp6i?key=RUZ6WkNMN2loMGFVdW9IczRtMkJORzBZX0ZodFp3')
        line_bot_api.reply_message(event.reply_token, message)
    elif '測顏值' in msg:
        message = TextSendMessage(text='https://www.beautyscoretest.com/zht/?fbclid=IwAR2VMJJQX8FMhMeSapYSwRzBAxtMRTwB-kIPlUuvZ2OFgzE6Rs5tVAl4VDQ')
        line_bot_api.reply_message(event.reply_token, message)
    elif '欸欸' in msg:
        message = TextSendMessage(text='每次我發這麼大一段文字，你都看都不看，甚至就按一個表情隨便敷衍幾句，現在欸什麼，在你心中，我的地位像一顆沙子，你只在乎你自己，你有想過我嗎，每次一想起你我就把褲子套在頭上偷偷哭，生怕被你發現，每次一想起你我就整整流淚五個小時，認真的回我一句很難嗎。')
        line_bot_api.reply_message(event.reply_token, message)
    elif '喔喔' in msg:
        message = TextSendMessage(text='好啊每次都隨便敷衍回復我，ok阿我沒差，反正妳也不在乎我，我就活該被當工具人啊，我要跳下去了，別攔我，反正我就爛命')
        line_bot_api.reply_message(event.reply_token, message)
    elif '哈囉' in msg:
        message = TextSendMessage(text='好啊')
        line_bot_api.reply_message(event.reply_token, message)
    elif '想你' in msg:
        message = TextSendMessage(text='想我囉，是不是妳外面的男人又對妳不好，我想也是，不是這樣妳也不會想到我，我沒生氣啊，我就備胎的命，不說了我還要吃20顆安眠藥去睡呢')
        line_bot_api.reply_message(event.reply_token, message)
    elif '在幹嘛' in msg:
        message = TextSendMessage(text='在幹你娘')
        line_bot_api.reply_message(event.reply_token, message)
    elif '在嗎' in msg:
        message = TextSendMessage(text='借錢沒有，要命一條')
        line_bot_api.reply_message(event.reply_token, message)
    elif '不要這樣' in msg:
        message = TextSendMessage(text='又怎樣，反正妳也沒在乎過我，我現在就去自殺也不關妳的事')
        line_bot_api.reply_message(event.reply_token, message)
    elif '拜託' in msg:
        message = TextSendMessage(text='情緒勒索我?7414')
        line_bot_api.reply_message(event.reply_token, message)
    elif '乖' in msg:
        message = TextSendMessage(text='又想叫我乖，有甚麼用，每次都這樣搞好玩嘛，妳沒錯啦，錯的都是我，我該死好不好')
        line_bot_api.reply_message(event.reply_token, message)
    elif '我沒有' in msg:
        message = TextSendMessage(text='妳沒有?小偷會說自己偷東西?老板會承認自己賣盜版?我是看開了拉，也習慣了，我這種人也活該被妳這樣弄')
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
    elif '滾' in msg:
        message = TextSendMessage(text='好，我滾，反正妳早就想叫我滾，今天終於說出口了吧，我就滾吧，在你看來我就一個小丑')
        line_bot_api.reply_message(event.reply_token, message)
    elif '還好嗎' in msg:
        message = TextSendMessage(text='妳覺得呢?我很好非常好，不用關心我，反正也沒人愛我')
        line_bot_api.reply_message(event.reply_token, message)
    elif '我錯了' in msg:
        message = TextSendMessage(text='妳沒錯，都我的錯，都我不好，我最爛')
        line_bot_api.reply_message(event.reply_token, message)
    elif '不理我' in msg:
        message = TextSendMessage(text='每次我發這麼大一段文字，你都看都不看，甚至就按一個表情隨便敷衍幾句，ok阿我沒差，反正妳也不在乎我，現在說我不理妳?')
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
        message = TextSendMessage(text='敢命令林北講話你去死一死啦')
        line_bot_api.reply_message(event.reply_token, message)
    elif '張瀚文' in msg:
        message = TextSendMessage(text='他超帥我偶像')
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
        message = TextSendMessage(text='阿你怎麼還沒死😕')
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
        message = TextSendMessage(text='情緒勒索我?🙄🙄🙄')
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
        message = TextSendMessage(text='揪你也不會去')
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
        message=TextSendMessage(text='我好大家好')
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
