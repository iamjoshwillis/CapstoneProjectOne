from models import *
from app import db, app

db.create_all()

#Fill Planet
mercury = Planet(name="Mercury", distance_from_sun="0.4")
venus = Planet(name="Venus", distance_from_sun="0.7")
earth = Planet(name="Earth", distance_from_sun="1")
mars = Planet(name="Mars", distance_from_sun="1.5")
jupiter = Planet(name="Jupiter", distance_from_sun="5.2")
saturn = Planet(name="Saturn", distance_from_sun="9.5")
uranus = Planet(name="Uranus", distance_from_sun="8.8")
neptune = Planet(name="Neptune", distance_from_sun="30.1")
planetnine = Planet(name="Planet 9", distance_from_sun="600")

#Fill Activity
graphite_skiiing = Activity(name="Graphite Skiing", description="Grab a pair of lighning-fast, self-navigating skiis and hit the slick graphite plains around the Caloris Basin of Mercury. It can be up to 800 Degrees F during the day, so cooling suits will be provided.", planet=1)
hyper_tan = Activity(name="Mercurian Hyper-Tan", description="While you're as close to the Sun as you're going to get, enjoy suntanning like you've never experienced before. Our proprietary steam matrix that circulates the air around the resort prevents you from getting burnt to a crisp immediately upon lying down on our state-of-the-art outdoor beds.", planet=1)
mineral_baking = Activity(name="Mineral Baking", description="This is culinary art like you've never experienced before. The rich, diverse minerals and searing heat on the surface of Mercury makes it's random regions of ground the ultimate hibachi grills. There's something special about sourdough baked on the metallic ground of this silver planet.", planet=1)

sulfur_sauna = Activity(name="Sulfur Sauna", description="We've made gaseous sulfuric acid safe and breathable! It's also wonderful for your immune system. Enjoy the field that contains a natural outdoor sauna under the beautiful skies of Venus.", planet=2)
tesserae_hiking = Activity(name="Tesserae Hiking", description="Venus is coated in natural mountains out of a fantasy movie called tesserae that are wonderful, and wonderfully dangerous to hike on if you enjoy the thrill of adventure.", planet=2)
solar_hang_gliding = Activity(name="Solar Wind Hang Gliding", description="Have you ever wanted to hold on for dear life on a hang glider through the intense solar winds on Venus? Sign up today because no one has yet.", planet=2)

glacier_hiking = Activity(name="Icelandic Glacier Hiking", description="Bundle up and get some sturdy boots to prepare to hike across some of Iceland's most captivating mountains of ice.", planet=3)
sailing_the_caribbean = Activity(name="Sailing the Caribbean", description="Experience Earth's Oceans up close with the wind of the sea gracing you. ", planet=3)
scuba = Activity(name="Scuba Diving", description="If you're captivated by Earth's oceans, they've figured out a way to allow you to descend into them without losing the ability to breathe. Get attached to a large metal tank and mask and feel free in the underwater world.", planet=3)

dune_riding = Activity(name="Sub-Zero Dune Riding", description="The crushing cold deserts of Mars make the perfect home to some of the solar system's most revered dune buggy tracks.", planet=4)
desert_high_jump = Activity(name="Desert Track and Field Experience", description="Mars' low gravity will make you feel like you have super powers, easily jumping high into the sky with minimal effort. Come enjoy our obstacle course and field with a variety of events to enjoy in low gravity.", planet=4)
red_sand_spa = Activity(name="Red Sand Spa", description="The rich mineral matrix in Mars' red sands is not only exfoliating, but Mitochondria-stimulating. Cover yourself in red dust and bring your rusty old self back to your glory.", planet=4)

parasailing = Activity(name="Parasail in The Great Red Spot", description="If you think we've lost our minds by bringing a giant airship and parasails into Jupiter's Great Red Spot, you're absolutely right. There's something thrilling about parasailing in extreme cold winds, lightning, and arouras that would exhilarate even the Sky Father himself.", planet=5)
aurora_tour = Activity(name="Purple Aurora Tour", description="Jupiter's vibrant purple Northern Lights have a mystical presentation. Hop on an airship with a guided tour up to Jupiter's North Pole to experience the extraordinary wash of purple lights.", planet=5)

