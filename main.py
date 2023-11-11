# This example requires the 'message_content' intent.
import discord
import requests
#code to fetch data from openweather API for Bryn Mawr using json requests
intents = discord.Intents.default()
intents.message_content = True
api_key = "eb903014378c9ef7ff99b45598749130"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
client = discord.Client(intents=intents)

#string for the bus schedule plz don't delete!
bmcMWF = "7:35a \n 8:15a \n 8:45a \n 9:10a \n 9:30a \n 10:05a \n 10:15a \n 10:35a \n 10:55a \n 11:05a \n 11:35a \n 12:10p \n 12:30p \n 1:10p \n 1:30p \n 2:00p \n 2:05p \n 2:45p \n 3:10p \n 4:00p \n 4:05p \n 4:20p \n 5:10p \n 5:50p \n 6:20p \n 7:15p \n 8:00p \n 8:35p \n 9:05p \n 9:35p \n 10:15p \n 10:55p \n 11:45p \n 12:30a"
hcMWF = "7:50a \n 8:50a \n 9:15a \n 9:40a \n 9:45a \n 10:20a \n 10:30a \n 10:50a \n 11:15a \n 11:30a \n 11:50a \n 12:40p \n 12:55p & 1:00p \n 1:45p \n 1:50p \n 2:20p \n 2:45p \n 3:20p \n 3:50p \n 4:10p \n 4:20p \n 4:35p \n 5:25p \n 6:05p \n 6:50p \n 7:30p \n 8:15p \n 8:50p \n 9:20p \n 10:05p \n 10:30p \n 11:10p \n 12:00a \n 12:45a"
bmcTTh = "7:20a \n 7:55a \n 8:15a \n 8:50a \n 9:10a \n 930a & 9:40a \n 9:50a \n 10:35a \n 10:55a \n 11:20a \n 11:25a \n 12:20p \n 12:40p \n 12:50p \n 1:10p \n 1:55p \n 2:10p \n 2:20p \n 3:10p \n 3:40p \n 4:05p \n 4:20p \n 5:10p \n 5:45p \n 6:20p \n 7:10p \n 8:00p \n 8:35p \n 9:05p \n 9:35p \n 10:15p \n 10:55p \n 11:45p \n 12:30a"
hcTTh = "7:40a \n 8:10a \n 8:35a \n 9:15a \n 9:30a & 9:40a \n 10:10a \n 10:20a \n 11:05a \n 11:10a \n 11:35a & 11:40a \n 12:10p \n 12:35p \n 1:00p \n 1:20p \n 1:45p \n 2:10p \n 2:40p \n 3:10p \n 3:50p \n 4:05p \n 4:20p \n 4:45p \n 5:30p \n 6:05p \n 6:50p \n 7:30p \n 8:15p \n 8:50p \n 9:20p \n 10:05p \n 10:30p \n 11:10p \n 12:00a \n 12:45a"

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    #saying hello
    if message.content.startswith('/hello'): 
      await message.channel.send("Hello " + message.author.name)
    
    #about function
    #give all the functions the bot can do
    if message.content.startswith('/about'):
      embed = discord.Embed(title="About", description="Hello! I am a bot providing Bryn Mawr College resources. I am a bot that can do a lot! \n\n/about: providing general information about the chatbot. \n/libraryName: provide general information about the libraries on campus \n/campus safety: provide the Campus Safety phone number. \n/health: provide the Health Center phone number.\n/weather: provide the weather today for the campus. \n/menu: provide the menu of Erdman and New Dorm. You can specify if you want the menu of the day after. \n/dean: provide the name of deans and their calendly. \n/bus day: provide the bus schedule for the campus. You can specify the day of the week. \n/courses/major/semester: provide the courses of a specific major being offered in that semester. \n/schedule semester: showing the schedule of the fall semester.\n\nHave fun with Bryn Mawr Bot!.")
      embed.set_thumbnail(url="https://i.imgur.com/Bfa7XyO.png")
      await message.channel.send(embed=embed)
    if message.content.startswith('/weather'):
      city_name = "Bryn Mawr"
      complete_url = base_url + "appid=" + api_key + "&q=" + city_name
      response = requests.get(complete_url) #get data from the website
      x = response.json() #generate json
    #get necessary values from the json
      y = x["main"]
      current_temperature = y["temp"]
      current_temperature_celsiuis = str(round(current_temperature - 273.15))
      current_pressure = y["pressure"]
      current_humidity = y["humidity"]
      z = x["weather"]
      weather_description = z[0]["description"]
      weather_description = z[0]["description"]
      embed = discord.Embed(title=f"Weather in {city_name}",
                        color=message.channel.guild.me.top_role.color,
                        timestamp=message.created_at,)
      embed.set_thumbnail(url="https://i.imgur.com/mefYEVt.png")
      embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
      embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
      embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)

      embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
      embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
      embed.set_footer(text=f"Requested by {message.author.name}")
      await message.channel.send(embed=embed)
    #schedule function
    #give the important dates of fall semester at Bryn Mawr 
    if message.content.startswith('/schedule'):
      if 'fall' in message.content[8:]:
        embed = discord.Embed(title="Fall Schedule Bryn Mawr College:",
        color=message.channel.guild.me.top_role.color,
        timestamp=message.created_at,description="JULY 1:    Fall tuition bills posted.\nAUG. 1: Fall tuition bill payment due.\nAUG. 29: International Students move in | Classes begin at the University of Pennsylvania.\nAUG. 30: All other New students move in \nAUG. 31: Registration opens (9 a.m.).\nSEPT. 1: Dorms open for returning students (9 a.m.).\nSEPT. 4: Labor Day: No classes at Bryn Mawr,  Haverford or Swarthmore.\nSEPT. 5: Classes begin at Bryn Mawr and Haverford (Including THRIVE). PE registration opens\nSEPT. 11: PE classes begin.\nSEPT. 13: End of Add/Drop period (11:59 p.m.)\nSEPT. 22: Last day to drop a fifth course at Bryn Mawr and Haverford. Last day to declare Cr/NC for first  quarter courses (5 p.m.).\nOCT. 13: Last day to declare Cr/NC for full semester courses (5 p.m.). Fall break begins after last class.\nOCT. 23: Classes resume (8 a.m.).\nOCT. 27: First quarter (including PE) courses end.\nOCT. 27-28: Family and Friends Weekend.\nOCT. 30: Second quarter (including PE) courses begin.\nNOV. 5:    Last day to add a second quarter course.\nNOV. 12: Last day to drop a second quarter course.\nNOV. 13-17: Pre-Registration for Spring 2024.\nNOV. 17: Last day to declare Cr/NC for second quarter courses (5 p.m.).\nNOV. 22: Thanksgiving break begins after last class.\nNOV. 27: Classes resume (8 a.m.).\nDEC. 1:    Spring tuition bill posted.\nDEC. 11: Last day of classes at the University of Pennsylvania (Exams: Dec. 14-21).\nDEC. 13: Last day of classes at Swarthmore (Exams: Dec. 13-21).\nDEC. 14: Last day of classes at Bryn Mawr: all written  work due 5 p.m.\nDEC. 15: Last day of classes/optional review day at Haverford.\nDEC. 15-16: Review Period.\nDEC. 17-22: Examination Period (ends at 12:30 p.m. on Dec. 22).\nDEC. 22: Winter Break begins (dorms close at 6 p.m.).")
        embed.set_thumbnail(url="https://i.imgur.com/FTiTlM7.png")
        await message.channel.send(embed=embed)
      #give the important dates of spring semester at Bryn Mawr 
      if 'spring' in message.content[8:]:
        embed = discord.Embed(title="Spring Schedule Bryn Mawr College:",
        color=message.channel.guild.me.top_role.color,
        timestamp=message.created_at,description="JAN. 2: Spring tuition bill payment due.\nJAN. 3: Faculty Grade Deadline for Fall 2023 grades due at noon.\nJAN. 15: Martin Luther King Day. \nJAN. 18: Classes begin at Penn.\nJAN. 19: Dorms reopen at noon.\nJAN. 22: Classes begin at Bryn Mawr, Haverford, and Swarthmore.\nJAN. 22-31:  Registration (all class years).\nFEB. 9:Last day to drop a fifth course at Bryn Mawr and Haverford. Last day to declare Cr/NC for first quarter courses (5 p.m.).\nMAR. 1: Last day to declare Cr/NC for full semester courses (5 p.m.).\nMAR. 8: Spring break begins after last class. First quarter (including PE) courses end.\nMAR. 18: Classes resume (8 a.m.). Second quarter (including PE) courses begin.\nMAR. 22: Last day to add a second quarter course.\nMAR. 29: Last day to drop a second quarter course.\nAPR. 5: Last day to declare Cr/NC for second quarter courses (5 p.m.).\nMAY 1: Last day of classes at the University of Pennsylvania (Exams May 6-14).\nMAY 3: Last day of classes at Bryn Mawr, Haverford, and Swarthmore. All written work due 5 p.m.\nMAY 4-5: Review period.\nMAY 6-11: Examination Period for seniors (ends at 5 p.m. on May 11).\nMAY 6-17: Examination Period (ends at 12:30 p.m. on May 17).\nMAY 13: Senior grade deadline 12 noon.\nMAY 18:Commencement.\nMAY 19: Dorms close at 12 noon.\n MAY 24: All other grades due 12 noon.")
        embed.set_thumbnail(url="https://i.imgur.com/FTiTlM7.png")
        await message.channel.send(embed=embed)
      
    

    #menu function
    #give the menu of the campus today and tomorrow
    if message.content.startswith('/menu'):
      #if the user wants today menu
      if 'today' in message.content[5:]:
        embed = discord.Embed(title="Menus for Saturday, November 11th",
        color=message.channel.guild.me.top_role.color,
        timestamp=message.created_at,)
        embed.set_thumbnail(url="https://i.imgur.com/BYsDWYK.png")
        embed.add_field(name="New Dorm Lunch", value="Greek Chicken Cutlet \n Spinach with Pine Nuts & Raisins \n Spicy Mango Tofu V \n Sweet Stewed Kidney Beans V \n Sauteed Baby Bok Choy  V \n Onion & Smoked Gouda Pizza* \n Pepperoni Pizza \n Cheese Pizza* \n Bruschetta Pizza \n Chicken Escarole Soup \n Chocolate Mousse Brownies* \n Sugar Cookies V", inline=True)
        embed.add_field(name="Erdman Brunch", value="Oatmeal V \n Pancakes* \n Hard Cooked Eggs  PWW* \n Fiesta Scrambled Eggs  PWW* \n Chocolate Chip Loaf* \n Tuscan Lemon Muffins V \n Buttermilk Biscuits* \n Hash Brown Patties \n Turkey Bacon PWW \n Omelet & Yogurt Bar \n Assorted Bagels* \n Doughnuts* \n Breakfast Sausage V PWW \n Pork Sausage Links  PWW \n Everything Bagel Tofu V \n Crepe Bar", inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=False)
        embed.add_field(name="New Dorm Dinner", value="Wanjan-Jeon Pork & Tofu Patty \n Sauteed Bean Sprouts with Sesame V \n Mango Habanero Meatball V \n Steamed Leaf Spinach \n Turkey Rice Soup \n Sausage Pizza \n Pepperoni Pizza \n Cheese Pizza* \n Fresh Dough Bread Knots* \n Chocolate Chip Pecan Cake * \n Apple Pie V", inline=True)
        
        embed.add_field(name="Erdman Dinner", value="South Philly Italian \n Roast Pork Sandwich \n Breaded Chicken \n Cutlet Sandwich \n Sauteed Broccoli Rabe V PWW \n Roasted Red \n Peppers V PWW \n Fried Long Hot Peppers V PWW \n Provolone Cheese * PWW \n Roasted Potato,  Artichokes, Mushrooms & Olives V PWW \n Tomato Caprese \n Sheet Pan Pasta* \n Roasted Italian Vegetables V \n Marinara V PWW \n Pesto Sauce* \n Farfalle V \n Garlic Breadsticks* \n Italian Lemon Cream Cake*", inline=True)
        embed.set_footer(text="*= VEGETARIAN      V = VEGAN     PWW = PREPARED without WHEAT \n Menu items identified with this mark are prepared in a common kitchen to be Prepared without Wheat, Vegan, or Vegetarian.")

        await message.channel.send(embed=embed)
      #if the user want the tomorrow menu
      if "tomorrow" in message.content[5:]:
        embed=discord.Embed(title="Tomorrow's Menu", description="Menus for Sunday, November 12th",
        color=message.channel.guild.me.top_role.color,
        timestamp=message.created_at)
        embed.set_thumbnail(url="https://i.imgur.com/BYsDWYK.png")
        embed.add_field(name="New Dorm Brunch", value="Blueberry Muffin V \n Hickory Smoked Bacon \n Chicken Sausage Patty \n Beyond Sausage Patty V \n Scrambled Eggs* \n French Toast* \n Hard Cooked Eggs \n Diced Potatoes* \n Gluten-free Waffles V \n Monkey Muffins \n Selection of Scones \n Selection of Artisan \n French Danish \n Selection of Donuts \n Assorted Bagels \n Cantaloupe Melon \n Honeydew Melon \n Fresh Orange Slices \n New England Clam Chowder \n BBQ Seitan V \n Seasoned Broccoli", inline=True)
        embed.add_field(name="Erdman Brunch", value="Oatmeal V \n French Toast* \n Hard Cooked  Eggs  PWW* \n Scrambled Eggs with Kale, & Mozzarella PWW* \n Chocolate Chip Muffins* \n Maple Granola Muffins V \n Buttermilk Biscuits* \n Shredded Potatoes PWW V \n Hickory Smoked Bacon PWW \n Turkey Sausage PWW \n Gruyere Frittata* \n Omelet & Yogurt Bar \n Assorted Bagels* \n Doughnuts* \n Sausage Gravy \n Breakfast Sausage V PWW \n Waffle Bar", inline=True)
        embed.add_field(name='\u200b', value='\u200b', inline=False)
        embed.add_field(name="New Dorm Dinner", value="Bulgogi (Korean BBQ Beef) \n Green Beans with Garlic Chili Sauce V \n Anticuchos de Vegetables V \n Seasoned Broccoli \n New England Clam Chowder \n Veggie Pizza* \n Pepperoni Pizza \n Cheese Pizza* \n Fresh Dough Bread Knots* \n Pecan Pie * \n Hot Fudge Cake V", inline=True)

        embed.add_field(name="Erdman Dinner", value="Vegetable Macaroni & Cheese V \n Beer Battered Cod \n Grilled Chicken Breast PWW \n Seasoned Sweet Potatoes V PWW \n French Fries \n Creamed Corn* \n Roasted Apples & Leeks *PWW \n Beans & Rice V PWW \n Marinara V PWW \n Bolognese Sauce  PWW \n Farfalle V \n Garlic Breadsticks* \n Sundae Bar", inline=True)
        embed.set_footer(text="*= VEGETARIAN      V = VEGAN     PWW = PREPARED without WHEAT \n Menu items identified with this mark are prepared in a common kitchen to be Prepared without Wheat, Vegan, or Vegetarian.")

        await message.channel.send(embed=embed)
      
    #library function
    #provide the general information about Carpenter library
    if message.content.startswith('/carpenter'):
      embed = discord.Embed(title="CARPENTER LIBRARY")
      embed.description = ('Carpenter Library Website: (https://www.brynmawr.edu/inside/offices-services/library-information-technology-services/about/spaces/libraries/carpenter-library) \nCarpenter Library collections support programs in History of Art; Classical and Near Eastern Archaeology; Greek, Latin, Classical Studies; and Growth and Structure of Cities. Carpenter also houses five classrooms and the Digital Media and Collaboration Lab. \n\nWeekday - Open: 8am / Close: 12am (10pm on Friday) \n Saturday - Open: 10am / Close: 10pm\nSunday - Open: 10am / Close: 12am')
      await message.channel.send(embed=embed)
      
    #library function 
    #provide the general information about Canaday library
    if message.content.startswith('/canaday'):
      embed = discord.Embed(title="CANADAY LIBRARY")
      embed.description = ('Canaday Library Website: (https://www.brynmawr.edu/inside/offices-services/library-information-technology-services/about/spaces/libraries/canaday-library) \nCanaday Library is the College’s main humanities and social sciences library. It houses the humanities and social sciences collections, Special Collections, the College Archives, computer labs, the Writing Center, the Lusty Cup Cafe, and many library staff offices.\n\nWeekday - Open: 8am / Close: 12am (10pm on Friday) \nSaturday - Open: 10am / Close: 10pm\nSunday - Open: 10am / Close: 12am')
      await message.channel.send(embed=embed)

    #campus safety function
    #provide the phone number of campus safety
    if message.content.startswith('/campus safety'):
      embed=discord.Embed(title="Campus Safety Phone Number", description="610-526-7911")
      embed.set_thumbnail(url="https://i.imgur.com/xH3a2B3.png")
      await message.channel.send(embed=embed)
    
    #health function
    #provide the phone number of health center
    if message.content.startswith('/health'):
      embed = discord.Embed(title="HEALTH AND WELLNESS CENTER")
      embed.description = ('For medical issues, please call: 610-517-4921\nFor making an appointment, please call 610-526-7360')
      embed.set_thumbnail(url="https://i.imgur.com/EKu9m5x.png")
      await message.channel.send(embed = embed)
      
    #all dean offic hours
    if message.content.startswith('/dean'):  
      embed = discord.Embed()
      embed.description = ('First Year Dean Mary Beth Horvath: [calendly](https://calendly.com/deanhorvath). \nSecond Year Dean Rachel Heiser: [calendly](https://calendly.com/rheiser-1/). \nThird and Fourth Year Dean Tonja Nixon: [calendly](https://calendly.com/tnixon1).')
      await message.channel.send(embed=embed)
      
    #bus function
    #Bus Schedule for Week
    #Sunday bus
    if message.content.startswith('/bus sunday'):
      embed = discord.Embed(
        title="Sunday"
      )
      embed.set_thumbnail(url="https://i.imgur.com/PoJk36B.png")
      embed.add_field(name="BMC to HC", value="9:30a \n 10:15a \n 11:30a \n 12:30p \n 1:30p \n 2:30p \n 3:30p \n 4:15p \n 5:00p \n 5:30p \n 6:00p \n 6:30p \n 7:00p \n 7:30p \n 8:00p \n 9:00p \n 10:00p \n 11:00p \n 12:00a", inline=True)
      embed.add_field(name="HC to BMC", value="9:45a \n 10:45a \n 11:45a \n 12:45p \n 1:45p \n 2:45p \n 3:45p \n 4:30p \n 5:15p \n 5:45p \n 6:15p \n 6:45p \n 7:15p \n 7:45p \n 8:15p \n 9:15p \n 10:15p \n 11:15p \n 12:15a", inline=True)
      await message.channel.send(embed=embed)

    #Saturday bus
    if message.content.startswith('/bus saturday'):
      embed1 = discord.Embed(
        title="Saturday Daytime"
      )
      embed2 = discord.Embed(
        title="Saturday Night"
      )
      embed1.set_thumbnail(url="https://i.imgur.com/PoJk36B.png")
      embed1.add_field(name="Leaves BMC", value="10:00a \n 11:15a \n 12:15p \n 1:15p \n 2:15p \n 3:15p \n 4:30p", inline=True)
      embed1.add_field(name="Leaves Suburban Square", value="-- \n 11:25a \n 12:25p \n 1:25p \n 2:25p \n 3:25p \n --", inline=True)
      embed1.add_field(name="Leaves HC South Lot", value="-- \n 11:35a \n 12:35p \n 1:35p \n 2:35p \n 3:35p \n --", inline=True)
      embed1.add_field(name="Leaves Stokes", value="11:00a \n 11:40a \n 12:40p \n 1:40p \n 2:40p \n 3:40p \n 4:45p", inline=True)
      embed1.add_field(name="Leaves Suburban Square", value="-- \n 11:50a \n 12:50p \n 1:50p \n 2:50p \n 3:50p \n --", inline=True)
      embed2.set_thumbnail(url="https://i.imgur.com/PoJk36B.png")
      embed2.add_field(name="BMC to HC", value="5:00p \n 5:30 \n 6:00p \n 6:30p \n 7:00p \n 8:00p \n 9:00p \n 9:30p \n 10:00p \n 10:30p \n 11:00p \n 12:00a \n 12:30a \n 1:00a \n 1:30a \n 2:15a", inline=True)
      embed2.add_field(name="HC to BMC", value="5:15p \n 5:45p \n 6:15p \n 6:45p \n 7:30p \n 8:30p \n 9:15p \n 9:45p \n 10:15p \n 10:45p \n 11:15p \n 12:15a \n 12:45a \n 1:15a \n 1:45a \n 2:45a", inline=True)
      await message.channel.send(embeds=[embed1, embed2])

    #weekday bus
    if message.content.startswith('/bus monday'):
      embed = discord.Embed(
        title="Monday"
      )
      embed.set_thumbnail(url="https://i.imgur.com/PoJk36B.png")
      embed.add_field(name="Leaves BMC", value=bmcMWF, inline=True)
      embed.add_field(name="Leaves HC", value=hcMWF, inline=True)
      await message.channel.send(embed=embed)

    if message.content.startswith('/bus tuesday'):
      embed = discord.Embed(
        title="Tuesday"
      )
      embed.set_thumbnail(url="https://i.imgur.com/PoJk36B.png")
      embed.add_field(name="Leaves BMC", value=bmcTTh, inline=True)
      embed.add_field(name="Leaves HC", value=hcTTh, inline=True)
      await message.channel.send(embed=embed)
  
    if message.content.startswith('/bus wednesday'):
      embed = discord.Embed(
        title="Wednesday"
      )
      embed.set_thumbnail(url="https://i.imgur.com/PoJk36B.png")
      embed.add_field(name="Leaves BMC", value=bmcMWF, inline=True)
      embed.add_field(name="Leaves HC", value=hcMWF, inline=True)
      await message.channel.send(embed=embed)

    if message.content.startswith('/bus thursday'):
      embed = discord.Embed(
        title="Thursday"
      )
      embed.set_thumbnail(url="https://i.imgur.com/PoJk36B.png")
      embed.add_field(name="Leaves BMC", value=bmcTTh, inline=True)
      embed.add_field(name="Leaves HC", value=hcTTh, inline=True)
      await message.channel.send(embed=embed)
  
    if message.content.startswith('/bus friday'):
      embed = discord.Embed(
        title="Friday"
      )
      embed.set_thumbnail(url="https://i.imgur.com/PoJk36B.png")
      embed.add_field(name="Leaves BMC", value=bmcMWF, inline=True)
      embed.add_field(name="Leaves HC", value=hcMWF, inline=True)
      await message.channel.send(embed=embed)
  
    #course function
    #print out the course in the specified semester of the major
    if message.content.startswith('/courses'):
      if '/computerScience' in message.content[8:]:
        if '/spring2024' in message.content[24:]:
          embed = discord.Embed(title="Computer Science Spring 2024 Courses",
          color=message.channel.guild.me.top_role.color,
          timestamp=message.created_at,)
  
          #print out the course name
          embed.add_field(name="Course Name", value="CMSC B113-001 Computer Science I \n\n CMSC B151-001	Introduction to Data Structures \n CMSC B231-001	Discrete Mathematics \n CMSC B240-001	Principles of Computer Organization \n CMSC B337-001	Algorithms: Design and Practice \n CMSC B355-001	Operating Systems \n\n CMSC B399-001	Senior Conference", inline=True)
          embed.set_thumbnail(url="https://i.imgur.com/yD1GUJe.png")
          #print out the course meeting time
          embed.add_field(name="Meeting Time", value="Lecture: 1:10 PM-2:30 PM MW / Laboratory: 2:40 PM-4:00 PM W \n Lecture: 1:10 PM-2:30 PM MW / Laboratory: 2:40 PM-4:00 PM M \n Lecture: 11:25 AM-12:45 PM TTH \n Lecture: 12:55 PM-2:15 PM TTH / Laboratory: 2:25 PM-3:45 PM T \n Lecture: 10:10 AM-11:30 AM MW / Laboratory: 2:40 PM-4:00 PM W \n Lecture: 1:10 PM-2:30 PM MW :/ Laboratory: 11:40 AM-1:00 PM W \n Lecure: 2:10 PM-4:00 PM F", inline=True)
        await message.channel.send(embed=embed)
        
#our token don't touch this!
client.run('MTE3MjcxNjI1MDQ1MTk0NzU0MA.GQ-LaK.KFyRK_ppaD-OBYCGdZcCaZBA3izku0YILdw7sM')