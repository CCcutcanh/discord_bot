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
from googletrans import Translator
import asyncio
import wikipedia
import datetime
import time
from bs4 import BeautifulSoup
bot = commands.Bot(command_prefix='/') 
bot.remove_command("help")
data_filename = "data.pickle"
@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "help", description = "sử dụng /help để biết các lệnh có thể sử dụng trên bot")
    em.add_field(name = "other command", value = "xsmb, covid19, weather, youtube_search, translate, truyentranh24, wiki")
    em.add_field(name = "game command", value = "dovui, play_taixiu, keobuabao, vuatiengviet, dhbc(đuổi hình bắt chữ), noitu")
    em.add_field(name = "role play command", value = "balance, bank, shop, work")
    em.add_field(name = "default command bot", value = "help, offbot, ping")
    em.add_field(name = "fun command", value = "thinh, mark, tiki, taoanhdep, shopmaihuong")
    await ctx.send(embed = em)
class Data:
    def __init__(self, wallet, bank, pc):
        self.wallet = wallet
        self.bank = bank
        self.pc = pc
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
    url = f'https://api.openweathermap.org/data/2.5/weather?q={arg}&lang=vi&appid=f5e58e5107262dd200ef30cc9e47355a'
    image = f'http://mewdev.pro/api/v2/weather?location={arg}&apikey=Meew.90c3759fff62c248ba845561583c76fa'
    get_image = requests.get(image)
    get = requests.get(url)
    img_txt = get_image.text
    data_txt = get.text
    data_json = json.loads(data_txt)
    image_json = json.loads(img_txt)
    if arg == None:
        await ctx.send('sai cú pháp')
    elif data_json['cod'] != "404" and image_json['success'] == True:
        img = requests.get(image_json['data'])
        file = open("weather.png", "wb")
        file.write(img.content)
        file.close()
        temp_min = data_json['main']['temp_min'] - 273.15
        temp_max = data_json['main']['temp_max'] - 273.15
        feel_like = data_json['main']['feels_like'] - 273.15
        sunrise = datetime.datetime.fromtimestamp(int(data_json['sys']['sunrise']))
        sunset = datetime.datetime.fromtimestamp(int(data_json['sys']['sunset']))
        description = data_json['weather'][0]['description']      
        await ctx.send(f'🌡️nhiệt độ cao nhât - thấp nhất: {temp_max} - {temp_min}\n🌡️nhiệt độ cảm nhận được: {feel_like}\n🌅mặt trời mọc: {sunrise}\n🌄mặt trời lặn: {sunset}\n🗄️mô tả: {description}', file = discord.File('weather.png'))
    else:
        await ctx.send('thành phố không tồn tại\nhãy thử viết tên thành phố không dấu, cách giữa hai từ\nví dụ: /weather ha noi')
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
async def offbot(ctx, m):
    if (m.author.id == ctx.author.id == 716146182849560598): 
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
            em_load = discord.Embed(colour = ctx.author.color, description = 'lắc xúc sắc...')
            em_load.set_image(url = gif)
            em_win = discord.Embed(colour = ctx.author.color, description = f'bạn đã thắng kết quả là: {result} và gom về được {arg2}$ tiền thưởng')
            em_win.set_image(url = gif2)
            await ctx.send(embed = em_load)
            await asyncio.sleep(3)
            await ctx.send(embed = em_win)
            update(ctx.message.author.id, arg2, 'keobuabao_win')
        elif arg1 != result:
            gif = 'https://media1.giphy.com/media/ckHAdLU2OmY7knUClD/giphy.gif?cid=ecf05e47venaa45nhe4pmfsckgtrjasrpdzs6vtmpvwya6fk&rid=giphy.gif&ct=g'
            gif2 = 'https://media1.giphy.com/media/g9582DNuQppxC/giphy.gif?cid=ecf05e4743jop5ctofl2a5763ih04tc5b91dfnor287cu5tv&rid=giphy.gif&ct=g'
            em_load = discord.Embed(colour = ctx.author.color, description = 'lắc xúc sắc...')
            em_load.set_image(url = gif)
            em_win = discord.Embed(colour = ctx.author.color, description = f'bạn đã thua, kết quả là: {result} và mất {arg2}$ tiền cược')
            em_win.set_image(url = gif2)
            await ctx.send(embed = em_load)
            await asyncio.sleep(3)
            await ctx.send(embed = em_win)
            update(ctx.message.author.id, arg2, 'keobuabao_lose')
        else:
            await ctx.send('lỗi')
    except Exception as e:
        print(e)
        await ctx.send('error')
