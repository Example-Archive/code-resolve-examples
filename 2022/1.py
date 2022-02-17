from discord.ext.commands import Bot

bot = Bot(...)

...

class Button(discord.ui.View):

    def __init__(self, message_id: int) -> None:
        super(Button, self).__init__()
        self.message_id: int = message_id

    @discord.ui.button(label="참가", style=discord.ButtonStyle.primary)
    async def button_in(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message_id
    
    @discord.ui.button(label="취소", style=discord.ButtonStyle.red)
    async def button_out(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.message_id

@bot.slash_command(description="test")
async def mojip(
    ctx,
    time: Option(str, "ttt.", required=False, default = ' '),
    etc: Option(str, "eee", required=False, default = ' '),
):
    embed = discord.Embed(title=f"{time} testembed", description=etc)

    message = await ctx.respond(embed=embed)
    
    view = Button(message_id=message.id)
    await message.edit(view=view)
