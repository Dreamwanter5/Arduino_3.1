int sensorC = S2;
int sensorLE = S3;
int sensorLD = S1;
int giroscopio = S4;
int motorE = D;
int motorD = A;

bool loop = true;
bool trajeto = true;
bool movimentoFinal = false;
int chave;
bool retorno;
int coordenada[];

void setup() {
  Serial.begin(9600);
  
  // Definindo aparelhos para entrada de informações no Robô
  pinMode(sensorC, INPUT);
  pinMode(sensorLE, INPUT);
  pinMode(sensorLD, INPUT);

  // Definindo aparelhos para saida de comandos no Robô
  pinMode(giroscopio, OUTPUT);
  pinMode(motorE, OUTPUT);
  pinMode(motorD, OUTPUT);
  
  //Começando criação de classes
  class Confirmacao{

  };
}

void loop() {
  // put your main code here, to run repeatedly:

}
