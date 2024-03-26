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
int pausa = 100;
int microseg = 1200;

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


// Definimos la funcion rotacion sentido horario
void rotation_C(int stepPin, int dirPin, int numSteps) {
  digitalWrite(dirPin, LOW); 
  for (int x = 0; x < numSteps; x++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(microseg);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(microseg);
  }
  delay(pausa);
}

// Definimos la funcion rotacion sentido antihorario
void rotation_CC(int stepPin, int dirPin, int numSteps) {
  digitalWrite(dirPin, HIGH); 
  for (int x = 0; x < numSteps; x++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(microseg);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(microseg);
  }
  delay(pausa);
}

int getStepPin(String option) {
  // Función para obtener el pin de paso correspondiente a la opción
  if (option == "F" || option == "F2" || option == "F'") {
    return stepPinF;
  } else if (option == "R" || option == "R2" || option == "R'") {
    return stepPinR;
  } else if (option == "L" || option == "L2" || option == "L'") {
    return stepPinL;
  } else if (option == "U" || option == "U2" || option == "U'") {
    return stepPinU;
  } else if (option == "D" || option == "D2" || option == "D'") {
    return stepPinD;
  } else if(option == "B" || option == "B2" || option == "B'"){
    return stepPinB;
  }
}

int getDirPin(String option) {
  // Función para obtener el pin de dirección correspondiente a la opción
  if (option == "F" || option == "F2" || option == "F'") {
    return dirPinF;
  } else if (option == "R" || option == "R2" || option == "R'") {
    return dirPinR;
  } else if (option == "L" || option == "L2" || option == "L'") {
    return dirPinL;
  } else if (option == "U" || option == "U2" || option == "U'") {
    return dirPinU;
  } else if (option == "D" || option == "D2" || option == "D'") {
    return dirPinD;
  } else if(option == "B" || option == "B2" || option == "B'"){
    return dirPinB;
  }
}

