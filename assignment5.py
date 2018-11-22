'''
Steven Caraballo
Assignment #5
It's alive!!
11/21/18
'''

################################################################################

class Human:
    '''This is a human being'''
    def __init__(self,name,stamina=70,hunger=70,motivation=70,knowledge=70):
        print('My name is {} and I should really start studying for my test... \n\n...nahhhhhh'.format(name))
        self.stamina = stamina
        self.hunger = hunger
        self.motivation = motivation
        self.knowledge = knowledge
        self.name = name

    def study(self):
        if (self.stamina > 50
        and self.hunger > 50
        and self.motivation > 50):
            self.stamina -= 10
            self.hunger -= 10
            self.knowledge += 10
            print(self.name + ' studied!\n')
            self.sort()
            self.stats()
        else:
            print(self.name + ' does not feel like studying right now... perhaps check his stats')

    def eat(self):
        if self.hunger != 100 and self.motivation > 60:
            self.stamina += 5
            self.hunger += 15
            self.motivation -= 5
            self.sort()
            print('{} ate food!\n'.format(self.name))
            self.stats()
        else:
            print('{} is not very hungry right now'.format(self.name))

    def sleep(self):
        if self.hunger > 40:
            self.stamina += 15
            self.hunger -= 10
            self.sort()
            print('zZzzzZZzZzzZZzZZZzz...\n')
            self.stats()
        else:
            print('{} is wayyyy to hungry to sleep... grubhub it is.'.format(self.name))

    def watch_inspirational_documentaries(self):
        if self.hunger > 40:
            self.stamina -= 5
            self.hunger -=5
            self.motivation += 10
            print('{} illegally streamed motivational videos\n'.format(self.name))
            self.sort()
            self.stats()
        else:
            print('{} is wayyyy to hungry to watch anything... he loves pizza.'.format(self.name))
    
    def sort(self):
        if self.stamina > 100:
            self.stamina = 100
        if self.hunger > 100:
            self.hunger = 100
        if self.motivation > 100:
            self.motivation = 100
        if self.knowledge > 100:
            self.knowledge = 100
        else:
            None

    def stats(self):
        print('stamina: {}'.format(self.stamina))
        print('hunger: {}'.format(self.hunger))
        print('motivation: {}'.format(self.motivation))
        print('knowledge: {}'.format(self.knowledge))

################################################################################
        
def take_test(human):
    '''Return test results'''
    total = human.stamina + human.hunger + human.motivation + human.knowledge
    status = (total/400) * 100
    if status >= 95:
        return '{} got an A+ on his python final!'.format(bob.name)
    elif status >= 90:
        return '{} got an A on his python final!'.format(bob.name)
    elif status >= 85:
        return '{} got a B+ on his python final!'.format(bob.name)
    elif status >= 80:
        return '{} got a B on his python final!'.format(bob.name)
    elif status >= 75:
        return '{} got a C+ on his python final!'.format(bob.name)
    elif status >= 70:
        return '{} got a C on his python final'.format(bob.name)
    else:
        return '{} Failed!'.format(bob.name)
    

################################################################################

bob = Human('Bob')
cindy = Human('cindy')

