void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 baud rate.
  pinMode(A0, INPUT);  // Set A0 as an input for joystick X-axis.
  pinMode(A1, INPUT);  // Set A1 as an input for joystick Y-axis.
}

void loop() {
 float xPosition = (analogRead(A0)/ 1023.0);  // Read the analog value from pin A0
  float yPosition = (analogRead(A1)/ 1023.0);  // Read the analog value from pin A1
  Serial.print(map(xPosition*100,0,100, 125, 375));
  Serial.print(",");
  Serial.println(map(yPosition*100,0,100, 375, 125));        
              
}