@bot.command()
async def dovui(ctx):
    url_dovui = 'http://manhict.tech/game/dovuiv1'
    get_dovui = requests.get(url_dovui)
    data_dovui = get_dovui.text
    json_dovui = json.loads(data_dovui)
    cau_hoi = json_dovui['questions']
    a_dv = json_dovui['a']
    b_dv = json_dovui['b']
    c_dv = json_dovui['c']
    d_dv = json_dovui['d']
    dap_an = json_dovui['dapan']
    result_dovui = """{cau_hoi} \nA.{a}\nB.{b}\nC.{c}\nD.{d}""".format(cau_hoi = str(cau_hoi), a = str(a_dv), b = str(b_dv), c = str(c_dv), d = str(d_dv))
    await ctx.send(result_dovui)
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check = check)
    if(message.content == dap_an):
        await ctx.send('câu trả lời chính xác, đáp án là {dap_an}'.format(dap_an = str(dap_an)))
    if(message.content != dap_an):
        await ctx.send('chưa chính xác rồiiiii:((, đáp án là {dap_an}'.format(dap_an = str(dap_an)))
@bot.command(name = "work")
@commands.cooldown(1, 3600, commands.BucketType.user)
async def work(ctx):
    await ctx.send('đây là các việc bạn có thể làm để kiếm tiền\n1. bán vé số\n2. sửa xe\n3. lập trình\n4. thợ hồ\n5. bán hàng online')
    def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["1", "2", "3", "4", "5"]
    message = await bot.wait_for('message', check = check)
    if message.content.lower() == "1":
        member_data = load_member_data(message.author.id)
        earning = random.randrange(301)
        member_data.bank += earning
        await ctx.send(f"bạn bán vé số và kiếm được {earning}$!")
        save_member_data(message.author.id, member_data)
    if message.content.lower() == "2":
        member_data = load_member_data(message.author.id)
        earning = random.randrange(301)
        member_data.bank += earning
        await ctx.send(f"bạn làm thợ sửa xe và kiếm được {earning}$!")
        save_member_data(message.author.id, member_data)
    if message.content.lower() == "3":
        member_data = load_member_data(message.author.id)
        earning = random.randrange(301)
        member_data.bank += earning
        await ctx.send(f"bạn làm lập trình viên và kiếm được {earning}$!")
        save_member_data(message.author.id, member_data)
    if message.content.lower() == "4":
        member_data = load_member_data(message.author.id)
        earning = random.randrange(301)
        member_data.bank += earning
        await ctx.send(f"bạn làm thợ hồ và kiếm được {earning}$!")
        save_member_data(message.author.id, member_data)
    if message.content.lower() == "5":
        member_data = load_member_data(message.author.id)
        earning = random.randrange(301)
        member_data.bank += earning
        await ctx.send(f"bạn bán hàng online và kiếm được {earning}$!")
        save_member_data(message.author.id, member_data)
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
async def balance(message):
    member_data = load_member_data(message.author.id)
    embed = discord.Embed(title=f"số tiền của {message.author.display_name}")
    embed.add_field(name="tiền mặt", value=str(member_data.wallet))
    embed.add_field(name="trong thẻ ngân hàng", value=str(member_data.bank))

    await message.channel.send(embed=embed)
@bot.group(invoke_without_command=True)
async def shop(ctx):
    await ctx.send('nơi mua bán các vật trong bot\nhãy chọn shop sell(bán đồ) hoặc shop buy(mua đồ)')
@shop.command()
async def sell(ctx):
    await ctx.send('đồ có thể bán\n1. máy tính: 700 tiền\nLưu ý: đây chỉ là lệnh đag thử nghiệm, sẽ update sau')
    def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["1"]
    message = await bot.wait_for('message', check = check)
    if(message.content.lower() == "1"):
        member_data = load_member_data(message.author.id)
        if member_data.pc == 1:
            member_data.bank += 700
            member_data.pc = 0
            await ctx.send('giao dịch thành công')
            save_member_data(message.author.id, member_data)
        else:
            await ctx.send('bạn bạn không có máy tính để bán')
    else:
        await ctx.send('đồ bạn muốn bán không hợp lệ')
        save_member_data(message.author.id, member_data)
@shop.command()
async def buy(ctx):
    await ctx.send('đồ có thể mua\n1. pc: 1500 tiền,')
    def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["1"]
    message = await bot.wait_for('message', check = check)
    if(message.content.lower() == "1"):
        member_data = load_member_data(message.author.id)
        if member_data.pc == 1:
            await ctx.send('bạn đã có pc rồi, mua làm gì nữa')
        else:
            if member_data.bank >= 1500:
                member_data.bank -= 1500
                member_data.pc = 1
                await ctx.send('giao dịch thành công')
                save_member_data(message.author.id, member_data)
            else:
                await ctx.send('bạn quá nghèo để mua được máy tính')
    else:
        await ctx.send('sai cú pháp, món đồ bạn cần mua không tồn tại')
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
    if arg == None:
        await ctx.send('nhập số tiền cần rút')
    else:
        await ctx.send(f'đã rút {arg}$ từ tài khoản')
        update(ctx.message.author.id, arg, 'bank')
