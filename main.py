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
from discord.ext import commands
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

 
app = discord.Client()

@app.event
async def on_ready():
    print('로그인 중 입니다 ..!')                           #이것은 수정할 필요 없음. 유저들에게 보여지지 않는 곳입니다.
    print(app.user.name)                                   #그냥 사람으로치면 웹사이트에 로그인하는 과정이라고 보시면 됩니다.
    print(app.user.id)
    print('===============')
    game = discord.Game("도리봇에게 !도와줘라고 도움을 요청해보세요!")
    await app.change_presence(status=discord.Status.online, activity=game)
    
@app.event
async def on_member_join(member):
    fmt = '{1.name} 서버에 온 것을 진심으로 환영합니다 {0.mention} 님'    #신규유저한테만 보여지는 메세지 입니다.
    channel = member.server.get_channel("721047251862159416")
    await app.message.channel.send( fmt.format(member, member.server))
    await app.message.channel.send(member, "안녕하세요? 전 도리봇이라고 해요.")
    await app.message.channel.send(member, "무슨 도움이 필요하신가요?")
    await app.message.channel.send(member, "제가 도울 수 있는 범위안에서 도와드릴게요.")
    await app.message.channel.send(member, "마지막으로, 우리 서버에 오신 것을 환영합니다!")
 
@app.event
async def on_member_remove(member):
    channel = member.server.get_channel("721047251862159416")         
    fmt = '{0.mention} 님이 서버를 떠나셨습니다'
    await app.message.channel.send( fmt.format(member, member.server))
          


        
