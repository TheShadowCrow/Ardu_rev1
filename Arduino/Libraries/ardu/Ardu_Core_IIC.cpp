#include "Arduino.h"
#include "Wire.h"
#include "Ardu_Core_IIC.h"

Ardu_Core_IIC::Ardu_Core_IIC()
{

}

void Ardu_Core_IIC::init()
{
  for (int i = 0; i < 32; i++) {
    this->registers_get[i].isActive = false;
  }
  
  for (int i = 0; i < 32; i++) {
    this->registers_send[i].isActive = false;
  }
  
  this->bytecount = 0;

}

void Ardu_Core_IIC::onRecieve(int n)
{
  reg_send in[(n/3)];
  int i = 0;
  while(Wire.available())
  {
    in[i].reg = Wire.read();
    in[i].data1 = Wire.read();
    in[i].data2 = Wire.read();
    i++;
  }
}

void Ardu_Core_IIC::onRequest()
{
	byte packet[(this->bytecount * 3)];
	int packetcount =0; 
	for(int i =0; i < (this->bytecount); i++)
	{	
			packet[packetcount]= this->registers_send[i].reg;
			packetcount++;
			packet[packetcount]= this->registers_send[i].data1;
			packetcount++;
			packet[packetcount]= this->registers_send[i].data2;
			packetcount++;		
	} 
	Wire.write(packet, packetcount);
}

void Ardu_Core_IIC::addDataRegister(reg_send reg)
{
	for(int i =0; 1 < 32; i++)
	{
		if(this->registers_send[i].reg != reg.reg && !this->registers_send[i].isActive)
		{
			this->registers_send[i] = reg;
			this->registers_send[i].isActive = true;
			this->bytecount++;
			break;
		}
	}
}

void Ardu_Core_IIC::addGetRegister(reg_send reg)
{
	for(int i =0; 1 < 32; i++)
	{
		if(this->registers_get[i].reg != reg.reg && !this->registers_get[i].isActive)
		{
			this->registers_get[i] = reg;
			this->registers_get[i].isActive = true;
			break;
		}
	}
}


void Ardu_Core_IIC::setData(reg_send data)
{
	for(int i =0; 1 < 32; i++)
	{
		if(this->registers_send[i].reg == data.reg)
		{
			this->registers_send[i] = data;
			break;
		}
	}
}

void Ardu_Core_IIC::executeCommand(reg_send inc)
{
	/* for(int i =0; 1 < 32; i++)
	{
		if(this->registers_get[i].reg == inc.reg)
		{
			this->registers_get[i].callback(inc);
			break;
		}
	} */
}

void Ardu_Core_IIC::setIntToData(char reg, int data)
{
	reg_send data_reg;
	data_reg.reg = reg;
	int data2 = 0 ;
		data_reg.data1 = data;
		data_reg.data2 = (data >> 8); 


	this->setData(data_reg);
}

reg_send Ardu_Core_IIC::convertIntToData(char reg, int data)
{
	reg_send data_reg;
	data_reg.reg = reg;
	int data2 = 0 ;
		data_reg.data1 = data;
		data_reg.data2 = (data >> 8); 
	return data_reg;
}


reg_in Ardu_Core_IIC::setDataToInt(reg_send incoming)
{
	reg_in instruction; 
	instruction.data = incoming.data1 + (incoming.data2 << 8);

	return instruction;
}

int Ardu_Core_IIC::convertDataToInt(reg_send incoming)
{
	int data = 0;
	data = incoming.data1 + (incoming.data2 << 8);


	return data; 
}
