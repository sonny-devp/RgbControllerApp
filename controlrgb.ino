int rled = 9;
int gled = 10;
int bled = 11;
int rled1;
int gled1;
int bled1;

void setup() {
  Serial.begin(9600);
  pinMode(rled , OUTPUT);
  pinMode(gled , OUTPUT);
  pinMode(bled , OUTPUT);
}

void loop (){
  rled1 = 0;
  gled1 = 0;
  bled1 = 0; 

if (Serial.available()>0) {
  
  rled1 = Serial.parseInt();
  gled1 = Serial.parseInt();
  bled1 = Serial.parseInt();

  selectcolor(rled1,gled1,bled1);

  if (Serial.read() == '\n') {
    rled1 = constrain(rled1, 0, 255);
    gled1 = constrain(gled1, 0, 255);
    bled1 = constrain(bled1, 0, 255); 
  }
}
  }


void selectcolor(int rlled,int glled,int blled){

  analogWrite(rled,rlled);
  analogWrite(gled,glled);
  analogWrite(bled,blled);

}