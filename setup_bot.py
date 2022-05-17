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
bot = commands.Bot(command_prefix='/')
bot.remove_command("help")
data_filename = "data.pickle"
@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "help", description = "sử dụng /help để biết các lệnh có thể sử dụng trên bot và /help <lệnh> để biết cách sử dụng lệnh (một số default command bot lỗi ko help đc nhưng chắc chả cần help đâu:>)")
    em.add_field(name = "info command", value = "xsmb, covid19, weather, youtube_search")
    em.add_field(name = "game command", value = "dovui, play_taixiu")
    em.add_field(name = "role play command", value = "balance, bank, shop(shop_buy, shop_sell), work")
    em.add_field(name = "default command bot", value = "help, offbot, ping")

    await ctx.send(embed = em)
@help.command()
async def xsmb(ctx):
    em = discord.Embed(title = "xsmb", description = "xem thông tin kết quả xổ số miền bắc", color = ctx.author.color) 
    em.add_field(name = "cách dùng", value = "/xsmb")
    await ctx.send(embed = em)
@help.command()
async def covid19(ctx): 
    em = discord.Embed(name = "covid19", description = "xem thông tin về dịch bệnh covid19 tại Việt Nam", color = ctx.author.color)
    em.add_field(name = "cách dùng", value = "/covid19")
    await ctx.send(embed = em)
@help.command()
async def weather(ctx):
    em = discord.Embed(title = "weather", description = "xem thông tin về thời tiết tại một thành phố", color = ctx.author.color)
    em.add_field(name = "weather", value = "/weather *sau khi bot nhắn tin* nhập tên thành phố trong tiếng Anh và gửi")
    await ctx.send(embed = em)
@help.command()
async def youtube_search(ctx):
    em = discord.Embed(title = "youtube_search", description = "tìm kiesm video trên youtube qua từ khóa", color = ctx.author.color)
    em.add_field(name = "cách dùng", value = "/youtube_search *sau khi bot nhắn tin* nhập từ khóa cần tìm kiếm và gửi")
    await ctx.send(embed = em)
@help.command()
async def dovui(ctx):
    em = discord.Embed(title = "dovui", description = "game trả lời các câu hỏi đố vui", color = ctx.author.color)
    em.add_field(name = "cách dùng", value = "/dovui *sau khi bot gửi câu hỏi* nhập câu đáp án (lưu ý: không nhập đáp án chữ như: A, B, C, D)" )
    await ctx.send(embed = em)
@help.command()
async def play_taixiu(ctx):
    em = discord.Embed(title = "play_taixiu", description = "chơi tài xỉu với bot", color = ctx.author.color)
    em.add_field(name = "cách dùng", value = "/play_taixiu *sau khi bot gửi tin nhắn* nhập nếu không biết luật có thể nhập hd để biết. nếu muốn cược ngay hãy nhập một trong 2 cách sau \n1. nhập tai hoặc xiu và gửi bot sẽ gửi lại kết quả\n2. nhập chan hoặc le và gửi bot sẽ gửi lại kết quả (không hiểu rõ có thể nhập lệnh và nhập hd)")
    await ctx.send(embed = em)
@help.command()
async def balance(ctx):
    em = discord.Embedt(title = "balance", description = "xem số tiền bạn đang có trong ví và tài khoản ngân hàng", color = ctx.author.color)
    em.add_field(name = "cách dùng", value = "/balance")
    await ctx.send(embed = em)
@help.command()
async def shop(ctx):
    em = discord.Embed(title = "shop", description = "shop mua, bán các món đồ của bạn và đồ bạn cần", color = ctx.author.color)
    em.add_field(name = "cách dùng", value = "/shop_buy *sau khi bot gửi tin nhắn* nhập và gửi số thứ tự của món đồ bạn cần mua, /shop_sell nhập số thứ tự thứ bạn cần bán")
    await ctx.send(embed = em)
