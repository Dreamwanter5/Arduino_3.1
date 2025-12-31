#include <AFMotor.h>

int sensores [] = {A5,A2};
int leituras [] = {0,0};
AF_DCMotor motorE(4); //inserir a porta do motor da esquerda
AF_DCMotor motorD(3); //inserir a porta do motor da direita
bool alinhou = false;
int sE;
int sD;
void setup() {

  for (int i = 0; i<2; i++){
    pinMode(sensores[i],INPUT);
  }
   Serial.begin(9600);
   motorE.run(FORWARD);
   motorD.run(FORWARD);
}

void loop() {

    sE = digitalRead(A2);
    sD = digitalRead(A5);

    alinhou = false;
    for (int i = 0; i<2; i++){
      leituras[i] = digitalRead(sensores[i]);
      Serial.print(leituras[i]);
      Serial.print(" ");
    }
    Serial.println();

    while (alinhou == false) {
      //1 = Branco
      //0 = Preto
        if (sE == 1 && sD == 1) {
            motorD.setSpeed(200);
            motorE.setSpeed(200);
            motorD.run(FORWARD);
            motorE.run(FORWARD);
            };

        if (sE == 0 && sD == 1) {
            motorD.setSpeed(200);
            motorD.run(FORWARD);
            motorE.setSpeed(200);
            motorE.run(BACKWARD);
        };

        if (sE == 1 && sD == 0) {
            motorD.setSpeed(200);
            motorD.run(BACKWARD);
            motorE.setSpeed(200);
            motorE.run(FORWARD);
        };

        if (sD == 0 && sE == 0) {
            motorD.setSpeed(0);
            motorE.setSpeed(0);
            motorD.run(FORWARD);
            motorE.run(FORWARD);
            alinhou = true;
        };
    }

  
}