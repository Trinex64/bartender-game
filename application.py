import tkinter

class Application:
    ##  Initialize Class  ##
    def __init__(self):
        # Main Window
        self.root = tkinter.Tk()
        self.root.title("Drink Maker")
        self.root.geometry("856x232")
        self.root.configure(bg="#1F1A2E")
        self.root.resizable(False, False)

        self.widgets = {}
        self.current_mixture = []
        self.current_toggled = []

        # All recipes
        self.Recipes = {  # A, B, D, F, K, 0/Ice/Aged, Mixed/Blended
            "Bad Touch": [0, 2, 2, 2, 4, 1, 1],
            "Beer": [1, 2, 1, 2, 4, 0, 1],
            "Bleeding Jane": [0, 1, 3, 3, 0, 0, 2],
            "Bloom Light": [4, 0, 1, 2, 3, 3, 1],  # Both on the rocks and aged
            "Blue Fairy": [4, 0, 0, 1, 0, 2, 1],
            "Brandtini": [6, 0, 3, 0, 1, 3, 1],  # Both on the rocks and aged
            "Cobalt Velvet": [2, 0, 0, 3, 5, 1, 1],
            "Crevice Spike": [0, 0, 2, 4, 0, 0, 2],
            "Flaming Moai": [1, 1, 2, 3, 5, 0, 1],
            "Fluffy Dream": [3, 0, 3, 0, 0, 2, 1],  # Only aged and mixed
            "Fringe Weaver": [1, 0, 0, 0, 9, 3, 1],  # Both on the rocks and aged
            "Frothy Water": [1, 1, 1, 1, 0, 3, 1],  # Both on the rocks and aged
            "Grizzly Temple": [3, 3, 3, 0, 1, 0, 2],
            "Gut Punch": [0, 5, 0, 1, 0, 3, 1],  # Both on the rocks and aged
            "Marsblast": [0, 6, 1, 4, 2, 0, 2],
            "Mercuryblast": [1, 1, 3, 3, 2, 1, 2],
            "Moonblast": [6, 0, 1, 1, 2, 1, 2],
            "Piano Man": [2, 3, 5, 5, 3, 1, 1],
            "Piano Woman": [5, 5, 2, 3, 3, 3, 1],  # Both on the rocks and aged
            "Pile Driver": [0, 3, 0, 3, 4, 0, 1],
            "Sparkle Star": [2, 0, 1, 0, 0, 2, 1],
            "Sugar Rush": [2, 0, 1, 0, 0, 0, 1],
            "Sunshine Cloud": [2, 2, 0, 0, 0, 1, 2],
            "Suplex": [0, 4, 0, 3, 3, 1, 1],
            "Zen Star": [4, 4, 4, 4, 4, 1, 1]
        }


    ##  Create Buttons  ##
    def InitializeButtons(self):
        self.CreateButton("Ice", [0,0])
        self.CreateButton("Aldehyde", [0,1], "#d21834")
        self.CreateButton("Bronson Extract", [0,2], "#f4dd4d")
        self.CreateButton("Powdered Delta", [0,3], "#88AEF6")

        self.CreateButton("Age", [1,0])
        self.CreateButton("Flanergide", [1,1], "#b0d479")
        self.CreateButton("Karmotrine", [1,3], "#98f5fc")

        self.CreateButton("Reset", [2,1], "black", "#fea142")
        self.CreateButton("Mix", [2,3], "black", "#77d96a")
        self.CreateButton("Blend", [3,3], "black", "#77d96a")


        ##  Configure button commands  ##
        self.ConfigureButton("Reset", "command", self.ResetMixture)
        self.ConfigureButton("Mix", "command", lambda: self.Mix(False))
        self.ConfigureButton("Blend", "command", lambda: self.Mix(True))
        self.ConfigureButton("Ice", "command", lambda: self.ToggleToMixture("Ice"))
        self.ConfigureButton("Age", "command", lambda: self.ToggleToMixture("Age"))

        self.ConfigureButton("Ice", "width", 5)
        self.ConfigureButton("Age", "width", 5)
        self.ConfigureButton("Reset", "width", 5)
        self.ConfigureButton("Mix", "width", 5)
        self.ConfigureButton("Blend", "width", 5)


    # Add ingredient to current_mixture
    def AddToMixture(self, name):
        if len(self.current_mixture) < 20:
            self.current_mixture.append(name)
            self.ConfigureButton(name, "text", self.current_mixture.count(name))

    # Toggle Ice/Age
    def ToggleToMixture(self, name):
        if name in self.current_toggled:
            self.current_toggled.remove(name)
            self.ConfigureButton(name, "bg", "black")
            self.ConfigureButton(name, "fg", "white")
        else:
            self.current_toggled.append(name)
            self.ConfigureButton(name, "bg", "white")
            self.ConfigureButton(name, "fg", "black")

    # Reset mixture and ingredients
    def ResetMixture(self, reset_output=True):
        for button in self.widgets:
            if reset_output and button == "Output":
                self.widgets[button].set("")
                continue
            if type(self.widgets[button]) == tkinter.StringVar:
                continue
            self.ConfigureButton(button, "text", button)

        self.ConfigureButton("Ice", "bg", "black")
        self.ConfigureButton("Ice", "fg", "white")
        self.ConfigureButton("Age", "bg", "black")
        self.ConfigureButton("Age", "fg", "white")
        self.current_mixture = []
        self.current_toggled = []

    # Mix or blend ingredients together.
    def Mix(self, blended):
        # Check if it is on the rocks, aged or both
        index_6 = 0
        if "Ice" in self.current_toggled and "Age" in self.current_toggled:
            index_6 = 3
        elif "Age" in self.current_toggled:
            index_6 = 2
        elif "Ice" in self.current_toggled:
            index_6 = 1

        temp_mixture = [
            self.current_mixture.count("Aldehyde"),
            self.current_mixture.count("Bronson Extract"),
            self.current_mixture.count("Powdered Delta"),
            self.current_mixture.count("Flanergide"),
            self.current_mixture.count("Karmotrine"),
            index_6,
            1 if not blended else 2] # 1 if not blended, 2 if it is
        
        found_drink = False

        for drink, recipe in self.Recipes.items(): 
            big_drink = [i * 2 for i in recipe][:5]
            big_drink.append(recipe[5])
            big_drink.append(recipe[6])

            if big_drink == temp_mixture:
                self.widgets["Output"].set(f"Big {drink}")
                found_drink = True
                break

            if recipe == temp_mixture:
                self.widgets["Output"].set(drink)
                found_drink = True
                break
            
        if not found_drink:
            self.widgets["Output"].set("3r?0r!")

        self.ResetMixture(False)


    ##  Creates Buttons  ##
    def CreateButton(self, text: str, grid: list, fg="white", bg="black"):

        new_button = tkinter.Button(
            self.root, text=text, fg=fg, bg=bg,
            font=("fixedsys", 17), highlightthickness=0, bd=0,
            command=lambda: self.AddToMixture(text), width=15
        )
        
        new_button.grid(row=grid[0], column=grid[1], padx=5, pady=5)
        self.widgets[text] = new_button
    
    # Change property of button
    def ConfigureButton(self, button, to, into):
        button: tkinter.Button = self.widgets[button]
        button.config({to: into})
    
    # Test fuction :)
    def DisplayButtons(self):
        print(self.widgets)

class RecipeBrowser(Application):
    def __init__(self):
        super().__init__()