void loop() {
  if (Serial.available() > 0){
    String option = Serial.readStringUntil(' ');
    // Movimientos simples
    if (option == "F" | option == "B" | option == "R" | option == "L" | option == "U" | option == "D") {
      rotation_C(getStepPin(option), getDirPin(option), 50);
    } else if (option == "F2" | option == "B2" | option == "R2" | option == "L2" | option == "U2" | option == "D2") {
      rotation_C(getStepPin(option), getDirPin(option), 100);
    } else if  (option == "F'" | option == "B'" | option == "R'" | option == "L'" | option == "U'" | option == "D'"){
      rotation_CC(getStepPin(option), getDirPin(option), 50);
    }
    
    // Movimientos dobles (Mover caras opuestas de forma simultanea)
    if (option == "FB" || option == "BF") {
      digitalWrite(dirPinF, LOW);
      digitalWrite(dirPinB, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinF, HIGH);
        digitalWrite(stepPinB, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinF, LOW);
        digitalWrite(stepPinB, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "RL" || option == "LR") {
      digitalWrite(dirPinR, LOW);
      digitalWrite(dirPinL, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinR, HIGH);
        digitalWrite(stepPinL, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinR, LOW);
        digitalWrite(stepPinL, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "UD" || option == "DU") {
      digitalWrite(dirPinU, LOW);
      digitalWrite(dirPinD, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinU, HIGH);
        digitalWrite(stepPinD, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinU, LOW);
        digitalWrite(stepPinD, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "FB'" || option == "B'F") {
      digitalWrite(dirPinF, LOW);
      digitalWrite(dirPinB, HIGH);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinF, HIGH);
        digitalWrite(stepPinB, HIGH); 
        delayMicroseconds(microseg);
        digitalWrite(stepPinF, LOW);
        digitalWrite(stepPinB, LOW); 
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "F'B" || option == "BF'") {
      digitalWrite(dirPinF, HIGH);
      digitalWrite(dirPinB, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinF, HIGH);
        digitalWrite(stepPinB, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinF, LOW);
        digitalWrite(stepPinB, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "RL'" || option == "L'R") {
        digitalWrite(dirPinR, LOW);
        digitalWrite(dirPinL, HIGH);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinR, HIGH);
        digitalWrite(stepPinL, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinR, LOW);
        digitalWrite(stepPinL, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "R'L" || option == "LR'") {
      digitalWrite(dirPinR, HIGH);
      digitalWrite(dirPinL, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinR, HIGH);
        digitalWrite(stepPinL, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinR, LOW);
        digitalWrite(stepPinL, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "UD'" || option == "D'U") {
      digitalWrite(dirPinU, LOW);
      digitalWrite(dirPinD, HIGH);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinU, HIGH);
        digitalWrite(stepPinD, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinU, LOW);
        digitalWrite(stepPinD, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "U'D" || option == "DU'") {
      digitalWrite(dirPinU, HIGH);
      digitalWrite(dirPinD, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinU, HIGH);
        digitalWrite(stepPinD, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinU, LOW);
        digitalWrite(stepPinD, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "F'B'" || option == "B'F'") {
      digitalWrite(dirPinF, HIGH);
      digitalWrite(dirPinB, HIGH);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinF, HIGH);
        digitalWrite(stepPinB, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinF, LOW);
        digitalWrite(stepPinB, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "R'L'" || option == "L'R'") {
      digitalWrite(dirPinR, HIGH);
      digitalWrite(dirPinL, HIGH);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinR, HIGH);
        digitalWrite(stepPinL, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinR, LOW);
        digitalWrite(stepPinL, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "U'D'" || option == "D'U'") {
      digitalWrite(dirPinU, HIGH);
      digitalWrite(dirPinD, HIGH);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinU, HIGH);
        digitalWrite(stepPinD, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinU, LOW);
        digitalWrite(stepPinD, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "FB2" || option == "B2F") {
      digitalWrite(dirPinF, LOW);
      digitalWrite(dirPinB, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinF, HIGH);
        digitalWrite(stepPinB, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinF, LOW);
        digitalWrite(stepPinB, LOW);
        delayMicroseconds(microseg);
      }
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinB, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinB, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "BF2" || option == "F2B") {
      digitalWrite(dirPinF, LOW);
      digitalWrite(dirPinB, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinF, HIGH);
        digitalWrite(stepPinB, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinF, LOW);
        digitalWrite(stepPinB, LOW);
        delayMicroseconds(microseg);
      }
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinF, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinF, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "RL2" || option == "L2R") {
      digitalWrite(dirPinR, LOW);
      digitalWrite(dirPinL, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinR, HIGH);
        digitalWrite(stepPinL, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinR, LOW);
        digitalWrite(stepPinL, LOW);
        delayMicroseconds(microseg);
      }
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinL, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinL, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "LR2" || option == "R2L") {
      digitalWrite(dirPinL, LOW);
      digitalWrite(dirPinR, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinL, HIGH);
        digitalWrite(stepPinR, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinL, LOW);
        digitalWrite(stepPinR, LOW);
        delayMicroseconds(microseg);
      }
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinR, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinR, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "UD2" || option == "D2U") {
      digitalWrite(dirPinU, LOW);
      digitalWrite(dirPinD, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinU, HIGH);
        digitalWrite(stepPinD, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinU, LOW);
        digitalWrite(stepPinD, LOW);
        delayMicroseconds(microseg);
      }
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinD, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinD, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "DU2" || option == "U2D") {
      digitalWrite(dirPinD, LOW);
      digitalWrite(dirPinU, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinD, HIGH);
        digitalWrite(stepPinU, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinD, LOW);
        digitalWrite(stepPinU, LOW);
        delayMicroseconds(microseg);
      }
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinU, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinU, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "F'B2" || option == "B2F'") {
      digitalWrite(dirPinF, HIGH);
      digitalWrite(dirPinB, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinF, HIGH);
        digitalWrite(stepPinB, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinF, LOW);
        digitalWrite(stepPinB, LOW);
        delayMicroseconds(microseg);
      }
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinB, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinB, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "B'F2" || option == "F2B'") {
      digitalWrite(dirPinF, LOW);
      digitalWrite(dirPinB, HIGH);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinF, HIGH);
        digitalWrite(stepPinB, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinF, LOW);
        digitalWrite(stepPinB, LOW);
        delayMicroseconds(microseg);
      }
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinF, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinF, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "R'L2" || option == "L2R'") {
      digitalWrite(dirPinR, HIGH);
      digitalWrite(dirPinL, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinR, HIGH);
        digitalWrite(stepPinL, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinR, LOW);
        digitalWrite(stepPinL, LOW);
        delayMicroseconds(microseg);
      }
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinL, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinL, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "L'R2" || option == "R2L'") {
      digitalWrite(dirPinL, HIGH);
      digitalWrite(dirPinR, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinL, HIGH);
        digitalWrite(stepPinR, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinL, LOW);
        digitalWrite(stepPinR, LOW);
        delayMicroseconds(microseg);
      }
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinR, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinR, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "U'D2" || option == "D2U'") {
      digitalWrite(dirPinU, HIGH);
      digitalWrite(dirPinD, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinU, HIGH);
        digitalWrite(stepPinD, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinU, LOW);
        digitalWrite(stepPinD, LOW);
        delayMicroseconds(microseg);
      }
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinD, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinD, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "D'U2" || option == "U2D'") {
      digitalWrite(dirPinD, HIGH);
      digitalWrite(dirPinU, LOW);
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinD, HIGH);
        digitalWrite(stepPinU, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinD, LOW);
        digitalWrite(stepPinU, LOW);
        delayMicroseconds(microseg);
      }
      for (int x = 0; x < 50; x++) {
        digitalWrite(stepPinU, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinU, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "F2B2" || option == "B2F2") {
      digitalWrite(dirPinF, LOW);
      digitalWrite(dirPinB, LOW);
      for (int x = 0; x < 100; x++) {
        digitalWrite(stepPinF, HIGH);
        digitalWrite(stepPinB, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinF, LOW);
        digitalWrite(stepPinB, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } else if (option == "R2L2" || option == "L2R2") {
      digitalWrite(dirPinR, LOW);
      digitalWrite(dirPinL, LOW);
      for (int x = 0; x < 100; x++) {
        digitalWrite(stepPinR, HIGH);
        digitalWrite(stepPinL, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinR, LOW);
        digitalWrite(stepPinL, LOW);
        delayMicroseconds(microseg);
      } 
      delay(pausa);
    } else if (option == "U2D2" || option == "D2U2") {
      digitalWrite(dirPinU, LOW);
      digitalWrite(dirPinD, LOW);
      for (int x = 0; x < 100; x++) {
        digitalWrite(stepPinU, HIGH);
        digitalWrite(stepPinD, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPinU, LOW);
        digitalWrite(stepPinD, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa);
    } 
  }
}
