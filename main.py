from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
class SaffrinoApp(App):
	pass
class Saffrino(BoxLayout):
	def increase(self):
		print "I am increasing"
	def decrease(self):
		print "I am decreasing"
	def neutral(self):
		print "I am neutral"
if __name__=="__main__":
	SaffrinoApp().run()