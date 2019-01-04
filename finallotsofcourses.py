from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from finaldatabase_setup import University, Base, Course, User
 
engine = create_engine('sqlite:///curriculum.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


#Dummy Users
# Create dummy user
User1 = User(name="Bob", email="bob@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()



#Curriculum for Hogwarts
university1 = University(user_id=1,name = "University of Hogwarts")

session.add(university1)
session.commit()


courseItem1 = Course(user_id=1,name = "Levitation Charm", description = "Makes objects fly!", professor = "Prof. Filius Flitwick ", school = "School of Spells", university = university1)

session.add(courseItem1)
session.commit()

courseItem2 = Course(user_id=1,name = "Curse of the Bogies", description = "Gives the recipient a strong cold!", professor = "Prof. Severus Snape", school = "School of Defence Against Dark Arts", university = university1)
session.add(courseItem2)
session.commit()

courseItem3 = Course(user_id=1,name = "Polyjuice Potion", description = "Makes you turn into form of someone else!", professor = "Prof. Horace Slughorn", school = "School of Potions", university = university1)

session.add(courseItem3)
session.commit()

courseItem4 = Course(user_id=1,name = "Hippogriff", description = "Half horse, half eagle creatures!", professor = "Prof. Rubeus Hagrid", school = "School of Creature Care", university = university1)

session.add(courseItem4)
session.commit()

courseItem5 = Course(user_id=1,name = "Fire-Making Charm", description = "Conjures a jet of orange and red flame!", professor = "Prof. Filius Flitwick ", school = "School of Spells", university = university1)

session.add(courseItem5)
session.commit()

courseItem6 = Course(user_id=1,name = "Forgetfulness Potion", description = "Causes memory loss in the drinker!", professor = "Prof. Horace Slughorn", school = "School of Potions", university = university1)
session.add(courseItem6)
session.commit()

courseItem7 = Course(user_id=1,name = "Full Body-Bind Curse", description = "Stiffens a person’s limbs!", professor = "Prof. Severus Snape", school = "School of Defence Against Dark Arts", university = university1)

session.add(courseItem7)
session.commit()

courseItem8 = Course(user_id=1,name = "Flobberworm", description = "Herbivorous, ten-inch, toothless brown worm!", professor = "Prof. Rubeus Hagrid", school = "School of Creature Care", university = university1)

session.add(courseItem8)
session.commit()





#Curriculum for Ilvermorny
university2 = University(user_id=1,name = "University of Ilvermorny")

session.add(university2)
session.commit()


courseItem1 = Course(user_id=1,name = "Mending Charm", description = "Repair broken objects with a flick of the wand!", professor = "Prof. Eulalie Hicks", school = "School of Spells", university = university2)

session.add(courseItem1)
session.commit()

courseItem2 = Course(user_id=1,name = "Knockback Jinx", description = "Knocks away the recepient!", professor = "Prof.  Rionach Steward", school = "School of Defence Against Dark Arts", university = university2)
session.add(courseItem2)
session.commit()

courseItem3 = Course(user_id=1,name = "Herbicide Potion", description = "Kills or damages plants!", professor = "Prof. Isolt Sayre", school = "School of Potions", university = university2)

session.add(courseItem3)
session.commit()

courseItem4 = Course(user_id=1,name = "Fire Dwelling Salamander", description = "Small lizard which can emit great heat!", professor = "Prof. Agilbert Fontaine", school = "School of Creature Care", university = university2)

session.add(courseItem4)
session.commit()

courseItem5 = Course(user_id=1,name = "Wand-Lighting Charm", description = "Illuminates the tip of the caster's wand!", professor = "Prof. Eulalie Hicks", school = "School of Spells", university = university2)

session.add(courseItem5)
session.commit()




#Curriculum for Gryffindor
university1 = University(user_id=1,name = "University of Gryffindor")

session.add(university1)
session.commit()


courseItem1 = Course(user_id=1,name = "Unlocking Charm", description = "Unlocks and opens locks!", professor = "Prof. Albus Dumbledore", school = "School of Spells", university = university1)

session.add(courseItem1)
session.commit()

courseItem2 = Course(user_id=1,name = "Tongue-Tying Curse", description = "Prevents your opponent from accurately casting their next spell!", professor = "Prof. Godric Gryffindor ", school = "School of Defence Against Dark Arts", university = university1)
session.add(courseItem2)
session.commit()

courseItem3 = Course(user_id=1,name = " Wiggenweld Potion", description = "Heals injuries, or reverse the effects of a Sleeping Draught!", professor = "Prof. Minerva McGonagall", school = "School of Potions", university = university1)

session.add(courseItem3)
session.commit()

courseItem4 = Course(user_id=1,name = "Niffler", description = "Long-snouted, burrowing creatures with a penchant for anything shiny!", professor = "Prof. Newt Scamander", school = "School of Creature Care", university = university1)

session.add(courseItem4)
session.commit()

courseItem5 = Course(user_id=1,name = " Melofors Jinx", description = "Encases the victim's head in a pumpkin!", professor = "Prof. Godric Gryffindor ", school = "School of Defence Against Dark Arts", university = university1)

session.add(courseItem5)
session.commit()



#Curriculum of Hufflepuff
university1 = University(user_id=1,name = "University of Hufflepuff")

session.add(university1)
session.commit()


courseItem1 = Course(user_id=1,name = "Softening Charm", description = "Softens a target area!", professor = "Prof. Helga Hufflepuff ", school = "School of Spells", university = university1)

session.add(courseItem1)
session.commit()

courseItem2 = Course(user_id=1,name = "Red Sparks", description = "Precipitates a jet of red sparks from the tip of the wand!", professor = "Prof. Zacharias Smith", school = "School of Defence Against Dark Arts", university = university1)
session.add(courseItem2)
session.commit()

courseItem3 = Course(user_id=1,name = "Sleeping Draught", description = "Makes drinker fall almost instantly into a deep, dreamless sleep!", professor = "Prof. Pomona Sprout", school = "School of Potions", university = university1)

session.add(courseItem3)
session.commit()

courseItem4 = Course(user_id=1,name = "Fire Crab", description = "Crabs that shoot hot flames!", professor = "Prof. Olympe Maxime", school = "School of Creature Care", university = university1)

session.add(courseItem4)
session.commit()

courseItem5 = Course(user_id=1,name = "Wand-Extinguishing Charm", description = "Makes light at the wand's tip to be extinguished!", professor = "Prof. Helga Hufflepuff ", school = "School of Spells", university = university1)

session.add(courseItem5)
session.commit()


#Curriculum for Ravenclaw
university1 = University(user_id=1,name = "University of Ravenclaw")

session.add(university1)
session.commit()


courseItem1 = Course(user_id=1,name = "Locking Spell", description = "Seals locks!", professor = "Prof. Rufus Scrimgeour", school = "School of Spells", university = university1)

session.add(courseItem1)
session.commit()

courseItem2 = Course(user_id=1,name = "Green Sparks", description = "Shoots out jets of green sparks!", professor = "Prof. Helena Ravenclaw", school = "School of Defence Against Dark Arts", university = university1)
session.add(courseItem2)
session.commit()

courseItem3 = Course(user_id=1,name = "Girding Potion", description = "Gives the consumer extra endurance!", professor = "Prof. Kingsley Shacklebolt", school = "School of Potions", university = university1)

session.add(courseItem3)
session.commit()

courseItem4 = Course(user_id=1,name = "Murtlap", description = "Marine beast resembling a rat!", professor = "Prof. Rowena Ravenclaw", school = "School of Creature Care", university = university1)

session.add(courseItem4)
session.commit()

courseItem5 = Course(user_id=1,name = "Streeler", description = "Giant snails that change colour on an hourly basis and leave a venomous trail!", professor = "Prof. Rowena Ravenclaw", school = "School of Creature Care", university = university1)

session.add(courseItem5)
session.commit()

#Curriculum for Slytherin 
university1 = University(user_id=1,name = "University of Slytherin")

session.add(university1)
session.commit()


courseItem1 = Course(user_id=1,name = "Skurge Scouring Charm", description = "Gets rid of ectoplasm created by passing ghosts!", professor = "Prof. Quirinus Quirrell", school = "School of Spells", university = university1)

session.add(courseItem1)
session.commit()

courseItem2 = Course(user_id=1,name = "Smokescreen Spell", description = "Creates a defensive cloud of smoke from wand's tip!", professor = "Prof. Lucius Malfoy", school = "School of Defence Against Dark Arts", university = university1)
session.add(courseItem2)
session.commit()

courseItem3 = Course(user_id=1,name = "Confusing Concoction", description = "Causes confusion in the drinker!", professor = "Prof. Salazar Slytherin", school = "School of Potions", university = university1)

session.add(courseItem3)
session.commit()

courseItem4 = Course(user_id=1,name = "Blast-Ended Skrewt", description = "Cross of Manticores and Fire crabs!", professor = "Prof. Theodore Nott", school = "School of Creature Care", university = university1)

session.add(courseItem4)
session.commit()

courseItem5 = Course(user_id=1,name = "Wideye Potion", description = "Prevents the drinker from falling asleep!", professor = "Prof. Salazar Slytherin", school = "School of Potions", university = university1)

session.add(courseItem5)
session.commit()



print("added courses!")

