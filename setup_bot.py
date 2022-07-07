import discord
from discord.ext import commands
import json 
import os
import requests
from youtube_search import YoutubeSearch
import random
import pickle
import os
import random
import asyncio
import wikipedia
import datetime
import time
from bs4 import BeautifulSoup
prefix = '/'
bot = commands.Bot(command_prefix=f'{prefix}')
bot.remove_command("help")
data_filename = "data.pickle"
@bot.group(invoke_without_command=True)
async def help(ctx, arg = None):
    if arg == None:
        em = discord.Embed(title = "ℹ️help", description = "sử dụng /help để biết các lệnh có thể sử dụng trên bot và /help <command> để biết cách sử dụng")
        em.add_field(name = "**✅other command**", value = "xsmb, covid19, weather, youtube_search, translate, truyentranh, wiki, news")
        em.add_field(name = "**🎮game command**", value = "dovui, play_taixiu, keobuabao, vuatiengviet, dhbc(đuổi hình bắt chữ), noitu, slot")
        em.add_field(name = "**🏵️roleplay command**", value = "balance, bank, work, daily, ")
        em.add_field(name = "**⚙️system command bot**", value = "help, offbot, ping, callad, sendnoti")
        em.add_field(name = "**🔫fun command**", value = "thinh, mark, tiki, taoanhdep, shopmaihuong, caunoihay, thayboi")
        await ctx.send(embed = em)
    elif arg == 'balance':
        em = discord.Embed(title = "balance", description = "xem số tiền hiện đang có của bạn")
        em.add_field(name = "**cách dùng**", value = f"{prefix}balance @mention")
        await ctx.send(embed = em)
    elif arg == 'bank':
        em = discord.Embed(title = "bank", description = "ngân hàng hỗ trợ rút và gửi tiền của bạn")
        em.add_field(name = "**cách dùng**", value = f"{prefix}bank withdraw <amount>\n{prefix}bank deposit <amount>\n{prefix}bank send <amount> @mention")
        await ctx.send(embed = em)
    elif arg == 'callad':
        em = discord.Embed(title = "callad", description = "báo cáo vấn đề hoặc câu hỏi bạn muốn gửi đến admin")
        em.add_field(name = "**cách dùng**", value = f"{prefix}callad <vấn đề cần báo cáo>")
        await ctx.send(embed = em)
    elif arg == 'caunoihay':
        em = discord.Embed(title = "caunoihay", description = "random một câu nói của các vĩ nhân:))")
        em.add_field(name = "**cách dùng**", value = f"{prefix}caunoihay")
        await ctx.send(embed = em)
    elif arg == 'covid19':
        em = discord.Embed(title = "covid19", description = "xem thông tin về dịch bệnh covid 19 tại Việt Nam")
        em.add_field(name = "**cách dùng**", value = f"{prefix}covid19")
        await ctx.send(embed = em)
    elif arg == 'daily':
        em = discord.Embed(title = "daily", description = "nhận thưởng online mỗi 24H")
        em.add_field(name = "**cách dùng**", value = f"{prefix}D>")
        await ctx.send(embed = em)
    elif arg == 'dhbc':
        em = discord.Embed(title = "dhbc", description = "game đuổi hình bắt chữ:))")
        em.add_field(name = "**cách dùng**", value = f"{prefix}dhbc")
        await ctx.send(embed = em)
    elif arg == 'keobuabao':
        em = discord.Embed(title = "keobuabao", description = "game kéo búa bao với bot")
        em.add_field(name = "**cách dùng**", value = f"{prefix}keobuabao <kéo/búa/bao> <số tiền cược>")
        await ctx.send(embed = em)
    elif arg == 'mark':
        em = discord.Embed(title = "mark", description = "ghép ảnh xàm")
        em.add_field(name = "**cách dùng**", value = f"{prefix}mark")
        await ctx.send(embed = em)
    elif arg == 'news':
        em = discord.Embed(title = "news", description = "xem tin mới mỗi ngày trên vnexpress")
        em.add_field(name = "**cách dùng**", value = f"{prefix}news")
        await ctx.send(embed = em)
    elif arg == 'noitu':
        em = discord.Embed(title = "noitu", description = "game nối từ cùng bot")
        em.add_field(name = "**cách dùng**", value = f"{prefix}noitu")
        await ctx.send(embed = em)
    elif arg == 'ping':
        em = discord.Embed(title = "ping", description = "pong!")
        em.add_field(name = "**cách dùng**", value = f"{prefix}ping")
        await ctx.send(embed = em)
    elif arg == 'play_taixiu':
        em = discord.Embed(title = "play_taixiu", description = "chơi game tài xỉu trên bot:)")
        em.add_field(name = "**cách dùng**", value = f"{prefix}play_taixiu <tài/xỉu> <số tiền cược>")
        await ctx.send(embed = em)
    elif arg == 'shopmaihuong':
        em = discord.Embed(title = "shopmaihuong", description = "ghép ảnh xàm")
        em.add_field(name = "**cách dùng**", value = f"{prefix}shopmaihuong")
        await ctx.send(embed = em)
    elif arg == 'slot':
        em = discord.Embed(title = "slot", description = "game")
        em.add_field(name = "**cách dùng**", value = f"{prefix}slot <số tiền cược>")
        await ctx.send(embed = em)
    elif arg == 'taoanhdep':
        em = discord.Embed(title = "taoanhdep", description = "ghép ảnh xàm")
        em.add_field(name = "**cách dùng**", value = f"{prefix}taoanhdep")
        await ctx.send(embed = em)
    elif arg == 'thayboi':
        em = discord.Embed(title = "thayboi", description = "xem bói online:))")
        em.add_field(name = "**cách dùng**", value = f"{prefix}thayboi")
        await ctx.send(embed = em)
    elif arg == 'thinh':
        em = discord.Embed(title = "thinh", description = "thính")
        em.add_field(name = "**cách dùng**", value = f"{prefix}thinh")
        await ctx.send(embed = em)
    elif arg == 'tiki':
        em = discord.Embed(title = "tiki", description = "ghép ảnh xàm")
        em.add_field(name = "**cách dùng**", value = f"{prefix}tiki")
        await ctx.send(embed = em)
    elif arg == 'translate':
        em = discord.Embed(title = "translate", description = "google dịch")
        em.add_field(name = "**cách dùng**", value = f"{prefix}translate")
        await ctx.send(embed = em)
    elif arg == 'truyentranh':
        em = discord.Embed(title = "truyentranh", description = "xem truyện tranh và tìm những truyện mới nhất trên toptruyen.net và truyentranh24.com")
        em.add_field(name = "**cách dùng**", value = f"{prefix}truyentranh search <keywword> (tìm truyện)\n{prefix}truyentranh news (xem các truyện mới nhất trên toptruyen.net)")
        await ctx.send(embed = em)
    elif arg == 'vuatiengviet':
        em = discord.Embed(title = "vuatiengviet", description = "chơi vua tiếng việt:0")
        em.add_field(name = "**cách dùng**", value = f"{prefix}vuatiengviet")
        await ctx.send(embed = em)
    elif arg == 'weather ':
        em = discord.Embed(title = "weather", description = "ghép ảnh xàm")
        em.add_field(name = "**cách dùng**", value = f"{prefix}weather <location>")
        await ctx.send(embed = em)
    elif arg == 'wiki':
        em = discord.Embed(title = "wiki", description = "tìm kiếm thông tin trên wikipedia")
        em.add_field(name = "**cách dùng**", value = f"{prefix}wiki <keywword>")
        await ctx.send(embed = em)
    elif arg == 'work':
        em = discord.Embed(title = "work", description = "có làm thì mới có ăn")
        em.add_field(name = "**cách dùng**", value = f"{prefix}work")
        await ctx.send(embed = em)
    elif arg == 'xsmb':
        em = discord.Embed(title = "xsmb", description = "xem kết quả xổ số miền Bắc")
        em.add_field(name = "**cách dùng**", value = f"{prefix}xsmb")
        await ctx.send(embed = em)
    elif arg == 'youtube_search':
        em = discord.Embed(title = "youtube_search", description = "tìm video youtube")
        em.add_field(name = "**cách dùng**", value = f"{prefix}youtube_search <keyword>")
        await ctx.send(embed = em)
    elif arg == 'dovui':
        em = discord.Embed(title = "dovui", description = "game đố vui, không vui thì thôi")
        em.add_field(name = "**cách dùng**", value = f"{prefix}dovui")
        await ctx.send(embed = em)
    else:
        await ctx.send(f'lệnh bạn nhập không tồn tại hoặc do thằng admin lỏl lười làm nên để thế=)). có thể sử dụng {prefix}callad để gọi nó dậy')
    
