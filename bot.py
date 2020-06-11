import discord
from discord.ext import commands

from country import Country

jeton = "NzE3NjY5MjYyOTY5NTM2NTY0.XtdsNg.jXktbFLO8yN5VTx8YPRoPgyK8bw"

client = commands.Bot(command_prefix=".")
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='.help'))
    print("Bot is ready")


@client.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour=discord.Colour.red()
    )
    embed.set_author(name="Help")
    embed.add_field(name="cov", value="Returns Covid-19 Statistics for entered Country", inline=False)
    embed.add_field(name="clear",
                    value="Clears all messages If they are not more than 100 and older than 14 days.",
                    inline=False)

    await ctx.send(author, embed=embed)


@client.command()
async def cov(ctx, input):
    input = input.strip()
    print(input)
    try:
        country = Country(input)
        embed = discord.Embed(
            title=country.CountryName,
            description=f"Covid-19 Statistics of {country.CountryName}",
            colour=discord.Colour.blue()
        )
        embed.set_thumbnail(url=country.flag_url)
        embed.set_author(name="Covid-19 Bot",
                         icon_url="https://cdn2.iconfinder.com/data/icons/covid-19-1/64/01-Virus-512.png")
        embed.add_field(name="Total Case", value=country.TotalConfirmed, inline=True)
        embed.add_field(name="Total Recovered", value=country.TotalRecovered, inline=True)
        embed.add_field(name="Total Deaths", value=country.TotalDeaths, inline=True)

        embed.add_field(name="Case Today", value=country.NewConfirmed, inline=True)
        embed.add_field(name="Recovered Today", value=country.NewRecovered, inline=True)
        embed.add_field(name="Deaths Today", value=country.NewDeaths, inline=True)

        await ctx.send(embed=embed)
    except:
        await ctx.send("Please enter a valid country name")


@client.command()
async def clear(ctx, amount=100):
    try:
        channel = ctx.message.channel
        deleted = await channel.purge(limit=amount)
        await channel.send(f"{len(deleted)} message(s) have/has been succesfully removed from the channel")
    except:
        await channel.send(f"Too much arguments to delete or messages are older than 14 days.")


client.run(jeton)