@help.command()
async def work(ctx):
    em = discord.Embed(title = "work", description = "có làm thì mới có ăn", color = ctx.author.color)
    em.add_field(name = "cách dùng", value = "/work *sau khi bot gửi tin có thể check lại tiền bằng lệnh balance*")
    await ctx.send(embed = em)
@help.command()
async def help(ctx):
    em = discord.Embed(title = "help", description = "cho bạn biết thông tin về các lệnh có tren bot", color = ctx.author.color)
    em.add_field(name = "cách dùng", value = "/help")
    await ctx.send(embed = em)
class Data:
    def __init__(self, wallet, bank, pc):
        self.wallet = wallet
        self.bank = bank
        self.pc = pc
#run bot
#client
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('bạn đã làm việc quá nhiều hãy nghỉ ngơi sau {:.2f} giây'.format(error.retry_after))
@bot.event
async def on_ready():
    print(f'[CLIENT] client completed')
#covid19
@bot.command()
async def covid19(ctx):
    full_url = 'https://manhict.tech/covid?country=viet%20nam'
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
    url = 'https://manhict.tech/xsmb'
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
    api_key = "f5e58e5107262dd200ef30cc9e47355a"

                    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

                        # complete_url variable to store
                        # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + str(message.content) + "&lang=vi"

                        # get method of requests module
                        # return response object
    response = requests.get(complete_url)

                        # json method of response object
                        # convert json format data into
                        # python format data
    x = response.json()

                        # Now x contains list of nested dictionaries
                        # Check the value of "cod" key is equal to
                        # "404", means city is found otherwise,
                        # city is not found
    if x["cod"] != "404":

                            # store the value of "main"
                            # key in variable y
        y = x["main"]

                            # store the value corresponding
                            # to the "temp" key of y
        current_temperature = y["temp"]
        unit = current_temperature - 273.15 
                            # store the value corresponding
                            # to the "pressure" key of y
        current_pressure = y["pressure"]

                            # store the value corresponding
                            # to the "humidity" key of y
        current_humidity = y["humidity"]

                            # store the value of "weather"
                            # key in variable z
        z = x["weather"]

                            # store the value corresponding
                            # to the "description" key at
                            # the 0th index of z
        weather_description = z[0]["description"]
                            # print following values
        result_weather = """thời tiết hiện thời của {city_name} \ncó nhiệt độ = {unit} \náp suất không khí = {current_pressure} \nđộ ẩm = {current_humidity} \n{weather_description}""".format(city_name = str(message.content), unit = unit, current_pressure = current_pressure, current_humidity = current_humidity, weather_description = weather_description) 
        await ctx.send(result_weather)
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
@bot.command()
async def ping(ctx):
    await ctx.send('pong!')
@bot.command()
async def play_taixiu(ctx):
    await ctx.send('đã bắt đầu game tài xỉu, nếu khoong biết luật bạn có thể nhập hd để biết rõ luật chơi')
    while True:
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and \
            m.content.lower() in ["hd", "start", "quit", "tai", "xiu", "chan", "le", "so"]
        message = await bot.wait_for('message', check = check)
        base_url_taixiu = 'https://manhict.tech/game/v2/taixiu?method='
        api_key_taixiu = '&apikey=KeyTest'
        full_url_taixiu = base_url_taixiu + str(message.content.lower()) + api_key_taixiu
        get_taixiu = requests.get(full_url_taixiu)
        data_taixiu = get_taixiu.text
        parse_json = json.loads(data_taixiu)
        if (message.content.lower() == "hd"):
            await ctx.send('luật chơi tài xỉu như sau: \n có 3 cách chơi \n cách 1: cược tài/xỉu. Nếu cược xỉu Sẽ thắng cược khi tổng số điểm của 3 xúc xắc là từ 4 đến 10. Nếu cược tài Sẽ thắng cược khi tổng số điểm của 3 xúc xắc là từ 11 đến 17. \n cách 2: cược chẵn/lẻ. Nếu cược chẵn sẽ thắng cược khi tổng số điểm của 3 xúc xắc là 4,6,8,10,12,14,16. Nếu cược lẻ sẽ thắng cược khi tổng số điểm của 3 xúc xắc là 5,7,9,11,13,15,17. \nnếu muốn out game hãy gõ quit')
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
            await ctx.send(result_taixiu_tai)
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
            await ctx.send(result_taixiu_xiu)
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
            await ctx.send(result_taixiu_chan)
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
            await ctx.send(result_taixiu_le)
            print(result_taixiu_le)
        elif (message.content.lower() == "quit"):
            await ctx.send("-----------------------------end game-----------------------------")
            break
        else:
            await ctx.send("cú pháp không hợp lệ, vui lòng gõ lại")