#run bot
#client
@bot.event
async def on_ready():
    print(f'[CLIENT] client completed')
#covid19
@bot.command()
async def covid19(ctx):
    full_url = 'https://api.phamvandien.xyz/covid?country=viet%20nam'
    get = requests.get(full_url)
    data = get.text
    parse_json = json.loads(data)
    data1 = parse_json['data']['danso']
    data2 = parse_json['data']['dangdieutri']
    data3 = parse_json['data']['ca_nhiem_moi']
    data4 = parse_json['data']['hoiphuc']
    data5 = parse_json['data']['total']
    data6 = parse_json['data']['tong_ca_tu_vong']
    result = """thông tin về dịch bệnh covid 19 tại Việt Nam như sau: dân số {data1} người\ntổng số ca nhiễm: {data5} \nsố ca đang điều trị {data2} ca \nsố bệnh nhân đã khỏi bệnh: {data4} bệnh nhân \nca nhiễm mới: {data3} \ntổng số ca dã tử vong: {data6}""".format(data1 = str(data1), data2 = str(data2), data3 = str(data3), data4 = str(data4), data5 = str(data5), data6 = str(data6))
    await ctx.send(result)
#xsmb
@bot.command()
async def xsmb(ctx):
    #xsmb
    url = 'http://manhict.tech/xsmb'
    get_data = requests.get(url)
    x = get_data.text
    json_xsmb = json.loads(x)
    data_xsmb = json_xsmb['data']
    await ctx.send(data_xsmb)
#weather
@bot.command()
async def weather(ctx, *, arg = None):
    if arg == None:
        await ctx.send('sai cú pháp')
    elif arg != None:
        url = f'https://api.accuweather.com/locations/v1/cities/search.json?q={arg}&apikey=d7e795ae6a0d44aaa8abb1a0a7ac19e4&language=vi-vn'
        image = f'http://mewdev.pro/api/v2/weather?location={arg}&apikey=Meew.90c3759fff62c248ba845561583c76fa'
        get_image = requests.get(image)
        get = requests.get(url)
        img_txt = get_image.text
        data_txt = get.text
        data_json = json.loads(data_txt)
        image_json = json.loads(img_txt)
        if len(data_json) != 0 and image_json['success'] == True:
            img = requests.get(image_json['data'])
            file = open("weather.png", "wb")
            file.write(img.content)
            file.close()
            key = data_json[0]['Key']
            get2 = requests.get(f'http://api.accuweather.com/forecasts/v1/daily/10day/{key}?apikey=d7e795ae6a0d44aaa8abb1a0a7ac19e4&details=true&language=vi')
            txt2 = get2.text
            json2 = json.loads(txt2) 
            temp_min = round((json2['DailyForecasts'][0]['Temperature']['Minimum']['Value'] - 32)/1.8)
            temp_max = round((json2['DailyForecasts'][0]['Temperature']['Maximum']['Value'] - 32)/1.8)
            feel_like = round((json2['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Value'] - 32)/1.8)
            sunrise = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Sun']['EpochRise']))
            sunset = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Sun']['EpochSet']))
            moonrise = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Moon']['EpochRise']))
            moonset = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Moon']['EpochSet']))
            day =  json2['DailyForecasts'][0]['Day']['LongPhrase']
            night = json2['DailyForecasts'][0]['Night']['LongPhrase']
            description = json2['Headline']['Text']      
            await ctx.send(f'Thời tiết hôm nay: {description}\n🌡️Nhiệt độ cao nhât - Thấp nhất: {temp_max}°C - {temp_min}°C\n🌡️Nhiệt độ cảm nhận được: {feel_like}°C\n🌅Mặt trời mọc: {sunrise}\n🌄Mặt trời lặn: {sunset}\n🌃Mặt trăng mọc: {moonrise}\n🌃Mặt trăng lặn: {moonset}\n🌞Ban ngày: {day}\n🌞Ban đêm: {night}', file = discord.File('weather.png'))
        elif len(data_json) != 0 and image_json['success'] == False:
            try:
                img = requests.get(f'https://manhict.tech/weather/vietnam?area={arg}&type=text/thoitiet')
                check = img.text
                if check == "Không tìm thấy địa điểm này!":
                    await ctx.send('error')
                else:
                    file = open("weather.png", "wb")
                    file.write(img.content)
                    file.close()
                    key = data_json[0]['Key']
                    get2 = requests.get(f'http://api.accuweather.com/forecasts/v1/daily/10day/{key}?apikey=d7e795ae6a0d44aaa8abb1a0a7ac19e4&details=true&language=vi')
                    txt2 = get2.text
                    json2 = json.loads(txt2) 
                    temp_min = round((json2['DailyForecasts'][0]['Temperature']['Minimum']['Value'] - 32)/1.8)
                    temp_max = round((json2['DailyForecasts'][0]['Temperature']['Maximum']['Value'] - 32)/1.8)
                    feel_like = round((json2['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Value'] - 32)/1.8)
                    sunrise = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Sun']['EpochRise']))
                    sunset = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Sun']['EpochSet']))
                    moonrise = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Moon']['EpochRise']))
                    moonset = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(json2['DailyForecasts'][0]['Moon']['EpochSet']))
                    day =  json2['DailyForecasts'][0]['Day']['LongPhrase']
                    night = json2['DailyForecasts'][0]['Night']['LongPhrase']
                    description = json2['Headline']['Text']     
                    await ctx.send(f'Thời tiết hôm nay: {description}\n🌡️Nhiệt độ cao nhât - Thấp nhất: {temp_max}°C - {temp_min}°C\n🌡️Nhiệt độ cảm nhận được: {feel_like}°C\n🌅Mặt trời mọc: {sunrise}\n🌄Mặt trời lặn: {sunset}\n🌃Mặt trăng mọc: {moonrise}\n🌃Mặt trăng lặn: {moonset}\n🌞Ban ngày: {day}\n🌞Ban đêm: {night}', file = discord.File('weather.png'))
            except Exception as e:
                print(e)
                await ctx.send('đã xảy ra lỗi không xác định')
        else:
            await ctx.send('error, lỗi chưa xác định')
    print(data_json['cod'])
    print(image_json['success'])
