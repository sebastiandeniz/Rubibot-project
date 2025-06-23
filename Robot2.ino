#include <TM1637Display.h>

#define stepPin 12
#define dirPinF 13
#define dirPinR 23
#define dirPinL 22
#define dirPinB 21
#define dirPinU 19
#define dirPinD 18
#define enableF 32
#define enableR 33
#define enableL 25
#define enableB 26
#define enableU 27
#define enableD 14
#define CLK 2
#define DIO 4
int pausa_mov = 10;
int pausa_enable = 10;
int microseg = 600;
bool counting = false;
unsigned long startTime = 0;
unsigned long elapsedTime = 0;



TM1637Display display(CLK, DIO);


void setup() {
  pinMode(enableF, OUTPUT);
  pinMode(enableR, OUTPUT);
  pinMode(enableL, OUTPUT);
  pinMode(enableB, OUTPUT);
  pinMode(enableU, OUTPUT);
  pinMode(enableD, OUTPUT);
  digitalWrite(enableF, HIGH);
  digitalWrite(enableR, HIGH);
  digitalWrite(enableL, HIGH);
  digitalWrite(enableB, HIGH);
  digitalWrite(enableU, HIGH);
  digitalWrite(enableD, HIGH);
  pinMode(stepPin, OUTPUT);
  pinMode(dirPinF, OUTPUT);
  pinMode(dirPinR, OUTPUT);
  pinMode(dirPinL, OUTPUT);
  pinMode(dirPinB, OUTPUT);
  pinMode(dirPinU, OUTPUT);
  pinMode(dirPinD, OUTPUT);
  Serial.begin(115200);
  display.setBrightness(0x0f);
  display.clear();
}

