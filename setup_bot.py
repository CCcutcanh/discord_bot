import discord
from discord.ext import commands
import json 
import requests
bot = commands.Bot(command_prefix='/')
#covid19
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
#run bot
#covid19
@bot.command()
async def covid19(ctx):
    await ctx.send(result)
#xsmb
@bot.command()
async def xsmb(ctx):
    #xsmb
    url = 'https://manhict.tech/xsmb'
    get_data = requests.get(url)
    x = get_data.json()
    data_xsmb = x['data']
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
        print(result_weather)
        print(complete_url)
        await ctx.send(result_weather)

bot.run('OTcxNzU1MTg5MDMzOTI2Njc2.Gpyr4V.Ij1Zsgl-HlWUF618BvGTz0P2qaPZohGC_Up4zY')