'''
#Multiple Inheritance ->Whatsapp Scenario ->Sendmessages,vediocall
class Messages:
    """base class-1"""
    def send_message(self):
        print("User sending messages")
class Voice_Calls:
    """base class-2"""
    def voice_call(self):
        print("User making voice calls")
class Users(Messages,Voice_Calls):
    """derived class"""
    #pass
    def video_call(self):
        print("User making video calls")
u1 = Users()
u1.voice_call()
u1.send_message()
u1.video_call()
'''
#Multilevel Inheritance ->level by level access
'''
class A:
    statement(s)....
    .................
class B:
    statement(s)...
    ................
class C:
    statement(s)...
    ...............

#Whatsapp ->User,Business User,Premium Users
class Users:
    """Base class"""
    def send_messages(self):
        print("User can send messages")
class Business_Users(Users):
    """Business User features"""
    def create_catalog(self):
        print("Catalogue creation can be done")
class Premium_Users(Business_Users):
    """Premium user features"""
    def avatars(self):
        print("User can create Avatras")
u1 = Users()
u1.send_messages()
u2 = Business_Users()
u2.send_messages()
u2.create_catalog()
u3 = Premium_Users()
u3.avatars()
u3.create_catalog()

#Hybrid Inheritance -> It is a combination of one or more types of Inheritance
#Single with Multiple Inheritance so on ...
class Users:
    """Users class with basic features"""
    def send_messages(self):
        print("User can send messages")
    def voice_calls(self):
        print("User can make voice calls")
class Notifications(Users):
    """Notifications feature"""
    def send_notifiction(self):
        print("User can receive alret notifications")
class Business_Users:
    """Business user features"""
    def catalog(self):
        print("Catalog is created")
class Premium_Users(Business_Users,Notifications):
    """Premium user features"""
    def connections(self):
        print("User can access networks")
u1 = Users()
u1.send_messages()
u1.voice_calls()
u2 = Premium_Users() #check the available
u2.connections()
u2.catalog()

#Polymorphism -> poly -> many,morp->forms
#Method Overloading,Method Overriding,Operator Overloeading
#Hotstar ->Free User,VIP User,Premium User
class Hotstar:
    """Method overloading scenario"""
    def watch(self):
        print("User has logged in")
    def watch(self,movie):
        self.movie = movie
        print(f'User started watching {self.movie}')
vishala = Hotstar()
vishala.watch("saki")

class Hotstar:
    """Method overloading with default arguments"""
    def watch(self,movie = None):
        self.movie = movie
        if self.movie == None:
            print("User logged in and in Home page")
        else:
            print(f"User watching {self.movie}")
u1 = Hotstar()
u1.watch()
u1.watch("Geetanjali")

class Hotstar:
    """MOL with *args usage"""
    def add_to_list(self,*movies):
        print(movies)
        for movie in movies:
            print(f"User is watching {movie}")
u1 = Hotstar()
u1.add_to_list("saki","Geetanjali","Bombay")

#Method Overloading with type of arguments usage
#Method Overloading with type of arguments usage
class Hotstar:
    """MOL with type of args usage"""
    def movieslist(self,content):
        self.content = content
        if isinstance(content,str):
            print(f'User is watching {self.content}')
        elif isinstance(content,list):
            print("Movie added to watch list")
            for movie in content:
                print(f'User started watching {movie}')
user = Hotstar()
#user.movieslist("Hello")
fav_movies = ['Happy Days','Maa inti Bangaram','Durandhar','Paradise']
user.movieslist(fav_movies)
#In all above cases depending on user scenario we can prefer variable
#length or type of arguments usage

#Method Overriding -> if same method is used in both base and derived class
class Freeuser:
    """Free User access"""
    def watch(self):
        print(f'Free user is watching movies with advertisements')
class VIPUser(Freeuser):
    """VIP User access"""
    def watch(self):
        print(f'VIP watching movie without Advertisements')
class PremiumUser(VIPUser):
    """Premium content access"""
    def watch(self):
        print(f'Premium user watching live content')
u1 = Freeuser()
#u1.watch()
u2 = VIPUser()
#u2.watch()
u3 = PremiumUser()
u3.watch()
#In above case usage of objects will vary,
'''
class Freeuser:
    """Free User access"""
    def watch(self):
        print(f'Free user is watching movies with advertisements')
class VIPUser(Freeuser):
    """VIP User access"""
    def watch(self):
        super().watch()
        print(f'VIP watching movie without Advertisements')
class PremiumUser(VIPUser):
    """Premium content """
    def watch(self):
        super().watch()
        print(f'Premium user watching live content')
u1 = PremiumUser()
#u1.watch()
u2 = VIPUser()
u2.watch()
