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
bot = commands.Bot(command_prefix='/') 
bot.remove_command("help")
data_filename = "data.pickle"
@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "help", description = "sử dụng /help để biết các lệnh có thể sử dụng trên bot")
    em.add_field(name = "info command", value = "xsmb, covid19, weather, youtube_search")
    em.add_field(name = "game command", value = "dovui, play_taixiu, keobuabao, vuatiengviet, dhbc(đuổi hình bắt chữ), noitu")
    em.add_field(name = "role play command", value = "balance, withdraw, deposit, shop_buy, shop_sell, work")
    em.add_field(name = "default command bot", value = "help, offbot, ping")
    em.add_field(name = "fun command", value = "thinh, mark, tiki, taoanhdep")

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
async def weather(ctx):
    await ctx.send('nhập tên thành phố')
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check)

                    # base_url variable to store url
    base_url = "http://manhict.tech/weather/vietnam?area="
                        # complete_url variable to store
                        # complete url address
    complete_url = base_url + str(message.content) + "&type=text"
    #get text
    response = requests.get(complete_url)
    data_weather = response.text
    json_weather = json.loads(data_weather)
    result_weather = json_weather['data']
    #get image
    url_image = complete_url + ".png" 
    response_image = requests.get(url_image)
    file = open("weather.png", "wb")
    file.write(response_image.content)
    file.close()
    await ctx.send(result_weather, file = discord.File('weather.png'))
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
        img1_taixiu = parse_json['images'][0]
        get_img1 = requests.get(img1_taixiu)
        file = open("taixiu1.png", "wb")
        file.write(get_img1.content)
        file.close()
        img2_taixiu = parse_json['images'][1]
        get_img2 = requests.get(img1_taixiu)
        file = open("taixiu2.png", "wb")
        file.write(get_img2.content)
        file.close()
        img3_taixiu = parse_json['images'][2]
        get_img3 = requests.get(img3_taixiu)
        file = open("taixiu3.png", "wb")
        file.write(get_img3.content)
        file.close()
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
@work.error
async def work_error(error, ctx):
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
    file = discord.File(r"C:\codde\discord_bot\image\bank.png", filename="bank.png") 
    embed.set_image(url="attachment://bank.png")
    await ctx.send(file=file, embed=embed)
@bank.command()
@commands.cooldown(3, 2400, commands.BucketType.user)
async def withdraw(ctx):
    member_data = load_member_data(message.author.id)
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check)
    if "withdraw" in message.content.lower():
        split = message.content.lower().split(" ")
        value = int(split[1])
        member_data.bank -= value
        member_data.wallet += value
        await ctx.send(f'đã rút thành công {value}$ vào ví')
        save_member_data(message.author.id, member_data)
    else:
        await ctx.send('sai cú pháp')
@withdraw.error
async def withdraw_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('ngân hàng hỏng ATM rồi:((, hãy quay lại sau {:.2f} giây'.format(error.retry_after))
@bank.command(name = "deposit")
@commands.cooldown(3, 2400, commands.BucketType.user)
async def deposit(ctx):
    await ctx.send('nhập số tiền bạn muốn gửi tiết kiệm vào ngân hàng')
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check)
    if "deposit" in message.content.lower():
        split = message.content.lower().split(" ")
        value = int(split[1])
        member_data = load_member_data(message.author.id)
        member_data.bank += value
        member_data.wallet -= value
        await ctx.send(f'đã gửi thành công {value}$ vào ngân hàng')
        save_member_data(message.author.id, member_data)
    else:
        await ctx.send('sai cú pháp')
@deposit.error
async def deposit_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('ngân hàng đóng cửa rồi, hãy quay lại sau {:.2f} giây'.format(error.retry_after))
@bot.command()
async def thinh(ctx):
    type_data = ["girl", "boy"]
    random_type = random.choice(type_data)
    full_url_thinh = 'http://manhict.tech/thathinh' + "?type" + random_type
    get_thinh = requests.get(full_url_thinh)
    data_thinh = get_thinh.text
    parse_json_thinh = json.loads(data_thinh)
    infomation = parse_json_thinh['result']['data']
    await ctx.send(infomation)
@bot.command()
async def keobuabao(ctx):
    await ctx.send('nhập kéo, búa, bao mức tiền cược mặc định là 50$/lần')
    while True:
        #get user input
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["kéo", "búa", "bao", "quit"]
        message = await bot.wait_for('message', check = check)
        #lấy api 
        url_keobuabao = 'http://manhict.tech/game/kbb?choose='
        full_url_keobuabao = url_keobuabao + message.content.lower()
        get_keobuabao = requests.get(full_url_keobuabao)
        data_keobuabao = get_keobuabao.text
        parse_json_keobuabao = json.loads(data_keobuabao)
        result_keobuabao = parse_json_keobuabao['data']
        if("thua" in result_keobuabao):
            member_data = load_member_data(message.author.id)
            await ctx.send(result_keobuabao.replace("thua", "thua 50$")) 
            member_data.wallet -= 50
            save_member_data(message.author.id, member_data)
        elif("thắng" in result_keobuabao):
            member_data = load_member_data(message.author.id)
            await ctx.send(result_keobuabao.replace("thắng", "thắng 50$"))
            member_data.wallet += 50
            save_member_data(message.author.id, member_data)
        elif("hòa" in result_keobuabao):
            member_data = load_member_data(message.author.id)
            await ctx.send(result_keobuabao)
            save_member_data(message.author.id, member_data)
        elif (message.content.lower() == "quit"):
            await ctx.send('end game!')
            break
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
    url_DHBC = 'http://manhict.tech/game/dhbcv3'
    get_DHBC = requests.get(url_DHBC)
    data_DHBC = get_DHBC.text
    json_DHBC = json.loads(data_DHBC)
    image_DHBC = json_DHBC['image1and2'] 
    sokt = json_DHBC['soluongkt']
    dapan = json_DHBC['wordcomplete']
    get_image_DHBC = requests.get(image_DHBC)
    file = open("DHBC.png", "wb")
    file.write(get_image_DHBC.content)
    file.close()
    await ctx.send(f'đây là câu hỏi của bạn\ngợi ý: từ này có {sokt} chữ', file = discord.File('DHBC.png'))
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
        url_noitu = 'http://manhict.tech/game/linkword?word='
        full_url_noitu = url_noitu + str(message.content)
        get_noitu = requests.get(full_url_noitu)
        data_noitu = get_noitu.text
        json_noitu = json.loads(data_noitu)
        word_noitu = json_noitu['text']
        if "thua" in word_noitu:
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
    url_taoanhdep = 'http://manhict.tech/taoanhdep/avatarwibu?id='
    value = message.content.lower().split(" | ")
    id_taoanhdep = str(value[0])
    chunen = str(value[1])
    chuky = str(value[2])
    complete_url_taoanhdep = url_taoanhdep + id_taoanhdep + "&chu_nen=" + chunen + "&chu_ky=" + chuky + "&apikey=KeyTest"
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
async def test(ctx):
    files = [{"filename": "taixiu1.png", "content": "taixiu1"}, {"filename": "taixiu2.png", "content": "taixiu2"}, {"filename": "taixiu3.png", "content": "taixiu3"}]
    await asyncio.wait([ctx.send(file=discord.File(f['filename']), content=f['content']) for f in files])
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
bot.run('')
#credit: Duc Anh