@bot.command()
async def dovui(ctx):
    url_dovui = 'https://manhict.tech/game/dovuiv1'
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
@bot.command()
@commands.cooldown(1, 2400, commands.BucketType.user)
async def work(ctx):
    await ctx.send('đây là các cộng việc bạn có thể làm\n1. lấp trình viên')
    def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["1"]
    message = await bot.wait_for('message', check = check)
    if(message.content.lower() == "1"):
        member_data = load_member_data(message.author.id)
        if(member_data.pc == 1):
            earning = random.randrange(375)
            member_data.bank += earning
            await ctx.send(f"bạn đã làm lập trình viên và kiếm được {earning} tiền!")
            save_member_data(message.author.id, member_data)
        else:
            await ctx.send('bạn chưa có máy tính để làm lập trình viên')

@bot.command()
async def balance(message):
    member_data = load_member_data(message.author.id)

    embed = discord.Embed(title=f"số tiền của {message.author.display_name}")
    embed.add_field(name="tiền mặt", value=str(member_data.wallet))
    embed.add_field(name="trong thẻ ngân hàng", value=str(member_data.bank))

    await message.channel.send(embed=embed)
@bot.command()
async def shop_sell(ctx):
    await ctx.send('đồ có thể bán\n1. pc: 80 tiền')
    def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["1"]
    message = await bot.wait_for('message', check = check)
    if(message.content.lower() == "1"):
        member_data = load_member_data(message.author.id)
        if member_data.pc == 1:
            member_data.bank += 80
            member_data.pc = 0
            await ctx.send('giao dịch thành công')
            save_member_data(message.author.id, member_data)
        else:
            await ctx.send('bạn bạn không có máy tính để bán')
    else:
        await ctx.send('đồ bạn muốn bán không hợp lệ')
        save_member_data(message.author.id, member_data)
@bot.command()
async def shop_buy(ctx):
    await ctx.send('đồ có thể mua\n1. pc: 150 tiền')
    def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["1"]
    message = await bot.wait_for('message', check = check)
    if(message.content.lower() == "1"):
        member_data = load_member_data(message.author.id)
        if member_data.pc == 1:
            await ctx.send('bạn đã có pc rồi, mua làm gì nữa')
        else:
            if member_data.bank >= 150:
                member_data.bank -= 150
                member_data.pc = 1
                await ctx.send('giao dịch thành công')
                save_member_data(message.author.id, member_data)
            else:
                await ctx.send('bạn quá nghèo để mua được máy tính')
    else:
        await ctx.send('sai cú pháp, món đồ bạn cần mua không tồn tại')
@bot.command()
@commands.cooldown(3, 1800, commands.BucketType.user)
async def bank(ctx):
    def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["1", "2", "3"]
    message = await bot.wait_for('message', check = check)
    await ctx.send('chọn điều bạn muôn làm ở ngân hàng \n1. rút tiền(300$/lần)\n2. gửi tiền(300$/lần)')
    if(message.content.lower() == "1"):
        member_data = load_member_data(message.author.id)
        member_data.bank -= 300
        member_data.wallet += 300
        save_member_data(message.author.id, member_data)
    if(message.content.lower() == "2"):
        member_data = load_member_data(message.author.id)
        member_data.bank += 300
        member_data.wallet -= 300
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
bot.run('OTcxNzU1MTg5MDMzOTI2Njc2.GGWvn9.jFez5hT5rC4rQVlD7BbfRm8b-aGw0QRiXM7ipU')
