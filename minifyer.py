import datetime
print("---------------------------------------------------------")
mydt = datetime.datetime.now()
print("welcome to minify for CSS/SASS/LESS/STYLUS")
print("make sure file path is exist!")
print("Copyright (c) " + mydt.strftime("%Y") + " Suresh. P \n")
ask_it = str(input("enter the file path to minify: \n".upper()))
css_save = []

try:
	with open(ask_it) as css:
				for source in css:
					trimed = source.strip()
					css_save.append(trimed)
except IOError:
	print("File doesn't exist")
finally:
	one_line_css = ''.join(css_save)

def tickornot():
			if '.css' in ask_it:
				return "✓"
			if '.scss' in ask_it:
				return "✓"
			if '.sass' in ask_it:
				return "✓"
			if '.styl' in ask_it:
				return "✓"
			if '.less' in ask_it:
				return "✓"
			else:
				return "x"

def say_file_paths():
	try:
			if '.css' in ask_it:
				return ask_it.replace(".css",".min.css")
			if '.scss' in ask_it:
				return ask_it.replace(".scss",".min.scss")
			if '.sass' in ask_it:
				return ask_it.replace(".sass",".min.sass")
			if '.styl' in ask_it:
				return ask_it.replace(".styl",".min.styl")
			if '.less' in ask_it:
				return ask_it.replace(".less",".min.less")
	except:
		pass
	
	
def pathorerror():
			if str(say_file_paths()) == 'None':
					return "Error: \n"
			if str(say_file_paths()):
				return "PATH: "
				
def comp():
				if str(say_file_paths()) == 'None':
					return "your file not based by minifyer \n only support css/sass/stylus/less \n"
				if str(say_file_paths()):
					return say_file_paths()
					
def successornot():
				if str(say_file_paths()) == 'None':
					return "failed"
				if str(say_file_paths()):
					return "completed"
								
with open(str(say_file_paths()),"w+") as mm:
			t = one_line_css.replace(" "," ")
			print(t, file=mm)
			print(" ")
			print("file-format-check:", tickornot())
			print(str(pathorerror()), comp())
			print("STATUS: ", successornot())
print(" ")