@bot.command()
async def youtube_search(ctx):
    await ctx.send('nhập từ khóa cần tìm kiếm')
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check = check)
    search = YoutubeSearch('{content}'.format(content = str(message.content)), max_results=5).to_json()
    search_dict = json.loads(search)
    for v in search_dict['videos']:
        result = 'https://www.youtube.com/watch?v=' + v['id'] + " - " + v['title'] + " của kênh " + v['channel']
        await ctx.send('đây là các kết quả tìm kiếm {result}'.format(result = result))
@bot.command()
@commands.is_owner()
async def offbot(ctx):
    if (ctx.message.author.id == 716146182849560598): 
        await ctx.send('đã tắt bot!')
        print("off bot")
        await ctx.bot.logout()
    else:
        await ctx.send('bạn không phải admin bot nên không đủ quyền hạn sử dụng lệnh này')
@bot.command()
async def ping(ctx):
    await ctx.send('pong!')
@bot.command()
async def play_taixiu(ctx, arg1 = None, arg2 = None):
    await open_account(ctx.message.author.id)
    member_data = await get_bank_data()
    if member_data[str(ctx.message.author.id)]["Wallet"] < int(arg2):
        await ctx.send('không đủ tiền để chơi:)')
    else:
        try:
            url = 'https://api.hclaptrinh.repl.co/api/taixiu'
            get = requests.get(url)
            data_txt = get.text
            data_json = json.loads(data_txt)
            result = data_json['result']
            if result == 'xiu':
                result = 'xỉu'
            elif result == 'tai':
                result = 'tài'
            if arg1 == None:
                await ctx.send('hãy cược tài hoặc xỉu')
            elif arg2 == None or int(arg2) <= 50:
                await ctx.send('số tiền cược không cược để trống và phải lớn hơn 50$')
            elif arg1 == result:
                gif = 'https://media1.giphy.com/media/ckHAdLU2OmY7knUClD/giphy.gif?cid=ecf05e47venaa45nhe4pmfsckgtrjasrpdzs6vtmpvwya6fk&rid=giphy.gif&ct=g'
                gif2 = 'https://media1.giphy.com/media/g9582DNuQppxC/giphy.gif?cid=ecf05e4743jop5ctofl2a5763ih04tc5b91dfnor287cu5tv&rid=giphy.gif&ct=g'
                em_load = discord.Embed(colour = ctx.author.color, description = 'đang lắc xúc sắc...')
                em_load.set_image(url = gif)
                em_win = discord.Embed(colour = ctx.author.color, description = f'bạn đã thắng kết quả là: {result} và gom về được {arg2}$ tiền thưởng')
                em_win.set_image(url = gif2)
                await ctx.send(embed = em_load)
                await asyncio.sleep(3)
                await ctx.send(embed = em_win)
                await update(ctx.message.author.id, arg2, 'keobuabao_win')
            elif arg1 != result:
                gif = 'https://media1.giphy.com/media/ckHAdLU2OmY7knUClD/giphy.gif?cid=ecf05e47venaa45nhe4pmfsckgtrjasrpdzs6vtmpvwya6fk&rid=giphy.gif&ct=g'
                gif2 = 'https://media3.giphy.com/media/l22ysLe54hZP0wubek/giphy.gif?cid=ecf05e47mba9xtd5rurzzo1flalwaqu6znpuld9vm6b2rz13&rid=giphy.gif&ct=g'
                em_load = discord.Embed(colour = ctx.author.color, description = 'đang lắc xúc sắc...')
                em_load.set_image(url = gif)
                em_win = discord.Embed(colour = ctx.author.color, description = f'bạn đã thua, kết quả là: {result} và mất {arg2}$ tiền cược')
                em_win.set_image(url = gif2)
                await ctx.send(embed = em_load)
                await asyncio.sleep(3)
                await ctx.send(embed = em_win)
                await update(ctx.message.author.id, arg2, 'keobuabao_lose')
            else:
                await ctx.send('lỗi')
        except Exception as e:
            print(e)
            await ctx.send('error')
@bot.command(name = "work")
@commands.cooldown(1, 3600, commands.BucketType.user)
async def work(ctx):
    await ctx.send('đây là các việc bạn có thể làm để kiếm tiền\n1. bán vé số\n2. sửa xe\n3. lập trình\n4. thợ hồ\n5. bán hàng online')
    def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["1", "2", "3", "4", "5"]
    message = await bot.wait_for('message', check = check)
    if message.content.lower() == "1":
        await open_account(message.author.id)
        member_data = await get_bank_data()
        earning = random.randrange(301)
        member_data[str(ctx.author.id)]['Bank'] += earning
        await ctx.send(f"bạn bán vé số và kiếm được {earning}$!")
        save_member_data(member_data)
    elif message.content.lower() == "2":
        await open_account(message.author.id)
        member_data = await get_bank_data()
        earning = random.randrange(301)
        member_data[str(ctx.author.id)]['Bank'] += earning
        await ctx.send(f"bạn làm thợ sửa xe và kiếm được {earning}$!")
        save_member_data(member_data)
    elif message.content.lower() == "3":
        await open_account(message.author.id)
        member_data = await get_bank_data()
        earning = random.randrange(301)
        member_data[str(ctx.author.id)]['Bank'] += earning
        save_member_data(member_data)
        await ctx.send(f"bạn làm lập trình viên và kiếm được {earning}$!")
    elif message.content.lower() == "4":
        await open_account(message.author.id)
        member_data = await get_bank_data()
        earning = random.randrange(301)
        member_data[str(ctx.author.id)]['Bank'] += earning
        save_member_data(member_data)
        await ctx.send(f"bạn làm thợ hồ và kiếm được {earning}$!")
    elif message.content.lower() == "5":
        await open_account(message.author.id)
        member_data = await get_bank_data()
        earning = random.randrange(301)
        member_data[str(ctx.author.id)]['Bank'] += earning
        save_member_data(member_data)
        await ctx.send(f"bạn bán hàng online và kiếm được {earning}$!")
    else:
        await ctx.send('bạn chỉ được chọn 1 trong 5 nghề trên')
