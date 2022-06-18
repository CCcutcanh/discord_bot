import discord
from discord.ext import commands
import json 
import os
import requests
from youtube_search import YoutubeSearch
from PIL import *
import random
import pickle
import youtube_dl
import os
import random
from googletrans import Translator
import asyncio
import wikipedia
import datetime
import time
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
    full_url = 'http://manhict.tech/covid?country=viet%20nam'
    get = requests.get(full_url)
    data = get.text
    parse_json = json.loads(data)
    data1 = parse_json['data']['danso']
    data2 = parse_json['data']['dangdieutri']
    data3 = parse_json['data']['ca_nhiem_moi']
    data4 = parse_json['data']['hoiphuc']
    data5 = parse_json['data']['total']
    data6 = parse_json['data']['tong_ca_tu_vong']
    result = """thông tin về dịch bệnh covid 19 tại Việt Nam như sau: dân số {data1} \nngười tổng số ca nhiễm: {data5} \nsố ca đang điều trị {data2} ca \nsố bệnh nhân đã khỏi bệnh: {data4} bệnh nhân \nca nhiễm mới: {data3} \ntổng số ca dã tử vong: {data6}""".format(data1 = str(data1), data2 = str(data2), data3 = str(data3), data4 = str(data4), data5 = str(data5), data6 = str(data6))
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
async def play_taixiu(ctx):
    await ctx.send('đã bắt đầu game tài xỉu, nếu không biết luật bạn có thể nhập hd để biết rõ luật chơi và nhập quit để out game')
    while True:
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and \
            m.content.lower() in ["hd", "quit", "tai", "xiu", "chan", "le"]
        message = await bot.wait_for('message', check = check)
        base_url_taixiu = 'http://manhict.tech/game/v2/taixiu?method='
        api_key_taixiu = '&apikey=KeyTest'
        full_url_taixiu = base_url_taixiu + str(message.content.lower()) + api_key_taixiu
        get_taixiu = requests.get(full_url_taixiu)
        data_taixiu = get_taixiu.text
        parse_json = json.loads(data_taixiu)
        if (message.content.lower() == "hd"):
            await ctx.send('luật chơi tài xỉu như sau: \n có 3 cách chơi \n cách 1: cược tài/xỉu. Nếu cược xỉu Sẽ thắng cược khi tổng số điểm của 3 xúc xắc là từ 4 đến 10. Nếu cược tài Sẽ thắng cược khi tổng số điểm của 3 xúc xắc là từ 11 đến 17. \n cách 2: cược chẵn/lẻ. Nếu cược chẵn sẽ thắng cược khi tổng số điểm của 3 xúc xắc là 4,6,8,10,12,14,16. Nếu cược lẻ sẽ thắng cược khi tổng số điểm của 3 xúc xắc là 5,7,9,11,13,15,17. \nLưu ý: nếu muốn out game hãy gõ quit, tiền cược mặc định của game là 200$/lần (ko thể thay đổi tại t lười code phần đấy vl:>)')
        if (message.content.lower() == "tai"):
            bat1 = parse_json['mở bát']['one']
            bat2 = parse_json['mở bát']['two']
            bat3 = parse_json['mở bát']['three']
            tong = parse_json['người chơi']['chất']
            nha_cai = parse_json['nhà cái']
            nha_cai_ra = parse_json['mở bát']['total']
            chat = parse_json['người chơi']['chất']
            ketqua = parse_json['ketqua']['total']
            result_taixiu_tai = """nhà cái ra {nha_cai_ra} ({nha_cai}), bạn chọn {tong}. Bạn {ketqua}""".format(nha_cai = str(nha_cai), tong = str(tong), chat = str(chat), ketqua = str(ketqua), nha_cai_ra = str(nha_cai_ra))
            member_data = load_member_data(message.author.id)
            if ("lose" in result_taixiu_tai):
                    await ctx.send(result_taixiu_tai.replace("lose", "đã thua 200$"))
                    member_data.wallet -= 200
                    save_member_data(message.author.id, member_data)
                    print(result_taixiu_tai)
            elif ("win" in result_taixiu_tai):
                await ctx.send(result_taixiu_tai.replace("win", "đã thắng 200$"))
                member_data.wallet += 200
                save_member_data(message.author.id, member_data)
                print(result_taixiu_tai)
        elif (message.content.lower() == "xiu"):
            bat1 = parse_json['mở bát']['one']
            bat2 = parse_json['mở bát']['two']
            bat3 = parse_json['mở bát']['three']
            tong = parse_json['người chơi']['chất']
            nha_cai = parse_json['nhà cái']
            nha_cai_ra = parse_json['mở bát']['total']
            chat = parse_json['người chơi']['chất']
            ketqua = parse_json['ketqua']['total']
            result_taixiu_xiu = """nhà cái ra {nha_cai_ra} ({nha_cai}), bạn chọn {tong}. Bạn {ketqua}""".format(nha_cai = str(nha_cai), tong = str(tong), chat = str(chat), ketqua = str(ketqua), nha_cai_ra = str(nha_cai_ra))
            if ("lose" in result_taixiu_xiu):
                    await ctx.send(result_taixiu_xiu.replace("lose", "đã thua 200$"), file = discord.File('taixiu1.png'))
                    await ctx.send()
                    member_data.wallet -= 200
                    save_member_data(message.author.id, member_data)
                    print(result_taixiu_xiu)
            elif ("win" in result_taixiu_xiu):
                await ctx.send(result_taixiu_xiu.replace("win", "đã thắng 200$"))
                member_data.wallet += 200
                save_member_data(message.author.id, member_data)
                print(result_taixiu_xiu)
        elif (message.content.lower() == "chan"):
            bat1 = parse_json['mở bát']['one']
            bat2 = parse_json['mở bát']['two']
            bat3 = parse_json['mở bát']['three']
            tong = parse_json['người chơi']['chất']
            nha_cai = parse_json['nhà cái']
            chat = parse_json['mở bát']['total']
            ketqua = parse_json['ketqua']['total']
            result_taixiu_chan = """nhà cái ra {chat} ({nha_cai}) bạn cược {tong} . Bạn {ketqua}""".format(nha_cai = str(nha_cai), tong = str(tong), chat = str(chat), ketqua = str(ketqua))
            if ("lose" in result_taixiu_chan):
                    await ctx.send(result_taixiu_chan.replace("lose", "đã thua 200$"))
                    member_data.wallet -= 200
                    save_member_data(message.author.id, member_data)
                    print(result_taixiu_chan)
            elif ("win" in result_taixiu_chan):
                await ctx.send(result_taixiu_chan.replace("win", "đã thắng 200$"))
                member_data.wallet += 200
                save_member_data(message.author.id, member_data)
                print(result_taixiu_chan)
        elif (message.content.lower() == "le"):
            bat1 = parse_json['mở bát']['one']
            bat2 = parse_json['mở bát']['two']
            bat3 = parse_json['mở bát']['three']
            tong = parse_json['người chơi']['chất']
            nha_cai = parse_json['nhà cái']
            chat = parse_json['mở bát']['total']
            ketqua = parse_json['ketqua']['total']
            result_taixiu_le = """nhà cái ra {chat} ({nha_cai}) bạn cược {tong}. Bạn {ketqua}""".format(nha_cai = str(nha_cai), tong = str(tong), chat = str(chat), ketqua = str(ketqua))
            if ("lose" in result_taixiu_le):
                    await ctx.send(result_taixiu_le.replace("lose", "đã thua 200$"))
                    member_data.wallet -= 200
                    save_member_data(message.author.id, member_data)
                    print(result_taixiu_le)
            elif ("win" in result_taixiu_le):
                await ctx.send(result_taixiu_le.replace("win", "đã thắng 200$"))
                member_data.wallet += 200
                save_member_data(message.author.id, member_data)
                print(result_taixiu_le)
        elif (message.content.lower() == "quit"):
            await ctx.send("-----------------------------end game-----------------------------")
            break
        else:
            await ctx.send("cú pháp không hợp lệ, vui lòng gõ lại")
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
@commands.cooldown(1, 2400, commands.BucketType.user)
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
    url_vuatiengviet = 'http://manhict.tech/vuatiengviet/image?word='
    word_vuatiengviet = ["tôi yêu bạn", "cá koi", "cuốn sách", "tình yêu", "độc dược", "cô đọng", "huyền thoại", "sao băng", "quấn quýt", "bậc thầy", "ước vọng", "mơ mộng", "tình tứ", "mộng mơ", "nông nghiệp", "băng hà", "hiếu động", "sung sức", "công lao", "tâm tình", "cờ bạc"]
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
@bot.command()
async def mark(ctx):
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
    url_DHBC = ['https://manhict.tech/game/dhbcv3', 'https://goatbot.tk/api/duoihinhbatchu']
    random = random.choice(url_DHBC)
    get_DHBC = requests.get(random)
    data_DHBC = get_DHBC.text
    json_DHBC = json.loads(data_DHBC)
    if random == 'https://goatbot.tk/api/duoihinhbatchu':
        image_DHBC = json_DHBC['data']['image1and2'] 
        sokt = json_DHBC['data']['soluongkt']
        dapan = json_DHBC['data']['wordcomplete']
        get_image_DHBC = requests.get(image_DHBC)
        file = open("DHBC.png", "wb")
        file.write(get_image_DHBC.content)
        file.close()
        await ctx.send(f'====ĐUỔI HÌNH BẮT CHỮ====\nđây là câu hỏi của bạn\ngợi ý: từ này có {sokt} chữ', file = discord.File('DHBC.png'))
        if "g" in url_DHBC:
            def check(m):
                return m.author.id == ctx.author.id
            message = await bot.wait_for('message', check=check)
            if str(message.content.upper()) == dapan:
                await ctx.send(f'bạn đã trả lời đúng, đáp án là: {dapan}')
            else:
                await ctx.send(f'sai rồi, đáp án là {dapan}')
    else:
        image_DHBC = json_DHBC['image1and2'] 
        sokt = json_DHBC['soluongkt']
        dapan = json_DHBC['wordcomplete']
        get_image_DHBC = requests.get(image_DHBC)
        file = open("DHBC.png", "wb")
        file.write(get_image_DHBC.content)
        file.close()
        await ctx.send(f'====ĐUỔI HÌNH BẮT CHỮ====\nđây là câu hỏi của bạn\ngợi ý: từ này có {sokt} chữ', file = discord.File('DHBC.png'))
        if "m" in url_DHBC:
            def check(m):
                return m.author.id == ctx.author.id
            message = await bot.wait_for('message', check=check)
            if str(message.content.upper()) == dapan:
                await ctx.send(f'bạn đã trả lời đúng, đáp án là: {dapan}')
            else:
                await ctx.send(f'sai rồi, đáp án là {dapan}')
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
    sentence = ['Một cách để tận dụng tối đa cuộc sống là xem nó như một cuộc phiêu lưu – William Feather',' Mạnh dạn nói Tôi đã sai là cách ta chấp nhận đối mặt với tình huống khó khăn. Việc đó có phần mạo hiểm nhưng những gì ta nhận được sẽ vượt ngoài sự mong đợi’ - Rich DeVos', 'Tích cực, tự tin và kiên trì là chìa khóa trong cuộc sống. Vì vậy đừng bao giờ từ bỏ chính mình’ – Khalid', 'Yêu tôi hay ghét tôi, cả hai đều có lợi cho tôi. Nếu bạn yêu tôi, tôi sẽ luôn ở trong tim bạn và nếu bạn ghét tôi, tôi sẽ ở trong tâm trí bạn’ – Baland Quandeel', 'Thái độ quan trọng hơn quá khứ, hơn giáo dục, hơn tiền bạc, hơn hoàn cảnh, hơn những gì mọi người làm hoặc nói. Nó quan trọng hơn ngoại hình, năng khiếu hay kỹ năng’ – Charles Swindoll', 'Hãy tin vào chính mình! Có niềm tin vào khả năng của bạn! Nếu không có sự tự tin khiêm tốn nhưng hợp lý vào năng lực của chính mình, bạn không thể thành công hay hạnh phúc’ - Norman Vincent Peale', 'Trong đời người, có hai con đường bằng phẳng không trở ngại: Một là đi tới lý tưởng, một là đi tới cái chết’ - Lev Tolstoy', 'Bạn có thể thay đổi thế giới của mình bằng cách thay đổi lời nói của bạn ... Hãy nhớ rằng, cái chết và sự sống nằm trong sức mạnh của lưỡi’ - Joel Osteen', 'Lạc quan là niềm tin dẫn đến thành tích. Không có gì có thể được thực hiện mà không có hy vọng và sự tự tin’ - Helen Keller']
    result_sentence = random.choice(sentence)
    await ctx.send(result_sentence)
