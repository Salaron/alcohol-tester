#include <TroykaMQ.h>
 
// имя пина, к которому подключен датчик
#define PIN_MQ3 A1
MQ3 mq3(PIN_MQ3);
 
void setup()
{
  Serial.begin(9600);
  // выполняем калибровку датчика
  mq3.calibrate();
  // выводим сопротивление датчика в чистом воздухе (Ro) в serial-порт
  Serial.print("Ro = ");
  Serial.println(mq3.getRo());
}

void loop()
{
  // выводим отношения текущего сопротивление датчика
  // к сопротивление датчика в чистом воздухе (Rs/Ro)
  Serial.print("Ratio: ");
  Serial.print(mq3.readRatio());
  // выводим значения паров алкоголя
  Serial.print(" Alcohol: ");
  Serial.print(mq3.readAlcoholMgL());
  Serial.print(" mG/L ");
  Serial.print(mq3.readAlcoholPpm());
  Serial.println(" ppm ");
  delay(100);
}