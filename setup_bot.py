import discord
from discord.ext import commands
import json 
import requests
from youtube_search import YoutubeSearch
bot = commands.Bot(command_prefix='/')
#run bot
#cllient
@bot.event
async def on_ready():
    print(f'client completed')
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
    search = YoutubeSearch('{message.content}', max_results=5).to_json()
    search_dict = json.loads(search)
    for v in search_dict['videos']:
        result = 'https://www.youtube.com/watch?v=' + v['id'] + " - " + v['title'] + " của kênh " + v['channel']
        await ctx.send('đây là các kết quả tìm kiếm {result}'.format(result = result))
@bot.command()
@commands.is_owner()
async def offbot(ctx):
    if (ctx.author.id == 716146182849560598):
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
            await ctx.send('luật chơi tài xỉu như sau: \n có 3 cách chơi \n cách 1: cược tài/xỉu. Nếu cược xỉu Sẽ thắng cược khi tổng số điểm của 3 xúc xắc là từ 4 đến 10. Nếu cược tài Sẽ thắng cược khi tổng số điểm của 3 xúc xắc là từ 11 đến 17. \n cách 2: cược chẵn/lẻ. Nếu cược chẵn sẽ thắng cược khi tổng số điểm của 3 xúc xắc là 4,6,8,10,12,14,16. Nếu cược lẻ sẽ thắng cược khi tổng số điểm của 3 xúc xắc là 5,7,9,11,13,15,17. \n cách 3: cược số. Thắng cược khi kết quả của 1 trong 3 xúc xắc hiển thị đúng con số mà người chơi đã chọn. cách 1 có 1 trường hợp đặc biệt đó là bộ ba bất kì nhưng do mình sẽ không làm kiểu chơi này vậy nên chúng ta vẫn sẽ chơi như thường\nnếu muốn out game hãy gõ quit')
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
        elif (message.content.lower() == "so"):
            await ctx.send('nhập số bạn muốn đặt cược (nếu không hiểu có thể gõ lệnh hd để biết luật chơi)')
            base_url_so = 'https://manhict.tech/game/v2/taixiu?method=so&'
            api_key_so = '&apikey=KeyTest'
            full_url_so = base_url_so + "value=" + message.content + api_key_so
            get_so = requests.get(full_url_so)
            data_so = get_so.text
            parse_json_so = json.loads(data_so)
            you = parse_json_so['người chơi']['total']
            ketqua2 = parse_json_so['ketqua']['total']
            ketqua_so = parse_json_so['mở bát']['bộ']
            result_taixiu_so = """bạn chọn {you}, kết quả là {ketqua_so}. bạn {ketqua2}""".format(ketqua2 = str(ketqua2), ketqua_so = str(ketqua_so), you = str(you))
            await ctx.send(result_taixiu_so)
            print(result_taixiu_so)
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
bot.run('OTcxNzU1MTg5MDMzOTI2Njc2.Gpyr4V.Ij1Zsgl-HlWUF618BvGTz0P2qaPZohGC_Up4zY')
