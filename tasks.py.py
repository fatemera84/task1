# mission 1
def decrypt_clue(text):
    mysterious_text = """ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocalpassraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelielsexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorpassprintraiereprreturnuperrywhlewihyiedTruFalsNonesyncawaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutpritlnnwMapSetGetAddRemoveClearIsEmptySizeContainsKeyContainsValueeyVaePaisForachDWhilSwithCasDefaltbrakcontinueiteratoriterablecollectionsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypeerasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobservermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousprogrammingeventdrivenarchitecturefunctionalprogrammingimmutables...
quantumcomputingqubitsentanglementsuperpositionquantumalgorithmsShorsGroverquantumcryptographyquantumteleportationartificialintelligenceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepthfirstsearchbreadthfirstsearchAstaralgorithmgeneticalgorithmssimulatedannealingparticlewarmoptimizationantcolonyoptimizationmachinelearningdeeplearningunsupervisedlearningreinforcementlearningneuralnetworksconvolutionalneuralnetworksrecurrentneuralnetworkslongshorttermmemorynetworksgenerativeadversar...
blockchaintechnologydistributedledgerconsensusalgorithmsproofOfWorkproofOfStakeByzantineFaultTolerancepeer-to-peerP2PnetworkscryptographyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigitalcertificatesdigital signaturesmartcontractsdecentralizedapplicationsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNFTsnon-fungibletokensDeFidecentralizedfinancedecentralizedexchangesDEXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypoolsoraclesDAOsdecentralizedautonomousorganizati..."""


    keywords = ['if', 'for', 'else', 'elif', 'False', 'True', 'None', 'as', 'and', 'or', 'not', 'aseert', 'async','await','break','class','continue','def','del','except',
                'finally','from','in','is','import','lambda','global','nonlocal','pass','raise','return','try','while','with','yield']
    result = []
    for char in keywords:
        if char in mysterious_text:
            result.append(char)
    return result
text = """ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocalpassraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelielsexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorpassprintraiereprreturnuperrywhlewihyiedTruFalsNonesyncawaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutpritlnnwMapSetGetAddRemoveClearIsEmptySizeContainsKeyContainsValueeyVaePaisForachDWhilSwithCasDefaltbrakcontinueiteratoriterablecollectionsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypeerasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobservermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousprogrammingeventdrivenarchitecturefunctionalprogrammingimmutables...
quantumcomputingqubitsentanglementsuperpositionquantumalgorithmsShorsGroverquantumcryptographyquantumteleportationartificialintelligenceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepthfirstsearchbreadthfirstsearchAstaralgorithmgeneticalgorithmssimulatedannealingparticlewarmoptimizationantcolonyoptimizationmachinelearningdeeplearningunsupervisedlearningreinforcementlearningneuralnetworksconvolutionalneuralnetworksrecurrentneuralnetworkslongshorttermmemorynetworksgenerativeadversar...
blockchaintechnologydistributedledgerconsensusalgorithmsproofOfWorkproofOfStakeByzantineFaultTolerancepeer-to-peerP2PnetworkscryptographyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigitalcertificatesdigital signaturesmartcontractsdecentralizedapplicationsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNFTsnon-fungibletokensDeFidecentralizedfinancedecentralizedexchangesDEXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypoolsoraclesDAOsdecentralizedautonomousorganizati..."""
a = decrypt_clue(text)
print(a)



#mission 2
def solve_puzzles(puzzles):
    for char in puzzles:
        print(str(char) + " is" , bool(char))
puzzles = [ "ali", 1233, 0, "", [], {}, False, None, 0, None, -1, [1, 2, 3], {'key': 'value'}, True, ' ', '[]', '[1, 2, 3]', '{}', True, 'ali', '1234',
           1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}', True, 'ali', '1234', 1, 0.1, -0.1]
solve_puzzles(puzzles)

#mission 3_1
import time
def magic_calculate_numbers(start,end):     
    x = time.time() 
    x = x - int(x) 
    result = x * (end-start) + start 
    print(int(result))

a = int(input("enter number a:")) 
b = int(input("enter number b :"))  
r = magic_calculate_numbers(a,b)
print(r)     

#mission 3_2
import random 
import time
def exam_numbers():
    binary_numbers = [] 
    for _ in range(4):
        rand = random.randint(0,1)
        binary_numbers.append(rand)
    return binary_numbers

true_answers = 0
false_answers = 0 

start_time = time.time()
binary_numbers = exam_numbers()
decimal_number = [2 ** i for i in range(4) if binary_numbers[i] == 1] 
result = sum(decimal_number)
a = int(input("enter a decimal of numbers:"))
end_time = time.time()

if end_time - start_time >= 20 :
    print("time is over!")  
    false_answers+=1
elif a == result :
    print("your answer is true")
    true_answers+=1
else :
    print("your answer is false")
    false_answers+=1
print("ture answes:",true_answers)
print("false answes:",false_answers)

 #mission 3_3
def check_pass(username,password):

    if len(password) >= 8:
        i1 = False
        i2 = False
        i3 = False

        punctuations = "!@#$%^&*_.?/\|"

        for char in password:

            if char.isupper():
                i1 = True

            if char.islower():
                i2 = True

            if char in punctuations:
                i3 = True

        if i1 and i2 and i3:
            return username
        else:
            print("The password is incorrect!")

username_password = ("enter your username:")
password = input("enter your password:")
r = check_pass(username,password)
print(r)


#mission 4_1






















#mission 4_2

       