void loop() {
  if (Serial.available() > 0) {
    String option = Serial.readStringUntil(' ');
    if (option == "start") {
      startTime = millis();
      counting = true;
      Serial.println("Cronómetro iniciado.");
    } else if (option == "stop" && counting) {
      elapsedTime = millis() - startTime;
      counting = false;
      Serial.print("Tiempo final: ");
      Serial.print(elapsedTime / 1000);  // Segundos
      Serial.print(".");
      Serial.println(elapsedTime % 1000);  // Milisegundos

      // Mostrar en la TM1637 en formato S.mmm
      int display_value = (elapsedTime / 1000) * 1000 + (elapsedTime % 1000);
      display.showNumberDecEx(display_value, 0b10000000, true, 4, 0);
    } else if (option == "0") {
      display.showNumberDec(0, true);
    }
    if (option == "F") {
      digitalWrite(enableF, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinF, LOW);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableF, HIGH);
      delay(pausa_mov);
    }
    if (option == "F'") {
      digitalWrite(enableF, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinF, HIGH);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableF, HIGH);
      delay(pausa_mov);
    }
    if (option == "F2") {
      digitalWrite(enableF, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinF, LOW);
      for (int x = 0; x < 99; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableF, HIGH);
      delay(pausa_mov);
    }

    if (option == "R") {
      digitalWrite(enableR, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinR, LOW);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableR, HIGH);
      delay(pausa_mov);
    }
    if (option == "R'") {
      digitalWrite(enableR, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinR, HIGH);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableR, HIGH);
      delay(pausa_mov);
    }
    if (option == "R2") {
      digitalWrite(enableR, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinR, LOW);
      for (int x = 0; x < 99; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableR, HIGH);
      delay(pausa_mov);
    }


    if (option == "L") {
      digitalWrite(enableL, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinL, LOW);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableL, HIGH);
      delay(pausa_mov);
    }
    if (option == "L'") {
      digitalWrite(enableL, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinL, HIGH);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableL, HIGH);
      delay(pausa_mov);
    }
    if (option == "L2") {
      digitalWrite(enableL, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinL, LOW);
      for (int x = 0; x < 99; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableL, HIGH);
      delay(pausa_mov);
    }


    if (option == "B") {
      digitalWrite(enableB, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinB, LOW);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableB, HIGH);
      delay(pausa_mov);
    }
    if (option == "B'") {
      digitalWrite(enableB, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinB, HIGH);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableB, HIGH);
      delay(pausa_mov);
    }
    if (option == "B2") {
      digitalWrite(enableB, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinB, LOW);
      for (int x = 0; x < 99; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableB, HIGH);
      delay(pausa_mov);
    }


    if (option == "U") {
      digitalWrite(enableU, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinU, LOW);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableU, HIGH);
      delay(pausa_mov);
    }
    if (option == "U'") {
      digitalWrite(enableU, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinU, HIGH);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableU, HIGH);
      delay(pausa_mov);
    }
    if (option == "U2") {
      digitalWrite(enableU, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinU, LOW);
      for (int x = 0; x < 99; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableU, HIGH);
      delay(pausa_mov);
    }

    if (option == "D") {
      digitalWrite(enableD, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinD, LOW);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableD, HIGH);
      delay(pausa_mov);
    }
    if (option == "D'") {
      digitalWrite(enableD, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinD, HIGH);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableD, HIGH);
      delay(pausa_mov);
    }
    if (option == "D2") {
      digitalWrite(enableD, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinD, LOW);
      for (int x = 0; x < 99; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);  //NO BAJAR DE 449
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableD, HIGH);
      delay(pausa_mov);
    }
    if (option == "FB" || option == "BF") {
      digitalWrite(enableF, LOW);
      digitalWrite(enableB, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinF, LOW);
      digitalWrite(dirPinB, LOW);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableF, HIGH);
      digitalWrite(enableB, HIGH);
      delay(pausa_mov);
    } else if (option == "RL" || option == "LR") {
      digitalWrite(enableR, LOW);
      digitalWrite(enableL, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinR, LOW);
      digitalWrite(dirPinL, LOW);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableR, HIGH);
      digitalWrite(enableL, HIGH);
      delay(pausa_mov);
    } else if (option == "UD" || option == "DU") {
      digitalWrite(enableU, LOW);
      digitalWrite(enableD, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinU, LOW);
      digitalWrite(dirPinD, LOW);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableU, HIGH);
      digitalWrite(enableD, HIGH);
      delay(pausa_mov);
    }
    if (option == "FB'" || option == "B'F") {
      digitalWrite(enableF, LOW);
      digitalWrite(enableB, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinF, LOW);
      digitalWrite(dirPinB, HIGH);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);  // Mantener HIGH antes de delay
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);  // Mantener LOW después de delay
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableF, HIGH);
      digitalWrite(enableB, HIGH);
      delay(pausa_mov);
    } else if (option == "F'B" || option == "BF'") {
      digitalWrite(enableF, LOW);
      digitalWrite(enableB, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinF, HIGH);
      digitalWrite(dirPinB, LOW);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableF, HIGH);
      digitalWrite(enableB, HIGH);
      delay(pausa_mov);
    } else if (option == "RL'" || option == "L'R") {
      digitalWrite(enableR, LOW);
      digitalWrite(enableL, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinR, LOW);
      digitalWrite(dirPinL, HIGH);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableR, HIGH);
      digitalWrite(enableL, HIGH);
      delay(pausa_mov);
    } else if (option == "R'L" || option == "LR'") {
      digitalWrite(enableR, LOW);
      digitalWrite(enableL, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinR, HIGH);
      digitalWrite(dirPinL, LOW);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableR, HIGH);
      digitalWrite(enableL, HIGH);
      delay(pausa_mov);
    } else if (option == "UD'" || option == "D'U") {
      digitalWrite(enableU, LOW);
      digitalWrite(enableD, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinU, LOW);
      digitalWrite(dirPinD, HIGH);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableU, HIGH);
      digitalWrite(enableD, HIGH);
      delay(pausa_mov);
    } else if (option == "U'D" || option == "DU'") {
      digitalWrite(enableU, LOW);
      digitalWrite(enableD, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinU, HIGH);
      digitalWrite(dirPinD, LOW);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableU, HIGH);
      digitalWrite(enableD, HIGH);
      delay(pausa_mov);
    }
    if (option == "F'B'" || option == "B'F'") {
      digitalWrite(enableF, LOW);
      digitalWrite(enableB, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinF, HIGH);
      digitalWrite(dirPinB, HIGH);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableF, HIGH);
      digitalWrite(enableB, HIGH);
      delay(pausa_mov);
    }
    if (option == "R'L'" || option == "L'R'") {
      digitalWrite(enableR, LOW);
      digitalWrite(enableL, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinR, HIGH);
      digitalWrite(dirPinL, HIGH);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableR, HIGH);
      digitalWrite(enableL, HIGH);
      delay(pausa_mov);
    } else if (option == "U'D'" || option == "D'U'") {
      digitalWrite(enableU, LOW);
      digitalWrite(enableD, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinU, HIGH);
      digitalWrite(dirPinD, HIGH);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableU, HIGH);
      digitalWrite(enableD, HIGH);
      delay(pausa_mov);
    }
    if (option == "FB2" || option == "B2F") {
      digitalWrite(enableF, LOW);
      digitalWrite(enableB, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinF, LOW);
      digitalWrite(dirPinB, LOW);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableF, HIGH);
      delay(pausa_mov);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableB, HIGH);
      delay(pausa_mov);
    }
    if (option == "BF2" || option == "F2B") {
      digitalWrite(enableF, LOW);
      digitalWrite(enableB, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinF, LOW);
      digitalWrite(dirPinB, LOW);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableB, HIGH);
      delay(pausa_mov);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableF, HIGH);
      delay(pausa_mov);
    }
    if (option == "RL2" || option == "L2R") {
      digitalWrite(enableR, LOW);
      digitalWrite(enableL, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinR, LOW);
      digitalWrite(dirPinL, LOW);

      // Movimiento doble (RL2)
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableR, HIGH);
      delay(pausa_mov);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableL, HIGH);
      delay(pausa_mov);
    } else if (option == "LR2" || option == "R2L") {
      digitalWrite(enableR, LOW);
      digitalWrite(enableL, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinL, LOW);
      digitalWrite(dirPinR, LOW);

      // Movimiento doble (LR2)
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableL, HIGH);
      delay(pausa_mov);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableR, HIGH);
      delay(pausa_mov);
    } else if (option == "UD2" || option == "D2U") {
      digitalWrite(enableU, LOW);
      digitalWrite(enableD, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinU, LOW);
      digitalWrite(dirPinD, LOW);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableU, HIGH);
      delay(pausa_enable);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableD, HIGH);
      delay(pausa_mov);
    } else if (option == "DU2" || option == "U2D") {
      digitalWrite(enableU, LOW);
      digitalWrite(enableD, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinD, LOW);
      digitalWrite(dirPinU, LOW);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableD, HIGH);
      delay(pausa_enable);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableU, HIGH);
      delay(pausa_mov);
    }
    if (option == "F'B2" || option == "B2F'") {
      digitalWrite(enableF, LOW);
      digitalWrite(enableB, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinF, HIGH);
      digitalWrite(dirPinB, LOW);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableF, HIGH);
      delay(pausa_mov);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableB, HIGH);
      delay(pausa_mov);
    }
    if (option == "B'F2" || option == "F2B'") {
      digitalWrite(enableF, LOW);
      digitalWrite(enableB, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinF, LOW);
      digitalWrite(dirPinB, HIGH);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableB, HIGH);
      delay(pausa_mov);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableF, HIGH);
      delay(pausa_mov);
    }
    if (option == "R'L2" || option == "L2R'") {
      digitalWrite(enableR, LOW);
      digitalWrite(enableL, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinR, HIGH);
      digitalWrite(dirPinL, LOW);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableR, HIGH);
      delay(pausa_mov);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableL, HIGH);
      delay(pausa_mov);
    } else if (option == "L'R2" || option == "R2L'") {
      digitalWrite(enableR, LOW);
      digitalWrite(enableL, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinL, HIGH);
      digitalWrite(dirPinR, LOW);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableL, HIGH);
      delay(pausa_mov);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableR, HIGH);
      delay(pausa_mov);
    } else if (option == "U'D2" || option == "D2U'") {
      digitalWrite(enableU, LOW);
      digitalWrite(enableD, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinU, HIGH);
      digitalWrite(dirPinD, LOW);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableU, HIGH);
      delay(pausa_mov);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableD, HIGH);
      delay(pausa_mov);
    } else if (option == "D'U2" || option == "U2D'") {
      digitalWrite(enableU, LOW);
      digitalWrite(enableD, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinD, HIGH);
      digitalWrite(dirPinU, LOW);

      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableD, HIGH);
      delay(pausa_mov);
      for (int x = 0; x < 49; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableU, HIGH);
      delay(pausa_mov);
    }
    if (option == "F2B2" || option == "B2F2") {
      digitalWrite(enableF, LOW);
      digitalWrite(enableB, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinF, LOW);
      digitalWrite(dirPinB, LOW);

      for (int x = 0; x < 99; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableF, HIGH);
      digitalWrite(enableB, HIGH);
      delay(pausa_mov);
    } else if (option == "R2L2" || option == "L2R2") {
      digitalWrite(enableR, LOW);
      digitalWrite(enableL, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinR, LOW);
      digitalWrite(dirPinL, LOW);

      for (int x = 0; x < 99; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableR, HIGH);
      digitalWrite(enableL, HIGH);
      delay(pausa_mov);
    } else if (option == "U2D2" || option == "D2U2") {
      digitalWrite(enableU, LOW);
      digitalWrite(enableD, LOW);
      delay(pausa_enable);
      digitalWrite(dirPinU, LOW);
      digitalWrite(dirPinD, LOW);

      for (int x = 0; x < 99; x++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(microseg);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(microseg);
      }
      delay(pausa_enable);
      digitalWrite(enableU, HIGH);
      digitalWrite(enableD, HIGH);
      delay(pausa_mov);
    }
  }
}
