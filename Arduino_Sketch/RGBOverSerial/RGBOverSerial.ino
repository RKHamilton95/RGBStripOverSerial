#include <Adafruit_NeoPixel.h>
#include <EEPROM.h>
String COMMANDSTATE = "ON";
#define PIN 7 //This is the Digital Pin the RGB LEDs will be connected too
#define NUMPIXELS 16
//LED STRIP
Adafruit_NeoPixel LEDS = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
//-----------------COLORS-----------------
uint32_t red = LEDS.Color(251, 13, 5);
uint32_t orange = LEDS.Color(251, 115, 5);
uint32_t yellow = LEDS.Color(251, 244, 5);
uint32_t green = LEDS.Color(26, 251, 5);
uint32_t lightblue = LEDS.Color(5, 208, 251);
uint32_t blue = LEDS.Color(1, 35, 224);
uint32_t indigo = LEDS.Color(92, 0, 147);
uint32_t violet = LEDS.Color(224, 1, 176);
uint32_t violet2 = LEDS.Color(251, 5, 189);
uint32_t white = LEDS.Color(255, 255, 255);
//Globals
uint32_t CURRENT_COLOR = red;
int CURRENT_BRIGHTNESS = 10;
//-----------------------------------------

void setup()
{
  pinMode(PIN, OUTPUT);
  Serial.begin(9600);
  LEDS.begin();
  LEDS.setBrightness(10);
  for (int i = 0; i < NUMPIXELS; i++) {
    LEDS.setPixelColor(i, blue);
  }
  LEDS.show();
}

void loop()
{
  if (Serial.available() > 0)
  {
    inputToOutput();
  }
}

void inputToOutput()
{
  String command = Serial.readStringUntil('\n');

  if (command == "ON")
  {
    ON();
  }
  else if (command == "OFF")
  {
    OFF();
  }
  else if (command == "SOLID")
  {
    SOLID(Serial.readStringUntil('\n'));
  }
  else if (command == "BRIGHTER") {
    BRIGHTER();
  }
  else if (command == "DARKER") {
    DARKER();
  }
}



void ON() {
  LEDS.setBrightness(CURRENT_BRIGHTNESS);
  for (int i = 0; i < NUMPIXELS; i++) {
    LEDS.setPixelColor(i, CURRENT_COLOR);
  }
  LEDS.show();
}

void OFF() {
  LEDS.setBrightness(0);
  LEDS.show();
}

void SOLID(String color) {
  uint32_t colorVar = stringToColor(color);
  CURRENT_COLOR = colorVar;
  for (int i = 0; i < NUMPIXELS; i++) {
    LEDS.setPixelColor(i, colorVar);
  }
  LEDS.show();
}

void BRIGHTER() {
  if(LEDS.getBrightness()+10 < 255)
  {
    LEDS.setBrightness(LEDS.getBrightness() + 10);
    CURRENT_BRIGHTNESS = LEDS.getBrightness();
  }
  LEDS.show();
}

void DARKER()
{
  if(LEDS.getBrightness()-10 > 0)
  {
    LEDS.setBrightness(LEDS.getBrightness() - 10);
    CURRENT_BRIGHTNESS = LEDS.getBrightness();
  }
  LEDS.show();
}

uint32_t stringToColor(String color)
{
  if (color == "RED") {
    return red;
  }
  else if (color == "ORANGE") {
    return orange;
  }
  else if (color == "YELLOW") {
    return yellow;
  }
  else if (color == "GREEN") {
    return green;
  }
  else if (color == "LIGHTBLUE") {
    return lightblue;
  }
  else if (color == "BLUE") {
    return blue;
  }
  else if (color == "INDIGO") {
    return indigo;
  }
  else if (color == "WHITE") {
    return white;
  }
}
