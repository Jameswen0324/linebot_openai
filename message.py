#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/BfTFVDN.jpg",
        alt_text='最新的合作廠商有誰呢？',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                #家樂福
                link_uri="https://tw.shop.com/search/%E5%AE%B6%E6%A8%82%E7%A6%8F",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #生活市集
                link_uri="https://tw.shop.com/search/%E7%94%9F%E6%B4%BB%E5%B8%82%E9%9B%86",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #阿瘦皮鞋
                link_uri="https://tw.shop.com/search/%E9%98%BF%E7%98%A6%E7%9A%AE%E9%9E%8B",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #塔吉特千層蛋糕
                link_uri="https://tw.shop.com/search/%E5%A1%94%E5%90%89%E7%89%B9",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=500
                )
            ),
            URIImagemapAction(
                #亞尼克生乳捲
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            )
        ]
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="是否要進行抽獎活動？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="看抽獎品項",
                    text="有哪些抽獎品項呢？"
                ),
                URITemplateAction(
                    label="免費註冊享回饋",
                    uri="https://tw.shop.com/nbts/create-myaccount.xhtml?returnurl=https%3A%2F%2Ftw.shop.com%2F"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='是否參加遊戲？',
        template=ConfirmTemplate(
            text="是否參加遊戲？",
            actions=[
                PostbackTemplateAction(
                    label="馬上參加",
                    text="我是臭甲",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="這次先不要",
                    text="今日確診145000人 ，好誇張。政府沒在做事? 陳死忠還想選北市。。。"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='爽拿優惠',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://lh3.googleusercontent.com/pw/AM-JKLXBeKqyTMHrhZgES9DKAbrTV5I7BGXMlptv1jdV9StarxG5BhlyWNukvwcKeWAMmp46zUqqWP6_KdX4XRyC8NCYSzMIX7MR1PUya0hRaA0PBUSRkT7uP4fVjeVEnnOxQFFb1Dzi9WM4sdj1jgUUPZRl9A=s200-no?authuser=0',
                    title='麥當勞優惠',
                    text='(11/24-12/28)',
                    actions=[
                        PostbackTemplateAction(
                            label='不要按',
                            data='這是ID=2',
                            text='我是乞丐'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我是乞丐'
                        ),
                        URITemplateAction(
                            label='拿優惠囉',
                            uri='https://campaign.mcdonalds.com.tw/2021EndOfTheYearCoupon/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://lh3.googleusercontent.com/pw/AM-JKLVJccBuRMr60VZgW0vnH37oO2YBwxHpa30oTL1CHZk8QMjfilBg8MVdM3D4kwe4eZeuJQ-jvp0ovHJQCWTJv44YTyGS5d6H9NqmnEX2jdTKFdFIovARQtaGS-2iAqFPhDVLeEyk1BghZcbY1X1BJjNz1w=w200-h199-no?authuser=0',
                    title='漢堡王優惠',
                    text='(11/19-1/17)',
                    actions=[
                        PostbackTemplateAction(
                            label='按了後悔',
                            data='這是ID=2',
                            text='我是乞丐'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我是乞丐'
                        ),
                        URITemplateAction(
                            label='按下我',
                            uri='https://www.burgerking.com.tw/coupon'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://lh3.googleusercontent.com/pw/AM-JKLUuTVMsDV2sFppjXnnFIvx5f-8JPLzpr4tq91WgCExFl65njYLS-mgdk5b0FKVmf6uuwhmC7EAzraa-etTDwlvEVuE7ub5xD4ilR2S-H4dGaIoE3ph_vG1wcnDD3ahq9ZqUKGuBnr9l02SKR6o2unX0PA=s200-no?authuser=0',
                    title='肯德基優惠',
                    text='爽用',
                    actions=[
                        PostbackTemplateAction(
                            label='就說不要按==',
                            data='這是ID=3',
                            text='我是乞丐'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我是乞丐'
                        ),
                        URITemplateAction(
                            label='點我拉智障',
                            uri='https://kfc.2dim.space/strict.html?fbclid=IwAR1U0kWLUm6R3Arjj78w2m55Rdb7nqf24abxRZPeGEEobuEta0sq3wDp4QA'
                        )
                    ]
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='優惠券',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://photos.google.com/share/AF1QipNlZw_zbE-VgIBxs3qccAVLF9uGDSEaCHiykyOVV7JCdmj262hAtIKmEcvx3B2wDA/photo/AF1QipO_9u1xz51Nh3k3-Y5kqGTGyIgKihUpq-rDVSfh?key=RUZ6WkNMN2loMGFVdW9IczRtMkJORzBZX0ZodFp3",
                    action=URITemplateAction(
                        label="麥當勞優惠(11/24-12/28)",
                        uri="https://campaign.mcdonalds.com.tw/2021EndOfTheYearCoupon/"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://photos.google.com/share/AF1QipNlZw_zbE-VgIBxs3qccAVLF9uGDSEaCHiykyOVV7JCdmj262hAtIKmEcvx3B2wDA/photo/AF1QipNQQCgTdTn3D_KKa7n7bZdmF-klvpdQMkllLiGO?key=RUZ6WkNMN2loMGFVdW9IczRtMkJORzBZX0ZodFp3",
                    action=URITemplateAction(
                        label="漢堡王優惠(11/19-1/17)",
                        uri="https://www.burgerking.com.tw/coupon"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://photos.google.com/share/AF1QipNlZw_zbE-VgIBxs3qccAVLF9uGDSEaCHiykyOVV7JCdmj262hAtIKmEcvx3B2wDA/photo/AF1QipP9QmBVoXwDIva_4mfXnRTvkwqr7fp8K4tiS7Ke?key=RUZ6WkNMN2loMGFVdW9IczRtMkJORzBZX0ZodFp3",
                    action=URITemplateAction(
                        label="肯德基優惠",
                        uri="https://kfc.2dim.space/strict.html?fbclid=IwAR1U0kWLUm6R3Arjj78w2m55Rdb7nqf24abxRZPeGEEobuEta0sq3wDp4QA"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message

#關於LINEBOT聊天內容範例
