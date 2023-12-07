import minimalmodbus as ModbusRTU

def connect():
    global slave
    try:
        slave = ModbusRTU.Instrument('COM2', 2)    
        slave.serial.baudrate  = 9600
        slave.serial.bytesize  = 8
        slave.serial.parity    = ModbusRTU.serial.PARITY_NONE
        slave.serial.stopbits  = 1 
        slave.serial.timeout = 5000
        slave.debug = False 
        print('Conectado')
    except Exception as erro:
        print(erro)

def read_register():
    try:
        connect()
        tensao = slave.read_register(0, functioncode=4)
        corrente = slave.read_register(1, functioncode=4)
        temp = slave.read_register(2, functioncode=4)
        vibracao = slave.read_register(3, functioncode=4)
        vtank = slave.read_register(4, functioncode=4)
        print('passou')
        print(tensao,corrente,temp,vibracao,vtank)
    except Exception as erro:
        print(erro)
    return (tensao, corrente, temp, vibracao, vtank) 