#include <Adafruit_NeoPixel.h>
#include <EEPROM.h>
String COMMANDSTATE = "ON";
#define PIN 7 //This is the Digital Pin the RGB LEDs will be connected too
#define NUMPIXELS 16
//LED STRIP
Adafruit_NeoPixel LEDS = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

//EEPROM FUNCTIONS
void EEPROMWritelong(int address, long value)
{
  //Decomposition from a long to 4 bytes by using bitshift.
  //One = Most significant -> Four = Least significant byte
  byte four = (value & 0xFF);
  byte three = ((value >> 8) & 0xFF);
  byte two = ((value >> 16) & 0xFF);
  byte one = ((value >> 24) & 0xFF);

  //Write the 4 bytes into the eeprom memory.
  EEPROM.write(address, four);
  EEPROM.write(address + 1, three);
  EEPROM.write(address + 2, two);
  EEPROM.write(address + 3, one);
}

long EEPROMReadlong(long address)
{
  //Read the 4 bytes from the eeprom memory.
  long four = EEPROM.read(address);
  long three = EEPROM.read(address + 1);
  long two = EEPROM.read(address + 2);
  long one = EEPROM.read(address + 3);

  //Return the recomposed long by using bitshift.
  return ((four << 0) & 0xFF) + ((three << 8) & 0xFFFF) + ((two << 16) & 0xFFFFFF) + ((one << 24) & 0xFFFFFFFF);
}

//This function will write a 2 byte integer to the eeprom at the specified address and address + 1
void EEPROMWriteInt(int p_address, int p_value)
{
  byte lowByte = ((p_value >> 0) & 0xFF);
  byte highByte = ((p_value >> 8) & 0xFF);

  EEPROM.write(p_address, lowByte);
  EEPROM.write(p_address + 1, highByte);
}

//This function will read a 2 byte integer from the eeprom at the specified address and address + 1
unsigned int EEPROMReadInt(int p_address)
{
  byte lowByte = EEPROM.read(p_address);
  byte highByte = EEPROM.read(p_address + 1);

  return ((lowByte << 0) & 0xFF) + ((highByte << 8) & 0xFF00);
}

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
uint32_t CURRENT_COLOR = EEPROMReadlong(1);
int CURRENT_BRIGHTNESS = EEPROMReadInt(20);
//-----------------------------------------

void setup()
{
  pinMode(PIN, OUTPUT);
  Serial.begin(9600);
  LEDS.begin();
  LEDS.setBrightness(CURRENT_BRIGHTNESS);
  for (int i = 0; i < NUMPIXELS; i++) {
    LEDS.setPixelColor(i, CURRENT_COLOR);
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
  if (CURRENT_BRIGHTNESS == 0) {
    LEDS.setBrightness(10);
    CURRENT_BRIGHTNESS = LEDS.getBrightness();
    EEPROMWriteInt(20, CURRENT_BRIGHTNESS);
  }
  for (int i = 0; i < NUMPIXELS; i++) {
    LEDS.setPixelColor(i, CURRENT_COLOR);
  }
  LEDS.show();
}

void OFF() {
  LEDS.setBrightness(0);
  CURRENT_BRIGHTNESS = LEDS.getBrightness();
  EEPROMWriteInt(20, CURRENT_BRIGHTNESS);
  LEDS.show();
}

void SOLID(String color) {
  uint32_t colorVar = stringToColor(color);
  writeColorToEEPROM(color);
  CURRENT_COLOR = colorVar;
  for (int i = 0; i < NUMPIXELS; i++) {
    LEDS.setPixelColor(i, colorVar);
  }
  LEDS.show();
}

void BRIGHTER() {
  if (LEDS.getBrightness() + 10 < 255)
  {
    LEDS.setBrightness(LEDS.getBrightness() + 10);
    CURRENT_BRIGHTNESS = LEDS.getBrightness();
    EEPROMWriteInt(20, CURRENT_BRIGHTNESS);
  }
  LEDS.show();
}

void DARKER()
{
  if (LEDS.getBrightness() - 10 > 0)
  {
    LEDS.setBrightness(LEDS.getBrightness() - 10);
    CURRENT_BRIGHTNESS = LEDS.getBrightness();
    EEPROMWriteInt(20, CURRENT_BRIGHTNESS);
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

void writeColorToEEPROM(String color) {
  EEPROMWritelong(1, stringToColor(color));
}
