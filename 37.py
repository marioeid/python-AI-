from pyknow import*
#First Expert System



class symptom(Fact):
    pass

sympts = []
clowsugar = ["shakiness", "hunger", "sweating", "headache", "pale"]
chighsugar = ["thirst" , "blurred vision", "headache", "dry mouth", "smelling breath", "shortnessof breath"]
cold = ["harsh cough", "runny nose"]
measeles = ["brownish-pink", "rash", "high and fast temperature", "bloodshot eyes" , "white spots inside cheek"]
mumps = ["has moderate temperature", "saliva is not normal" , "swollen lymph nodes in neck" , "mouth dry then"]
flu= ["conjunctives","strong body aches", "weakness, vomiting", "sore throat and sneezing"]
class patient(KnowledgeEngine):

    @Rule(symptom(age="child",ls= L(3) | L(4) |L(5)))
    def low_sugar(self):
        print("you have signs of low sugar")
        #yield symptom(hasLowSugar="yes")

        dp =input("does/did any of your parents have diabetes?")
        if dp == "yes":
            print("you have diabetes")

    @Rule(symptom(age="child", hs= L(3) | L(4) |L(5)|L(6)))
    def high_sugar(self):
        print("you have signs of high sugar")


    @Rule(symptom(clds=L(2)))
    def cold_signs(self):
        print("you have signs of cold")
        if len(set(sympts) & set(measeles)) == 5:
            print("you have measles")

    @Rule(symptom(age="child",mmps=L(4)))
    def has_mumps(self):
        print("you have mumps")

    @Rule(symptom(age="child",fl=L(5)))
    def ch_flu(self):
        print("you have child flu")

    @Rule(symptom(age="adult", fl=L(5)))
    def ch_flu(self):
        print("you have adult flu")

# print("\t\tWelcome to PyDoc")
# Age = input("please enter your age\n")
# if (int)(Age) <= 5:

#     status = "child"
# else :
#     status = "adult"
# cont = 'y'
#
# while cont == 'y':
#     sym = input("Tell us one of your symptoms\n")
#     sympts.append(sym)
#     cont = (input("if you would like to add more symptoms press y, or press any key to continue\n"))
#
#
# pat = patient()
# pat.reset()
# pat.declare(symptom(age=status,ls=len(set(sympts)&set(clowsugar)), hs=len(set(sympts)&set(chighsugar)),clds = len(set(sympts)&set(cold)), msls=len(set(sympts)&set(measeles)), mmps= len(set(sympts)&set(mumps)), fl=len(set(sympts)&set(flu))))
# pat.run()



#Second Expert System


'''*************************************************Welcome to Py_plant**********************************************'''


class Describe(Fact):
    pass


class the_plant(KnowledgeEngine):
    @Rule((Describe(temperature='high', humidity='normal', tuber='spots', tuber_color='reddish-brown')))
    def black_heart(self):
        print("the plant has black heart.")

    @Rule((Describe(temperature='low', humidity='high', tuber='spots', type_tuber='normal')))
    def late_blight(self):
        print("the plant has late blight.")

    @Rule((Describe(temperature='high', humidity='normal', tuber='circles', type_tuber='dry')))
    def dry_rot(self):
        print("the plant has dry rot.")

    @Rule((Describe(temperature='normal', humidity='normal', tuber='wrinkles', type_tuber='dry', tuber_color='brown')))
    def early_blight(self):
        print("the plant has early blight.")


'''****************************************************Welcome to PyDoc**********************************************'''


class symptom(Fact):
    pass


sympts = []
clowsugar = ["shakiness", "hunger", "sweating", "headache", "pale"]
chighsugar = ["thirst", "blurred vision", "headache", "dry mouth", "smelling breath", "shortnessof breath"]
cold = ["harsh cough", "runny nose"]
measeles = ["brownish-pink", "rash", "high and fast temperature", "bloodshot eyes", "white spots inside cheek"]
mumps = ["has moderate temperature", "saliva is not normal", "swollen lymph nodes in neck", "mouth dry then"]
flu = ["conjunctives", "strong body aches", "weakness, vomiting", "sore throat and sneezing"]


class patient(KnowledgeEngine):

    @Rule(symptom(age="child", ls=L(3) | L(4) | L(5)))
    def low_sugar(self):
        print("you have signs of low sugar")
        # yield symptom(hasLowSugar="yes")

        dp = input("does/did any of your parents have diabetes?")
        if dp == "y":
            print("you have diabetes")

    @Rule(symptom(age="child", hs=L(3) | L(4) | L(5) | L(6)))
    def high_sugar(self):
        print("you have signs of high sugar")

    @Rule(symptom(clds=L(2)))
    def cold_signs(self):
        print("you have signs of cold")
        if len(set(sympts) & set(measeles)) == 5:
            print("you have measles")

    @Rule(symptom(age="child", mmps=L(4)))
    def has_mumps(self):
        print("you have mumps")

    @Rule(symptom(age="child", fl=L(5)))
    def ch_flu(self):
        print("you have child flu")

    @Rule(symptom(age="adult", fl=L(5)))
    def ch_flu(self):
        print("you have adult flu")


def Main():
    x = input("if you want to choose pyDoc enter [1] or py_plant enter [2]")
    if x == '1':
        print("\t\tWelcome to PyDoc")
        Age = input("please enter your age\n")
        if (int)(Age) <= 5:
            status = "child"
        else:
            status = "adult"
        cont = 'y'

        while cont == 'y':
            sym = input("Tell us one of your symptoms\n")
            sympts.append(sym)
            cont = (input("if you would like to add more symptoms press y, or press any key to continue\n"))

        pat = patient()
        pat.reset()
        pat.declare(symptom(age=status, ls=len(set(sympts) & set(clowsugar)), hs=len(set(sympts) & set(chighsugar)),
                            clds=len(set(sympts) & set(cold)), msls=len(set(sympts) & set(measeles)),
                            mmps=len(set(sympts) & set(mumps)), fl=len(set(sympts) & set(flu))))
        pat.run()

    elif x == '2':
        print("\t\tWelcome to Py_plant")
        tem = input("ENTER status of temperature")
        hum = input("ENTER status of humidity")
        sh = input("ENTER shape of tuber")

        x = input("ENTER y if you want to enter type of tuber ")
        if x == 'y':
            ty = input("ENTER type of tuber")
            x = input("ENTER y if you want to enter color of tuber ")
            if x == 'y':
                col = input("ENTER color of tuber")
                p = the_plant()
                p.reset()
                p.declare(Describe(tuber=sh, temperature=tem, humidity=hum, type_tuber=ty, tuber_color=col))
                p.run()
            else:
                p = the_plant()
                p.reset()
                p.declare(Describe(tuber=sh, temperature=tem, humidity=hum, type_tuber=ty))
                p.run()
        else:
            x = input("ENTER y if you want to enter color of tuber ")
            if x == 'y':
                col = input("ENTER color of tuber")
                p = the_plant()
                p.reset()
                p.declare(Describe(tuber=sh, temperature=tem, humidity=hum, tuber_color=col))
                p.run()

while 1<145:
 Main()

