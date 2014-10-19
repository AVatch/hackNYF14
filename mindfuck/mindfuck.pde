import processing.serial.*;

Serial serial;
int lf = 10; // ASCII linefeed
String inString;
PrintWriter output;

void setup(){
  // Create output file
  output = createWriter("brain_activity.txt");
  
  // List all availible serial ports
  println("Listening on Port:");
  println(Serial.list()[3]); // User port 3
  
  // Define serial port to listent to
  serial = new Serial(this, Serial.list()[3], 9600);
  serial.bufferUntil(lf);
}

void draw(){
//  point(mouseX, mouseY);
//  output.println(mouseX);
  
  output.println(inString); 
}

void serialEvent(Serial p){
  inString = p.readString();
}

void keyPressed(){
  output.flush();
  output.close();
  exit();
}
