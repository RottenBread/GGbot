import discord
from module import *
import re
from enum import Enum
from discord import app_commands,Interaction,ui,ButtonStyle,SelectOption

GUILD_ID=your-guild-id

class MyClient(discord.Client):
    async def on_ready(self):
        await self.wait_until_ready()
        await tree.sync(guild= discord.Object(id=GUILD_ID))
intents= discord.Intents.all()
client = MyClient(intents=intents)
tree = app_commands.CommandTree(client)

class rankType(Enum):
    솔로랭크 = 1
    자유랭크 = 2

@tree.command(guild= discord.Object(id=GUILD_ID),name="전적", description="Riot ID인 경우에는 태그까지 작성해 주세요.")
async def mk전적(interaction:Interaction, 랭크유형:rankType, 이름:str):
    print(이름)
    try:
        if 랭크유형.value == 1:
            embed = discord.Embed(title="데이터를 불러오기까지 많은 시간이 걸릴 수 있습니다.", color=discord.Color.random())
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(color=discord.Color.random())
            embed.set_author(name=f'{이름} | 솔로랭크', url="https://www.op.gg/summoners/kr/{}".format(이름.replace('#', '-').replace(' ', '%20')), icon_url="https://cdn.discordapp.com/attachments/579272051282542595/1182186534947000360/Q2yS7PKGww04abPtNFHLS8npW_L0evvVmQkxqB0iRWA934Ecsea8rZPVZwh0eKJhj_quAfgLTCusaHCa4XVU2w.webp?ex=6583c801&is=65715301&hm=c9e3561ee36391700505fae2fe025896c4e9310999ee4e4c150e97040e629638&")
            embed.add_field(name='', value=f'티어 : {getGG_solotier(이름).get_text().title()} ({getGG_sololp(이름).get_text()})', inline=False)
            embed.add_field(name='', value=f'승/패 : {getGG_solowl(이름).get_text()}', inline=False)
            embed.add_field(name='', value=f'최근 게임 : {getFOW_recent_win(이름).get_text()} | {remove_after_char(getFOW_recent(이름).get_text(), "랭크")} | {getFOW_recent_avg(이름).get_text()}', inline=False)

            block_id=["green","white"]
            guild = client.get_guild(GUILD_ID)
            block=[discord.utils.get(guild.emojis,name=i) for i in block_id]
            wr = re.sub(r'[^0-9]', '', getGG_solowr(이름).get_text())
            wr = wr.strip()
            if round(int(wr)/10) == 0:
                embed.add_field(name ='', value=f"{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 1:
                embed.add_field(name ='', value=f"{block[0]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 2:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 3:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 4:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 5:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 6:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 7:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 8:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 9:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 10:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}  (WR {wr}%)", inline=False)
            embed.set_footer(text='닉네임을 클릭하면 OP.GG로 이동합니다.')
            await interaction.followup.send(embed=embed)
        elif 랭크유형.value == 2:
            embed = discord.Embed(title="데이터를 불러오기까지 많은 시간이 걸릴 수 있습니다.", color=discord.Color.random())
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(color=discord.Color.random())
            embed.set_author(name=f'{이름} | 자유랭크', url="https://www.op.gg/summoners/kr/{}".format(이름.replace('#', '-')), icon_url="https://cdn.discordapp.com/attachments/579272051282542595/1182186534947000360/Q2yS7PKGww04abPtNFHLS8npW_L0evvVmQkxqB0iRWA934Ecsea8rZPVZwh0eKJhj_quAfgLTCusaHCa4XVU2w.webp?ex=6583c801&is=65715301&hm=c9e3561ee36391700505fae2fe025896c4e9310999ee4e4c150e97040e629638&")
            embed.add_field(name='', value=f'티어 : {getGG_flextier(이름).get_text().title()} ({getGG_flexlp(이름).get_text()})', inline=False)
            embed.add_field(name='', value=f'승/패 : {getGG_flexwl(이름).get_text()}', inline=False)
            embed.add_field(name='', value=f'최근 게임 : {getFOW_recent_win(이름).get_text()} | {remove_after_char(getFOW_recent(이름).get_text(), "랭크")} | {getFOW_recent_avg(이름).get_text()}', inline=False)

            block_id=["green","white"]
            guild = client.get_guild(GUILD_ID)
            block=[discord.utils.get(guild.emojis,name=i) for i in block_id]
            wr = re.sub(r'[^0-9]', '', getGG_flexwr(이름).get_text())
            wr = wr.strip()
            if round(int(wr)/10) == 0:
                embed.add_field(name ='', value=f"{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 1:
                embed.add_field(name ='', value=f"{block[0]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 2:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 3:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 4:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 5:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[1]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 6:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[1]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 7:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[1]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 8:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[1]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 9:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[1]}  (WR {wr}%)", inline=False)
            elif round(int(wr)/10) == 10:
                embed.add_field(name ='', value=f"{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}{block[0]}  (WR {wr}%)", inline=False)
            embed.set_footer(text='닉네임을 클릭하면 OP.GG로 이동합니다.')
            await interaction.followup.send(embed=embed)
    except:
        embed = discord.Embed(title="올바르지 않은 이름입니다.", color=discord.Color.red())


client.run('your-own-key')
