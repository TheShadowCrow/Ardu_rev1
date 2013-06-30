#include "Arduino.h"
#ifndef Ardu_Core_IIC_h
#define Ardu_Core_IIC_h



typedef struct {
	char reg;
	byte data1;
	byte data2;

	boolean isActive;
} reg_send;

typedef struct {
	char reg;
	int data;
} reg_in;


typedef struct {
  char reg;                  // command for execution
  void (*callback)(reg_send);            // callback function 
  boolean isActive   ;               // true if this command is enabled 
} reg_t;

class Ardu_Core_IIC{
	public:
		 
		Ardu_Core_IIC();
		
		void init();
		void onRecieve(int numchars);
		void onRequest();
		void addGetRegister(reg_send reg);
		void addDataRegister(reg_send reg);
		void setData(reg_send data);
		void executeCommand(reg_send inc);
		void setIntToData(char reg, int data);
		static reg_send convertIntToData(char reg, int data);
		static reg_in setDataToInt(reg_send incoming);
		static int convertDataToInt(reg_send incoming);
		
		int bytecount;
		
	private: 
		reg_send registers_get[32];
		reg_send registers_send[32];
		
		
};
#endif