@app.event
async def on_message(message):

    if message.content.startswith("!도와줘"):
        channel = message.channel
        embed = discord.Embed(
            title = '명령어 목록',
            description = '아래는 명령어 목록 입니다. 명령어 목록은 계속 업데이트 중 입니다.',
            colour = discord.Colour.red()
        )

        #embed.set_footer(text = '')
        dtime = datetime.datetime.now()
        #print(dtime[0:4]) # 년도
        #print(dtime[5:7]) #월
        #print(dtime[8:11])#일
        #print(dtime[11:13])#시
        #print(dtime[14:16])#분
        #print(dtime[17:19])#초
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        #embed.set_footer(text=dtime[0:4]+"년 "+dtime[5:7]+"월 "+dtime[8:11]+"일 "+dtime[11:13]+"시 "+dtime[14:16]+"분 "+dtime[17:19]+"초")
        embed.add_field(name = '!안녕', value = '도리봇이 인사를 해줍니다',inline = False)
        embed.add_field(name='!코로나', value='도리봇이 실시간 코로나 현황을 불러옵니다', inline=False)
        embed.add_field(name='!오늘의운세', value=' 도리봇이 오늘의운세를 불러옵니다 ', inline=False)
        embed.add_field(name='!오늘의시한편', value=' 도리봇이 오늘의 시한편을 읊어줍니다 ', inline=False)        
        embed.add_field(name='!PC 게임 추천', value=' 도리봇이 PC 게임을 추천해줍니다 ', inline=False)
        embed.add_field(name='!모바일 게임 추천', value=' 도리봇이 모바일 게임을 추천해줍니다 ', inline=False)
        embed.add_field(name='!주사위굴리기', value=' 도리봇이 주사위를 굴려줍니다 ', inline=False)
        embed.add_field(name='!유튜버 추천', value=' 도리봇이 검증된 유튜버를 추천해줍니다 ', inline=False)
        embed.add_field(name='!MBTI', value=' 도리봇이 MBTI끼리의 궁합을 불러옵니다 ', inline=False)
        embed.add_field(name='!혈액형', value=' 도리봇이 혈액형의 특징,혈액형끼리의 궁합을 불러옵니다 ', inline=False)
        embed.add_field(name='!자살', value=' 도리봇이 자살의 정의들을 불러옵니다. ', inline=False)
        embed.add_field(name='!조선시대 내 이름', value=' 도리봇이 조선시대에 태어났으면 평생 소유하게될 당신의 이름을 알려줍니다 ', inline=False)        
        embed.add_field(name='!도리도리곰도리', value=' 도리봇이 도리도리곰도리의 자기소개를 대신 무료로 해줍니다 ', inline=False)
        embed.add_field(name='!!7호선', value=' 도리봇이 7호선의 자기소개를 대신 무료로 해줍니다 (느낌표 2개) ', inline=False)
        embed.add_field(name='!나냡', value=' 도리봇이 나냡의 자기소개를 대신 무료로 해줍니다 ', inline=False)        
        

        await message.channel.send(channel,embed=embed)

        
    if message.content.startswith("!안녕"):             
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)       
        msg = "{0.author.mention} 안녕하세요?? 오늘 하루도 잘 보내셨나요?".format(message)
        await message.channel.send( msg)
    
      
        
    if message.content.startswith("!오늘의운세"):       #추가바람.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
        await message.channel.send(embed=embed)
        await message.channel.send(embed=discord.Embed(title="당신이 받은 숫자를 [!숫자]와 동일한 형식으로 채팅창에 적어주시길 바랍니다.", color=0xfefefe))
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
            await message.channel.send(embed=discord.Embed(title="일시적인 오류 발생! 잠시만 기다리세요...", color=0xff0000))
            
    if message.content.startswith("!3"):
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
        
    if message.content.startswith("!7"):
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
        
      
    if message.content.startswith("!8"):
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
        
        
    if message.content.startswith("!9"):
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

        
    if message.content.startswith("!10"):
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
        
        
    if message.content.startswith("!1"):
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
        
        
    if message.content.startswith("!2"):
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
        
        
    if message.content.startswith("!4"):
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
        
    if message.content.startswith("!5"):
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
        
        
    if message.content.startswith("!6"):
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
        

        
    if message.content.startswith('!코로나') or message.content.startswith('코로나') or message.content.startswith('3단계') or message.content.startswith('우한폐렴') or message.content.startswith('서울페렴') or message.content.startswith('대구폐렴'):
        # 보건복지부 코로나 바이러스 정보사이트"
        covidSite = "http://ncov.mohw.go.kr/index.jsp"
        covidNotice = "http://ncov.mohw.go.kr"
        html = urlopen(covidSite)
        bs = BeautifulSoup(html, 'html.parser')
        latestupdateTime = bs.find('span', {'class': "livedate"}).text.split(',')[0][1:].split('.')
        statisticalNumbers = bs.findAll('span', {'class': 'num'})
        beforedayNumbers = bs.findAll('span', {'class': 'before'})

        #주요 브리핑 및 뉴스링크
        briefTasks = []
        mainbrief = bs.findAll('a',{'href' : re.compile('\/tcmBoardView\.do\?contSeq=[0-9]*')})
        for brf in mainbrief:
            container = []
            container.append(brf.text)
            container.append(covidNotice + brf['href'])
            briefTasks.append(container)
        print(briefTasks)

        # 통계수치
        statNum = []
        # 전일대비 수치
        beforeNum = []
        for num in range(7):
            statNum.append(statisticalNumbers[num].text)
        for num in range(4):
            beforeNum.append(beforedayNumbers[num].text.split('(')[-1].split(')')[0])

        totalPeopletoInt = statNum[0].split(')')[-1].split(',')
        tpInt = ''.join(totalPeopletoInt)
        lethatRate = round((int(statNum[3]) / int(tpInt)) * 100, 2)
        embed = discord.Embed(title="Covid-19 Virus Korea Status", description="",color=0x5CD1E5)
        embed.add_field(name="Data source : Ministry of Health and Welfare of Korea", value="http://ncov.mohw.go.kr/index.jsp", inline=False)
        embed.add_field(name="Latest data refred time",value="해당 자료는 " + latestupdateTime[0] + "월 " + latestupdateTime[1] + "일 "+latestupdateTime[2] +" 자료입니다.", inline=False)
        embed.add_field(name="확진환자(누적)", value=statNum[0].split(')')[-1]+"("+beforeNum[0]+")",inline=True)
        embed.add_field(name="완치환자(격리해제)", value=statNum[1] + "(" + beforeNum[1] + ")", inline=True)
        embed.add_field(name="치료중(격리 중)", value=statNum[2] + "(" + beforeNum[2] + ")", inline=True)
        embed.add_field(name="사망", value=statNum[3] + "(" + beforeNum[3] + ")", inline=True)
        embed.add_field(name="누적확진률", value=statNum[6], inline=True)
        embed.add_field(name="치사율", value=str(lethatRate) + " %",inline=True)
        embed.add_field(name="- 최신 브리핑 1 : " + briefTasks[0][0],value="Link : " + briefTasks[0][1],inline=False)
        embed.add_field(name="- 최신 브리핑 2 : " + briefTasks[1][0], value="Link : " + briefTasks[1][1], inline=False)
        embed.set_thumbnail(url="https://wikis.krsocsci.org/images/7/79/%EB%8C%80%ED%95%9C%EC%99%95%EA%B5%AD_%ED%83%9C%EA%B7%B9%EA%B8%B0.jpg")
        embed.set_footer(text='#Stay at Home #사회적 거리두기')
        await message.channel.send("Covid-19 Virus Korea Status", embed=embed)        
        
        
    if message.content.startswith("닥쳐"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("시발"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("씨발"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("니애미"):
        await message.channel.send("응 니애미 창녀")

    if message.content.startswith("ㄴㅇㅁ"):
        await message.channel.send("응 느그애미")

    if message.content.startswith("니애비"):
        await message.channel.send("응 니애비 외노자 ")

    if message.content.startswith("ㄴㅇㅂ"):
        await message.channel.send("응 느그애비 ")

    if message.content.startswith("개새끼"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("닭쳐"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개새기"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개샛기"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("문재인"):
        await message.channel.send("욕 하지마라 진짜 뒤진다 ")

    if message.content.startswith("전라도"):
        await message.channel.send("지역 비하하지 마라 ")

    if message.content.startswith("ㅗ"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("ㅅㅂ"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("ㅆㅂ"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("ㄱㅅㄲ"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개자식"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("ㅋㅋㅋ"):
        await message.channel.send("쪼개지마라  ")

    if message.content.startswith("ㅇㅈㄹ"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("이지랄"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("추미애"):
        await message.channel.send(" 진짜 욕하지 마라 ")

    if message.content.startswith("박원순"):
        await message.channel.send("패드립보다 심한 욕을 박네 니네 엄마가 그리 가르쳤냐 ")

    if message.content.startswith("대깨문"):
        await message.channel.send("와.. 이건 좀 심했다... 상처 받음.. ")

    if message.content.startswith("문빠"):
        await message.channel.send("와.. 이건 좀 심했다... 상처 받음.. ")

    if message.content.startswith("씹새끼"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("10새끼"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("십새끼"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("십새기"):
        await message.channel.send("욕하지 마라")

    if message.content.startswith("씹새기"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("10새기"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개독"):
        await message.channel.send("종교 비하 발언 하지 마라 진짜 추방당하기 싫으면 ")

    if message.content.startswith("ㅁㄹ"):
        await message.channel.send("좆까 ")
      
    if message.content.startswith("좆까"):
        await message.channel.send("욕 작작해 시발련아 ")

    if message.content.startswith("ㅈㄲ"):
        await message.channel.send("하시발 추방 마렵다 ")

    if message.content.startswith("좃까"):
        await message.channel.send("진짜 뒤지기 전에 작작해라 ")

    if message.content.startswith("조까"):
        await message.channel.send("욕 작작 하렴^^ ")

    if message.content.startswith("조카"):
        await message.channel.send("욕 하지 마라 ")

    if message.content.startswith("좃카"):
        await message.channel.send("욕 하지 마라 ")
   
    if message.content.startswith("삼성"):
        await message.channel.send("대한민국을 먹여살리는 국내 1위 기업 삼성전자. 삼성전자 제품을 사용하는 대한민국의 청소년들과 대학생들은 미래가 밝습니다. ")

    if message.content.startswith("애플"):
        await message.channel.send("좋은 것만 쓰면서 자라야 할 청소년들을 지옥길로 인도하는 저주 받은 기업, 애플. 대한민국의 청소년들과 대학생들을 위해 애플을 대한민국에서 추방해야만 합니다. 대한민국의 미래가 달린 문제니 청원 부탁드립니다. ")

    if message.content.startswith("아이폰"):
        await message.channel.send("대가리 없는 저능아들이나 환장하는 쓰레기 기업이 만든 쓰레기 폰 ")

    if message.content.startswith("갤럭시"):
        await message.channel.send("이 시대 최고의 엘리트들이 선호하는 대한민국 1위 기업 삼성의 스마트폰  ")

    if message.content.startswith("앱등이"):
        await message.channel.send("중증 장애인들 중에 유독 앱등이가 많다. 그것은 과학이다. ")

    if message.content.startswith("삼엽충"):
        await message.channel.send("이 시대 최고의 엘리트 ")

    if message.content.startswith("애플빠"):
        await message.channel.send("중증 장애인들 중에 유독 애플빠가 많다. 그것은 과학이다. ")

    if message.content.startswith("삼성빠"):
        await message.channel.send("이 시대 최고의 엘리트이자 천재이며 인싸 ")

    if message.content.startswith("개씨발"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개씹"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개좆"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개씨발"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개씹할"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개지랄"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개족새"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("아다"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("동정"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("걸레"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("간나새끼"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개새"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개돼지"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개나리"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개쓰레기"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("고자"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("거지"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("졸라"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("존나"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("좆나"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("좃나"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("ㅈㄴ"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("김치녀"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("꺼저"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("꺼져"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("급식"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("급식충"):
        await message.channel.send("욕하지 마라 ")

    if message.content.startswith("개초딩"):
        await message.channel.send("욕하지 마라 ")   

    if message.content.startswith("게임"):
        await message.channel.send(" 그럴 시간에 공부를 하렴.. ")
        
    if message.content.startswith("중국놈"):
        await message.channel.send(" 넌 조센징이라는걸 항상 명심하렴^^ ")

    if message.content.startswith("중국년"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("중국새끼"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("중국"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("일본"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("일본놈"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("일본년"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("일본새끼"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("짱깨"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("짱깨놈"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("짱깨년"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("짱깨새끼"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("쪽발이"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("쪽바리"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("쪽발이놈"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("쪽바리놈"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("쪽발이년"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("쪽바리새끼"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("쪽발이새끼"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("문재앙"):
        await message.channel.send(" 패드립보다 심한 욕을 하네? 알았으면 삭제해라^^ 추방해버리기전에^^  ")

    if message.content.startswith("디시"):
        await message.channel.send("일베충아 꺼지렴~~^^ ")

    if message.content.startswith("틀딱"):
        await message.channel.send("그런 표현 쓰지마라.. 니네 애미 애비도 틀딱이라 곧 뒤질 나이인데;; 너도 그렇고, 나도 그렇고 모든 인간은 다 틀딱이 되어 죽을 운명이다. ")

    if message.content.startswith("빡쳐서"):
        await message.channel.send("난 니얼굴 봐서 빡침..  ")

    if message.content.startswith("빡침"):
        await message.channel.send("난 니얼굴 봐서 빡침..  ")

    if message.content.startswith("빡치네"):
        await message.channel.send("난 니얼굴 봐서 빡침..  ")

    if message.content.startswith("빡친다"):
        await message.channel.send("난 니얼굴 봐서 빡침..  ")

    if message.content.startswith("빡치넹"):
        await message.channel.send("난 니얼굴 봐서 빡침..  ")

    if message.content.startswith("빡쳐"):
        await message.channel.send("난 니얼굴 봐서 빡침..  ")

    if message.content.startswith("빡치기전에"):
        await message.channel.send("난 니얼굴 봐서 빡침..  ")

    if message.content.startswith("노예"):
        await message.channel.send("욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("노예놈"):
        await message.channel.send("욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("노예년"):
        await message.channel.send("욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("노예새끼"):
        await message.channel.send("욕하지 말자구~~^^ 사이좋게 지내자구~^^  ")

    if message.content.startswith("노예새기"):
        await message.channel.send("욕하지 말자구~~^^ 사이좋게 지내자구~^^  ")

    if message.content.startswith("쪽바리새기"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^  ")

    if message.content.startswith("쪽발이새기"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^ ")

    if message.content.startswith("짱깨새기"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^ ")

    if message.content.startswith("일본새기"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^ ")

    if message.content.startswith("중국새기"):
        await message.channel.send("넌 조센징이라는걸 항상 명심하렴^^ ")

    if message.content.startswith("틀딱새기"):
        await message.channel.send("애미애비도 없는 새끼 ")

    if message.content.startswith("틀딱새끼"):
        await message.channel.send("애미애비도 없는 새끼 ")

    if message.content.startswith("틀딱샛기"):
        await message.channel.send("애미애비도 없는 새끼 ")

    if message.content.startswith("틀니딱딱"):
        await message.channel.send("애미애비도 없는 새끼 ")

    if message.content.startswith("틀니딱딱이"):
        await message.channel.send("애미애비도 없는 새끼 ")

    if message.content.startswith("틀"):
        await message.channel.send("애미애비도 없는 새끼 ")

    if message.content.startswith("나무위키"):
        await message.channel.send("꺼라위키, 대가리에 든거 없는 애미애비 등골 빨아먹는 새끼들이나 좋아한다는 희대의 위키 사이트. ")

    if message.content.startswith("병신"):
        await message.channel.send(" 이시발 추방 존나 마렵네? 적당히 하자~^^ ")

    if message.content.startswith("병신놈"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^  ")

    if message.content.startswith("병신년"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^  ")

    if message.content.startswith("병신새기"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("병신새끼"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("병신샛기"):
        await message.channel.send("욕하지 말자구~~^^ 사이좋게 지내자구~^^")

    if message.content.startswith("ㅂㅅㅅㄲ"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("ㅂㅅ"):
        await message.channel.send("욕하지 말자구~~^^ 사이좋게 지내자구~^^")

    if message.content.startswith("ㅂㅅㄴ"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("ㅄ"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("ㅄㅅㄲ"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("ㅄㄴ"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("시발아"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("퍼큐"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("뻐큐"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("ㅈ같네"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")

    if message.content.startswith("개같네"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")
      
    if message.content.startswith("시1발"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")
     
    if message.content.startswith("씨1발"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")
      
    if message.content.startswith("씨1발년"):
        await message.channel.send(" 욕하지 말자구~~^^ 사이좋게 지내자구~^^ ")  
      
    if message.content.startswith("도리 병신"):
        await message.channel.send("씹/새/끼야 천한 신분 주제에 감히 그분을 욕하느냐?")
       
    if message.content.startswith("도리"):
        await message.channel.send("개/새/끼야 천한 신분 주제에 감히 그분의 존함을 언급했느냐? ")
      
    if message.content.startswith("ㅊㅋㅊㅋ"):
        await message.channel.send(" 이시발 존나 띠껍네? ")
      
    if message.content.startswith("졸려"):
        await message.channel.send(" 라면먹구갈래? ")
      
    if message.content.startswith("졸리다"):
        await message.channel.send(" 라면먹구갈래? ") 
      
    if message.content.startswith("타르코프"):
        await message.channel.send(" 망겜 언급해서 추방 존나 마렵네;; ")
      
    if message.content.startswith("사람"):
        await message.channel.send(" #Stay at Home #사회적 거리두기 ")
      
    if message.content.startswith("인간"):
        await message.channel.send(" #Stay at Home #사회적 거리두기 ")
      
    if message.content.startswith("유튜브"):
        await message.channel.send(" 좋은 것만 보고 자라야 할 대한민국의 꿈나무들을 병들게 하는 악마의 기업, 유튜브. 유튜브 사이트를 국내에서 접속할 수 없게 막아야합니다. 대한민국의 미래가 달린 문제니 청원 부탁드립니다. ")
      
    if message.content.startswith("사회적거리두기"):
        await message.channel.send(" #Stay at Home ")
      
    if message.content.startswith("사회적 거리두기"):
        await message.channel.send(" #Stay at Home ")
      
    if message.content.startswith("안 졸려"):
        await message.channel.send(" 그러다 몸 씹창나면 아무도 책임 안져준다.. 좋은 말로 할때 자라... 젊을 때는 모르겠지만, 늙고나면 땅을 치고 후회할거다. ")

    if message.content.startswith("안졸려"):
        await message.channel.send(" 그러다 몸 씹창나면 아무도 책임 안져준다.. 좋은 말로 할때 자라... 젊을 때는 모르겠지만, 늙고나면 땅을 치고 후회할거다.")

    if message.content.startswith("안졸리다"):
        await message.channel.send(" 그러다 몸 씹창나면 아무도 책임 안져준다.. 좋은 말로 할때 자라... 젊을 때는 모르겠지만, 늙고나면 땅을 치고 후회할거다. ")

    if message.content.startswith("안 졸리다"):
        await message.channel.send(" 그러다 몸 씹창나면 아무도 책임 안져준다.. 좋은 말로 할때 자라... 젊을 때는 모르겠지만, 늙고나면 땅을 치고 후회할거다. ")

    if message.content.startswith("안졸림"):
        await message.channel.send(" 그러다 몸 씹창나면 아무도 책임 안져준다.. 좋은 말로 할때 자라... 젊을 때는 모르겠지만, 늙고나면 땅을 치고 후회할거다. ")

    if message.content.startswith("안 졸림"):
        await message.channel.send(" 그러다 몸 씹창나면 아무도 책임 안져준다.. 좋은 말로 할때 자라... 젊을 때는 모르겠지만, 늙고나면 땅을 치고 후회할거다. ")
      
    if message.content.startswith("왜"):
        await message.channel.send(" ? ")

    if message.content.startswith("!좆까"):
        await message.channel.send(" 욕하지 마라")

    if message.content.startswith("!좃까"):
        await message.channel.send(" 욕하지 마라 ")

    if message.content.startswith("!좇까"):
        await message.channel.send(" 욕하지 마라 ")

    if message.content.startswith("!족까"):
        await message.channel.send(" 욕하지 마라 ")

    if message.content.startswith("!ㅈㄲ"):
        await message.channel.send(" 욕하지 마라 ")

    if message.content.startswith("나냡"):
        await message.channel.send("7호선새키야 이분 이름 언급할거면 신분 상승부터 하라고  ")
      
    if message.content.startswith("밴스드"):
        await message.channel.send(" 순정 유튜브 앱에 여러 강력한 편의 기능을 더한 앱이다. 유튜브 프리미엄과 비슷하게 보이지만 실제로는 유튜브 앱을 뜯어고친 Mod 버전이다. ")

    if message.content.startswith("유튜브 밴스드"):
        await message.channel.send("순정 유튜브 앱에 여러 강력한 편의 기능을 더한 앱이다. 유튜브 프리미엄과 비슷하게 보이지만 실제로는 유튜브 앱을 뜯어고친 Mod 버전이다. ")

    if message.content.startswith("유튜브밴스드"):
        await message.channel.send(" 순정 유튜브 앱에 여러 강력한 편의 기능을 더한 앱이다. 유튜브 프리미엄과 비슷하게 보이지만 실제로는 유튜브 앱을 뜯어고친 Mod 버전이다. ")
      
    if message.content.startswith("!INTP"):
        await message.channel.send(" 당신의 MBTI는 INTP 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 ENFJ와 ENTJ 이며, ")
        await message.channel.send(" 잘맞는 타입은 ENFP, INFJ, INFP, INTJ, ENTP, INTP 이고, ")
        await message.channel.send(" 당신의 MBTI와 안맞는 타입은 ESFJ, ISFJ, ESTJ, ISTJ, ESFP, ISFP, ESTP 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *사소한 관심, 코드 잘 맞춰주는 사람 ")
        await message.channel.send(" *좋아하는 것을 티내주는 사람 ")
        await message.channel.send(" *특별함을 계속 말해주는 사람 ")
        await message.channel.send(" *많은 관심과 질문이 필요함 ")
        await message.channel.send(" *경청해주는 자세가 필요함 ")
        await message.channel.send(" ============ ")
        await message.channel.send(" 상대방이 원하는 대로 하려고 노력하지만 연애를 하면서 에너지 소모가 커서 금방 지치는 성향을 가지고 있으며, ")
        await message.channel.send(" 상대방에게 관심이 식으면 빠르게 손절하는 경향이 있다. 개인주의적 성향이 강한 INTP는 연인에게 의지하기보다는 ")
        await message.channel.send(" 독립적인 성향이 강하며 독신주의자가 은근히 많다. INTP에게 연애나 사랑이 1순위가 아닌 경우가 많다. ")


    if message.content.startswith("!INFP"):
        await message.channel.send(" 당신의 MBTI는 INFP 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 ENFJ와 ENTJ 이며, ")
        await message.channel.send(" 잘맞는 타입은 INFP, ENFP, INFJ, INTJ, INTP, ENTP 이고, ")
        await message.channel.send(" 당신의 MBTI와 최악의 타입은 ISFP, ESFP, ISTP, ESTP, ISFJ, ESFJ, ISTJ, ESTJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *한결같은 사람, 예의바르고 배려하는 사람 ")
        await message.channel.send(" *사생활 존중할 것, 당일 연락 싫어함 ")
        await message.channel.send(" *선경에 모순이 보이지 않을 것 ")
        await message.channel.send(" *똑똑하고 배울 것 많은 사람, 논리적인 사람 ")
        await message.channel.send(" *자기자랑 안통함 ")
        await message.channel.send(" *말 많은 사람 싫어함 ")
        await message.channel.send(" *허세, 감정호소 싫어함 ")
        await message.channel.send(" *차분한 성격을 좋아함 ")

    if message.content.startswith("!ISTJ"):
        await message.channel.send(" 당신의 MBTI는 ISTJ 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 ESFP와 ESTP 이며, ")
        await message.channel.send(" 잘맞는 타입은 ISFJ, ESFJ, ISTJ, ESTJ 이고, ")
        await message.channel.send(" 반반 타입은 ISTP, ISFP, ENTJ 이고, ")
        await message.channel.send(" 당신의 MBTI와 안맞는 타입은 INTJ, INTP, ENTP 입니다. ")
        await message.channel.send(" 당신의 MBTI와 최악의 타입은 INFP, ENFP, INFJ, ENFJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *과묵하고 책임감 있는, 나대지 않는 사람 ")
        await message.channel.send(" *갈등 싫음, 평화주의자인 사람 ")
        await message.channel.send(" *ISTJ를 잘 이해해줄 것 ")
        await message.channel.send(" *신뢰감을 줄 것 ")
        await message.channel.send(" *조용히 챙겨주고, 먼저 도와주는 사람 ")
        await message.channel.send(" *충동적인 모습을 싫어함 ")
        await message.channel.send(" *지나치게 활동적인 것은 부담스러움 ")
        await message.channel.send(" *지적이나 평가 싫어함 ")
        await message.channel.send(" ============ ")
        await message.channel.send(" ISTJ형은 신중하게 상대를 선택하는 경향이 있으며, 적극적으로 접근하는 것에 그다지 자신있어 하지 않습니다. ")
        await message.channel.send(" 배려심이 강하고 책임감도 강하기 때문에 상대를 슬프게 하는 행동은 하지 않으며 참는 경우도 많아 폭발한다면 감당하기 어려울 수 있습니다. ")
        await message.channel.send(" 동료 의식이 높기 때문에 동료에 대해 나쁘게 말하면 관계가 무너지기 쉬운 것도 특징입니다. ")

    if message.content.startswith("!ISFJ"):
        await message.channel.send(" 당신의 MBTI는 ISFJ 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 ESFP와 ESTP 이며, ")
        await message.channel.send(" 잘맞는 타입은 ISFJ, ESFJ, ISTJ, ESTJ 이고, ")
        await message.channel.send(" 반반 타입은 ISFP, ISTP 이고, ")
        await message.channel.send(" 당신의 MBTI와 안맞는 타입은 INTJ, INTP, ENTP 입니다. ")
        await message.channel.send(" 당신의 MBTI와 최악의 타입은 INFP, ENFP, INFJ, ENFJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *성실하고 똑똑한 사람 ")
        await message.channel.send(" *매사 열심히 할 것 ")
        await message.channel.send(" *인권의식 높은 사람 ")
        await message.channel.send(" *내가 해주는 만큼 돌려주는 사람에게 크게 감동 ")
        await message.channel.send(" *10주고 2받아도 감동하는 스타일 ")
        await message.channel.send(" *잘해주는데 나한테만 잘해줘야함 ")
        await message.channel.send(" *칭찬은 크게 필요 없음 ")
        await message.channel.send(" *노력한 결과에 대해서 칭찬 OK ")
        await message.channel.send(" ============ ")
        await message.channel.send(" ISFJ 유형에게 있어서 관계를 맺는 일은 매우 가치 있는 일입니다. 당신을 기쁘게 하는 일을 하는 것을 아주 좋아하며, 보통 그들은 당신이 원하거나 ")
        await message.channel.send(" 필요로 하는 것들을 꽤 정확하게 알아 맞춥니다. 당신은 그들의 이러한 행동들에 의존해지거나 익숙해지기 쉽지만, 이들 스스로 당신을 위해 하는 행동들에  ")
        await message.channel.send(" 매우 신경을 쓰고 있다는 것을 알아야 합니다. 당신이 이들의 배려와 호의에 대해서 고마움과 애정을 자주 표현해주는 것이 중요합니다. ")

    if message.content.startswith("!ENFJ"):
        await message.channel.send(" 당신의 MBTI는 ENFJ 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 INFP와 ISFP 이며, ")
        await message.channel.send(" 잘맞는 타입은 ENFP, INFJ, ENFJ, INTJ, ENTJ, INTP, ENTP 이고, ")
        await message.channel.send(" 당신의 MBTI와 최악의 타입은 ESFP, ISTP, ESTP, ISFJ, ESFJ, ISTJ, ESTJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *고맙게 여길줄아는 사람 ")
        await message.channel.send(" *ENFJ가 주는 것에 감동하기 ")
        await message.channel.send(" *먼저 다가와주기 ")
        await message.channel.send(" *얘기 많이 들어주기")
        await message.channel.send(" *ENFJ의 영향력을 긍정적으로 평가해줄 것 ")
        await message.channel.send(" ============ ")
        await message.channel.send(" ENFJ는 자신에게 공감하는지, 상대방의 감정이 내 감정과 같은지, 우리 관계는 어떤지 등에 대해서 여러번 물어봅니다. 이것은 종종 관계에 ")
        await message.channel.send(" 문제가 있을 때는 좋은 극복 방법이 되기도 합니다. 하지만 너무 많은 질문은 오히려 관계를 방해하는 요소가 될 수 있습니다. 상대방의 감정을 ")
        await message.channel.send(" 살피는 것도 좋지만 끊임없이 사랑을 확인하려는 자세는 그만 두는 것이 좋습니다. ")

    if message.content.startswith("!ENTP"):
        await message.channel.send(" 당신의 MBTI는 ENTP 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 INFJ와 INTJ 이며, ")
        await message.channel.send(" 잘맞는 타입은 INFP, ENFP, ENFJ, ENTJ, INTP, ENTP 이고, ")
        await message.channel.send(" 반반 타입은 ISFP, ESFP, ISTP, ESTP 이고, ")
        await message.channel.send(" 당신의 MBTI와 안맞는 타입은 ISFJ, ESFJ, ISTJ, ESTJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *내 맘에 드는 사람 ")
        await message.channel.send(" *지속적인 플러팅 필요 ")
        await message.channel.send(" *말보다 행동 ")
        await message.channel.send(" *희생적인 태도, 살뜰히 챙겨주기 ")
        await message.channel.send(" *함께있을때 ENTP를 성장시킬 수 있는 사람 ")
        await message.channel.send(" *스스로 성장하고 비전있는 사람 ")
        await message.channel.send(" *공감 잘 해주고 우쭈쭈 잘해 줄것 ")
        await message.channel.send(" *리액션 필수, 관심 계속 가져주기 ")
        await message.channel.send(" *독특하고 자유분방하되 허세는 절대 금물 ")
        await message.channel.send(" *플러팅 난이도 높음 ")
        await message.channel.send(" *밀당 싫음 ")
        await message.channel.send(" *논쟁에서 져주는 사람")
        await message.channel.send(" ============ ")
        await message.channel.send(" ENTP는 재치있고 활기차기 때문에 흥미진진한 연인입니다. 하지만 관계가 안정되멩 따라 지루한 관계를 견디지 못해서 더 많은 즐거움을 만드려는 경향이 있습니다. ")
        await message.channel.send(" 지금 사귀는 상대에게 진지하건 아니건, ENTP는 여러 사람들과의 가능성을 열어두는 것을 좋아합니다. 당신은 연인에게 솔직하고 진지하게 행동하는 게 좋습니다. ")


    if message.content.startswith("!ENTJ"):
        await message.channel.send(" 당신의 MBTI는 ENTJ 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 INFP와 INTP 이며, ")
        await message.channel.send(" 잘맞는 타입은 ENFP, INFJ, ENFJ, INTJ, ENTJ, INTP, ENTP 이고, ")
        await message.channel.send(" 반반 타입은 ISFP, ESFP, ISTP, ESTP, ISFJ, ISTJ, ESTJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *플러팅이 의미가 없음, 먼저 올 때까지 기다릴 것 ")
        await message.channel.send(" *팀플 같이해서 빡세게 일하는 모습 보일 것 ")
        await message.channel.send(" *순수하게 똑똑한 벗 선호 ")
        await message.channel.send(" *가벼운 관계 싫어함 ")
        await message.channel.send(" *불호가 매우 강함 ")
        await message.channel.send(" *기준이 매우 높음 ")
        await message.channel.send(" *인간적으로 존중할 수 있는 모습 보일 것 ")
        await message.channel.send(" *퍼주는 건 좋은데 너무 부담스러운건 자제 ")
        await message.channel.send(" *밀당하지 말것 ")
        await message.channel.send(" *무성애자 많음, 상처 받지 말것 ")
        await message.channel.send(" *ENTJ는 기본적으로 자기애가 강함 ")
        await message.channel.send(" ============ ")
        await message.channel.send(" 연애도 주도적으로 많이하며, 연애 상대에게 꽤 충실한 편 입니다. 이들이 끌리는 스타일은 자신이 못하는 것을 잘하는 상대에게 ")
        await message.channel.send(" 유능함을 느껴 빠지기도 하며, 자신의 말을 잘 들어주는 상대에게 끌리기도 합니다. 이들은 연애에 나름 충실하고 연인을 잘 챙기지만 연인에게도 ")
        await message.channel.send(" 강압적인 태도를 가끔씩 드러내어 갈등의 원인이 되기도 합니다. ")
        await message.channel.send(" 자신의 직감에 확신이 있는 ENTJ는 헤어지고 싶다고 생가갛면 배려없고 단호해질 수 있습니다. 당신의 의사를 전달하는 방식과 시점을 생각하고 관계를 정리하는 것이 좋습니다. ")        

    if message.content.startswith("!ESFP"):
        await message.channel.send(" 당신의 MBTI는 ESFP 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 ISFJ와 ISTJ 이며, ")
        await message.channel.send(" 반반 타입은 INTJ, ENTJ, INTP, ENTP, ESFJ, ESTJ 이고, ")
        await message.channel.send(" 당신의 MBTI와 안맞는 타입은 ISFP, ESFP, ISTP, ESTP 입니다. ")
        await message.channel.send(" 당신의 MBTI와 최악의 타입은 INFP, ENFP, INFJ, ENFJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *연락 자주하고 약속 많이 잡기 ")
        await message.channel.send(" *심심할때마다 연락하기 ")
        await message.channel.send(" *ESFP가 맘에 드는 사람 ")
        await message.channel.send(" *우연한 만남포인트 자주 만들기 ")
        await message.channel.send(" *선물 많이 주기 ")
        await message.channel.send(" ============ ")
        await message.channel.send(" 자주 만나는 것을 좋아하며 감정적으로도 물질적으로도 표현에 적극적입니다. 대상을 지배하려고 하지 않으며, 우연한 만남에 포인트를 만들며 친구 같은 연애를 좋아합니다. ")
        await message.channel.send(" ESFP는 자신이 맘에 드는 사람이 우선이지만 쉽게 상대방에게 질리는 편이며, 연애를 시작하는 자주 연락을 하며 평화로운 관계를 추구합니다. 아주 열정적으로 연애를 하기 때문에 이별 후엔 미련이 없습니다. ")

    if message.content.startswith("!ESFJ"):
        await message.channel.send(" 당신의 MBTI는 ESFJ 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은ISFP와 ISTP 이며, ")
        await message.channel.send(" 잘맞는 타입은 ISFJ, ESFJ, ISTJ, ESTJ 이고, ")
        await message.channel.send(" 반반 타입은 ESFP, ESTP, ENTJ 이고, ")
        await message.channel.send(" 당신의 MBTI와 안맞는 타입은 INTJ, INTP, ENTP 입니다. ")
        await message.channel.send(" 당신의 MBTI와 최악의 타입은 INFP, ENFP, INFJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *'내 사람'이 될 것 ")
        await message.channel.send(" *먼저 다가갈 것 ")
        await message.channel.send(" *적당한 선에서 적당히 다가올 것 ")
        await message.channel.send(" *친한 사이 아니면 플러팅 비추")
        await message.channel.send(" *공통점 많이 만들기, 배려해주기, 취미공유 ")
        await message.channel.send(" *다정다감, 배려, 쏘스윗 ")
        await message.channel.send(" *직접적인 표현 ")
        await message.channel.send(" *다정한 영상 선호 ")
        await message.channel.send(" ============ ")
        await message.channel.send(" 사회성이 대부분 좋고 다정한 편이라 인기가 많다. 주변에 이성도 많아서 본인이 활동하는 영역에서 연인관계를 발전시킨다. 현실적인  ")
        await message.channel.send(" 성향이 강해서인지 마음이 있어도 상대와 내가 현재 조건이 맞지 않는다면 그 관계에 대해 크게 고민한다. 그러나 연애 발전 단계에서는 ")
        await message.channel.send(" 생각보다 그렇게 적극적이지 않다. 상대의 반응에 따라 단계를 발전시키며, 이들은 관계 발전 전까지는 상대와 내가 맞는지를 고민을 많이하지만, 막상 연애가 시작되면 장기 연애하는 경우가 많다.")

    if message.content.startswith("!ESTP"):
        await message.channel.send(" 당신의 MBTI는 ESTP 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 ISFJ와 ISTJ 이며, ")
        await message.channel.send(" 반반 타입은 INTJ, ENTJ, INTP, ENTP 이고, ")
        await message.channel.send(" 당신의 MBTI와 안맞는 타입은 ISFP, ESFP, ISTP, ESTP 입니다. ")
        await message.channel.send(" 당신의 MBTI와 최악의 타입은 INFP, ENFP, INFJ, ENFJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *관심 지나치게 절대 X ")
        await message.channel.send(" *개인영역 침범 금지 ")
        await message.channel.send(" *ESTP를 알려고 하지 말고 그에 대해 느끼는 감정표현을 해줄 것 ")
        await message.channel.send(" *잘난척 금지 ")
        await message.channel.send(" *나를 좋아해주는 사람 ")
        await message.channel.send(" *나만 아는 무언가를 가진 사람 ")
        await message.channel.send(" *즉흥적인 것 좋아함 ")
        await message.channel.send(" *변덕에 맞추어 융통성있게 대응해줄 수 있는 사람 ")
        await message.channel.send(" *토론 좋아하고 취미 공유 가능한 사람 ")
        await message.channel.send(" ============ ")
        await message.channel.send(" 적극적이고 활발해서 인기가 많은 ESTP는 스스로가 원하는 상대를 고를 수 잇습니다. ESTP는 사교적이고 재미있지만 상대와의 진지한 관계에 대해 생각하지 않으며, 관계가 지루해지면 떠나는 편 입니다. ")
        await message.channel.send(" 장기 연애는 낯선 것일지도 모르지만, 관계에서 가장 좋은 시기는 초반의 설레임이 지나간 이후라는 사실을 기억해야 합니다. 어느 순간부터 상대의 소중함을 돌아보는 것이 중요합니다.  ")

    if message.content.startswith("!ISFP"):
        await message.channel.send(" 당신의 MBTI는 ISFP 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 ENFJ와 ESFJ, ESTJ 이며, ")
        await message.channel.send(" 반반 타입은 INTJ, ENTJ, INTP, ENTP, ISFJ, ISTJ 이고, ")
        await message.channel.send(" 당신의 MBTI와 안맞는 타입은 ISFP, ESFP, ISTP, ESTP 입니다. ")
        await message.channel.send(" 당신의 MBTI와 최악의 타입은 INFP, ENFP, INFJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *개인 영역 침범 금지 ")
        await message.channel.send(" *플러팅 부담 ")
        await message.channel.send(" *첫인상 중요 ")
        await message.channel.send(" *연애 자체가 그닥 관심 없음 ")
        await message.channel.send(" *좋아하는 사람 생기면 혼자 안절부절함. ")
        await message.channel.send(" *사소한것에 크게 신경씀 ")
        await message.channel.send(" ============ ")
        await message.channel.send(" 수수께끼 투성에 흥미로운 ISFP는 진지한 관계에 오픈 마인드입니다. 하지만 관계가 깊어질수록 두려움이 앞서기 때문에 속마음을 숨기고 도망 갈 수도 있습니다. ")
        await message.channel.send(" 상대에게 당신의 감정에 대해 솔직하게 말하는 것이 좋습니다.")

    if message.content.startswith("!INTJ"):
        await message.channel.send(" 당신의 MBTI는 INTJ 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 ENFP와 ENTP 이며, ")
        await message.channel.send(" 잘맞는 타입은 INFP, INFJ, ENFJ, INTJ, ENTJ, INTP 이고, ")
        await message.channel.send(" 반반 타입은 ISFP, ESFP, ISTP, ESTP 이고, ")
        await message.channel.send(" 당신의 MBTI와 안맞는 타입은 ISFJ, ESFJ, ISTJ, ESTJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *금사빠 ")
        await message.channel.send(" *한결같은 사람, 예의바르고 배려하는 사람 ")
        await message.channel.send(" *사생활 존중할 것, 당일 연락 싫어함 ")
        await message.channel.send(" *선경에 모순이 보이지 않을 것 ")
        await message.channel.send(" *똑똑하고 배울 것이 많은 사람 논리적인 사람 ")
        await message.channel.send(" *대신 가르치려드는건 좋지 않다 ")
        await message.channel.send(" *자기자랑 안통함")
        await message.channel.send(" *말 많은 사람 싫어함 ")
        await message.channel.send(" *허세 싫어함 ")
        await message.channel.send(" *감정호소 싫어함 ")
        await message.channel.send(" *차분한 사람 좋아함 ")
        await message.channel.send(" ============ ")
        await message.channel.send(" INTJ는 사랑때문에 시간낭비를 하지 않습니다. 관계에 있어 서로를 알아보는 등의 과정은 없고, 갑자기 너무 깊은 대화로 넘어가 버립니다.  ")
        await message.channel.send(" 이런 태도에 상대방은 겁을 먹거나 피하고 싶어집니다. 소소한 잡담은 당신 스타일이 아니기는 하지만 진지한 관계로 넘어가기 앞서 가볍게 서로를 알아가는 단계를 거치는 것이 좋습니다.  ")

    if message.content.startswith("!ISTP"):
        await message.channel.send(" 당신의 MBTI는 ISTP 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 ESFP와 ESTP 이며, ")
        await message.channel.send(" 잘맞는 타입은 ISFJ, ESFJ, ISTJ, ESTJ 이고, ")
        await message.channel.send(" 반반 타입은 ISTP, ISFP, ENTJ 이고, ")
        await message.channel.send(" 당신의 MBTI와 안맞는 타입은 INTJ, INTP, ENTP 입니다. ")
        await message.channel.send(" 당신의 MBTI와 최악의 타입은 INFP, ENFP, INFJ, ENFJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *일상 방해 금지 ")
        await message.channel.send(" *내버려두기 ")
        await message.channel.send(" *연락 계속하기 힘들어함 ")
        await message.channel.send(" *전화보단 카톡 ")
        await message.channel.send(" *'내'가 좋아하는 사람 ")
        await message.channel.send(" *의사소통 및 감정표현이 '정확;할 것 ")
        await message.channel.send(" *질투유발, 헷갈리게 하는 행동 절대 금지 ")
        await message.channel.send(" ============ ")
        await message.channel.send(" ISTP의 열정과 독립심은 관계에서 좋은 역할을 합니다. 하지만 썸타는 시간을 늘리면서 여러가지 옵션을 열어두고 싶어합니다. 다른 사람들 자신의 인생에 포함시키기를 원하지 않기 때문입니다.  ")
        await message.channel.send(" 서로를 알아가는데 지나치게 오랜시간이 걸릴 필요는 없습니다. 사랑하는 사람과의 관계가 진심이라고 느껴질 때, 비밀스러운 당신의 곁은 내어주는 것도 필요합니다. ")

    if message.content.startswith("!ESTJ"):
        await message.channel.send(" 당신의 MBTI는 ESTJ 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 ENTJ와ISFP, ISTP 이며, ")
        await message.channel.send(" 잘맞는 타입은 ISFJ, ESFJ, ISTJ, ESTJ 이고, ")
        await message.channel.send(" 반반 타입은 ENTJ, ESFP, ESTP 이고, ")
        await message.channel.send(" 당신의 MBTI와 안맞는 타입은 INTJ, ENTP 입니다. ")
        await message.channel.send(" 당신의 MBTI와 최악의 타입은 INFP, ENFP, INFJ, ENFJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *둥기둥기 니가 최고 ")
        await message.channel.send(" *일단 ESTJ가 표현하는 만큼 표현해줄 것 ")
        await message.channel.send(" *유머로 승부하지 말것, 진증한 사람 ")
        await message.channel.send(" *깊은 얘기 통하는 사람")
        await message.channel.send(" *물질적으로 챙겨주고 기념일 까먹으면 안됨 ")
        await message.channel.send(" *한말을 꼭 지킬 것, 즉흥 싫음 ")
        await message.channel.send(" *티나게 챙겨주고 티나게 표현하기")
        await message.channel.send(" ============ ")
        await message.channel.send(" 직설적이고 자기 주장이 강한 ESTJ는 초반에 너무 좋은 감정과 미묘한 관계를 유지하는 것을 힘들어 합니다. 강렬한 감정을 잠시 그대로 두십시오.")
        await message.channel.send(" 우리가 어떤 사인인지 묻기 전에 두 사람의 감정이 자연스럽게 발전할 시간을 주는 것이 좋습니다.")

    if message.content.startswith("!INFJ"):
        await message.channel.send(" 당신의 MBTI는 INFJ 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 ENFP와 ENTP 이며, ")
        await message.channel.send(" 잘맞는 타입은 INFP, INFJ, ISTJ, ENFJ, INTJ, ENTJ, INTP 이고, ")
        await message.channel.send(" 당신의 MBTI와 최악의 타입은 ISFP, ESFP, ISTP, ESTP, ISFJ, ISTJ, ESTJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *호의에는 호의로 ")
        await message.channel.send(" *믿을 수 있는 사람 ")
        await message.channel.send(" *서서히 스며들기 ")
        await message.channel.send(" *도덕적인 사람 ")
        await message.channel.send(" *적극적으로 다가오는 사람 ")
        await message.channel.send(" *표현 잘해주고 다정하고 배려심 있는 사람 ")
        await message.channel.send(" *혼자만의 시간을 주는 사람 ")
        await message.channel.send(" *귀여워 해줄 사람 ")
        await message.channel.send(" ============ ")
        await message.channel.send(" 가볍게 데이트하는게 불가능한 타입이며, 정말 믿을만한 사람을 기다릴 수 있는 사람입니다. INFJ는 대립을 싫어하고 조화를 우선시하기 ")
        await message.channel.send(" 때문에 이별하는게 맞는 상황임에도 불구하고 결단을 내리지 못합니다. 당신과 상대방의 시간과 에너지를 낭비하지 말고 필요할 때에는 ")
        await message.channel.send(" 과감한 선택을 할 필요가 있습니다. ")
        
    if message.content.startswith("!ENFP"):
        await message.channel.send(" 당신의 MBTI는 ENFP 입니다. ") 
        await message.channel.send(" 당신의 MBTI와 가장 잘맞는 궁합은 INFJ와 INTJ 이며, ")
        await message.channel.send(" 잘맞는 타입은 INFP, ENFP, ENFJ, ENTJ, INTP, ENTP 이고, ")
        await message.channel.send(" 당신의 MBTI와 최악의 타입은 ISFP, ESFP, ISTP, ESTP, ISFJ, ESFJ, ISTJ, ESTJ 입니다. ")
        await message.channel.send(" ============ ")
        await message.channel.send(" *'내가' 좋아하는 사람 ")
        await message.channel.send(" *알고보니 좋아하는 사람도 ENFP ")
        await message.channel.send(" *세심한 기억력, 카리스마, 수줍은 인간미 ")
        await message.channel.send(" *대화자주, 다양한 화제 ")
        await message.channel.send(" *솔직하게 대답하는 사람 ")
        await message.channel.send(" *혼자만의 시간을 줄 것 ")
        await message.channel.send(" *가만있어도 편안한 사람 ")
        await message.channel.send(" *한 분야의 전문가")
        await message.channel.send(" *성실한 사람")
        await message.channel.send(" *ENFP 좋아해줄것")
        await message.channel.send(" *선 넘지 않고 많은 것을 바라지 않기")
        await message.channel.send(" *애정표현 적으면 불안해함. 지속적인 애정표현 필요")
        await message.channel.send(" *지지부진 싫음, 신뢰를 줄것")
        await message.channel.send(" ============ ")
        await message.channel.send(" ENFP는 관계를 진지하게 받아들이고, 연인을 행복하게 하기 위해 최선을 다하지만, 이러한 노력에 대해 화답할 필요가 있습니다. ")
        await message.channel.send(" 이들은 함께하기에 즐거운 사람이고, 애정 관계에 있어서 수줍어 하지 않습니다. 이 덕분에 관계를 쉽게 시작하는 편이기도 합니다.")
        await message.channel.send(" 또한 가능한 건강한 관계를 만들기 위해 헌신하며, 열정을 다하지만 관계에 있어서 스스로를 위한 여유를 필요로 하기도 합니다. ")
        await message.channel.send(" 이들은 자신의 연인들이 느끼는 감정을 잘 알아차리는 능력을 가지고 있기 때문에 자신의 연인이 원하는 것을 쉽게 파악하며, 만족시켜줍니다. ")
        await message.channel.send(" ENFP의 정신적, 감정적, 물리적 욕구를 잘파악하고 잘 지원해주는 것이 중요합니다. ")

    if message.content.startswith("!A"):
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

    if message.content.startswith("!B"):
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

    if message.content.startswith("!O"):
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

    if message.content.startswith("!AB"):
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
      

    if message.content.startswith("샹년"):
        await message.channel.send("욕하지 말자 부모님 안 계시니? ")    
      
    if message.content.startswith("썅년"):
        await message.channel.send("욕하지 말자 부모님 안 계시니? ") 
      
    if message.content.startswith("샹놈"):
        await message.channel.send("욕하지 말자 부모님 안 계시니? ")   
       
    if message.content.startswith("썅놈"):
        await message.channel.send("욕하지 말자 부모님 안 계시니? ") 
       
    if message.content.startswith("상년"):
        await message.channel.send("욕하지 말자 부모님 안 계시니? ")   
      
    if message.content.startswith("상놈"):
        await message.channel.send("욕하지 말자 부모님 안 계시니? ")

    if message.content.startswith("자살하고싶어"):
        await message.channel.send("우리, 맘 잡고 다시 해 보아요. 행운은 잠시 쉬고 있을 뿐입니다 ")

    if message.content.startswith("자살하고싶다"):
        await message.channel.send("힘들 땐 가만히 눈을 감고 스스로에게 말을 걸어주세요. 나는 어떤 사람인지 얼마나 소중한 사람인지 ")

    if message.content.startswith("자살할래"):
        await message.channel.send("젊었을 때 고민 같은 거, 암 것도 아니여, 나이들어봐 ")

    if message.content.startswith("자살하고프다"):
        await message.channel.send("음... 힘든 일들 모두 그냥, 지나가는 바람이라 생각해 보면 어떨까? ")

    if message.content.startswith("자살마렵다"):
        await message.channel.send("풋 하고 웃지 말고 하하하하하하하")

    if message.content.startswith("자살마려워"):
        await message.channel.send("3년 전에 고민한 거 기억나세요? 기억 안 나죠? 이번에도 그럴 거예요. ")

    if message.content.startswith("죽여주"):
        await message.channel.send("마음을 열어 보세요. 혼자가 아닙니다, 당신은. ")

    if message.content.startswith("죽을"):
        await message.channel.send("많이 힘들었지? ")

    if message.content.startswith("죽고"):
        await message.channel.send("뒷감당 잘해요? ")
       
    if message.content.startswith("롤"):
        await message.channel.send("LOL이 왜 애미뒤진 게임인줄 아냐? 대답을 듣고 싶으면 '!롤'을 채팅창에 입력해라 ")

    if message.content.startswith("!롤"):
        await message.channel.send("간단함. 애미뒤진애들만 모아서 하니까 애미뒤진게임인거야")
        await message.channel.send("LOL은애미뒤진 희대의 좆병신 팀운게임이맞음.")
        await message.channel.send("이걸 부정하는 새끼들도 애미뒤진게맞고 저능아새끼들임.")
        await message.channel.send("지금부터 왜 LOL이 애미뒤진 좆병신 팀운게임이라는건지 설명한다.")
        await message.channel.send("============")
        await message.channel.send("1.일단 게임장르부터 5대5 기반 게임이다.")
        await message.channel.send("따라서 팀중에서 한놈이 저능아에 1인분도 못하는 병신새끼면")
        await message.channel.send("그 팀중에서 다른애가 그 싸는새끼 몫까지 해야 커버가 가능하다.")
        await message.channel.send("2.여왕벌과 대리충")
        await message.channel.send("노력조차 안 하고 그저 티어만 올리려는 애미뒤진 생각을 가진")
        await message.channel.send("저능아새끼들이 LOL에는 유독 많아서")
        await message.channel.send("이런새끼 실력도없이 고티어로가서 팀에게 민폐주고")
        await message.channel.send("이런 현상이 많다는곳도 문제가 심각하다.")
        await message.channel.send("3.챔피언 상성과 벨런스의 문제")
        await message.channel.send("LOL은 애미뒤진 패치를 많이하고 벨런스가 좆망한 GAME이다.")
        await message.channel.send("GAME 승패따윈 안중에도없고 그저")
        await message.channel.send("지 하고싶은챔하고 트롤하는새끼들이 있는 팀이 불리하단 소리다.")
        await message.channel.send("고티어로 갈수록 그런새끼들이 많이 줄어드는 건 맞지만")
        await message.channel.send("그래도 아에 안 걸릴거라 장담할수는없다.")
        await message.channel.send("그저 같은편에 장애인이 안 걸리길 비는게 최선이지.")
        await message.channel.send("============")
        await message.channel.send("결론, LOL 한판이라도 한사람은 다 애미뒤진놈들임.")
        await message.channel.send("대한민국 피시방 순위 1위를 이딴 애미뒤진 GAME이 먹은것부터가")
        await message.channel.send("조센징들은 애미애비 둘다 쌍으로 뒤진 개시발 민족이라는 증거임.") 
        
    if message.content.startswith("ㅋㅋㅋ"):     #없어도 되는 기능.

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
        
        
    if message.content.startswith("도리야"):     #없어도 되는 기능.

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


    if message.content.startswith("!코로나"):     #없어도 되는 기능.

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


    if message.content.startswith("!도와줘"):     #없어도 되는 기능.

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
        
        
    if message.content.startswith("도리도리곰도리"):     #없어도 되는 기능.

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

    if message.content.startswith("!MBTI"):     #없어도 되는 기능.

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

    if message.content.startswith("!혈액형"):     #없어도 되는 기능.

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

        
        
        
    if message.content.startswith("!PC 게임 추천"):      #다소 편협함. 추가바람.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
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

          
          
    if message.content.startswith("!모바일 게임 추천"):       #추가바람
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
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
          
          
    if message.content.startswith("!주사위굴리기"):         #이것도 없어도 지장없는 기능. 
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
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
          
          
    if message.content.startswith("!유튜버 추천"):             #다소 편협함. 추가바람.
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초", color=0xff0000)
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
          
    if message.content.startswith("!자살이란"):       #추가바람.
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
          
        
    if message.content.startswith("!오늘의시한편"):
        randomNum = random.randrange(1, 15)
        if randomNum==1:
            await message.channel.send("방문객")
            await message.channel.send("정현종 시인")
            await message.channel.send("============")
            await message.channel.send("사람이 온다는 건")
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
            await message.channel.send("사람이")
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
            await message.channel.send("엄마야 누나야 강변 살자  ")
            await message.channel.send("뜰에는 반짝이는 금모래 빛 ")
            await message.channel.send("뒷문 밖에는 갈잎의 노래")
            await message.channel.send("엄마야 누나야 강변 살자")
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
            await message.channel.send("죽는 날까지 하늘을 우러러  ")
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
            
            
                  
    if message.content.startswith("!MBTI") or message.content.startswith('MBTI') or message.content.startswith('엠비티아이') or message.content.startswith('성격') or message.content.startswith('!mbti') or message.content.startswith('mbti'):
        await message.channel.send("당신의 MBTI 를 채팅창에 입력해주세요.(무조건, 대문자로만 입력해주세요, 대문자만 인식합니다.) ")
        await message.channel.send("예시) !ENFP (느낌표 + ENFP) ")

    if message.content.startswith("!혈액형") or message.content.startswith('혈관고') or message.content.startswith('혈액유형') or message.content.startswith('혈엑형'):
        await message.channel.send("당신의 혈액형을 채팅창에 입력해주세요.(무조건, 대문자로만 입력해주세요, 대문자만 인식합니다.) ")
        await message.channel.send("예시) !O (느낌표 + O) ")


    if message.content.startswith("!도리도리곰도리"):        #이 부분은 이 소스를 수정해서 새로운 자작봇을 만드실 분들에 해당하시는 분들만 수정 부탁드립니다.
        embed = discord.Embed(title=" 도리도리곰도리는 2000년 봄과 여름의 사이인 달에 태어났으며  ")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 남자같아 보이지만 사실 여자다.  ")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 원래는 인터넷 상에서 남자인척 하고 다녔지만, ")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 이제는 오히려 여자라고 말하면 넷카마라고 불리워지는 상황이 되어버렸다. ")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" MBTI는 ENFP 이고, 혈액형은 O 이다.")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 배틀그라운드 모바일을 즐겨하고, 오버워치는 초창기때 질리도록 하고나서 경쟁전의 비매너 유저들때문에 오버워치를 손절했다. ")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 타르코프는 7호선새키때문에 7만원에 정가로 사서 대가리가 단단히 깨져서 환불도 안하고 방치중이며, 배틀그라운드는 핵쟁이들때문에 사실상 방치중이다. ")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 사실 배틀그라운드 모바일도 솔로 모드와 듀오 에서 핵쟁이들에게 대가리가 단단히 깨져서 그런지 복귀할 엄두도 못내고 있다.  ")
        await message.channel.send(embed=embed)
        msg = "이상 마치도록 하겠다.{0.author.mention} ".format(message)
        await message.channel.send( msg)
        
    if message.content.startswith("!!7호선"):        #이 부분은 이 소스를 수정해서 새로운 자작봇을 만드실 분들에 해당하시는 분들만 수정 부탁드립니다.
        embed = discord.Embed(title=" 대한민국의 고딩이고,  ")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 타르코프와 오버워치를 즐겨하며,   ")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 오버워치에서는 라인 원챔이다.   ")
        await message.channel.send(embed=embed)     
        embed = discord.Embed(title=" 심해에서 탱커를 해주는 것은 사실 굉장히 고마운 행위이나, 팀을 생각할 줄 모르는 플레이를 남발한다.  ")
        await message.channel.send(embed=embed)     
        embed = discord.Embed(title=" 남발하는 수준이 아니다. 매판 솔플 하면서 팀원이 그거에 대해 반응을 보이면 먹잇감을 물은 하이에나처럼 정치질을 시전하기 시작한다.  ")
        await message.channel.send(embed=embed)  
        embed = discord.Embed(title=" 매판 이렇게 플레이 하지만, 욕설로 정지를 먹은적이 없다. (오버워치 좆망겜 클라스가 여기서 보일거라곤 상상도 못했다.) ")
        await message.channel.send(embed=embed)        
        msg = "이상 마치도록 하겠다.{0.author.mention} ".format(message)
        await message.channel.send( msg)
        
    if message.content.startswith("!나냡"):        #이 부분은 이 소스를 수정해서 새로운 자작봇을 만드실 분들에 해당하시는 분들만 수정 부탁드립니다.
        embed = discord.Embed(title=" 대한민국의 직장인이고,  ")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 오버워치와 배틀그라운드 모바일을 즐겨하며,  ")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 오버워치를 순수하게 즐기는 빠대만 돌리는 유저이다.  ")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 메르시 원챔이면서도 메르시보다 모이라를 재밌어한다. ")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 무엇보다 힐러 역할을 즐겨하면서 정치질을 대놓고는 안한다.  ")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 아마도, 오버워치 경쟁전을 한번도 제대로 해본적이 없어서, 오버워치를 진짜 순수하게 즐기는 마인드다 보니 팀탓, 남탓을 안하는 것 같다. (사실, 빠대 유저들이 부럽다. 나도 2016년으로 돌아가고 싶다. 다시 돌아간다면 경쟁전은 절대 안돌릴 것)   ")
        await message.channel.send(embed=embed)
        msg = "이상 마치도록 하겠다.{0.author.mention} ".format(message)
        await message.channel.send( msg)        
       
    if message.content == "!조선시대 내 이름":
        channel = message.channel
        urllib.request.urlretrieve("https://i.imgur.com/KoougXb.jpeg", "explain.png")
        image = discord.File("explain.png", filename="image.png")
        embed = discord.Embed(title="조선시대 내 이름", description=".", color=0x00ff56)
        embed.set_thumbnail(url="https://i.imgur.com/P6HdGr1.png")
        embed.add_field(name=".", value=". ", inline=True)
        await channel.send(embed=embed, file=image)

            
accross_token = os.environ["BOT_TOKEN"]
app.run(accross_token)