@withdraw.error
async def withdraw_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('ngân hàng hỏng ATM rồi:((, hãy quay lại sau {:.2f} giây'.format(error.retry_after))
@bank.command(name = "deposit")
@commands.cooldown(3, 2400, commands.BucketType.user)
async def deposit(ctx, arg = None):
    if arg == None:
        await ctx.send('nhập số tiền cần bỏ vào tài khoản')
    else:
        await ctx.send(f'đã trừ {arg}$ của ví')
        update(ctx.message.author.id, arg, 'wallet')
@deposit.error
async def deposit_error(ctx, error):
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
    member_data = load_member_data(ctx.message.author.id)
    choice = ['kéo', 'búa', 'bao']
    bot = random.choice(choice)
    if arg1 == None or arg2 == None or arg1 == None and arg2 == None:
        await ctx.send('chỉ nhập kéo, búa hoặc bao')
    elif arg1 == bot:
        await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nkết quả: Hòa')
    elif arg1 == 'bao' and bot == 'búa':
        await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nkết quả: Bạn đã thắng và nhận đươc {arg2}$')
        update(ctx.message.author.id, arg2, 'keobuabao_win')
    elif arg1 == 'bao' and bot == 'kéo':
        await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thua và mất {arg2}$')
        update(ctx.message.author.id, arg2, 'keobuabao_lose')
    elif arg1 == 'kéo' and bot == 'búa':
        await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thua và mất {arg2}$')
        update(ctx.message.author.id, arg2, 'keobuabao_lose')
    elif arg1 == 'kéo' and bot == 'bao':
        await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thắng và nhận được {arg2}$')
        update(ctx.message.author.id, arg2, 'keobuabao_win')
    elif arg1 == 'búa' and bot == 'bao':
        await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thua và mất {arg2}$')
        update(ctx.message.author.id, arg2, 'keobuabao_lose')
    elif arg1 == 'búa' and bot == 'kéo':
        await ctx.send(f'[kéo búa bao]\nbot chọn: {bot}\nbạn chọn: {arg1}\nKết quả: Bạn đã thắng và nhận được {arg2}$')
        update(ctx.message.author.id, arg2, 'keobuabao_win')
    else:
        await ctx.send('lỗi')
@bot.command()
async def vuatiengviet(ctx):
    try: 
        url_vuatiengviet = 'https://api.phamvandien.xyz/vuatiengviet/image?word='
        word_vuatiengviet = ["tôi yêu bạn", "cá koi", "cuốn sách", "tình yêu", "độc dược", "cô đọng", "huyền thoại", "sao băng", "quấn quýt", "bậc thầy", "ước vọng", "mơ mộng", "tình tứ", "mộng mơ", "nông nghiệp", "băng hà", "hiếu động", "sung sức", "công lao", "tâm tình", "cờ bạc", "ngu ngốc"]
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
            if message.content == random_word_vuatiengviet:
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
    url_tiki = 'http://manhict.tech/tiki?text='
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
async def translate(ctx):
    await ctx.send('nhập văn bản cần dịch')
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check)
    translator = Translator()
    translated = translator.translate(f'{message.content.lower()}', src='auto', dest='vi')
 
    await ctx.send(translated.text)
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
        url = 'https://manhict.tech/shopmaihuong?text1=' + text1 + "&text2=" + text2
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
    await user.send(f"báo cáo từ {ctx.message.author}\ntừ nhóm: {ctx.channel.id}\nnội dung: {arg}")
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
    member_data = load_member_data(ctx.message.author.id)
    member_data.wallet += 100
    save_member_data(ctx.message.author.id, member_data)
    await ctx.send('nhận thưởng ngày thành công 100$')
@daily.error
async def daily_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('bạn đã nhận thưởng ngày hôm nay rồi hãy quay lại sau {:.2f} giây'.format(error.retry_after))
@bot.command()
async def slot(ctx, arg = None):
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
                update(ctx.message.author.id, arg, 'keobuabao_lose')
            elif data['result'] == "win":
                await ctx.send(f'====SLOT====\nkết quả: {slot}\nBạn đã thắng {arg}$')
                update(ctx.message.author.id, arg, 'keobuabao_win')
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

#Functions
def load_data():
    if os.path.isfile(data_filename):
        with open(data_filename, "rb") as file:
            return pickle.load(file)
    else:
        return dict()

def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)
def update(user, change, mode):
    member_data = load_member_data(user)
    if mode == 'wallet':
        member_data.wallet -= int(change)
        member_data.bank += int(change)
        save_member_data(user, member_data)
    elif mode == 'bank':
        member_data.wallet += int(change)
        member_data.bank -= int(change)
        save_member_data(user, member_data)
    elif mode == 'keobuabao_win':
        member_data.wallet += int(change)
        save_member_data(user, member_data)
    elif mode == 'keobuabao_lose':
        member_data.wallet -= int(change)
        save_member_data(user, member_data)
    else:
        print('error')
bot.run('token')
#credit: Duc Anh