@bot.event
async def on_command_error(ctx, error):
    pass
@work.error
async def work_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('bạn đã làm việc quá nhiều rồi, hãy nghỉ ngơi và quay lại sau {:.2f} giây'.format(error.retry_after))
@bot.command()
async def balance(ctx, member: discord.User=None):
    try:
        if member == None:
            await open_account(ctx.author.id)
            member_data = await get_bank_data()
            wallet = member_data[str(ctx.author.id)]['Wallet']
            bank = member_data[str(ctx.author.id)]["Bank"]
            embed = discord.Embed(title=f"số tiền của {ctx.author.display_name}")
            embed.add_field(name="tiền mặt", value=wallet)
            embed.add_field(name="trong thẻ ngân hàng", value=bank)
            await ctx.send(embed=embed)
        else:
            await open_account(member.id)
            member_data = await get_bank_data()
            wallet = member_data[str(member.id)]["Wallet"]
            bank = member_data[str(member.id)]["Bank"]
            embed = discord.Embed(title=f"số tiền của {member}")
            embed.add_field(name="tiền mặt", value=wallet)
            embed.add_field(name="trong thẻ ngân hàng", value= bank)
            await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        await ctx.send('error')
@bot.group(invoke_without_command=True)
async def bank(ctx):
    embed = discord.Embed(title="MIRAI BANK", description="nơi gửi và rút tiền từ ngân hàng", color=0x00ff00)
    embed.add_field(name = "cách sử dụng", value = "/bank withdraw, /bank deposit") #creates embed
    file = discord.File(r"image\bank.png", filename="bank.png") 
    embed.set_image(url="attachment://bank.png")
    await ctx.send(file=file, embed=embed)
@bank.command()
@commands.cooldown(3, 2400, commands.BucketType.user)
async def withdraw(ctx, arg = None):
    await open_account(ctx.message.author.id)
    member_data = await get_bank_data()
    if member_data[str(ctx.author.id)]["Bank"] < int(arg):
        await ctx.send('m ko đủ số tiền để rút, t ko ngu đâu mà đòi lừa=))')
    elif arg == None:
        await ctx.send('nhập số tiền cần rút')
    elif member_data[str(ctx.author.id)]["Bank"] >= int(arg):
        await ctx.send(f'đã rút {arg}$ từ tài khoản')
        await update(ctx.message.author.id, arg, 'bank')
@withdraw.error
async def withdraw_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('ngân hàng hỏng ATM rồi:((, hãy quay lại sau {:.2f} giây'.format(error.retry_after))
@bank.command(name = "deposit")
@commands.cooldown(3, 2400, commands.BucketType.user)
async def deposit(ctx, arg = None):
    await open_account(ctx.message.author.id)
    member_data = await get_bank_data()
    if arg == None:
        await ctx.send('nhập số tiền cần bỏ vào tài khoản')
    elif member_data[str(ctx.author.id)]["Wallet"] < int(arg):
        await ctx.send('m ko đủ số tiền để gửi vào tài khoản, t ko ngu đâu mà đòi lừa=))')
    elif member_data[str(ctx.author.id)]["Wallet"] >= int(arg):
        await ctx.send(f'đã trừ {arg}$ của ví')
        await update(ctx.message.author.id, arg, 'wallet')
@deposit.error
async def deposit_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('ngân hàng đóng cửa rồi, hãy quay lại sau {:.2f} giây'.format(error.retry_after))
@bank.command(name = "send")
@commands.cooldown(3, 2400, commands.BucketType.user)
async def send(ctx, member: discord.User=None, amount = None):
    await open_account(ctx.message.author.id)
    await open_account(member.id)
    data_send_user = await get_bank_data() 
    data_receive_user = await get_bank_data()
    if discord.User == None or amount == None or discord.User == None and amount == None:
        await ctx.send('sai cú pháp')
    elif data_send_user[str(ctx.author.id)]["Bank"] < int(amount):
        await ctx.send('không đủ số tiền trong tài khoản để gửi')
    else:
        try:
            await update(ctx.message.author.id, amount, 'send_user')
            await update(member.id, amount, 'receive_user')
            await ctx.send(f'đã chuyển tiền thành công cho {member.mention}')
        except Exception as e:
            print(e)
            await ctx.send('error')
@send.error
async def send_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('ngân hàng đóng cửa rồi, hãy quay lại sau {:.2f} giây'.format(error.retry_after))
@bot.command()
async def thinh(ctx):
    global random, json
    url = 'https://raw.githubusercontent.com/ledingg1997/ledingg-/main/datathinh.json'
    random_thinh = random.randint(1, 187)
    get = requests.get(url)
    data = get.text
    data_json = json.loads(data)
    result = data_json['data'][f'{random_thinh}']
    await ctx.send(result)
@bot.command()
async def keobuabao(ctx, arg1 = None, arg2 = None):
    await open_account(ctx.message.author.id)
    member_data = await get_bank_data()
    choice = ['kéo', 'búa', 'bao']
    bot = random.choice(choice)
    if member_data[str(ctx.author.id)]["Wallet"] < int(arg2):
        await ctx.send('ko đủ tiền để chơi')
    else:
        if arg1 == None or arg2 == None or arg1 == None and arg2 == None:
            await ctx.send('sai cú pháp')
        elif arg1 == bot:
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nkết quả: Hòa')
        elif arg1 == 'bao' and bot == 'búa':
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nkết quả: Bạn đã thắng và nhận đươc {arg2}$')
            await update(ctx.message.author.id, arg2, 'keobuabao_win')
        elif arg1 == 'bao' and bot == 'kéo':
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thua và mất {arg2}$')
            await update(ctx.message.author.id, arg2, 'keobuabao_lose')
        elif arg1 == 'kéo' and bot == 'búa':
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thua và mất {arg2}$')
            await update(ctx.message.author.id, arg2, 'keobuabao_lose')
        elif arg1 == 'kéo' and bot == 'bao':
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thắng và nhận được {arg2}$')
            await update(ctx.message.author.id, arg2, 'keobuabao_win')
        elif arg1 == 'búa' and bot == 'bao':
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thua và mất {arg2}$')
            await update(ctx.message.author.id, arg2, 'keobuabao_lose')
        elif arg1 == 'búa' and bot == 'kéo':
            await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thắng và nhận được {arg2}$')
            await update(ctx.message.author.id, arg2, 'keobuabao_win')
        else:
            await ctx.send('lỗi')
