import random

hammurabi_info = {
    "key": "value",
    "people": 95,
    "entered_people":5,
    "bushels": 2800,
    "acres":1000,
    "landValue":19,
    "Year_Counter":1
}


class Hammurabi:
    def __init__(self) -> None:
        self.rand = random.Random()

    def main(self):
        self.rungame()
        #self.playGame()

    def playGame(self):
        # declare local variables here: grain, population, etc.
        # statements go after the declarations
        pass
    #other methods go here

    def summary():
        """
        print the summary each year:
            O great Hammurabi!
            You are in year 1 of your ten year rule.
            In the previous year 0 people starved to death.
            In the previous year 5 people entered the kingdom.
            The population is now 100.
            We harvested 3000 bushels at 3 bushels per acre.
            Rats destroyed 200 bushels, leaving 2800 bushels in storage.
            The city owns 1000 acres of land.
            Land is currently worth 19 bushels per acre.
        """
        print("O great Hammurabi!\n"+
              "You are in year "+str(hammurabi_info["Year_Counter"])+" of your ten year rule.\n"+
              "In the previous year 0 people starved to death.\n"
              "In the previous year "+str(hammurabi_info["entered_people"])+" people entered the Kingdom.\n"+
              "The population is now "+(str(hammurabi_info["people"]+hammurabi_info["entered_people"]))+".\n"+
              "We harvested 3000 bushels at 3 bushls per acre.\n"+
              "Rats destroyed 0 bushels, leaving " +str(hammurabi_info["bushels"])+" bushels in storage.\n"+
              "The city owns "+str(hammurabi_info["acres"])+" acres of land.\n"+
              "Land is currently worth "+str(hammurabi_info["landValue"])+" bushels per acre."
              )
        
        pass


    def ask_How_Many_Acres_To_buy(price, bushels):
        """
        Asks the player how many acres of land to buy, and returns that number. You must have enough grain to pay for your purchase.
        """
        print("How many acres do you want to buy?")
        answer = int(input())
        if (answer*price)<bushels:
            hammurabi_info["bushels"]-=answer*price
            hammurabi_info["acres"]+=answer
            return answer
        else:
            print("you dont have enough grain")
            Hammurabi.ask_How_Many_Acres_To_buy(price,bushels)
        

    def ask_How_Many_Acres_To_sell(acresOwned):
        """
        Asks the player how many acres of land to sell, and returns that number. You can't sell more than you have.
        """
        print("How many acres do you want to sell?")
        answer = int(input())
        if answer<acresOwned:
            hammurabi_info["bushels"]+=answer*hammurabi_info["landValue"]
            hammurabi_info["acres"]-=answer
            return answer
        else:
            print("you don't have enough land")
            Hammurabi.ask_How_Many_Acres_To_sell(acresOwned)
        

    def ask_How_Much_Grain_To_Feed_People(bushels):
        """
        Ask the player how much grain to feed people, and returns that number. You can't feed them more grain than you have. You can feed them more than they need to survive.
        """
        print("How much grain to feed people?")
        answer = int(input())
        if answer>bushels:
            print("You don't have enough grain")
            Hammurabi.ask_How_Much_Grain_To_Feed_People(bushels)
        elif(answer<(hammurabi_info["people"]+hammurabi_info["entered_people"])*20):
            hammurabi_info["people"]=answer//20
            return answer
        else:
            hammurabi_info["bushels"]-= answer
            return answer



    def ask_How_Many_Acres_To_Plant(acresOwned,population,bushels):
        """
        Ask the player how many acres to plant with grain, and returns that number. You must have enough acres, enough grain, and enough people to do the planting. Any grain left over goes into storage for next year.
        """
        print("How many acres do you want to plant?")
        answer = int(input())
        if(answer<population*10 and answer*2<bushels and answer<acresOwned):
            hammurabi_info["bushels"]-=answer*2
            hammurabi_info["bushels"]+=answer*random.randint(1,7)
            return answer
        else:
            print("you don't have enough resourse")
            Hammurabi.ask_How_Many_Acres_To_Plant(acresOwned,population,bushels)



    def rungame():
        game = Hammurabi()
        Hammurabi.summary()
        while hammurabi_info["Year_Counter"]<10:
            people_thisyear = hammurabi_info["people"]+hammurabi_info["entered_people"]
            print("Do you want to buy the land or sell the land?")
            buy_or_sell = input().lower()
            if buy_or_sell =="buy":
                Hammurabi.ask_How_Many_Acres_To_buy(hammurabi_info["landValue"],hammurabi_info["bushels"])
            elif buy_or_sell =="sell":
                Hammurabi.ask_How_Many_Acres_To_sell(hammurabi_info["acres"])
            else:
                print("got it, no buy no sell.")
            Hammurabi.ask_How_Much_Grain_To_Feed_People(hammurabi_info["bushels"])

            if(hammurabi_info["people"]+hammurabi_info["entered_people"]<people_thisyear*0.55):
                print("Too many people dead from starvation.")
                break

            Hammurabi.ask_How_Many_Acres_To_Plant(hammurabi_info["acres"],hammurabi_info["people"],hammurabi_info["bushels"])

            hammurabi_info["people"]+=hammurabi_info["entered_people"]



            hammurabi_info["Year_Counter"]+=1
            hammurabi_info["people"]+=hammurabi_info["entered_people"]
            hammurabi_info["entered_people"]=random.randint(0,5)
            hammurabi_info["landValue"]=random.randint(17,24)
            Hammurabi.summary()
            pass

        print("You done with your rule.")
        print("===========================")
        pass

Hammurabi.rungame()

#if __name__ == "__main__":
#    hammurabi = Hammurabi()
#    hammurabi.main()


"""
Hammurabi.summary()
Hammurabi.ask_How_Many_Acres_To_buy(hammurabi_info["landValue"],hammurabi_info["bushels"])
Hammurabi.summary()
Hammurabi.ask_How_Many_Acres_To_sell(hammurabi_info["acres"])
Hammurabi.summary()
Hammurabi.ask_How_Much_Grain_To_Feed_People(hammurabi_info["bushels"])
Hammurabi.summary()
Hammurabi.ask_How_Many_Acres_To_Plant(hammurabi_info["acres"],hammurabi_info["people"],hammurabi_info["bushels"])
Hammurabi.summary()
"""