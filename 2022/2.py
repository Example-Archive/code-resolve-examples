from discord.ext.commands import Bot

bot = Bot(...)

...

class Button(discord.ui.View):

    @discord.ui.button(label="참가", style=discord.ButtonStyle.primary)
    async def button_in(self, button: discord.ui.Button, interaction: discord.Interaction):
        interaction.message.id
    
    @discord.ui.button(label="취소", style=discord.ButtonStyle.red)
    async def button_out(self, button: discord.ui.Button, interaction: discord.Interaction):
        interaction.message.id

@bot.slash_command(description="test")
async def mojip(
    ctx,
    time: Option(str, "ttt.", required=False) = '',
    etc: Option(str, "eee", required=False) = '',
):
    embed = discord.Embed(title=f"{time} testembed", description=etc)

    view = Button()
    message = await ctx.respond(embed=embed, view=view)
    await view.wait()
