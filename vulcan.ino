const int TRIGGERPIN = 8;
const int LASERPIN = 9;
const int TRIGGER = 0;
const int LASER = 1;
const int ON = 1;
const int OFF = 0;

const int NUMBER_OF_FIELDS = 3;
int fieldIndex = 0;
int values[NUMBER_OF_FIELDS];

int input;
int startbyte;
int device;

void setup() {
  Serial.begin(9600);
  pinMode(TRIGGERPIN,OUTPUT);
  pinMode(LASERPIN,OUTPUT);
}

void loop() {
    if( Serial.available()){
      char ch = Serial.read();
      if( ch >= '0' && ch <= '9'){
         if(fieldIndex < NUMBER_OF_FIELDS) {
             values[fieldIndex] = (values[fieldIndex] * 10) + (ch - '0');
         }
      }else if(ch == ','){
          fieldIndex++;
      }else{
        /*Serial.println("message complete, printing received values");
        for(int i=0; i< min(NUMBER_OF_FIELDS, fieldIndex+1); i++){
           Serial.println(values[i]);
           //values[i] = 0;
        }
        */
        if( values[0] == 255 ){
          //Serial.println("start sequence initialized");
          /*if( values[1] == TRIGGERPIN ){
            //Serial.println("TRIGGERPIN specified");
            if( values[2] == ON ){
              //Serial.println("pulling trigger");
            }
          }
          */
          digitalWrite(values[1],values[2]);
        }
        for(int i=0; i< min(NUMBER_OF_FIELDS, fieldIndex+1); i++){
          values[i] = 0;
        }
        fieldIndex=0;
      }  
      Serial.flush();    
    }
}
