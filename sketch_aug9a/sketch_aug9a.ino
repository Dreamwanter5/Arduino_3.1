#include <AFMotor.h>
AF_DCMotor motorE(4); //inserir a porta do motor da esquerda
AF_DCMotor motorD(3); //inserir a porta do motor da direita
int s1 = A5;
int s2 = A3;
int s3 = A4;
int s4 = A2;
int s5 = A1;

int vS1 = 0;
int vS2 = 0;
int vS3 = 0;
int vS4 = 0;
int vS5 = 0;

// após verificar o funcionamento do seu sensor, defina eles nas variáveis PISTA e LINHA abaixo:


void setup() {
  
   motorD.setSpeed(50);
   motorE.setSpeed(50);  
   pinMode(s1, INPUT);
   pinMode(s2, INPUT);
   pinMode(s3, INPUT);
   pinMode(s4, INPUT);
   pinMode(s5, INPUT);
   Serial.begin(9600);

}

void loop() {
  
  vS1 = digitalRead(s1);
  vS2 = digitalRead(s2);
  vS3 = digitalRead(s3);
  vS4 = digitalRead(s4);
  vS5 = digitalRead(s5);

  Serial.print(vS1);
  Serial.print(" ");
  Serial.print(vS3);
  Serial.print(" ");
  Serial.print(vS2);
  Serial.print(" ");
  Serial.print(vS4);
  Serial.print(" ");
  Serial.print(vS5);
  Serial.println(" ");
/*
  motorE.run(BACKWARD);
  motorD.run(FORWARD);

  if(s1 == 1 || s2 == 1 || s3 == 1){
    while(s1 != 1 && s2 != 1 && s3 != 1){
      if (s1 == 1 || s3 == 1){
        if (s1 == 1 && s2 == 0 || s1 == 1 && s3 == 0) {
          motorE.run(BACKWARD);
          motorD.run(FORWARD);
        }
        if (s3 == 1 && s2 == 0 || s3 == 1 && s1 == 0) {
          motorE.run(FORWARD);
          motorD.run(BACKWARD);
        }
      }
      if (s1 == 0 && s2 == 0 && s3 == 0){
          motorE.run(FORWARD);
          motorD.run(FORWARD);
        }
    }}
  Serial.print("Alinhou");


  
  //motorE.run(FORWARD);
  //motorD.run(FORWARD);
  //delay(3000);
  //motorE.run(RELEASE);
  //motorD.run(RELEASE);
  //delay(3000);
  //motorE.run(BACKWARD);
  //motorD.run(BACKWARD);
  //delay(3000);
  */
  
}