@bot.command()
async def vuatiengviet(ctx):
    try: 
        url_vuatiengviet = 'https://api.phamvandien.xyz/vuatiengviet/image?word='
        word_vuatiengviet = ["tôi yêu bạn", "cá koi", "cuốn sách", "tình yêu", "độc dược", "cô đọng", "huyền thoại", "sao băng", "quấn quýt", "bậc thầy", "ước vọng", "mơ mộng", "tình tứ", "mộng mơ", "nông nghiệp", "băng hà", "hiếu động", "sung sức", "công lao", "tâm tình", "cờ bạc", "ngu ngốc", "nông trường", "trường thọ", "tôn trọng"]
        random_word_vuatiengviet = random.choice(word_vuatiengviet)
        full_url_vuatiengviet = url_vuatiengviet + random_word_vuatiengviet
        get_vuatiengviet = requests.get(full_url_vuatiengviet)
        file = open("vuatiengviet.png", "wb")
        file.write(get_vuatiengviet.content)
        file.close()
        await ctx.send('đây là câu hỏi của bạn', file = discord.File('vuatiengviet.png'))
        if " " in random_word_vuatiengviet:
            def check(m):
                return m.author.id == ctx.author.id
            message = await bot.wait_for('message', check=check)
            if message.content.lower() == random_word_vuatiengviet:
                await ctx.send(f'bạn đã trả lời đúng, đáp án là "{random_word_vuatiengviet}"')
            else:
                await ctx.send(f'sai rồi đáp án là "{random_word_vuatiengviet}"')
    except:
        await ctx.send('hiện tại lệnh bạn đang sử dụng đã gặp lỗi, hãy thử lại sau. xin lỗi vì sự cố này')
@bot.command()
async def mark(ctx):
    try:
        await ctx.send('nhập điều bạn muốn ghi')
        def check(m):
            return m.author.id == ctx.author.id
        message = await bot.wait_for('message', check=check)
        url_mark = 'http://manhict.tech/markcmt?text='
        full_url_mark = url_mark + str(message.content)
        get_mark = requests.get(full_url_mark)
        file = open("mark.png", "wb")
        file.write(get_mark.content)
        file.close()
        await ctx.send('ảnh đây:)', file = discord.File('mark.png'))
    except:
        await ctx.send('hiện tại lệnh bạn đang sử dụng đã gặp lỗi, hãy thử lại sau. xin lỗi vì sự cố này')
@bot.command()
async def tiki(ctx):
    await ctx.send('nhập tên bạn vào đây (không nên để dấu)')
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check)
    url_tiki = 'https://api.phamvandien.xyz/tiki?text='
    full_url_tiki = url_tiki + str(message.content)
    get_tiki = requests.get(full_url_tiki)
    file = open("tiki.png", "wb")
    file.write(get_tiki.content)
    file.close()
    await ctx.send('ảnh đây:)', file = discord.File('tiki.png'))
@bot.command()
async def dhbc(ctx):
    global random
    try:
        url_DHBC = ['https://goatbot.tk/api/duoihinhbatchu', 'https://api.phamvandien.xyz/game/dhbcv1', 'https://www.nguyenmanh.name.vn/api/dhbc1?apikey=rcwGtaxg']
        random_dhbc = random.choice(url_DHBC)
        get_DHBC = requests.get(random_dhbc)
        data_DHBC = get_DHBC.text
        json_DHBC = json.loads(data_DHBC)
        if random_dhbc == 'https://goatbot.tk/api/duoihinhbatchu':
            image_DHBC = json_DHBC['data']['image1and2'] 
            sokt = json_DHBC['data']['soluongkt']
            dapan = json_DHBC['data']['wordcomplete']
            get_image_DHBC = requests.get(image_DHBC)
            file = open("DHBC.png", "wb")
            file.write(get_image_DHBC.content)
            file.close()
            await ctx.send(f'====ĐUỔI HÌNH BẮT CHỮ====\nđây là câu hỏi của bạn\ngợi ý: từ này có {sokt} chữ', file = discord.File('DHBC.png'))
            if "g" in random_dhbc:
                def check(m):
                    return m.author.id == ctx.author.id
                message = await bot.wait_for('message', check=check)
                if str(message.content.upper()) == dapan:
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là: {dapan}')
                else:
                    await ctx.send(f'sai rồi, đáp án là {dapan}')
        elif random_dhbc == 'https://api.phamvandien.xyz/game/dhbcv1':
            image_DHBC = json_DHBC['dataGame']['link'] 
            sokt = json_DHBC['dataGame']['sokitu']
            dapan = json_DHBC['dataGame']['tukhoa']
            get_image_DHBC = requests.get(image_DHBC)
            file = open("DHBC.png", "wb")
            file.write(get_image_DHBC.content)
            file.close()
            await ctx.send(f'====ĐUỔI HÌNH BẮT CHỮ====\nđây là câu hỏi của bạn\ngợi ý: từ này là {sokt}', file = discord.File('DHBC.png'))
            if "a" in random_dhbc:
                def check(m):
                    return m.author.id == ctx.author.id
                message = await bot.wait_for('message', check=check)
                if str(message.content.lower()) == dapan:
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là: {dapan}')
                else:
                    await ctx.send(f'sai rồi, đáp án là {dapan}')
        elif random_dhbc == 'https://www.nguyenmanh.name.vn/api/dhbc1?apikey=rcwGtaxg':
            image_DHBC = json_DHBC['result']['link'] 
            sokt = json_DHBC['result']['sokitu']
            dapan = json_DHBC['result']['tukhoa']
            get_image_DHBC = requests.get(image_DHBC)
            file = open("DHBC.png", "wb")
            file.write(get_image_DHBC.content)
            file.close()
            await ctx.send(f'====ĐUỔI HÌNH BẮT CHỮ====\nđây là câu hỏi của bạn\ngợi ý: từ này là {sokt}', file = discord.File('DHBC.png'))
            if "a" in random_dhbc:
                def check(m):
                    return m.author.id == ctx.author.id
                message = await bot.wait_for('message', check=check)
                if str(message.content.lower()) == dapan:
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là: {dapan}')
                else:
                    await ctx.send(f'sai rồi, đáp án là {dapan}')
    except Exception as e:
        print(e)
        await ctx.send('hiện tại lệnh bạn đang sử dụng đã gặp lỗi, hãy thử lại sau. xin lỗi vì sự cố này')
@bot.command()
async def noitu(ctx):
    await ctx.send('đã bắt đầu, hãy mở đầu trò chơi với một từ đầu tiên')
    while True:
        def check(m):
            return m.author.id == ctx.author.id
        message = await bot.wait_for('message', check=check)
        url_noitu = 'https://goatbot.tk/api/wordlink?text='
        full_url_noitu = url_noitu + str(message.content)
        get_noitu = requests.get(full_url_noitu)
        data_noitu = get_noitu.text
        json_noitu = json.loads(data_noitu)
        word_noitu = json_noitu['data']
        if "lose" in word_noitu:
            await ctx.send('bạn thắng rồi:((')
            break
        if message.content == "quit":
            await ctx.send('bạn thua rồiiiii:)')
            break
        else:
            await ctx.send(word_noitu)
