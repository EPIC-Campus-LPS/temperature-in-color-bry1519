# Temperature in Color

## Objective
1. Create a program to collect temperature data from a DHT11 sensor
2. Write to a file from inside a Python program
3. Make a graph with a line of best fit to illustrate temerature decay


## Materials

- 1 red and 1 blue 5mm LED
- 2 65 Ω (Ohm) resistors
- 7 male-to-male jumper wires

## Part 1: Blink Red, Blink Blue 

1. Create a new script, `temperature.py`, for this lab.
2. Wire a red and a blue light on two GPIO pins. Don't forget your resistors!
3. Write a short program to turn on the red light for one second, then turns on the blue light for one second. When the program is finished, both lights should be off.

- [ ] There is nothing to submit for this part.
## Part 2: Temperature Indicator
<img width="550" height="509" alt="Untitled drawing(18)" src="https://github.com/user-attachments/assets/6591a7fe-b5ff-497c-921c-abd832ad4aff" />


1. Wire your DHT11 temperature and humidity sensor using the diagram above. **Note: There are two different types of DHT11. Be careful about which one you have.** Attach the sensor to GPIO pin 16 or adjust the code accordingly.
2. Activate your virtual environment and install the necessary library with `python3 -m pip install adafruit-circuitpython-dht` in your terminal. 
3. Copy the following starter code into your program. Complete the method `to_farienheit(c)` before running. 
```python
import time
import board
import adafruit_dht
from datetime import datetime

sensor = adafruit_dht.DHT11(board.D16) # Change the pin number to the data pin of your DHT11 

print("time,celsius,fahrenheit")

def to_fahrenheit(c):
    # TODO: Assign f where f represents the Farienheit equivalent to the input Celcius c
    f = ??
    return f 

while True:
    try:
        celsius = sensor.temperature # Get the temperature in Celcius from the sensor
        fahrenheit = to_fahrenheit(celsius)
        current_time = datetime.now()
        print("{0},{1:0.1f},{2:0.1f}".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit))

		# TODO: Light up the red light when the temperature is above 72, and blue when it is below 72.
		time.sleep(3.0)
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except KeyboardInterrupt:
        GPIO.cleanup()
    except Exception as error:
        sensor.exit()
        raise error    
``` 
3. We are now going to use Python to model a piecewise function. When the temperature is over 72 degrees the red light will turn on and when the temperature is below 72 degrees the blue light will turn on. Once your program runs correctly and is outputting temperatures, combine the starter code with your LED program to turn on a red light when the temperature is above 72 degrees, and the blue light when the temperature is below 72 degrees.  

- [ ] Upload a video of your functional program.

## Part 3: Temperature Decay

1. Modify your program above to send your  output to a new file, `temperature.csv`, instead of printing to the terminal. "CSV" stands for comma separated values. Each line of your file should contain "time, temperature". Make sure your file is writing to new lines! It will not automatically add the line breaks for you! Otherwise you will have one really long line and need to split it apart. 
2. The next step is to record temperature decay of cold air. Place an ice pack on your sensor for a few minutes then remove the ice pack. The temperature should slowly rise until it returns to room temperature. 

- [ ]  Upload `temperature.csv` and your code file, `temperature.py` to your repository.
## Part 4: Plotting and Results

2. Open `temperature.csv` in Google Sheets or a similar program. Using our data, we will make two different graphs.
3. Also, open a new Markdown document to paste screenshots of your graphs and answer the following questions.
4. First, plot Celsius vs Fahrenheit. Then, add a line of best fit. Make sure to add a title and axis labels!
	1. What is the equation is the line of best fit?
	2. Why does that make sense based on what we know about Celsius and Fahrenheit? 
5. Second, plot Celsius or Fahrenheit over time. Make sure to add a title and axis labels!
	1. What kind of model best represents our data(linear, quadratic, exponential)? 
	2. What is the equation of the line of best fit?
	3. Why does this make sense for representing temperature? 

- [ ] Upload a PDF of this document to your repository
## Resources

- [DHT11/DHT22 Tutorial](https://randomnerdtutorials.com/raspberry-pi-dht11-dht22-python/)
- [Alternate Library](https://pypi.org/project/dht11/)

## Rubric 

- 6 points - All required items are present.    
- 5 points - Task was completed, but supplementary materials are weak or missing.    
    - Code is complete, but poorly communicates necessary information
- 4 points - Task was attempted, but is missing major components.    
    - Missing comments, videos/photos, or reflection questions  
- 3 points - Did not attempt or student should reattempt.  
    - Inappropriate use of AI tools.
