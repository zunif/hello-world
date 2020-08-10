import json
import re

class Controller:

    def __init__(self):
        self.existingUsersFile = '/Users/fer/CODE/Taller 5/data/existing_users.json'
        self.registrationFile = '/Users/fer/CODE/Taller 5/data/registration.json'
        self.loginFile = '/Users/fer/CODE/Taller 5/data/login.json'
        self.flag = False

#region Metodos LOGIN
    def load_login(self):     # muestra datos login del archivo JSON
        with open(self.loginFile) as json_file:      # lee archivo  
            player = json.load(json_file)
            username = player.get("username")
            password = player.get("password")
            print(f"Usuario: {username}")
            print(f"Password: {password}")
            return player

    def update_login(self, logindata):  # modifica datos login del archivo JSON
        with open(self.loginFile , "w") as json_file:
            json.dump(logindata, json_file)


    def validaCrendenciales(self, userLogin):
        with open(self.existingUsersFile) as json_file:      # lee archivo  
            players = json.load(json_file)
            for player in players:
                if player.get("username") == userLogin.get("username") and player.get("password") == userLogin.get("password"):
                    self.flag = True
                    break
                else:
                    self.flag = False
                
            if self.flag == True:
                print("Credenciales correctos!")
            else:
                print("Contraseña equivocada")
#endregion


#region Metodos Registrar
    def load_Registration(self):     # muestra datos registration del archivo JSON
        with open(self.registrationFile) as json_file:      # lee archivo  
            player = json.load(json_file)
            username = player.get("username")
            password = player.get("password")
            icon = player.get("icon")
            email = player.get("email")
            print(f"Usuario: {username}")
            print(f"Password: {password}")
            print(f"icon: {icon}")
            print(f"email: {email}")
            return player

    def update_Registration(self, newPlayer):  # modifica datos registration del archivo JSON
        with open(self.registrationFile , "w") as json_file:
            json.dump(newPlayer, json_file)

    def validaregistro(self, newPlayer):
        regExpEmail= '^\w+@[a-zA-Z_]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,2})?$'
        regExpUsername= '^\w+$'
        regExpPassword= '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'

        username = newPlayer.get("username")
        password = newPlayer.get("password")
        email = newPlayer.get("email")
        
        if re.match(regExpEmail,email):
            if re.match(regExpUsername,username):
                if re.match(regExpPassword,password):
                    self.flag = True
                    print("Registro Validado")
                else:
                    print("Password invalido")
            else:
                print("Username invalido")
        else:
            print("correo invalido")

    def new_players(self, newUser):
        with open(self.existingUsersFile , "w") as json_file:
            json.dump(newUser, json_file)


    def update_ExistingUsers(self, newUser):      
        with open(self.existingUsersFile, "r+") as json_file:      # lee archivo  
            players = json.load(json_file)

            username = newUser.get("username")
            password = newUser.get("password")
            newPlayer = {'username': username, 'password': password}
            
            print("-----")
            print(newPlayer)
            print("-----")
  
            players.append(newPlayer)
            json_file.seek(0)
            json.dump(players, json_file)



#endregion



#region Metodos Mostrar usuarios existentes
    def load_players(self):
        with open(self.existingUsersFile) as json_file:      # lee archivo  
            players = json.load(json_file)
            for player in players:
                print("")
                username = player.get("username")
                password = player.get("password")
                print(f"Usuario: {username}")
                print(f"Password: {password}")

#endregion
                

    def usuarioExiste(self, user):
        with open(self.existingUsersFile) as json_file:      # lee archivo  
            players = json.load(json_file)
            for player in players:
                if (player.get("username")) == (user.get("username")):
                    return True
                    break
            return False





controller = Controller()
# newUser = {'username':"Mario", 'password' : "7fdshjgbjhfs"}
# controller.load_players()
# controller.update_ExistingUsers(newUser)
# print("")
# print("---- Add an aditional user -----------")
# print("")
# controller.load_players()

# controller.update_ExistingUsers(newUser)

#region 1)  Registrar usuarios ------------------------
# controller.load_Registration()
# print("")
# registrationdata =  {'username':"FER", 'password' : "888", 'icon' : 'image225.jpg', 'email' : "fjimenez_01@hotmail.com"}
# controller.update_Registration(registrationdata)
# controller.load_Registration()
# verificar 
# newPlayer = controller.load_Registration() #usuario almacenado en el JSON Login
# print("-----")
# usuarioExiste = controller.usuarioExiste(newPlayer)
# if usuarioExiste:
#     print("Usuario YA exite")
# else:
#     print("Usuario no exite")
#     # controller.validaregistro(newPlayer)
#     # controller.update_player(newPlayer)
    #------
    # print(newPlayer)
# controller.update_player(newPlayer)

#endregion



#region 2) Mostrar login / Actualizarlos / Validar usuario ----------------------
# controller.load_login()    #muestra usuario actual con el que intentará loguearse
# print("")
# logindata =  {'username':"Fer", 'password' : "777"}
# controller.update_login(logindata)   #modifica el usuario del Json para logearse
# controller.load_login()


# verificar 
# userLogin = controller.load_login() #usuario almacenado en el JSON Login
# print("-----")

# usuarioExiste = controller.usuarioExiste(userLogin)
# if usuarioExiste:
#     print("Usuario exite")
#     controller.validaCrendenciales(userLogin)
# else:
#     print("Usuario no exite")

#endregion





#region 3) mostrar usuarios existentes ------------------------------
# controller.load_players()   
#endregion


#region Menu






# option = ""
# while option != "4":


#     print("""              **** Menu ****

#         Digite una de las siguientes opciones:

#         1) Registrar un nuevo usuario
#         2) Ingresar al sistema (Login)
#         3) Mostrar lista de usuarios existentes
#         4) Salir
#         """)

#     option = input("Opcion: ")

#     if option == "1":
#         print(option)


#     if option == "2":
#         print(option)

#     if option == "3":
#         controller.load_players() 
#         print("")
#         continuar= input("Desea volver al menu 1=Si 2=No: ")
#         if continuar == "1":
#             continue
#         else:
#             exit()   
#     if option == "4":
#         exit()
#     else:
#         print("Digite una opcion valida")

#endregion





if __name__ == "__main__":
    Controller()