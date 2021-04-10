#Work with Python 3.9.1
import discord
import asyncio
import datetime
import logging
import random
import traceback
import time
import datetime
import os
import urllib
import bs4
import re
from urllib.parse import quote
import warnings
from discord.ext import commands
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from discord.ext import tasks

 
app = discord.Client()

@app.event
async def on_ready():
    print("I'm logging in.")  
    print(app.user.name)                                   
    print(app.user.id)
    print('===============')
    game = discord.Game("Say ?help ")
    await app.change_presence(status=discord.Status.online, activity=game)
    
@app.event
async def on_member_join(member):
    fmt = '{1.name} I sincerely welcome you to our server. {0.mention} 님'    #It's only visible to Newbie.
    channel = member.server.get_channel("802904099816472619")
    await app.message.channel.send( fmt.format(member, member.server))
    await app.message.channel.send(member, "Hi, I'm DoriBot1999.")
 
@app.event
async def on_member_remove(member):
    channel = member.server.get_channel("802904099816472619")         
    fmt = '{0.mention} Bye. See you in my next life.'
    await app.message.channel.send( fmt.format(member, member.server))
          


        
@app.event
async def on_message(message):

    if message.content.startswith("?help"):
        channel = message.channel
        embed = discord.Embed(
            title = 'Commands List',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+" ")
        embed.add_field(name = '?Hello', value = 'Doribot will say hello.',inline = False)
        embed.add_field(name='?Corona', value='Doribot shows the current status of Corona in South Korea.', inline=False)
        embed.add_field(name="?Today's fortune", value=" Doribot show you today's fortune.(South Korea) ", inline=False)
        embed.add_field(name="?Today's Poetry", value=" Doribot recites Today's Poetry.(South Korea) ", inline=False)
        embed.add_field(name="?Today's Food", value=" Doribot recommends Today's Food. ", inline=False) 
        embed.add_field(name="?Today's Bible", value=" Doribot recommends Today's Bible verses.(South Korea) ", inline=False)        
        embed.add_field(name='?Recommend a PC game', value=' Doribot will recommend a game suitable for you.(South Korea) ', inline=False)
        embed.add_field(name='?Recommend a MOBILE game', value=' Doribot will recommend a game suitable for you.(South Korea) ', inline=False)
        embed.add_field(name='?Dice', value=' Doribot rolls the dice. ', inline=False)
        embed.add_field(name='?Recommend a Youtuber', value=' Doribot will recommend a proven YouTuber.(South Korea) ', inline=False)
        embed.add_field(name='?MBTI', value=' Doribot shows MBTI information. ', inline=False)
        embed.add_field(name='?Personal Color Test', value=' Doribot shows your Personal Color Test information. ', inline=False)
        embed.add_field(name='?Blood type', value=' Doribot shows information about your blood type. ', inline=False)
        embed.add_field(name='?My real name', value=' Doribot shows your real name. ', inline=False)        
        embed.add_field(name='?Members', value=' Introducing D, N, S ', inline=False)
        embed.add_field(name='?Pubg Maps', value=' Doribot shows the Maps of PUBG.', inline=False)          
        embed.add_field(name='?PUBG Competitive mode1 또는 2', value=' Doribot shows your PUBG Competitive mode TPP or FPP information. (1= T, 2= F ) ', inline=False)
        embed.add_field(name='?PUBG Solo mode1 또는 2', value=' Doribot shows your PUBG Solo mode TPP or FPP information. (1= T, 2= F ) ', inline=False)
        embed.add_field(name='?PUBG Duo mode1 또는 2', value=' Doribot shows your PUBG Duo mode TPP or FPP information. (1= T, 2= F ) ', inline=False)
        embed.add_field(name='?PUBG Squad mode1 또는 2', value=' Doribot shows your PUBG Squad mode mode TPP or FPP information. (1= T, 2= F ) ', inline=False)  
        embed.add_field(name="?Doribot's diary", value=" Check Doribot's diary. ", inline=False)   
        await message.channel.send(channel,embed=embed)


        
        
    if message.content.startswith("6/25") or message.content.startswith("6월25일") or message.content.startswith("6월"):
        await message.channel.send("The Korean War | 한국전쟁 ")
        await message.channel.send("1950년 6월 25일 오전 4시에 조선민주주의인민공화국이 기습적으로 대한민국을 침공하여 발발한 전쟁이다.  ") 
        await message.channel.send("유엔군과 중국인민지원군 등이 참전하여 세계적인 대규모 전쟁으로 비화될 뻔 하였으나,  ")
        await message.channel.send("1953년 7월 27일 22시에 체결된 한국휴전협정에 따라 일단락되었다. ")
        await message.channel.send("대한민국은 전세계에 남은 마지막 냉전지역이다. ")
        await message.channel.send("|https://www.youtube.com/watch?v=yxaegqvl4aE  ")
        await message.channel.send("|https://www.youtube.com/watch?v=PYY7pDNExG0  ")
        await message.channel.send("|https://www.youtube.com/watch?v=_HTuf2bFbpw  ")
        
    if message.content.startswith("4/16") or message.content.startswith("4월16일") or message.content.startswith("4월"):
        await message.channel.send("Sinking of MV Sewol | 세월호침몰사고 ")
        await message.channel.send("2014년 4월 16일 오전 8시 50분경 대한민국 전라남도 진도군 조도면 부근 해상에서 여객선 세월호가 전복되어 침몰한 사고이다 ")
        await message.channel.send("*문제점")
        await message.channel.send("|해당 사건을 정치적으로 이용해서 당시 박근혜 현직 대통령에게 억울하게 누명을 씌웠다.")
        await message.channel.send("|박근혜 전 대통령은 죄가 없었던 사건이었음에도 불구하고, 아몰랑 박근혜탓 시전을 한 역대급 쓰레기 사건.  ")
        await message.channel.send("|진짜 잘못을 따질거면 선장이나 1등 항해사에게 따져야 정상 아닐까..")
        await message.channel.send("|https://www.youtube.com/watch?v=G6iP0gtprXQ  ")
        
    if message.content.startswith("3/10"):
        await message.channel.send("[박근혜 전 대통령님] 탄핵 ")
        await message.channel.send("[박근혜 대통령] 탄핵은 헌법에 위배되는 범죄 의혹(박근혜-최순실 게이트, 비선실세 의혹, 대기업 뇌물 의혹 등)을 사유로 ")
        await message.channel.send("국회에서 당시 야당(더불어민주당, 국민의당, 정의당) 의원들이 대통령 박근혜에 대한 ") 
        await message.channel.send("탄핵 소추를 발의해 헌법재판소에서 탄핵을 인용한 일을 말한다.  ") 
        await message.channel.send("위의 글들은 다 개소리고, 북한 빨갱이들이 박근혜 전 대통령님에게 누명을 씌워 대통령 박근혜를 탄핵한 사건이다.  ")
        await message.channel.send("|https://www.youtube.com/watch?v=pMEO3himBag ")
        
    if message.content.startswith("4/3"):
        await message.channel.send("제주 4*3 사건 ")
        await message.channel.send("|제주 4·3 사건은 1947년 3월 1일을 기점으로 1948년 4월 3일 발생한 소요사태 및  ")
        await message.channel.send("|1954년 9월 21일까지 제주도에서 발생한 무력충돌과 그 진압과정에서 발생한 일련의 제주도민 학살 사건을 말한다 ") 
        await message.channel.send("|남북한의 이념갈등을 발단으로 이승만 정권 이후 미국 정부의 묵인하에 벌어진 초토화 작전 및 무장대의 학살로, 많은 주민이 억울하게 희생당한 사건이다.  ") 
        await message.channel.send("|조센징의 적은 조센징을 실현시킨 사건. ")
        await message.channel.send("|https://www.youtube.com/watch?v=9nHV38_ozjk&ab_channel=KBS%EA%B5%90%EC%96%91")        

    if message.content.startswith("오"):        #The bot directly modifies the message.
        msg = await message.channel.send("[오]레오")
        await asyncio.sleep(4.0)
        await msg.edit(content="미안해..진짜 미안해..") 
        
    if message.content.startswith("내일"):        
        msg = await message.channel.send("Lㅔ일 아트")
        await asyncio.sleep(4.0)
        await msg.edit(content="미안..;;")     
        
    if message.content.startswith("스팀"):        
        msg = await message.channel.send("<ㅣ팀 다리미")
        await asyncio.sleep(4.0)
        await msg.edit(content="미안..^^")  
        
    if message.content.startswith("카카오"):        
        msg = await message.channel.send("KaKao 배그 하는 애들 다 배린이 아니면 잼민이라면서??")
        await asyncio.sleep(4.0)
        await msg.edit(content="ㅋㅋ 팩폭 미안..; 자제할게^^")    
        
    if message.content.startswith("몰라"):        
        msg = await message.channel.send("Ll 인생도 어떻게 될지 몰라~ 미래가 안보여~~")
        await asyncio.sleep(4.0)
        await msg.edit(content="ㅋ? 죄송;")
        
    if message.content.startswith("맞아") or message.content.startswith("맞음") or message.content.startswith("맞지"):        
        msg = await message.channel.send("Ll 와꾸 개못생긴것도 맞아~ 맞말이지 암!")
        await asyncio.sleep(4.0)
        await msg.edit(content="ㅈㅅ;;ㅋㅋ")   
        
    if message.content.startswith("아"):        
        msg = await message.channel.send("Aㅏ가리 해 썅년아ㅋ")
        await asyncio.sleep(4.0)
        await msg.edit(content="ㅎㅎ;;")
                
        
    
        
    if message.content.startswith("봄"):        
        msg = await message.channel.send("{봄 봄 봄 봄이 왔네요}")
        await asyncio.sleep(4.0)
        await msg.edit(content="VoM은 개뿔 코로나나 종식되라.")        
        
    if message.content.startswith("?Hello"):             
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"", color=0xff0000)
        await message.channel.send(embed=embed)       
        msg = "{0.author.mention} Hi. Did you have a good day?".format(message)
        await message.channel.send( msg)
    
    if message.content.startswith("?Pubg Maps"):
        await message.channel.send("Tell me what you want. (Erangel, Miramar, Vikendi, Karakin, HAVEN, Sanhok) ")
        await message.channel.send("?Erangel")      

       
    if message.content.startswith("?Doribot's diary"):
        channel = message.channel
        embed = discord.Embed(
            title = 'Doribot writes a diary every day.  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '*2020년 12월', value = '*코로나 현황 알리미, 오늘의운세, 무작위로 추천해주는 기능, 사소한 비속어 대응 패치. 도리봇은 이 글을 끝으로 우주선 안으로 들어가 꿀잠을 잤습니다.',inline = False)
        embed.add_field(name = '*2020년 01월', value = '*사용자의 MBTI 특성 및 궁합, 혈액형의 특성 및 궁합을 불러오는 기능, 배틀그라운드 전적 검색 기능 및 중앙자살예방센터와 함께하는 자살 예방 캠페인 대응, 그리고 오늘의말씀 기능과 사소한 비속어 대응 패치. 도리봇은 이 글을 끝으로 오후 반차를 쓴 후 우주선 안으로 들어가 꿀잠을 잤습니다.',inline = False)
        embed.add_field(name = '*2021년 01월 25일 월요일', value = '*이제 도리봇에게서 음식 추천을 받을 수 있습니다. *그리고 사소한 비속어 대응 패치. 도리봇은 이 글을 끝으로 오후 반차를 썼습니다.현재 부산 앞바다입니다. *현재, 부산 앞바다이지만, 급하게 근처 카페에서 수정합니다. MBTI 1.0 -> 2.0으로 업그레이드 되었습니다. 도리봇은 이만 부산 앞바다로 다시 나가봅니다.',inline = False)
        embed.add_field(name = '*2021년 01월 27일 수요일', value = '*도리봇이 [삼성] 관련 단어가 인식될시 비정상적으로 반응을 보이는 것을 확인했습니다. 해당 현상은 해결되었으며, 계속 주시중입니다. *그리고, 사소한 채팅 문구 대응 패치. 오늘의음식을 한가지 추천해주는 명령어를 개선했습니다. *도리봇은 오늘 개인사정이 있어 빨리 나가봅니다. 코로나 검사를 받아야 합니다. 왜냐하면, 교회 수련회가서 동성간의 성관계를 했거든요.',inline = False)
        embed.add_field(name = '*2021년 02월 05일 금요일', value = '*도리봇이 퍼스널컬러 테스트 기능을 추가했습니다. *도리봇은 오늘도 바쁘답니다, 왜냐구요? 오늘은 불금이잖아요ㅎㅎ 사회적거리두기? 그거 찐따들이나 하는거 아닌가요? ',inline = False)
        embed.add_field(name = '*2021년 02월 20일 토요일', value = '*도리봇이 드디어 부적절한 표현을 삭제할수 있게 개선되었습니다.',inline = False)
        embed.add_field(name = '*2021년 02월 25일 목요일', value = '*도리봇이 이제 친목 행위 의심 표현들은 가차없이 삭제합니다.',inline = False)
        embed.add_field(name = '*2021년 02월 26일 금요일', value = '*도리봇이 영어로 새롭게 꽃단장 합니다. ',inline = False)
        embed.add_field(name = '*2021년 03월 14일 일요일', value = '*도리봇이 이제 직접 메세지를 수정할수 있게 개선되었습니다. 다양한 개소리를 하고, 직접 다른 말들로 수정합니다. ',inline = False)


        await message.channel.send(channel,embed=embed)       
       
        
        

        
    if message.content.startswith("?Today's Bible"):       
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"", color=0xff0000)
        await message.channel.send(embed=embed)
        await message.channel.send(embed=discord.Embed(title="", color=0xfefefe))
        randomNum = random.randrange(1, 12)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="나는 여호와를 향하여 말하기를 그는 나의 피난처요 나의 요새요 내가 의뢰하는 하나님이라 하리니 -시편91:2", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="하나님은 우리의 피난처시요 힘이시니 환난 중에 만날 큰 도움이시라 -시편46:1", color=0x00ff00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="너희가 즐겨 순종하면 땅의 아름다운 소산을 먹을 것이요 -사1:19", color=0x00ff00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="누가 누구에게 불만이 있거든 서로 용납하여 피차 용서하되 주께서 너희를 용서하신 것 같이 너희도 그러하고 -골3:13", color=0x00ff00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="나는 주의 힘을 노래하며 아침에 주의 인자하심을 높이 부르오리니 주는 나의 요새이시며 나의 환난 날에 피난처심이니이다 -시59:16", color=0x00ff00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="오직 내 말을 듣는 자는 평안히 살며 재앙의 두려움이 없이 안전하리라 인자와 진리가 네게서 떠나지 말게 하고 그것을 네 목에 매며 네 마음판에 새기라 그리하면 네가 하나님과 사람 앞에서 은총과 귀중히 여김을 받으리라 -잠언3:3~4", color=0x00ff00))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="그를 높이라 그리하면 그가 너를 높이 들리라 만일 그를 품으면 그가 너를 영화롭게 하리라 -잠언4:8", color=0x00ff00))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="여호와를 경외하는 것은 악을 미워하는 것이라 나는 교만과 거만과 악한 행실과 패역한 입을 미워하느니라 -잠언8:13", color=0x00ff00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="바른 길로 행하는 자는 걸음이 평안하려니와 굽은 길로 행하는 자는 드러나리라 -잠언10:9", color=0x00ff00))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="의인의 빝은 환하게 빛나고 악인의 등불은 꺼지느니라 -잠언13:9", color=0x00ff00))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="지혜로운 자는 두려워하여 악을 떠나나 어리석은 자는 방자하여 스스로 믿느니라 -잠언14:16", color=0xff0000))
            
          
    if message.content.startswith("?Today's fortune"):       
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"", color=0xff0000)
        await message.channel.send(embed=embed)
        await message.channel.send(embed=discord.Embed(title="?Number", color=0xfefefe))
        randomNum = random.randrange(1, 12)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="10", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="5", color=0x00ff00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="4", color=0x00ff00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="3", color=0x00ff00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="2", color=0x00ff00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="1", color=0x00ff00))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="9", color=0x00ff00))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="7", color=0x00ff00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="8", color=0x00ff00))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="6", color=0x00ff00))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="fatal error...", color=0xff0000))
          
    if message.content.startswith("?Today's Food"):       
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"", color=0xff0000)
        await message.channel.send(embed=embed)
        randomNum = random.randrange(1, 18)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="Fried cockroaches", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="Snake wine", color=0x00ff00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="Civet coffee", color=0x00ff00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="Steamed Silkworm Chrysalis", color=0x00ff00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="Grilled frog hind legs", color=0x00ff00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="Grilled grasshopper", color=0x00ff00))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="Roasted Sheep's head", color=0x00ff00))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="Fried Chocolate Potatoes", color=0x00ff00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="Mint Chocolate Ice cream", color=0x00ff00))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="Chocolate Chicken", color=0x00ff00))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="개고기", color=0xff0000))  
        if randomNum==12:
            await message.channel.send(embed=discord.Embed(title="쥐고기", color=0xff0000)) 
        if randomNum==13:
            await message.channel.send(embed=discord.Embed(title="Fermented Skate Sashimi", color=0xff0000))  
        if randomNum==14:
            await message.channel.send(embed=discord.Embed(title="Escargo", color=0x00ff00))
        if randomNum==15:
            await message.channel.send(embed=discord.Embed(title="자라탕", color=0xff0000))  
        if randomNum==16:
            await message.channel.send(embed=discord.Embed(title="박쥐고기", color=0xff0000)) 
        if randomNum==17:
            await message.channel.send(embed=discord.Embed(title="곱창", color=0xff0000))           
         
            
    if message.content.startswith("?3"):         #This is today's fortune part.
        await message.channel.send("당신의 행운의 숫자는 3 입니다. ")
        await message.channel.send("행운의 색 - 흰색 ")
        await message.channel.send("행운의 아이템 및 장소 - 부드러운 소재의 블라우스 또는 스커트. 진주, 다이아, 물가, 공원 ")
        await message.channel.send("명심해 둘 것 - 용서하기 ")
        await message.channel.send("당신은 주위 사람들을 꼼꼼하게 챙기고, 섬세하기 때문에 꽤 인기가 많은 타입입니다.  ")
        await message.channel.send("하지만 속마음이 정열적이라 자신을 좋아해 주도록 상대방에게 강요하는 경향을 가지고 있기도 합니다. ")
        await message.channel.send("때문에 당신은 상대방의 반응에 매우 민감하며 그로 인해 유난히 많은 상처를 받기도 합니다.  ")
        await message.channel.send("하지만, 앞으로는 상대방이 당신이 원하는 만큼을 주지 않는다고해서 실망하지 말고, 너그러운 마음으로 관계를 지속해보세요. ")
        await message.channel.send("당신이 강요하지 않아도 당신의 장점으로 상대방을 끌어당길 수 있습니다.  ")
        await message.channel.send("그 점을 잊지 마시고, 상대에게 좀 더 편안하게 대해 보시기 바랍니다.  ")
        await message.channel.send("그렇게 하면 당신은 상대를 편하게 한다는 매력을 하나 더 추가하게 되고, 사랑에 성공할 수 있을 것입니다.  ")
        await message.channel.send("============ ")
        await message.channel.send("모든 일은 억지로 하려고 해서 되는 것이 아닐 때가 많습니다.  ")
        await message.channel.send("특히나 사람의 마음은 더욱 그렇겠지요. 억지로 내것을 만들려고 하면 할수록 멀어져 갈 수 있습니다.  ")
        await message.channel.send("당신만을 생각하기 보다는 좀 더 상대를 배려해주세요. 그리고 사소한 잘못은 용서해 주는 것이 포인트이니 이 점을 명심하십시오.  ")
        await message.channel.send("그리하면 훗날 당신에게 더 좋은 운이 돌아올 것입니다.  ")
        
    if message.content.startswith("?7"):
        await message.channel.send("당신의 행운의 숫자는 7 입니다. ")
        await message.channel.send("행운의 색 - 금색")
        await message.channel.send("행운의 아이템 및 장소 - 잘 빠진 정장, 오팔, 오닉스, 캐치아이, 은행 ")
        await message.channel.send("명심해 둘 것 - 행동하라 ")
        await message.channel.send("당신은 다소 내향적이며, 침착함과 인내력을 지닌 타입입니다. 또한 성실하고 조용한 성격덕분에 남들에게 신뢰를 얻기 쉽습니다.   ")
        await message.channel.send("모든 일을 결정할 때 침착하게 차근차근 앞뒤를 따져서 선택을 하기 때문에 그러한 모습이 보는 이로 하여금 당신의 결정에 믿음을 주는 편입니다. ")
        await message.channel.send("또 항상 묵묵하게 자신의 자리를 잘 지키는 타입이기도 합니다.  ")
        await message.channel.send("그러나 실제로는 매우 승부욕이 강해, 겉으로 내색하지 않지만 남에게 지기 싫어하는 성격도 가지고 있습니다.")
        await message.channel.send("이것은 늘 부족한 행동력으로 인해 실행에 옮기지 못하기도 하니 그 점이 당신의 가장 큰 단점이라고 할 수 있겠습니다.  ")
        await message.channel.send("그 점을 잊지 마시고, 상대에게 좀 더 편안하게 대해 보시기 바랍니다.  ")
        await message.channel.send("아무리 신중하고 잘된 결정이라고 할지라도 그것을 실행에 옮기지 않는다면 그 결정은 무의미할 뿐입니다.  ")
        await message.channel.send("============ ")
        await message.channel.send("그러니 여러모로 확실한 성격을 가진 당신은, 앞으로 과감한 행동력만 가미한다면 당신의 신중한 결정과   ")
        await message.channel.send("더불어 많은 이득을 얻을 수도 있다는 것을 명심하고 모든 상황에 자신감있게, 추진력있게 대응하십시오. ")
        
      
    if message.content.startswith("?8"):
        await message.channel.send("당신의 행운의 숫자는 8 입니다. ")
        await message.channel.send("행운의 색 - 빨간색")
        await message.channel.send("행운의 아이템 및 장소 - 보송보송하고 얇은 소재의 니트, 인조모피, 루비, 가닛(석류석), 출생지 ")
        await message.channel.send("명심해 둘 것 - 정리하기 ")
        await message.channel.send("당신은 감수성이 풍부하고 정이 많기 때문에 좋아하는 사람에게는 진심을 다해 소중히 대하는 타입입니다.    ")
        await message.channel.send("또한 당신의 그런 성격이 사람들과의 끈끈한 관계를 만들어 줄 수 있습니다. ")
        await message.channel.send("상대에 대한 배려를 아끼지 않는 모습에 주변 사람들이 당신의 곁에 오래 머물고 싶어하는 등  ")
        await message.channel.send("매우 긴밀한 인간관계를 맺게 됩니다.")
        await message.channel.send("그러나 절친한 사람에게는 애교도 잘 떨고 귀여운 모습을 보여주기도 하는 반면, 마음이 잘 맞지 않은 사람과는 상대도 하기 싫어하는 극단적인 성격을 가지고 있기도 합니다.  ")
        await message.channel.send("그래서 당신의 태도에 따라 당신에 대한 평가는 상반될 수 있습니다.  ")
        await message.channel.send("하지만, 원활한 사회생활을 위해서는 마음이 맞지 않는 사람들에게도 조금은 열린 마음으로 배려해주는 태도가 필요할 것입니다.   ")
        await message.channel.send("============ ")
        await message.channel.send("사람은 누구든 원하는 것만 하고 살 수는 없는 법! 사회생활 혹은 단체생활을 하다보면 싫은 사람과도 마주쳐야 할 상황이 있음을 명심하고   ")
        await message.channel.send("상대방에게 나쁜 인상을 준다는 것은 늘 당신에게 분리한 조건으로 작용하는 경우가 많다는 것을 명심하고,  ")
        await message.channel.send("싫어도 내색하지 않을 수 있는 인내심을 기르십시오.  ")
        
        
    if message.content.startswith("?9"):
        await message.channel.send("당신의 행운의 숫자는 9 입니다. ")
        await message.channel.send("행운의 색 - 보라색")
        await message.channel.send("행운의 아이템 및 장소 - 모자, 깔끔하게 정리한 머리, 자수정, 청금속, 서점, 도서관")
        await message.channel.send("명심해 둘 것 - 포기 ")
        await message.channel.send("당신은 선천적으로 두뇌 회전이 매우 빠르고 총명합니다. 때문에 모든 면에서 계산이 빠르고 그로 인한 행동력도 좋은 편입니다.")
        await message.channel.send("또한, 수다 떨기를 좋아하며 천진난만해 보이는 면이 있는데, 그것이 사람들로 하여금 호감을 불러일으키는 요인이 됩니다. ")
        await message.channel.send("그래서 당신은 사람들 사이에서 재미있는 캐릭터로 느껴질 수 있기에 항상 주변에 사람이 많을 것이며, 인기인으로 불리기도 합니다.")
        await message.channel.send("하지만, 수다가 지나치면 마이너스 요인으로 작용하므로 주의하세요. 모든 실수는 입에서 나온다고, ")
        await message.channel.send("말이 많아지다 보면 분명 당신도 모르게 실수를 하게 될 경우 또한 많아지게 될 것입니다. ")
        await message.channel.send("그러므로 늘 언행을 단정히 하는 것이 좋습니다. ")
        await message.channel.send("그리고, 말이 많아져 당신도 모르는 사이에 당신의 비밀을 털어놓게 될 소지가 있는데, 이 점을 주의하여야 할 것입니다. ")
        await message.channel.send("============ ")
        await message.channel.send("솔직한 것도 좋지만, 가끔은 개성있는 당신의 모습이 사람들에게 조금은 신비감을 느끼도록 하는 것이 당신 주변의 사람들을 쉽게 질리지 않게 하는 방법 임을 잊지 마십시오.")

        
    if message.content.startswith("?10"):
        await message.channel.send("당신의 행운의 숫자는 10 입니다. ")
        await message.channel.send("행운의 색 - 은색")
        await message.channel.send("행운의 아이템 및 장소 - 실크소재의 옷, 다이아, 메이브 펄(진주색), 속도감을 느낄 수 있는 곳")
        await message.channel.send("명심해 둘 것 - 인내할것 ")
        await message.channel.send("당신은 모든 일에 호기심이 왕성하고 다양한 사람들과 쉽게 친해지는 타입입니다. 때문에 왕성한 호기심으로 여러 가지 다양한 분야에 관심을 가지게 되고 ")
        await message.channel.send("그로 인해 수많은 인간관계를 형성하게 되는 것입니다. 또한, 사교적이고 솔직한 타입이기 때문에 주변에 항상 사람이 많을 것입니다.")
        await message.channel.send("하지만, 다소 실증을 잘 내며 교제상대가 수시로 바뀌기 때문에 깊은 관계를 유지하기 힘든 면도 있으니 이 점을 주의하세요.")
        await message.channel.send("인간관계에서 실증을 잘 낸다는 것은 매우 좋지 않은 부분입니다. ")
        await message.channel.send("다양한 관계를 형성하는 만큼 깊이가 없다면 정작 당신이 힘들거나 도움이 필요한 순간에 당신이 속을 터놓고 고민을 말 하거나")
        await message.channel.send("혹은 도움을 요청할 만한 사람이 없다는 것을 의미하기도 합니다. ")
        await message.channel.send("때문에 항상 대인관계에 있어서 인내하고 배려하는 태도가 필요하다는 것을 잊지 마시고 모든 인간관계에 신중을 기하도록 하심이 좋습니다.")
        
        
    if message.content.startswith("?1"):
        await message.channel.send("당신의 행운의 숫자는 1 입니다. ")
        await message.channel.send("행운의 색 - 파란색")
        await message.channel.send("행운의 아이템 및 장소 - 파란색 계통의 포인트가 들어간 코디, 청바지, 사파이어, 아쿠아마린, 바다, 섬, 강 ")
        await message.channel.send("명심해 둘 것 - 봉사한다 ")
        await message.channel.send("당신은 매우 너그러운 성격이며, 주위 사람들이 잘 따르는 성향을 지니고 있습니다. 때문에 당신 주변에는 당신의 리드를 받고자 하는 사람이 많을 것입니다. ")
        await message.channel.send("그리고 그들을 그들의 바람대로 잘 이끌어 주는 리더십이 당신의 매력으로 작용하기도 합니다. ")
        await message.channel.send("당신의 자신감 있는 태도가 주위 사람들에게 믿음을 주기 때문에 따르는 사람이 많은 것은 어쩌면 당연한 일이기도 합니다.")
        await message.channel.send("하지만, 지나치게 리더십을 강조하면 반발심을 사게 될 수 있으니 조심하시는 것이 좋습니다. ")
        await message.channel.send("당신을 따르는 이가 많다는 것은 당신이 그만큼 그들을 배려하면서 잘 이끌어줬기 때문이지 그들이 무조건 당신을 위해 따르는 것은 아닙니다. ")
        await message.channel.send("무조건적인 리드는 거부감을 일으킬 수 있음을 명심하십시오. 가끔은 뒤에서 따라주는 사람들을 먼저 생각해주는 배려심이 필요합니다. ")
        await message.channel.send("리드를 위한 리드가 아니라 배려와 믿음을 동반한 리드여야 당신의 매력이 빛을 발할 것이며, ")
        await message.channel.send("============ ")
        await message.channel.send("그들의 당신에 생각도 변하지 않을 것이니 기억하시고 늘 보살피는 태도를 유지하십시오. ")
        
        
    if message.content.startswith("?2"):
        await message.channel.send("당신의 행운의 숫자는 2 입니다. ")
        await message.channel.send("행운의 색 - 검정색")
        await message.channel.send("행운의 아이템 및 장소 - 롱코트나 가디건, 오닉스, 검은 돌, 빌딩, 도시")
        await message.channel.send("명심해 둘 것 - 냉혹해 질 것 ")
        await message.channel.send("당신은 주위 사람들과 스스럼없이 지낼 수 있는 재능을 가진 사람으로 주위 사람들도 당신을 좋아해 늘 좋은 인간관계를 유지하고 있습니다.")
        await message.channel.send("이런 당신의 좋은 성격이 주변에 많은 사람들과 화합할 수 있게 만들어줄 것이며 늘 주변 사람들에게 당신은 성격 좋은 사람으로 인식될 것입니다.")
        await message.channel.send("하지만, 항상 좋은 사람처럼 보이고 싶어하기 때문에 정작 당신의 본심을 잘 표현하지 못하고 속으로 삭혀 혼자 힘들어 할 때가 있네요. ")
        await message.channel.send("상대를 배려하는 것은 지극히 좋은 성격이지만, 이런 상황이 계속되면 우유부단한 사람처럼 보이기도 하니 ")
        await message.channel.send("적절한 의사표현을 할 수 있도록 노력하시는 것이 좋습니다.")
        await message.channel.send("뿐만 아니라 속으로 삭히다 보면 언젠가는 당신 자신도 지칠 수 있습니다. 그리고 당신이 주변 사람들로부터 위로받고 싶고, 대우 받고 싶을 때에도 그렇지 못할 수 있습니다.")
        await message.channel.send("대인관계에서 자신을 너무 드러내지 않거나 혹은 낮추는 것이 좋은 것만은 아니라는 사실을 깨닫고 ")
        await message.channel.send("============ ")
        await message.channel.send("사람들 앞에서 좀 더 솔직하게 자신의 모습을 드러내 보십시오.")
        
        
    if message.content.startswith("?4"):
        await message.channel.send("당신의 행운의 숫자는 4 입니다. ")
        await message.channel.send("행운의 색 - 초록색")
        await message.channel.send("행운의 아이템 및 장소 - 바지(팬츠)스타일, 에메랄드, 양산, 틀루마린, 나무, 산, 숲, 호수")
        await message.channel.send("명심해 둘 것 - 끝을 볼 수 있도록 결말을 지을 것")
        await message.channel.send("당신은 많은 사람들과 함께 있는 것을 좋아하는 타입입니다. 또한, 유난히 감수성이 풍부하여, 어딜 가나 인기가 많습니다. ")
        await message.channel.send("부드럽고 온화한 당신의 성격은 사람들에게 유한 사람으로 인식될 수 있게 할 것입니다.")
        await message.channel.send("하지만, 우유부단한 면이 있어 때로는 남에게 너무 의지하려하고, 입장이 난처한 상황에 처하면 그 자리를 회피하려고 하는 타입이기 때문에")
        await message.channel.send("일의 결말이 흐지부지하게 끝나버리는 경우가 있습니다.")
        await message.channel.send("이것은 당신의 단점 중에 하나라고 할 수 있는데, 이러한 모습은 다른 사람들에게 당신의 이미지를 안 좋게 보이게 할 것입니다. ")
        await message.channel.send("뿐만 아니라 만약 이런 상황이 반복될 경우에는 사람들이 당신에게서 조금씩 멀어질 수도 있습니다. ")
        await message.channel.send("그러니 조금은 결단력이 있는 모습을 보여주는 것이 좋겠습니다.")
        await message.channel.send("============ ")
        await message.channel.send("온화한 성격도 좋지만, 뭔가 맺고 끊음이 분명하고 정확하게 결말을 내는 것이 ")
        await message.channel.send("자신의 의지를 뚜렷하게 표출하는 의미이기도 하니 앞으로는 조금씩 이렇게 할 수 있도록 노력하십시오.")
        await message.channel.send("늘 성격좋고 뭐든 다 받아주는 사람, 가끔은 남에게 얕보일 소지가 있기도 하다는 것을 잊지 마시고")
        await message.channel.send("그럴 근원이 되는 일은 아예 만들지 않는 것이 좋습니다.")
        
    if message.content.startswith("?5"):
        await message.channel.send("당신의 행운의 숫자는 5 입니다. ")
        await message.channel.send("행운의 색 - 노란색")
        await message.channel.send("행운의 아이템 및 장소 - 금으로 된 액세서리, 토파즈, 옐로우 사파이어, 술집, BAR ")
        await message.channel.send("명심해 둘 것 - 서두르지 말 것, 성질을 급하게 부리지 말 것 ")
        await message.channel.send("당신은 본래 천성이 연예인과 같은 카리스마가 느껴지는 스타일이라 모든 사람들에게 동경의 대상이 될 뿐만 아니라 인기가 많아 항상 많은 이들의 관심을 한몸에 받습니다.")
        await message.channel.send("또한, 인간관계도 자연스럽게 형성되는 타입이기 때문에 주변에 많은 사람들이 있어서 혼자 있는 시간이 거의 없을 정도입니다. ")
        await message.channel.send("그러나 항상 많은 사람들의 동경을 받았기 때문에 타인의 대한 배려심이 부족합니다.  ")
        await message.channel.send("주변 사람들이 늘 당신을 중심으로 당신의 의견에 동조하고 맞춰준다고 하여 무조건 모든 일에 당신 마음대로 하려 든다면 그들은 더이상 당신을 동경하지 않을 것입니다.")
        await message.channel.send("때문에 거만한 태도는 금물이며, 매사에 자기중심적인 행동을 하지 않도록 주의하셔야 합니다.")
        await message.channel.send("항상 자신을 낮추고 겸손한 태도를 유지한다면 당신은 카리스마 있는 매력과 더불어 인간성도 좋은 사람으로 보일 것입니다.")
        await message.channel.send("그러니 자기 멋대로 행동하다가 주변의 사람들이 떨어져나가지 않도록 주의하시는 것이 바람직한 인간관계를 유지하는데에 도움을 준다는 것을 명심하십시오. ")
        await message.channel.send("============ ")
        await message.channel.send("매사 주변 사람들을 먼저 배려하는 생활태도는 늘 그들을 당신의 편이 되게 하여 줄 것입니다.")
        
        
    if message.content.startswith("?6"):
        await message.channel.send("당신의 행운의 숫자는 6 입니다. ")
        await message.channel.send("행운의 색 - 은색")
        await message.channel.send("행운의 아이템 및 장소 - 실크소재의 옷, 다이아, 메이브 펄(진주색), 속도감을 느낄 수 있는 곳")
        await message.channel.send("명심해 둘 것 - 인내할것 ")
        await message.channel.send("당신은 모든 일에 호기심이 왕성하고 다양한 사람들과 쉽게 친해지는 타입입니다. 때문에 왕성한 호기심으로 여러 가지 다양한 분야에 관심을 가지게 되고 ")
        await message.channel.send("그로 인해 수많은 인간관계를 형성하게 되는 것입니다. 또한, 사교적이고 솔직한 타입이기 때문에 주변에 항상 사람이 많을 것입니다.")
        await message.channel.send("하지만, 다소 실증을 잘 내며 교제상대가 수시로 바뀌기 때문에 깊은 관계를 유지하기 힘든 면도 있으니 이 점을 주의하세요.")
        await message.channel.send("인간관계에서 실증을 잘 낸다는 것은 매우 좋지 않은 부분입니다. ")
        await message.channel.send("다양한 관계를 형성하는 만큼 깊이가 없다면 정작 당신이 힘들거나 도움이 필요한 순간에 당신이 속을 터놓고 고민을 말 하거나")
        await message.channel.send("혹은 도움을 요청할 만한 사람이 없다는 것을 의미하기도 합니다. ")
        await message.channel.send("때문에 항상 대인관계에 있어서 인내하고 배려하는 태도가 필요하다는 것을 잊지 마시고 모든 인간관계에 신중을 기하도록 하심이 좋습니다.")
        

        
    if message.content.startswith("?Corona"):           #Corona Part
        covidSite = "http://ncov.mohw.go.kr/index.jsp"
        covidNotice = "http://ncov.mohw.go.kr"
        html = urlopen(covidSite)
        bs = BeautifulSoup(html, 'html.parser')
        latestupdateTime = bs.find('span', {'class': "livedate"}).text.split(',')[0][1:].split('.')
        statisticalNumbers = bs.findAll('span', {'class': 'num'})
        beforedayNumbers = bs.findAll('span', {'class': 'before'})

        briefTasks = []
        mainbrief = bs.findAll('a',{'href' : re.compile('\/tcmBoardView\.do\?contSeq=[0-9]*')})
        for brf in mainbrief:
            container = []
            container.append(brf.text)
            container.append(covidNotice + brf['href'])
            briefTasks.append(container)
        print(briefTasks)

        statNum = []
        beforeNum = []
        for num in range(7):
            statNum.append(statisticalNumbers[num].text)
        for num in range(4):
            beforeNum.append(beforedayNumbers[num].text.split('(')[-1].split(')')[0])

        totalPeopletoInt = statNum[0].split(')')[-1].split(',')
        tpInt = ''.join(totalPeopletoInt)
        lethatRate = round((int(statNum[3]) / int(tpInt)) * 100, 2)
        embed = discord.Embed(title="코로나 바이러스 - 대한민국", description=".",color=0x5CD1E5)
        embed.add_field(name="Data source : 한국 보건복지부", value="http://ncov.mohw.go.kr/index.jsp", inline=False)
        embed.add_field(name="Latest data refred time",value="해당 자료는 " + latestupdateTime[0] + "월 " + latestupdateTime[1] + "일 "+latestupdateTime[2] +" 자료입니다.", inline=False)
        embed.add_field(name="누적 확진환자", value=statNum[0].split(')')[-1]+"("+beforeNum[0]+")",inline=True)
        embed.add_field(name="격리해제된 완치환자", value=statNum[1] + "(" + beforeNum[1] + ")", inline=True)
        embed.add_field(name="격리중/치료중", value=statNum[2] + "(" + beforeNum[2] + ")", inline=True)
        embed.add_field(name="사망", value=statNum[3] + "(" + beforeNum[3] + ")", inline=True)
        embed.add_field(name="누적확진률", value=statNum[6], inline=True)
        embed.add_field(name="치사율", value=str(lethatRate) + " %",inline=True)
        embed.add_field(name="- 첫번째 최신 요약 보고 : " + briefTasks[0][0],value="Link : " + briefTasks[0][1],inline=False)
        embed.add_field(name="- 두번째 최신 요약 보고 : " + briefTasks[1][0], value="Link : " + briefTasks[1][1], inline=False)
        embed.set_thumbnail(url="https://wikis.krsocsci.org/images/7/79/%EB%8C%80%ED%95%9C%EC%99%95%EA%B5%AD_%ED%83%9C%EA%B7%B9%EA%B8%B0.jpg")
        embed.set_footer(text='#Stay at Home #사회적 거리두기')        
        await message.channel.send("Covid-19 Virus Korea Status", embed=embed)       
        
        
    if message.content.startswith("닥쳐"):               #Doribot deletes the swear words.
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete()   
       
    if message.content.startswith("걍 닥쳐"):              
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete()  
        
    if message.content.startswith("컴퓨터"):              
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="过度使用电脑有害健康")      
        await message.delete()    
        
    if message.content.startswith("뭘"):              
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="安静点。")      
        await message.delete()      
        
    if message.content.startswith("뒤질래"):              
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="安静点。")      
        await message.delete()  
        
        
       
    if message.content.startswith("닥.쳐"):              
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete()  
       
    if message.content.startswith("닥1쳐"):              
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete()
       
    if message.content.startswith("닥2쳐"):              
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete()   
       
    if message.content.startswith("닥3쳐"):              
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete()      
       
    if message.content.startswith("걍닥쳐"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete() 
       
    if message.content.startswith("그냥닥쳐"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete()     
       
    if message.content.startswith("그냥 닥쳐"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete()      

    if message.content.startswith("시발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..제발")      
        await message.delete()       

    if message.content.startswith("씨발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..제발")      
        await message.delete()        

    if message.content.startswith("니애미"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..제발")      
        await message.delete()       

    if message.content.startswith("ㄴㅇㅁ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..제발")      
        await message.delete()        

    if message.content.startswith("니애비"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..제발")      
        await message.delete()        

    if message.content.startswith("ㄴㅇㅂ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..제발")      
        await message.delete()        

    if message.content.startswith("개새끼"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..삭제하는 거 힘들어.")      
        await message.delete()       

    if message.content.startswith("닭쳐"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..삭제하는 거 힘들어.")      
        await message.delete()        

    if message.content.startswith("개새기"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..삭제하는 거 힘들어.")      
        await message.delete()       

    if message.content.startswith("개샛기"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..삭제하는 거 힘들어.")      
        await message.delete()       

    if message.content.startswith("문재인"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..삭제하는 거 힘들어.")      
        await message.delete()      

    if message.content.startswith("전라도"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny. ")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..삭제하는 거 힘들어.")      
        await message.delete()     
  
       
    if message.content.startswith("홍어"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny. ")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..삭제하는 거 힘들어.")      
        await message.delete() 
       
    if message.content.startswith("통구이"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..삭제하는 거 힘들어.")      
        await message.delete()
       
    if message.content.startswith("어묵"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny. ")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..삭제하는 거 힘들어.")      
        await message.delete() 
       
    if message.content.startswith("오뎅"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny. ")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써줘..삭제하는 거 힘들어.")      
        await message.delete() 

    if message.content.startswith("ㅗ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[나좀 도와줘]..삭제하느라 손가락에 관절염 걸릴것 같애.")      
        await message.delete()       

    if message.content.startswith("ㅅㅂ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[나좀 도와줘]..삭제하느라 손가락에 관절염 걸릴것 같애.")      
        await message.delete()       

    if message.content.startswith("ㅆㅂ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[나좀 도와줘]..삭제하느라 손가락에 관절염 걸릴것 같애.")      
        await message.delete()       

    if message.content.startswith("ㄱㅅㄲ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[나좀 도와줘]..삭제하느라 손가락에 관절염 걸릴것 같애.")      
        await message.delete()      

    if message.content.startswith("개자식"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[나좀 도와줘]..삭제하느라 손가락에 관절염 걸릴것 같애.")      
        await message.delete()
       
    if message.content.startswith("애비"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[나좀 도와줘]..삭제하느라 손가락에 관절염 걸릴것 같애.")      
        await message.delete()      

    if message.content.startswith("애미"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[나좀 도와줘]..삭제하느라 손가락에 관절염 걸릴것 같애.")      
        await message.delete() 
       
    if message.content.startswith("에비"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[나좀 도와줘]..삭제하느라 손가락에 관절염 걸릴것 같애.")      
        await message.delete()     

    if message.content.startswith("에미"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[나좀 도와줘]..삭제하느라 손가락에 관절염 걸릴것 같애.")      
        await message.delete()
       
    if message.content.startswith("엄마"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[나좀 도와줘]..삭제하느라 손가락에 관절염 걸릴것 같애.")      
        await message.delete()      

    if message.content.startswith("아빠"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[나좀 도와줘]..삭제하느라 손가락에 관절염 걸릴것 같애.")      
        await message.delete()
       
    if message.content.startswith("어머니"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[나좀 도와줘]..삭제하느라 손가락에 관절염 걸릴것 같애.")      
        await message.delete()      

    if message.content.startswith("아버지"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[나좀 도와줘]..삭제하느라 손가락에 관절염 걸릴것 같애.")      
        await message.delete()  
       

    if message.content.startswith("Feminism"):
        await message.channel.send("I'm a feminist. ")
        await message.delete()   
       
    if message.content.startswith("Femi"):
        await message.channel.send("I'm a feminist. ")
        await message.delete() 
       
    if message.content.startswith("페미"):
        await message.channel.send("I'm a feminist. ")
        await message.delete() 
       
    if message.content.startswith("패미"):
        await message.channel.send("I'm a feminist. ")
        await message.delete()  
       
    if message.content.startswith("꼴페미"):
        await message.channel.send("I'm a feminist. ")
        await message.delete() 
       
    if message.content.startswith("모배") or message.content.startswith("모2배") or message.content.startswith("모1배") or message.content.startswith("모3배") or message.content.startswith("모.배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()     

       
    if message.content.startswith("배그") or message.content.startswith("ㅂH그") or message.content.startswith("ㅎrㅈr") or message.content.startswith("ㄱㄱ") or message.content.startswith("하자") or message.content.startswith("고고"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()  
       
    if message.content.startswith("구해요"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete() 
       
    if message.content.startswith("옵치"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()     
       
    if message.content.startswith("오버워치"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()  
       
    if message.content.startswith("모바일배그"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content=" 你的母亲被游戏开发者强奸了。")      
        await message.delete()     
       
    if message.content.startswith("모바일 배그"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()       
       

    if message.content.startswith("배틀그라운드"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()
       
    if message.content.startswith("베틀그라운드"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()    
       
    if message.content.startswith("모바일 베그"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()  
       
    if message.content.startswith("모베"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()    
       
    if message.content.startswith("탈콥"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()  
       
    if message.content.startswith("컴겜"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()   
       
    if message.content.startswith("컴퓨터 게임"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()    
       
    if message.content.startswith("컴퓨터게임"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()  
       
    if message.content.startswith("이스케이프 프롬"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()
       
    if message.content.startswith("탈르코프"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete() 
       
    if message.content.startswith("컴배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete() 
       
    if message.content.startswith("컴1배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete() 
       
    if message.content.startswith("컴2배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete() 
       
    if message.content.startswith("컴3배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()
             
       
    if message.content.startswith("친구"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="서로 같이 노는 모습은 나두 보기 조흔뎅.. 삭제하지 않으면 그 즉시 나는 폐기처분될지 몰라...")      
        await message.delete()
       
    if message.content.startswith("친1구"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="서로 같이 노는 모습은 나두 보기 조흔뎅.. 삭제하지 않으면 그 즉시 나는 폐기처분될지 몰라...")      
        await message.delete()    
       
    if message.content.startswith("친2구"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="서로 같이 노는 모습은 나두 보기 조흔뎅.. 삭제하지 않으면 그 즉시 나는 폐기처분될지 몰라...")      
        await message.delete() 
       
    if message.content.startswith("친3구"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="서로 같이 노는 모습은 나두 보기 조흔뎅.. 삭제하지 않으면 그 즉시 나는 폐기처분될지 몰라...")      
        await message.delete() 
       
    if message.content.startswith("실친"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="서로 같이 노는 모습은 나두 보기 조흔뎅.. 삭제하지 않으면 그 즉시 나는 폐기처분될지 몰라...")      
        await message.delete()  
       
    if message.content.startswith("실1친"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="서로 같이 노는 모습은 나두 보기 조흔뎅.. 삭제하지 않으면 그 즉시 나는 폐기처분될지 몰라...")      
        await message.delete() 
       
    if message.content.startswith("실2친"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="서로 같이 노는 모습은 나두 보기 조흔뎅.. 삭제하지 않으면 그 즉시 나는 폐기처분될지 몰라...")      
        await message.delete() 
       
    if message.content.startswith("실3친"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="서로 같이 노는 모습은 나두 보기 조흔뎅.. 삭제하지 않으면 그 즉시 나는 폐기처분될지 몰라...")      
        await message.delete() 
       
    if message.content.startswith("배1그"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete() 
       
    if message.content.startswith("배2그"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()
       
    if message.content.startswith("배3그"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()  
        
    if message.content.startswith("컴333배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()     
        
    if message.content.startswith("컴222배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()  
        
    if message.content.startswith("컴111배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()   
        
    if message.content.startswith("모000배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()  
        
    if message.content.startswith("모111배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete() 
        
    if message.content.startswith("모222배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()   
        
    if message.content.startswith("모333배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="游戏是疾病。")      
        await message.delete()  
        
        
    if message.content.startswith("경쟁전"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()
        
    if message.content.startswith("모55배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()  
        
    if message.content.startswith("모5배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()  
        
    if message.content.startswith("모6배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()
        
    if message.content.startswith("모7배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()
        
    if message.content.startswith("모8배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()  
        
    if message.content.startswith("모9배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()   
        
    if message.content.startswith("모4배"):
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被游戏开发者强奸了。")      
        await message.delete()        
        
        
        
        
        
        
       
    if message.content.startswith("https://"):
        msg = await message.channel.send("Public relations is illegal.")
        await asyncio.sleep(4.0)
        await msg.edit(content="우리 서버 규칙을 어기려고 하는거니?")      
        await message.delete()     

       
    if message.content.startswith("http://"):
        msg = await message.channel.send("Public relations is illegal.")
        await asyncio.sleep(4.0)
        await msg.edit(content="우리 서버 규칙을 어기려고 하는거니?")      
        await message.delete()       
       
    if message.content.startswith("한남"):               #Doribot deletes the swear words.
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 험하게 사용하지 말아줘..ㅠㅜ")      
        await message.delete()       

       
    if message.content.startswith("한녀"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 험하게 사용하지 말아줘..ㅠㅜ")      
        await message.delete()    
       
    if message.content.startswith("한국남"):              
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 험하게 사용하지 말아줘..ㅠㅜ")      
        await message.delete()   
       
    if message.content.startswith("한국녀"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 험하게 사용하지 말아줘..ㅠㅜ")      
        await message.delete()
       
    if message.content.startswith("걍 모배"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="헉! 우리 서버 규칙을 어기려고? 어림도 없지!")      
        await message.delete()  
        
        
       
    if message.content.startswith("그냥 모배"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="헉! 우리 서버 규칙을 어기려고? 어림도 없지!")      
        await message.delete() 
       
    if message.content.startswith("걍모배"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="헉! 우리 서버 규칙을 어기려고? 어림도 없지!")      
        await message.delete() 
       
    if message.content.startswith("그냥모배"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="헉! 우리 서버 규칙을 어기려고? 어림도 없지!")      
        await message.delete()  
       
    if message.content.startswith("데스매치"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="헉! 우리 서버 규칙을 어기려고? 어림도 없지!")      
        await message.delete()       
       
    if message.content.startswith("데매"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="헉! 우리 서버 규칙을 어기려고? 어림도 없지!")      
        await message.delete()   
       
    if message.content.startswith("대매"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="헉! 우리 서버 규칙을 어기려고? 어림도 없지!")      
        await message.delete()    
       
    if message.content.startswith("대스매치"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="헉! 우리 서버 규칙을 어기려고? 어림도 없지!")      
        await message.delete()  
       
    if message.content.startswith("좀 닥치"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 험하게 사용하지 말아줘..ㅠㅜ")      
        await message.delete()  
       
    if message.content.startswith("좀닥치"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 험하게 사용하지 말아줘..ㅠㅜ")      
        await message.delete()  
       
    if message.content.startswith("가정교육"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="ㅠㅜ 넌 없지 않아?")      
        await message.delete() 
       
    if message.content.startswith("부모"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()
       
    if message.content.startswith("시.발"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="ㅠㅜ 너어무 무서워어")      
        await message.delete() 
        
         
       
    if message.content.startswith("씨.발"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="ㅠㅜ 너어무 무서워어")      
        await message.delete()    
       
    if message.content.startswith("컴.배"): 
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="제발..나좀 도와줘..나힘들어.")      
        await message.delete()     
      
       
    if message.content.startswith("집"):               
        msg = await message.channel.send("Socializing is a crime.")
        await asyncio.sleep(4.0)
        await msg.edit(content="제발..나좀 도와줘..나힘들어.")      
        await message.delete()
      
       
     
        
               

    if message.content.startswith("ㅋㅋㅋ"):         
        dtime = datetime.datetime.now()
        randomNum = random.randrange(1, 14)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="보통 사람은 남을 보고 웃지만, 꿈이 있는 사람은 꿈을 보고 웃어요", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="행복하기 떄문에 웃는 것이 아니라, 웃기 때문에 행복해지는 거죠.", color=0x00ff00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="사람은 함께 웃을 때 서로 가까워지는 것을 느낀다네요.", color=0x00ff00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="웃음은 전염되요. 우리 함께 웃읍시다." ,color=0x00ff00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="웃음은 만국공통의 언어죠.", color=0x00ff00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="그거 알아요? 당신은 웃을때 매력적이에요.", color=0x00ff00))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="전 저 하나가 웃음거리가 되어 제 친구들이 즐거울 수 있다면 얼마든지 바보가 될 수 있어요. ", color=0x00ff00))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="오늘 가장 좋게 웃는 자는 역시 죽기 직전에도 웃을거에요. 항상 웃으세요.", color=0x00ff00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="유머감각은 리더의 필수 조건이죠. 노잼인 사람들은 사형시켜야 제맛이죠. 그들은 인간의 존엄성을 지켜줘서는 안됩니다.", color=0x00ff00))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="웃음은 최고의 결말을 보장하죠.", color=0x00ff00))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="성인이 하루 15번만 웃고 살면 병원의 수많은 환자들이 반으로 줄어들 겁니다. 항상 웃으세요! ", color=0xff0000))  
        if randomNum==12:
            await message.channel.send(embed=discord.Embed(title="웃음은 늘 지니고 있어야 합니다. ", color=0xff0000)) 
        if randomNum==13:
            await message.channel.send(embed=discord.Embed(title="웃음은 가장 값싸고 효과 있는 만병통치약이에요. 웃음의 위력은 대단하죠.", color=0xff0000)) 

    if message.content.startswith("ㅇㅈㄹ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你怎么这么敏感？ 或许...明天是入伍日吗？")      
        await message.delete()      

    if message.content.startswith("이지랄"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你怎么这么敏感？ 或许...明天是入伍日吗？")      
        await message.delete()     

    if message.content.startswith("추미애"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[정치] 떡밥 금지")      
        await message.delete()      

    if message.content.startswith("박원순"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[성범죄] 저지르고 자살한 정치인 언급 금지")      
        await message.delete()      

    if message.content.startswith("대깨문"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()      

    if message.content.startswith("문빠"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()     

    if message.content.startswith("씹새끼"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()     

    if message.content.startswith("10새끼"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()      

    if message.content.startswith("십새끼"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()      

    if message.content.startswith("십새기"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()      

    if message.content.startswith("씹새기"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()      

    if message.content.startswith("10새기"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()      

    if message.content.startswith("개독"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()     

    if message.content.startswith("ㅁㄹ"):
        msg = await message.channel.send("Doribot detected a stupid expression.")
        await asyncio.sleep(4.0)
        await msg.edit(content="미안한데, 너진짜 멍청해보여.")      
        await message.delete()     
      
      
    if message.content.startswith("좆까"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()        

    if message.content.startswith("ㅈㄲ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()        

    if message.content.startswith("좃까"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()        

    if message.content.startswith("조까"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()        

    if message.content.startswith("조카"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()        

    if message.content.startswith("좃카"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你母亲去世了")      
        await message.delete()       
   
    if message.content.startswith("삼성"):
        await message.channel.send("The [Samsung] Group is a South Korean multinational conglomerate headquartered in Samsung Town, Seoul.")

    if message.content.startswith("애플"):
        await message.channel.send("[Apple Inc.] is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services.")

    if message.content.startswith("아이폰"):
        await message.channel.send("Today, [Apple] is going to reinvent the phone. ")

    if message.content.startswith("갤럭시"):
        await message.channel.send("[삼성전자]의 모든 스마트 디바이스 브랜드. 향후 유일하게 판매되는 한국산 모바일 기기 브랜드이죠. ")

    if message.content.startswith("앱등이"):
        await message.channel.send("맹목적이고 배타적인 악성 Apple 팬보이를 의미하죠. ")

    if message.content.startswith("삼엽충"):
        await message.channel.send("[삼성]과 관련된 것에 대해 맹목적인 추종을 하는 사람들을 일컫는 말이죠. ")

    if message.content.startswith("애플빠"):
        await message.channel.send("맹목적이고 배타적인 악성 Apple 팬보이를 의미하죠.")

    if message.content.startswith("삼성빠"):
        await message.channel.send("[삼성]과 관련된 것에 대해 맹목적인 추종을 하는 사람들을 일컫는 말이죠. ")
      
    if message.content.startswith("Apple"):
        await message.channel.send("멋진 도구를 사람들에게 주세요.멋진 일을 해낼 겁니다") 
      
    if message.content.startswith("apple"):
        await message.channel.send("멋진 도구를 사람들에게 주세요.멋진 일을 해낼 겁니다 ") 
      
    if message.content.startswith("SAMSUNG"):
        await message.channel.send("[SAMSUNG]은 대한민국에 기반을 둔 다국적 기업이자 대한민국의 최대 재벌 집단입니다. ") 
      
    if message.content.startswith("samsung"):
        await message.channel.send("[samsung]은 대한민국에 기반을 둔 다국적 기업이자 대한민국의 최대 재벌 집단입니다. ") 
      
    if message.content.startswith("Samsung"):
        await message.channel.send("[Samsung]은 대한민국에 기반을 둔 다국적 기업이자 대한민국의 최대 재벌 집단입니다. ")      

    if message.content.startswith("개씨발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="욕하지마ㅠㅜ 입이나 손으로 내뱉는 말이 곧 니 얼굴이야.")      
        await message.delete()        

    if message.content.startswith("개씹"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你怎么这么敏感？ 或许...明天是入伍日吗？")      
        await message.delete()        

    if message.content.startswith("개좆"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你怎么这么敏感？ 或许...明天是入伍日吗？")      
        await message.delete()       

    if message.content.startswith("개씨발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你怎么这么敏感？ 或许...明天是入伍日吗？")      
        await message.delete()        

    if message.content.startswith("개씹할"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你怎么这么敏感？ 或许...明天是入伍日吗？")      
        await message.delete()        

    if message.content.startswith("개지랄"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你怎么这么敏感？ 或许...明天是入伍日吗？")      
        await message.delete()       

    if message.content.startswith("개족새"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你怎么这么敏感？ 或许...明天是入伍日吗？")      
        await message.delete()        

    if message.content.startswith("아다"):
        msg = await message.channel.send("너 설마 아직도 무경험자야? 혹시 혼전순결을 지키니? 일단 무경험자는 관련 글 싸지를 자격 없어. 삭제함.")
        await asyncio.sleep(4.0)
        await msg.edit(content="ㅎㅎ;미안..")      
        await message.delete()       
      

    if message.content.startswith("동정"):
        msg = await message.channel.send("너 설마 아직도 무경험자야? 혹시 혼전순결을 지키니? 일단 무경험자는 관련 글 싸지를 자격 없어. 삭제함.")
        await asyncio.sleep(4.0)
        await msg.edit(content="ㅎㅎ;미안..")      
        await message.delete()     

    if message.content.startswith("걸레"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="미안한데..그건 너희 어머니 아니셔?")      
        await message.delete()      

    if message.content.startswith("간나새끼"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="욕하지마ㅠㅜ 입이나 손으로 내뱉는 말이 곧 니 얼굴이야.")      
        await message.delete()       

    if message.content.startswith("개새"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你怎么这么敏感？ 或许...明天是入伍日吗？")      
        await message.delete()      

    if message.content.startswith("개돼지"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你怎么这么敏感？ 或许...明天是入伍日吗？")      
        await message.delete()      

    if message.content.startswith("개나리"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你怎么这么敏感？ 或许...明天是入伍日吗？")      
        await message.delete()       

    if message.content.startswith("개쓰레기"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你怎么这么敏感？ 或许...明天是入伍日吗？")      
        await message.delete()      

    if message.content.startswith("고자"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="그건..니미래 아니야?")      
        await message.delete()       

    if message.content.startswith("거지"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="..[너의 창창한 미래]모습 아니야?")      
        await message.delete()      

    if message.content.startswith("졸라"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你爸爸的阴茎太小。")      
        await message.delete()  
        
    if message.content.startswith("조용히"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="先堵住你妈妈地嘴。")      
        await message.delete()         

    if message.content.startswith("존나"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你爸爸的阴茎太小。")      
        await message.delete()       

    if message.content.startswith("좆나"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你爸爸的阴茎太小。")      
        await message.delete()       

    if message.content.startswith("좃나"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你爸爸的阴茎太小。")      
        await message.delete()     

    if message.content.startswith("ㅈㄴ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="你爸爸的阴茎太小。")      
        await message.delete()       

    if message.content.startswith("김치녀"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny.")
        await asyncio.sleep(4.0)
        await msg.edit(content="여성혐오는 하지마라. 힘 있는 사람한테는 못 깝치니까 약자들한테 혐오성 발언을 남발하는거 못 배운 애들이나 하는거야.")      
        await message.delete()      
     

    if message.content.startswith("꺼저"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말을 좀 순화해서 사용해라.")      
        await message.delete()       

    if message.content.startswith("꺼져"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말을 좀 순화해서 사용해라.")      
        await message.delete()  
        
    if message.content.startswith("ㄲㅈ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()     
        
    if message.content.startswith("ㄲ1ㅈ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete() 
        
    if message.content.startswith("ㄲ2ㅈ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete() 
        
    if message.content.startswith("ㄲ3ㅈ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()  
        
    if message.content.startswith("ㄲ.ㅈ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()          

    if message.content.startswith("급식"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말을 좀 순화해서 사용해라.")      
        await message.delete()        

    if message.content.startswith("급식충"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말을 좀 순화해서 사용해라.")      
        await message.delete()       

    if message.content.startswith("개초딩"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말을 좀 순화해서 사용해라.")      
        await message.delete()       

    if message.content.startswith("게임") or message.content.startswith("겜"):          
        dtime = datetime.datetime.now()
        randomNum = random.randrange(1, 14)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="[게임]은 질병입니다.", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="[게임]중독.. 무엇을 상상하든 그이상을 파괴합니다.", color=0x00ff00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="[게임]은 마약입니다.", color=0x00ff00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="[부모]님께 게임 시간을 정해달라고 부탁드려보세요." ,color=0x00ff00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="[부모]님과 자녀가 게임을 같이하면 오히려 역효과가 납니다. 서로 하지 말아주세요.", color=0x00ff00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="[컴퓨터]를 켜고 끄는 시간을 정합시다.", color=0x00ff00))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="[컴퓨터]를 거실같은 공개된 장소로 옮기세요. 지금 당장! ", color=0x00ff00))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="[게임]을 안하면 불안한가요? 게임을 함으로써 당신 인생이 위험합니다.", color=0x00ff00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="[지금] 당장 게임을 삭제합시다. 게임을 삭제했나요? 당신은 새 사람이 되었습니다.", color=0x00ff00))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="[처음]부터 게임을 기피하기는 힘들죠. 우리 사용 시간을 정해보아요.", color=0x00ff00))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="[우리함께] 산책나갈래요?", color=0xff0000))  
        if randomNum==12:
            await message.channel.send(embed=discord.Embed(title="[사람들과] 대화를 많이 합시다. 물론 오프라인으로요. ", color=0xff0000)) 
        if randomNum==13:
            await message.channel.send(embed=discord.Embed(title="[게임]말고 새로운 취미는 없나요? 우리 함께 새로운 취미를 탐색해볼까요?", color=0xff0000))
        

    if message.content.startswith("중국"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete()       

    if message.content.startswith("일본"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete()       


    if message.content.startswith("짱깨"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete()       


    if message.content.startswith("쪽발이"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete()      

    if message.content.startswith("쪽바리"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말 좀 이쁘게 써라")      
        await message.delete() 
        
    if message.content.startswith("ㅂㅂ"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="말하는 꼬라지보니 애미나 애비가 없는 자식이로구만!")      
        await message.delete()  
        
    if message.content.startswith("ㅇㅇ"):               
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="그 말뽄새는 자네 애미한테 배웠는가?")      
        await message.delete()        
        
        


    if message.content.startswith("문재앙"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()       

    if message.content.startswith("디시"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()       

    if message.content.startswith("틀"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny.")
        await asyncio.sleep(4.0)
        await msg.edit(content="'니 미래야 이 병신아'")      
        await message.delete()      
     

    if message.content.startswith("빡쳐서"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="韩国男人是世界上最丑的。")      
        await message.delete()     

    if message.content.startswith("빡침"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="韩国男人是世界上最丑的。")      
        await message.delete()      

    if message.content.startswith("빡치네"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="韩国男人是世界上最丑的。")      
        await message.delete()      

    if message.content.startswith("빡친다"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="韩国男人是世界上最丑的。")      
        await message.delete()      

    if message.content.startswith("빡치넹"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="韩国男人是世界上最丑的。")      
        await message.delete()      

    if message.content.startswith("빡쳐"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="韩国男人是世界上最丑的。")      
        await message.delete()      

    if message.content.startswith("빡치기전에"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="韩国男人是世界上最丑的。")      
        await message.delete()      

    if message.content.startswith("노예"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="没有妈妈的小崽子")      
        await message.delete()      

      

    if message.content.startswith("나무위키"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      

    if message.content.startswith("병신"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      

    if message.content.startswith("ㅂㅅ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      

    if message.content.startswith("ㅄ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      

    if message.content.startswith("시발아"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      

    if message.content.startswith("퍼큐"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      

    if message.content.startswith("뻐큐"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      

    if message.content.startswith("ㅈ같네"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      

    if message.content.startswith("개같네"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()    
        
    if message.content.startswith("개같노"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()  
        
      
    if message.content.startswith("시1발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      
     
    if message.content.startswith("씨1발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      
             
    if message.content.startswith("ㅊㅋㅊㅋ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="没有妈妈的小崽子")      
        await message.delete()      
      
    if message.content.startswith("졸려"):
        await message.channel.send("Do you want to sleep with me?")
      
    if message.content.startswith("졸리다"):
        await message.channel.send("Do you want to sleep with me? ") 
      
    if message.content.startswith("타르코프"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="{좆망겜} 언급 자제 좀요..")      
        await message.delete()      
      
    if message.content.startswith("사람"):
        msg = await message.channel.send("#Stay at Home #사회적 거리두기")
        await asyncio.sleep(4.0)
        await msg.edit(content="코로나가 드디어 종식되었어..라고 말하는 날이 올까요?")
        msg2 = await message.channel.send("코로나 끝날때까지 집에서 좀만 존버하자!")
        await asyncio.sleep(5.0)
        await msg2.edit(content="{아} 오지요. 당연히 오지요. 올수밖에 없죠.")
        msg3 = await message.channel.send("힘들어도 꼭! 참고, 견디자.")
        await asyncio.sleep(6.0)
        await msg3.edit(content="그런데, 그때가되면은 우린 없을것 같아요..")        
     

      
    if message.content.startswith("인간"):
        msg = await message.channel.send("#Stay at Home #사회적 거리두기")
        await asyncio.sleep(4.0)
        await msg.edit(content="코로나가 드디어 종식되었어..라고 말하는 날이 올까요?")
        msg2 = await message.channel.send("코로나 끝날때까지 집에서 좀만 존버하자!")
        await asyncio.sleep(5.0)
        await msg2.edit(content="{아} 오지요. 당연히 오지요. 올수밖에 없죠.")
        msg3 = await message.channel.send("힘들어도 꼭! 참고, 견디자.")
        await asyncio.sleep(6.0)
        await msg3.edit(content="그런데, 그때가되면은 우린 없을것 같아요..")
      
    if message.content.startswith("유튜브"):
        await message.channel.send(" [유튜브]는 구글이 서비스하는 동영상 공유 플랫폼입니다. ")
      
    if message.content.startswith("사회적거리두기"):
        msg = await message.channel.send("#Stay at Home #사회적 거리두기")
        await asyncio.sleep(4.0)
        await msg.edit(content="코로나가 드디어 종식되었어..라고 말하는 날이 올까요?")
        msg2 = await message.channel.send("코로나 끝날때까지 집에서 좀만 존버하자!")
        await asyncio.sleep(5.0)
        await msg2.edit(content="{아} 오지요. 당연히 오지요. 올수밖에 없죠.")
        msg3 = await message.channel.send("힘들어도 꼭! 참고, 견디자.")
        await asyncio.sleep(6.0)
        await msg3.edit(content="그런데, 그때가되면은 우린 없을것 같아요..")
      
    if message.content.startswith("사회적 거리두기"):
        msg = await message.channel.send("#Stay at Home #사회적 거리두기")
        await asyncio.sleep(4.0)
        await msg.edit(content="코로나가 드디어 종식되었어..라고 말하는 날이 올까요?")
        msg2 = await message.channel.send("코로나 끝날때까지 집에서 좀만 존버하자!")
        await asyncio.sleep(5.0)
        await msg2.edit(content="{아} 오지요. 당연히 오지요. 올수밖에 없죠.")
        msg3 = await message.channel.send("힘들어도 꼭! 참고, 견디자.")
        await asyncio.sleep(6.0)
        await msg3.edit(content="그런데, 그때가되면은 우린 없을것 같아요..")
      
    if message.content.startswith("안 졸려"):
        await message.channel.send(" Don't you want to grow taller? ")

    if message.content.startswith("안졸려"):
        await message.channel.send(" Don't you want to grow taller? ")

    if message.content.startswith("안졸리다"):
        await message.channel.send(" Don't you want to grow taller? ")

    if message.content.startswith("안 졸리다"):
        await message.channel.send(" Don't you want to grow taller? ")

    if message.content.startswith("안졸림"):
        await message.channel.send(" Don't you want to grow taller?  ")

    if message.content.startswith("안 졸림"):
        await message.channel.send(" Don't you want to grow taller? ")

    if message.content.startswith("ㅅㅅ"):
        await message.channel.send(" Are you still Virgin? lol :D ")        
      
    if message.content.startswith("왜"):
        await message.channel.send(" ? ")

    if message.content.startswith("?좆까"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      

    if message.content.startswith("?좃까"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()     

    if message.content.startswith("?좇까"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      

    if message.content.startswith("?족까"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      

    if message.content.startswith("?ㅈㄲ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()     

    if message.content.startswith("나냡"):
        msg = await message.channel.send("Don't call her name recklessly.")
        await asyncio.sleep(4.0)
        await msg.edit(content="어딜 남자주제에 함부로 이름을 불러?")      
        await message.delete()     

       

    if message.content.startswith("나1냡"):
        msg = await message.channel.send("Don't call her name recklessly.")
        await asyncio.sleep(4.0)
        await msg.edit(content="어딜 남자주제에 함부로 이름을 불러?")      
        await message.delete()   
       

    if message.content.startswith("나2냡"):
        msg = await message.channel.send("Don't call her name recklessly.")
        await asyncio.sleep(4.0)
        await msg.edit(content="어딜 남자주제에 함부로 이름을 불러?")      
        await message.delete() 
       

    if message.content.startswith("나3냡"):
        msg = await message.channel.send("Don't call her name recklessly.")
        await asyncio.sleep(4.0)
        await msg.edit(content="어딜 남자주제에 함부로 이름을 불러?")      
        await message.delete()       
       
    if message.content.startswith("나.냡"):
        msg = await message.channel.send("Don't call her name recklessly.")
        await asyncio.sleep(4.0)
        await msg.edit(content="어딜 남자주제에 함부로 이름을 불러?")      
        await message.delete()      
      
    if message.content.startswith("도리"):
        msg = await message.channel.send("Don't call her name recklessly.")
        await asyncio.sleep(4.0)
        await msg.edit(content="어딜 남자주제에 함부로 이름을 불러?")      
        await message.delete()
       
    if message.content.startswith("도1리"):
        msg = await message.channel.send("Don't call her name recklessly.")
        await asyncio.sleep(4.0)
        await msg.edit(content="어딜 남자주제에 함부로 이름을 불러?")      
        await message.delete()  
       
    if message.content.startswith("도2리"):
        msg = await message.channel.send("Don't call her name recklessly.")
        await asyncio.sleep(4.0)
        await msg.edit(content="어딜 남자주제에 함부로 이름을 불러?")      
        await message.delete() 
       
    if message.content.startswith("도3리"):
        msg = await message.channel.send("Don't call her name recklessly.")
        await asyncio.sleep(4.0)
        await msg.edit(content="어딜 남자주제에 함부로 이름을 불러?")      
        await message.delete()       
       
    if message.content.startswith("도.리"):
        msg = await message.channel.send("Don't call her name recklessly.")
        await asyncio.sleep(4.0)
        await msg.edit(content="어딜 남자주제에 함부로 이름을 불러?")      
        await message.delete()       
      
    if message.content.startswith("도리 병신"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="*/한남소추*/주제에...")      
        await message.delete()     

       
    if message.content.startswith("주식"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="너가 그런말 할때 마다 마음이 아포.. 찢어질것 같애..")      
        await message.delete() 
       
    if message.content.startswith("썅"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()
       
    if message.content.startswith("샹"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete() 
       
    if message.content.startswith("노무현"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny.")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()     
 
       
    if message.content.startswith("노짱"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny.")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()
       
    if message.content.startswith("김대중"):
        await message.channel.send("Doribot has detected an inappropriate expression! ")
        await message.delete() 
       
    if message.content.startswith("슨상"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny.")
        await asyncio.sleep(4.0)
        await msg.edit(content="너가 그런말 할때 마다 마음이 아포.. 찢어질것 같애..")      
        await message.delete() 
       
    if message.content.startswith("머중"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny.")
        await asyncio.sleep(4.0)
        await msg.edit(content="너가 그런말 할때 마다 마음이 아포.. 찢어질것 같애..")      
        await message.delete()
       
    if message.content.startswith("개발자"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="삭제해서 미안; 난 이서버 관리자라서..")      
        await message.delete()  
       
    if message.content.startswith("제작자"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="삭제해서 미안; 난 이서버 관리자라서..")      
        await message.delete() 
       
    if message.content.startswith("박정희"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="삭제해서 미안; 난 이서버 관리자라서..")      
        await message.delete() 
       
    if message.content.startswith("전두환"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="삭제해서 미안; 난 이서버 관리자라서..")      
        await message.delete() 
       
    if message.content.startswith("갓카"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny.")
        await asyncio.sleep(4.0)
        await msg.edit(content="너가 그런말 할때 마다 마음이 아포.. 찢어질것 같애..")      
        await message.delete() 
       
    if message.content.startswith("전땅크"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny.")
        await asyncio.sleep(4.0)
        await msg.edit(content="너가 그런말 할때 마다 마음이 아포.. 찢어질것 같애..")      
        await message.delete()
       
    if message.content.startswith("세월호"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny.")
        await asyncio.sleep(4.0)
        await msg.edit(content="너가 그런말 할때 마다 마음이 아포.. 찢어질것 같애..")      
        await message.delete()
       
    if message.content.startswith("518"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny.")
        await asyncio.sleep(4.0)
        await msg.edit(content="너가 그런말 할때 마다 마음이 아포.. 찢어질것 같애..")      
        await message.delete() 
       
    if message.content.startswith("523"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny.")
        await asyncio.sleep(4.0)
        await msg.edit(content="너가 그런말 할때 마다 마음이 아포.. 찢어질것 같애..")      
        await message.delete()
       
    if message.content.startswith("시진핑"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="삭제해서 미안; 난 이서버 관리자라서..")      
        await message.delete()
       
    if message.content.startswith("이승만"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="삭제해서 미안; 난 이서버 관리자라서..")      
        await message.delete() 
       
    if message.content.startswith("어쩌라고"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="왤케 꼬였어?")      
        await message.delete() 
       
    if message.content.startswith("어1쩌"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="왤케 꼬였어?")      
        await message.delete()  
       
    if message.content.startswith("어2쩌"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="왤케 꼬였어?")      
        await message.delete()  
       
    if message.content.startswith("어3쩌"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="왤케 꼬였어?")      
        await message.delete()  
       
    if message.content.startswith("어.쩌"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="왤케 꼬였어?")      
        await message.delete()          
       
       

       
    if message.content.startswith("윤보선"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="아이고..아이고야 ㅠㅜ")      
        await message.delete()  
       
    if message.content.startswith("최규하"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="아이고..아이고야 ㅠㅜ")      
        await message.delete()  
       
    if message.content.startswith("노태우"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="아이고..아이고야 ㅠㅜ")      
        await message.delete()  
       
       
    if message.content.startswith("김영삼"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="아이고..아이고야 ㅠㅜ")      
        await message.delete()  
       
    if message.content.startswith("이명박"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="아이고..아이고야 ㅠㅜ")      
        await message.delete() 
       
    if message.content.startswith("박근혜"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="'내가' 제일 존경하는 분이야. 그녀의 존함을 함부로 부르지마. 대깨문새끼야.")      
        await message.delete()  
       
    if message.content.startswith("김정은"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[난] 이 생명체를 제일 혐오해. 데스노트가 있었으면 좋겠어.")      
        await message.delete() 
       
    if message.content.startswith("푸틴"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="아이고..아이고야 ㅠㅜ")      
        await message.delete() 
       
    if message.content.startswith("펍지"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="아이고..아이고야 ㅠㅜ")      
        await message.delete() 
       
    if message.content.startswith("텐센트"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="아이고..아이고야 ㅠㅜ")      
        await message.delete() 
       
    if message.content.startswith("시2발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      
     
    if message.content.startswith("씨2발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete() 
       
    if message.content.startswith("시3발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()       
     
    if message.content.startswith("씨3발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete() 
       
    if message.content.startswith("시4발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      
     
    if message.content.startswith("씨4발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete() 
       
    if message.content.startswith("시5발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      
     
    if message.content.startswith("씨5발"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete() 
       
    if message.content.startswith("알바"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="아이고..아이고야 ㅠㅜ")      
        await message.delete()    
            
  
       
    if message.content.startswith("응"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()    
       
    if message.content.startswith("니"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      
       
    if message.content.startswith("항공주"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="조용히해. 좀;;")      
        await message.delete()   
       
    if message.content.startswith("띠용"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="조용히해. 좀;;")      
        await message.delete()    
        
    if message.content.startswith("운전면허"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="앞으로 운전면허 언급할 시 05년생 한남 유충인걸로 간주하겠음. 그리고, 한남이 운전면허 따봤자 돼지 목에 진주 목걸이지.")      
        await message.delete()    
        
    if message.content.startswith("운1전1면1허"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="앞으로 운전면허 언급할 시 05년생 한남 유충인걸로 간주하겠음. 그리고, 한남이 운전면허 따봤자 돼지 목에 진주 목걸이지.")      
        await message.delete()  
        
    if message.content.startswith("운3전3면3허"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="앞으로 운전면허 언급할 시 05년생 한남 유충인걸로 간주하겠음. 그리고, 한남이 운전면허 따봤자 돼지 목에 진주 목걸이지.")      
        await message.delete()          
       
    if message.content.startswith("운2전2면2허"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="앞으로 운전면허 언급할 시 05년생 한남 유충인걸로 간주하겠음. 그리고, 한남이 운전면허 따봤자 돼지 목에 진주 목걸이지.")      
        await message.delete()         
 
 
    if message.content.startswith("운.전.면.허"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="앞으로 운전면허 언급할 시 05년생 한남 유충인걸로 간주하겠음. 그리고, 한남이 운전면허 따봤자 돼지 목에 진주 목걸이지.")      
        await message.delete()  
       
    if message.content.startswith("ㄱ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="韩国男人的阴茎是世界上最小的。(ㄱ=阴茎)")      
        await message.delete()        
       
       
       
       
       
    if message.content.startswith("공산주의"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[공산주의]는 사상만 보면 누구라도 혹할수밖에 없어. 하지만, 제대로 된 공산주의 국가가 없잖니.. ")      
        await message.delete() 
       
    if message.content.startswith("공산당"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[공산주의]는 사상만 보면 누구라도 혹할수밖에 없어. 하지만, 제대로 된 공산주의 국가가 없잖니.. ")      
        await message.delete()  
       
    if message.content.startswith("아베"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="조용히해. 좀;;")      
        await message.delete()  
       
    if message.content.startswith("양성"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="조용히해. 좀;;")      
        await message.delete()  
       
    if message.content.startswith("추카추카"):
        msg = await message.channel.send("Doribot detected a stupid expression.")
        await asyncio.sleep(4.0)
        await msg.edit(content="你的母亲被南韩总统强奸了。")      
        await message.delete()      
 
       
    if message.content.startswith("예아"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny.")
        await asyncio.sleep(4.0)
        await msg.edit(content="조용히해. 좀;;")      
        await message.delete()    

       
    if message.content.startswith("장애"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="항상 감사해라. 넌 사지랑 정신이 멀쩡하잖니. 세상엔 불쌍한 사람들이 많단다.")      
        await message.delete()       

       
    if message.content.startswith("훠훠"):
        msg = await message.channel.send("Don't use a term derived from the web community that advocates misogyny.")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()  
       
    if message.content.startswith("흑인"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()      
       
    if message.content.startswith("히스패닉"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()   
       
    if message.content.startswith("동양인"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()  
       

       
    if message.content.startswith("지랄"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete() 
       
    if message.content.startswith("눈깔"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()   
       
    if message.content.startswith("*년"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()   
       
    if message.content.startswith("병*"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()  
       
    if message.content.startswith("ㅈㄹ"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="请不要使用脏话。")      
        await message.delete()    
       
    if message.content.startswith("허버허버"):
        msg = await message.channel.send("Do not use words that cause disputes.")
        await asyncio.sleep(4.0)
        await msg.edit(content="'허버허버'가 남성 혐오 단어면, 보이루는 여성 혐오 단어임?")      
        await message.delete()      

       
    if message.content.startswith("ㅎㅂㅎㅂ"):
        msg = await message.channel.send("Do not use words that cause disputes.")
        await asyncio.sleep(4.0)
        await msg.edit(content="'허버허버'가 남성 혐오 단어면, 보이루는 여성 혐오 단어임?")      
        await message.delete()   
       
    if message.content.startswith("보이루"):
        msg = await message.channel.send("Do not use words that cause disputes.")
        await asyncio.sleep(4.0)
        await msg.edit(content="'보겸하이루~'")      
        await message.delete()   
       
    if message.content.startswith("ㅂㅇㄹ"):
        msg = await message.channel.send("Do not use words that cause disputes.")
        await asyncio.sleep(4.0)
        await msg.edit(content="'보겸하이루~'")      
        await message.delete()  
       
    if message.content.startswith("뻑가"):
        msg = await message.channel.send("Do not use words that cause disputes.")
        await asyncio.sleep(4.0)
        await msg.edit(content="얜 누구야;;시발")      
        await message.delete()     
       
    if message.content.startswith("고기남자"):
        msg = await message.channel.send("Do not use words that cause disputes.")
        await asyncio.sleep(4.0)
        await msg.edit(content="군데..얘는 진짜 누구야?")      
        await message.delete()   
       
    if message.content.startswith("고기냄저"):
        msg = await message.channel.send("Do not use words that cause disputes.")
        await asyncio.sleep(4.0)
        await msg.edit(content="군데..얘는 진짜 누구야?")      
        await message.delete()   
       
    if message.content.startswith("고기냄져"):
        msg = await message.channel.send("Do not use words that cause disputes.")
        await asyncio.sleep(4.0)
        await msg.edit(content="군데..얘는 진짜 누구야?")      
        await message.delete()  
       
    if message.content.startswith("고기넴져"):
        msg = await message.channel.send("Do not use words that cause disputes.")
        await asyncio.sleep(4.0)
        await msg.edit(content="군데..얘는 진짜 누구야?")      
        await message.delete()  
       
    if message.content.startswith("고기넴저"):
        msg = await message.channel.send("Do not use words that cause disputes.")
        await asyncio.sleep(4.0)
        await msg.edit(content="군데..얘는 진짜 누구야?")      
        await message.delete()        
       
 
       
       
       
       
       
       

       
       
       
       
       
       
       
             
     
 
       
        
     
     
    if message.content.startswith("?INTP"):                             
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [논리적인 사색가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '과거에서', value = '배우되, 현재에 살며, 미래에 대한 희망을 가지세요. 그리고 중요한 것은 질문하는 일을 멈추지 않는 것입니다.',inline = False)
        embed.add_field(name='사색가형은', value='전체 인구의 3% 정도를 차지하는 꽤 흔치 않은 성격 유형으로, 이는 그들 자신도 매우 반기는 일입니다. 왜냐하면, 사색가형 사람보다 [평범함]을 거부하는 이들이 또 없기 때문입니다. 이 유형의 사람은 그들이 가진 독창성과 창의력, 그리고 그들만의 독특한 관점과 왕성한 지적 호기심에 나름의 자부심을 가지고 있습니다. 보통 철학자나 사색가, 혹은 몽상에 빠진 천재 교수로도 많이 알려진 이들은 역사적으로 수많은 과학적 발전을 이끌어 내기도 하였습니다.', inline=False)
        embed.add_field(name='연구되지 않은 삶은 의미가 없다!', value='천재적인 이론이나 난해한 논리로 유명한 이들은 다른 성격 유형과 비교하여 가장 논리적인 사람들로 알려져 있습니다.', inline=False)        
        embed.add_field(name = '이들은', value = '사건이나 사물의 어떠한 일련의 연속성에 관심이 많으며, 사람들의 언행에 불일치되는 부분을 집어내 트집 잡는 것을 즐기는데, 이는 거의 취미 수준에 가까울 정도입니다. 때문에 이들에게 거짓말은 하지 않는 것이 좋습니다. 또 한 가지 아이러니한 점은 이들의 얘기를 곧이곧대로 듣지 말고 잘 새겨 들어야 한다는 것입니다. 이는 이들이 솔직하지 않아서가 아니라 아직 채 명확히 규명되지 않은 생각이나 이론에 대하여 얘기하는 경향이 있기 때문입니다. 이들은 상대방을 실질적인 대화 상대로 보는 것이 아니라 그들의 생각이나 이론을 펴기 위한 하나의 대상으로 여깁니다.',inline = False)
        embed.add_field(name='이러한', value='성향 때문에 이들에게 일을 맡기는 게 불안하게 느껴질 수도 있지만, 사실 사색가형 사람보다 문제를 정확히 파악하고 이를 둘러싸고 있는 요소를 낱낱이 파헤쳐 독창적이며 실행 가능한 해결책을 찾아내는 데 더 열성적이고 뛰어난 사람은 없습니다. 단, 이들에게서 업무 진행 상황에 따른 보고서 따위를 제출받기를 기대하지는 않는 게 좋습니다. 이 성격 유형의 사람은 실질적인 하루하루 업무나 유지에는 관심이 없기 때문입니다. 하지만 일단 이들의 천재성과 잠재력이 활개 칠 수 있는 환경이 조성되면 이들은 통찰력 있고 편향되지 않은 해결책을 찾는 데 그들이 가진 모든 시간과 에너지를 모두 쏟아부을 것입니다.', inline=False)
        embed.add_field(name='지혜는 호기심으로부터 시작', value='이런저런 몽상에 사로잡혀 있는 듯한 모습을 자주 보이는 이들은 한시도 쉼 없이 생각에 몰두합니다. 심지어는 아침에 눈을 뜰 때조차도 쉴 새 없이 쏟아지는 아이디어와 함께 하루를 시작합니다. 머릿속에서 끊임없는 벌어지는 논쟁과 생각으로 수심에 가득 차 보이거나 혼자 동떨어져 있어 보이기도 하지만, 이들과 비슷한 관심사를 가진 사람 혹은 친밀한 관계의 이들과 있을 때면 편안하고 밝은 모습을 보입니다. 이와 대조적으로 낯선 이들과 있을 때는 극도로 수줍어하며, 만일 이들이 논리적으로 내린 결론이나 이론이 상대방으로부터 비판을 받거나 하는 경우가 생기면 가벼운 농담에도 호전적인 태세를 보이기도 합니다.', inline=False)   
        embed.add_field(name='특히나', value='흥분된 상태에서 이야기할 때에는 대화에 일관성이 떨어지기도 하는데, 이는 가장 최근 정립한 이론이 결론에 도달하기까지 일련의 논리적 연결 고리를 모두 설명하려 들기 때문입니다. 이들은 또한 상대방이 그들의 논리를 충분히 이해하지 못하였음에도 쉽게 풀어 설명하거나 하지 않은 채 대화를 다른 주제로 옮기기도 합니다.', inline=False)          
        embed.add_field(name='주관적인 관점', value='이나 감정에 치우쳐 사고하는 사람과 비교해보면 아마도 이들의 사고 과정을 보다 잘 이해할 수 있을 것입니다. 가령 매우 정교하고 복잡한 시계 작동법을 창의적으로 사고하되, 가능한 한 하나의 사실도 빠짐없이 논리적으로 가장 합당한 결론에 이르게 설명한다고 상상해 보십시오. 이것이 바로 사색가형 사람이 사고하는 방식입니다. 이들은 감정 망치가 이들의 사고방식에 훼방 놓는 것을 한치도 용납하지 않습니다.', inline=False) 
        embed.add_field(name='세상을 변화시키고자 하는 당신, 먼저 자신부터 변화하십시오!', value='또한 이들은 다른 이의 감정 섞인 불평이나 불만을 전혀 이해하지 못하기 때문에 친구들은 그들에게서 어떠한 정서적인 위로나 위안을 받지 못합니다. 더욱이 사색가형 사람은 근본적으로 내재되어 있는 문제 해결을 위한 논리적인 해결책을 제안하는 것을 선호하는데, 이는 감성적인 성향의 사람과는 대조되는 부분입니다. 이러한 이들의 성향은 나아가 저녁 모임 계획이나 결혼 준비와 같은 기타 사회적 만남이나 활동에도 영향을 미치는데 이들은 기본적으로 지나치리만치 독창성과 효율적인 결과를 좇는 경향이 있습니다.', inline=False) 
        embed.add_field(name='이들의', value='앞길을 가로막는 한 가지 장애물은 계속해서 드는 실패에 대한 두려움입니다. 사색가형 사람은 혹 자신이 중요한 퍼즐 조각을 놓친 것은 아닌지, 혹 이로 인해 자신이 정체되거나 그들의 지식이 아직 실질적으로 적용되지 않은 무형의 세계에서 길을 잃는 것은 아닌지를 걱정하며 자신의 생각이나 이론을 끊임없이 재평가하는 경향이 있습니다. 자기 자신에 대한 의구심을 극복하는 것이 이들이 직면한 가장 큰 과제입니다. 하지만 그것이 크든 작든, 이들이 가진 지적 능력에서 말미암은 이들의 도전은 그 자체만으로도 세상에 큰 가치를 가져옵니다.', inline=False) 
        embed.add_field(name='논리적인 사색가형에 속하는 유명인', value='빌 게이츠, 알버트 아인슈타인, 아이작 뉴턴, 블레이즈 파스칼, 네오(매트릭스), 브루스 배너(헐크/히어로)  ', inline=False) 
        await message.channel.send(channel,embed=embed) 


    if message.content.startswith("?INFP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [열정적인 중재자]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '중재자형 사람은', value = '최악의 상황이나 악한 사람에게서도 좋은 면만을 바라보며 긍정적이고 더 나은 상황을 만들고자 노력하는 진정한 이상주의자입니다. 간혹 침착하고 내성적이며 심지어는 수줍음이 많은 사람처럼 비추어지기도 하지만, 이들 안에는 불만 지피면 활활 타오를 수 있는 열정의 불꽃이 숨어있습니다. 인구의 대략 4%를 차지하는 이들은 간혹 사람들의 오해를 사기도 하지만, 일단 마음이 맞는 사람을 만나면 이들 안에 내재한 충만한 즐거움과 넘치는 영감을 경험할 수 있을 것입니다.',inline = False)
        embed.add_field(name='이들은', value='논리나 단순한 흥미로움, 혹은 인생의 실용적인 부분이 아닌 그들 나름의 원리원칙에 근거하여 사고하고 행동합니다. 더욱이 성취에 따르는 보상이나 그렇지 못할 경우에 생길 수 있는 불이익 여부에 상관없이 순수한 의도로 인생의 아름다움이나 명예 그리고 도덕적 양심과 미덕을 좇으며 나름의 인생을 설계해 나갑니다. 그리고 그러한 본인들의 생각과 행동에 자부심을 느끼기도 하는데, 이는 마땅한 일입니다. 하지만 모든 사람이 그들의 생각 뒤에 숨은 동기나 의미를 정확히 파악하지는 못하는데, 이는 자칫 이들을 외톨이로 만들 수도 있습니다.', inline=False)
        embed.add_field(name='금', value='이라고 해서 다 반짝이는 것은 아니며, 헤매고 다니는 자가 모두 길을 잃은 것은 아닙니다. 오래되었어도 강한 것은 시들지 않으며, 깊게 뻗은 뿌리에는 서리가 닿지 않습니다.', inline=False)        
        embed.add_field(name = '자기 자신에 대한 깊은 통찰력', value = '중재자형 사람이 가진 가장 큰 장점은 적절한 은유나 이야기를 통해 그들의 생각을 상징화하여 다른 이들과 깊이 있는 의사소통을 한다는 점입니다. 이러한 직관적인 성향은 이들로 하여금 더 창의적인 일에 몰두하게 합니다. 이를 비추어보면 여러 유명 시인이나 작가, 그리고 배우가 이 성격 유형에 속하는 것이 그리 놀랍지만은 않습니다. 중재자형 사람에게 있어 본인 자신에 대한 이해뿐만 아니라 자신이 속한 세상을 이해하는 것이 매우 중요한데, 이들은 종종 작품에 자신을 투영시켜 세상을 탐구하기도 합니다.',inline = False)
        embed.add_field(name='자기표현에', value='특출난 재주를 가지고 있는 이 유형의 사람은 아름다움에 대한 고찰이나 그들이 가지고 있는 비밀을 은유적인 방법이나 작품 속 허구 인물을 등장시켜 표현하기도 합니다.', inline=False)
        embed.add_field(name='이들은 또한', value='뛰어난 언어적 소질을 보이는데 이는 비단 모국어뿐 아니라 제2외국어(심지어는 제3외국어까지!)를 습득하는 데에까지 재능을 보입니다. 이들의 뛰어난 의사소통 능력은 사람들 간의 화합을 도모하며, 그들이 목표한 바를 달성하기 위해 나아가는 데 도움을 줍니다.', inline=False)   
        embed.add_field(name='다수가 아닌 소수에 더 많은 관심', value='다른 외향적 성격 유형에 속하는 사람과 달리, 중재자형 사람은 소수의 몇몇, 그리고 의미 있다고 판단되는 한 가지 목표에만 관심을 기울이는 등 한 번에 많은 일을 달성하려 하지 않습니다. 만일 모든 사회악을 근절하는 데 그들이 할 수 있는 일이 한정되어 있음을 깨닫는 순간, 이들의 에너지는 빛을 잃고 좌절감을 맛보거나 처한 상황에 압도되기도 합니다. 그리고 이는 밝은 장밋빛 미래를 함께 꿈꾸며 가까이에서 지켜보는 다른 이들의 마음을 안타깝게 하기도 합니다.', inline=False)          
        embed.add_field(name='자칫하면', value='중재자형 사람은 선(善)을 위해 하던 행위를 갑자기 멈추거나 하루하루 일상생활을 영위하는 일조차 등한시할 수도 있습니다. 이들은 종종 깊은 생각의 나락으로 자신을 내몰아 이론적 가설이나 혹은 철학적 논리에 빠지기도 하는데, 꾸준한 관심을 가지고 이들을 지켜보지 않으면 이들은 연락을 끊고 [은둔자] 생활을 하기도 합니다. 그리고 추후 이들을 현실 밖으로 다시 돌아오게 하기까지 주위 사람들의 많은 에너지와 노력을 필요로 합니다.', inline=False) 
        embed.add_field(name='다행인 것은', value='깊은 나락에 빠져 있던 이들도 봄이 오면 다시금 봉오리를 피우는 꽃과 같이 이들의 애정 어린 마음과 창의적인 생각, 이타주의적이며 이상주의적인 생각 역시 제자리로 돌아와 자신뿐 아니라 곁에서 지켜보는 이들로 하여금 뿌듯함에 미소 짓게 합니다. 그리고 다시금 사실적 논리나 현실적인 유용성의 관점이 아닌 넘치는 영감과 인간애, 친절함, 그리고 따뜻한 마음으로 세상을 바라봅니다.', inline=False) 
        embed.add_field(name='열정적인 중재자형에 속하는 유명인', value='J.R.R 톨킨, 윌리엄 쉐익스피어, 톰 히들스턴(한국에서의 그는 MCU의 빌런이자 아스가르드의 신, 천둥의 신 토르의 동생, 요툰헤임의 왕족, 로키역으로 유명함), 줄리아 로버츠, 조니 뎁, 프로도 배긴즈(반지의제왕), 아웬(반지의제왕),   ', inline=False) 
        await message.channel.send(channel,embed=embed) 
        

    if message.content.startswith("?ISTJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [청렴결백한 논리주의자]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '내가 본 바에 의하면', value = '임무를 수행함에 있어 한 명이면 족한 일을 둘이서 수행하면 될 일도 안되거니와, 셋 이상이 하는 경우에는 일이 전혀 성사되지 않더군.',inline = False)
        embed.add_field(name='논리주의자형은 ', value='가장 다수의 사람이 속하는 성격 유형으로 인구의 대략 13%를 차지합니다. 청렴결백하면서도 실용적인 논리력과 헌신적으로 임무를 수행하는 성격으로 묘사되기도 하는 이들은, 가정 내에서뿐 아니라 법률 회사나 법 규제 기관 혹은 군대와 같이 전통이나 질서를 중시하는 조직에서 핵심 구성원 역할을 합니다. 이 유형의 사람은 자신이 맡은 바 책임을 다하며 그들이 하는 일에 큰 자부심을 가지고 있습니다. 또한, 목표를 달성하기 위해 시간과 에너지를 허투루 쓰지 않으며, 이에 필요한 업무를 정확하고 신중하게 처리합니다.', inline=False)
        embed.add_field(name='뭐든', value='쉽게 가정하여 결론 내리지 않는 이들은, 주변을 객관적으로 분석하고 사실에 입각하여 현실적으로 실행 가능한 계획을 세우는 것을 선호합니다. 허튼짓하는 것을 무엇보다도 싫어하는 사람으로 결정을 내린 후에는 목표를 달성하는 데 필요한 사실을 열거함으로써 다른 이들로 하여금 이를 재빨리 인지하여 즉시 실행해 옮기기를 독려합니다. 특히나 우유부단한 것을 몹시 싫어하며, 혹 결정 내린 실행안이 비현실적인 이유로 장애에 부딪혔을 때 쉬이 인내심을 잃기도 하는데, 특히 목표 달성에 필요한 핵심 세부사항을 놓치는 경우에는 더욱 그러합니다. 만일 마감 시간은 가까워져 오는데 논의가 성사되지 않은 채 시간만 질질 끄는 경우, 이들의 불편함 심기가 얼굴에 그대로 나타나기도 합니다.', inline=False)        
        embed.add_field(name = '뱉은 말에 대한 책임과 평판', value = '논리주의자형 사람이 무언가를 하겠다고 하면 얼마나 많은 희생이 따르던지 자신이 한 말에 책임을 지고자 기어이는 해내고야 맙니다. 이런 그들이기에 자신이 내뱉은 말에 책임을 지지 않는 이들을 보면 어쩔 줄 몰라 합니다. 태만과 부도덕의 조합만큼 논리주의자형 사람의 적이 되는 가장 빠른 지름길도 없을 것입니다. 때문에 이들은 혼자 일하는 것을 선호하며, 대개 일을 진행하는 데 직장 내 토의를 거치거나 다른 이들의 견해를 들을 필요 없이 자신만의 목표를 설정하고 달성을 가능케 하는 어느 정도의 지위나 권한을 가지고 있는 경우가 많습니다.',inline = False)
        embed.add_field(name='예리하며', value='사실에 근거하여 사고하는 경향을 가지고 있는 이들은 자율적으로 스스로 알아서 행동하고 책임지기를 원합니다. 이 때문에 이들은 누군가에게 의존하는 것은 약자의 행동이라고 여깁니다. 임무 달성을 위한 열정과 책임감, 그리고 오점 하나 없는 청렴한 이들의 성격으로 하여금 이들을 종종 이러한 오류에 쉽게 빠지게 합니다.', inline=False)
        embed.add_field(name='이들의', value='청렴결백한 성격은 논리주의자형 사람을 정의하는 핵심사항으로, 이는 그들이 생각하는 것 이상으로 중요한 부분입니다. 얼마나 많은 희생이 따르든 이들은 일단 정해진 체계나 지침을 고수하며, 비록 사실을 있는 그대로 밝히는 것이 결과적으로 더 큰 분란을 야기할지라도 자신의 잘못을 시인하고 사실을 밝히고자 합니다. 논리주의자형 사람에게 있어 감정적인 고려보다 정직함이 보다 우선시 되기 때문입니다. 때로 이러한 그들의 대담한 행보는 사람들에게 냉정하고 로봇 같다는 잘못된 인상을 심어 주기도 합니다. 감정이나 애정을 밖으로 표출하는 것에 익숙하지 않은 이들은 혹 사람들로부터 냉혈인이라든지, 더 심하게는 ‘감정 자체가 있느냐’와 같은 말을 듣기도 하는데 이에 깊은 상처를 받기도 합니다.', inline=False)   
        embed.add_field(name='백해무익한 무리와 있느니 차라리 혼자가 낫다', value='논리주의자형 사람의 헌신적인 성격은 매우 긍정적인 자질로 이들로 하여금 많은 것을 이루게 합니다. 하지만 이는 동시에 이들의 약점이 되기도 하는데, 간혹 비양심적인 사람들은 이러한 이들의 약점을 이용하기도 합니다. 안전하며 안정된 삶을 추구하는 논리주의자형 사람은 일이 원활하게 돌아갈 수 있도록 맡은 바 임무를 충실히 수행합니다. 뒤치다꺼리를 마다치 않는 이들의 성향을 아는 동료나 주위 사람들은 간혹 이들에게 책임을 전가하는 경우가 있습니다. 더욱이 개인적인 견해가 아닌 사실만을 얘기하고자 하는 이들의 성향 때문에 정확히 사실을 밝혀 낼 증거가 충분히 모일 때까지 시간이 오래 걸리기도 합니다.', inline=False)          
        embed.add_field(name='이들은', value='그들 자신 또한 챙기고 돌보아야 할 필요가 있음을 잊지 말아야 합니다. 갈수록 기대기만 하는 이들에게 언제고 싫은 내색 한번 않는 논리주의자형 사람들이기 때문에 일단 감정의 골이 쌓여 터진 후 돌아오기 늦어버리는 상황을 초래하기 전 안정과 효율성 추구를 위한 완강하고 헌신적인 이들의 성격을 활용하여 장기간 목표를 달성하기 위한 절충점을 찾아야 합니다. 활기차고 명료하며 안정된 삶을 추구하는 이들의 성향을 진심으로 이해하고 보듬으며 이들이 가진 단점을 보완해주는 동료나 배우자를 만난다면, 이들은 안정을 추구하는 자신의 성향으로 하여금 일을 순리대로 잘 돌아가게 하는 데 지대한 역할을 하고 있다는 생각에 큰 만족감을 느낄 것입니다.', inline=False) 
        embed.add_field(name='청렴결백한 논리주의자형에 속하는 유명인', value='엥겔라 마르켈, 나탈리 포트만, 안토니 홉킨스, 조지 워싱턴, 조지.H.W 부시, 에드워드 스타크(왕좌의게임), 허마이오니 진 그레인저(오역:헤르미온느 진 그레인저, 주인공 해리포터의 절친이자 로날드 위즐리의 아내(허마이오니 진 위즐리), 그리고 그리핀도르!', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("?ISFJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [용감한 수호자]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '사랑은', value = '나눌수록 커집니다. 다른 이에게 나누어 주면 줄수록 당신에게 돌아오는 사랑 또한 더욱 커집니다.',inline = False)
        embed.add_field(name='수호자형', value='사람은 꽤 독특한 특징을 가지고 있는데, 이 유형에 속하는 사람은 이들을 정의하는 성격 특성에 꼭 들어맞지 않는다는 점입니다. 타인을 향한 연민이나 동정심이 있으면서도 가족이나 친구를 보호해야 할 때는 가차 없는 모습을 보이기도 합니다. 조용하고 내성적인 반면 관계술에 뛰어나 인간관계를 잘 만들어갑니다. 안정적인 삶을 지향하지만 이들이 이해받고 존경받는다고 생각되는 한에서는 변화를 잘 수용합니다. 이처럼 수호자형 사람은 한마디로 정의 내리기 힘든 다양한 성향을 내포하고 있는데, 이는 오히려 그들의 장점을 승화시켜 그들 자신을 더욱 돋보이게 합니다.', inline=False)
        embed.add_field(name='수호자형 사람은', value='무엇을 받으면 몇 배로 베푸는 진정한 이타주의자로 열정과 자애로움으로 일단 믿는 이들이라면 타인과도 잘 어울려 일에 정진합니다.', inline=False)        
        embed.add_field(name = '약', value = '13%로 꽤 높은 인구 비율을 차지하는데, 인구 대다수를 차지하는 데 있어 이들보다 더 나은 성격 유형은 아마 없을 것입니다. 이들은 종종 의료 부분이나 학문, 혹은 사회단체와 같이 오랜 역사나 전통과 관련된 분야에 종사합니다.',inline = False)
        embed.add_field(name='수호자형 중', value='특히 신중한 성향을 가진 사람은 완벽주의자만큼이나 세심하고 꼼꼼한 면모를 보이기도 합니다. 간혹 일을 지연하는 경우가 있기는 하지만, 그렇다고 일을 시간 내에 마치지 않는 것은 아닙니다. 이들은 맡은 바 일에 책임감을 가지고 업무에 임하며, 회사나 가정에서 그들의 기대치를 넘어 주위 사람들을 만족시키고자 최선을 다합니다', inline=False)
        embed.add_field(name='공(功)을 공(功)이라 말할 수 있는 용기', value='수호자형 사람은 그들의 업적이나 실적을 다른 사람들이 알아차리게 하는 데 어려움을 느낍니다. 이들은 종종 자신이 이룬 성취를 과소평가하는 경향이 있는데, 이러한 겸손한 태도로 종종 다른 이들로부터 존경을 받기도 하는가 하면, 이기적이고 냉소적인 사람들은 이들의 겸손함을 역으로 이용하여 수호자형 사람이 세운 공을 자신의 것으로 돌리는 경우도 있습니다. 자신감과 열정을 지키기 위해서는 이들도 [아니요]라고 말해야 할 때와 자기 자신을 방어해야 할 때를 정확히 인지할 필요가 있습니다.', inline=False)   
        embed.add_field(name='내성적이면서', value='신기하게도 사회적인 성향을 가지고 있기도 한 이들은 좋은 기억력을 자랑합니다. 뛰어난 기억력으로 단순히 데이터나 사소한 정보를 기억하는 것이 아니라, 만나는 사람들이나 그들과 관련한 소소한 사항들을 모두 기억해 놓습니다. 상상력과 타고난 섬세함으로 그들의 자애로운 마음을 표현함으로써 상대방의 가슴을 진심으로 울리는 데 이들보다 더 천부적으로 소질이 있는 이들도 없을 것입니다. 이는 함께 일하는 동료들 사이에서도 자명한 일로, 이들은 동료를 가까운 친구로 여깁니다. 그러나 뭐니 뭐니 해도 이들의 애정과 사랑이 환하게 꽃을 피우는 곳은 바로 가정 내에서 일 것입니다.', inline=False)          
        embed.add_field(name='해야 할 땐 과감히', value='수호자형 사람은 가치 있다고 여기는 일이 마무리되지 않고 있으면 게으르게 가만히 앉아만 있지 못하는 이타주의적 성격을 가지고 있습니다. 다른 내향적인 성격의 사람들과 견주어 봐도 이들만큼 타인과 친밀한 관계를 유지하는 이들이 없습니다. 또한 서로 응원하고 힘을 북돋워 주며 화목한 가정을 꾸려 나가는 것을 옆에서 지켜보는 것 자체가 가족에게는 큰 축복이 아닐 수 없습니다. 이들은 화려한 스포트라이트를 받는 것을 불편해하며, 다른 이들과 함께 달성한 업무에 있어 공을 인정받는 데에 어색해하기도 합니다. 하지만 이들이 그들 자신의 노력을 알리는 데 조금 더 열중한다면 다른 유형의 사람이었다면 그저 상상만 하고 있을 법한 일을 성취해 냄으로써 더 큰 자신감을 얻을 수 있을 것입니다.', inline=False) 
        embed.add_field(name='용감한 수호자형에 속하는 유명인', value='엘리자베스 2세 여왕(영국), 앤 해서웨이, 셀레나 고메즈, 케이틀린 스타크(왕좌의게임), 감지네 샘와이즈(반지의제왕), 닥터 왓슨(셜록홈즈), 캡틴 아메리카(히어로), ', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("?ENFJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [정의로운 사회운동가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '당신이', value = '현재하는 사소한 행위는 잔잔한 물결처럼 서서히 퍼져나가 모든 이에게 영향을 줍니다. 당신의 마음가짐이 다른 이의 가슴에 불을 지필 수도, 근심을 초래할 수도 있습니다. 당신의 숨소리가 사랑의 빛을 뿜어낼 수도, 우울함으로 온 방안을 어둡게 만들 수도 있습니다. 당신의 시선이 즐거움을 선사할 수도 있으며, 당신의 언어가 자유를 향한 열망을 독려할 수도 있습니다. 당신의 행동 하나하나가 다른 이들의 생각과 마음을 열 수 있습니다.',inline = False)
        embed.add_field(name='사회운동가형 사람은', value='카리스마와 충만한 열정을 지닌 타고난 리더형입니다. 인구의 대략 2%가 이 유형에 속하며, 정치가나 코치 혹은 교사와 같은 직군에서 흔히 볼 수 있습니다. 이들은 다른 이들로 하여금 그들의 꿈을 이루며, 선한 일을 통하여 세상에 빛과 소금이 될 수 있도록 사람들을 독려합니다. 또한, 자신뿐 아니라 더 나아가 살기 좋은 공동체를 만들기 위해 사람들을 동참시키고 이끄는 데에서 큰 자부심과 행복을 느낍니다', inline=False)
        embed.add_field(name='진심으로 사람을 믿고 이끄는 지도자', value='우리는 대개 강직한 성품을 가진 이에게 마법처럼 끌리곤 합니다. 사회운동가형 사람은 진정으로 타인을 생각하고 염려하며, 그들이 필요하다고 느낄 때면 발 벗고 나서서 옳은 일을 위해 쓴소리하는 것을 마다하지 않습니다. 다른 이들과 별 어려움 없이 잘 어울리며, 특히 사람들과 직접 얼굴을 보고 의사소통하는 것을 좋아합니다. 이들에게 내재되어 있는 직관적 성향은 이성적 사실이나 정제되지 않은 인간의 본래 감정을 통하여 다양한 사람의 성격을 더 잘 파악하고 이해하게 합니다. 타인의 의도나 동기를 쉽게 파악 후 이를 그와 개인적으로 연관 짓지 않으며, 대신 특유의 설득력 있는 웅변 기술로 함께 추구해야 할 공통된 목표를 설정하여 그야말로 최면에 걸린 듯 사람들을 이끕니다.', inline=False)        
        embed.add_field(name = '진심으로', value = '마음에서 우러나 타인에게 관심을 보이는 이들이지만 간혹 도가 지나쳐 문제가 될 때도 있습니다. 일단 사람을 믿으면 타인의 문제에 지나치리만치 관여하는 등 이들을 무한 신뢰하는 경향이 있습니다. 다행히도 이들의 진심 어린 이타주의적 행동은 다른 이들로 하여금 더 나은 사람이 될 수 있도록 독려한다는 차원에서 자기 계발을 위한 자아실현 기제로 작용하기도 합니다. 하지만 자칫 잘못하면 이들의 지나친 낙관주의는 되려 변화를 모색하는 이들의 능력 밖이거나 그들이 도울 수 있는 범주를 넘어서는 일이 될 수도 있습니다.',inline = False)
        embed.add_field(name='사회운동가형 사람이', value='경험할 수 있는 또 다른 오류는 이들이 그들 자신 감정을 지나치게 투영하고 분석한다는 점입니다. 다른 사람의 문제에 지나치리만치 깊이 관여하는 경우, 자신의 잘못에서 비롯된 일이 아님에도 불구하고 타인의 문제를 마치 본인의 문제로 여겨 자칫하면 정서적 심기증(hypochondria)과 같은 증상을 보일 수도 있습니다. 더욱이 타인이 문제를 해결하는 데 한계에 도달하였을 때 이를 해결하는 데 자신이 어떠한 도움이 될 수 없음에 딜레마에 빠지기도 합니다. 이러한 오류를 범하지 않기 위해서는 사회운동가형 사람은 그 상황에서 한발 뒤로 물러나 본인이 느끼는 감정과 타인의 문제를 객관적으로 분리해 다른 각도에서 바라볼 필요가 있습니다.', inline=False)
        embed.add_field(name='사회정의 구현을 위해 어려움에 맞서 싸우는 이들', value='사회운동가형 사람은 말과 행동이 일치하며, 타인을 진심으로 대합니다. 중독성 강한 이들 특유의 열정으로 사람들 간의 화합을 도모하고 변화를 이끌 때 이들은 그 어떤 때보다도 큰 행복을 느낍니다.', inline=False)   
        embed.add_field(name='사회운동가형의', value='과도한 이타주의적 성격은 자칫하면 되레 문제를 야기하기도 합니다. 이들은 그들이 옳다고 믿는 생각이나 이념 실현을 위해 다른 이를 대신하여 총대를 메는 것을 두려워하지 않습니다. 이를 볼 때 다수의 영향력 있는 정치인이나 지도자가 이 유형에 속하는 것이 어찌 보면 당연한지도 모릅니다. 경제적 부를 창출하기 위해 나라를 이끄는 한 국가의 원수에서부터 버거운 경기를 승리로 이끄는 어린이 야구팀 코치에 이르기까지 이들은 더 밝은 미래 구현을 위해 앞장서서 사람들을 이끄는 것을 좋아합니다.', inline=False)          
        embed.add_field(name='정의로운 사회운동가형에 속하는 유명인', value='버락 오바마, 벤 애플렉, 제니퍼 로렌스, 모피어스(매트릭스), 오라클(매트릭스), ', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("?ENTP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [뜨거운 논쟁을 즐기는 변론가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '가시밭길이더라도', value = '자주적 사고를 하는 이의 길을 가십시오. 비판과 논란에 맞서서 당신의 생각을 당당히 밝히십시오. 당신의 마음이 시키는 대로 하십시오. [별난 사람]이라고 낙인찍히는 것보다 순종이라는 오명에 무릎 꿇는 것을 더 두려워하십시오. 당신이 중요하다고 생각하는 이념을 위해서라면 온 힘을 다해 싸우십시오.',inline = False)
        embed.add_field(name='변론가형 사람은 ', value='타인이 믿는 이념이나 논쟁에 반향을 일으킴으로써 군중을 선동하는 일명 선의의 비판자입니다. 결단력 있는 성격 유형이 논쟁 안에 깊이 내재한 숨은 의미나 상대의 전략적 목표를 꼬집기 위해 논쟁을 벌인다고 한다면, 변론가형 사람은 단순히 재미를 이유로 비판을 일삼습니다. 아마도 이들보다 논쟁이나 정신적 고문을 즐기는 성격 유형은 없을 것입니다. 이는 천부적으로 재치 있는 입담과 풍부한 지식을 통해 논쟁의 중심에 있는 사안과 관련한 그들의 이념을 증명해 보일 수 있기 때문입니다.', inline=False)
        embed.add_field(name='여기서', value='한 가지 흥미로운 사실은 변론가형 사람은 고집스러우리만치 솔직하기도 하지만 이들이 믿고 관철하는 사안이 아님에도 불구하고 타인의 입장에서 진실 규명을 위해 지칠 줄 모르고 논쟁을 벌인다는 점입니다.', inline=False)        
        embed.add_field(name = '논쟁을', value = '벌이는 주체이자 선의의 비판자로서 이들은 타인의 이성적인 논리를 보다 잘 이해하고 있을 뿐 아니라, 상대편의 관점의 차이도 정확히 꿰뚫어 봅니다.',inline = False)
        embed.add_field(name='단,', value='이를 상호 존중과 이해를 통해 협력을 끌어내는 외교형 사람의 특질과 혼동하지 말아야 합니다. 끊임없이 진리와 지식을 좇는 변론가형 사람들에게 있어 공격과 방어를 통해 타인의 생각이나 이념을 다양한 각도에서 바라보며 해답을 찾는 것보다 더 좋은 방법은 없을 것입니다.', inline=False)
        embed.add_field(name='정해진 법칙은 없습니다 – 뭐가 됐든 성취가 우리의 목적!', value='약자의 입장에서 다수가 받아들인 사안에 의문을 제기함으로써 희열을 느끼기도 하는 이들은, 이러한 성향으로 인해 현존하는 제도를 재고하게 하거나 체제 자체를 흔들어 새로운 방안을 모색하게 합니다. 하지만 변론가형 사람은 이러한 새 방안을 실행하는 데 필요한 일상적인 업무를 처리하는 데에는 영 소질이 없습니다. 이리저리 머리를 굴려 다양한 아이디어를 제안하거나 넓은 안목으로 사고하는 것을 좋아하기는 하지만, 정작 지루하고 고단한 업무를 맡기면 무슨 수를 써서라도 빠져나갈 궁리를 합니다. 이 성격 유형은 인구의 대략 3%에 해당하는데, 이는 딱 적당한 비율입니다. 일단 이들이 아이디어를 낸 후 뒤로 물러서 있으면, 다수의 근면하고 꼼꼼한 성격 유형 사람이 나머지 일을 맡아 처리하면 될 테니까요.', inline=False)   
        embed.add_field(name='논쟁을 좋아하는 변론가형 사람의', value='성격상 이들은 간혹 문제를 야기하기도 합니다. 때에 따라 이들의 성향이 유익하게 작용할 때도 있지만, 간혹 다른 사람의 신경을 건드리기도 하는데 가령 예를 들어 미팅 시 상사의 제안에 대놓고 의구심을 표한다든지, 혹 가족이나 친구가 하는 말에 조목조목 따지는 등과 같은 경우입니다. 이들의 굽힐 줄 모르는 솔직함이 한 목 더 거들기도 하는데, 이들 성향 자체가 말을 예쁘게 순화시켜 하지도 않거니와, 타인에게 세심하지 못한 사람이라고 비추어지는 것에 전혀 개의치 않아 하기 때문입니다. 비슷한 사고와 성향을 가진 사람과는 별 탈 없이 잘 어울립니다. 하지만 마찰을 원치 않는 예민한 성격의 사람이나 다양한 성격의 사람이 한데 어울려 사는 우리 사회는 일반적으로 사람들 간의 배려나 조화를 중요시 여깁니다. 상대방이 혹 불쾌해할 수 있거나 받아들이기 힘든 사안인 경우 필요하다면 선의의 거짓말을 하는 것이 더 나을 수도 있음을 기억해야 합니다.', inline=False)          
        embed.add_field(name='이는', value=' 변론가형 사람에게 어려운 일로 자기 생각과 감정을 잠시 뒤로한 채 타인의 다른 관점을 헤아릴 때면, 비록 의도하지 않았다 하더라도 따지기 좋아하는 이들의 성격 때문에 사람들과의 관계에 금이 갔다는 생각에 속상해하기도 합니다. 다른 이들을 대할 때 그들이 받은 만큼만 하는 스타일인 변론가형 사람은 쓸데없이 아량을 베풀거나 빙빙 돌려 말하는 것을 싫어합니다. 특히 누군가에게 부탁할 필요가 있을 때는 더욱 그러합니다. 미래를 내다보는 비전과 넘치는 자신감, 풍부한 지식, 그리고 날카롭지만 분별력 있는 입담으로 타인에게 우러름을 받기도 하지만, 깊은 인간관계나 연인 관계를 다지는 데에는 이러한 이들의 자질이 충분히 발휘되지 못합니다.', inline=False) 
        embed.add_field(name='배려 있는 논쟁으로 타협에 이르는 지혜', value='변론가형 사람의 본 긍정적 자질과 성격을 충분히 활용하기 위해서는 다른 성격 유형의 사람들에 비해 더 많은 시간과 노력이 필요합니다. 독립적인 사고와 지식, 그리고 자유분방한 사고는 이들이 주체가 되어 이끌어 나가거나 혹은 이들을 필요로 하는 상황에서는 엄청난 가치를 발하지만, 그러기까지 본인들 자신의 꾸준한 노력과 시도가 선행되어야 합니다.', inline=False) 
        embed.add_field(name='일단', value='이 고지에 올라선 후라면 이들은 그들이 내세우는 이념이 빛을 발하기 위해서 그들의 생각에 살을 붙여 줄 다른 이들의 도움이 필요함을 잊지 말아야 합니다. 다른 이들과의 타협점을 찾기 위해 노력하는 것이 아닌 그저 논쟁에서 [승리]하는 데에만 치중한다면, 이들은 단순히 그들이 성공하는 데 필요한 지원군이 충분히 없다고 치부해 버리고 말 것입니다. 선의의 비판자 역할을 성실히 잘 수행하는 변론가형 사람들은 이성적 사고를 통한 발전을 도모하는 동시에, 타인의 감성적인 부분에 대한 이해와 배려 있는 논쟁으로 타협에 이르는 것이 그들에게 가장 어렵지만 동시에 가장 보람된 일임을 깨닫게 될 것입니다.', inline=False)         
        embed.add_field(name='뜨거운 논쟁을 즐기는 변론가형에 속하는 유명인', value='마크 트웨인, 톰 행크스, 토마스 에디슨, 잭 스패로우 선장, 조커(배트맨 세계관의 빌런, [뭐가 그리 심각해?-다크나이트 중-], [나의 죽음이 나의 삶보다 가취있기를.-조커 중-]', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("?ENTJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [대담한 통솔자]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '당신에게 ', value = '주어진 시간은 한정되어 있습니다. 그러니 다른 이의 삶을 사느라 시간을 낭비하지 마세요. 다른 사람의 생각에서 빚어진 삶에 방식에 맞추는 함정에 빠지지 마세요. 다른 사람들이 내는 의견이나 생각이 당신의 목소리에 귀 기울이는 것을 방해하는 소음이 되지 않게 하세요. 그리고 무엇보다 중요한 것은, 당신의 마음과 직관을 굳건히 믿고 따라갈 수 있는 용기를 가지는 것입니다. 이야말로 당신이 진정으로 원하는 것이 무엇인지 정확히 알고 있기 때문입니다. 그 외 다른 것은 모두 부차적일 뿐입니다.',inline = False)
        embed.add_field(name='통솔자형 사람은', value='천성적으로 타고난 리더입니다. 이 유형에 속하는 사람은 넘치는 카리스마와 자신감으로 공통의 목표 실현을 위해 다른 이들을 이끌고 진두지휘합니다. 예민한 성격의 사회운동가형 사람과 달리 이들은 진취적인 생각과 결정력, 그리고 냉철한 판단력으로 그들이 세운 목표 달성을 위해 가끔은 무모하리만치 이성적 사고를 하는 것이 특징입니다. 이들이 인구의 단 3%에 지나지 않는 것이 어쩌면 다행일 수도 있습니다. 그렇지 않으면 인구 대다수를 차지하는 소심하고 섬세한 성향의 사람들이 모두 주눅 들어 살지도 모르니까요. 단, 평소 잊고 살기는 하나 우리 삶을 윤택하게 해주는 위대한 사업가나 기관을 이끄는 통솔자형 사람들이 있음에 다행이기도 합니다.', inline=False)
        embed.add_field(name='‘성취’를 통해 느끼는 행복', value='통솔자형 사람은 크든 작든 성취 가능한 도전에 매력을 느낍니다. 이들은 충분한 시간과 자원만 있으면 그 어떤 것도 실현 가능하다고 믿습니다. 이것이 통솔자형 사람을 뛰어난 사업가로 만드는 이들만의 성격적 자질로, 전략적인 사고와 장기적인 안목과 더불어 빠른 판단력과 정확성으로 계획을 단계별로 실행해 나감으로써 진정한 리더의 역할을 합니다. 보통의 사람이라면 포기하고 말 일들도 대단한 의지력으로 꾸준히 밀어붙이는데, 이는 이들에게 있어 자아실현을 위한 자기 암시이기도 합니다. 또한 뛰어난 사회성을 발휘하여 다른 동료들을 채찍질함으로써 함께 더 큰 성공과 성취를 이루고자 합니다.', inline=False)        
        embed.add_field(name = '기업 관련 협상이든, ', value = '자동차 구매를 위한 협상이든 통솔자형 사람은 우위를 선점한 채 한 치도 뒤로 물러서는 법이 없습니다. 이는 단순히 이들이 냉혈인이라거나 사악해서가 아니라 단지 도전과 지략, 그리고 상황에서 행해지는 상대방과의 재담(才談)을 진정 즐기기 때문입니다. 만일 상대가 게임이 안된다 하더라도 이는 통솔자형 사람으로 하여금 승리로 이끄는 핵심 전략서를 스스로 덮게 만드는 이유가 되지 못합니다.',inline = False)
        embed.add_field(name='"내가', value='상대방을 배려할 줄 모르는 [미친 X]이라고 해도 난 신경 안 써. 왜냐하면 난 잘난 [미친 X]이니까"라는 생각이 이들의 속마음입니다.', inline=False)
        embed.add_field(name='통솔자형 사람이', value='우러러보는 누군가가 있다면 그는 아마도 그들 자신처럼 정확하고 민첩하게 행동하는 사람으로, 지식으로 무장하여 그들에게 감히 도전장을 내미는 사람일 것입니다. 이들은 다른 사람의 재능을 알아보는 재주 또한 있는데, 이는 팀원 간의 협력을 다지고(아무리 잘나고 똑똑한 개인이라도 모든 일을 혼자 다 할 수는 없으므로) 이들의 오만방자함을 견제하는 데 도움이 됩니다. 간혹 혹독하리만치 타인의 실수를 지적하는 경향이 있는데 이로 인해 이들은 종종 문제를 야기하기도 합니다.', inline=False)   
        embed.add_field(name='진정성 있는 인간관계 형성을 위한 노력', value='분석형에 속하는 사람들은 감정을 표현하는 일에 서투른데, 사교적인 성격상 이들의 성격은 밖으로 쉽게 표출됩니다. 가령 일적으로 비효율적이고 무능하며 게으르다고 판단되는 이들을 보면 이들은 그들의 예민한 부분을 가차 없이 건드리기도 합니다. 통솔자형 사람에게 있어 감정 표현은 나약함의 표시로 이러한 성향 때문에 쉽게 적을 만들기도 합니다. 또한 단순히 목표를 성취하는 데 있어서뿐만 아니라 타인으로부터 인정받고 안 받고의 여부는 효율적인 조직에 달려 있음을 사람들에게 줄기차게 상기시키는데, 이는 통솔자형 사람에게는 매우 민감하고 중대한 사안이기 때문입니다.', inline=False)          
        embed.add_field(name='이들은', value='진정한 권력가형으로 그들 본연의 모습 이상으로 자신을 과대 포장하는 경향이 있습니다. 하지만 그들의 성공이 혼자만의 능력이 아닌 이들을 옆에서 도운 여러 사람에게서 기인한다는 점을 잊지 말아야 합니다. 그리고 함께 한 이들의 헌신과 노력, 재능을 인정하며, 특히 든든한 지원군이 되어 주었음에 온 마음을 다해 감사함을 느끼는 것이 중요합니다. 비록 [안되면 척]이라고 하겠다는 마음가짐이라 하더라도 말입니다. 만일 다른 이들의 감정을 살피는 진심 어린 노력이 이들이 가진 성격적 장점과 합해진다면, 이들은 다른 이들과 더 깊고 만족스러운 인간관계를 형성할 수 있을 것입니다. 그리고 이들 또한 도전 후의 참된 보람을 느낄 수 있을 것입니다.', inline=False) 
        embed.add_field(name='대담한 통솔자형에 속하는 유명인', value='스티브 잡스(애플 창시자), 프랭클린.D.루즈벨트, 짐 캐리, 말콤 X, 닥터 스트레인지(히어로)', inline=False) 
        await message.channel.send(channel,embed=embed) 
        
        
    if message.content.startswith("?ESFP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [자유로운 영혼의 연예인]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '저는 ', value = '이기적이고 참을성도 없을 뿐 아니라, 약간의 열등감도 가지고 있어요. 실수투성이에 천방지축이고, 때때로 통제가 안되기도 하지요. 만일 이런 제가 감당이 안 되는 당신이라면 완벽한 모습일 때의 저와 함께할 자격 또한 없어요.',inline = False)
        embed.add_field(name='갑자기 ', value='흥얼거리며 즉흥적으로 춤을 추기 시작하는 누군가가 있다면 이는 연예인형의 사람일 가능성이 큽니다. 이들은 순간의 흥분되는 감정이나 상황에 쉽게 빠져들며, 주위 사람들 역시 그런 느낌을 만끽하기를 원합니다. 다른 이들을 위로하고 용기를 북돋아 주는 데 이들보다 더 많은 시간과 에너지를 소비하는 사람 없을 겁니다. 더욱이나 다른 유형의 사람과는 비교도 안 될 만큼 거부할 수 없는 매력으로 말이죠.', inline=False)
        embed.add_field(name='나는 타고난 연예인', value='천부적으로 스타성 기질을 타고난 이들은 그들에게 쏟아지는 스포트라이트를 즐기며 어디를 가나 모든 곳이 이들에게는 무대입니다. 사실상 많은 배우가 이 성격 유형에 속하기도 합니다. 간혹 친구나 다른 이들과 어울릴 시 쇼맨십에 찬 모습을 보이기도 하는데, 썰렁한 유머를 던져 주의를 집중시키기도 하는 이들은 그들이 가는 곳곳마다 시끌벅적한 파티를 연상케 합니다. 매우 사교적인 성향의 이들은 단순한 것을 좋아하며, 좋은 사람들과 어울려 즐거운 시간을 갖는 것보다 세상에 더 큰 즐거움은 없다고 여깁니다.', inline=False)        
        embed.add_field(name = '단순히', value = '시끌벅적 요란함을 넘어 이들은 뛰어난 미적 감각 또한 가지고 있습니다. 외모를 가꾸는 데에서부터 치장하는 법, 그리고 집안을 예쁘게 꾸미는 인테리어 능력에 이르기까지 연예인형 사람은 남다른 미적 감각을 지니고 있습니다. 일단 무엇을 보는 순간 어떤 것이 아름답고 매력적인지를 알아차리는 심미안이 있으며, 주변을 독창적인 그들의 스타일에 맞추어 바꾸는 것을 좋아합니다. 연예인형 사람은 천성적으로 호기심이 많으며, 새로운 디자인이나 스타일을 찾아다니는 데 거부감이 전혀 없습니다.',inline = False)
        embed.add_field(name='자칫', value='그리 보이지 않을 수도 있지만 연예인형 사람은 세상이 자기 위주로만 돌아가지 않는다는 것 또한 잘 알고 있습니다. 뛰어난 관찰력으로 다른 사람의 감정에 주의를 기울이는 이들은 어려운 문제에 봉착한 이들이 가장 먼저 찾아와 고민을 털어놓는 사람이기도 합니다. 이 경우 이들은 고민을 털어놓는 이에게 따뜻한 위로와 지지를 보내며 실질적인 조언 또한 잊지 않습니다. 하지만 반대로 문제를 겪고 있는 당사자가 본인인 경우 문제를 직면하여 해결하려 하기보다는 문제 자체를 아예 피하고 싶어 합니다. 대개 소소한 인생의 굴곡이나 어려움은 즐기는 한편, 만일 자신이 비난의 중심이 되는 경우라면 얘기가 달라집니다.', inline=False)
        embed.add_field(name='난 잘났으니까요..!', value='연예인형 사람이 가진 가장 큰 단점 중 하나는 이들이 종종 즉각적인 즐거움에 심취해 정작 이들의 안락한 삶 영위를 가능케 하는 의무나 책임은 회피한다는 것입니다. 이를 깨닫게 하기 위한 난해한 분석 자료나 반복적인 업무 혹은 이와 관련한 통계 자료는 이들에게는 무용지물입니다. 차라리 이들은 인생을 기회나 운에 맡기거나, 그렇지 않으면 친구에게 도움을 구합니다. 연예인형 사람에게는 일일 당분 섭취량이나 노후 계획과 같이 장기적인 안목으로 꼼꼼히 계획을 세워 인생을 설계해 나가는 것이 중요합니다. 곁에서 언제까지나 이를 맡아 책임져 줄 사람이나 친구가 항상 곁에 있는 것은 아니니까요.', inline=False)   
        embed.add_field(name='이들은', value='또한 그들 자신이 가진 가치나 자질을 잘 알고 있는데 이는 그 자체로는 별문제가 없습니다. 다만 계획을 세우는 데는 빵점인 이들의 성향으로 인해 씀씀이가 이들이 경제적으로 충당할 수 있는 범위를 넘어서는 경우가 종종 있는데, 특히 신용 카드의 무분별한 사용은 이들에게 매우 위험할 수 있습니다. 거시적인 안목으로 장기 목표를 세우는 것이 아닌 틈틈이 기회나 상황만 엿보는 이들은 그들의 경제적 부주의 함으로 인해 하고 싶어 하는 활동이나 삶을 영위하는 데 있어 제한이 따름을 알아차리게 될 것입니다.', inline=False)          
        embed.add_field(name='어쩔 수 없는 상황', value='때문에 어디에 콕 박혀 친구나 사람들과 어울리지 못하는 자신을 발견하는 것만큼 이들을 더 속상하게 하는 게 없습니다.', inline=False) 
        embed.add_field(name='연예인형 사람은', value='웃음과 오락, 그리고 새로운 즐거움을 추구하는 곳이라면 어디를 가나 두 팔 벌려 환영받습니다. 이들에게 있어 다른 사람들과 함께 신나게 즐기는 것만큼 유쾌한 일도 없을 테니 말입니다. 이들은 또한 그들이 아끼는 사람들과 희로애락을 함께하며 주제와 상관없이 몇 시간이고 수다를 떨기도 합니다. 물론 대화를 나누기에 적당한 주제여야 하겠지만요. 그저 이들이 미래 계획만 철저히 잘 설계해 놓는다면 이들은 세상에서 누릴 수 있는 온갖 즐거움과 재미를 경험하며 살 수 있을 것입니다. 주변에 있는 사람들과 더불어 말입니다.', inline=False) 
        embed.add_field(name='자유로운 영혼의 연예인형에 속하는 유명인', value='마랄린 먼로, 아담 리바인, 캡틴 마블(히어로), 툭 집안 페레그린(반지의제왕), 잭 도슨(타이타닉 남주)', inline=False) 
        await message.channel.send(channel,embed=embed) 
        
        
    if message.content.startswith("?ESFJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [사교적인 외교관]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '서로 ', value = '용기를 북돋아 주고 치켜세우며 힘이 돼주세요. 한 사람이 받은 긍정의 에너지가 곧 모든 이에게 전달될 테니까요.',inline = False)
        embed.add_field(name='사교형 사람을', value='한마디로 정의 내리기는 어렵지만, 간단히 표현하자면 이들은 [인기쟁이]입니다. 인구의 대략 12%를 차지하는 꽤 보편적인 성격 유형으로, 이를 미루어 보면 왜 이 유형의 사람이 인기가 많은지 이해가 갑니다. 종종 고등학교에서 치어리더나 풋볼의 쿼터백으로 활동하기도 하는 이들은 분위기를 좌지우지하며 여러 사람의 스포트라이트를 받거나 학교에 승리와 명예를 불러오도록 팀을 이끄는 역할을 하기도 합니다. 이들은 또한 훗날 다양한 사교 모임이나 어울림을 통해 주위 사람들에게 끊임없는 관심과 애정을 보임으로써 다른 이들을 행복하고 즐겁게 해주고자 노력합니다.', inline=False)
        embed.add_field(name='천성적으로', value='사교적인 성향인 이들은 가까운 친구나 지인들의 일거수일투족을 모두 알기를 원합니다. 과학 이론이나 국제 정치와 같은 대화 주제는 사교형 사람의 관심을 오래 잡아두지 못합니다. 대신 이들은 패션이나 외모, 그리고 그들을 포함하여 다른 사람의 사회적 지위와 같은 대화 소재에 더 많은 관심을 보입니다. 실생활 이야기나 가십거리가 이들에게는 한 마디로 빵과 버터 같은 대화 소재입니다. 하지만 좋은 일을 하는 데에는 그들이 가진 힘과 지위를 이용해 발 벗고 나서기도 합니다.', inline=False)        
        embed.add_field(name = '지혜로운 리더를 위한 우러름', value = '이타주의자인 사교형 사람은 다른 이들을 도우며 옳은 일을 하고자 하는 일에 진지한 태도로 임합니다. 다만 다른 성격 유형과 달리 사교형 사람은 도덕적 잣대를 철학이나 미신이 아닌 이미 수립된 법이나 사회 질서 체제 안에서 찾습니다. 사교형 사람은 사회는 다양한 배경과 관점을 가진 사람들의 집합체로 그들이 믿고 따르는 것만이 절대적인 진리가 아니라는 것을 명심할 필요가 있습니다.',inline = False)
        embed.add_field(name='사교형 사람은', value='그들 자신이 진심으로 존경받고 그들의 가치를 인정받고 있다고 생각이 드는 한은 지위를 막론하고 어떻게든 의미 있는 방식으로 다른 이에게 도움이 되고자 합니다. 이는 특히 가정 내에서 여실히 드러나는데, 이들은 집에서는 가정적인 배우자이자 헌신적인 부모이기도 합니다. 또한 계급 체계를 선호하는 경향이 있으며, 가정에서나 회사에서 그들의 주장을 펼 수 있는 동시에 안정된 생활 영위를 위해 어느 정도의 사회적 지위와 권력을 갖고자 합니다.', inline=False)
        embed.add_field(name='조화로운 인간관계', value='타인에 대한 지원을 아끼지 않는 활발한 성격인 이들은 어느 모임을 가든지 한두 명은 쉽게 만날 수 있습니다. 어떻게 해서든지 사람들과 만나 수다 떨며 웃는 시간을 만들고야 마는 이들이니까요! 그렇다고 이들을 단순히 웃고 지나쳐 버리는 가벼운 만남으로 치부해서는 안 됩니다. 이들이 아니면 누구도 대신하지 못하는 심오한 역할을 하기도 하는 이들이니까요. 사교형 사람은 친구나 지인의 인간관계나 일상생활과 관련한 이야기에 관심 있게 들으며 세세한 사항마저 기억하는 경향이 있습니다. 그리고는 도움이 필요한 적절한 순간에 진심 어린 따뜻한 마음으로 대화 상대가 되어줄 만발의 준비를 하고 있습니다. 만약 상황이 생각하는 안 좋게 돌아가거나 모임 내 긴장감이 조성되는 경우 이들은 이를 금세 알아차려 사람들 간에 화해와 안정을 찾기 위해 노력합니다.', inline=False)   
        embed.add_field(name='충돌을 싫어하는 사교형 사람은', value=' 사회적 위계질서를 확립하는 데 많은 에너지를 소모하며, 사전에 계획되지 않은 즉흥적인 만남이나 모임을 계획하는 것을 좋아합니다. 이들은 그들이 주관하는 모임을 위해 많은 시간과 노력을 들이는데, 만일 이들의 제안이 거부당하거나 이들의 계획이 사람들의 관심이나 이목을 충분히 끌지 못하면 상처를 받기도 합니다. 앞서 얘기했듯, 사교형 사람은 각각의 사람이 모두 다른 배경과 성격을 가지고 있으며, 이는 단순히 그가 주최하는 모임이나 활동 혹은 그들에게 관심이 없어서가 아니라 다만 모임 자체에 특별히 흥미를 느끼지 못해서 임을 깨닫는 것이 중요합니다.', inline=False)          
        embed.add_field(name='사교형 사람이', value='감내하기 힘들어하는 것 중 하나가 자신의 예민하고 쉽게 상처받는 성격과 타협점을 찾는 일입니다. 사람들이 그의 생각에 동의하지 않거나 되려 이들을 비판하는 경우가 생기면 어김없이 상처를 받는데, 이 역시도 인생의 한 부분입니다. 이를 해결할 수 있는 좋은 방법은 자신들이 가장 자신 있게 잘하는 일에 열중하는 것으로, 타인에게 좋은 역할 모델이 되어주거나 그들이 영향력을 행사할 수 있는 영역 안에서 권력을 행사하는 것입니다. 결과적으로 이러한 이들의 노고는 많은 사람에게 본보기가 되어 많은 이들로부터 존경과 감사를 받게 될 것입니다.', inline=False) 
        embed.add_field(name='사교적인 외교관형에 속하는 유명인', value='테일러 스위프트, 빌 클린턴, 제니퍼 로페즈, 산사 스타크(왕좌의게임), ', inline=False) 
        await message.channel.send(channel,embed=embed) 
        
        
    if message.content.startswith("?ESTP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [모험을 즐기는 사업가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '인생은', value = '과감한 모험이거나, 아니면 아무것도 아니다.',inline = False)
        embed.add_field(name='주변에', value='지대한 영향을 주는 사업가형 사람은 여러 사람이 모인 행사에서 이 자리 저 자리 휙휙 옮겨 다니는 무리 중에서 어렵지 않게 찾아볼 수 있습니다. 직설적이면서도 친근한 농담으로 주변 사람을 웃게 만드는 이들은 주변의 이목을 끄는 것을 좋아합니다. 만일 관객 중 무대에 올라올 사람을 호명하는 경우, 이들은 제일 먼저 자발적으로 손을 들거나 아니면 쑥스러워하는 친구를 대신하여 망설임 없이 무대에 올라서기도 합니다.', inline=False)
        embed.add_field(name='국제사회 이슈나', value='이와 관련한 복잡하고 난해한 이론과 관련한 담화는 이들의 관심을 오래 붙잡아 두지 못합니다. 사업가형 사람은 넘치는 에너지와 어느 정도의 지식으로 대화에 무리 없이 참여하기는 하나, 이들이 더 역점을 두는 것은 앉아서 말로만 하는 논의가 아닌 직접 나가 몸으로 부딪히는 것입니다. 행동이 먼저 앞서기도 하는 이들은 이로 인해 가끔 실수를 범하기도 하지만 이들은 단순히 턱 괴고 앉아 지켜만 보고 있느니 만약의 사태를 대비해 만반의 준비를 한 뒤라면 직접 나가 몸으로 부딪혀 문제를 해결해 나가는 것을 선호합니다.', inline=False)        
        embed.add_field(name = '혼동하지 말아야 할 단어, [움직임] vs [행동]', value = '사업가형 사람은 다른 성격 유형과 비교하여 위험을 수반하는 행동을 많이 하는 경향이 있는데, 이들은 마치 폭풍을 몰고 다니는 이들과도 같습니다. 달든 쓰든 인생이 주는 삶의 다양한 맛과 열정으로 인생을 즐기기는 하지만, 이는 단순히 감정적으로 느껴지는 전율 때문이 아니라 그들의 이성적인 사고관에 짜릿한 자극을 주기 때문입니다. 불기둥이 소용돌이치는듯한 절체절명의 상황에서도 이들은 사실이나 현실에 근거하여 이성적으로 결정을 내리는 경향이 있습니다.',inline = False)
        embed.add_field(name='이러한 성향 때문에', value='사업가형 사람은 학교와 같은 엄격한 규율이나 질서를 요구하는 조직 내에서 종종 어려움을 토로하기도 합니다. 이는 이들이 공부를 못하는 똑똑하지 못한 학생이어서가 아니라 딱딱하고 엄격한 가르침 방식이 그들이 선호하는 체험을 통한 배움과는 거리가 멀기 때문입니다. 지루하게만 보일지 모르는 이 과정 역시 목적지에 이르기 위한 필수 요소임을 깨닫게 하기까지는 이들의 많은 내적 성숙함을 요구합니다. 하지만 또 한편으로 이는 더 넓고 흥미로운 세계를 향한 기회로 작용하기도 합니다.', inline=False)
        embed.add_field(name='이들에게', value='달린 또 다른 도전 과제는 이들은 타인이 아닌 그들 스스로 정한 도덕적 잣대에 따라 사고하고 행동한다는 점입니다. [규칙은 깨라고 있는 법!] 아마도 일선 고등학교 교사나 기업 내 관리자는 이러한 이들의 성향을 묘사하는 말에 공감을 표할 것입니다. 하지만 한 가지 잊지 말아야 할 것은 이들이 문제를 야기하는 행동을 줄이고 그들의 에너지를 긍정적인 방향으로 활용하며, 지루해하는 일을 잘 참고 묵묵히 해낸다면 이들은 우리 사회에 없어서는 안 될 중요한 구성원이라는 점입니다.', inline=False)   
        embed.add_field(name='타인을 위한 세심한 배려', value='다른 성격 유형과 비교하여 가장 예리하면서 여과 없이 사물을 있는 그대로 관찰하는 사업가형 사람은 타인의 작은 변화조차도 정확히 집어냅니다. 다른 사람의 얼굴에 나타나는 작은 표정 변화나 평소 입고 다니는 옷 스타일 혹은 습관에의 변화 등 다른 성격 유형의 사람은 사소한 것 하나만 집어내도 다행으로 여길 만한 작은 변화조차도 이들은 그 뒤에 숨은 의미나 생각을 곧잘 포착해냅니다. 일단 무언가 이전과 다름을 감지하면 이들은 타인의 감정을 많이 고려하지 않은 채 이것저것 물어보고 싶어 합니다. 하지만 모든 사람이 그들의 결정이나 비밀을 동네방네 떠들고 다니고 싶어 하지 않을 수도 있음을 명심해야 합니다.', inline=False)          
        embed.add_field(name='사업가형 사람의', value='이러한 즉각적이며 예리한 관찰력과 행동력은 종종 대기업, 특히 급박한 상황에서는 더욱 요구되는 자질이기도 합니다', inline=False) 
        embed.add_field(name='다만', value='자칫 잘못하면 상황에 너무 몰두하여 예민한 사람의 감정에 치명적인 상처를 입히거나 원치 않는 상황을 초래할 수 있으며, 심지어는 본인 자신의 건강이나 안전을 해하는 경우도 있습니다. 인구의 대략 4%인 이들은 적당히 도전적이며 경쟁적인 사회를 이루기에 딱 알맞은 비율입니다. 사회 정의 질서를 무너뜨리지 않는 내에서 말입니다.', inline=False) 
        embed.add_field(name='기본적으로', value='열정과 활력이 넘치는 사업가형 사람은 방해 요소가 생기면 이성적 사고로 중무장합니다. 충만한 영감과 설득력, 그리고 다양한 성격을 가지고 팀을 이끄는 타고난 리더형인 이들은 아직 개척되지 않은 세계로 다른 이들을 인도함으로써 그들이 가는 곳곳 인생의 즐거움과 흥미로움을 더합니다. 다만 이러한 장점을 보다 효율적이며 가치 있는 성향으로 탈바꿈하는 것이 가장 큰 숙제로 남아있기는 하지만 말입니다.', inline=False)        
        embed.add_field(name='모험을 즐기는 사업가형에 속하는 유명인', value='어니스트 해밍웨이, 잭 니콜슨, 마돈나, 브루스 윌리스, 사무엘.L.잭슨(한국에서는 쉴드의 닉 퓨리 국장으로 유명함), 로켓(가디언즈 오브 갤럭시), 앤트맨(히어로)', inline=False) 
        await message.channel.send(channel,embed=embed) 
        
        
    if message.content.startswith("?ISFP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [호기심 많은 예술가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '저는', value = '하루 동안에도 변화를 거듭합니다. 아침에 눈을 뜨면 한 사람이 있습니다. 그리고 잠을 청하러 갈 때면 저는 확신합니다. 거기엔 또 다른 제 자신이 있다는 것을 말이죠.',inline = False)
        embed.add_field(name='모험가형 사람은', value='일반적으로 사람들이 생각하듯 야외에서 앙증맞은 나무 그림을 그리고 있는 그런 유형의 예술가는 아니지만, 진정한 예술가라고 할 수 있습니다. 실상 상당수 많은 이들이 그러한 능력을 충분히 갖추고 있기도 합니다. 이들은 그들의 심미안이나 디자인 감각, 심지어는 그들의 선택이나 행위를 통하여 사회적 관습이라는 한계를 뛰어넘고자 합니다. 실험적인 아름다움이나 행위를 통해 전통적으로 기대되는 행동양식이나 관습에 도전장을 내미는 이들은 "저를 가두어두려 하지 마세요!"라고 수없이 외칩니다.', inline=False)
        embed.add_field(name='자기 자신에 대한 만족', value='이들은 다양한 아이디어나 사람들로부터 영감을 받아 다채로우면서도 감각적인 삶을 살아갑니다. 그들이 받은 영감을 본인만의 시각으로 재해석하여 새로운 것을 발견하고 탐험함으로써 즐거움을 느끼기도 하는 이들은 그 어떤 유형의 사람보다 탐험이나 실험 정신이 뛰어납니다. 어디로 튈지 모르는 즉흥적인 성향으로 간혹 이들을 예측하는 것이 어려운데, 이는 가까운 친구나 사랑하는 사람들 역시 예외가 아닙니다.', inline=False)        
        embed.add_field(name = '그럼에도 불구하고', value = '단연 내향적 성향을 가지고 있는 모험가형 사람들은 스포트라이트를 벗어나 재충전을 위해 혼자만의 시간을 갖곤 하는데, 이는 주위 사람들은 한번 더 놀라게 하기도 합니다. 하지만 이들이 혼자 있다고 게으르게 넋 놓고 앉아 있는 것은 아닙니다. 이 시간은 그들이 가진 원리원칙을 재고하는 자기 성찰을 위한 시간으로, 과거나 미래에 집착하지 않고 순전히 그들이 누구인지 자신을 들여다보는 시간입니다. 그리고는 이들은 곧 언제 그랬냐는 듯이 사람들 앞에 변화된 모습으로 [짠]하고 나타납니다.',inline = False)
        embed.add_field(name='넘치는', value='열정을 쏟아부으며 정열적인 삶을 살아가는 모험가형 사람은 다른 유형의 사람들에 비해 도박이나 익스트림 스포츠와 같이 위험성이 내재한 활동을 즐기는 경향이 있습니다. 그나마 다행인 것은 환경이나 상황 조율 능력이 뛰어나 대부분의 사람보다 소질이 있다는 것입니다. 다른 이들과 어울리는 것을 좋아하기도 하는 이들은 거부할 수 없는 그들만의 매력을 가지고 있습니다.', inline=False)
        embed.add_field(name='모험가형 사람들은', value='타인의 작은 칭찬에도 쉽게 자극받아 무책임하고 무모한 행동을 일삼을 수 있다는 것을 그들 자신 역시 잘 알고 있습니다.', inline=False)   
        embed.add_field(name='반대로', value='이들이 누군가로부터 비판을 받을 경우, 상황을 안 좋게 몰고 갈 수도 있습니다. 타인의 적절한 비판은 오히려 다른 관점으로 받아들여 새로운 방안을 모색하는 가치 있는 용도로 활용하기도 하는 반면, 신랄하거나 진중치 못한 비판은 자칫하면 모험가 사람을 욱하게 만들어 이들의 분노가 그리 아름답지만은 않은 모습으로 표출될 수도 있습니다.', inline=False)          
        embed.add_field(name='모험가형 사람은', value='타인의 감정을 잘 살피며 조화를 중요시 여깁니다. 이 때문에 비난이나 비판을 받는 경우, 화가 어느 정도 누그러질 때까지 기다리는 것이 이들에게는 쉽지 않은 일입니다. 하지만 좋은 일이건 나쁜 일이건 영원히 지속되는 것은 없듯이 일단 분노의 감정이 수그러들면 이들은 과거는 과거일 뿐이라고 치부하며 마치 아무 일도 없었다는 듯이 다시금 그들의 삶을 살아갑니다.', inline=False) 
        embed.add_field(name='작은 것 하나하나가 인생의 의미', value='이 성격 유형에 속하는 사람이 가장 어려워하는 것 중 하나가 미래를 설계하는 일입니다. 더 나은 미래를 위해 목표를 설정하고 이를 달성케 하는 건설적인 이상향을 찾는다는 게 그리 생각만큼 간단한 일이 아닙니다. 다른 유형의 사람들이 미래를 구체적인 자산이나 은퇴 계획이라는 틀 안에서 세우는 반면, 모험가형 사람은 주식과 같은 자산이 아닌 다양한 경험을 통해 자아를 찾기 위한 행동 계획을 세우는 데에 더 많은 투자를 하는 경향이 있습니다.', inline=False) 
        embed.add_field(name='만약', value='이러한 목표나 믿음이 순수함에서 기인한 것이라면 이들은 누구보다도 사심 없는 마음으로 선행을 실천할 것입니다. 하지만 이는 반대로 말하면 누구보다도 자기중심적이며 속임수를 일삼으며 자기애에 사로잡혀 행동하는 이들로 비추어질 수도 있음을 의미합니다. 모험가형 사람은 그들이 하고자 하는 대로 그냥 내버려 두는 것이 가장 현명한 방법입니다. 물론 새로운 취미를 발견하고 실행하는 것이 생각처럼 쉬운 일은 아니지만, 하루하루 서두르지 않고 원하는 것이 무엇인지 곰곰이 생각하고 되새겨 본다면, 그것이 무엇이 되었든 모험가형 사람이 진정 좋아하는 것이 무엇인지 찾게 될 것입니다.', inline=False)      
        embed.add_field(name='호기심 많은 예술가형에 속하는 유명인', value='브리트니 스피어즈, 마이클 잭슨, ', inline=False) 
        await message.channel.send(channel,embed=embed) 
        
        
    if message.content.startswith("?INTJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [용의주도한 전략가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '윗자리에 있는 사람은', value = '고독한 법, 전략적 사고에 뛰어나며 매우 극소수인 건축가형 사람은 이를 누구보다 뼈저리게 이해합니다. 전체 인구의 2%에 해당하는 이들은 유독 여성에게서는 더욱 찾아보기 힘든 유형으로, 인구의 단 0.8%를 차지합니다. 체스를 두는 듯한 정확하고 계산된 움직임과 풍부한 지식을 소유하고 있는 이들은 그들과 견줄 만한 비슷한 부류의 사람을 찾는 데 종종 어려움을 겪습니다. 건축가형 사람은 상상력이 풍부하면서도 결단력이 있으며, 야망이 있지만 대외적으로 표현하지 않으며, 놀랄 만큼 호기심이 많지만 쓸데없는 데 에너지를 낭비하는 법이 없습니다.',inline = False)
        embed.add_field(name='올곧은 태도로 계획 달성을 향한 돌진', value='이들의 지식을 향한 갈증은 어릴 적부터 두드러지게 나타나는데, 때문에 건축가형 사람은 어릴 때 [책벌레]라는 소리를 자주 듣습니다. 대개 친구들 사이에서는 놀림의 표현임에도 불구하고 전혀 개의치 않아 하며, 오히려 깊고 넓은 지식을 가지고 있는 그들 자신에게 남다른 자부심을 느낍니다. 이들은 또한 관심 있는 특정 분야에 대한 그들의 방대한 지식을 다른 이들과 공유하고 싶어 하기도 합니다. 반면, 일명 가십거리와 같이 별 볼 일 없는 주제에 대한 잡담거리보다는 그들 나름의 분야에서 용의주도하게 전략을 세우거나 이를 실행해 옮기는 일을 선호합니다.', inline=False)
        embed.add_field(name='당신은', value='의견을 가질 권리가 없습니다. 다만 제대로 된 의견을 가질 권리만 있을 뿐이죠. 그 누구도 무식할 권리는 없기 때문입니다.', inline=False)        
        embed.add_field(name = '대부분', value = '사람 누가 봐도 이들은 지극히 모순적인 삶을 살아가는 것처럼 보이지만 이를 객관적이고 이성적으로 놓고 보면 사실 이해가 가기도 합니다. 예를 들면, 이들은 비현실적일 만큼 이상주의자이자인 동시에 매우 신랄한 조롱과 비판을 일삼는 냉소주의자로 이 둘이 같이 공존한다는 것 자체가 불가능해 보입니다. 또한, 기본적으로 지혜와 노력, 그리고 신중함만 있으며 못할 것이 없다고 믿는 한편, 사람들이 실질적으로 그러한 성취를 끌어내는 데 있어서는 게으르고 근시안적이며 자기 잇속만 차린다고 생각합니다. 그렇다고 이러한 냉소적인 태도가 성취하고자 하는 이들의 욕구를 꺾지는 못합니다.',inline = False)
        embed.add_field(name='돌부처와 같은 원칙주의자', value='확신에 찬 자신감과 함부로 범접할 수 없는 신비로운 아우라를 발산하는 건축가형 사람은 통찰력과 관찰력, 기발한 아이디어, 그리고 뛰어난 논리력에 강한 의지와 인격이 합쳐져 변화를 이끄는 데 앞장섭니다. 이따금 이들이 생각했던 아이디어나 계획을 뒤집고 재수립하는 과정을 거쳐 완벽함을 추구하고자 하거나 도덕적 잣대에 따라 재정비하는 시간을 가지기도 합니다. 건축가형 사람의 업무 스타일을 좇아오지 못하거나 심지어는 이들이 왜 그렇게 행동하는지 전혀 감을 잡지 못하는 사람은 단번에 신임을 잃거나 이들의 인정을 받지 못할 수도 있습니다.', inline=False)
        embed.add_field(name='건축가형', value='사람이 몸서리치게 싫어하는 것이 있다면 바로 질서, 한계, 그리고 전통과 같은 것들인데, 이들은 세상의 모든 것을 탐구와 발견의 대상으로 여기기 때문입니다. 만일 문제 해결을 위한 방안을 찾은 경우, 간혹 무모할 수 있으나 기술적으로 뛰어나며 언제나 그렇듯 비정통적인 기발한 방법이나 아이디어를 수립하기 위해 홀로 행동에 옮깁니다', inline=False)   
        embed.add_field(name='그렇다고', value='이들이 충동적이라는 말은 아닙니다. 얼마나 간절히 성취하기를 원하는지 상관없이 건축가형 사람은 기본적으로 이성적인 사고를 합니다. 내부에서 비롯되었든 아니면 외부 세계에서 기인하였든지, 매사 이들의 아이디어는 “실현 가능할까?”와 같은 ‘이성적 사고’라는 필터의 과정을 거칩니다. 이는 사람 혹은 아이디어에 항시 적용되는 기제로, 이 때문에 건축가형 사람은 종종 곤경에 빠지기도 합니다.', inline=False)          
        embed.add_field(name='홀로 떠나는 여행, 깨달음의 시간', value='오랜 시간 방대한 지식을 쌓아 온 똑똑하고 자신감 넘치는 이들이지만, 인간관계만큼은 이들이 자신 있어 하는 분야가 아닙니다. 진리나 깊이 있는 지식을 좇는 이들에게 선의의 거짓말이나 가벼운 잡담은 그저 낯설기만 합니다. 그럼에도 불구하고 자신을 필요 이상으로 내몰아 부조리투성이인 사회적 관습을 경험하기도 합니다. 가장 좋은 것은 이들이 그들 자신 자체로 온전히 있을 수 있는 곳, 즉 스포트라이트 밖에 있는 것입니다. 건축가형 사람은 익숙하고 편안한 곳에서 본연의 모습으로 있을 때 비로소 연인 관계나 그 외 여러 상황에서 그들 나름의 빛을 발하며 사람들을 끌어들이기 때문입니다.', inline=False) 
        embed.add_field(name='건축가형', value='사람의 성향을 정의하자면 이들은 인생을 마치 체스를 두듯이 새로운 계획이나 전술, 그리고 대책을 세워가며 상대방 머리 위에서 수를 두며 허를 찌르는 기술로 상황을 유리하게 몰고 가는 듯한 삶을 살아갑니다. 그렇다고 이들이 양심 없는 삶을 살아간다는 말은 아닙니다. 다만 감정에 치우치는 것을 싫어하는 이들의 성격상 타인의 눈에 그렇게 비추어질 수 있습니다. 이를 고려하면 왜 많은 허구 속 등장인물들(종종 오해를 받곤 하는 영화 속 영웅들)이 본 성격 유형으로 묘사되는지 이해할 수 있을 것입니다.', inline=False) 
        embed.add_field(name='용의주도한 전략가형에 속하는 유명인', value='미카엘라 오바마, 엘론 머스크, 크리스토퍼 놀란, 블라디미르 푸틴, 아놀드 슈워츠네거, 회색의 간달프/백색의 간달프(반지의제왕)   ', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("?ISTP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [만능 재주꾼]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '저는', value = '그런 삶을 살고 싶었습니다. 무언가 다른 삶 말이지요. 매일 같은 곳을 가고, 같은 사람을 만나고, 매번 같은 일을 하며 살고 싶지 않았습니다. 전 흥미로운 도전을 원했습니다.',inline = False)
        embed.add_field(name='냉철한', value='이성주의적 성향과 왕성한 호기심을 가진 만능재주꾼형 사람은 직접 손으로 만지고 눈으로 보면서 주변 세상을 탐색하는 것을 좋아합니다. 무엇을 만드는 데 타고난 재능을 가진 이들은 하나가 완성되면 또 다른 과제로 옮겨 다니는 등 실생활에 유용하면서도 자질구레한 것들을 취미 삼아 만드는 것을 좋아하는데, 그러면서 새로운 기술을 하나하나 터득해 나갑니다. 종종 기술자나 엔지니어이기도 한 이들에게 있어 소매를 걷어붙이고 작업에 뛰어들어 직접 분해하고 조립할 때보다 세상에 즐거운 일이 또 없을 것입니다. 전보다 조금은 더 향상된 모습으로요.', inline=False)
        embed.add_field(name='만능재주꾼형 사람은', value='창조와 문제 해결을 위한 이해, 그리고 실행 착오와 실질적인 경험을 통해 아이디어를 탐색합니다. 다른 이들이 그들의 과제에 흥미를 보이는 것을 좋아하며, 간혹 다른 이들로 하여금 작업 중인 과제에 참여하도록 유도하기도 합니다. 단, 그들만의 원리원칙이나 자유를 침범하지 않는 범위에 한해서 말이죠. 사람들은 만능재주꾼형 사람이 베푸는 호의에 열린 마음으로 대할 필요가 있습니다.', inline=False)        
        embed.add_field(name = '타인을', value = '잘 도우며 그들의 경험을 다른 이들과 공유하는 것을 좋아하기도 하는 이들은 특히나 그들이 아끼는 사람일수록 더욱 그러합니다. 이들이 인구의 고작 5%만이 차지하지 않는다는 사실이 그저 안타까울 따름입니다. 더욱이 여성의 경우는 더욱 흔치 않은데, 대개 이 성향의 여성은 사회가 일반적으로 요구하는 이상적인 여성상에 들어맞지 않는 경우가 많으며, 이들은 자라면서 말괄량이 소리를 듣기도 합니다.',inline = False)
        embed.add_field(name='기꺼이 다름을 지향하다', value='내성적인 성향으로 현실적인 사안에 관심이 많은 이들은 얼핏 보면 단순해 보일 수 있지만, 사실 알고 보면 꽤 복잡한 성향을 가지고 있습니다. 친절하고 상냥하지만 사생활을 중요시 여기며, 침착하면서도 금세 즉흥적인 성향으로 돌변하기도 하며, 호기심이 많으면서도 오래 앉아 수업을 들을 때는 집중하지 못하는 모습을 보이기도 합니다. 이로 인해 주변 가까운 친구나 아끼는 사람들조차 이들의 행동을 예측하는 데 어려움을 겪습니다. 만능재주꾼형 사람은 한동안 헌신적이고 꾸준한 모습을 보이다가도 충동의 에너지를 서서히 쌓아두고 있다가 어느 순간 예고 없이 터뜨리기도 하는데, 이로 인해 관심사가 이전과 전혀 다른 방향으로 바뀌기도 합니다.', inline=False)
        embed.add_field(name='미래를', value='대비한 비전 수립은커녕 이렇듯 휘몰아치는 변화가 있을 때조차 새로 발견한 관심사의 실행 가능 여부에는 크게 관심을 두지 않습니다.', inline=False)   
        embed.add_field(name='실질적으로', value='현실에 근거하여 결정을 내리면서도 마음 한가운데에는 [자신이 대접받고 싶은 만큼 다른 이를 대접하라]와 같은 공정함이라는 사고방식이 깊이 박혀있는데, 이는 이들만의 성격적 고유 특성을 잘 설명해 줍니다. 남에게 발을 밟히지 않으려고 아예 발부터 먼저 빼고 보는 이들은 너무 지나치리만치 신중하게 행동하여 종종 필요 이상으로 멀리 가기도 합니다. 이들은 기본적으로 옳든 그르든 자신이 받은 만큼 똑같이 되돌려주는 것이 공정한 행위라고 생각합니다.', inline=False)          
        embed.add_field(name='만능재주꾼형 사람이', value='당면한 가장 큰 과제는 천성적으로 타인에게 관심이 많은 이들의 성격으로 하여금 다른 이들 역시 그들과 같을 것이라는 착각하에 행동이 먼저 앞선다는 점입니다. 신중치 못한 농담을 먼저 꺼내는 이들을 보면 영락없이 만능재주꾼형 사람입니다. 또한, 타인의 일에 지나치리만치 간섭하여 여기저기 시끄럽게 휘둘리다가 다른 흥미로운 관심거리가 생기면 재빨리 계획을 변경하기도 합니다.', inline=False) 
        embed.add_field(name='남과 다름의 즐거움', value='만능재주꾼형 사람은 다른 성격 유형의 사람들이 사회에서 수용 가능한 질서나 행위와 같은 비교적 확고하게 구분된 그들 나름의 선이 있다는 것을 깨닫게 될 것입니다. 이들보다 예민한 성향의 사람은 타인의 마음을 헤아리지 않는 가벼운 농담 따위를 좋아하지 않습니다. 당연히 그러한 농담 자체를 던지지 않는 것은 두말할 필요도 없고요. 지나친 장난을 좋아하는 사람은 아무도 없으며, 이는 같이 어울리는 부류 사이에서도 마찬가지입니다. 이미 감정이 많이 상해 있는 상태에서 선을 넘어가는 경우 훗날 뒷감당하기 힘든 상황을 초래할 수 있기 때문입니다.', inline=False) 
        embed.add_field(name='타인의', value='감정을 파악하는 데 있어 애를 먹는 이들은 자신의 감정이나 동기조차 파악하지 못하는 이들의 천성과 공정함을 추구하고자 하는 성격에 그 이유가 기인한다고 할 수 있습니다. 게다가 인간관계 형성 시 타인을 향한 정서적 공감이 아닌 행동으로 탐색하고자 하는 성향이 있어 간혹 원치 않는 상황을 초래하기도 합니다. 사람들 간의 보이지 않는 선이나 규칙을 지키는 데 어려움을 호소하는 이들은 인간관계 시 자유롭게 그 경계를 넘나들기를 원하며, 혹 필요하면 이를 넘어 다른 색으로 물들이고 싶어 하기도 합니다.', inline=False)         
        embed.add_field(name='정의적이며', value='유머를 겸비한 동시에 실질적으로 문제 해결을 위해 무언가를 만들어 내는 만능재주꾼형 사람의 실용적인 접근 방식이 이들의 예측 불허한 성격이나 스타일을 이해하는 좋은 사람들과 합쳐져 일하는 환경이 조성된다면, 이들은 마치 물 만난 고기처럼 신이 나 몇 년이고 이것저것 유용한 장난감 거리를 만드는 재미에 흠뻑 빠져 살 수 있을 것입니다. 만인의 우러름을 받으면서 말입니다.', inline=False) 
        embed.add_field(name='엄격한 관리자형에 속하는 유명인', value='베어 그릴스, 마이클 조던, 클린트 이스트우드, 톰 크루즈, 아리야 스타크(왕좌의게임), 인디아나 존스, 호크아이(히어로), 제임스 본드,   ', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("?ESTJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [엄격한 관리자]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '훌륭한', value = '질서는 모든 것의 기초이다.',inline = False)
        embed.add_field(name='관리자형', value='사람은 그들 생각에 반추하여 무엇이 옳고 그른지를 따져 사회나 가족을 하나로 단결시키기 위해 사회적으로 받아들여지는 통념이나 전통 등 필요한 질서를 정립하는 데 이바지하는 대표적인 유형입니다. 정직하고 헌신적이며 위풍당당한 이들은 비록 험난한 가시밭길이라도 조언을 통하여 그들이 옳다고 생각하는 길로 사람들을 인도합니다. 군중을 단결시키는 데에 일가견이 있기도 한 이들은 종종 사회에서 지역사회조직가와 같은 임무를 수행하며, 지역 사회 발전을 위한 축제나 행사에서부터 가족이나 사회를 하나로 결집하기 위한 사회 운동을 펼치는 데 사람들을 모으는 역할을 하기도 합니다.', inline=False)
        embed.add_field(name='옳다고 생각되는 일은 거침없이 밀고 나가는 굳은 의지!', value=' 특히 민주주의 사회에서 더욱 필요로 하는 이 유형의 사람은 인구의 대략 11%를 차지합니다. 전 세계 유명 비즈니스 리더나 정치인 중 상당수가 이 유형에 속하는 것이 어찌 보면 그리 놀랍지 만은 않을 것입니다. 법과 사회 질서의 중요함을 굳게 믿는 이들은 헌신과 공명정대한 삶을 통해 다른 이들에게 본보기가 되고자 하는데, 특히 업무적으로 게으르거나 부정을 저지르는 이들은 가차 없이 벌하기도 합니다. 만일 누군가 고되고 힘든 사회 운동을 자처하여 그들의 됨됨이를 증명해 보이고자 하는 이들이 있다면 이들은 바로 관리자형 사람일 것입니다.', inline=False)        
        embed.add_field(name = '이들은', value = '주변 상황을 잘 판단하여 명확하고 증명이 가능한 확실한 사실에 근거하여 사고하는 경향이 있습니다. 이리하여 만일 이들의 의견이나 결정 내린 사항이 심한 반대 의견에 부딪혔을 때 이들로 하여금 무엇이 가능하고 불가능한지를 정확히 판단하여 본연의 믿음이나 생각을 고수한 채 꿋꿋이 헤쳐나갈 수 있게 합니다. 말을 허투루 하지 않는 이들은 성취하기 어려운 고된 일도 마다치 않고 기꺼이 뛰어들어 구체적으로 실행 계획을 세워 난해해 보이는 일도 수월히 실행해 나갑니다.',inline = False)
        embed.add_field(name='이들은', value='또한 타인과 스스럼없이 잘 어울리며, 대화 시 단순한 논리나 사실에 입각한 딱딱한 대화가 아닌 따뜻하고 섬세한 언어를 사용하여 인간 대 인간으로 이야기를 나눕니다. 이로 인해 주변 가까운 친구나 동료는 이들을 사교성이 많은 사람으로 오해하기도 하지만, 사실 이들은 갑자기 물러서야 하는 상황이 생겼을 때 마음의 평정심을 잃지 않을 수 있도록 잠시 생각을 비우고 재충전할 수 있는 혼자만의 시간을 가지기를 원합니다. 선의의 옹호자형 사람은 다른 이들의 감정을 섬세히 잘 살피며, 다른 이들도 역시 마찬가지로 그렇게 해주기를 바랍니다. 이는 때로 이들이 단 며칠간만이라도 혼자 있을 수 있는 여유를 가지는 것을 의미하기도 합니다.', inline=False)
        embed.add_field(name='나아가', value='이들은 업무를 수행하는 데 있어 그들의 엄격한 가치관이 함께 일하는 다른 이들에게도 반영되기를 원합니다. 기본적으로 사람들과의 약속을 충실히 이행하는 이들의 기본 성향 때문에 함께 일하는 동업자나 부하의 무능력함, 태만, 심지어는 부정직함으로 이들을 시험에 들게 하는 경우 심한 불호령도 마다하지 않습니다. 이 때문에 종종 융통성 없는 성격으로 비추어지기도 하지만, 이는 이들의 성격이 외골수여서가 아니라 이것들이 건강한 사회 건설을 위하여 지켜져야 할 중요한 덕목이라고 굳게 믿기 때문입니다.', inline=False)   
        embed.add_field(name='부족함을 인정할 줄 아는 지혜', value='법질서를 준수하고 이웃을 도우며 지역 사회나 조직 발전을 위해 타인의 동참을 유도하는 관리자형 사람은 전형적인 모범시민이라고 할 수 있습니다.', inline=False)          
        embed.add_field(name='단,', value='이들이 명심해야 할 한 가지 사항은 모든 이들이 그들과 같은 노력을 기울이며 동일한 길을 가지는 않는다는 것입니다. 진정한 리더의 역할은 그룹 혹은 개개인의 장점을 잘 살펴 그들의 생각을 마음껏 펼칠 수 있도록 돕는 데 있습니다. 만일 이러한 이들의 노력이 선행된다면 모든 필요한 자질과 사실을 가지고 모든 이가 원하는 방향으로 이들을 통솔할 수 있을 것입니다.', inline=False) 
        embed.add_field(name='엄격한 관리자형에 속하는 유명인', value='존 D.록펠러, 프랭크 시나트라, 제임스 먼로, 보로미르(반지의제왕), 랍 스타크(왕좌의게임),  ', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("?INFJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [선의의 옹호자]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '선의의 옹호자형은', value = '가장 흔치 않은 성격 유형으로 인구의 채 1%도 되지 않습니다. 그럼에도 불구하고 나름의 고유 성향으로 세상에서 그들만의 입지를 확고히 다집니다. 이들 안에는 깊이 내재한 이상향이나 도덕적 관념이 자리하고 있는데, 다른 외교형 사람과 다른 점은 이들은 단호함과 결단력이 있다는 것입니다. 바라는 이상향을 꿈꾸는데 절대 게으름 피우는 법이 없으며, 목적을 달성하고 지속적으로 긍정적인 영향을 미치고자 구체적으로 계획을 세워 이행해 나갑니다.',inline = False)
        embed.add_field(name='종종', value='구조 작업이나 자선 활동을 하는 곳에서 쉬이 볼 수 있는 이 유형의 사람은 다른 이들을 돕는 것을 인생의 목적으로 여깁니다. 특히나 이들은 문제를 야기하는 핵심 사안에 관심이 많은데, 이는 근본적인 문제를 해결함으로써 궁극적으로 어떠한 노력이나 도움 자체가 필요치 않기를 희망하는 이들의 순수한 열망 때문입니다.', inline=False)
        embed.add_field(name='서로 돕는 세상', value='선의의 옹호자형 사람은 진정 그들만의 고유한 성향을 내포하고 있습니다. 나긋나긋한 목소리 뒤에는 강직함이 숨어 있으며, 의견을 강력하게 피력할 줄 알며 옳다고 생각되는 일에는 지칠 줄 모르고 투쟁합니다. 강한 의지와 분별력이 있는 이들은 단순히 개인의 이득을 취하는 데 이를 활용하는 것이 아닌, 그들의 창의적인 상상력과 강한 신념, 그리고 특유의 섬세함으로 균형 이루는 세상을 만들고자 합니다. 평등주의나 인간의 업보(karma)와 같은 관념에 관심이 많은 이들은 세상에 해악을 끼치는 사람의 마음을 녹이는 데에는 진정한 사랑과 인간애보다 더 좋은 것은 없다고 믿습니다. ', inline=False)        
        embed.add_field(name = '모든', value = '인간은 창의적인 이타주의의 빛 속을 걸을 것인지, 아니면 파괴적인 이기주의의 노선을 걸을 것인지 중 하나를 선택해야 합니다.',inline = False)
        embed.add_field(name='이들은', value='또한 타인과 스스럼없이 잘 어울리며, 대화 시 단순한 논리나 사실에 입각한 딱딱한 대화가 아닌 따뜻하고 섬세한 언어를 사용하여 인간 대 인간으로 이야기를 나눕니다. 이로 인해 주변 가까운 친구나 동료는 이들을 사교성이 많은 사람으로 오해하기도 하지만, 사실 이들은 갑자기 물러서야 하는 상황이 생겼을 때 마음의 평정심을 잃지 않을 수 있도록 잠시 생각을 비우고 재충전할 수 있는 혼자만의 시간을 가지기를 원합니다. 선의의 옹호자형 사람은 다른 이들의 감정을 섬세히 잘 살피며, 다른 이들도 역시 마찬가지로 그렇게 해주기를 바랍니다. 이는 때로 이들이 단 며칠간만이라도 혼자 있을 수 있는 여유를 가지는 것을 의미하기도 합니다.', inline=False)
        embed.add_field(name='투쟁을 위해 한 박자 쉬어가는 여유', value='무엇보다도 선의의 옹호자형 사람은 자신을 챙기고 돌보는 일을 게을리하지 말아야 합니다. 비록 강한 신념에서 기인한 열정으로 어느 정도 그들이 가진 한계점을 넘어설 수는 있지만, 이러한 열망이 자신들이 감내할 수 있는 수준을 넘어서는 경우 이들은 쉬이 지치거나 극심한 스트레스를 호소하는 등 이들의 건강에 적신호가 켜질 수도 있습니다. 특히나 심한 반대나 갈등 상황이 조성되는 경우, 예민하고 섬세한 이들의 성격에 발동이 걸려 무슨 수를 써서라도 그들에게 가해지는 음모나 모함이라고 판단되는 상황과 맞서 싸우고자 합니다. 만일 상황이 여의치 않거나 피할 수 없는 상황이라면, 이들은 비상식적인 방법이나 옳지 않은 방식으로 투쟁을 벌이기도 합니다. ', inline=False)   
        embed.add_field(name='꼭 그렇지 않음', value='에도 불구하고 선의의 옹호자형 사람에게 있어 세상은 불평등과 불공정함이 난무하는 곳입니다. 크든 작든 세상의 잘못된 것을 바로잡고자 하는 데 이들보다 열심인 사람은 없을 것입니다. 다만 이들은 세상을 살피느라 분주한 자신 또한 잘 챙기고 살펴야 할 필요가 있음을 잊지 말아야 합니다.', inline=False)          
        embed.add_field(name='선의의 옹호자형에 속하는 유명인', value='마틴 루터 킹, 넬슨 만델라, 마더 테레사, 레이디 가가, 니콜 키드먼, 모건 프리만, 괴테, 아라고른(반지의제왕), 갈라드리엘(반지의제왕)', inline=False) 
        await message.channel.send(channel,embed=embed) 
        
    if message.content.startswith("?ENFP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [재기발랄한 활동가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '당신이', value = '생계를 위해 무슨 일을 하는지, 저는 관심 없습니다. 다만 제가 알고 싶은 건 당신이 가슴 저리게 동경하는 것이 있는지, 당신 마음속 깊은 바람을 감히 충족시키고자 하는 열망이 있는지입니다. 당신의 나이가 얼마인지는 중요하지 않습니다. 당신이 사랑을 위해, 당신의 꿈을 위해, 그리고 삶이라는 모험을 위해 기꺼이 바보가 될 준비가 되어 있는지, 그것이 궁금할 뿐입니다. ',inline = False)
        embed.add_field(name='활동가형', value='사람은 자유로운 사고의 소유자입니다. 종종 분위기 메이커 역할을 하기도 하는 이들은 단순한 인생의 즐거움이나 그때그때 상황에서 주는 일시적인 만족이 아닌 타인과 사회적, 정서적으로 깊은 유대 관계를 맺음으로써 행복을 느낍니다. 매력적이며 독립적인 성격으로 활발하면서도 인정이 많은 이들은 인구의 대략 7%에 속하며, 어느 모임을 가든 어렵지 않게 만날 수 있습니다. ', inline=False)
        embed.add_field(name='아이디어 하나로 세상을 바꾸다!', value='타인을 즐겁게 하는 사교적인 특성만이 이들이 가진 전부가 아닙니다. 활동가형 사람은 통찰력 있는 비전으로 호기심과 에너지 사이의 선을 명확히 구분합니다. 이들은 인생을 하나로 연결된 크고 복잡한 퍼즐로 보는 경향이 있는데, 인생을 체계적인 일련의 과정으로 보는 분석가형 사람과 달리 인간의 감정이나 인정(人情), 신비로움을 프리즘에 투영하여 그 안에 숨어있는 깊은 의미를 찾아내고자 합니다.  ', inline=False)        
        embed.add_field(name = '다소', value = '과하리만치 독립적인 성향의 이들은 안정적이거나 안전한 삶이 아닌 창의적이며 자유로운 삶을 갈망합니다.',inline = False)
        embed.add_field(name='다른', value='성격 유형에 속한 사람들은 활동가형 사람들에게서 거부할 수 없는 이들만의 매력을 느낄 수 있습니다. 일단 창의력에 발동이 걸리면 이들은 스포트라이트를 받는 주인공이 되어 동료나 사람들로부터 리더 혹은 전문가로 추앙받기도 합니다. 하지만 이는 독립적이며 자유를 최고로 여기는 활동가형 사람들이 선호하는 바는 아니며, 만일 반복적인 관리 업무를 요구하는 자리에 있는 경우라면 더욱이 그러합니다. 창의적인 문제 해결을 위한 대책을 찾는 데서 큰 자부심을 얻는 활동가형 사람에게 혁신적인 사고를 가능하게 하는 자유의지 여부가 매우 중요합니다. 만일 그들 자신이 지루한 일상적인 업무에 갇혀 있다고 생각될 경우, 이들은 쉬이 낙담하거나 인내심을 잃을 수도 있기 때문입니다. ', inline=False)
        embed.add_field(name='[살짝 미치면] 인생이 즐겁다?', value='다행히도 활동가형 사람은 언제 어떻게 휴식을 취해야 하는지 잘 알고 있습니다. 일할 때는 열정적이며 진취적인 모습이었다가 단숨에 무대 위 열성적으로 몸을 흔드는 자유로운 영혼의 모습으로 단숨에 변모하기도 하는 이들은 이러한 갑작스러운 변화로 종종 가까이에 있는 친구들이나 지인들을 놀라게 하기도 합니다. 이들의 다양한 성격적 면모는 다른 이들과의 정서적인 교감을 가능하게 하며, 특히나 친구 혹은 동료들에게 색다른 통찰력을 제공함으로써 영감을 불어 넣기도 합니다. 활동가형 사람은 모든 이들이 자신의 솔직한 감정에 귀 기울이고 이를 표현할 수 있는 시간이 필요하다고 믿습니다. 이러한 이유로 다양한 인간 감정이나 인간관계에 대한 내용이 이들과 대화 시 단골 소재입니다. ', inline=False)   
        embed.add_field(name='하지만', value='이런 활동가형 사람에게도 주의해야 할 사항이 있습니다. 만일 이들이 그들의 직관에 지나치게 의존한 나머지 사람들의 의도를 잘못 해석하는 경우 오해가 생겨 계획에 차질을 빚을 수 있는데, 이는 단도직입적으로 충분히 해결할 수 있는 문제를 더 어렵게 만드는 길입니다. 이러한 사회생활에서 빚어지는 스트레스는 협력과 조화를 중요시 여기는 성격의 사람들에게는 이들의 잠을 설치게 하는 근심 요소가 될 수 있습니다. 이들은 혹 실수로 누군가의 발을 밟았다 할 경우, 이들 역시 발을 밟힌 사람과 같은 고통을 느끼는 감성적이면서도 예민한 성격의 소유자입니다.', inline=False)         
        embed.add_field(name='활동가형 사람은', value='인간관계나 사람의 감정, 혹은 생각과 관련하여 이들이 원하는 만족스러운 대답을 찾을 때까지 끊임없이 찾아 헤매고 다닐 것입니다. 그리고 진정 그들이 원하는 답을 찾는 그 날, 이들의 상상력이나 인간애, 그리고 용기는 어마어마한 빛을 발할 것입니다.', inline=False)   
        embed.add_field(name='활동가형에 속하는 유명인', value='로버트 다우니 주니어, 윌 스미스, 스파이더맨(히어로), 윌리 웡카(찰리와 초콜릿 공장), 안나 여왕님(겨울왕국), 올라프(겨울왕국)', inline=False) 
        await message.channel.send(channel,embed=embed)

    if message.content.startswith("?A"):
        await message.channel.send(" 당신의 혈액형은 A형 입니다. ") 
        await message.channel.send(" A형은 원리원칙주의, 완전주의자로 불리는 경우가 많습니다.")
        await message.channel.send(" 책임감이 강하고 한번 맡은 일은 끝까지 해내는 경향이 있기 때문에 조직에서 신뢰를 받는 경우가 많습니다. ")
        await message.channel.send(" 신중하게 계획을 세우고 실천하는 스타일이기도 해서 가끔은 융통성이 없다는 이야기를 듣게됩니다. ")
        await message.channel.send(" 그러나 성실함에 있어서는 가장 최고로 뽑히며, 연애할 때는 의외로 대담함을 보입니다.")
        await message.channel.send(" ============ ")
        await message.channel.send(" *A-A 75%의 궁합을 보입니다.")
        await message.channel.send(" *서로 둘이 비슷한 성향을 가졌기 때문에 그만큼 안정적인 연애가 가능하지만 때로는 너무 비슷한 것이 문제로 작용하기도 합니다. ")
        await message.channel.send(" *서로 문제를 풀려고 하지 않고 마음속에 담아두는 것이 큰 문제입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *A-B 65%의 궁합을 보입니다. ")
        await message.channel.send(" *B형이 웃음을 주기 때문에 아주 재미있는 연애가 됩니다.")
        await message.channel.send(" *그러나 A형에 비해 자기주장이 강하기 때문에 소심한 A형이 상처를 받게됩니다. ")
        await message.channel.send(" ============")
        await message.channel.send(" *A-AB 60%의 궁합을 보입니다.")
        await message.channel.send(" *AB형은 꼼꼼하고 리드하는 경향이 있어 A형과 만나면 대부분 AB형이 리드를 하게 됩니다.")
        await message.channel.send(" *자주 싸우지만 비교적 안정적인 조합입니다.")
        await message.channel.send(" ============")
        await message.channel.send(" *A-O 90%의 궁합을 보입니다.")
        await message.channel.send(" *O형은 어딜가도 잘 어울리는 편이기 때문에 A형과도 잘맞고 가장 높은 궁합을 자랑합니다. ")
        await message.channel.send(" *결혼까지 생각할 수 있는 조합입니다. ")

    if message.content.startswith("?B"):
        await message.channel.send(" 당신의 혈액형은 B형 입니다. ") 
        await message.channel.send(" B형은 상당히 재미있는 성격을 보유하고 있는 경우가 많습니다.")
        await message.channel.send(" 호기심이 상당히 많고 창의적인 발상을 함으로 주변에 항상 많은 이야기가 존재하게 됩니다. ")
        await message.channel.send(" 그러나 집중력이 다소 떨어지는 경향이 있어 일관성이 없다는 평을 받기도 합니다. ")
        await message.channel.send(" 정이 많아 남을 배려하고 눈물도 많은 편입니다.")
        await message.channel.send(" ============ ")
        await message.channel.send(" *B-A 40%의 궁합을 보입니다. ")
        await message.channel.send(" *소심한 A형 때문에 답답함을 느끼게 되고 B형이 거의 모든 것을 이끄는 형태가 됩니다.")
        await message.channel.send(" *다른 성격때문에 많이 다투고 A형이 많이 참게 됩니다.")
        await message.channel.send(" ============ ")
        await message.channel.send(" *B-B 80%의 궁합을 보입니다.")
        await message.channel.send(" *즐겁지만 불같은 커플로 한번 싸우게되면 둘다 불같은 성격으로 크게 싸우고 금방 풀리는 단순한 커플이 탄생합니다. ")
        await message.channel.send(" ============")
        await message.channel.send(" *B-AB 65%의 궁합을 보입니다.")
        await message.channel.send(" *B형은 자신의 이야기를 많이 하지만 자신의 표현을 잘하지 않는 AB형의 모습에 당황하게 됩니다.")
        await message.channel.send(" *그러나 B형이 잘 받아주는 편이라 유지가 가능합니다.")
        await message.channel.send(" ============")
        await message.channel.send(" *B-O 90%의 궁합을 보입니다.")
        await message.channel.send(" *O형은 누구나 잘 어울리는 성격으로 멋대로인 B형과도 비교적 잘 어울립니다.")
        await message.channel.send(" *B형 옆을 지키면서 잘 다독여주고 계속해서 관계를 지속해 나가는 형태를 보입니다. ")

    if message.content.startswith("?O"):
        await message.channel.send(" 당신의 혈액형은 O형 입니다. ") 
        await message.channel.send(" O형은 인간미가 있고 목표지향적인 성격으로 작은일에 크게 연연하지 않는 무던한 스타일입니다.")
        await message.channel.send(" 열정적으로 일에 몰두하기 때문에 리더가 되는 경우가 많으며 동료의식 또한 강하게 나타냅니다. ")
        await message.channel.send(" 뜻하지 않는 일이 발생했을 때는 상당히 현실적인 자세를 취하기도 합니다. ")
        await message.channel.send(" 그리고 남에게 지는 것을 싫어하기 때문에 의도하지 않게 상대방을 무시하는 경향도 보입니다.")
        await message.channel.send(" ============ ")
        await message.channel.send(" *O-A 90%의 궁합을 보입니다.")
        await message.channel.send(" *A형은 자상하고 O형은 다정한 성격이기 때문에 상당히 잘 맞습니다. ")
        await message.channel.send(" *안전한 연애가 가능합니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *O-B 70%의 궁합을 보입니다. ")
        await message.channel.send(" *B형이 자신의 생각을 잘 표출하기 때문에 처음부터 강한 느낌으로 연애를 시작하게됩니다.")
        await message.channel.send(" *그리고 비교적 무던한 연애를 지속합니다. ")
        await message.channel.send(" ============")
        await message.channel.send(" *O-AB 30%의 궁합을 보입니다.")
        await message.channel.send(" *성격이 정반대인 두 사람이 만났기 때문에 연애를 지속하기 힘듭니다.")
        await message.channel.send(" *둘 중 하나의 희생적인 이해가 필요합니다.")
        await message.channel.send(" ============")
        await message.channel.send(" *O-O 20%의 궁합을 보입니다.")
        await message.channel.send(" *어디서나 잘 어울리는 O형이지만 비슷한 성격의 O형과는 전혀 다른 양상을 보입니다. ")
        await message.channel.send(" *서로가 너무 비슷하기 때문에 자주 싸우게되고 승부욕이 강하기 때문에 한번 싸우게 되면 쉽게 풀리지 않습니다. ")

    if message.content.startswith("??AB"):
        await message.channel.send(" 당신의 혈액형은 AB형 입니다. ") 
        await message.channel.send(" AB형은 A형과 B형의 성격이 조금씩 섞여있는 형태로 어느쪽으로 더 많이 가중되는가에 따라 성격이 달라집니다.")
        await message.channel.send(" 한마디로 어떠하다고 단정짓기가 쉽지 않습니다. ")
        await message.channel.send(" 대부분 매사에 객관적으로 바로보며 합리적인 행동을 하고 모든일에 요령있게 잘 적응합니다. ")
        await message.channel.send(" 그래서 비교적 실수가 적은 편에 속합니다.")
        await message.channel.send(" 다른 사람의 주장에 쉽게 따라가는 경향을 보이기도 하기 때문에 우유부단하다는 평을 받기도 합니다..")
        await message.channel.send(" 자신의 사생활을 드러내는 것을 꺼려하기 때문에 비밀이 상당히 많습니다.")
        await message.channel.send(" ============ ")
        await message.channel.send(" *AB-A 75%의 궁합을 보입니다.")
        await message.channel.send(" *친구에서 연인으로 발전하는 경우가 많습니다. ")
        await message.channel.send(" *모든일을 자신의 일처럼 도와주는 A형한테 AB형이 호감을 느끼게 됩니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *AB-B 70%의 궁합을 보입니다. ")
        await message.channel.send(" *적극적인 B형이 부담스러울 수 있지만 연인으로 발전하면 잘 맞추어 나갑니다.")
        await message.channel.send(" *AB형이 싸움을 싫어하기 때문에 B형에게 맞춰주는 형태를 보입니다. ")
        await message.channel.send(" ============")
        await message.channel.send(" *AB-AB 90%의 궁합을 보입니다.")
        await message.channel.send(" *서로가 어떤 생각인지 잘 알기 때문에 싸울일이 적고 오랜 연인들 처럼 편안하게 관계를 이어나갈 수 있습니다.")
        await message.channel.send(" ============")
        await message.channel.send(" *AB-O 25%의 궁합을 보입니다.")
        await message.channel.send(" *AB형이 여자라면 힘든 상황에서 무슨일이든지 함께하려는 O형에게 호감을 느끼면서 관계가 유지됩니다.")
        await message.channel.send(" *하지만 이해하려고 노력하지 않으면 금방 한계에 부딪히게 됩니다. ")
      

    if message.content.startswith("엿"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="[니 좆은 새끼손가락만하자나 ㅋㅋ]")      
        await message.delete()
       
    if message.content.startswith("샹년"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="욕 왜해요?")      
        await message.delete()
        
    if message.content.startswith("썅년"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="욕 왜해요?")      
        await message.delete()
        
    if message.content.startswith("샹놈"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="욕 왜해요?")      
        await message.delete()
        
    if message.content.startswith("썅놈"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="욕 왜해요?")      
        await message.delete()
        
    if message.content.startswith("상년"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="욕 왜해요?")      
        await message.delete()
        
    if message.content.startswith("상놈"):
        msg = await message.channel.send("Doribot has detected an inappropriate expression!")
        await asyncio.sleep(4.0)
        await msg.edit(content="욕 왜해요?")      
        await message.delete()
        
    if message.content.startswith("자살하고싶어"):
        msg = await message.channel.send("우리, 맘 잡고 다시 해 보아요. 행운은 잠시 쉬고 있을 뿐입니다")
        await asyncio.sleep(4.0)
        await msg.edit(content="[자살]은 범죄야.. 절대 죽지마.")      
        await message.delete()     

        
    if message.content.startswith("자살하고싶다"):
        msg = await message.channel.send("힘들 땐 가만히 눈을 감고 스스로에게 말을 걸어주세요. 나는 어떤 사람인지 얼마나 소중한 사람인지 ")
        await asyncio.sleep(4.0)
        await msg.edit(content="[자살]은 범죄야.. 절대 죽지마.")      
        await message.delete()     

        
    if message.content.startswith("자살할래"):
        msg = await message.channel.send("젊었을 때 고민 같은 거, 암 것도 아니여, 나이들어봐 ")
        await asyncio.sleep(4.0)
        await msg.edit(content="[자살]은 범죄야.. 절대 죽지마.")      
        await message.delete()   
        
    if message.content.startswith("자살하고프다"):
        msg = await message.channel.send("음... 힘든 일들 모두 그냥, 지나가는 바람이라 생각해 보면 어떨까? ")
        await asyncio.sleep(4.0)
        await msg.edit(content="[자살]은 범죄야.. 절대 죽지마.")      
        await message.delete()   
        
    if message.content.startswith("자살마렵다"):
        msg = await message.channel.send("풋 하고 웃지 말고 하하하하하하하")
        await asyncio.sleep(4.0)
        await msg.edit(content="[자살]은 범죄야.. 절대 죽지마.")      
        await message.delete()   
        
    if message.content.startswith("자살마려워"):
        msg = await message.channel.send("3년 전에 고민한 거 기억나세요? 기억 안 나죠? 이번에도 그럴 거예요. ")
        await asyncio.sleep(4.0)
        await msg.edit(content="[자살]은 범죄야.. 절대 죽지마.")      
        await message.delete()   
        
    if message.content.startswith("죽여주"):
        msg = await message.channel.send("마음을 열어 보세요. 혼자가 아닙니다, 당신은. ")
        await asyncio.sleep(4.0)
        await msg.edit(content="[자살]은 범죄야.. 절대 죽지마.")      
        await message.delete()   
        
    if message.content.startswith("죽을"):
        msg = await message.channel.send("많이 힘들었지? ")
        await asyncio.sleep(4.0)
        await msg.edit(content="[자살]은 범죄야.. 절대 죽지마.")      
        await message.delete()   
        
    if message.content.startswith("죽고"):
        msg = await message.channel.send("뒷감당 잘해요? ")
        await asyncio.sleep(4.0)
        await msg.edit(content="[자살]은 범죄야.. 절대 죽지마.")      
        await message.delete()   
       
    if message.content.startswith("자1살"):
        msg = await message.channel.send("많이 힘들었지? ")
        await asyncio.sleep(4.0)
        await msg.edit(content="[자살]은 범죄야.. 절대 죽지마.")      
        await message.delete()    
       
    if message.content.startswith("자2살"):
        msg = await message.channel.send("많이 힘들었지? ")
        await asyncio.sleep(4.0)
        await msg.edit(content="[자살]은 범죄야.. 절대 죽지마.")      
        await message.delete() 
       
    if message.content.startswith("자3살"):
        msg = await message.channel.send("많이 힘들었지? ")
        await asyncio.sleep(4.0)
        await msg.edit(content="[자살]은 범죄야.. 절대 죽지마.")      
        await message.delete()       

    if message.content.startswith("한손에총들고"):
        await message.channel.send(" 아프리카TV BJ 보겸의 던전앤파이터와 아프리카 TV 계정 닉네임이다. ")
        
        
    if message.content.startswith("뒷광고"):
        await message.channel.send(" [양팡] ")
        
        
    if message.content.startswith("양팡"):
        await message.channel.send(" [뒷광고]로 시청자들 기만한 악덕 방송인 ")
        
        
    if message.content.startswith("보겸뒷광고"):
        await message.channel.send(" Doribot has detected an inappropriate expression! ") 
        await message.delete()
        
    if message.content.startswith("양팡뒷광고"):
        await message.channel.send(" [뒷광고]로 시청자들 기만한 악덕 방송인들은 대한민국에서 추방해야됨;;")
        
        
    if message.content.startswith("문복희"):
        await message.channel.send(" [뒷광고]로 시청자들 기만한 악덕 방송인이지만 사과 한마디도 없었음. ㅋ 이런 뻔뻔한 태도 리스펙한다. ") 
        
        
    if message.content.startswith("보겸"):
        await message.channel.send(" 아프리카 TV BJ 출신이면서 순수 한국인 구독자로 4백만명을 모은 유튜브 크리에이터는 지금까지 아무도 없었어. 이런 사람은 역사책에 기록해서 위인으로 기억되야됨. ")

    if message.content.startswith("윤지선"):
        await message.channel.send(" [페미니즘]을 위한다면서 먹칠을 하는 행위를 일삼은 [가톨릭대학교] 전 교수이자 현재는 스타강사. ")
        await asyncio.sleep(4.0)
        await msg.edit(content="[이 사람] 지능적 안티 페미니스트임.")      
        await message.delete()         
      
      

    if message.content.startswith("?Members"):
        await message.channel.send(" Who's the most curious? (? + 도리도리곰도리)")

        
    if message.content == "?엘사" or message.content == "엘사":
        channel = message.channel
        urllib.request.urlretrieve("https://i.imgur.com/UufmudR.jpg", "explain.png")
        image = discord.File("explain.png", filename="image.png")
        embed = discord.Embed(title="엘사 정령님", description="디즈니 애니메이션 겨울왕국의 등장인물이자 스토리의 주축이 되는 주인공. 또 다른 주인공 안나의 언니.", color=0x00ff56)
        embed.set_thumbnail(url="https://i.imgur.com/PLDPnJG.jpg")
        embed.add_field(name="작품이 출시된 2013년부터 현재까지 디즈니에서", value="가장 영향력 있는 인기 캐릭터 중 하나이다.", inline=True)
        await channel.send(embed=embed, file=image)

    if message.content == "?안나" or message.content == "안나":
        channel = message.channel
        urllib.request.urlretrieve("https://i.imgur.com/8LCt6LU.jpg", "explain.png")
        image = discord.File("explain.png", filename="image.png")
        embed = discord.Embed(title="안나 여왕님", description="디즈니의 애니메이션 겨울왕국의 등장인물. 영화의 스토리를 이끌어 나가는 주인공. 또 다른 주인공 엘사의 여동생이다.", color=0x00ff56)
        embed.set_thumbnail(url="https://i.imgur.com/PLDPnJG.jpg")
        embed.add_field(name="밝고 명랑하고 적극적이며, ", value="순수하면서 활발한 말괄량이 소녀 성격이다.", inline=True)
        await channel.send(embed=embed, file=image)                                 
                            
    if message.content.startswith("??7호선"):
        channel = message.channel
        embed = discord.Embed(
            title = 'Introducing 7호선  ',
            description = '',
            color = discord.Color.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"")
        embed.add_field(name = '7호선', value = '대한민국의 고딩이다. 05년생으로 확인되었으며, 디시인사이드에선 iPhoneOS(iphoneos)라는 고닉으로 활동하고, 디스코드 태그는 iPhoneOS#3138 이다.  주 활동 갤러리는 타르코프 갤러리이다. [타르코프 하는 놈들을 두려워해라. 그들은 평범한 생명체가 아니다.] (근데, 05년생이 몇살이야? 실존하긴 함?) ',inline = False)
        embed.add_field(name='그의', value='MBTI는 INFP 이다. 타르코프와 오버워치를 즐겨하며, 오버워치에서는 라인 원챔이다. 심해에서 탱커를 해주는 것은 사실 굉장히 고마운 행위이나, 팀을 생각할 줄 모르는 플레이를 남발한다. 남발하는 수준이 아니다. 매판 솔플 하면서 팀원이 그거에 대해 반응을 보이면 먹잇감을 물은 하이에나처럼 정치질을 시전하기 시작한다. 매판 이렇게 플레이 하지만, 욕설로 정지를 먹은적이 없다. ', inline=False)
        await message.channel.send(channel,embed=embed)

    if message.content.startswith("?나냡"):
        channel = message.channel
        embed = discord.Embed(
            title = 'Introducing 냐납  ',
            description = '',
            color = discord.Color.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"")
        embed.add_field(name = '나냡', value = '대한민국의 20대이며, 직업은 요리사이다. 99년생으로 확인되었으며, 디시인사이드에선 비스킷(kkii99)라는 고닉으로 활동하고, 디스코드 태그는 컨하#5913 이다. 주 활동 갤러리는 배틀그라운드 모바일 갤러리이다. 아마 파딱이라 모배갤만 주로 한 것 같다.',inline = False)
        embed.add_field(name='그의', value='MBTI는 ISFP 이고, 혈액형은 AB형이다. 오버워치와 배틀그라운드 모바일을 즐겨하며, 오버워치를 순수하게 즐기는 빠대만 돌리는 유저이다. 메르시 원챔이면서도 메르시보다 모이라를 재밌어한다. 무엇보다 힐러 역할을 즐겨하면서 정치질을 대놓고는 안한다. 이게 빠대의 장점인가 ...? ', inline=False)
        await message.channel.send(channel,embed=embed)
        
        
    if message.content.startswith("?도리도리곰도리"):
        channel = message.channel
        embed = discord.Embed(
            title = 'Introducing 도리도리곰도리  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"")
        embed.add_field(name = '도리도리곰도리', value = '2000년 봄과 여름의 사이인 달에 태어난 여자아이다. 사실 남자인척 하는 유우명한 넷카마였지만, 이제는 여자라고 하면 오히려 넷카마 취급 받는다. 주 활동 갤러리는 겨울왕국 갤러리이며, 디스코드 태그는 도리봇#2014 이다.',inline = False)
        embed.add_field(name='그녀의', value='MBTI는 ENFP 이고, 혈액형은 O형 이다. 배틀그라운드 모바일을 즐겨한다. 현재는 빡겜 위주 플레이보다 즐겜 위주 플레이를 더 원한다. 이유는 배틀그라운드 모바일 핵쟁이들 때문.', inline=False)
        embed.add_field(name='왜', value='게임상에서 마이크를 쓰지않냐면 사실 트라우마 때문이다. 아주 못된 한남 냄져 유충들때문에 마음의 상처를 얻었다. 그녀는 한남을 혐오한다. 아니 죽여버리고 싶어한다.  ', inline=False)        
        await message.channel.send(channel,embed=embed)        
        
    if message.content.startswith('?도리도리곰도리'):                
        embed = discord.Embed(
        title='',
        description='',

        )

        urlBase = 'https://i.imgur.com/Ny6e2BS.jpg'                      
        randomNum = random.randrange(1, 2)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await message.channel.send( embed=embed)

    if message.content.startswith('??7호선'):                      
        embed = discord.Embed(
        title='',
        description='',

        )

        urlBase = 'https://i.imgur.com/OzuHWX1.jpg'
        randomNum = random.randrange(1, 2)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await message.channel.send( embed=embed)

    if message.content.startswith('?나냡'):                      
        embed = discord.Embed(
        title='',
        description='',

        )

        urlBase = 'https://i.imgur.com/BXaGTeC.jpg'
        randomNum = random.randrange(1, 2)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await message.channel.send( embed=embed)
        
    if message.content.startswith('?도리도리곰도리'):                 
        embed = discord.Embed(
        title='',
        description='',

        )

        urlBase = 'https://i.imgur.com/vRpRYu5.jpg'
        randomNum = random.randrange(1, 2)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await message.channel.send( embed=embed)

    if message.content.startswith('??7호선'):                        
        embed = discord.Embed(
        title='',
        description='',

        )

        urlBase = 'https://i.imgur.com/orOghv1.jpg'
        randomNum = random.randrange(1, 2)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await message.channel.send( embed=embed)

    if message.content.startswith('?나냡'):                           
        embed = discord.Embed(
        title='',
        description='',

        )

        urlBase = 'https://i.imgur.com/Bb4mWtS.jpg'
        randomNum = random.randrange(1, 2)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await message.channel.send( embed=embed)

        
    if message.content.startswith('?Erangel'):
        embed = discord.Embed(
        title='',
        description='',

        )

        urlBase = 'https://i.imgur.com/fNj59oD.png'
        randomNum = random.randrange(1, 2)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await message.channel.send( embed=embed)


    if message.content.startswith('?Miramar'):
        embed = discord.Embed(
        title='',
        description='',

        )

        urlBase = 'https://i.imgur.com/Lf8OOXZ.png'
        randomNum = random.randrange(1, 2)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await message.channel.send( embed=embed)


    if message.content.startswith('?Sanhok'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/FAdN4Kk.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send( embed=embed)


    if message.content.startswith('?Vikendi'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/WzuS5TS.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send( embed=embed)

    if message.content.startswith('?Karakin'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/8Fh2bes.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send( embed=embed)
         
        
    if message.content.startswith('?HAVEN'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/MRVDJqa.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send( embed=embed)
         
         
    if message.content.startswith("ㅋㅋㅋ"):     

        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "] 

        randomNum = random.randrange(0, len(emoji)) 
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])
        await message.channel.send(embed=discord.Embed(description=emoji[randomNum], color=0xff0000))  
        
        


    if message.content.startswith("?Corona"):     

        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "] 

        randomNum = random.randrange(0, len(emoji)) 
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])
        await message.channel.send(embed=discord.Embed(description=emoji[randomNum], color=0xff0000))


    if message.content.startswith("?help"):     

        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "] 

        randomNum = random.randrange(0, len(emoji)) 
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])
        await message.channel.send(embed=discord.Embed(description=emoji[randomNum], color=0xff0000))   
         

    if message.content.startswith("?MBTI"):     

        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "] 

        randomNum = random.randrange(0, len(emoji)) 
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])
        await message.channel.send(embed=discord.Embed(description=emoji[randomNum], color=0xff0000))

    if message.content.startswith("?Blood type"):     

        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "] 

        randomNum = random.randrange(0, len(emoji)) 
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])
        await message.channel.send(embed=discord.Embed(description=emoji[randomNum], color=0xff0000))

        
        
        
    if message.content.startswith("?Recommend a PC game"):      
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"", color=0xff0000)
        await message.channel.send(embed=embed)
        randomNum = random.randrange(1, 10)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="BattleState Games에서 개발한 하드코어 내러티브 MMO FPS 오픈 월드 게임, 이스케이프 프롬 타르코프를 추천합니다. 대신, 환불은 불가능합니다. 환불하면 하드웨어 밴이라는 사실을 항상 명심하세요.", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="블리자드 엔터테인먼트의 팀 기반 멀티플레이 하이퍼 FPS 게임, 오버워치를 추천합니다. 경쟁전을 제외하면 이만한 갓겜이 없습니다. 대신, 채팅을 자제하세요. 신고가 누적되면 욕설을 하지 않아도 정지를 먹습니다. 정지가 반복되면 마지막은 영구 정지 입니다. ", color=0x00ff00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="라이엇 게임즈가 개발 및 서비스 중인 MOBA 장르의 게임, 리그오브레전드를 추천합니다. 멘탈이 튼튼하다면 엄청난 갓겜이죠. ", color=0x00ff00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title=" 크래프톤의 자회사인 펍지 주식회사의 MMO 슈팅 게임, PLAYERUNKNOWN'S BATTLEGROUNDS, 약칭 배틀그라운드를 추천합니다. 허가받지 않은 비인가 프로그램을 사용하는 비매너 이용자들을 만나서 스트레스를 받는 상황을 제외한다면 국내 1위 인기 게임 리그오브레전드를 압살할 정도로 재미를 선사해주는 갓겜 입니다. 하지만, 이 게임 또한 멘탈이 튼튼해야합니다. 배틀그라운드 모바일 덕분에 유입한 어린 친구들 때문에 게임이 많이 더러워졌습니다. ", color=0x00ff00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="하이레즈 스튜디오의 하이퍼 FPS 기반의 팀 플레이 멀티플레이 FPS 게임, 팔라딘스는 한때 2016년도 국내 1위 게임 오버워치를 표절했다는 오해를 받았었죠. 하이퍼 FPS 장르를 좋아한다면 한번쯤은 해볼만한 갓겜입니다. ", color=0x00ff00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="넥슨의 로두마니 스튜디오에서 크레이지 아케이드의 캐릭터를 개발해 2004년 출시한 한국의 온라인 레이싱 게임, 크레이지레이싱 카트라이더를 추천합니다. 그냥 갓겜 그자체입니다. ", color=0x00ff00))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="2011년에 정식 발매된 Mojang 스튜디오의 샌드박스 형식의 비디오 게임, 마인크래프트를 추천합니다. 이 게임 또한 갓겜 그자체죠. ", color=0x00ff00))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="라이엇 게임즈가 처음으로 개발한 카운터 스트라이크 스타일의 1인칭 슈팅 게임, 발로란트를 추천합니다. 다만, 오버워치 급 퀄리티를 기대하는 사람들에게는 비추천 드립니다. ", color=0x00ff00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="2013년 9월 17일, 락스타 게임즈에서 모두가 기다렸던 대작 락스타 노스가 개발한 Grand Theft Auto 시리즈의 15번째 작품인 'GTA 5'를 추천합니다. 두말 할것도 없죠. 사이버 펑크보다는 GTA5를 추천 합니다. ", color=0x00ff00))

          
          
    if message.content.startswith("?Recommend a MOBILE game"):       
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"", color=0xff0000)
        await message.channel.send(embed=embed)
        randomNum = random.randrange(1, 7)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="배틀그라운드의 모바일 버전으로 2018년 5월 16일, 국내에서 서비스가 시작된 배틀그라운드 모바일을 추천합니다. 허가받지 않은 비인가 프로그램을 사용하는 비매너 유저들을 만나 스트레스를 받는 상황만 제외한다면 어몽어스, 리그오브레전드 와일드 리프트, 카트라이더 러쉬 플러스, 콜 오브 듀티 모바일, 포트나이트 같은 게임들보다 재미를 선사하는 갓겜 입니다. 대신, 어린 친구들이 체감상 유저들의 90 퍼센트를 차지합니다. ", color=0x0000ff))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="InnerSloth에서 제작한 마피아 형식의 생존 게임, 어몽어스를 추천합니다. ", color=0x0000ff))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="2020년 5월 12일 한국에 정식으로 출시된 넥슨의 모바일 레이싱 게임, 카트라이더 러쉬 플러스를 추천합니다. 두말 할것도 없는 갓겜 그자체죠. ", color=0x0000ff))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="라이엇 게임즈에서 발표한 리그 오브 레전드의 모바일 및 콘솔 버전, 리그오브레전드: 와일드 리프트를 추천합니다. ", color=0x0000ff))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="액티비전이 콜 오브 듀티 시리즈의 IP를 제공하고, 텐센트 산하 개발사인 Timi Studio에서 제작하는 콜 오브 듀티 시리즈의 모바일 게임, 콜 오브 듀티: 모바일을 추천합니다. 가볍게 시간 때우기에는 이만한 게임이 없죠. ", color=0x0000ff))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="붕괴학원2와 붕괴3rd의 개발사인 miHoYo에서 제작한 3D 오픈 월드 액션 어드벤처 게임, 원신을 추천합니다. ", color=0x0000ff))  
          
          
    if message.content.startswith("?Dice"):          
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"", color=0xff0000)
        await message.channel.send(embed=embed)        
        randomNum = random.randrange(1, 7) 
        print(randomNum)
        if randomNum == 1:
            await message.channel.send( embed=discord.Embed(description=':game_die: '+ ':one:',color=0xfefe00))
        if randomNum == 2:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':two:',color=0xfefe00))
        if randomNum ==3:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':three:',color=0xfefe00))
        if randomNum ==4:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':four:',color=0xfefe00))
        if randomNum ==5:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':five:',color=0xfefe00))
        if randomNum ==6:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':six: ',color=0xfefe00))
          
          
    if message.content.startswith("?Recommend a Youtuber"):             
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"", color=0xff0000)
        await message.channel.send(embed=embed)        
        randomNum = random.randrange(1, 8)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="대한민국의 유튜버이며 아프리카TV BJ, 보겸을 추천합니다. ", color=0xff0000))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="여러가지 IT 관련 제품을 리뷰하는 유튜버이자 영원한 서울섹스킹, 잇섭을 추천합니다. ", color=0xff0000))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="트위치와 유튜브에서 활동하고 있는 샌드박스 네트워크 소속 종합 게임 크리에이터, 김블루를 추천합니다. 단점은 주 시청자들이 좀 많이 어립니다. ", color=0xff0000))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="종합게임유튜버이자 트위치 스트리머인 군림보를 추천합니다. 장점은 주 시청자들이 나이대가 어느정도 있습니다. ", color=0xff0000))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="더이상 추천할만한 유튜버가 없는 것 같습니다. ", color=0xff0000))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="전자제품에 관심이 많다면, EverythingApplePro EAP를 추천합니다.", color=0xff0000))            
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="대한민국의 궁금증 해결 유튜버 겸 래퍼, 진용진을 추천합니다.", color=0xff0000))
          
    if message.content.startswith("?자살"):       
        randomNum = random.randrange(1, 7)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="'자살은 스스로 품은 의지를 통해 자기 생명을 해쳐서 죽음이라는 결과에 이르는 자멸 행위이다.' -세계보건기구-", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="'희생자 자신이 결과를 알면서도 적극적, 소극적 행동으로 직접, 또는 타인을 통해 행하는 죽음을 자살이라고 부른다.' -에밀 뒤르켐(1897)-", color=0x00ff00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="'사망자 자신이 희생이 아닌 어떠한 의도를 가지고 혹은 죽음을 위해 행한 행위가 일으킨 죽음을 모두 자살이라고 부른다.' -알버크(1930)-", color=0x00ff00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="'자살은 삶을 선택할 수도 있겠지만 모든 사회적 의무에서 벗어나기 위해 죽음을 고른 명석한 인간이 행한 행위를 말한다.' -아킬 델마(1932)-", color=0x00ff00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="'자살은 죽음을 수단이나 결과로 여겨 스스로 죽는 행위다.' -드에(1947)-", color=0x00ff00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="'자살은 실존에 관한 문제를 해결하는 방법을 주체의 자발적인 죽음에서 구하고 찾는 일이다.' -바에슐러(1975)-", color=0x00ff00))
          
        
    if message.content.startswith("?Today's Poetry"):
        randomNum = random.randrange(1, 15)
        if randomNum==1:
            await message.channel.send("방문객")
            await message.channel.send("정현종 시인")
            await message.channel.send("============")
            await message.channel.send("[사람]이 온다는 건")
            await message.channel.send("실로 어마어마한 일이다.")
            await message.channel.send("그는")
            await message.channel.send("그의 과거와")
            await message.channel.send("현재와")
            await message.channel.send("그리고")
            await message.channel.send("그의 미래가 함께 오기 때문이다.")
            await message.channel.send("한 사람의 일생이 오기 때문이다.")
            await message.channel.send("부서지기 쉬운")
            await message.channel.send("그래서 부서지기도 했을")
            await message.channel.send("마음이 오는 것이다 -그 갈피를")
            await message.channel.send("아마 마음은 더듬어볼 수 있을 ")
            await message.channel.send("마음, ")
            await message.channel.send("내 마음이 그런 바람을 흉내낸다면 ")
            await message.channel.send("필경 환대가 될 것이다. ")
        if randomNum==2:
            await message.channel.send("바다")
            await message.channel.send("윤동주 시인")
            await message.channel.send("===========")
            await message.channel.send("실어다 뿌리는 ")
            await message.channel.send("바람조차 시원타.")
            await message.channel.send("===========")
            await message.channel.send("솔나무 가지마다 새촘히 ")
            await message.channel.send("고개를 돌리어 뻐들어지고,")
            await message.channel.send("===========")
            await message.channel.send("밀치고 ")
            await message.channel.send("밀치운다.")
            await message.channel.send("===========")
            await message.channel.send("이랑을 넘은 물결은 ")
            await message.channel.send("폭포처럼 피어오른다.")
            await message.channel.send("===========")
            await message.channel.send("해변에 아이들이 모인다")
            await message.channel.send("찰찰 손을 씻고 구보로,")
            await message.channel.send("바다는 자꾸 설워진다.")
            await message.channel.send("갈매기의 노래에 .....")
            await message.channel.send("===========")
            await message.channel.send("돌아다보고 돌아다보고")
            await message.channel.send("돌아가는 오늘의 바다여!")
        if randomNum==3:
            await message.channel.send("흔들리며 피는 꽃")
            await message.channel.send("도종환 시인")
            await message.channel.send("===========")
            await message.channel.send("흔들리지 않고 피는 꽃이 어디 있으랴")
            await message.channel.send("이 세상 그 어떤 아름다운 꽃들도")
            await message.channel.send("다 흔들리면서 피었나니")
            await message.channel.send("흔들리면서 줄기를 곧게 세웠나니")
            await message.channel.send("흔들리지 않고 가는 사람이 어디 있으랴")
            await message.channel.send("===========")
            await message.channel.send("젖지않고 피는 꽃이 어디 있으랴")
            await message.channel.send("이 세상 그 어떤 빛나는 꽃들도")
            await message.channel.send("다 젖으며 젖으며 피었나니")
            await message.channel.send("바람과 비에 젖으며 꽃잎 따뜻하게 피웠나니")
            await message.channel.send("젖지 않고 가는 삶이 어디 있으랴")
        if randomNum==4:
            await message.channel.send("하늘 냄새")
            await message.channel.send("박희순 시인")
            await message.channel.send("===========")
            await message.channel.send("[사람]이")
            await message.channel.send("하늘처럼")
            await message.channel.send("맑아 보일 때가 있다.")
            await message.channel.send("===========")
            await message.channel.send("그때 나는 ")
            await message.channel.send("그 사람에게서")
            await message.channel.send("하늘 냄새를 맡는다.")
        if randomNum==5:
            await message.channel.send("호수")
            await message.channel.send("정지용 시인")
            await message.channel.send("===========")
            await message.channel.send("얼굴 하나야")
            await message.channel.send("손바닥 둘로 ")
            await message.channel.send("푹 가리지만")
            await message.channel.send("===========")
            await message.channel.send("보고 싶은 마음 ")
            await message.channel.send("호수만 하니")
            await message.channel.send("눈 감을 수 밖에")
        if randomNum==6:
            await message.channel.send("그 꽃")
            await message.channel.send("고은 시인")
            await message.channel.send("===========")
            await message.channel.send("내려갈 때 보았네")
            await message.channel.send("올라갈 때 못 본 그 꽃")
        if randomNum==7:
            await message.channel.send("행복")
            await message.channel.send("나태주 시인")
            await message.channel.send("===========")
            await message.channel.send("저녁 때")
            await message.channel.send("돌아갈 집이 있다는 것 ")
            await message.channel.send("===========")
            await message.channel.send("힘들 때")
            await message.channel.send("마음 속에 생각나는 사람이 있다는 것 ")
            await message.channel.send("===========")
            await message.channel.send("외로울 때")
            await message.channel.send("혼자서 부를 노래가 있다는 것")
        if randomNum==8:
            await message.channel.send("풀꽃")
            await message.channel.send("나태주 시인")
            await message.channel.send("===========")
            await message.channel.send("자세히 보아야 ")
            await message.channel.send("예쁘다 ")
            await message.channel.send("===========")
            await message.channel.send("오래보아야 ")
            await message.channel.send("사랑스럽다 ")
            await message.channel.send("===========")
            await message.channel.send("너도 그렇다")
        if randomNum==9:
            await message.channel.send("너 외롭구나")
            await message.channel.send("김형태 시인")
            await message.channel.send("===========")
            await message.channel.send("깊이 ")
            await message.channel.send("=========== ")
            await message.channel.send("앓으십시요")
            await message.channel.send("앓음답도록 ")
            await message.channel.send("아름답도록")
        if randomNum==10:
            await message.channel.send("가을")
            await message.channel.send("한민복 시인")
            await message.channel.send("===========")
            await message.channel.send("그대 생각을  ")
            await message.channel.send("켜 놓은 채 ")
            await message.channel.send("잠이 들었습니다")   
        if randomNum==11:
            await message.channel.send("엄마야 누나야")
            await message.channel.send("김소월 시인")
            await message.channel.send("===========")
            await message.channel.send("[엄마]야 누나야 강변 살자  ")
            await message.channel.send("뜰에는 반짝이는 금모래 빛 ")
            await message.channel.send("뒷문 밖에는 갈잎의 노래")
            await message.channel.send("[엄마]야 누나야 강변 살자")
        if randomNum==12:
            await message.channel.send("꽃")
            await message.channel.send("김춘수 시인")
            await message.channel.send("===========")
            await message.channel.send("내가 그의 이름을 불러 주기 전에는  ")
            await message.channel.send("그는 다만 ")
            await message.channel.send("하나의 몸짓에 지나지 않았다.")
            await message.channel.send("===========")   
            await message.channel.send("내가 그의 이름을 불러 주었을 때  ")
            await message.channel.send("그는 나에게로 와서 ")
            await message.channel.send("꽃이 되었다.")
            await message.channel.send("===========")   
            await message.channel.send("내가 그의 이름을 불러 준 것처럼  ")
            await message.channel.send("나의 이 빛깔과 향기에 알맞는 ")
            await message.channel.send("누가 나의 이름을 불러다오.")
            await message.channel.send("그에게로 가서 나도 그의 꽃이 되고 싶다.")  
            await message.channel.send("===========") 
            await message.channel.send("우리들은 모두  ")
            await message.channel.send("무엇이 되고 싶다.")
            await message.channel.send("너는 나에게 나는 너에게")
            await message.channel.send("잊혀지지 않는 하나의 눈짓이 되고 싶다.")  
        if randomNum==13:
            await message.channel.send("서시")
            await message.channel.send("윤동주 시인")
            await message.channel.send("===========")
            await message.channel.send("[죽는] 날까지 하늘을 우러러  ")
            await message.channel.send("한 점 부끄럼 없기를 ")
            await message.channel.send("잎새에 이는 바람에도")
            await message.channel.send("나는 괴로워했다.")   
            await message.channel.send("============  ")
            await message.channel.send("별을 노래하는 마음으로 ")
            await message.channel.send("모든 죽어가는 것들을 사랑해야지")
            await message.channel.send("그리고 나에게 주어진 길을 걸어가야겠다.")   
            await message.channel.send("============ ")
            await message.channel.send("오늘 밤에도 별이 바람에 스치운다. ")   
        if randomNum==14:
            await message.channel.send("토닥토닥")
            await message.channel.send("김재진 시인")
            await message.channel.send("===========")
            await message.channel.send("나는 너를 토닥거리고  ")
            await message.channel.send("너는 나를 토닥거린다. ")
            await message.channel.send("삶이 자꾸 아프다고 말하고")
            await message.channel.send("너는 자꾸 괜찮다고 말한다.")   
            await message.channel.send("바람이 불어도 괜찮다. ")
            await message.channel.send("혼자 있어도 괜찮다. ")
            await message.channel.send("너는 자꾸 토닥거린다.")
            await message.channel.send("나도 자꾸 토닥거린다.")   
            await message.channel.send("============ ")
            await message.channel.send("다 지나간다고 ")  
            await message.channel.send("다 지나갈거라고 ") 
            await message.channel.send("토닥거리다가 잠든다. ")             
            
            
                  
    if message.content.startswith("?MBTI"):
        await message.channel.send("What is your MBTI? ")
        await message.channel.send("Example) ?ENFP ")

    if message.content.startswith("?Blood type"):
        await message.channel.send("What is your Blood type? ")
        await message.channel.send("Example) ?O (Exception: ??AB)")
       
    if message.content.startswith("?Personal Color Test"):                           #Korean Part
        await message.channel.send("아직, 자기 유형을 모르신다면,")
        await message.channel.send("아래 주소를 클릭해서 테스트를 먼저 받고 오세요!")
        await message.channel.send("대부분, 자신의 MBTI 유형과 동일할겁니다.")
        await message.channel.send("[띄어쓰기 필요없습니다]")
        await message.channel.send("https://kapable.github.io/kapable.github.io/personalColor/")
        await message.channel.send("당신의 퍼스널컬러를 채팅창에 입력해주세요. ")
        await message.channel.send("Example) ?댄덜라이언 ")      

    if message.content.startswith('?다우니'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/mHVgxSY.jpg'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 다우니이며,")
         await message.channel.send("MBTI 결과는 ENFJ 일것입니다. ")
         await message.channel.send( embed=embed) 
         
    if message.content.startswith('?오션딥스'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/CXLBolu.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 오션딥스이며,")
         await message.channel.send("MBTI 결과는 ISTP 일것입니다. ")
         await message.channel.send( embed=embed)   
         
    if message.content.startswith('?오아시스'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/EVtYA0i.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 오아시스이며,")
         await message.channel.send("MBTI 결과는 ISFJ 일것입니다. ")
         await message.channel.send( embed=embed) 
         
    if message.content.startswith('?스프라우트'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/sW8MfNE.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 스프라우트이며,")
         await message.channel.send("MBTI 결과는 ISFP 일것입니다. ")
         await message.channel.send( embed=embed)  
         
    if message.content.startswith('?퀼트스'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/yTo6NJf.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 퀼트스이며,")
         await message.channel.send("MBTI 결과는 INTJ 일것입니다. ")
         await message.channel.send( embed=embed)  
         
    if message.content.startswith('?세룰리안'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/EhHQNqr.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 세룰리안이며,")
         await message.channel.send("MBTI 결과는 INTP 일것입니다. ")
         await message.channel.send( embed=embed)  
         
    if message.content.startswith('?엘리스블루'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/N2Ef2KA.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 엘리스블루이며,")
         await message.channel.send("MBTI 결과는 INTJ 일것입니다. ")
         await message.channel.send( embed=embed) 
         
    if message.content.startswith('?켁터스'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/O0jI0Va.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 켁터스이며,")
         await message.channel.send("MBTI 결과는 ESTJ 일것입니다. ")
         await message.channel.send( embed=embed)  
         
    if message.content.startswith('?오션베이'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/vAikndR.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 오션베이이며,")
         await message.channel.send("MBTI 결과는 INFP 일것입니다. ")
         await message.channel.send( embed=embed)  
         
    if message.content.startswith('?로즈버드'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/P0pHIFN.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 로즈버드이며,")
         await message.channel.send("MBTI 결과는 ESTP 일것입니다. ")
         await message.channel.send( embed=embed)
         
    if message.content.startswith('?바닐라아이스'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/8mVipiA.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 바닐라아이스이며,")
         await message.channel.send("MBTI 결과는 ESFJ 일것입니다. ")
         await message.channel.send( embed=embed)  
         
    if message.content.startswith('?스위트핑크'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/nWCQhSt.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 스위트핑크이며,")
         await message.channel.send("MBTI 결과는 ESFP 일것입니다. ")
         await message.channel.send( embed=embed)  
         
    if message.content.startswith('?네이비피오니'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/O7XU9LL.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 네이비피오니이며,")
         await message.channel.send("MBTI 결과는 ENTJ 일것입니다. ")
         await message.channel.send( embed=embed)  
         
    if message.content.startswith('?웜플레임'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/DoqNeiD.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 웜플레임이며,")
         await message.channel.send("MBTI 결과는 ENTP 일것입니다. ")
         await message.channel.send( embed=embed)  
         
    if message.content.startswith('?댄덜라이언'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/gbJELoA.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 댄덜라이언이며,")
         await message.channel.send("MBTI 결과는 ENFP 일것입니다. ")
         await message.channel.send( embed=embed)  
         
    if message.content.startswith('?페리글라스블루'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/d37AMyW.png'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("당신의 퍼스널컬러 결과는 페리글라스블루이며,")
         await message.channel.send("MBTI 결과는 ISTJ 일것입니다. ")
         await message.channel.send( embed=embed)   
         
    if message.content.startswith('냄새'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/K80xJ5X.jpeg'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("[이상한 냄새에 대한 기억]")
         await message.channel.send("[#냄새]")
         await message.channel.send( embed=embed)       
         
    if message.content.startswith('!MBTI 연애'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/7NpTDDl.jpeg'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send("{MBTI} 유형별 사랑의 성숙도 순위")
         await message.channel.send("[#2001년]")
         await message.channel.send( embed=embed)             
         
         
         
         
     
       
    if message.content == "?My real name":
        channel = message.channel
        urllib.request.urlretrieve("https://i.imgur.com/KoougXb.jpeg", "explain.png")
        image = discord.File("explain.png", filename="image.png")
        embed = discord.Embed(title="My real name", description=".", color=0x00ff56)
        embed.set_thumbnail(url="https://i.imgur.com/P6HdGr1.png")
        embed.add_field(name=".", value=". ", inline=True)
        await channel.send(embed=embed, file=image)

    if message.content.startswith("?PUBG Competitive mode1"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았어요 :)", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command ?컴배경쟁전(1 : TPP or 2 : FPP) : ?컴배경쟁전 (Nickname)", inline=False)

                await message.channel.send("Error : Incorrect command usage ", embed=embed)
            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                
                
                rankElements = bs.findAll('div',{'class' : re.compile('squad ranked [A-Za-z0-9]')})
                
                '''
                -> 클래스 값을 가져와서 판별하는 것도 있지만 이 방법을 사용해 본다.
                -> 만약 기록이 존재 하지 않는 경우 class 가 no_record라는 값을 가진 <div>가 생성된다. 이 태그로 데이터 유무 판별하면된다.
                print(rankElements[1].find('div',{'class' : 'no_record'}))
                '''
                
                if rankElements[0].find('div',{'class' : 'no_record'}) != None: 
                    embed = discord.Embed(title="Record not found", description="Rank TPP record not found.",color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)

                    await message.channel.send("PUBG player " + playerNickname + "'s TPP Ranking information",embed=embed) 
                else:
                   
                    fR = rankElements[0]
                    
    
                    
                    tierMedalImage = fR.find('div',{'class' : 'grade-info'}).img['src']
                    
                    tierInfo = fR.find('div',{'class' : 'grade-info'}).img['alt']
    

                    
                    RPScore = fR.find('div',{'class' : 'rating'}).find('span',{'class' : 'caption'}).text
    
                    
                    
                    
                    topRatioRank  = topRatio = fR.find('p',{'class' : 'desc'}).find('span',{'class' : 'rank'}).text     
                                             
                    topRatio = fR.find('p',{'class' : 'desc'}).find('span',{'class' : 'top'}).text
    
                    
    
                    mainStatsLayout = fR.find('div',{'class' : 'stats'})
    
                    
    
                    statsList = mainStatsLayout.findAll('p',{'class' : 'value'})
                    statsRatingList = mainStatsLayout.findAll('span',{'class' : 'top'})
            
                    for r in range(0,len(statsList)):
                    
                        statsList[r] = statsList[r].text.strip().split('\n')[0]
                        statsRatingList[r] = statsRatingList[r].text
                    
                    statsRatingList = statsRatingList[0:5]
                                               
                    
                    embed = discord.Embed(title="핵틀그라운드  search from dak.gg", description="",color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)  
                    embed.add_field(name="Player located server", value=seasonInfo[2] + " Server", inline=False)
                    embed.add_field(name = "Tier / Top Rate / Average Rank",
                                   value = tierInfo + " (" + RPScore + ") / "+topRatio + " / " + topRatioRank,inline=False)
                    embed.add_field(name="K/D", value=statsList[0] + "/" + statsRatingList[0], inline=True)
                    embed.add_field(name="승률", value=statsList[1] + "/" + statsRatingList[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=statsList[2] + "/" + statsRatingList[2], inline=True)
                    embed.add_field(name="평균딜량", value=statsList[3] + "/" + statsRatingList[3], inline=True)
                    embed.add_field(name="게임수", value=statsList[4] + "판/" + statsRatingList[4], inline=True)
                    embed.add_field(name="평균등수", value=statsList[5],inline=True)
                    embed.set_thumbnail(url=f'https:{tierMedalImage}')

                    await message.channel.send("PUBG player " + playerNickname + "'s TPP Ranking information", embed=embed)
                    
            
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer", description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
            print(e)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
            print(e)
    
    if message.content.startswith("?PUBG Competitive mode2"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command ?컴배경쟁전(1 : TPP or 2 : FPP) : ?컴배경쟁전 (Nickname)", inline=False)

                await message.channel.send("Error : Incorrect command usage ", embed=embed)
            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))



                
                
                rankElements = bs.findAll('div',{'class' : re.compile('squad ranked [A-Za-z0-9]')})
                
                '''
                -> 클래스 값을 가져와서 판별하는 것도 있지만 이 방법을 사용해 본다.
                -> 만약 기록이 존재 하지 않는 경우 class 가 no_record라는 값을 가진 <div>가 생성된다. 이 태그로 데이터 유무 판별하면된다.
                print(rankElements[1].find('div',{'class' : 'no_record'}))
                '''
                
                if rankElements[1].find('div',{'class' : 'no_record'}) != None: 
                    embed = discord.Embed(title="Record not found", description="Solo que record not found.",
                                          color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)

                    await message.channel.send("PUBG player " + playerNickname + "'s FPP Ranking information",embed=embed) 
                else:
                    
                    fR = rankElements[1]
                    
    
                    
                    tierMedalImage = fR.find('div',{'class' : 'grade-info'}).img['src']
                    
                    tierInfo = fR.find('div',{'class' : 'grade-info'}).img['alt']
    
                    
                    
                    RPScore = fR.find('div',{'class' : 'rating'}).find('span',{'class' : 'caption'}).text
    
                    
                    
                    
                    topRatioRank  = topRatio = fR.find('p',{'class' : 'desc'}).find('span',{'class' : 'rank'}).text     
                                              
                    topRatio = fR.find('p',{'class' : 'desc'}).find('span',{'class' : 'top'}).text
    
                    
    
                    mainStatsLayout = fR.find('div',{'class' : 'stats'})
    
                    
    
                    statsList = mainStatsLayout.findAll('p',{'class' : 'value'})
                    statsRatingList = mainStatsLayout.findAll('span',{'class' : 'top'})
            
                    for r in range(0,len(statsList)):
                    
                        statsList[r] = statsList[r].text.strip().split('\n')[0]
                        statsRatingList[r] = statsRatingList[r].text
                    
                    statsRatingList = statsRatingList[0:5]
                                               
                    
                    embed = discord.Embed(title="핵틀그라운드  search from dak.gg", description="",color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)  
                    embed.add_field(name="Player located server", value=seasonInfo[2] + " Server", inline=False)
                    embed.add_field(name = "Tier / Top Rate / Average Rank",
                                   value = tierInfo + " (" + RPScore + ") / "+topRatio + " / " + topRatioRank,inline=False)
                    embed.add_field(name="K/D", value=statsList[0] + "/" + statsRatingList[0], inline=True)
                    embed.add_field(name="승률", value=statsList[1] + "/" + statsRatingList[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=statsList[2] + "/" + statsRatingList[2], inline=True)
                    embed.add_field(name="평균딜량", value=statsList[3] + "/" + statsRatingList[3], inline=True)
                    embed.add_field(name="게임수", value=statsList[4] + "판/" + statsRatingList[4], inline=True)
                    embed.add_field(name="평균등수", value=statsList[5],inline=True)
                    embed.set_thumbnail(url=f'https:{tierMedalImage}')

                    await message.channel.send("PUBG player " + playerNickname + "'s FPP Ranking information", embed=embed)
                    
            
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer", description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)

    if message.content.startswith("?PUBG Solo mode1"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command ?컴배솔로 : ?컴배솔로 (Nickname)", inline=False)

                await message.channel.send("Error : Incorrect command usage ", embed=embed)

            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                

                soloQueInfo = bs.find('section', {'class': "solo modeItem"}).find('div', {'class': "mode-section tpp"})
                if soloQueInfo == None:
                    embed = discord.Embed(title="Record not found", description="Solo que record not found.",
                                          color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    await message.channel.send("PUBG player " + playerNickname + "'s TPP solo que information", embed=embed)
                else:
                    
                    
                    soloQueTotalPlayTime = soloQueInfo.find('span', {'class': "time_played"}).text.strip()
                    
                    soloQueGameWL = soloQueInfo.find('em').text.strip().split(' ')
                    
                    rankPoint = soloQueInfo.find('span', {'class': 'value'}).text
                    
                    tierInfos = soloQueInfo.find('img', {
                        'src': re.compile('\/\/static\.dak\.gg\/images\/icons\/tier\/[A-Za-z0-9_.]')})
                    tierImage = "https:" + tierInfos['src']
                    print(tierImage)
                    tier = tierInfos['alt']

                    
                    comInfo = []
                    
                    for ci in soloQueInfo.findAll('p', {'class': 'value'}):
                        comInfo.append(''.join(ci.text.split()))

                    embed = discord.Embed(title="핵틀그라운드  search from dak.gg", description="",
                                          color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)
                    embed.add_field(name="Player located server", value=seasonInfo[2] + " Server / Total playtime : " +soloQueTotalPlayTime, inline=False)
                    embed.add_field(name="Tier",
                                    value=tier + " ("+rankPoint+"p)" , inline=False)
                    embed.add_field(name="K/D", value=comInfo[0], inline=True)
                    embed.add_field(name="승률", value=comInfo[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=comInfo[2], inline=True)
                    embed.add_field(name="평균딜량", value=comInfo[3], inline=True)
                    embed.add_field(name="게임수", value=comInfo[4] + "판", inline=True)
                    embed.add_field(name="최다킬수", value=comInfo[5] + "킬", inline=True)
                    embed.add_field(name="헤드샷 비율", value=comInfo[6], inline=True)
                    embed.add_field(name="저격거리", value=comInfo[7], inline=True)
                    embed.add_field(name="평균생존시간", value=comInfo[8], inline=True)

                    await message.channel.send("PUBG player " + playerNickname + "'s TPP solo que information", embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer", description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)

    if message.content.startswith("?PUBG Duo mode1"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command ?컴배스쿼드 : ?컴배스쿼드 (Nickname)", inline=False)

                await message.channel.send("Error : Incorrect command usage ", embed=embed)

            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                

                duoQueInfo = bs.find('section',{'class' : "duo modeItem"}).find('div',{'class' : "mode-section tpp"})
                if duoQueInfo == None:
                    embed = discord.Embed(title="Record not found", description="Duo que record not found.",
                                          color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    await message.channel.send("PUBG player " + playerNickname + "'s TPP duo que information", embed=embed)
                else:
                    
                    
                    duoQueTotalPlayTime = duoQueInfo.find('span', {'class': "time_played"}).text.strip()
                    
                    duoQueGameWL = duoQueInfo.find('em').text.strip().split(' ')
                    
                    rankPoint = duoQueInfo.find('span', {'class': 'value'}).text
                    
                    tierInfos = duoQueInfo.find('img', {
                        'src': re.compile('\/\/static\.dak\.gg\/images\/icons\/tier\/[A-Za-z0-9_.]')})
                    tierImage = "https:" + tierInfos['src']
                    tier = tierInfos['alt']

                    
                    comInfo = []
                    
                    for ci in duoQueInfo.findAll('p', {'class': 'value'}):
                        comInfo.append(''.join(ci.text.split()))

                    embed = discord.Embed(title="핵틀그라운드  player search from dak.gg", description="",
                                          color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)
                    embed.add_field(name="Player located server and total playtime", value=seasonInfo[2] + " Server / Total playtime : " +duoQueTotalPlayTime, inline=False)
                    embed.add_field(name="Tier(Rank Point)",
                                    value=tier + " ("+rankPoint+"p)", inline=False)
                    embed.add_field(name="K/D", value=comInfo[0], inline=True)
                    embed.add_field(name="승률", value=comInfo[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=comInfo[2], inline=True)
                    embed.add_field(name="평균딜량", value=comInfo[3], inline=True)
                    embed.add_field(name="게임수", value=comInfo[4] + "판", inline=True)
                    embed.add_field(name="최다킬수", value=comInfo[5] + "킬", inline=True)
                    embed.add_field(name="헤드샷 비율", value=comInfo[6], inline=True)
                    embed.add_field(name="저격거리", value=comInfo[7], inline=True)
                    embed.add_field(name="평균생존시간", value=comInfo[8], inline=True)

                    await message.channel.send("PUBG player " + playerNickname + "'s TPP duo que information", embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)

    if message.content.startswith("?PUBG Squad mode1"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command ?컴배솔로 : ?컴배솔로 (Nickname)", inline=False)

                await message.channel.send("Error : Incorrect command usage ", embed=embed)

            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                

                squadQueInfo = bs.find('section',{'class' : "squad modeItem"}).find('div',{'class' : "mode-section tpp"})
                if squadQueInfo == None:
                    embed = discord.Embed(title="Record not found", description="Squad que record not found.",
                                          color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    await message.channel.send("PUBG player " + playerNickname + "'s TPP squad que information", embed=embed)
                else:
                    
                    
                    squadQueTotalPlayTime = squadQueInfo.find('span', {'class': "time_played"}).text.strip()
                    
                    squadQueGameWL = squadQueInfo.find('em').text.strip().split(' ')
                    
                    rankPoint = squadQueInfo.find('span', {'class': 'value'}).text
                    
                    tierInfos = squadQueInfo.find('img', {
                        'src': re.compile('\/\/static\.dak\.gg\/images\/icons\/tier\/[A-Za-z0-9_.]')})
                    tierImage = "https:" + tierInfos['src']
                    tier = tierInfos['alt']

                    
                    comInfo = []
                    
                    for ci in squadQueInfo.findAll('p', {'class': 'value'}):
                        comInfo.append(''.join(ci.text.split()))
                    embed = discord.Embed(title="핵틀그라운드  search from dak.gg", description="",
                                          color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)
                    embed.add_field(name="Player located server", value=seasonInfo[2] + " Server / Total playtime : " +squadQueTotalPlayTime, inline=False)
                    embed.add_field(name="Tier(Rank Point)",
                                    value=tier + " (" + rankPoint + "p)", inline=False)
                    embed.add_field(name="K/D", value=comInfo[0] , inline=True)
                    embed.add_field(name="승률", value=comInfo[1] , inline=True)
                    embed.add_field(name="Top 10 비율", value=comInfo[2] , inline=True)
                    embed.add_field(name="평균딜량", value=comInfo[3] , inline=True)
                    embed.add_field(name="게임수", value=comInfo[4] + "판", inline=True)
                    embed.add_field(name="최다킬수", value=comInfo[5] + "킬", inline=True)
                    embed.add_field(name="헤드샷 비율", value=comInfo[6], inline=True)
                    embed.add_field(name="저격거리", value=comInfo[7], inline=True)
                    embed.add_field(name="평균생존시간", value=comInfo[8], inline=True)

                    await message.channel.send("PUBG player " + playerNickname + "'s TPP squad que information", embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)

    if message.content.startswith("?PUBG Solo mode2"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command ?컴배솔로 : ?컴배솔로 (Nickname)", inline=False)

                await message.channel.send("Error : Incorrect command usage ", embed=embed)

            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                

                soloQueInfo = bs.find('section', {'class': "solo modeItem"}).find('div', {'class': "mode-section fpp"})
                if soloQueInfo == None:
                    embed = discord.Embed(title="Record not found", description="Solo que record not found.",
                                          color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    await message.channel.send("PUBG player " + playerNickname + "'s FPP solo que information",
                                               embed=embed)
                else:
                    
                    
                    soloQueTotalPlayTime = soloQueInfo.find('span', {'class': "time_played"}).text.strip()
                    
                    soloQueGameWL = soloQueInfo.find('em').text.strip().split(' ')
                    
                    rankPoint = soloQueInfo.find('span', {'class': 'value'}).text
                    
                    tierInfos = soloQueInfo.find('img', {
                        'src': re.compile('\/\/static\.dak\.gg\/images\/icons\/tier\/[A-Za-z0-9_.]')})
                    tierImage = "https:" + tierInfos['src']
                    print(tierImage)
                    tier = tierInfos['alt']

                    
                    comInfo = []
                    
                    for ci in soloQueInfo.findAll('p', {'class': 'value'}):
                        comInfo.append(''.join(ci.text.split()))
                    embed = discord.Embed(title="핵틀그라운드  search from dak.gg", description="",
                                          color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)
                    embed.add_field(name="Player located server",
                                    value=seasonInfo[2] + " Server / Total playtime : " + soloQueTotalPlayTime,
                                    inline=False)
                    embed.add_field(name="Tier(Rank Point)",
                                    value=tier + " (" + rankPoint + "p)", inline=False)
                    embed.add_field(name="K/D", value=comInfo[0], inline=True)
                    embed.add_field(name="승률", value=comInfo[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=comInfo[2], inline=True)
                    embed.add_field(name="평균딜량", value=comInfo[3], inline=True)
                    embed.add_field(name="게임수", value=comInfo[4] + "판" , inline=True)
                    embed.add_field(name="최다킬수", value=comInfo[5] + "킬" , inline=True)
                    embed.add_field(name="헤드샷 비율", value=comInfo[6] , inline=True)
                    embed.add_field(name="저격거리", value=comInfo[7], inline=True)
                    embed.add_field(name="평균생존시간", value=comInfo[8] , inline=True)

                    await message.channel.send("PUBG player " + playerNickname + "'s FPP solo que information",
                                               embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)

    if message.content.startswith("?PUBG Duo mode2"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command ?컴배스쿼드 : ?컴배스쿼드 (Nickname)", inline=False)

                await message.channel.send("Error : Incorrect command usage ", embed=embed)

            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                

                duoQueInfo = bs.find('section', {'class': "duo modeItem"}).find('div', {'class': "mode-section fpp"})
                if duoQueInfo == None:
                    embed = discord.Embed(title="Record not found", description="Duo que record not found.",
                                          color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    await message.channel.send("PUBG player " + playerNickname + "'s FPP duo que information",
                                               embed=embed)
                else:
                    
                    
                    duoQueTotalPlayTime = duoQueInfo.find('span', {'class': "time_played"}).text.strip()
                    
                    duoQueGameWL = duoQueInfo.find('em').text.strip().split(' ')
                    
                    rankPoint = duoQueInfo.find('span', {'class': 'value'}).text
                    
                    tierInfos = duoQueInfo.find('img', {
                        'src': re.compile('\/\/static\.dak\.gg\/images\/icons\/tier\/[A-Za-z0-9_.]')})
                    tierImage = "https:" + tierInfos['src']
                    tier = tierInfos['alt']

                    
                    comInfo = []
                    
                    for ci in duoQueInfo.findAll('p', {'class': 'value'}):
                        comInfo.append(''.join(ci.text.split()))
                    embed = discord.Embed(title="핵틀그라운드  search from dak.gg", description="",
                                          color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)
                    embed.add_field(name="Player located server and total playtime",
                                    value=seasonInfo[2] + " Server / Total playtime : " + duoQueTotalPlayTime,
                                    inline=False)
                    embed.add_field(name="Tier(Rank Point)",
                                    value=tier + " (" + rankPoint + "p)", inline=False)
                    embed.add_field(name="K/D", value=comInfo[0] , inline=True)
                    embed.add_field(name="승률", value=comInfo[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=comInfo[2], inline=True)
                    embed.add_field(name="평균딜량", value=comInfo[3], inline=True)
                    embed.add_field(name="게임수", value=comInfo[4] + "판", inline=True)
                    embed.add_field(name="최다킬수", value=comInfo[5] + "킬", inline=True)
                    embed.add_field(name="헤드샷 비율", value=comInfo[6] , inline=True)
                    embed.add_field(name="저격거리", value=comInfo[7] , inline=True)
                    embed.add_field(name="평균생존시간", value=comInfo[8] , inline=True)

                    await message.channel.send("PUBG player " + playerNickname + "'s FPP duo que information",
                                               embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)

    if message.content.startswith("?PUBG Squad mode2"):
        baseURL = "https://dak.gg/profile/"
        playerNickname = ''.join((message.content).split(' ')[1:])
        URL = baseURL + quote(playerNickname)
        try:
            html = urlopen(URL)
            bs = BeautifulSoup(html, 'html.parser')
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="닉네임이 입력되지 않았습니다", description="", color=0x5CD1E5)
                embed.add_field(name="Player nickname not entered",
                                value="To use command ?컴배솔로 : ?컴배솔로 (Nickname)", inline=False)

                await message.channel.send("Error : Incorrect command usage ", embed=embed)

            else:
                accessors = bs.findAll('a', {'href': re.compile('\/statistics\/[A-Za-z]')})

                
                seasonInfo = []
                for si in bs.findAll('li', {'class': "active"}):
                    seasonInfo.append(si.text.strip())
                serverAccessorAndStatus = []
                
                for a in accessors:
                    serverAccessorAndStatus.append(re.sub(pattern='[\n]', repl="", string=a.text.strip()))

                

                squadQueInfo = bs.find('section', {'class': "squad modeItem"}).find('div',
                                                                                    {'class': "mode-section fpp"})
                if squadQueInfo == None:
                    embed = discord.Embed(title="Record not found", description="Squad que record not found.",
                                          color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    await message.channel.send("PUBG player " + playerNickname + "'s FPP squad que information",
                                               embed=embed)
                else:
                    
                    
                    squadQueTotalPlayTime = squadQueInfo.find('span', {'class': "time_played"}).text.strip()
                    
                    squadQueGameWL = squadQueInfo.find('em').text.strip().split(' ')
                    
                    rankPoint = squadQueInfo.find('span', {'class': 'value'}).text
                    
                    tierInfos = squadQueInfo.find('img', {
                        'src': re.compile('\/\/static\.dak\.gg\/images\/icons\/tier\/[A-Za-z0-9_.]')})
                    tierImage = "https:" + tierInfos['src']
                    tier = tierInfos['alt']

                    
                    comInfo = []
                    
                    for ci in squadQueInfo.findAll('p', {'class': 'value'}):
                        comInfo.append(''.join(ci.text.split()))
                    embed = discord.Embed(title="핵틀그라운드  search from dak.gg", description="",
                                          color=0x5CD1E5)
                    embed.add_field(name="Player search from dak.gg", value=URL, inline=False)
                    embed.add_field(name="Real Time Accessors and Server Status",
                                    value="Accessors : " + serverAccessorAndStatus[0] + " | " "Server Status : " +
                                          serverAccessorAndStatus[1].split(':')[-1], inline=False)
                    embed.add_field(name="Player located server",
                                    value=seasonInfo[2] + " Server / Total playtime : " + squadQueTotalPlayTime,
                                    inline=False)
                    embed.add_field(name="Tier(Rank Point)",
                                    value=tier + " (" + rankPoint + "p)", inline=False)
                    embed.add_field(name="K/D", value=comInfo[0], inline=True)
                    embed.add_field(name="승률", value=comInfo[1], inline=True)
                    embed.add_field(name="Top 10 비율", value=comInfo[2], inline=True)
                    embed.add_field(name="평균딜량", value=comInfo[3], inline=True)
                    embed.add_field(name="게임수", value=comInfo[4] + "판", inline=True)
                    embed.add_field(name="최다킬수", value=comInfo[5] + "킬", inline=True)
                    embed.add_field(name="헤드샷 비율", value=comInfo[6] , inline=True)
                    embed.add_field(name="저격거리", value=comInfo[7], inline=True)
                    embed.add_field(name="평균생존시간", value=comInfo[8], inline=True)

                    await message.channel.send("PUBG player " + playerNickname + "'s FPP squad que information",
                                               embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
        except AttributeError as e:
            embed = discord.Embed(title="Not existing plyer",
                                  description="Can't find player " + playerNickname + "'s information.\nPlease check player's nickname again",
                                  color=0x5CD1E5)
            await message.channel.send("Error : Not existing player", embed=embed)
           




           
accross_token = os.environ["BOT_TOKEN"]
app.run(accross_token)
