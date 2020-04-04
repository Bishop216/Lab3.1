import kivy.app
import kivy.uix.boxlayout
import kivy.uix.textinput
import kivy.uix.label
import kivy.uix.button
import math

class App(kivy.app.App):
    def build_application(self):
        self.textInput = kivy.uix.textinput.TextInput()
        self.label = kivy.uix.label.Label(text="Введите число")
        self.button = kivy.uix.button.Button(text="Факторизация")
        self.button.bind(on_press=self.displayMessage)
        self.boxLayout = kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        self.boxLayout.add_widget(self.textInput)
        self.boxLayout.add_widget(self.label)
        self.boxLayout.add_widget(self.button)

        return self.boxLayout

    def Message(self, btn):
        input = self.textInput.text
        if input.isdigit():
            F, S = self.factorization(int(input))
            self.label.text = f"n = {int(input)}.\nF = {F}.\nS = {S}."
        else:
            self.label.text = "Введите число"

    def factorization(self, n):
        s = math.ceil(math.sqrt(n))
        k = 0
        while True:
            x = s + k
            y_2 = x**2 - n
            y = int(math.sqrt(y_2))

            if y*y == y_2:
                break
            elif x > (n+1) / 2:
                x, y = 0, 0
                break
            
            k += 1
        
        p = x + y
        q = x - y
        return p, q


if __name__ == "__main__":
    app = App()
    app.run()