ring_surfing = Activity(name="Ring Surfing", description="Our electromagnetic hover boards follow a predetermined path around the region of Saturn's rings that will make you feel like you're surfing them.", planet=6)
lazy_jet_stream = Activity(name="Lazy Jet Stream", description="If you enjoy a lazy river that is common on Earth, imagine the same concept in the sky. Grab a lounge pod and let a jet stream that will effortlessly sail you around the atmosphere of Saturn do the rest.", planet=6)
ptolemys_observatory = Activity(name="Ptolemy's Observatory", description="Placed at the perfectly optimal longitude for a prime view of the Rings of Saturn, Ptolemy's Observatory has high quality telescopes that intelligently filter through Saturn's distinct three layers of clouds. There is also hot chocolate when the machine isn't down.", planet=6)

ultradark = Activity(name="Ultradark Cloud Resort", description="A mesmerizing spa resort that has zero natural light. Some of the gas particles will glow a relaxing deep blue that will make you feel like you're in a neon fantasy world.", planet=7)
diamond_bergs = Activity(name="Diamond Bergs Lake Sailing", description="You've more than likely heard of icebergs, but how about diamond bergs? Giant masses of diamonds float in a lake that we placed a fleet of sailboats on.", planet=7)
natural_cryotherapy = Activity(name="Natural Cryotherapy", description="Uranus is the coldest planet in our solar system, and your inflammation could use it's help. Although incredibly high risk, we allow people to step outside with a helmet, gloves, and boots. You will either freeze-dry or feel like your best self.", planet=7)

deprivation_spa = Activity(name="Sensory Deprivation Pressure Spa", description="With Neptune's relatively high gravity, we've developed monitored cubicles that act as a sensory deprivation tank, but use Neptune's natural gravity.", planet=8)
meteor_zip_lining = Activity(name="Meteor Zip Lining", description="Tracking technology on Neptune has allowed us to place zip lining courses on its orbiting meteors. It's a thrill you'll never forget.", planet=8)
great_dark_spot_skydiving = Activity(name="Skydiving in the Great Dark Spot", description="This is a captivating experience as you have the opportunity to jump into a dark, seemingly infinite abyss.", planet=8)

infrared_therapy = Activity(name="Infrared Spa Therapy", description="Red light and infrared therapy is a relatively new hidden gem. Planet 9's high volume of infrared light will give you brand new skin.", planet=9)
black_hole_experience = Activity(name="Black Hole Experience", description="We've perfectly captured a safe region within a nearby black hole that allows visitors to have the experience of seeing sped up time on the outside and an oddly pleasant increase in gravity.", planet=9)

#Fill Hotel
hermes_palace = Hotel(name="Hermes' Palace", description="Luxury Resort that contains an oasis of rivers and natural waterslides in a quarter-mile-wide ultraglass dome.", planet=1)
hotel_caloris = Hotel(name="Hotel Caloris", description="Beautiful, modern resort that overlooks the Caloris Basin of Mercury.", planet=1)

flying_goddess = Hotel(name="The Flying Goddess", description="The premiere luxury resort of Venus. While it's a 5 minute walk to the Sulfur Sauna, it may take longer if you're not used to walking in Venus' intense gravity. Please plan ahead.", planet=2)

hotel_hamar = Hotel(name="Hotel Hamar", description="One of Iceland's hidden gems, Hotel Hamar overlooks a snowy mountain range that captures the winter beauty of this mystical country on Earth.", planet=3)
jade_mountain = Hotel(name="Jade Mountain Resort", description="If you've never experienced the Caribbean during the season of Summer on Earth, enjoy the ocean breeze of this region of the planet.", planet=3)

inn_of_the_god_of_war = Hotel(name="Inn of the God of War", description="The red desert is all that you can see in the 360 degree windows of this mid-level Martian hotel.", planet=4)
red_resort = Hotel(name="The Red Resort", description="Mars' finest display of cuisine, hospitality, and scenery. The -80 degree F temperatures make this a wonderful location for cryotherapy and breathholding training.", planet=4)

