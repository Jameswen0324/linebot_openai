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