@bot.command()
async def taoanhdep(ctx):
    await ctx.send('nhập để tạo ảnh theo mẫu sau:\n<id nhân vật> | <chữ nền> | <chữ kí>')
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check)
    url_taoanhdep = 'https://goatbot.tk/taoanhdep/avataranime?apikey=ntkhangGoatBot'
    value = message.content.lower().split(" | ")
    id_taoanhdep = str(value[0])
    chunen = str(value[1])
    chuky = str(value[2])
    complete_url_taoanhdep = url_taoanhdep + "&chu_Nen=" + chunen + "&chu_Ky=" + chuky + "&id=" +id_taoanhdep 
    get_taoanhdep = requests.get(complete_url_taoanhdep)
    file = open("taoanhdep.png", "wb")
    file.write(get_taoanhdep.content)
    file.close()
    await ctx.send('ảnh của bạn đây:>', file = discord.File('taoanhdep.png'))
@bot.command()
async def translate(ctx, arg = None):
    if arg == None:
        await ctx.send('do bạn không nhập ngôn ngữ cần chuyển nên bot sẽ sử dụng ngôn ngữ mặc định (ngôn ngữ gốc -> tiếng anh hoặc ngôn ngữ gốc -> tiếng việt ) nhập văn bản cần dịch')
        def check(m):
            return m.author.id == ctx.author.id
        message = await bot.wait_for('message', check=check)
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

        payload = f"q={message.content.lower()}"
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Key": "084e013269msh51bb766925d9cb1p188f2fjsn2ff8a09c96fd",
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        data = json.loads(response.text)
        src = data['data']['detections'][0][0]['language']
        if src == "vi":
            url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

            payload = f"q={message.content.lower()}&target=en&source=vi"
            headers = {
                "content-type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "application/gzip",
                "X-RapidAPI-Key": "084e013269msh51bb766925d9cb1p188f2fjsn2ff8a09c96fd",
                "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
            }

            response2 = requests.request("POST", url, data=payload, headers=headers)
            data = json.loads(response2.text)
            text = data['data']['translations'][0]['translatedText']
            await ctx.send(f'kết quả dịch: "{text}"')
        elif src == "en":
            url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

            payload = f"q={message.content.lower()}&target=vi&source=en"
            headers = {
                "content-type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "application/gzip",
                "X-RapidAPI-Key": "084e013269msh51bb766925d9cb1p188f2fjsn2ff8a09c96fd",
                "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
            }

            response3 = requests.request("POST", url, data=payload, headers=headers)
            data = json.loads(response3.text)
            text = data['data']['translations'][0]['translatedText']
            await ctx.send(f'kết quả dịch: "{text}"')
        else:
            url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

            payload = f"q={message.content.lower()}&target=vi&source={src}"
            headers = {
                "content-type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "application/gzip",
                "X-RapidAPI-Key": "084e013269msh51bb766925d9cb1p188f2fjsn2ff8a09c96fd",
                "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
            }

            response3 = requests.request("POST", url, data=payload, headers=headers)
            data = json.loads(response3.text)
            text = data['data']['translations'][0]['translatedText']
            await ctx.send(f'kết quả dịch: "{text}"')
    else:
        await ctx.send(f'bạn đã chọn ngôn ngữ cần dịch là "{arg}"\nvui lòng nhập văn bản cần dịch')
        def check(m):
            return m.author.id == ctx.author.id
        message = await bot.wait_for('message', check=check)
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

        payload = f"q={message.content.lower()}"
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Key": "084e013269msh51bb766925d9cb1p188f2fjsn2ff8a09c96fd",
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

        response4 = requests.request("POST", url, data=payload, headers=headers)
        data = json.loads(response.text)
        src = data['data']['detections'][0][0]['language']
        if response4.status_code != 200:
            await ctx.send('error')
        elif response4.status_code == 200:
            data = json.loads(response4.text)
            text = data['data']['translations'][0]['translatedText']
            await ctx.send(f'kết quả dịch: "{text}"')
@bot.command()
async def caunoihay(ctx):
    sentence = ['Một cách để tận dụng tối đa cuộc sống là xem nó như một cuộc phiêu lưu – William Feather',' Mạnh dạn nói Tôi đã sai là cách ta chấp nhận đối mặt với tình huống khó khăn. Việc đó có phần mạo hiểm nhưng những gì ta nhận được sẽ vượt ngoài sự mong đợi’ - Rich DeVos', 'Tích cực, tự tin và kiên trì là chìa khóa trong cuộc sống. Vì vậy đừng bao giờ từ bỏ chính mình’ – Khalid', 'Yêu tôi hay ghét tôi, cả hai đều có lợi cho tôi. Nếu bạn yêu tôi, tôi sẽ luôn ở trong tim bạn và nếu bạn ghét tôi, tôi sẽ ở trong tâm trí bạn’ – Baland Quandeel', 'Thái độ quan trọng hơn quá khứ, hơn giáo dục, hơn tiền bạc, hơn hoàn cảnh, hơn những gì mọi người làm hoặc nói. Nó quan trọng hơn ngoại hình, năng khiếu hay kỹ năng’ – Charles Swindoll', 'Hãy tin vào chính mình! Có niềm tin vào khả năng của bạn! Nếu không có sự tự tin khiêm tốn nhưng hợp lý vào năng lực của chính mình, bạn không thể thành công hay hạnh phúc’ - Norman Vincent Peale', 'Trong đời người, có hai con đường bằng phẳng không trở ngại: Một là đi tới lý tưởng, một là đi tới cái chết’ - Lev Tolstoy', 'Bạn có thể thay đổi thế giới của mình bằng cách thay đổi lời nói của bạn ... Hãy nhớ rằng, cái chết và sự sống nằm trong sức mạnh của lưỡi’ - Joel Osteen', 'Lạc quan là niềm tin dẫn đến thành tích. Không có gì có thể được thực hiện mà không có hy vọng và sự tự tin’ - Helen Keller', '‘Nếu bạn muốn thành công, bạn nên tìm ra những con đường mới, thay vì đi trên những con đường mòn của sự thành công được chấp nhận’ - John D. Rockefeller', '‘Nếu bạn không thích cái gì đó, hãy thay đổi nó. Nếu bạn không thể thay đổi nó, hãy thay đổi thái độ của bạn’ - Maya Angelou']
    result_sentence = random.choice(sentence)
    await ctx.send(result_sentence)