great_red_spot_resort = Hotel(name="The Great Red Spot Resort", description="Arguably a wonder of the solar system, this hotel is peacefully suspended in the gaseous clouds of The Great Red Spot.", planet=5)
cyclone_hotel = Hotel(name="Cyclone Hotel", description="Not for individuals who suffer from motion sickness. This flying capsule contains 328 suites and spins at a rapid pace around the windstorms of Jupiter.", planet=5)

treasure_cove = Hotel(name="The God of Wealth's Treasure Cove", description="A giant, building-sized pirate ship with decorative gold coins spilling all over the floors. This is a mobile resort that floats around the clouds of Saturn.", planet=6)
ring_view_resort = Hotel(name="Ring View Resort", description="A hotel up on the rings of Saturn was placed on the optimal piece of debris for this relaxing, spaceous retreat.", planet=6)

white_gold = Hotel(name="White Gold Luxury Resort", description="Get your wallet out for Uranus, as this is the most opulent, expensive place to stay in the Solar System.", planet=7)
auroral_clouds = Hotel(name="Auroral Clouds Hotel", description="The bright purple auroras of Uranus are a sight you're going to want a front row seat for.", planet=7)

neptunes_trident = Hotel(name="Neptune's Trident Resort", description="The ultimate spot for cold exposure therapy. The lustrious pool area with icy waterfalls and chaotic dynamic storms aren't for the faint of heart. You'll leave thinking that you're Dennis Quaid in The Day After Tomorrow.", planet=8)
galileo = Hotel(name="The Galileo", description="Imagine watching some of the most intense storm systems with 1300 MPH winds from a large lounge designed to look like a room in Galileo's time with a tranquil fire.", planet=8)

hotel_nine = Hotel(name="Hotel 9", description="A Vanta Black building that is invisible to the human eye. You will be led to the entrance by Planet 9's mysterious inhabitants that may or may not be dangerous. No one has ever checked out of the hotel, so please exercise your own discretion.", planet=9)
dark_origin_resort = Hotel(name="Dark Origin Resort", description="Planet 9's premiere resort that features a liquid anti-matter swimming pool and slides. Due to differing laws of physics than humans are familiar with, and the unknown behavior of gravity, you'll feel like a super hero navigating the resort's Dark Matter Trail and Park.", planet=9)



#Fill Airport
mercurius = Airport(name="Mercurius Interplanetary Airport", planet=1)
ishtar = Airport(name="Ishtar Terra Airport", planet=2)
world_of_water = Airport(name="World of Water Interplanetary Airport", planet=3)
olympus_mons = Airport(name="Olympus Mons Interplanetary Airport", planet=4)
king_airport = Airport(name="The King of Planets Airport", planet=5)
saturni = Airport(name="Saturni Interplanetary", planet=6)
ouranos = Airport(name="Airport of Ouranos", planet=7)
god_of_the_sea = Airport(name="God of the Sea Interplanetary Airport", planet=8)
airport_nine = Airport(name="Interplanetary Airport 9", planet=9)

#Fill Restaurant
mercurmeals = Restaurant(name="MercurMeals", description="The oddly suspicious silver arches resemble an iconic logo that most humans are familiar with on Earth. The food is strangeley similar, as well.", planet=1)
graphite_steakhouse = Restaurant(name="Graphite Steakhouse", description="The culinary artform of graphite searing is something Mercury has mastered at this fine dining establishment.", planet=1)

volcanic_steakhouse = Restaurant(name="The Volcanic Steakhouse", description="Everything is superheated in our revolutionary lava fryer to perfection. The dishes served on a cooled plate of lava within our rocky ambience is a dream.", planet=2)
the_greenhouse = Restaurant(name="The Greenhouse", description="Venus is essentially a giant greenhouse, so enjoy this one of a kind experience of bowls, grains, meats, and other clean foods.", planet=2)

hyeholde = Restaurant(name="Hyeholde Castle", description="A garganuan castle hidden in Pennsylvania, USA, Hyeholde Castle is an exquisite fine dining experience.", planet=3)
mcdonalds = Restaurant(name="McDonald's", description="The golden standard of culinary glory here on Earth.", planet=3)

