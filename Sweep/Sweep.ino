/* Sweep
 by BARRAGAN <http://barraganstudio.com> 
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/ 

#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 
Servo myservotwo; // twelve servo objects can be created on most boards
 
int pos = 0;    // variable to store the servo position 
int x = 0;
int incomingByte = 0;
void setup() 
{ 
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
  myservotwo.attach(8);
}
  
void loop() { 
  if (Serial.available() > 0) {
      // read the incoming byte:        
      if (Serial.read()==49) {                              // in steps of 1 degree 
        myservo.write(150);              // tell servo to go to position in variable 'pos' 
        myservotwo.write(150);
        delay(1250);   
        myservo.write(0); 
        myservotwo.write(0);                  
      }
  }
} 

