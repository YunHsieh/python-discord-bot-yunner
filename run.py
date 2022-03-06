#導入 Discord.py
import discord
import environments
import re
#client 是我們與 Discord 連結的橋樑

my_guild_id = 682654394772226087

class YunnerClient(discord.Client):

    def get_guild(self, id):
        for guild in self.guilds:
            if guild.id == id:
                return guild
        return None

    def get_category_newest(self, guild, name):
        newest = None
        for channel in guild.channels:
            if channel.name == name:
                if not newest or newest.created_at < channel.created_at:
                    newest = channel
        return newest

    def get_channel_newest(self, guild, name):
        newest = None
        for channel in guild.channels:
            if channel.name == name:
                if not newest or newest.created_at < channel.created_at:
                    newest = channel
        return newest

    #當機器人完成啟動時
    async def on_ready(self):
        print('目前登入身份：', self.user)
        # category_name = '測試私密頻道'
        # voice_channel_name = '測試語音頻道'
        # guild = self.get_guild(my_guild_id)
        # category_obj = await guild.create_category_channel(category_name)
        # channel_obj = await category_obj.create_voice_channel(voice_channel_name)
        # invite_obj = await channel_obj.create_invite()
        # print(">>>", invite_obj)
        # # channel_obj = self.get_channel_newest(guild, voice_channel_name)

        # my_user = None
        # for member in guild.members:
        #     if member.name == 'Yun':
        #         my_user = member
        # # await channel_obj.invite([my_user])
       
        # for guild in self.guilds:
        #     print(guild, guild.id)
        #     for channel in guild.channels:
        #         print(channel, channel.id)


    async def on_member_join(self, member):
        await member.send('welcome to ...')
    
    async def on_voice_state_update(self, member, before, after):
        return

    #當有訊息時
    async def on_message(self, message):
        print(message, '\n')
        if not message.channel.id==865628070869598210:
            return
        #排除自己的訊息，避免陷入無限循環
        if message.author == self.user:
            return
        #如果包含 ping，機器人回傳 pong
        # if message.content == '妳媽':
        #     await message.channel.send('自助餐')
        if message.content in ['help', '/']:
            await message.channel.send('我們的指令有...')
        
        # await message.author.send('hihi')
        if re.match(r'.*hi.*', message.content):
            await message.reply('回覆您的訊息')
            await message.channel.send('哈囉')

    async def on_message_edit(self, before, after):
        if before.content == 'test':
            await before.reply('原始訊息: ' + before.content)

client = YunnerClient()

# print([i for i in client.get_all_channels()])
client.run(environments.DISCORD_TOKEN)