@bot.command()
async def thayboi(ctx):
    random_card = ['con bốc được lá ♥️, Cơ là nước bài màu đỏ, được thể hiện bằng hình vẽ tim sẽ cho bạn những dự đoán trong chuyện tình cảm, hôn nhân vợ chồng, gia đình nói chung… Vận lá bài nước Cơ hên hay xui, may hay rủi còn phụ thuộc vào những con số của chúng.', 'con bốc được lá ♦️, là nước bài nổi bật với hình vẽ tượng trưng tựa như hình thoi dựng đứng, con Rô là dự báo tốt về đường công danh, sự nghiệp vững vàng, sự sung túc về tiền bạc.', 'con bốc được lá ♣️. Trong hình tượng như cái cây mang màu đen, nước Chuồn mang theo sự tốt lành về nhân duyên, tiền bạc, sự nghiệp, cuộc sống… Tóm lại, nước Chuồn báo hiệu sự viên mãn của đời người. Vì vậy nên trong ngôn ngữ của bói bài, người ta hay nói: “Có Chuồn là có tiền"', 'con bốc được lá ♠️. Đây có lẽ là nước bài không được trông chờ nhất trong các quân bài Tây vì ý nghĩa của nó mang lại thật sự không tốt. Người có quân bài nước này thường gặp những vướng mắc và khó khăn khó giải quyết ở nhiều phương diện.\nCon người: hay ốm đau, bệnh vặt, phải vươn lên trong vất vả.\nSự nghiệp công danh: khó thăng tiến, luôn gặp trắc trở, vật cản…\nTình duyên: lận đận, gãy gánh, chia cắt…']
    result =  random.choice(random_card)
    await ctx.send(result)
@bot.group(invoke_without_command=True)
async def truyentranh(ctx):
    await ctx.send('đọc, tìm, xem các truyện mới ra trên truyentranh24.com và toptruyen\nsử dụng: /truyentranh search <keyword> (tìm kiếm truyện)\ntruyentranh news (các truyện mới nhất truyên toptruyen)')
@truyentranh.command()
async def search(ctx, *, arg = None):
    if arg == None:
        await ctx.send('phần tìm kiếm truyện không được để trống')
    else:
        full_url_search = 'https://goatbot.tk/truyentranh24/search?q=' + str(arg) + '&apikey=ntkhang'
        get_search = requests.get(full_url_search)
        json = get_search.json()
        name = json['data'][0]['name']
        img = json['data'][0]['thumbnail']
        get_img = requests.get(img)
        file = open("truyentranh.png", "wb")
        file.write(get_img.content)
        file.close()
        href = json['data'][0]['href']  
        result = str(name) + '\n' + 'href: ' + str(href)
        await ctx.send(result, file = discord.File('truyentranh.png'))
@truyentranh.command()
async def news(ctx):
    try:
        full_url = 'https://thieutrungkien.up.railway.app/toptruyen/'
        get = requests.get(full_url)
        data_txt = get.text
        data_json = json.loads(data_txt)
        truyen1_name = data_json['data'][0]['name']
        truyen1_link = data_json['data'][0]['url']
        truyen2_name = data_json['data'][1]['name']
        truyen2_link = data_json['data'][1]['url']
        truyen3_name = data_json['data'][2]['name']
        truyen3_link = data_json['data'][2]['url']
        truyen4_name = data_json['data'][3]['name']
        truyen4_link = data_json['data'][3]['url']
        truyen5_name = data_json['data'][4]['name']
        truyen5_link = data_json['data'][4]['url']
        truyen1_image = data_json['data'][0]['images']
        get_img = requests.get(truyen1_image)
        file = open("truyentranh.png", "wb")
        file.write(get_img.content)
        file.close()
        await ctx.send(f'top 5 các truyện mới nhất trên toptruyen.net\n\n**{truyen1_name}**\nlink: {truyen1_link}\n\n**{truyen2_name}**\nlink: {truyen2_link}\n\n**{truyen3_name}\nlink: {truyen3_link}**\n\n**{truyen4_name}**\nlink: {truyen4_link}\n\n**{truyen5_name}**\nlink: {truyen5_link}',file = discord.File('truyentranh.png'))
    except Exception as e:
        print(e)
        await ctx.send('error')
@bot.command()
async def shopmaihuong(ctx):
    try:
        await ctx.send('nhập tin nhắn để tạo ảnh theo mẫu sau:\ntext1 | text2')
        def check(m):
            return m.author.id == ctx.author.id
        message = await bot.wait_for('message', check=check)
        value = message.content.lower().split(" | ")
        text1 = str(value[0])
        text2 = str(value[1])
        url = 'https://api.phamvandien.xyz/shopmaihuong?text1=' + text1 + "&text2=" + text2
        get = requests.get(url)
        file = open("shopmaihuong.png", "wb")
        file.write(get.content)
        file.close()
        await ctx.send('ảnh của bạn đây:)', file = discord.File('shopmaihuong.png'))
    except:
        await ctx.send('hiện tại lệnh bạn đang sử dụng đã gặp lỗi, hãy thử lại sau. xin lỗi vì sự cố này')
@bot.command()
async def wiki(ctx, *, arg = None):
    if arg == None:
        await ctx.send('/wiki <keyword>\nphần tìm kiếm không được để trống')
    else:
        wikipedia.set_lang("vi")
        result = wikipedia.summary(f"{arg}", sentences=5)
        await ctx.send(result)
@bot.command()
async def callad(ctx, *, arg=None):
    user = await bot.fetch_user("716146182849560598")
    await user.send(f"báo cáo từ: {ctx.message.author}\nid: {ctx.message.author.id}\ntừ nhóm: {ctx.channel.id}\nnội dung: {arg}")
    await ctx.send('đã báo cáo về admin thành công')
@bot.command()
async def sendnoti(ctx):
    await ctx.send('nhập theo mẫu sau:\n<id channel> | phản hồi user | phản hồi channel | <id user>')
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check)
    value = message.content.lower().split(" | ")
    id_channel = str(value[0])
    reply_user = str(value[1])
    reply_channel = str(value[2])
    id_user = str(value[3])
    channel = await bot.fetch_channel(id_channel)
    user = await bot.fetch_user(f"{id_user}")
    await user.send(f'cảm ơn bạn về đóng góp, sau đây là phản hồi của admin:\n{reply_user}')
    await channel.send(f'phản hồi từ admin đến kênh:\nnội dung: {reply_channel}')
@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    await open_account(ctx.message.author.id)
    member_data = await get_bank_data()
    member_data[str(ctx.message.author.id)]['Wallet'] += 100
    save_member_data(member_data)
    await ctx.send('nhận thưởng online thành công 100$')
@daily.error
async def daily_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('bạn đã nhận thưởng ngày hôm nay rồi hãy quay lại sau {:.2f} giây'.format(error.retry_after))
@bot.command()
async def slot(ctx, arg = None):
    await open_account(ctx.message.author.id)
    member_data = await get_bank_data()
    if member_data[str(ctx.message.author.id)]['Wallet'] < int(arg):
        await ctx.send('tiền cược không hợp lệ')
    else:
        try:
            if int(arg) == None:
                await ctx.send('sai cú pháp')
            else:
                url = 'https://manhict.tech/game/slot'
                get = requests.get(url)
                data_txt = get.text
                data = json.loads(data_txt)
                slot = data['data']
                if data['result'] == "lose":
                    await ctx.send(f'====SLOT====\nkết quả: {slot}\nBạn đã thua! {arg}$')
                    await update(ctx.message.author.id, arg, 'keobuabao_lose')
                elif data['result'] == "win":
                    await ctx.send(f'====SLOT====\nkết quả: {slot}\nBạn đã thắng {arg}$')
                    await update(ctx.message.author.id, arg, 'keobuabao_win')
        except:
            await ctx.send('hiện tại lệnh bạn đang sử dụng đã gặp lỗi, hãy thử lại sau. xin lỗi vì sự cố này')
