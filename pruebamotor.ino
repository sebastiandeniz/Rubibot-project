#define stepPinF 2
#define dirPinF 3
#define stepPinR 4
#define dirPinR 5
#define stepPinL 6
#define dirPinL 7
#define stepPinB 8
#define dirPinB 9
#define stepPinU 10
#define dirPinU 11
#define stepPinD 12
#define dirPinD 13
int pausa = 200;
int microseg = 1500;

void setup() {
  pinMode(stepPinF,OUTPUT);
  pinMode(dirPinF,OUTPUT);
  pinMode(stepPinR,OUTPUT);
  pinMode(dirPinR,OUTPUT);
  pinMode(stepPinL,OUTPUT);
  pinMode(dirPinL,OUTPUT);
  pinMode(stepPinB,OUTPUT);
  pinMode(dirPinB,OUTPUT);
  pinMode(stepPinU,OUTPUT);
  pinMode(dirPinU,OUTPUT);
  pinMode(stepPinD,OUTPUT);
  pinMode(dirPinD,OUTPUT);
  Serial.begin(9600);
}

void loop() {
 if (Serial.available() > 0){
  String option = Serial.readStringUntil(' ');
  if (option == "F"){
  digitalWrite(dirPinF,LOW);
    for(int x = 0; x < 50; x++){
   digitalWrite(stepPinF,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinF,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
  if (option == "F'"){
  digitalWrite(dirPinF,HIGH);
    for(int x = 0; x < 50; x++){
   digitalWrite(stepPinF,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinF,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
   if (option == "F2"){
  digitalWrite(dirPinF,LOW);
    for(int x = 0; x < 100; x++){
   digitalWrite(stepPinF,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinF,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }

  if (option == "R"){
  digitalWrite(dirPinR,LOW);
    for(int x = 0; x < 50; x++){
   digitalWrite(stepPinR,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinR,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
  if (option == "R'"){
  digitalWrite(dirPinR,HIGH);
    for(int x = 0; x < 50; x++){
   digitalWrite(stepPinR,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinR,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
   if (option == "R2"){
  digitalWrite(dirPinR,LOW);
    for(int x = 0; x < 100; x++){
   digitalWrite(stepPinR,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinR,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
  

  if (option == "L"){
  digitalWrite(dirPinL,LOW);
    for(int x = 0; x < 50; x++){
   digitalWrite(stepPinL,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinL,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
  if (option == "L'"){
  digitalWrite(dirPinL,HIGH);
    for(int x = 0; x < 50; x++){
   digitalWrite(stepPinL,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinL,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
   if (option == "L2"){
  digitalWrite(dirPinL,LOW);
    for(int x = 0; x < 100; x++){
   digitalWrite(stepPinL,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinL,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
  

  if (option == "B"){
  digitalWrite(dirPinB,LOW);
    for(int x = 0; x < 50; x++){
   digitalWrite(stepPinB,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinB,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
  if (option == "B'"){
  digitalWrite(dirPinB,HIGH);
    for(int x = 0; x < 50; x++){
   digitalWrite(stepPinB,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinB,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
   if (option == "B2"){
  digitalWrite(dirPinB,LOW);
    for(int x = 0; x < 100; x++){
   digitalWrite(stepPinB,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinB,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }


  if (option == "U"){
  digitalWrite(dirPinU,LOW);
    for(int x = 0; x < 50; x++){
   digitalWrite(stepPinU,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinU,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
  if (option == "U'"){
  digitalWrite(dirPinU,HIGH);
    for(int x = 0; x < 50; x++){
   digitalWrite(stepPinU,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinU,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
   if (option == "U2"){
  digitalWrite(dirPinU,LOW);
    for(int x = 0; x < 100; x++){
   digitalWrite(stepPinU,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinU,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }

  if (option == "D"){
  digitalWrite(dirPinD,LOW);
    for(int x = 0; x < 50; x++){
   digitalWrite(stepPinD,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinD,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
  if (option == "D'"){
  digitalWrite(dirPinD,HIGH);
    for(int x = 0; x < 50; x++){
   digitalWrite(stepPinD,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinD,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
   if (option == "D2"){
  digitalWrite(dirPinD,LOW);
    for(int x = 0; x < 100; x++){
   digitalWrite(stepPinD,HIGH);
   delayMicroseconds(microseg); //NO BAJAR DE 450
   digitalWrite(stepPinD,LOW);
   delayMicroseconds(microseg);
      }
    delay(pausa);
    }
  }
}