green_martian_grill = Restaurant(name="The Green Martian Grill", description="Enjoy pizza, junk food, and deep fried Martian antannae in this cartoony, futuristic arcade restaurant.", planet=4)
red_dust_delicacies = Restaurant(name="Red Dust Delicacies", description="Mars is home to some of the most unique, freeze-dried desserts. You'll never care about powdered sugar again after you've tried Mars' famous Confectioner's Dusted Red Rock.", planet=4)

gas_giant_grill = Restaurant(name="Gas Giant Grill", description="While we can't guarantee our probiotic-rich food won't turn you into a gas giant, we pride ourselves in the highest-quality cuisine in The Great Red Spot.", planet=5)
sky_father = Restaurant(name="Sky Father's Distillery and Restaurant", description="Vodka distillation in the extreme temperature gradients in the storms of Jupiter has made this planet famous among fine spirits connoisseurs. We also have mediocre burgers.", planet=5)

hexagonal_clouds = Restaurant(name="Hexagonal Clouds Eatery", description="Saturn is home to many of the most spectacular displays of weather. We are the premiere place for ice cream, cotton candy, and chocolates here on Saturn.", planet=6)
brewhouse_of_the_rings = Restaurant(name="Brewhouse of the Rings", description="One of Saturn's rings to rule them all, one of Saturn's rings to find them, one of Saturn's rings to bring them all, and in our brewhouse bind them.", planet=6)

cyan_cafe = Restaurant(name="Cyan Cafe", description="The wonderous milky blue hue of Uranus was a generic and easy idea to capitalize making a restaurant on.", planet=7)
dark_nebula = Restaurant(name="Dark Nebula", description="The only Michelin Starred restaurant on Uranus, Dark Nebula is a beautiful room with naturally illuminated folliage.", planet=7)

oceanus = Restaurant(name="Oceanus", description="Exquisite seafood in liquid oceans like no other. Several species of Neptune's diverse alien aquatic life make wonderful filets.", planet=8)
dark_spot_grill = Restaurant(name="Great Dark Spot Grill", description="If you are brave enough to venture to Neptune's Great Dark Spot, this restaurant will give you the power to run against the 1300 MPH winds just outside our convenient location in a massive, lethal storm system.", planet=8)

dark_matter_tavern = Restaurant(name="Dark Matter Tavern", description="Lit only by red light from this planet's mysterious photons, this tavern is the perfect spot to hide away and eat questionable entrees.", planet=9)
chipotle = Restaurant(name="Chipotle Mexican Grill", description="Just when you thought that Chipotle couldn't impress you any more, they outdid themselves by opening a location on a -375 degree F planet with an unknown form of gravity. You're going to want to add that extra guacamole.", planet=9)

db.session.add_all([mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, planetnine])

db.session.commit()

db.session.add_all([mercurmeals, graphite_steakhouse, hyeholde, mcdonalds, green_martian_grill, gas_giant_grill, sky_father, hexagonal_clouds, brewhouse_of_the_rings, cyan_cafe, dark_nebula, oceanus, dark_matter_tavern, chipotle, graphite_skiiing, sulfur_sauna, tesserae_hiking, solar_hang_gliding, mineral_baking, glacier_hiking, sailing_the_caribbean, scuba, dune_riding, desert_high_jump, red_dust_delicacies, dark_spot_grill, red_sand_spa, parasailing, aurora_tour, ring_surfing, ptolemys_observatory, lazy_jet_stream, hermes_palace, hotel_caloris, flying_goddess, ultradark, natural_cryotherapy, diamond_bergs, deprivation_spa, meteor_zip_lining, great_dark_spot_skydiving, infrared_therapy, black_hole_experience, mercurius, ishtar, world_of_water, olympus_mons, king_airport, saturni, ouranos, god_of_the_sea, airport_nine, volcanic_steakhouse, the_greenhouse, hotel_hamar, jade_mountain, inn_of_the_god_of_war, red_resort, great_red_spot_resort, cyclone_hotel, treasure_cove, ring_view_resort, white_gold, auroral_clouds, neptunes_trident, galileo, hotel_nine, dark_origin_resort])

db.session.commit()