@bot.command()
async def news(ctx):
    get = requests.get('https://vnexpress.net/')
    soup = BeautifulSoup( get.content , 'html.parser')
    results = []
    dess = []
    for result in soup.find_all(class_ = 'title-news'):
        results.append(result.text)
        results.append(result.a.get('href'))
    for des in soup.find_all(class_ = 'description'):
        dess.append(des.text)
    title = results[0]
    link = results[1]
    des = dess[1]
    await ctx.send(f'tin mới nhất hôm nay: {title}{des}\nlink: {link}')
@bot.command()
async def dovui(ctx):
    try:
        get = requests.get('https://www.nguyenmanh.name.vn/api/dovui2?apikey=rcwGtaxg')
        data_txt = get.text
        data_json = json.loads(data_txt)
        question = data_json['result']['question']
        option = data_json['result']['option']
        result = data_json['result']['correct']
        if len(option) == 3:
            option1 = data_json['result']['option'][0]
            option2 = data_json['result']['option'][1]
            option3 = data_json['result']['option'][2]
            await ctx.send(f'{question}\n1. {option1}\n2. {option2}\n3. {option3}\nTrả lời theo số thứ tự các đáp')
            def check(m):
                return m.author.id == ctx.author.id
            message = await bot.wait_for('message', check=check)
            if int(message.content.lower()) == result:
                if result == 1:
                    result = option1
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
                elif result == 2:
                    result = option2
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
                elif result == 3:
                    result = option3
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
            elif int(message.content.lower()) != result:
                if result == 1:
                    result = option1
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
                elif result == 2:
                    result = option2
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
                elif result == 3:
                    result = option3
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
        elif len(option) == 4:
            option1 = data_json['result']['option'][0]
            option2 = data_json['result']['option'][1]
            option3 = data_json['result']['option'][2]
            option4 = data_json['result']['option'][3]
            await ctx.send(f'{question}\n1. {option1}\n2. {option2}\n3. {option3}\n4. {option4}\nTrả lời theo số thứ tự các đáp')
            def check(m):
                return m.author.id == ctx.author.id
            message = await bot.wait_for('message', check=check)
            if int(message.content.lower()) == result:
                if result == 1:
                    result = option1
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
                elif result == 2:
                    result = option2
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
                elif result == 3:
                    result = option3
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
                elif result == 4:
                    result = option4
                    await ctx.send(f'bạn đã trả lời đúng, đáp án là {result}')
            elif int(message.content.lower()) != result:
                if result == 1:
                    result = option1
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
                elif result == 2:
                    result = option2
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
                elif result == 3:
                    result = option3
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
                elif result == 4:
                    result = option4
                    await ctx.send(f'bạn đã trả lời sai rồi:(, đáp án đúng là {result}')
    except Exception as e:
        print(e)
        await ctx.send(f'lệnh bạn đang sử dụng đã xảy ra lỗi, hãy báo cáo về admin bằng lệnh {prefix}callad, hoặc câu trả lời của bạn không phải là một con số')
@bot.command(name = "setmoney")
async def setmoney(ctx, arg = None, arg2 = None):
    if arg == None or arg2 == None or arg == None and arg2 == None:
        await ctx.send('sai cú pháp')
    elif ctx.message.author.id != 716146182849560598:
        await ctx.send('bạn không phải admin nên không có quyền sử dụng lệnh này')
    else:
        await update(ctx.message.author.id, arg, arg2)
        await ctx.send('done')
@bot.command(name = "google_search")
async def google_search(ctx, *, arg = None):
    url = f"https://google-search3.p.rapidapi.com/api/v1/search/q={arg}"
    headers = {
            "X-User-Agent": "desktop",
            "X-Proxy-Location": "VI",
            "X-RapidAPI-Key": "084e013269msh51bb766925d9cb1p188f2fjsn2ff8a09c96fd",
            "X-RapidAPI-Host": "google-search3.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    if arg == None:
        await ctx.send('phần tìm kiếm không được để trống')
    elif len(data['results']) != 0:
        url = f"https://google-search3.p.rapidapi.com/api/v1/search/q={arg}"
        headers = {
            "X-User-Agent": "desktop",
            "X-Proxy-Location": "VI",
            "X-RapidAPI-Key": "084e013269msh51bb766925d9cb1p188f2fjsn2ff8a09c96fd",
            "X-RapidAPI-Host": "google-search3.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        data = json.loads(response.text)
        result1_des = data['results'][0]['description']
        result1_title = data['results'][0]['title']
        result1_link = data['results'][0]['link']
        await ctx.send(f'kết quả search google hàng đầu cho từ khóa "{arg}":\n{result1_title}\n-{result1_des}-\nlink: {result1_link}')
    else:
        await ctx.send('không có kết quả cho từ khóa bạn nhập')
#Functions
async def open_account(user):
    users = await get_bank_data()

    if str(user) in users:
        return False
    else:
        users[str(user)] = {}
        users[str(user)]["Wallet"] = 0
        users[str(user)]["Bank"] = 0
        users[str(user)]["pc"] = 0

    with open("data.json", 'w') as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open("data.json", 'r') as f:
        users = json.load(f)
    return users
async def update(user, change, mode):
    await open_account(user)
    member_data = await get_bank_data()
    if mode == 'wallet':
        member_data[str(user)]['Wallet'] -= int(change)
        member_data[str(user)]['Bank'] += int(change)
        save_member_data(member_data)
    elif mode == 'bank':
        member_data[str(user)]['Wallet'] += int(change)
        member_data[str(user)]['Bank'] -= int(change)
        save_member_data(member_data)
    elif mode == 'keobuabao_win':
        member_data[str(user)]['Wallet'] += int(change)
        save_member_data(member_data)
    elif mode == 'keobuabao_lose':
        member_data[str(user)]['Wallet'] -= int(change)
        save_member_data(member_data)
    elif mode == 'receive_user':
        member_data[str(user)]['Bank'] += int(change)
        save_member_data(member_data)
    elif mode == 'send_user':
        member_data[str(user)]['Bank'] -= int(change)
        save_member_data(member_data)
    elif mode == 'setmoney-wallet':
        member_data[str(user)]['Wallet'] = int(change)
        save_member_data(member_data)
    elif mode == 'setmoney-bank':
        member_data[str(user)]['Bank'] = int(change)
        save_member_data(member_data)
    else:
        print('error')
def save_member_data(data):
    with open("data.json", 'w') as f:
        json.dump(data, f)
bot.run('token')
#credit: Duc Anh