@bot.command()
async def thayboi(ctx):
    base_url_thayboi = 'http://manhict.tech/other/thayboi'
    get_thayboi = requests.get(base_url_thayboi)
    data_thayboi = get_thayboi.text 
    json_thayboi = json.loads(data_thayboi)
    result_thayboi = json_thayboi['data']
    await ctx.send(result_thayboi)
@bot.group(invoke_without_command=True)
async def truyentranh24(ctx):
    await ctx.send('tìm truyện trên truyentranh24.com\n/truyentranh24 search')
@truyentranh24.command()
async def search(ctx):
    await ctx.send('nhập tên truyện cần tìm')
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check)
    full_url_search = 'https://goatbot.tk/truyentranh24/search?q=' + str(message.content.lower()) + '&apikey=ntkhang'
    get_search = requests.get(full_url_search)
    json = get_search.json()
    name = json['data'][0]['name']
    img = json['data'][0]['thumbnail']
    get_img = requests.get(img)
    file = open("truyentranh24.png", "wb")
    file.write(get_img.content)
    file.close()
    href = json['data'][0]['href']  
    result = str(name) + '\n' + 'href: ' + str(href) + ' (dùng khi sử dụng lệnh đọc tryện)'
    await ctx.send(result, file = discord.File('truyentranh24.png'))
@bot.command()
async def shopmaihuong(ctx):
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
    await ctx.send('nhập theo mẫu sau:\n<id channel> | phản hồi user | phản hồi channel')
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check)
    value = message.content.lower().split(" | ")
    id_channel = str(value[0])
    reply_user = str(value[1])
    reply_channel = str(value[2])
    channel = await bot.fetch_channel(id_channel)
    user = await bot.fetch_user(f"{ctx.message.author.id}")
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
@bot.command()
async def news(ctx):
    url = 'https://manhict.tech/news/v1/vnexpress'
    get = requests.get(url)
    data = get.text
    data = json.loads(data)
    result = data['title']
    link = data['link']
    await ctx.send(f'Tin mới: {result}\nLink: {link}')
@bot.command()
async def test(ctx):
    await ctx.send('update...')
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
#code credit: Duc Anh 
